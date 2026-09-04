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


def test_validate_rejects_nonfile_lifecycle_receipt(tmp_path: Path) -> None:
    # Given: the canonical lifecycle receipt is a directory rather than a file.
    fixture = copy_item6_repository(tmp_path)
    fixture.lifecycle.unlink()
    fixture.lifecycle.mkdir()

    # When/Then: a directory cannot satisfy the lifecycle reference contract.
    with pytest.raises(ValueError, match="regular non-symlink file"):
        validate(fixture.frozen, fixture.manifest, fixture.audit)


def test_validate_rejects_malformed_lifecycle_receipt(tmp_path: Path) -> None:
    # Given: the canonical lifecycle receipt contains malformed JSON.
    fixture = copy_item6_repository(tmp_path)
    fixture.lifecycle.write_text("{", encoding="utf-8")

    # When/Then: malformed receipt bytes cannot prove the lifecycle contract.
    with pytest.raises(ValueError, match="lifecycle receipt is malformed"):
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


@pytest.mark.parametrize("field", ["ready", "save_all_flush", "clean_stop"])
def test_validate_rejects_unsuccessful_lifecycle_status(tmp_path: Path, field: str) -> None:
    # Given: one required lifecycle status is false.
    fixture = copy_item6_repository(tmp_path)
    _rewrite_json(fixture.lifecycle, lambda receipt: _set_false(receipt, field))

    # When/Then: the lifecycle cannot prove a clean generation boundary.
    with pytest.raises(ValueError, match=f"lifecycle {field} must be true"):
        validate(fixture.frozen, fixture.manifest, fixture.audit)


@pytest.mark.parametrize("return_code", [1, True])
def test_validate_rejects_invalid_lifecycle_return_code(
    tmp_path: Path, return_code: int | bool
) -> None:
    # Given: the lifecycle has a nonzero integer or boolean return code.
    fixture = copy_item6_repository(tmp_path)
    _rewrite_json(
        fixture.lifecycle,
        lambda receipt: receipt.__setitem__("return_code", return_code),
    )

    # When/Then: only the exact integer zero is accepted.
    with pytest.raises(
        ValueError, match=r"lifecycle receipt is malformed|return_code must be zero"
    ):
        validate(fixture.frozen, fixture.manifest, fixture.audit)


def test_validate_rejects_wrong_lifecycle_schema(tmp_path: Path) -> None:
    # Given: a structurally valid receipt under an unrecognized schema.
    fixture = copy_item6_repository(tmp_path)
    _rewrite_json(
        fixture.lifecycle,
        lambda receipt: receipt.__setitem__("schema_version", "item4-server-lifecycle-v2"),
    )

    # When/Then: validation rejects the unrecognized lifecycle protocol.
    with pytest.raises(ValueError, match="unsupported lifecycle receipt schema"):
        validate(fixture.frozen, fixture.manifest, fixture.audit)


def test_validate_rejects_noncanonical_lifecycle_source(tmp_path: Path) -> None:
    # Given: the manifest points at an existing receipt under a different repository path.
    fixture = copy_item6_repository(tmp_path)
    alternate = fixture.lifecycle.with_name("alternate-lifecycle.json")
    fixture.lifecycle.rename(alternate)
    _rewrite_manifest(
        fixture.manifest,
        lambda manifest: _set_lifecycle_path(manifest, "evidence/item-6/alternate-lifecycle.json"),
    )
    rebind_audit(fixture)

    # When/Then: only the canonical retained lifecycle receipt is accepted.
    with pytest.raises(ValueError, match="source_lifecycle must name the canonical receipt"):
        validate(fixture.frozen, fixture.manifest, fixture.audit)


def _rewrite_manifest(path: Path, mutate: Callable[[dict], None]) -> None:
    manifest = json.loads(path.read_text(encoding="utf-8"))
    mutate(manifest)
    path.write_text(json.dumps(manifest), encoding="utf-8")


def _rewrite_json(path: Path, mutate: Callable[[dict], None]) -> None:
    payload = json.loads(path.read_text(encoding="utf-8"))
    mutate(payload)
    path.write_text(json.dumps(payload), encoding="utf-8")


def _set_retained_path(manifest: dict, reference: str) -> None:
    manifest["retained_manifest"]["path"] = reference


def _set_lifecycle_path(manifest: dict, reference: str) -> None:
    manifest["source_lifecycle"] = reference


def _set_false(payload: dict, field: str) -> None:
    payload[field] = False


def _set_retained_identity(manifest: dict, field: str, value: int | str) -> None:
    manifest["retained_manifest"][field] = value
