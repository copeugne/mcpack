# pyright: standard
"""Seal the frozen Item 6 manifest against coordinated evidence rebinding."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest

from mcpack_evidence.item6_validation import sha256
from tests.item6.helpers import copy_item6_repository, rebind_audit, validate

if TYPE_CHECKING:
    from pathlib import Path


def test_validate_rejects_rebound_baseline_seed(tmp_path: Path) -> None:
    # Given: the manifest and receipt agree on a different seed and all digests are rebound.
    fixture = copy_item6_repository(tmp_path)
    materialization = json.loads(fixture.materialization.read_text(encoding="utf-8"))
    materialization["seed"] = "43"
    _write_json(fixture.materialization, materialization)
    manifest = json.loads(fixture.manifest.read_text(encoding="utf-8"))
    manifest["seed"] = "43"
    manifest["materialization_sha256"] = sha256(fixture.materialization)
    _write_json(fixture.manifest, manifest)
    rebind_audit(fixture)

    # When/Then: cross-consistent mutable evidence cannot replace the frozen baseline.
    with pytest.raises(ValueError, match="manifest identity does not match frozen baseline"):
        validate(fixture.frozen, fixture.manifest, fixture.audit)


def test_validate_rejects_rebound_retained_candidate_manifest(tmp_path: Path) -> None:
    # Given: an alternate 136-line candidate set is bound through every mutable receipt.
    fixture = copy_item6_repository(tmp_path)
    candidates = fixture.retained.read_text(encoding="utf-8").splitlines()
    candidates[0] = f"{candidates[0]}-alternate"
    alternate = fixture.retained.with_name("alternate-candidates.txt")
    alternate.write_text("\n".join(candidates) + "\n", encoding="utf-8")
    retained_digest = sha256(alternate)
    materialization = json.loads(fixture.materialization.read_text(encoding="utf-8"))
    materialization["retained_manifest_sha256"] = retained_digest
    _write_json(fixture.materialization, materialization)
    manifest = json.loads(fixture.manifest.read_text(encoding="utf-8"))
    manifest["retained_manifest"] = {
        "path": "evidence/item-3/runtime/alternate-candidates.txt",
        "count": len(candidates),
        "sha256": retained_digest,
    }
    manifest["materialization_sha256"] = sha256(fixture.materialization)
    _write_json(fixture.manifest, manifest)
    rebind_audit(fixture)

    # When/Then: a different retained set cannot become the certified Item 6 source.
    with pytest.raises(ValueError, match="manifest identity does not match frozen baseline"):
        validate(fixture.frozen, fixture.manifest, fixture.audit)


def test_validate_rejects_rebound_generation_stage_swap(tmp_path: Path) -> None:
    # Given: installation and startup rows exchange stages while aggregate counts stay valid.
    fixture = copy_item6_repository(tmp_path)
    manifest = json.loads(fixture.manifest.read_text(encoding="utf-8"))
    installation = next(
        row for row in manifest["files"] if row["generation_stage"] == "installation"
    )
    startup = next(row for row in manifest["files"] if row["generation_stage"] == "first_startup")
    installation["generation_stage"], startup["generation_stage"] = (
        startup["generation_stage"],
        installation["generation_stage"],
    )
    _write_json(fixture.manifest, manifest)
    rebind_audit(fixture)

    # When/Then: per-file stage provenance remains bound to the frozen manifest.
    with pytest.raises(ValueError, match="manifest identity does not match frozen baseline"):
        validate(fixture.frozen, fixture.manifest, fixture.audit)


def _write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload), encoding="utf-8")
