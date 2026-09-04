from __future__ import annotations

import json
from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal, TypedDict

import pytest
from tools.disposition_item7_warnings import run

from mcpack_evidence.item7_warning_disposition import (
    DownstreamAction,
    DownstreamStatus,
    WarningDispositionError,
    WarningDispositionReport,
    disposition_audit,
)

if TYPE_CHECKING:
    from pathlib import Path


class _EvidencePayload(TypedDict):
    path: str
    line: int
    text: str


class _SignaturePayload(TypedDict):
    signature_id: str
    severity: Literal["WARN", "ERROR"]
    occurrences: int
    first_evidence: _EvidencePayload
    provider_mod_tokens: list[str]
    disposition: Literal["requires_follow_up", "untriaged"]
    consumer_status: Literal["identified", "unresolved", "not_applicable"]


class _AuditPayload(TypedDict):
    schema_version: Literal["item7-warning-audit-v1"]
    input_logs: list[str]
    signatures: list[_SignaturePayload]
    warning_occurrences: int
    error_occurrences: int
    untriaged_signatures: int


@dataclass(frozen=True, slots=True)
class _SignatureOptions:
    severity: Literal["WARN", "ERROR"] = "WARN"
    occurrences: int = 1
    path: str = "run-a/ordinary/minecraft-latest.log"
    text: str = "[time] [thread/WARN] [example/]: ordinary warning"
    disposition: Literal["requires_follow_up", "untriaged"] = "untriaged"
    consumer_status: Literal["identified", "unresolved", "not_applicable"] = "unresolved"


def _signature(
    signature_id: str,
    options: _SignatureOptions | None = None,
) -> _SignaturePayload:
    selected = _SignatureOptions() if options is None else options
    return {
        "signature_id": signature_id,
        "severity": selected.severity,
        "occurrences": selected.occurrences,
        "first_evidence": {"path": selected.path, "line": 1, "text": selected.text},
        "provider_mod_tokens": ["example"],
        "disposition": selected.disposition,
        "consumer_status": selected.consumer_status,
    }


def _audit(signatures: list[_SignaturePayload]) -> _AuditPayload:
    warning_occurrences = sum(
        signature["occurrences"] for signature in signatures if signature["severity"] == "WARN"
    )
    error_occurrences = sum(
        signature["occurrences"] for signature in signatures if signature["severity"] == "ERROR"
    )
    input_logs = sorted({str(signature["first_evidence"]["path"]) for signature in signatures})
    return {
        "schema_version": "item7-warning-audit-v1",
        "input_logs": input_logs,
        "signatures": signatures,
        "warning_occurrences": warning_occurrences,
        "error_occurrences": error_occurrences,
        "untriaged_signatures": sum(
            signature["disposition"] == "untriaged" for signature in signatures
        ),
    }


