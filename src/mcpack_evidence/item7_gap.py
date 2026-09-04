# ruff: noqa: D100, D101, D102, D103, EM101

from __future__ import annotations

import os
import queue
import re
import shutil
import signal
import subprocess
import threading
import time
from typing import IO, TYPE_CHECKING, ClassVar, Final, Literal, final

from pydantic import BaseModel, ConfigDict, model_validator

from mcpack_evidence.item7_runtime import Item7RuntimeError, WorldgenRequest

if TYPE_CHECKING:
    from pathlib import Path

_READY: Final = '! For help, type "help"'
_COMPLETE: Final = "Task finished for minecraft:overworld. Processed: 81 chunks (100.00%)"
_LOCATE: Final = re.compile(
    r"The nearest (?P<structure>[a-z0-9_./-]+:[a-z0-9_./-]+) is at \[(?P<x>-?\d+), ~, (?P<z>-?\d+)] \(\d+ blocks away\)"  # noqa: E501
)


GapError = Item7RuntimeError


class GapTarget(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")
    structure: str


GAP_TARGETS: Final = (
    GapTarget(structure="betterdeserttemples:desert_temple"),
    GapTarget(structure="betterstrongholds:stronghold"),
    GapTarget(structure="betterwitchhuts:witch_hut"),
    GapTarget(structure="integrated_stronghold:stronghold"),
)


class LocatedTarget(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True)
    structure: str
    x: int
    z: int


class GapRequest(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")
    runtime: WorldgenRequest

    @model_validator(mode="after")
    def require_ordinary_pilot(self) -> GapRequest:
        if self.runtime.role != "ordinary" or self.runtime.mode != "pilot":
            raise GapError("preflight", "gap targets support the ordinary seed only in pilot mode")
        return self


class GapLifecycleReceipt(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True)
    schema_version: Literal["item7-gap-lifecycle-v1"] = "item7-gap-lifecycle-v1"
    ready: bool
    located_targets: tuple[LocatedTarget, ...]
    completed_targets: tuple[str, ...]
    save_all_flush: bool
    clean_stop: bool
    return_code: int
    commands: tuple[str, ...]
    log: str
    minecraft_log: str | None
    process_group_killed: bool
    rejection_reason: str | None


@final
class _State:
    __slots__ = tuple("commands completed flushed killed located ready rejection started".split())  # noqa: SIM905

    def __init__(self) -> None:
        self.commands: list[str] = []
        self.completed: list[str] = []
        self.located: list[LocatedTarget] = []
        self.ready = self.flushed = self.killed = False
        self.rejection: str | None = None
        self.started = time.monotonic()


def parse_locate_line(line: str, target: GapTarget) -> LocatedTarget:
    match = _LOCATE.search(line)
    if match is None:
        raise GapError("lifecycle", "located coordinate marker differs")
    structure = match.group("structure")
    if structure != target.structure:
        raise GapError("lifecycle", "located structure differs from requested target")
    return LocatedTarget(structure=structure, x=int(match.group("x")), z=int(match.group("z")))


def parse_completion_marker(line: str, target: GapTarget) -> str:
    if _COMPLETE not in line:
        raise GapError("lifecycle", "completion marker differs from requested target")
    return target.structure


def run_gap_lifecycle(request: GapRequest, java_executable: Path) -> GapLifecycleReceipt:
    run = request.runtime
    run.log_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        log = run.log_path.open("w", encoding="utf-8")
    except OSError as error:
        raise GapError("lifecycle", f"runtime log could not be opened: {error}") from error
    environment = os.environ.copy()
    environment["PATH"] = f"{java_executable.parent}:{environment['PATH']}"
    try:
        process: subprocess.Popen[str] = subprocess.Popen(
            ["./run.sh", "nogui"],
            cwd=run.target,
            env=environment,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
            start_new_session=True,
        )
    except OSError as error:
        log.close()
        raise GapError("lifecycle", f"server launch failed: {error}") from error
    stdin, stdout = _pipes(process, log)
    state = _State()
    lines: queue.Queue[str | None] = queue.Queue()
    reader = threading.Thread(target=_read, args=(stdout, lines), daemon=True)
    reader.start()
    try:
        _drive(request, stdin, lines, log, state)
    except OSError:
        state.rejection = "server lifecycle I/O failed"
    return_code = _finish(process, state)
    try:
        stdin.close()
    except (BrokenPipeError, OSError):
        state.rejection = state.rejection or "server console pipe failed"
    stdout.close()
    log.close()
    reader.join(timeout=1)
    minecraft_log = _capture_log(request, state)
    clean = return_code == 0 and state.flushed and state.rejection is None
    return GapLifecycleReceipt(
        ready=state.ready,
        located_targets=tuple(state.located),
        completed_targets=tuple(state.completed),
        save_all_flush=state.flushed,
        clean_stop=clean,
        return_code=return_code,
        commands=tuple(state.commands),
        log=str(run.log_path),
        minecraft_log=str(minecraft_log) if minecraft_log is not None else None,
        process_group_killed=state.killed,
        rejection_reason=state.rejection,
    )


def _drive(
    request: GapRequest, stdin: IO[str], lines: queue.Queue[str | None], log: IO[str], state: _State
) -> None:
    while state.rejection is None and not state.flushed:
        remaining = request.runtime.timeout_seconds - (time.monotonic() - state.started)
        if remaining <= 0:
            state.rejection = "gap target lifecycle timed out"
            return
        try:
            line = lines.get(timeout=min(1.0, remaining))
        except queue.Empty:
            continue
        if line is None:
            state.rejection = "server exited before gap target completion"
            return
        _ = log.write(line)
        log.flush()
        _observe(stdin, line, state)


def _observe(stdin: IO[str], line: str, state: _State) -> None:
    if not state.ready and "Done (" in line and _READY in line:
        state.ready = True
        state.rejection = _send(stdin, state.commands, _locate_command(GAP_TARGETS[0]))
        return
    if state.ready and len(state.located) < len(GAP_TARGETS) and "The nearest " in line:
        target = GAP_TARGETS[len(state.located)]
        try:
            state.located.append(parse_locate_line(line, target))
        except GapError as error:
            state.rejection = error.detail
            return
        if len(state.located) < len(GAP_TARGETS):
            state.rejection = _send(
                stdin, state.commands, _locate_command(GAP_TARGETS[len(state.located)])
            )
        else:
            state.rejection = _send_chunky(stdin, state.commands, state.located[0])
        return
    if (
        len(state.located) == len(GAP_TARGETS)
        and len(state.completed) < len(GAP_TARGETS)
        and "Task finished" in line
    ):
        target = GAP_TARGETS[len(state.completed)]
        try:
            state.completed.append(parse_completion_marker(line, target))
        except GapError as error:
            state.rejection = error.detail
            return
        if len(state.completed) < len(GAP_TARGETS):
            state.rejection = _send_chunky(
                stdin, state.commands, state.located[len(state.completed)]
            )
        else:
            state.rejection = _send(stdin, state.commands, "save-all flush")
        return
    if len(state.completed) == len(GAP_TARGETS) and "Saved the game" in line:
        state.flushed = True
        state.rejection = _send(stdin, state.commands, "stop")


def _locate_command(target: GapTarget) -> str:
    return f"locate structure {target.structure}"


def _send_chunky(stdin: IO[str], commands: list[str], target: LocatedTarget) -> str | None:
    for command in (
        "chunky world minecraft:overworld",
        f"chunky center {target.x} {target.z}",
        "chunky radius 4c",
        "chunky start",
    ):
        rejection = _send(stdin, commands, command)
        if rejection is not None:
            return rejection
    return None


def _send(stdin: IO[str], commands: list[str], command: str) -> str | None:
    try:
        _ = stdin.write(command + "\n")
        stdin.flush()
    except (BrokenPipeError, OSError):
        return "server console pipe failed"
    commands.append(command)
    return None


def _read(stdout: IO[str], lines: queue.Queue[str | None]) -> None:
    for line in iter(stdout.readline, ""):
        lines.put(line)
    lines.put(None)


def _pipes(process: subprocess.Popen[str], log: IO[str]) -> tuple[IO[str], IO[str]]:
    if process.stdin is not None and process.stdout is not None:
        return process.stdin, process.stdout
    if process.poll() is None:
        os.killpg(process.pid, signal.SIGKILL)
    log.close()
    raise GapError("lifecycle", "server process pipe was not created")


def _finish(process: subprocess.Popen[str], state: _State) -> int:
    if state.rejection is not None and process.poll() is None:
        os.killpg(process.pid, signal.SIGKILL)
        state.killed = True
    try:
        return process.wait(timeout=30)
    except (OSError, subprocess.TimeoutExpired):
        if process.poll() is None:
            os.killpg(process.pid, signal.SIGKILL)
            state.killed = True
        state.rejection = "server lifecycle I/O failed"
        return process.wait()


def _capture_log(request: GapRequest, state: _State) -> Path | None:
    destination = request.runtime.log_path.with_name("gap-minecraft-latest.log")
    try:
        _ = shutil.copyfile(request.runtime.target / "logs/latest.log", destination)
    except OSError:
        if state.rejection is None:
            state.rejection = "authoritative Minecraft log capture failed"
        return None
    return destination
