from __future__ import annotations

import hashlib
import json
from typing import TYPE_CHECKING

import pytest

import mcpack_evidence.item7_completion_sources as completion_sources
from mcpack_evidence.item7_completion_io import CompletionError
from mcpack_evidence.item7_warning_disposition import disposition_audit
from mcpack_evidence.item7_warnings import audit_logs

if TYPE_CHECKING:
    from pathlib import Path


def _file_identity(path: Path, records: int) -> dict[str, str | int]:
    return {
        "path": path.name,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "size_bytes": path.stat().st_size,
        "record_count": records,
    }


def test_warning_completion_rebuilds_and_binds_every_source_log(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    raw = tmp_path / "raw"
    log = raw / "run-a/ordinary/minecraft-latest.log"
    log.parent.mkdir(parents=True)
    _ = log.write_text(
        "[04Sep2026 07:10:40.829] [main/WARN] [example/]: Unrecognized warning\n",
        encoding="utf-8",
    )
    audit_path = raw / "warning-audit.json"
    audit = audit_logs((log,), evidence_root=raw)
    _ = audit_path.write_text(audit.model_dump_json(indent=2) + "\n", encoding="utf-8")
    disposition_path = raw / "warning-disposition.json"
    disposition = disposition_audit(raw, audit_path)
    _ = disposition_path.write_text(disposition.model_dump_json(indent=2) + "\n", encoding="utf-8")
    monkeypatch.setattr(completion_sources, "_WARNING_SIGNATURES", 1)
    monkeypatch.setattr(completion_sources, "_WARNING_OCCURRENCES", 1)

    artifacts = completion_sources.validate_warnings(raw, audit_path, disposition_path)

    assert tuple(row.path for row in artifacts) == (
        "warning-audit.json",
        "warning-disposition.json",
        "run-a/ordinary/minecraft-latest.log",
    )
    _ = log.write_text("changed\n", encoding="utf-8")
    with pytest.raises(CompletionError, match="warning audit source logs"):
        _ = completion_sources.validate_warnings(raw, audit_path, disposition_path)


def test_control_completion_binds_all_embedded_source_identities(tmp_path: Path) -> None:
    raw = tmp_path / "raw"
    control = raw / "control/ordinary"
    pilot = raw / "pilot/ordinary-success"
    control.mkdir(parents=True)
    pilot.mkdir(parents=True)
    for root, marker in ((control, "control"), (pilot, "pilot")):
        _ = (root / "run-receipt.json").write_text("{}\n", encoding="utf-8")
        _ = (root / "chunks.jsonl").write_text(
            f'{{"source":"{marker}-1"}}\n{{"source":"{marker}-2"}}\n',
            encoding="utf-8",
        )
    repeat = raw / "repeat-comparison.json"
    _ = repeat.write_text("{}\n", encoding="utf-8")
    fields = {
        "schema_version": 0,
        "dimension": 0,
        "slot": 0,
        "chunk_x": 0,
        "chunk_z": 0,
        "data_version": 0,
        "status": 0,
        "full": 0,
        "heightmaps": 1,
        "biome_sections": 0,
        "structure_starts": 0,
    }
    report = {
        "schema_version": "item7-control-comparison-v1",
        "selection": {"expected_count": 81},
        "control": {
            "run_receipt": _file_identity(control / "run-receipt.json", 1),
            "chunks": _file_identity(control / "chunks.jsonl", 2),
            "normalized_sha256": "a" * 64,
            "preflight": {},
            "lifecycle": {},
        },
        "pilot": {
            "run_receipt": _file_identity(pilot / "run-receipt.json", 1),
            "chunks": _file_identity(pilot / "chunks.jsonl", 2),
            "normalized_sha256": "b" * 64,
            "preflight": {},
            "lifecycle": {},
        },
        "repeat_comparison": _file_identity(repeat, 1),
        "equal": False,
        "field_mismatch_counts": fields,
        "first_mismatch": {"field": "heightmaps"},
        "disposition": "not_attributable_due_to_measured_stack_nondeterminism",
    }
    comparison = raw / "control-comparison.json"
    _ = comparison.write_text(json.dumps(report), encoding="utf-8")

    artifacts = completion_sources.validate_control(raw, comparison, repeat)

    assert tuple(row.path for row in artifacts) == (
        "control-comparison.json",
        "control/ordinary/run-receipt.json",
        "control/ordinary/chunks.jsonl",
        "pilot/ordinary-success/run-receipt.json",
        "pilot/ordinary-success/chunks.jsonl",
    )
    _ = (pilot / "chunks.jsonl").write_text("changed\n", encoding="utf-8")
    with pytest.raises(CompletionError, match="control source identity"):
        _ = completion_sources.validate_control(raw, comparison, repeat)
