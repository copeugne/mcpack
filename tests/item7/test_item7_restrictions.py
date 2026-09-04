from __future__ import annotations

import hashlib
import json
from typing import TYPE_CHECKING
from zipfile import ZipFile

import pytest

from mcpack_evidence.item7_restriction_inputs import ArchiveInput
from mcpack_evidence.item7_restrictions import audit_restrictions, validate_restriction_audit

if TYPE_CHECKING:
    from pathlib import Path


def _archive(path: Path, files: dict[str, object]) -> ArchiveInput:
    with ZipFile(path, "w") as archive:
        for name, value in files.items():
            archive.writestr(name, json.dumps(value))
    return ArchiveInput(path.name, path, hashlib.sha256(path.read_bytes()).hexdigest())


def test_audit_resolves_tags_and_records_active_impossible_restrictions(tmp_path: Path) -> None:
    source = _archive(
        tmp_path / "provider.jar",
        {
            "data/example/tags/worldgen/biome/valid.json": {"values": ["minecraft:plains"]},
            "data/example/tags/worldgen/biome/empty.json": {"values": []},
            "data/example/worldgen/structure/valid.json": {"biomes": "#example:valid"},
            "data/example/worldgen/structure/empty.json": {"biomes": "#example:empty"},
            "data/example/worldgen/structure/missing.json": {"biomes": "#example:missing"},
            "data/example/worldgen/structure_set/set.json": {
                "structures": [{"structure": "example:missing", "weight": 1}],
                "placement": {"type": "minecraft:random_spread"},
            },
        },
    )

    report = audit_restrictions((source,), "a" * 64)

    assert report.exit_gate == "PASS"
    assert (report.structure_count, report.resolved_structure_count) == (3, 1)
    assert (report.candidate_count, report.active_candidate_count) == (2, 1)
    candidates = {row.structure_id: row for row in report.candidates}
    assert candidates["example:empty"].status == "empty_tag"
    assert candidates["example:missing"].status == "missing_tag"
    assert candidates["example:missing"].placement_sets == ("example:set",)


def test_audit_rejects_changed_archive_bytes(tmp_path: Path) -> None:
    source = _archive(tmp_path / "provider.jar", {})
    _ = source.path.write_bytes(b"changed")

    with pytest.raises(ValueError, match="hash mismatch"):
        _ = audit_restrictions((source,), "a" * 64)


def test_committed_audit_binds_provider_catalog_hash(tmp_path: Path) -> None:
    source = _archive(tmp_path / "provider.jar", {})
    report = audit_restrictions((source,), "a" * 64)
    path = tmp_path / "audit.json"
    _ = path.write_text(report.model_dump_json(), encoding="utf-8")

    assert validate_restriction_audit(path, "a" * 64) == report
    with pytest.raises(ValueError, match="catalog hash mismatch"):
        _ = validate_restriction_audit(path, "b" * 64)
