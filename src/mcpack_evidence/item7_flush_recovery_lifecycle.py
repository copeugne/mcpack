"""Execute one response-gated Item 7 recovery server lifecycle."""

from __future__ import annotations

import os
import queue
import shutil
import signal
import subprocess
import threading
import time
from typing import IO, TYPE_CHECKING, Protocol, final

from mcpack_evidence.item7_console import (
    FlushCorrelation,
    advance_correlated_flush,
    begin_correlated_flush,
)
from mcpack_evidence.item7_flush_recovery_models import RecoveryLifecycle, recovery_target
from mcpack_evidence.item7_output_sequence import OutputSequence, read_output
from mcpack_evidence.item7_runtime import Item7RuntimeError, WorldgenRequest, sha256_file

if TYPE_CHECKING:
    from pathlib import Path


class RecoveryLifecycleRequest(Protocol):
    """Inputs used by the recovery lifecycle without coupling its model."""

    runtime: WorldgenRequest
    world_key: str
    console_log: Path


@final
class _State:
    def __init__(self) -> None:
        self.started = time.monotonic()
        self.commands: list[str] = []
        self.ready = self.flushed = self.killed = False
        self.correlation: FlushCorrelation | None = None
        self.rejection: str | None = None


def run_recovery_lifecycle(request: RecoveryLifecycleRequest, java: Path) -> RecoveryLifecycle:
    """Boot, correlate one flush, stop, and retain both server logs."""
    request.console_log.parent.mkdir(parents=True, exist_ok=True)
    with request.console_log.open("w", encoding="utf-8") as log:
        process = _launch(request, java)
        stdin, stdout = _pipes(process)
        state = _State()
        lines = OutputSequence()
        reader = threading.Thread(target=read_output, args=(stdout, lines), daemon=True)
        reader.start()
        try:
            _drive(request, state, stdin, lines, log)
        except OSError:
            state.rejection = "server lifecycle I/O failed"
        return_code = _finish(process, state)
        try:
            stdin.close()
        except (BrokenPipeError, OSError):
            state.rejection = state.rejection or "server console pipe failed"
        stdout.close()
        reader.join(timeout=1)
    minecraft_log = request.console_log.with_name("minecraft-latest.log")
    try:
        _ = shutil.copyfile(request.runtime.target / "logs/latest.log", minecraft_log)
    except OSError:
        state.rejection = state.rejection or "authoritative Minecraft log capture failed"
    clean = return_code == 0 and state.ready and state.flushed and state.rejection is None
    root = recovery_target(request.world_key).evidence_root
    return RecoveryLifecycle(
        ready=state.ready,
        save_all_flush=state.flushed,
        clean_stop=clean,
        return_code=return_code,
        commands=tuple(state.commands),
        console_log=f"{root}/console.log",
        console_log_size_bytes=request.console_log.stat().st_size,
        console_log_sha256=sha256_file(request.console_log),
        minecraft_log=f"{root}/minecraft-latest.log",
        minecraft_log_size_bytes=minecraft_log.stat().st_size if minecraft_log.is_file() else 0,
        minecraft_log_sha256=sha256_file(minecraft_log) if minecraft_log.is_file() else "0" * 64,
        duration_seconds=round(time.monotonic() - state.started, 3),
        process_group_killed=state.killed,
        rejection_reason=state.rejection,
    )


def _launch(request: RecoveryLifecycleRequest, java: Path) -> subprocess.Popen[str]:
    environment = os.environ.copy()
    environment["PATH"] = f"{java.parent}:{environment['PATH']}"
    try:
        return subprocess.Popen(
            ["./run.sh", "nogui"],
            cwd=request.runtime.target,
            env=environment,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
            start_new_session=True,
        )
    except OSError as error:
        stage = "lifecycle"
        detail = f"server launch failed: {error}"
        raise Item7RuntimeError(stage, detail) from error


def _drive(
    request: RecoveryLifecycleRequest,
    state: _State,
    stdin: IO[str],
    lines: OutputSequence,
    log: IO[str],
) -> None:
    while state.rejection is None and not state.flushed:
        remaining = request.runtime.timeout_seconds - (time.monotonic() - state.started)
        if remaining <= 0:
            state.rejection = "flush recovery timed out"
            return
        try:
            line = lines.get(timeout=min(1.0, remaining))
        except queue.Empty:
            continue
        if line is None:
            state.rejection = "server exited before flush recovery completed"
            return
        _ = log.write(line)
        log.flush()
        if not state.ready and "Done (" in line and '! For help, type "help"' in line:
            state.ready = True
            state.correlation = begin_correlated_flush(stdin, state.commands)
            if state.correlation is None:
                state.rejection = "server console pipe failed"
        elif state.correlation is not None:
            flushed, state.rejection = advance_correlated_flush(
                state.correlation, line, stdin, state.commands
            )
            state.flushed = state.flushed or flushed


def _pipes(process: subprocess.Popen[str]) -> tuple[IO[str], IO[str]]:
    if process.stdin is not None and process.stdout is not None:
        return process.stdin, process.stdout
    if process.poll() is None:
        os.killpg(process.pid, signal.SIGKILL)
    stage = "lifecycle"
    detail = "server process pipe was not created"
    raise Item7RuntimeError(stage, detail)


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
