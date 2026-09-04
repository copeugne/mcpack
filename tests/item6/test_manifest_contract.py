# pyright: standard
"""Characterize and harden the Item 6 manifest contract."""

from __future__ import annotations

import json
from copy import deepcopy
from typing import TYPE_CHECKING

import pytest
from pydantic import ValidationError

from mcpack_evidence.item6_manifest import (
    Manifest,
    parse_manifest,
    validate_manifest_contract,
    validate_manifest_inventory,
)
from mcpack_evidence.item6_validation import sha256
from tests.item6.helpers import AUDIT, FROZEN, MANIFEST, validate

if TYPE_CHECKING:
    from pathlib import Path


def test_committed_manifest_inventory_is_valid() -> None:
    # Given: the committed frozen tree and its manifest.
    manifest = parse_manifest(MANIFEST)

    # When: the manifest inventory is checked directly.
    expected = validate_manifest_inventory(FROZEN, manifest)
    validate_manifest_contract(manifest)

    # Then: every recorded path is present exactly once in the frozen tree.
    assert len(expected) == manifest["file_count"]


def test_manifest_contract_rejects_duplicate_path(tmp_path: Path) -> None:
    # Given: a duplicate row with its file count and audit identity recomputed.
    manifest = _committed_manifest()
    manifest["files"].insert(1, deepcopy(manifest["files"][0]))
    manifest["file_count"] += 1

    # When: the duplicate inventory is validated.
    manifest_path, audit_path = _write_bound_manifest(tmp_path, manifest)

    # Then: duplicate paths cannot masquerade as an additional frozen file.
    _assert_manifest_rejected(manifest_path, audit_path, "manifest paths must be unique")


def test_manifest_contract_rejects_unsorted_paths(tmp_path: Path) -> None:
    # Given: two valid rows whose order is swapped and whose identity is recomputed.
    manifest = _committed_manifest()
    manifest["files"][0], manifest["files"][1] = manifest["files"][1], manifest["files"][0]

    # When: the reordered inventory is validated.
    manifest_path, audit_path = _write_bound_manifest(tmp_path, manifest)

    # Then: path ordering is part of the deterministic manifest contract.
    _assert_manifest_rejected(
        manifest_path, audit_path, "manifest paths must be strictly component-ordered"
    )


def test_manifest_contract_rejects_wrong_file_count(tmp_path: Path) -> None:
    # Given: an otherwise valid manifest with a stale count and bound audit identity.
    manifest = _committed_manifest()
    manifest["file_count"] += 1

    # When: the count is validated.
    manifest_path, audit_path = _write_bound_manifest(tmp_path, manifest)

    # Then: the declared count must equal its row count.
    _assert_manifest_rejected(
        manifest_path, audit_path, "frozen file inventory does not match manifest"
    )


def test_manifest_contract_rejects_shutdown_row(tmp_path: Path) -> None:
    # Given: one startup row reclassified as shutdown with a bound audit identity.
    manifest = _committed_manifest()
    row = next(row for row in manifest["files"] if row["generation_stage"] == "first_startup")
    row["generation_stage"] = "shutdown"

    # When: the lifecycle-stage partition is validated.
    manifest_path, audit_path = _write_bound_manifest(tmp_path, manifest)

    # Then: the frozen baseline contains no shutdown-classified rows.
    _assert_manifest_rejected(
        manifest_path, audit_path, "manifest generation-stage counts are invalid"
    )


def test_manifest_contract_rejects_invalid_capture_boundary(tmp_path: Path) -> None:
    # Given: a capture boundary that predates the required clean shutdown.
    manifest = _committed_manifest()
    manifest["capture_boundary"] = "after_first_startup"

    # When: the boundary is validated with its recomputed audit identity.
    manifest_path, audit_path = _write_bound_manifest(tmp_path, manifest)

    # Then: only the documented post-shutdown capture point is accepted.
    _assert_manifest_rejected(manifest_path, audit_path, "invalid manifest capture boundary")


@pytest.mark.parametrize(
    ("anchor", "unexpected_field"),
    [
        ("{\n", '  "unexpected_top_level": true,\n'),
        ('  "java": {\n', '    "unexpected_java_field": true,\n'),
        ('  "retained_manifest": {\n', '    "unexpected_retained_field": true,\n'),
        (
            '    {\n      "path": "config/accessories.json5",\n',
            '      "unexpected_row_field": true,\n',
        ),
    ],
)
def test_parse_manifest_rejects_unknown_fields(
    tmp_path: Path, anchor: str, unexpected_field: str
) -> None:
    # Given: a committed manifest with one syntactically valid unknown field.
    mutated = MANIFEST.read_text(encoding="utf-8").replace(
        anchor, f"{anchor}{unexpected_field}", 1
    )
    manifest_path = tmp_path / "manifest-with-unknown-field.json"
    manifest_path.write_text(mutated, encoding="utf-8")

    # When/Then: typed parsing rejects the unknown object member.
    with pytest.raises(ValidationError, match="extra_forbidden"):
        parse_manifest(manifest_path)


def _committed_manifest() -> Manifest:
    return parse_manifest(MANIFEST)


def _write_bound_manifest(tmp_path: Path, manifest: Manifest) -> tuple[Path, Path]:
    manifest_path = tmp_path / "manifest.json"
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
    audit = json.loads(AUDIT.read_text(encoding="utf-8"))
    audit["configuration_identity"] = f"sha256:{sha256(manifest_path)}"
    audit_path = tmp_path / "audit.json"
    audit_path.write_text(json.dumps(audit), encoding="utf-8")
    return manifest_path, audit_path


def _assert_manifest_rejected(manifest_path: Path, audit_path: Path, message: str) -> None:
    with pytest.raises(ValueError, match=message):
        validate(FROZEN, manifest_path, audit_path)
