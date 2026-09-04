"""Transfer lifecycle console output from the reader thread."""

from __future__ import annotations

import queue
from typing import IO, final


@final
class OutputSequence:
    """Transfer complete console lines from the reader to the lifecycle."""

    __slots__ = ("_lines",)

    def __init__(self) -> None:
        """Create an empty synchronized output sequence."""
        self._lines: queue.Queue[str | None] = queue.Queue()

    def get(self, timeout: float) -> str | None:
        """Return the next reader-published output line."""
        return self._lines.get(timeout=timeout)

    def publish(self, text: str) -> None:
        """Add one complete console line."""
        self._lines.put(text)

    def finish(self) -> None:
        """Mark the end of console output."""
        self._lines.put(None)


def read_output(stdout: IO[str], output: OutputSequence) -> None:
    """Publish every stdout line in order before marking output complete."""
    for line in iter(stdout.readline, ""):
        output.publish(line)
    output.finish()
