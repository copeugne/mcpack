"""Capture NeoForge's effective registry keys without changing the mod stack."""

from __future__ import annotations

import queue
import re
import signal
import subprocess
import threading
import time
from dataclasses import dataclass, field
from os import killpg
from typing import IO, TYPE_CHECKING, ClassVar

from pydantic import BaseModel, ConfigDict

from .item7_console import (
    FlushCorrelation,
    advance_correlated_flush,
    begin_correlated_flush,
    send_command,
)
from .item7_output_sequence import OutputSequence, read_output

if TYPE_CHECKING:
    from pathlib import Path

REGISTRIES = (
    "minecraft:worldgen/structure",
    "minecraft:worldgen/structure_set",
    "minecraft:worldgen/template_pool",
    "minecraft:worldgen/configured_feature",
    "minecraft:worldgen/placed_feature",
    "minecraft:worldgen/biome",
    "minecraft:dimension_type",
)
_ID = re.compile(r"[a-z0-9_.-]+:[a-z0-9_./-]+")
_EXIT_TIMEOUT = 120


class RegistryLifecycle(BaseModel):
    """Observed lifecycle result, including rejected attempts."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid", strict=True)
    ready: bool
    completed_registries: tuple[str, ...]
    commands: tuple[str, ...]
    save_all_flush: bool
    clean_stop: bool
    return_code: int
    process_group_killed: bool
    rejection_reason: str | None


@dataclass
class _Capture:
    commands: list[str] = field(default_factory=list)
    completed: list[str] = field(default_factory=list)
    ready: bool = False
    flushed: bool = False
    correlation: FlushCorrelation | None = None
    rejection: str | None = None

    def observe(self, line: str, stdin: IO[str]) -> None:
        if self.correlation is not None and not self.flushed:
            self.flushed, self.rejection = advance_correlated_flush(
                self.correlation, line, stdin, self.commands
            )
        elif not self.ready:
            if "Done (" in line and '! For help, type "help"' in line:
                self.ready = True
                self._next(stdin)
        elif len(self.completed) < len(REGISTRIES):
            registry = REGISTRIES[len(self.completed)]
            if f"New file created with {registry} registry's contents is at " in line:
                self.completed.append(registry)
                self._next(stdin)
            elif "Failed to create new file" in line or "Unknown registry" in line:
                self.rejection = f"registry command failed: {line.strip()}"

    def _next(self, stdin: IO[str]) -> None:
        if len(self.completed) < len(REGISTRIES):
            registry = REGISTRIES[len(self.completed)]
            self.rejection = send_command(
                stdin, self.commands, f"neoforge dump registry {registry} true false"
            )
        else:
            self.correlation = begin_correlated_flush(stdin, self.commands)
            if self.correlation is None:
                self.rejection = "server console pipe failed"


def run_registry_lifecycle(
    target: Path, java: Path, console_log: Path, timeout_seconds: int
) -> RegistryLifecycle:
    """Dump each registry after readiness, then correlate flush and require clean exit."""
    state = _Capture()
    killed = False
    deadline = time.monotonic() + timeout_seconds
    reader: threading.Thread | None = None
    with console_log.open("x", encoding="utf-8") as log:
        process = subprocess.Popen(  # noqa: S603 - pinned executable and fixed server arguments.
            [
                str(java),
                "@user_jvm_args.txt",
                "@libraries/net/neoforged/neoforge/21.1.249/unix_args.txt",
                "nogui",
            ],
            cwd=target,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
            start_new_session=True,
        )
        try:
            if process.stdin is None or process.stdout is None:
                message = "server console pipes are unavailable"
                raise OSError(message)  # noqa: TRY301 - cleanup must cover missing pipes.
            lines = OutputSequence()
            reader = threading.Thread(target=read_output, args=(process.stdout, lines), daemon=True)
            reader.start()
            deadline = _drive(state, lines, process.stdin, log, deadline)
            if state.rejection is None:
                try:
                    _ = process.wait(timeout=max(0.01, deadline - time.monotonic()))
                except subprocess.TimeoutExpired:
                    state.rejection = "server did not exit after console EOF"
        except OSError as error:
            state.rejection = f"registry lifecycle I/O failure: {error}"
        finally:
            if process.poll() is None:
                killpg(process.pid, signal.SIGKILL)
                killed = True
            return_code = process.wait()
            if reader is not None:
                reader.join(timeout=1)
            if process.stdin is not None:
                try:
                    process.stdin.close()
                except OSError:
                    state.rejection = state.rejection or "server console close failed"
            if process.stdout is not None:
                process.stdout.close()
        clean = (
            state.ready
            and tuple(state.completed) == REGISTRIES
            and state.flushed
            and return_code == 0
            and not killed
            and state.rejection is None
        )
        return RegistryLifecycle(
            ready=state.ready,
            completed_registries=tuple(state.completed),
            commands=tuple(state.commands),
            save_all_flush=state.flushed,
            clean_stop=clean,
            return_code=return_code,
            process_group_killed=killed,
            rejection_reason=None if clean else state.rejection or "incomplete registry lifecycle",
        )


def _drive(
    state: _Capture, lines: OutputSequence, stdin: IO[str], log: IO[str], deadline: float
) -> float:
    while state.rejection is None:
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            state.rejection = "registry capture or clean shutdown timed out"
            break
        try:
            line = lines.get(timeout=min(1.0, remaining))
        except queue.Empty:
            continue
        if line is None:
            break
        _ = log.write(line)
        log.flush()
        was_flushed = state.flushed
        state.observe(line, stdin)
        if state.flushed and not was_flushed:
            deadline = time.monotonic() + _EXIT_TIMEOUT
    return deadline


def registry_relative_path(registry: str) -> str:
    """Return NeoForge's fixed dump path for a declared registry."""
    if registry not in REGISTRIES:
        message = f"undeclared registry: {registry}"
        raise ValueError(message)
    namespace, name = registry.split(":")
    return f"dumps/registry/{namespace}/{name.replace('/', '_')}.txt"


def read_registry(path: Path) -> tuple[str, ...]:
    """Reject empty, unsorted, duplicate, or malformed registry dumps."""
    rows = tuple(path.read_text(encoding="utf-8").splitlines())
    if (
        not rows
        or rows != tuple(sorted(set(rows)))
        or any(_ID.fullmatch(row) is None for row in rows)
    ):
        message = f"invalid registry dump: {path}"
        raise ValueError(message)
    return rows
