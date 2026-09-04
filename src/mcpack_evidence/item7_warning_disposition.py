"""Strict per-signature downstream dispositions for Item 7 warning evidence."""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path, PurePosixPath
from typing import ClassVar, Literal, NoReturn, override

from pydantic import BaseModel, ConfigDict, Field, ValidationError

from mcpack_evidence.item6_json import StrictJsonError, parse_strict_json
from mcpack_evidence.item7_warning_models import (
    ConsumerStatus,
    Disposition,
    EvidenceLine,
    WarningAudit,
    WarningSignature,
)


class PathClass(StrEnum):
    """Accepted Item 7 log path classes."""

    CONTROL = "control"
    RUN_A = "run-a"
    RUN_B = "run-b"
    GAP_A = "gap-a"
    GAP_B = "gap-b"


class DownstreamAction(StrEnum):
    """Required Item 7 follow-on action for one signature."""

    GENERATION_FAILURE = "generation_failure"
    PERFORMANCE = "performance"
    REQUIRES_FOLLOW_UP = "requires_follow_up"
    UNTRIAGED_UNRESOLVED = "untriaged_unresolved"


class DownstreamStatus(StrEnum):
    """Whether the known downstream impact is confirmed or remains unknown."""

    CONFIRMED = "confirmed"
    UNKNOWN = "UNKNOWN"


@dataclass(slots=True)
class WarningDispositionError(Exception):
    """The warning disposition evidence boundary rejected its input or output."""

    detail: str

    @override
    def __str__(self) -> str:
        """Render the evidence-boundary failure."""
        return self.detail


