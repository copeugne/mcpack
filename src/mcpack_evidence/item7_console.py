"""Write ordered lifecycle commands to the Minecraft console."""

from __future__ import annotations

import secrets
from dataclasses import dataclass
from typing import IO, Literal

type FlushProgress = Literal["pending", "complete", "pipe-failed"]


@dataclass(slots=True)
class FlushCorrelation:
    """Track one uniquely bracketed save-all flush response."""

    before_marker: str
    after_marker: str
    phase: Literal["before", "saving", "saved", "after"] = "before"

    def observe(self, line: str, stdin: IO[str], commands: list[str]) -> FlushProgress:
        """Advance the save protocol only after each exact prior response."""
        if self.phase == "before" and line.rstrip().endswith(f"[Server] {self.before_marker}"):
            if send_command(stdin, commands, "save-all flush") is not None:
                return "pipe-failed"
            self.phase = "saving"
        elif self.phase == "saving" and "Saving the game" in line:
            self.phase = "saved"
        elif self.phase == "saved" and "Saved the game" in line:
            if send_command(stdin, commands, f"say {self.after_marker}") is not None:
                return "pipe-failed"
            self.phase = "after"
        elif self.phase == "after" and line.rstrip().endswith(f"[Server] {self.after_marker}"):
            return "complete"
        return "pending"


def send_command(stdin: IO[str], commands: list[str], command: str) -> str | None:
    """Write one command, record it, and report a broken console pipe."""
    try:
        _ = stdin.write(command + "\n")
        stdin.flush()
    except (BrokenPipeError, OSError):
        return "server console pipe failed"
    commands.append(command)
    return None


def begin_correlated_flush(stdin: IO[str], commands: list[str]) -> FlushCorrelation | None:
    """Send the unpredictable marker that must precede one flush request."""
    token = secrets.token_hex(16)
    correlation = FlushCorrelation(
        before_marker=f"mcpack-item7-flush-{token}-before",
        after_marker=f"mcpack-item7-flush-{token}-after",
    )
    if send_command(stdin, commands, f"say {correlation.before_marker}") is not None:
        return None
    return correlation


def advance_correlated_flush(
    correlation: FlushCorrelation, line: str, stdin: IO[str], commands: list[str]
) -> tuple[bool, str | None]:
    """Advance one response-gated flush and stop only after its after marker."""
    progress = correlation.observe(line, stdin, commands)
    if progress == "pipe-failed":
        return False, "server console pipe failed"
    if progress == "complete":
        rejection = send_command(stdin, commands, "stop")
        return rejection is None, rejection
    return False, None
