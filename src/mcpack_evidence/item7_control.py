# ruff: noqa: EM101, TRY003
"""Lifecycle and configuration evidence for the retained Item 7 control."""

from __future__ import annotations

import hashlib
import os
import queue
import shutil
import signal
import subprocess
import threading
import time
from typing import IO, TYPE_CHECKING, ClassVar, Final, Literal, final

from pydantic import BaseModel, ConfigDict, Field, model_validator

from mcpack_evidence.item6_capture import capture
from mcpack_evidence.item7_config import FROZEN_FILE_COUNT, ConfigCaptureReceipt, RuntimeConfigDrift
from mcpack_evidence.item7_console import FlushCorrelation, send_command, send_correlated_flush
from mcpack_evidence.item7_output_sequence import OutputSequence, read_output
from mcpack_evidence.item7_runtime import (
    Item7RuntimeError,
    WorldgenRequest,
    materialized_seed,
    replace_property,
)

if TYPE_CHECKING:
    from pathlib import Path

_SUCCESS: Final = "Marked 81 chunks in Overworld from [-4, -4] to [4, 4] to be force loaded"
# fmt: off
_NORMALIZED: Final = frozenset(("config/bettervillage_1.properties", "config/c2me.toml",
                                "config/libraryferret_1.properties", "server.properties"))
# fmt: on


ControlError = Item7RuntimeError


class ControlRequest(BaseModel):  # noqa: D101
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")
    runtime: WorldgenRequest
    settle_seconds: float = Field(ge=0)

    @model_validator(mode="after")
    def require_ordinary_pilot(self) -> ControlRequest:  # noqa: D102
        if self.runtime.role != "ordinary" or self.runtime.mode != "pilot":
            raise ValueError("control supports the ordinary seed only in pilot mode")
        return self


class ControlLifecycleReceipt(BaseModel):  # noqa: D101
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True)
    schema_version: Literal["item7-control-lifecycle-v1"] = "item7-control-lifecycle-v1"
    ready: bool
    forceload_success: bool
    save_all_flush: bool
    clean_stop: bool
    return_code: int
    commands: tuple[str, ...]
    settle_seconds: float
    log: str
    minecraft_log: str | None
    process_group_killed: bool
    rejection_reason: str | None


@final
class _State:
    def __init__(self) -> None:
        self.commands: list[str] = []
        self.started = time.monotonic()
        self.ready = self.success = self.flushed = self.killed = False
        self.rejection: str | None = None
        self.flush_correlation: FlushCorrelation | None = None


def run_control_lifecycle(  # noqa: D103
    request: ControlRequest, java_executable: Path
) -> ControlLifecycleReceipt:
    run = request.runtime
    environment = os.environ.copy()
    environment["PATH"] = f"{java_executable.parent}:{environment['PATH']}"
    run.log_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        log = run.log_path.open("w", encoding="utf-8")
    except OSError as error:
        raise ControlError("lifecycle", f"runtime log could not be opened: {error}") from error
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
        raise ControlError("lifecycle", f"server launch failed: {error}") from error
    stdin, stdout = _pipes(process, log)
    lines = OutputSequence()
    reader = threading.Thread(target=read_output, args=(stdout, lines), daemon=True)
    reader.start()
    state = _State()
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
    minecraft_log = _capture_log(request, return_code, state)
    clean = return_code == 0 and state.flushed and state.rejection is None
    return ControlLifecycleReceipt(
        ready=state.ready,
        forceload_success=state.success,
        save_all_flush=state.flushed,
        clean_stop=clean,
        return_code=return_code,
        commands=tuple(state.commands),
        settle_seconds=request.settle_seconds,
        log=str(run.log_path),
        minecraft_log=str(minecraft_log) if minecraft_log else None,
        process_group_killed=state.killed,
        rejection_reason=state.rejection,
    )


