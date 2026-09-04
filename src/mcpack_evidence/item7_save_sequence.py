"""Validate Item 7 console save ordering after accepted lifecycle work."""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from typing import TYPE_CHECKING, Final

from pydantic import JsonValue, ValidationError

from mcpack_evidence.item7_archive_models import ArchiveManifest, ArchiveValidationError
from mcpack_evidence.item7_runtime import Item7RuntimeError

if TYPE_CHECKING:
    from pathlib import Path

_SAVING: Final = "Saving the game (this may take a moment!)"
_SAVED: Final = "Saved the game"
_BEFORE: Final = re.compile(r"mcpack-item7-flush-(?P<token>[0-9a-f]{32})-before")
_AFTER: Final = re.compile(r"mcpack-item7-flush-(?P<token>[0-9a-f]{32})-after")
_LIFECYCLE_STAGE: Final = "lifecycle"
SAVE_SEQUENCE_TARGETS: Final = (
    ("control/ordinary", "Marked 81 chunks in Overworld"),
    ("gap-a/ordinary", "Task finished for"),
    ("gap-b/ordinary", "Task finished for"),
    ("pilot/ordinary-success", "Task finished for"),
    *(
        (f"run-{run}/{seed}", "Task finished for")
        for run in ("a", "b")
        for seed in ("ordinary", "mountainous", "ocean-heavy", "biome-diverse")
    ),
)


@dataclass(frozen=True, slots=True)
class SaveSequence:
    """One accepted lifecycle's final work and save-marker line numbers."""

    relative_path: str
    size_bytes: int
    sha256: str
    work_line: int
    before_marker_line: int
    saving_line: int
    saved_line: int
    after_marker_line: int


def validate_save_sequences(
    root: Path, manifest_path: Path | None = None
) -> tuple[SaveSequence, ...]:
    """Return the final work, save-start, and save-finish ordering for all accepted logs."""
    records = tuple(
        _validate(root / relative / "console.log", relative, marker)
        for relative, marker in SAVE_SEQUENCE_TARGETS
    )
    if manifest_path is not None:
        _validate_manifest(records, manifest_path)
    return records


def build_save_sequence_audit(root: Path, manifest_path: Path) -> dict[str, JsonValue]:
    """Build the portable machine-readable audit bound to the core archive manifest."""
    records = validate_save_sequences(root, manifest_path)
    return {
        "schema_version": "item7-save-sequence-audit-v2",
        "core_manifest": {
            "path": manifest_path.name,
            "size_bytes": manifest_path.stat().st_size,
            "sha256": hashlib.sha256(manifest_path.read_bytes()).hexdigest(),
        },
        "records": [
            {
                "relative_path": record.relative_path,
                "size_bytes": record.size_bytes,
                "sha256": record.sha256,
                "work_line": record.work_line,
                "before_marker_line": record.before_marker_line,
                "saving_line": record.saving_line,
                "saved_line": record.saved_line,
                "after_marker_line": record.after_marker_line,
            }
            for record in records
        ],
    }


def _validate(path: Path, relative: str, work_marker: str) -> SaveSequence:
    try:
        content = path.read_bytes()
        lines = tuple(content.decode("utf-8").splitlines())
    except (OSError, UnicodeDecodeError) as error:
        detail = f"console log could not be read: {relative}"
        raise Item7RuntimeError(_LIFECYCLE_STAGE, detail) from error
    work_line = _last_line(lines, work_marker, relative)
    before_line, token = _last_token_line(lines, _BEFORE, relative)
    saving_line = _last_line(lines, _SAVING, relative)
    saved_line = _last_line(lines, _SAVED, relative)
    after_line, after_token = _last_token_line(lines, _AFTER, relative)
    if token != after_token or not work_line < before_line < saving_line < saved_line < after_line:
        raise Item7RuntimeError(_LIFECYCLE_STAGE, f"save sequence differs: {relative}")
    return SaveSequence(
        relative,
        len(content),
        hashlib.sha256(content).hexdigest(),
        work_line,
        before_line,
        saving_line,
        saved_line,
        after_line,
    )


def _last_line(lines: tuple[str, ...], marker: str, relative: str) -> int:
    matches = tuple(index for index, line in enumerate(lines, start=1) if marker in line)
    if not matches:
        raise Item7RuntimeError(_LIFECYCLE_STAGE, f"save marker missing: {relative}: {marker}")
    return matches[-1]


def _last_token_line(
    lines: tuple[str, ...], pattern: re.Pattern[str], relative: str
) -> tuple[int, str]:
    matches = tuple(
        (index, match.group("token"))
        for index, line in enumerate(lines, start=1)
        if (match := pattern.search(line)) is not None
    )
    if not matches:
        raise Item7RuntimeError(_LIFECYCLE_STAGE, f"save marker missing: {relative}")
    return matches[-1]


def _validate_manifest(records: tuple[SaveSequence, ...], path: Path) -> None:
    try:
        manifest = ArchiveManifest.model_validate_json(path.read_bytes(), strict=True)
    except (OSError, ValidationError, ArchiveValidationError) as error:
        raise Item7RuntimeError(_LIFECYCLE_STAGE, "core archive manifest is invalid") from error
    identities = {row.relative_path: row for row in manifest.files}
    for record in records:
        archived = identities.get(f"{record.relative_path}/console.log")
        if archived is None or (archived.size_bytes, archived.sha256) != (
            record.size_bytes,
            record.sha256,
        ):
            raise Item7RuntimeError(
                _LIFECYCLE_STAGE, f"console log differs from core manifest: {record.relative_path}"
            )