class _StrictModel(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(extra="forbid", frozen=True, strict=True)


class AuditIdentity(_StrictModel):
    """Hash-bound warning-audit input identity."""

    path: str
    sha256: str = Field(pattern=r"^[0-9a-f]{64}$")


class SignatureProvenance(_StrictModel):
    """The accepted path class of the preserved first evidence line only."""

    first_evidence_path_class: PathClass


class SignatureDownstream(_StrictModel):
    """Independent action and certainty for one retained signature."""

    action: DownstreamAction
    status: DownstreamStatus
    rule_id: Literal[
        "source_requires_follow_up",
        "better_caves_aquifer_error",
        "level_chunk_block_entity_anomaly",
        "server_cannot_keep_up",
        "untriaged_source_signature",
    ]


class DispositionRow(_StrictModel):
    """One unmerged input signature with its path-derived and downstream axes."""

    signature_id: str
    severity: Literal["WARN", "ERROR"]
    occurrences: int = Field(gt=0)
    first_evidence: EvidenceLine
    provider_mod_tokens: tuple[str, ...]
    original_disposition: Disposition
    original_consumer_status: ConsumerStatus
    provenance: SignatureProvenance
    downstream: SignatureDownstream


class WarningDispositionReport(_StrictModel):
    """Exact-once Item 7 warning disposition report."""

    schema_version: Literal["item7-warning-disposition-v1"]
    warning_audit: AuditIdentity
    accepted_input_path_classes: tuple[PathClass, ...]
    rows: tuple[DispositionRow, ...]
    signature_count: int = Field(ge=0)
    occurrence_count: int = Field(ge=0)
    warning_occurrences: int = Field(ge=0)
    error_occurrences: int = Field(ge=0)
    source_untriaged_signatures: int = Field(ge=0)
    untriaged_unresolved_signatures: int = Field(ge=0)
    untriaged_unresolved_occurrences: int = Field(ge=0)


_ACCEPTED_CLASSES: tuple[PathClass, ...] = tuple(PathClass)
_MIN_PATH_PARTS = 2


def _fail(detail: str) -> NoReturn:
    raise WarningDispositionError(detail)


def disposition_audit(root: Path, audit_path: Path) -> WarningDispositionReport:
    """Parse one strict audit and emit exactly one row for every source signature."""
    resolved_audit, relative_audit = _resolve_input(root, audit_path)
    audit = _load_audit(resolved_audit)
    _validate_audit(audit)
    rows = tuple(_row(signature) for signature in audit.signatures)
    _validate_rows(audit, rows)
    return WarningDispositionReport(
        schema_version="item7-warning-disposition-v1",
        warning_audit=AuditIdentity(
            path=relative_audit.as_posix(),
            sha256=hashlib.sha256(resolved_audit.read_bytes()).hexdigest(),
        ),
        accepted_input_path_classes=_ACCEPTED_CLASSES,
        rows=rows,
        signature_count=len(rows),
        occurrence_count=sum(row.occurrences for row in rows),
        warning_occurrences=sum(row.occurrences for row in rows if row.severity == "WARN"),
        error_occurrences=sum(row.occurrences for row in rows if row.severity == "ERROR"),
        source_untriaged_signatures=audit.untriaged_signatures,
        untriaged_unresolved_signatures=sum(
            row.downstream.action is DownstreamAction.UNTRIAGED_UNRESOLVED for row in rows
        ),
        untriaged_unresolved_occurrences=sum(
            row.occurrences
            for row in rows
            if row.downstream.action is DownstreamAction.UNTRIAGED_UNRESOLVED
        ),
    )


def _resolve_input(root: Path, audit_path: Path) -> tuple[Path, PurePosixPath]:
    if audit_path.is_symlink() or not audit_path.is_file():
        detail = f"cannot read warning audit: {audit_path}"
        _fail(detail)
    try:
        relative = audit_path.resolve().relative_to(root.resolve())
    except ValueError:
        detail = f"warning audit escapes root: {audit_path}"
        _fail(detail)
    return audit_path.resolve(), PurePosixPath(relative.as_posix())


def _load_audit(path: Path) -> WarningAudit:
    try:
        raw = path.read_bytes()
        _ = parse_strict_json(raw)
        return WarningAudit.model_validate_json(raw, strict=True)
    except (OSError, StrictJsonError, ValidationError):
        detail = f"invalid warning audit: {path}"
        _fail(detail)


def _validate_audit(audit: WarningAudit) -> None:
    input_logs = tuple(_path_class(path) for path in audit.input_logs)
    if len(input_logs) != len(set(audit.input_logs)):
        _fail("duplicate warning audit input path")
    signature_ids = tuple(signature.signature_id for signature in audit.signatures)
    if len(signature_ids) != len(set(signature_ids)):
        _fail("duplicate warning signature")
    if any(signature.occurrences <= 0 for signature in audit.signatures):
        _fail("warning signature has non-positive occurrence count")
    warnings = sum(
        signature.occurrences for signature in audit.signatures if signature.severity == "WARN"
    )
    errors = sum(
        signature.occurrences for signature in audit.signatures if signature.severity == "ERROR"
    )
    if (warnings, errors) != (audit.warning_occurrences, audit.error_occurrences):
        _fail("warning audit occurrence count drift")
    source_untriaged = sum(
        signature.disposition is Disposition.UNTRIAGED for signature in audit.signatures
    )
    if source_untriaged != audit.untriaged_signatures:
        _fail("warning audit untriaged signature count drift")
    if any(signature.first_evidence.path not in audit.input_logs for signature in audit.signatures):
        _fail("warning signature first evidence is absent from input logs")


def _path_class(path: str) -> PathClass:
    candidate = PurePosixPath(path)
    if candidate.is_absolute() or ".." in candidate.parts or len(candidate.parts) < _MIN_PATH_PARTS:
        detail = f"unaccepted Item 7 log path class: {path}"
        _fail(detail)
    try:
        return PathClass(candidate.parts[0])
    except ValueError:
        detail = f"unaccepted Item 7 log path class: {path}"
        _fail(detail)


def _row(signature: WarningSignature) -> DispositionRow:
    text = signature.first_evidence.text.lower()
    match signature.disposition:
        case Disposition.REQUIRES_FOLLOW_UP:
            downstream = SignatureDownstream(
                action=DownstreamAction.REQUIRES_FOLLOW_UP,
                status=DownstreamStatus.UNKNOWN,
                rule_id="source_requires_follow_up",
            )
        case Disposition.UNTRIAGED:
            downstream = _untriaged_downstream(signature, text)
    return DispositionRow(
        signature_id=signature.signature_id,
        severity=signature.severity,
        occurrences=signature.occurrences,
        first_evidence=signature.first_evidence,
        provider_mod_tokens=signature.provider_mod_tokens,
        original_disposition=signature.disposition,
        original_consumer_status=signature.consumer_status,
        provenance=SignatureProvenance(
            first_evidence_path_class=_path_class(signature.first_evidence.path)
        ),
        downstream=downstream,
    )


def _untriaged_downstream(signature: WarningSignature, text: str) -> SignatureDownstream:
    if signature.severity == "ERROR" and "[bettercaves/]" in text and "aquifercontext" in text:
        return SignatureDownstream(
            action=DownstreamAction.GENERATION_FAILURE,
            status=DownstreamStatus.CONFIRMED,
            rule_id="better_caves_aquifer_error",
        )
    if "levelchunk" in text and "block entity" in text:
        return SignatureDownstream(
            action=DownstreamAction.GENERATION_FAILURE,
            status=DownstreamStatus.CONFIRMED,
            rule_id="level_chunk_block_entity_anomaly",
        )
    if "can't keep up! is the server overloaded?" in text:
        return SignatureDownstream(
            action=DownstreamAction.PERFORMANCE,
            status=DownstreamStatus.UNKNOWN,
            rule_id="server_cannot_keep_up",
        )
    return SignatureDownstream(
        action=DownstreamAction.UNTRIAGED_UNRESOLVED,
        status=DownstreamStatus.UNKNOWN,
        rule_id="untriaged_source_signature",
    )


def _validate_rows(audit: WarningAudit, rows: tuple[DispositionRow, ...]) -> None:
    if len(rows) != len(audit.signatures):
        _fail("warning disposition row count drift")
    if sum(row.occurrences for row in rows) != (
        audit.warning_occurrences + audit.error_occurrences
    ):
        _fail("warning disposition occurrence count drift")


__all__ = (
    "DownstreamAction",
    "DownstreamStatus",
    "WarningDispositionError",
    "WarningDispositionReport",
    "disposition_audit",
)
