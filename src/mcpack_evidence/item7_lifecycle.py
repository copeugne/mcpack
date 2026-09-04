"""Drive the bounded Item 7 Chunky process state machine."""

from __future__ import annotations

import os
import queue
import shutil
import signal
import subprocess
import threading
import time
from typing import IO, TYPE_CHECKING, ClassVar, Final, Literal, final

from pydantic import BaseModel, ConfigDict

from mcpack_evidence.item7_console import FlushCorrelation, send_correlated_flush
from mcpack_evidence.item7_output_sequence import OutputSequence, read_output
from mcpack_evidence.item7_runtime import Item7RuntimeError, WorldgenRequest
from mcpack_evidence.item7_selections import WorldgenSelection  # noqa: TC001

if TYPE_CHECKING:
    from pathlib import Path

_READY_MARKER: Final = '! For help, type "help"'
_LIFECYCLE_STAGE: Final = "lifecycle"


class LifecycleReceipt(BaseModel):
    """Observed lifecycle markers, commands, cleanup, and disposition."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True)

    schema_version: Literal["item7-worldgen-lifecycle-v1"] = "item7-worldgen-lifecycle-v1"
    ready: bool
    generation_finished: bool
    save_all_flush: bool
    clean_stop: bool
    return_code: int
    commands: tuple[str, ...]
    selections: tuple[WorldgenSelection, ...]
    completed_selection_labels: tuple[str, ...]
    log: str
    minecraft_log: str | None
    duration_seconds: float
    process_group_killed: bool
    rejection_reason: str | None


@final
class _LifecycleState:
    """Mutable state owned by one synchronous process lifecycle."""

    __slots__ = (
        "commands",
        "completed",
        "flush_correlation",
        "flushed",
        "killed",
        "ready",
        "rejection",
        "request",
        "started",
        "stdin",
    )
    request: WorldgenRequest
    stdin: IO[str]
    started: float
    commands: list[str]
    completed: list[str]
    ready: bool
    flushed: bool
    killed: bool
    rejection: str | None
    flush_correlation: FlushCorrelation | None

    def __init__(self, request: WorldgenRequest, stdin: IO[str]) -> None:
        self.request = request
        self.stdin = stdin
        self.started = time.monotonic()
        self.commands = []
        self.completed = []
        self.ready = False
        self.flushed = False
        self.killed = False
        self.rejection = None
        self.flush_correlation = None


def run_lifecycle(request: WorldgenRequest, java_executable: Path) -> LifecycleReceipt:
    """Generate all four selections, flush, and stop in a new process session."""
    environment = os.environ.copy()
    environment["PATH"] = f"{java_executable.parent}:{environment['PATH']}"
    request.log_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        log = request.log_path.open("w", encoding="utf-8")
    except OSError as error:
        detail = f"runtime log could not be opened: {error}"
        raise Item7RuntimeError(_LIFECYCLE_STAGE, detail) from error
    try:
        process: subprocess.Popen[str] = subprocess.Popen(
            ["./run.sh", "nogui"],
            cwd=request.target,
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
        raise Item7RuntimeError(_LIFECYCLE_STAGE, f"server launch failed: {error}") from error
    stdin, stdout = _process_pipes(process, log)
    state = _LifecycleState(request, stdin)
    lines = OutputSequence()
    reader = threading.Thread(target=read_output, args=(stdout, lines), daemon=True)
    reader.start()
    try:
        try:
            _drive_lifecycle(state, lines, log)
        except OSError:
            state.rejection = "server lifecycle I/O failed"
        return_code = _finish_process(state, process)
    finally:
        try:
            stdin.close()
        except (BrokenPipeError, OSError):
            state.rejection = state.rejection or "server console pipe failed"
        stdout.close()
        log.close()
        reader.join(timeout=1)
    expected_labels = tuple(selection.label for selection in request.selections)
    generation_finished = tuple(state.completed) == expected_labels
    minecraft_log: Path | None = None
    if return_code == 0 and state.ready and generation_finished and state.flushed:
        minecraft_log = request.log_path.with_name("minecraft-latest.log")
        try:
            _ = shutil.copyfile(request.target / "logs/latest.log", minecraft_log)
        except OSError:
            state.rejection = "authoritative Minecraft log capture failed"
            minecraft_log = None
    clean = (
        return_code == 0
        and state.ready
        and generation_finished
        and state.flushed
        and state.rejection is None
    )
    return LifecycleReceipt(
        ready=state.ready,
        generation_finished=generation_finished,
        save_all_flush=state.flushed,
        clean_stop=clean,
        return_code=return_code,
        commands=tuple(state.commands),
        selections=request.selections,
        completed_selection_labels=tuple(state.completed),
        log=str(request.log_path),
        minecraft_log=str(minecraft_log) if minecraft_log is not None else None,
        duration_seconds=round(time.monotonic() - state.started, 3),
        process_group_killed=state.killed,
        rejection_reason=state.rejection,
    )


def _drive_lifecycle(state: _LifecycleState, lines: OutputSequence, log: IO[str]) -> None:
    while state.rejection is None and not state.flushed:
        remaining = state.request.timeout_seconds - (time.monotonic() - state.started)
        if remaining <= 0:
            state.rejection = "world generation timed out"
            return
        try:
            output = lines.get(timeout=min(1.0, remaining))
        except queue.Empty:
            continue
        if output is None:
            state.rejection = "server exited before lifecycle completion"
            return
        _ = log.write(output)
        log.flush()
        _handle_line(state, output)


def _handle_line(state: _LifecycleState, line: str) -> None:
    if not state.ready and "Done (" in line and _READY_MARKER in line:
        state.ready = True
        state.rejection = _send_selection(state, state.request.selections[0])
        return
    if state.ready and len(state.completed) < len(state.request.selections):
        selection = state.request.selections[len(state.completed)]
        marker = (
            f"Task finished for {selection.dimension}. "
            f"Processed: {selection.expected_chunk_count} chunks (100.00%)"
        )
        if marker in line:
            state.completed.append(selection.label)
            if len(state.completed) < len(state.request.selections):
                next_selection = state.request.selections[len(state.completed)]
                state.rejection = _send_selection(state, next_selection)
            else:
                state.flush_correlation = send_correlated_flush(state.stdin, state.commands)
                if state.flush_correlation is None:
                    state.rejection = "server console pipe failed"
            return
    if state.flush_correlation is not None and state.flush_correlation.observe(line):
        state.flushed = True
        if not _send(state, "stop"):
            state.rejection = "server console pipe failed"


def _finish_process(state: _LifecycleState, process: subprocess.Popen[str]) -> int:
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


def _required_pipe(pipe: IO[str] | None) -> IO[str]:
    if pipe is None:
        detail = "server process pipe was not created"
        raise Item7RuntimeError(_LIFECYCLE_STAGE, detail)
    return pipe


def _process_pipes(process: subprocess.Popen[str], log: IO[str]) -> tuple[IO[str], IO[str]]:
    try:
        return _required_pipe(process.stdin), _required_pipe(process.stdout)
    except Item7RuntimeError:
        if process.poll() is None:
            os.killpg(process.pid, signal.SIGKILL)
        log.close()
        raise


def _send(state: _LifecycleState, command: str) -> bool:
    try:
        _ = state.stdin.write(command + "\n")
        state.stdin.flush()
    except (BrokenPipeError, OSError):
        return False
    state.commands.append(command)
    return True


def _send_selection(state: _LifecycleState, selection: WorldgenSelection) -> str | None:
    for command in (
        f"chunky world {selection.dimension}",
        f"chunky center {selection.center_x} {selection.center_z}",
        f"chunky radius {selection.radius_chunks}c",
        "chunky start",
    ):
        if not _send(state, command):
            return "server console pipe failed"
    return None
