# pyright: standard
"""Top-level Item 6 binding tests for sanitization evidence identity."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest

from mcpack_evidence.item6_manifest import parse_manifest
from tests.item6.helpers import MANIFEST, copy_item6_repository, rebind_audit, validate

if TYPE_CHECKING:
    from collections.abc import Callable
    from pathlib import Path


def test_committed_manifest_declares_canonical_sanitization_metadata() -> None:
    """The delivered manifest is version 2 and names a sanitization identity."""
    # Given: the committed Item 6 manifest.
    manifest = parse_manifest(MANIFEST)

    # When: its schema and sanitization metadata are inspected.
    schema_version = manifest["schema_version"]

    # Then: phase C's strict evidence identity is present.
    assert schema_version == "item6-frozen-config-manifest-v2"
    assert manifest["sanitization"]["receipt"] == "evidence/item-6/config-sanitization.json"


def test_validate_accepts_committed_sanitization_identity(tmp_path: Path) -> None:
    """Top-level validation binds the frozen target, receipt, and manifest metadata."""
    # Given: a complete mutable copy of the committed Item 6 evidence.
    fixture = copy_item6_repository(tmp_path)

    # When: validation follows the manifest's canonical sanitization receipt binding.
    validate(fixture.frozen, fixture.manifest, fixture.audit)

    # Then: the preserved canonical receipt is accepted.
    assert fixture.sanitization.is_file()


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("receipt", "evidence/item-6/alternate.json", "canonical repository path"),
        ("receipt", "../config-sanitization.json", "canonical repository path"),
        ("sha256", "0" * 64, "digest does not match manifest"),
        ("sanitized_file_count", 2, "counts must each equal one"),
        ("redaction_count", 2, "counts must each equal one"),
    ],
)
def test_validate_rejects_sanitization_metadata_mutations(
    tmp_path: Path, field: str, value: int | str, message: str
) -> None:
    """The manifest cannot redirect or misstate the sanitization identity."""
    # Given: a complete copy with one mutated metadata claim and updated audit identity.
    fixture = copy_item6_repository(tmp_path)
    _rewrite_manifest(fixture.manifest, lambda manifest: _set_metadata(manifest, field, value))
    rebind_audit(fixture)

    # When/Then: top-level validation rejects the inconsistent identity claim.
    with pytest.raises(ValueError, match=message):
        validate(fixture.frozen, fixture.manifest, fixture.audit)


@pytest.mark.parametrize("mutation", ["unknown", "missing"])
def test_validate_rejects_missing_or_unknown_sanitization_metadata(
    tmp_path: Path, mutation: str
) -> None:
    """Manifest v2 sanitization metadata is a strict required object."""
    # Given: an otherwise complete repository copy with one metadata shape error.
    fixture = copy_item6_repository(tmp_path)
    if mutation == "unknown":
        _rewrite_manifest(
            fixture.manifest,
            lambda manifest: manifest["sanitization"].__setitem__("unexpected", 1),
        )
    else:
        _rewrite_manifest(fixture.manifest, lambda manifest: manifest.pop("sanitization"))
    rebind_audit(fixture)

    # When/Then: strict manifest parsing refuses the unsafe metadata shape.
    with pytest.raises(ValueError, match=r"extra_forbidden|Field required"):
        validate(fixture.frozen, fixture.manifest, fixture.audit)


def test_validate_rejects_stale_sanitization_receipt_digest(tmp_path: Path) -> None:
    """Receipt bytes are bound by the manifest digest, not merely its parsed shape."""
    # Given: a valid receipt whose bytes receive an otherwise harmless trailing newline.
    fixture = copy_item6_repository(tmp_path)
    _ = fixture.sanitization.write_text(
        fixture.sanitization.read_text(encoding="utf-8") + "\n", encoding="utf-8"
    )

    # When/Then: validation rejects the stale digest binding.
    with pytest.raises(ValueError, match="digest does not match manifest"):
        validate(fixture.frozen, fixture.manifest, fixture.audit)


def test_validate_rejects_missing_sanitization_receipt(tmp_path: Path) -> None:
    """The manifest cannot validate without its canonical receipt file."""
    # Given: a complete copy whose canonical receipt is absent.
    fixture = copy_item6_repository(tmp_path)
    fixture.sanitization.unlink()

    # When/Then: top-level validation refuses the incomplete evidence package.
    with pytest.raises(ValueError, match="sanitization receipt binding is invalid"):
        validate(fixture.frozen, fixture.manifest, fixture.audit)


def test_validate_rejects_symlinked_sanitization_receipt(tmp_path: Path) -> None:
    """The canonical receipt cannot resolve through a filesystem indirection."""
    # Given: a canonical receipt path replaced by a symlink to identical bytes.
    fixture = copy_item6_repository(tmp_path)
    external = fixture.sanitization.with_name("external-sanitization.json")
    fixture.sanitization.replace(external)
    fixture.sanitization.symlink_to(external)

    # When/Then: validation rejects the symlink before digesting its target.
    with pytest.raises(ValueError, match="sanitization receipt binding is invalid"):
        validate(fixture.frozen, fixture.manifest, fixture.audit)


def _rewrite_manifest(path: Path, mutate: Callable[[dict], None]) -> None:
    manifest = json.loads(path.read_text(encoding="utf-8"))
    mutate(manifest)
    _ = path.write_text(json.dumps(manifest), encoding="utf-8")


def _set_metadata(manifest: dict, field: str, value: int | str) -> None:
    manifest["sanitization"][field] = value
