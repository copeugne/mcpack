"""Source-file bindings for Item 7 derived completion evidence."""

from __future__ import annotations

from pathlib import Path  # noqa: TC003
from typing import TYPE_CHECKING, ClassVar, Final, Literal

from pydantic import BaseModel, ConfigDict, Field, JsonValue

from mcpack_evidence.item7_completion_io import (
    CompletionError,
    fail,
    identity,
    portable_path,
    sha256_file,
    strict_model,
)
from mcpack_evidence.item7_warning_disposition import WarningDispositionReport
from mcpack_evidence.item7_warning_models import WarningAudit
from mcpack_evidence.item7_warnings import WarningAuditError, audit_logs

if TYPE_CHECKING:
    from mcpack_evidence.item7_completion_models import ArtifactIdentity

_WARNING_SIGNATURES: Final = 1222
_WARNING_OCCURRENCES: Final = 14003
_CONTROL_CHUNKS: Final = 81


class _Strict(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid", strict=True)


class _SourceIdentity(_Strict):
    path: str
    sha256: str = Field(pattern=r"^[0-9a-f]{64}$")
    size_bytes: int = Field(ge=0)
    record_count: int = Field(ge=0)


class _ControlSide(_Strict):
    run_receipt: _SourceIdentity
    chunks: _SourceIdentity
    normalized_sha256: str = Field(pattern=r"^[0-9a-f]{64}$")
    preflight: dict[str, JsonValue]
    lifecycle: dict[str, JsonValue]


class _ControlReport(_Strict):
    schema_version: Literal["item7-control-comparison-v1"]
    selection: dict[str, JsonValue]
    control: _ControlSide
    pilot: _ControlSide
    repeat_comparison: _SourceIdentity
    equal: Literal[False]
    field_mismatch_counts: dict[str, int]
    first_mismatch: dict[str, JsonValue]
    disposition: Literal["not_attributable_due_to_measured_stack_nondeterminism"]


def _raw_artifact(raw_root: Path, logical_path: str) -> tuple[Path, ArtifactIdentity]:
    relative = portable_path(logical_path)
    path = raw_root / relative
    try:
        _ = path.resolve(strict=True).relative_to(raw_root.resolve(strict=True))
    except (OSError, ValueError) as error:
        issue = "raw input escapes or is absent"
        raise CompletionError(issue, logical_path) from error
    return path, identity(path, relative)


def validate_warnings(
    raw_root: Path, audit_path: Path, disposition_path: Path
) -> tuple[ArtifactIdentity, ...]:
    """Rebuild the warning audit and bind every source log."""
    audit = strict_model(audit_path, WarningAudit)
    report = strict_model(disposition_path, WarningDispositionReport)
    sources = tuple(_raw_artifact(raw_root, path) for path in audit.input_logs)
    try:
        rebuilt = audit_logs(tuple(path for path, _artifact in sources), evidence_root=raw_root)
    except WarningAuditError as error:
        issue = "warning audit source logs"
        raise CompletionError(issue, str(audit_path)) from error
    if rebuilt != audit:
        fail("warning audit source logs", audit_path)
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
        *(artifact for _path, artifact in sources),
    )


def _line_count(path: Path) -> int:
    with path.open("rb") as stream:
        return sum(1 for _line in stream)


def _control_source(
    raw_root: Path, logical_path: str, expected_name: str, declared: _SourceIdentity
) -> ArtifactIdentity:
    path, observed = _raw_artifact(raw_root, logical_path)
    record_count = _line_count(path) if expected_name == "chunks.jsonl" else 1
    if (
        declared.path != expected_name
        or declared.sha256 != observed.sha256
        or declared.size_bytes != observed.size_bytes
        or declared.record_count != record_count
    ):
        fail("control source identity", logical_path)
    return observed


def validate_control(raw_root: Path, path: Path, repeat_path: Path) -> tuple[ArtifactIdentity, ...]:
    """Bind the 81-chunk control result to every source file."""
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
    repeat = identity(repeat_path, "repeat-comparison.json")
    if (
        set(report.field_mismatch_counts) != expected_fields
        or report.selection.get("expected_count") != _CONTROL_CHUNKS
        or report.repeat_comparison.path != repeat.path
        or report.repeat_comparison.sha256 != repeat.sha256
        or report.repeat_comparison.size_bytes != repeat.size_bytes
        or report.repeat_comparison.record_count != 1
        or not report.first_mismatch
    ):
        fail("control comparison accounting", path)
    return (
        identity(path, "control-comparison.json"),
        _control_source(
            raw_root,
            "control/ordinary/run-receipt.json",
            "run-receipt.json",
            report.control.run_receipt,
        ),
        _control_source(
            raw_root,
            "control/ordinary/chunks.jsonl",
            "chunks.jsonl",
            report.control.chunks,
        ),
        _control_source(
            raw_root,
            "pilot/ordinary-success/run-receipt.json",
            "run-receipt.json",
            report.pilot.run_receipt,
        ),
        _control_source(
            raw_root,
            "pilot/ordinary-success/chunks.jsonl",
            "chunks.jsonl",
            report.pilot.chunks,
        ),
    )
