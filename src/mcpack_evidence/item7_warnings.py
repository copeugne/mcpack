"""Deterministic, conservative warning extraction for Item 7 runtime logs."""

from __future__ import annotations

import hashlib
import re
from collections import defaultdict
from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from mcpack_evidence.item7_warning_models import (
    ConsumerStatus,
    Disposition,
    EvidenceLine,
    WarningAudit,
    WarningAuditError,
    WarningSignature,
)

if TYPE_CHECKING:
    from pathlib import Path

_ANSI: re.Pattern[str] = re.compile(r"\x1b\[[0-9;]*[A-Za-z]")
_IDENTIFIER_NAMESPACE: re.Pattern[str] = re.compile(r"\b[a-z][a-z0-9_.-]{1,31}:[a-z0-9_./-]+\b")
_ENTRY: re.Pattern[str] = re.compile(
    r"""^\[[^\]]*\d{2}:\d{2}:\d{2}(?:\.\d{3})?]
    [ ]\[[^\]]+/(?P<severity>WARN|ERROR)]
    [ ]\[(?P<logger>[^\]]+)/]:[ ](?P<message>.*)$""",
    re.VERBOSE,
)


@dataclass(frozen=True, slots=True)
class _Rule:
    signature_id: str
    required: tuple[str, ...]
    consumer_status: ConsumerStatus


@dataclass(frozen=True, slots=True)
class _Occurrence:
    severity: Literal["WARN", "ERROR"]
    evidence: EvidenceLine
    signature_id: str
    disposition: Disposition
    consumer_status: ConsumerStatus
    provider_mod_tokens: tuple[str, ...]


_RULES = (
    _Rule(
        "integrated-villages-empty-cabin-pool",
        (
            "integrated api: empty or nonexistent pool:",
            "integrated_villages:cabin_village/villager_random",
        ),
        ConsumerStatus.IDENTIFIED,
    ),
    _Rule(
        "basalt-chambers-missing-pool",
        ("couldn't find template pool reference:", "minecraft:basalt_chambers/chambers"),
        ConsumerStatus.UNRESOLVED,
    ),
    _Rule(
        "c2me-chunk-save-hook",
        ("certain optimizations may be disabled", "chunkdataevent.save", "architectury.event"),
        ConsumerStatus.UNRESOLVED,
    ),
    _Rule(
        "yung-beardifier-unique-method-discard",
        (
            "discarding @unique public method",
            "yungsapi.mixins.json:beardifiermixin",
            "from mod yungsapi",
        ),
        ConsumerStatus.NOT_APPLICABLE,
    ),
    _Rule(
        "moog-beardifier-unique-method-discard",
        (
            "discarding @unique public method",
            "moogs_structures-common.mixins.json",
            "from mod moogs_structures",
        ),
        ConsumerStatus.NOT_APPLICABLE,
    ),
    _Rule(
        "surface-rules-overwrite-conflict",
        (
            "method overwrite conflict",
            "surfacerulescontextaccessor",
            "lithostitched",
            "skipping method",
        ),
        ConsumerStatus.NOT_APPLICABLE,
    ),
)

_TOKEN_MARKERS = (
    ("architectury", "architectury"),
    ("bclib", "bclib"),
    ("c2me", "c2me"),
    ("integrated api", "integrated_api"),
    ("integrated_villages", "integrated_villages"),
    ("lithostitched", "lithostitched"),
    ("moogs_structures", "moogs_structures"),
    ("wover", "wover"),
    ("yungsapi", "yungsapi"),
)


def audit_logs(paths: tuple[Path, ...], *, evidence_root: Path) -> WarningAudit:
    """Parse input logs and return deterministic deduplicated signatures."""
    input_logs: list[str] = []
    occurrences: list[_Occurrence] = []
    for path in sorted(set(paths), key=lambda item: item.as_posix()):
        relative = _relative_path(path, evidence_root)
        raw = _read_log(path)
        parsed = _parse_log(relative, raw)
        occurrences.extend(parsed)
        input_logs.append(relative.as_posix())
    signatures = _group_occurrences(occurrences)
    return WarningAudit(
        schema_version="item7-warning-audit-v1",
        input_logs=tuple(input_logs),
        signatures=signatures,
        warning_occurrences=sum(item.severity == "WARN" for item in occurrences),
        error_occurrences=sum(item.severity == "ERROR" for item in occurrences),
        untriaged_signatures=sum(item.disposition is Disposition.UNTRIAGED for item in signatures),
    )


