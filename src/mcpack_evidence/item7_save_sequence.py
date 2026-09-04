"""Validate source-bound Item 7 flush recovery evidence."""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from typing import TYPE_CHECKING

from pydantic import ValidationError

from mcpack_evidence.item7_archive_models import ArchiveManifest, ArchiveValidationError
from mcpack_evidence.item7_flush_recovery_models import RECOVERY_TARGETS, RecoveryTarget
from mcpack_evidence.item7_runtime import Item7RuntimeError
from mcpack_evidence.item7_save_sequence_receipt import validate_recovery_receipt

if TYPE_CHECKING:
    from pathlib import Path

_SAVING = "Saving the game (this may take a moment!)"
_SAVED = "Saved the game"
_READY = "Done ("
_HELP = '! For help, type "help"'
_STAGE = "lifecycle"


@dataclass(frozen=True, slots=True)
class SaveSequence:
    """One source-bound receipt and its exact archived flush sequence."""

    relative_path: str
    receipt_size_bytes: int
    receipt_sha256: str
    console_size_bytes: int
    console_sha256: str
    minecraft_log_size_bytes: int
    minecraft_log_sha256: str
    source_world_key: str
    source_tree_sha256: str
    ready_line: int
    before_marker_line: int
    saving_line: int
    saved_line: int
    after_marker_line: int


def validate_save_sequences(
    root: Path, manifest_path: Path, inventory_path: Path
) -> tuple[SaveSequence, ...]:
    """Require all 12 receipts, source worlds, logs, and archive identities."""
    records = tuple(_validate(root, target, inventory_path) for target in RECOVERY_TARGETS)
    _validate_manifest(records, manifest_path)
    return records


def build_save_sequence_audit(
    root: Path, manifest_path: Path, inventory_path: Path
) -> dict[str, object]:
    """Build the portable audit bound to core and world archive identities."""
    records = validate_save_sequences(root, manifest_path, inventory_path)
    return {
        "schema_version": "item7-save-sequence-audit-v3",
        "core_manifest": _document_identity(manifest_path),
        "world_inventory": _document_identity(inventory_path),
        "records": [
            {
                "relative_path": record.relative_path,
                "receipt_size_bytes": record.receipt_size_bytes,
                "receipt_sha256": record.receipt_sha256,
                "console_size_bytes": record.console_size_bytes,
                "console_sha256": record.console_sha256,
                "minecraft_log_size_bytes": record.minecraft_log_size_bytes,
                "minecraft_log_sha256": record.minecraft_log_sha256,
                "source_world_key": record.source_world_key,
                "source_tree_sha256": record.source_tree_sha256,
                "ready_line": record.ready_line,
                "before_marker_line": record.before_marker_line,
                "saving_line": record.saving_line,
                "saved_line": record.saved_line,
                "after_marker_line": record.after_marker_line,
            }
            for record in records
        ],
    }


def _document_identity(path: Path) -> dict[str, object]:
    content = path.read_bytes()
    return {
        "path": path.name,
        "size_bytes": len(content),
        "sha256": hashlib.sha256(content).hexdigest(),
    }


def _validate(root: Path, target: RecoveryTarget, inventory_path: Path) -> SaveSequence:
    evidence = validate_recovery_receipt(root, target, inventory_path)
    lifecycle = evidence.receipt.lifecycle
    source = evidence.receipt.source
    if lifecycle is None or source is None:
        raise _sequence_error(target)
    console_path = root / lifecycle.console_log
    minecraft_path = root / lifecycle.minecraft_log
    try:
        console = console_path.read_bytes()
        minecraft = minecraft_path.read_bytes()
        receipt = evidence.path.read_bytes()
        lines = tuple(console.decode("utf-8").splitlines())
    except (OSError, UnicodeDecodeError) as error:
        raise _sequence_error(target) from error
    if (len(console), _digest(console)) != (
        lifecycle.console_log_size_bytes,
        lifecycle.console_log_sha256,
    ) or (len(minecraft), _digest(minecraft)) != (
        lifecycle.minecraft_log_size_bytes,
        lifecycle.minecraft_log_sha256,
    ):
        raise _sequence_error(target)
    before = _unique_marker(lines, f"mcpack-item7-flush-{evidence.token}-before", target)
    after = _unique_marker(lines, f"mcpack-item7-flush-{evidence.token}-after", target)
    ready = _first_ready(lines, target)
    saving = _unique_between(lines, _SAVING, before, after, target)
    saved = _unique_between(lines, _SAVED, saving, after, target)
    if not ready < before < saving < saved < after:
        raise _sequence_error(target)
    return SaveSequence(
        target.evidence_root,
        len(receipt),
        _digest(receipt),
        len(console),
        _digest(console),
        len(minecraft),
        _digest(minecraft),
        source.world_key,
        source.tree_sha256,
        ready,
        before,
        saving,
        saved,
        after,
    )


def _digest(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def _first_ready(lines: tuple[str, ...], target: RecoveryTarget) -> int:
    matches = tuple(
        index for index, line in enumerate(lines, start=1) if _READY in line and _HELP in line
    )
    if not matches:
        raise _sequence_error(target)
    return matches[0]


def _unique_marker(lines: tuple[str, ...], marker: str, target: RecoveryTarget) -> int:
    suffix = f"[Server] {marker}"
    matches = tuple(
        index for index, line in enumerate(lines, start=1) if line.rstrip().endswith(suffix)
    )
    if len(matches) != 1:
        raise _sequence_error(target)
    return matches[0]


def _unique_between(
    lines: tuple[str, ...], marker: str, lower: int, upper: int, target: RecoveryTarget
) -> int:
    matches = tuple(
        index
        for index, line in enumerate(lines, start=1)
        if lower < index < upper and marker in line
    )
    if len(matches) != 1:
        raise _sequence_error(target)
    return matches[0]


def _validate_manifest(records: tuple[SaveSequence, ...], path: Path) -> None:
    try:
        manifest = ArchiveManifest.model_validate_json(path.read_bytes(), strict=True)
    except (OSError, ValidationError, ArchiveValidationError) as error:
        detail = "core archive manifest is invalid"
        raise Item7RuntimeError(_STAGE, detail) from error
    identities = {row.relative_path: row for row in manifest.files}
    for record in records:
        expected = (
            ("run-receipt.json", record.receipt_size_bytes, record.receipt_sha256),
            ("console.log", record.console_size_bytes, record.console_sha256),
            (
                "minecraft-latest.log",
                record.minecraft_log_size_bytes,
                record.minecraft_log_sha256,
            ),
        )
        for name, size, digest in expected:
            archived = identities.get(f"{record.relative_path}/{name}")
            if archived is None or (archived.size_bytes, archived.sha256) != (size, digest):
                detail = (
                    f"flush recovery evidence differs from core manifest: {record.relative_path}"
                )
                raise Item7RuntimeError(_STAGE, detail)


def _sequence_error(target: RecoveryTarget) -> Item7RuntimeError:
    detail = f"save sequence differs: {target.key}"
    return Item7RuntimeError(_STAGE, detail)
