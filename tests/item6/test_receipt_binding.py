# pyright: standard
"""Bind Item 6 validation to its repository provenance receipts."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest

from tests.item6.helpers import copy_item6_repository, rebind_audit, validate

if TYPE_CHECKING:
    from collections.abc import Callable
    from pathlib import Path


def test_validate_accepts_bound_repository_references(tmp_path: Path) -> None:
    # Given: the committed inputs copied beneath their canonical repository paths.
    fixture = copy_item6_repository(tmp_path)

    # When: the complete copied evidence set is validated.
    validate(fixture.frozen, fixture.manifest, fixture.audit)

    # Then: the reference paths, retained count, and retained digest agree.
    assert fixture.retained.is_file()


@pytest.mark.parametrize(
    "reference",
    [
        "/etc/passwd",
        "../retained-server-candidates.txt",
        "evidence/item-3/runtime/../retained-server-candidates.txt",
        r"evidence\item-3\runtime\retained-server-candidates.txt",
    ],
)
def test_validate_rejects_unconfined_retained_manifest_reference(
    tmp_path: Path, reference: str
) -> None:
    # Given: an absolute, traversing, non-normalized, or non-POSIX retained reference.
    fixture = copy_item6_repository(tmp_path)
    _rewrite_manifest(fixture.manifest, lambda manifest: _set_retained_path(manifest, reference))
    rebind_audit(fixture)

    # When/Then: validation rejects the reference before reading outside the repository.
    with pytest.raises(ValueError, match="repository-relative POSIX path"):
        validate(fixture.frozen, fixture.manifest, fixture.audit)


@pytest.mark.parametrize("reference", ["/outside/lifecycle.json", "../lifecycle.json"])
def test_validate_rejects_unconfined_lifecycle_reference(tmp_path: Path, reference: str) -> None:
    # Given: an absolute or traversing lifecycle reference.
    fixture = copy_item6_repository(tmp_path)
    _rewrite_manifest(fixture.manifest, lambda manifest: _set_lifecycle_path(manifest, reference))
    rebind_audit(fixture)

    # When/Then: validation rejects the reference before reading outside the repository.
    with pytest.raises(ValueError, match="repository-relative POSIX path"):
        validate(fixture.frozen, fixture.manifest, fixture.audit)


def test_validate_rejects_symlinked_retained_manifest(tmp_path: Path) -> None:
    # Given: the retained reference resolves through a symlink to a regular file.
    fixture = copy_item6_repository(tmp_path)
    fixture.retained.unlink()
    fixture.retained.symlink_to("replacement.txt")
    _ = fixture.retained.with_name("replacement.txt").write_bytes(b"replacement\n")

    # When/Then: a symlink cannot satisfy the evidence reference contract.
    with pytest.raises(ValueError, match="regular non-symlink file"):
        validate(fixture.frozen, fixture.manifest, fixture.audit)


def test_validate_rejects_symlinked_lifecycle_receipt(tmp_path: Path) -> None:
    # Given: the lifecycle reference resolves through a symlink to a regular file.
    fixture = copy_item6_repository(tmp_path)
    fixture.lifecycle.unlink()
    fixture.lifecycle.symlink_to("replacement.json")
    _ = fixture.lifecycle.with_name("replacement.json").write_text("{}", encoding="utf-8")

    # When/Then: a symlink cannot satisfy the evidence reference contract.
    with pytest.raises(ValueError, match="regular non-symlink file"):
        validate(fixture.frozen, fixture.manifest, fixture.audit)


def test_validate_rejects_nonfile_retained_manifest(tmp_path: Path) -> None:
    # Given: the retained reference names a directory rather than a regular file.
    fixture = copy_item6_repository(tmp_path)
    fixture.retained.unlink()
    fixture.retained.mkdir()

    # When/Then: a directory cannot satisfy the evidence reference contract.
    with pytest.raises(ValueError, match="regular non-symlink file"):
        validate(fixture.frozen, fixture.manifest, fixture.audit)


def test_validate_rejects_missing_lifecycle_receipt(tmp_path: Path) -> None:
    # Given: the referenced lifecycle receipt is absent.
    fixture = copy_item6_repository(tmp_path)
    fixture.lifecycle.unlink()

    # When/Then: a missing receipt cannot satisfy the evidence reference contract.
    with pytest.raises(ValueError, match="regular non-symlink file"):
        validate(fixture.frozen, fixture.manifest, fixture.audit)


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("count", 135, "retained manifest count does not match"),
        ("sha256", "0" * 64, "retained manifest digest does not match"),
    ],
)
def test_validate_rejects_retained_manifest_identity_mismatch(
    tmp_path: Path, field: str, value: int | str, message: str
) -> None:
    # Given: the manifest misstates one retained candidate identity field.
    fixture = copy_item6_repository(tmp_path)
    _rewrite_manifest(
        fixture.manifest,
        lambda manifest: _set_retained_identity(manifest, field, value),
    )
    rebind_audit(fixture)

    # When/Then: the retained source is checked rather than trusted by assertion.
    with pytest.raises(ValueError, match=message):
        validate(fixture.frozen, fixture.manifest, fixture.audit)


def _rewrite_manifest(path: Path, mutate: Callable[[dict], None]) -> None:
    manifest = json.loads(path.read_text(encoding="utf-8"))
    mutate(manifest)
    path.write_text(json.dumps(manifest), encoding="utf-8")


def _set_retained_path(manifest: dict, reference: str) -> None:
    manifest["retained_manifest"]["path"] = reference


def _set_lifecycle_path(manifest: dict, reference: str) -> None:
    manifest["source_lifecycle"] = reference


def _set_retained_identity(manifest: dict, field: str, value: int | str) -> None:
    manifest["retained_manifest"][field] = value