def _drive(  # noqa: C901
    request: ControlRequest,
    stdin: IO[str],
    lines: OutputSequence,
    log: IO[str],
    state: _State,
) -> None:
    while state.rejection is None:
        remaining = request.runtime.timeout_seconds - (time.monotonic() - state.started)
        if remaining <= 0:
            state.rejection = "control generation timed out"
            return
        try:
            output = lines.get(timeout=min(1.0, remaining))
        except queue.Empty:
            continue
        if output is None:
            if not state.flushed:
                state.rejection = "server exited before control completion"
            return
        _ = log.write(output)
        log.flush()
        line = output
        if not state.ready and "Done (" in line and '! For help, type "help"' in line:
            state.ready = True
            state.rejection = send_command(stdin, state.commands, "forceload add -64 -64 64 64")
        elif state.ready and not state.success and _SUCCESS in line:
            state.success = True
            if request.settle_seconds > remaining:
                state.rejection = "control settling exceeded lifecycle timeout"
                return
            time.sleep(request.settle_seconds)
            state.flush_correlation = send_correlated_flush(stdin, state.commands)
            if state.flush_correlation is None:
                state.rejection = "server console pipe failed"
        elif state.flush_correlation is not None and state.flush_correlation.observe(line):
            state.flushed = True
            state.rejection = send_command(stdin, state.commands, "stop")


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


def _capture_log(request: ControlRequest, return_code: int, state: _State) -> Path | None:
    if return_code != 0 or not state.flushed or state.rejection is not None:
        return None
    destination = request.runtime.log_path.with_name("control-minecraft-latest.log")
    try:
        _ = shutil.copyfile(request.runtime.target / "logs/latest.log", destination)
    except OSError:
        state.rejection = "authoritative Minecraft log capture failed"
        return None
    return destination


def _pipes(process: subprocess.Popen[str], log: IO[str]) -> tuple[IO[str], IO[str]]:
    if process.stdin is not None and process.stdout is not None:
        return process.stdin, process.stdout
    if process.poll() is None:
        os.killpg(process.pid, signal.SIGKILL)
    log.close()
    raise ControlError("lifecycle", "server process pipe was not created")


def capture_control_configuration(  # noqa: D103
    request: ControlRequest,
) -> ConfigCaptureReceipt:
    run = request.runtime
    if any(path.is_file() for path in run.target.glob("config/chunky/**/*")):
        raise ControlError("capture", "Chunky configuration is forbidden in the control")
    try:
        capture(run.target, run.captured_config)
        frozen = _files(run.frozen_config)
        captured = _files(run.captured_config)
        drifts = _compare(run, frozen, captured)
    except ControlError:
        raise
    except (OSError, ValueError) as error:
        raise ControlError("capture", str(error)) from error
    if len(frozen) != FROZEN_FILE_COUNT:
        raise ControlError("capture", "frozen Item 6 inventory is not exactly 228 files")
    return ConfigCaptureReceipt(
        base_file_count=FROZEN_FILE_COUNT, chunky_files=(), normalized_runtime_drifts=drifts
    )


def _compare(
    run: WorldgenRequest, frozen: dict[str, Path], captured: dict[str, Path]
) -> tuple[RuntimeConfigDrift, ...]:
    if set(captured) != set(frozen):
        raise ControlError("capture", "captured inventory differs from frozen Item 6")
    drifts: list[RuntimeConfigDrift] = []
    for relative, source in frozen.items():
        expected = source.read_bytes()
        if relative == "server.properties":
            expected = replace_property(expected, "level-seed", materialized_seed(run))
        observed = captured[relative].read_bytes()
        if observed == expected:
            continue
        if relative not in _NORMALIZED or _semantic(observed) != _semantic(expected):
            raise ControlError("capture", f"captured Item 6 file differs: {relative}")
        drifts.append(
            RuntimeConfigDrift(
                path=relative,
                frozen_sha256=hashlib.sha256(expected).hexdigest(),
                captured_sha256=hashlib.sha256(observed).hexdigest(),
            )
        )
    return tuple(drifts)


def _files(root: Path) -> dict[str, Path]:
    return {
        path.relative_to(root).as_posix(): path
        for path in sorted(root.rglob("*"))
        if path.is_file()
    }


def _semantic(content: bytes) -> tuple[str, ...]:
    return tuple(
        line
        for line in content.decode().splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    )
