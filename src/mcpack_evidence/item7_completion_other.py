"""Cross-surface acceptance checks for Item 7 completion."""

from __future__ import annotations

from pathlib import Path  # noqa: TC003
from typing import ClassVar, Final, Literal

from pydantic import BaseModel, ConfigDict, JsonValue

from mcpack_evidence.item7_archive import ArchiveManifest, RestoreReceipt
from mcpack_evidence.item7_completion_io import fail, identity, sha256_file, strict_model
from mcpack_evidence.item7_completion_models import ArtifactIdentity  # noqa: TC001
from mcpack_evidence.item7_gap import GAP_TARGETS, GapLifecycleReceipt
from mcpack_evidence.item7_runtime import PreflightReceipt  # noqa: TC001
from mcpack_evidence.item7_warning_disposition import WarningDispositionReport
from mcpack_evidence.item7_warning_models import WarningAudit

_WARNING_SIGNATURES: Final = 1222
_WARNING_OCCURRENCES: Final = 14003
_CONTROL_CHUNKS: Final = 81
_ARCHIVE_COUNT: Final = 4


class _Strict(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid", strict=True)


class _ControlReport(_Strict):
    schema_version: Literal["item7-control-comparison-v1"]
    selection: dict[str, JsonValue]
    control: dict[str, JsonValue]
    pilot: dict[str, JsonValue]
    repeat_comparison: dict[str, JsonValue]
    equal: Literal[False]
    field_mismatch_counts: dict[str, int]
    first_mismatch: dict[str, JsonValue]
    disposition: Literal["not_attributable_due_to_measured_stack_nondeterminism"]


class _GapReceipt(_Strict):
    schema_version: Literal["item7-gap-run-v1"]
    preflight: PreflightReceipt
    lifecycle: GapLifecycleReceipt
    configuration: dict[str, JsonValue]
    rejection_reason: None


def validate_warnings(audit_path: Path, disposition_path: Path) -> tuple[ArtifactIdentity, ...]:
    """Account for all warning signatures and occurrences exactly once."""
    audit = strict_model(audit_path, WarningAudit)
    report = strict_model(disposition_path, WarningDispositionReport)
    if (
        report.warning_audit.sha256 != sha256_file(audit_path)
        or len(audit.signatures) != _WARNING_SIGNATURES
        or len(report.rows) != _WARNING_SIGNATURES
        or report.signature_count != _WARNING_SIGNATURES
        or report.occurrence_count != _WARNING_OCCURRENCES
        or audit.warning_occurrences != report.warning_occurrences
        or audit.error_occurrences != report.error_occurrences
        or audit.warning_occurrences + audit.error_occurrences != _WARNING_OCCURRENCES
    ):
        fail("warning total or input identity", disposition_path)
    source = {row.signature_id: (row.severity, row.occurrences) for row in audit.signatures}
    disposed = {row.signature_id: (row.severity, row.occurrences) for row in report.rows}
    row_warnings = sum(row.occurrences for row in report.rows if row.severity == "WARN")
    row_errors = sum(row.occurrences for row in report.rows if row.severity == "ERROR")
    if (
        source != disposed
        or len(disposed) != len(report.rows)
        or row_warnings != report.warning_occurrences
        or row_errors != report.error_occurrences
        or sum(row.occurrences for row in report.rows) != report.occurrence_count
    ):
        fail("warning signature exact-once accounting", disposition_path)
    return (
        identity(audit_path, "warning-audit.json"),
        identity(disposition_path, "warning-disposition.json"),
    )


def validate_control(path: Path, repeat_path: Path) -> ArtifactIdentity:
    """Require a complete 81-chunk control comparison and honest disposition."""
    report = strict_model(path, _ControlReport)
    expected_fields = {
        "schema_version",
        "dimension",
        "slot",
        "chunk_x",
        "chunk_z",
        "data_version",
        "status",
        "full",
        "heightmaps",
        "biome_sections",
        "structure_starts",
    }
    if (
        set(report.field_mismatch_counts) != expected_fields
        or report.selection.get("expected_count") != _CONTROL_CHUNKS
        or report.repeat_comparison.get("sha256") != sha256_file(repeat_path)
        or not report.first_mismatch
    ):
        fail("control comparison accounting", path)
    return identity(path, "control-comparison.json")


def validate_gaps(raw_root: Path) -> tuple[ArtifactIdentity, ...]:
    """Require both fresh targeted runs to reproduce the same four coordinates."""
    receipts: list[tuple[Path, _GapReceipt]] = []
    expected = tuple(target.structure for target in GAP_TARGETS)
    for run_id in ("gap-a", "gap-b"):
        path = raw_root / run_id / "ordinary" / "run-receipt.json"
        receipt = strict_model(path, _GapReceipt)
        lifecycle = receipt.lifecycle
        if (
            receipt.preflight.seed_role != "ordinary"
            or receipt.preflight.seed != "42"
            or tuple(row.structure for row in lifecycle.located_targets) != expected
            or tuple(lifecycle.completed_targets) != expected
            or not all(
                (
                    lifecycle.ready,
                    lifecycle.save_all_flush,
                    lifecycle.clean_stop,
                    lifecycle.return_code == 0,
                    not lifecycle.process_group_killed,
                    lifecycle.rejection_reason is None,
                )
            )
        ):
            fail("targeted gap lifecycle", path)
        receipts.append((path, receipt))
    coordinates = [
        tuple((row.structure, row.x, row.z) for row in receipt.lifecycle.located_targets)
        for _path, receipt in receipts
    ]
    if coordinates[0] != coordinates[1]:
        fail("targeted gap coordinate reproducibility", raw_root)
    return tuple(
        identity(path, f"{path.parts[-3]}/ordinary/run-receipt.json") for path, _ in receipts
    )


def validate_archives(
    manifests: tuple[Path, ...],
    receipts: tuple[Path, ...],
    required: tuple[ArtifactIdentity, ...],
) -> tuple[ArtifactIdentity, ...]:
    """Bind four immutable archive manifests to four verified restore receipts."""
    if len(manifests) != _ARCHIVE_COUNT or len(receipts) != _ARCHIVE_COUNT:
        fail("archive pair count", len(manifests))
    output: list[ArtifactIdentity] = []
    names: set[str] = set()
    archived: dict[str, list[tuple[str, int]]] = {}
    for index, (manifest_path, receipt_path) in enumerate(zip(manifests, receipts, strict=True)):
        manifest = strict_model(manifest_path, ArchiveManifest)
        receipt = strict_model(receipt_path, RestoreReceipt)
        if (
            receipt.archive_name != manifest.archive_name
            or receipt.archive_sha256 != manifest.archive_sha256
            or receipt.manifest_sha256 != sha256_file(manifest_path)
            or receipt.revision != manifest.revision
            or receipt.file_count != manifest.file_count
            or receipt.total_size_bytes != manifest.total_size_bytes
            or manifest.archive_name in names
        ):
            fail("archive restore identity", manifest_path)
        names.add(manifest.archive_name)
        for row in manifest.files:
            archived.setdefault(row.relative_path, []).append((row.sha256, row.size_bytes))
        output.extend(
            (
                identity(manifest_path, f"archive/archive-{index + 1}-manifest.json"),
                identity(receipt_path, f"archive/archive-{index + 1}-restore.json"),
            )
        )
    for artifact in required:
        if archived.get(artifact.path) != [(artifact.sha256, artifact.size_bytes)]:
            fail("archive cross-input identity", artifact.path)
    return tuple(output)
