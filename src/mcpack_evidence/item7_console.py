"""Write ordered lifecycle commands to the Minecraft console."""

from __future__ import annotations

import secrets
from dataclasses import dataclass
from typing import IO


@dataclass(slots=True)
class FlushCorrelation:
    """Track one uniquely bracketed save-all flush response."""

    before_marker: str
    after_marker: str
    before_seen: bool = False
    save_started: bool = False
    save_finished: bool = False

    def observe(self, line: str) -> bool:
        """Accept only a complete save sequence between the two unique markers."""
        if not self.before_seen:
            self.before_seen = self.before_marker in line
            return False
        if not self.save_started:
            self.save_started = "Saving the game" in line
            return False
        if not self.save_finished:
            self.save_finished = "Saved the game" in line
            return False
        return self.after_marker in line


def send_command(stdin: IO[str], commands: list[str], command: str) -> str | None:
    """Write one command, record it, and report a broken console pipe."""
    try:
        _ = stdin.write(command + "\n")
        stdin.flush()
    except (BrokenPipeError, OSError):
        return "server console pipe failed"
    commands.append(command)
    return None


def send_correlated_flush(stdin: IO[str], commands: list[str]) -> FlushCorrelation | None:
    """Bracket a flush command with unpredictable server-echoed markers."""
    token = secrets.token_hex(16)
    correlation = FlushCorrelation(
        before_marker=f"mcpack-item7-flush-{token}-before",
        after_marker=f"mcpack-item7-flush-{token}-after",
    )
    for command in (
        f"say {correlation.before_marker}",
        "save-all flush",
        f"say {correlation.after_marker}",
    ):
        if send_command(stdin, commands, command) is not None:
            return None
    return correlation