def _read_log(path: Path) -> bytes:
    if path.is_symlink() or not path.is_file():
        detail = f"cannot read warning log: {path}"
        raise WarningAuditError(detail)
    try:
        return path.read_bytes()
    except OSError as error:
        detail = f"cannot read warning log: {path}"
        raise WarningAuditError(detail) from error


def _relative_path(path: Path, evidence_root: Path) -> Path:
    try:
        return path.resolve().relative_to(evidence_root.resolve())
    except ValueError as error:
        detail = f"warning log escapes evidence root: {path}"
        raise WarningAuditError(detail) from error


def _parse_log(path: Path, raw: bytes) -> tuple[_Occurrence, ...]:
    try:
        lines = raw.decode("utf-8").splitlines()
    except UnicodeDecodeError as error:
        detail = f"warning log is not UTF-8: {path}"
        raise WarningAuditError(detail) from error
    parsed: list[_Occurrence] = []
    for line_number, raw_line in enumerate(lines, start=1):
        line = _ANSI.sub("", raw_line).rstrip()
        match = _ENTRY.fullmatch(line)
        if match is None:
            continue
        severity: Literal["WARN", "ERROR"] = "WARN" if match["severity"] == "WARN" else "ERROR"
        logger = match["logger"].strip()
        message = " ".join(match["message"].split())
        evidence = EvidenceLine(path=path.as_posix(), line=line_number, text=line)
        parsed.append(_classify(severity, logger, message, evidence))
    return tuple(parsed)


def _classify(
    severity: Literal["WARN", "ERROR"],
    logger: str,
    message: str,
    evidence: EvidenceLine,
) -> _Occurrence:
    lowered = f"{logger} {message}".lower()
    rule = next(
        (
            candidate
            for candidate in _RULES
            if severity == "WARN" and all(part in lowered for part in candidate.required)
        ),
        None,
    )
    if rule is None:
        digest = hashlib.sha256(f"{severity}\0{logger}\0{message}".encode()).hexdigest()
        signature_id = f"untriaged-{digest}"
        disposition = Disposition.UNTRIAGED
        consumer_status = ConsumerStatus.UNRESOLVED
    else:
        signature_id = rule.signature_id
        disposition = Disposition.REQUIRES_FOLLOW_UP
        consumer_status = rule.consumer_status
    identifiers = tuple(match.group(0) for match in _IDENTIFIER_NAMESPACE.finditer(lowered))
    namespaces = {identifier.partition(":")[0] for identifier in identifiers}
    provider_ids = tuple(
        sorted(
            {mod_id for marker, mod_id in _TOKEN_MARKERS if marker in lowered}
            | {
                namespace
                for namespace in namespaces
                if "." not in namespace and namespace != "name"
            }
        )
    )
    return _Occurrence(
        severity=severity,
        evidence=evidence,
        signature_id=signature_id,
        disposition=disposition,
        consumer_status=consumer_status,
        provider_mod_tokens=provider_ids,
    )


def _group_occurrences(occurrences: list[_Occurrence]) -> tuple[WarningSignature, ...]:
    grouped: defaultdict[str, list[_Occurrence]] = defaultdict(list)
    for occurrence in occurrences:
        grouped[occurrence.signature_id].append(occurrence)
    signatures: list[WarningSignature] = []
    for signature_id in sorted(grouped):
        items = grouped[signature_id]
        first = items[0]
        signatures.append(
            WarningSignature(
                signature_id=signature_id,
                severity=first.severity,
                occurrences=len(items),
                first_evidence=min(
                    (item.evidence for item in items),
                    key=lambda evidence: (evidence.path, evidence.line),
                ),
                provider_mod_tokens=tuple(
                    sorted({token for item in items for token in item.provider_mod_tokens})
                ),
                disposition=first.disposition,
                consumer_status=first.consumer_status,
            )
        )
    return tuple(signatures)


__all__ = (
    "ConsumerStatus",
    "Disposition",
    "WarningAudit",
    "WarningAuditError",
    "audit_logs",
)
