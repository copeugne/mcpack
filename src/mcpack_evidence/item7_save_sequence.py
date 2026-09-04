"""Validate Item 7 console save ordering after accepted lifecycle work."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Final

from mcpack_evidence.item7_runtime import Item7RuntimeError

if TYPE_CHECKING:
    from pathlib import Path

_SAVING: Final = "Saving the game (this may take a moment!)"
_SAVED: Final = "Saved the game"
_LIFECYCLE_STAGE: Final = "lifecycle"
SAVE_SEQUENCE_TARGETS: Final = (
    ("control/ordinary", "Marked 81 chunks in Overworld"),
    ("gap-a/ordinary", "Task finished for"),
    ("gap-b/ordinary", "Task finished for"),
    ("pilot/ordinary-success", "Task finished for"),
    *((f"run-{run}/{seed}", "Task finished for") for run in ("a", "b") for seed in (
        "ordinary", "mountainous", "ocean-heavy", "biome-diverse"
    )),
)


@dataclass(frozen=True, slots=True)
class SaveSequence:
    """One accepted lifecycle's final work and save-marker line numbers."""

    relative_path: str
    work_line: int
    saving_line: int
    saved_line: int


def validate_save_sequences(root: Path) -> tuple[SaveSequence, ...]:
    """Return the final work, save-start, and save-finish ordering for all accepted logs."""
    return tuple(
        _validate(root / relative / "console.log", relative, marker)
        for relative, marker in SAVE_SEQUENCE_TARGETS
    )


def _validate(path: Path, relative: str, work_marker: str) -> SaveSequence:
    try:
        lines = tuple(path.read_text(encoding="utf-8").splitlines())
    except OSError as error:
        detail = f"console log could not be read: {relative}"
        raise Item7RuntimeError(_LIFECYCLE_STAGE, detail) from error
    work_line = _last_line(lines, work_marker, relative)
    saving_line = _last_line(lines, _SAVING, relative)
    saved_line = _last_line(lines, _SAVED, relative)
    if not work_line < saving_line < saved_line:
        raise Item7RuntimeError(_LIFECYCLE_STAGE, f"save sequence differs: {relative}")
    return SaveSequence(relative, work_line, saving_line, saved_line)


def _last_line(lines: tuple[str, ...], marker: str, relative: str) -> int:
    matches = tuple(index for index, line in enumerate(lines, start=1) if marker in line)
    if not matches:
        raise Item7RuntimeError(_LIFECYCLE_STAGE, f"save marker missing: {relative}: {marker}")
    return matches[-1]
