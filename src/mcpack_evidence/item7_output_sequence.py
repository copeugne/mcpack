"""Sequence console output around lifecycle command checkpoints."""

from __future__ import annotations

import queue
import threading
from dataclasses import dataclass
from typing import IO, TYPE_CHECKING, final

if TYPE_CHECKING:
    from collections.abc import Callable


@dataclass(frozen=True, slots=True)
class OutputLine:
    """One console line with its reader-assigned sequence number."""

    sequence: int
    text: str


@final
class OutputSequence:
    """Serialize reader publication and command checkpoints with one lock."""

    __slots__ = ("_lines", "_lock", "_sequence")

    def __init__(self) -> None:
        """Create an empty synchronized output sequence."""
        self._lines: queue.Queue[OutputLine | None] = queue.Queue()
        self._lock = threading.Lock()
        self._sequence = 0

    def checkpoint_and_send(self, send: Callable[[], bool]) -> int | None:
        """Send a command and return the sequence boundary it must follow."""
        with self._lock:
            checkpoint = self._sequence
            if not send():
                return None
            return checkpoint

    def get(self, timeout: float) -> OutputLine | None:
        """Return the next reader-published output line."""
        return self._lines.get(timeout=timeout)

    def publish(self, text: str) -> None:
        """Add a console line after assigning its monotonic sequence number."""
        with self._lock:
            self._sequence += 1
            self._lines.put(OutputLine(sequence=self._sequence, text=text))

    def finish(self) -> None:
        """Mark the end of console output."""
        self._lines.put(None)


def read_output(stdout: IO[str], output: OutputSequence) -> None:
    """Publish every stdout line in order before marking output complete."""
    for line in iter(stdout.readline, ""):
        output.publish(line)
    output.finish()