def test_disposition_preserves_every_member_and_applies_only_evidenced_rules(
    tmp_path: Path,
) -> None:
    # Given: source signatures spanning accepted path classes and concrete findings.
    audit_path = tmp_path / "warning-audit.json"
    signatures = [
        _signature(
            "better-caves-aquifer",
            _SignatureOptions(
                severity="ERROR",
                occurrences=2,
                path="gap-a/ordinary/gap-minecraft-latest.log",
                text=(
                    "[time] [thread/ERROR] [bettercaves/]: Failed to fetch the AquiferContext. "
                    "Liquid Regions for YUNG's Better Caves may not generate properly."
                ),
            ),
        ),
        _signature(
            "level-chunk-block-entity",
            _SignatureOptions(
                occurrences=3,
                path="gap-b/ordinary/gap-minecraft-latest.log",
                text=(
                    "[time] [thread/WARN] [net.minecraft.world.level.chunk.LevelChunk/]: "
                    "Tried to load a block entity for block Block{minecraft:air} but failed"
                ),
            ),
        ),
        _signature(
            "slow-generation",
            _SignatureOptions(
                path="control/ordinary/control-minecraft-latest.log",
                text=(
                    "[time] [thread/WARN] [net.minecraft.server.MinecraftServer/]: Can't keep up! "
                    "Is the server overloaded?"
                ),
            ),
        ),
        _signature(
            "existing-follow-up",
            _SignatureOptions(
                path="run-b/ordinary/minecraft-latest.log",
                disposition="requires_follow_up",
                consumer_status="identified",
            ),
        ),
        _signature("unresolved", _SignatureOptions(path="run-a/ordinary/minecraft-latest.log")),
    ]
    _ = audit_path.write_text(json.dumps(_audit(signatures)), encoding="utf-8")

    # When: the strict audit receives dispositions.
    report = disposition_audit(tmp_path, audit_path)
    rows = {row.signature_id: row for row in report.rows}

    # Then: every source member remains separate, counted, and conservatively classified.
    assert report.signature_count == 5
    assert report.occurrence_count == 8
    assert rows["better-caves-aquifer"].downstream.action is DownstreamAction.GENERATION_FAILURE
    assert rows["better-caves-aquifer"].downstream.status is DownstreamStatus.CONFIRMED
    assert rows["level-chunk-block-entity"].provenance.first_evidence_path_class == "gap-b"
    assert rows["level-chunk-block-entity"].downstream.action is DownstreamAction.GENERATION_FAILURE
    assert rows["slow-generation"].downstream.action is DownstreamAction.PERFORMANCE
    assert rows["slow-generation"].downstream.status is DownstreamStatus.UNKNOWN
    assert rows["existing-follow-up"].downstream.action is DownstreamAction.REQUIRES_FOLLOW_UP
    assert rows["unresolved"].downstream.action is DownstreamAction.UNTRIAGED_UNRESOLVED
    assert rows["unresolved"].downstream.status is DownstreamStatus.UNKNOWN


def test_disposition_rejects_duplicate_members_count_drift_and_unknown_path_class(
    tmp_path: Path,
) -> None:
    # Given: a strict audit with a duplicate member identity.
    duplicate = _signature("same")
    invalid = _audit([duplicate, duplicate])
    invalid["warning_occurrences"] = 2
    audit_path = tmp_path / "warning-audit.json"
    _ = audit_path.write_text(json.dumps(invalid), encoding="utf-8")

    # When and Then: the exact-once accounting boundary fails closed.
    with pytest.raises(WarningDispositionError, match="duplicate warning signature"):
        _ = disposition_audit(tmp_path, audit_path)

    malformed = _audit([_signature("outside", _SignatureOptions(path="pilot/ordinary/latest.log"))])
    _ = audit_path.write_text(json.dumps(malformed), encoding="utf-8")
    with pytest.raises(WarningDispositionError, match="unaccepted Item 7 log path class"):
        _ = disposition_audit(tmp_path, audit_path)


def test_cli_writes_atomically_and_preserves_existing_output_after_strict_parse_failure(
    tmp_path: Path,
) -> None:
    # Given: a valid source audit and a pre-existing output receipt.
    audit_path = tmp_path / "warning-audit.json"
    _ = audit_path.write_text(json.dumps(_audit([_signature("known")])), encoding="utf-8")
    output = tmp_path / "disposition.json"
    _ = output.write_text("sentinel\n", encoding="utf-8")
    arguments = (
        "--root",
        tmp_path.as_posix(),
        "--audit",
        audit_path.as_posix(),
        "--output",
        "disposition.json",
    )

    # When: the command writes its strict evidence output.
    assert run(arguments) == 0
    document = WarningDispositionReport.model_validate_json(output.read_bytes())
    assert document.schema_version == "item7-warning-disposition-v1"

    # Then: an invalid source cannot replace the existing output.
    _ = audit_path.write_text(
        '{"schema_version":"item7-warning-audit-v1","unknown":1}', encoding="utf-8"
    )
    with pytest.raises(WarningDispositionError):
        _ = run(arguments)
    assert WarningDispositionReport.model_validate_json(output.read_bytes()) == document
