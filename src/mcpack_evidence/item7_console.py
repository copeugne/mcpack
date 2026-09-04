"""Write ordered lifecycle commands to the Minecraft console."""

from __future__ import annotations

from typing import IO


def send_command(stdin: IO[str], commands: list[str], command: str) -> str | None:
    """Write one command, record it, and report a broken console pipe."""
    try:
        _ = stdin.write(command + "\n")
        stdin.flush()
    except (BrokenPipeError, OSError):
        return "server console pipe failed"
    commands.append(command)
    return None
