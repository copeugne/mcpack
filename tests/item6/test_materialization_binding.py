# pyright: standard
"""Bind Item 6 validation to the retained materialization receipt."""

from __future__ import annotations

import json
from pathlib import Path
from typing import TYPE_CHECKING

import pytest

from tests.item6.helpers import copy_item6_repository, validate

if TYPE_CHECKING:
    from collections.abc import Callable


def test_validate_accepts_materialization_with_absent_historical_source(tmp_path: Path) -> None:
    # Given: the committed receipt retains a historical absolute pristine-source observation.
    fixture = copy_item6_repository(tmp_path)
    receipt = json.loads(fixture.materialization.read_text(encoding="utf-8"))
    assert not Path(receipt["pristine_source"]).exists()

    # When/Then: the historical observation is not treated as a live dependency.
    validate(fixture.frozen, fixture.manifest, fixture.audit)


def test_validate_rejects_missing_materialization_receipt(tmp_path: Path) -> None:
    # Given: the canonical materialization receipt is absent.
    fixture = copy_item6_repository(tmp_path)
    fixture.materialization.unlink()

    # When/Then: validation requires the canonical regular file.
    with pytest.raises(ValueError, match="regular non-symlink file"):
        validate(fixture.frozen, fixture.manifest, fixture.audit)


def test_validate_rejects_symlinked_materialization_receipt(tmp_path: Path) -> None:
    # Given: the canonical receipt is replaced by a symlink.
    fixture = copy_item6_repository(tmp_path)
    fixture.materialization.rename(fixture.materialization.with_name("replacement.json"))
    fixture.materialization.symlink_to("replacement.json")

    # When/Then: symlinked evidence is rejected.
    with pytest.raises(ValueError, match="regular non-symlink file"):
        validate(fixture.frozen, fixture.manifest, fixture.audit)


def test_validate_rejects_nonfile_materialization_receipt(tmp_path: Path) -> None:
    # Given: the canonical receipt path is a directory.
    fixture = copy_item6_repository(tmp_path)
    fixture.materialization.unlink()
    fixture.materialization.mkdir()

    # When/Then: only a regular file can prove materialization.
    with pytest.raises(ValueError, match="regular non-symlink file"):
        validate(fixture.frozen, fixture.manifest, fixture.audit)


@pytest.mark.parametrize("contents", ["{", "[]", '{"schema_version": 1}'])
def test_validate_rejects_malformed_materialization_receipt(tmp_path: Path, contents: str) -> None:
    # Given: the canonical receipt does not satisfy the typed object boundary.
    fixture = copy_item6_repository(tmp_path)
    fixture.materialization.write_text(contents, encoding="utf-8")

    # When/Then: malformed or structurally invalid JSON is rejected.
    with pytest.raises(ValueError, match="materialization receipt is malformed"):
        validate(fixture.frozen, fixture.manifest, fixture.audit)


def test_validate_rejects_wrong_materialization_schema(tmp_path: Path) -> None:
    # Given: a structurally valid receipt declares an unsupported schema.
    fixture = copy_item6_repository(tmp_path)
    _rewrite(fixture.materialization, lambda receipt: _set(receipt, "schema_version", "v2"))

    # When/Then: schema identity is exact.
    with pytest.raises(ValueError, match="unsupported materialization receipt schema"):
        validate(fixture.frozen, fixture.manifest, fixture.audit)


def test_validate_rejects_extra_materialization_field(tmp_path: Path) -> None:
    # Given: an undeclared field attempts to extend the evidence protocol.
    fixture = copy_item6_repository(tmp_path)
    _rewrite(fixture.materialization, lambda receipt: _set(receipt, "unexpected", "value"))

    # When/Then: strict parsing forbids silent schema drift.
    with pytest.raises(ValueError, match="materialization receipt is malformed"):
        validate(fixture.frozen, fixture.manifest, fixture.audit)


def test_validate_rejects_materialization_receipt_identity_mismatch(tmp_path: Path) -> None:
    # Given: a structurally valid receipt claims a different pristine source.
    fixture = copy_item6_repository(tmp_path)
    _rewrite(
        fixture.materialization,
        lambda receipt: _set(receipt, "pristine_source", "/different/pristine-source"),
    )

    # When/Then: the manifest-bound materialization bytes cannot be substituted.
    with pytest.raises(ValueError, match="materialization receipt digest does not match"):
        validate(fixture.frozen, fixture.manifest, fixture.audit)


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("production_state_used", True, "production_state_used must be false"),
        ("production_state_used", 0, "materialization receipt is malformed"),
        ("copied_world_removed", False, "copied_world_removed must be true"),
        ("copied_world_removed", 1, "materialization receipt is malformed"),
    ],
)
def test_validate_rejects_invalid_materialization_safety_flag(
    tmp_path: Path, field: str, value: bool | int, message: str
) -> None:
    # Given: a safety flag has the wrong value or primitive type.
    fixture = copy_item6_repository(tmp_path)
    _rewrite(fixture.materialization, lambda receipt: _set(receipt, field, value))

    # When/Then: the isolation guarantees are exact typed booleans.
    with pytest.raises(ValueError, match=message):
        validate(fixture.frozen, fixture.manifest, fixture.audit)


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("configuration_version", "different", "configuration_version does not match"),
        ("seed_role", "mountainous", "seed_role does not match"),
        ("seed", "042", "seed does not match"),
        ("retained_candidate_count", 135, "retained_candidate_count does not match"),
        ("retained_candidate_count", True, "materialization receipt is malformed"),
        ("retained_manifest_sha256", "0" * 64, "retained_manifest_sha256 does not match"),
    ],
)
def test_validate_rejects_materialization_identity_mismatch(
    tmp_path: Path, field: str, value: str | int | bool, message: str
) -> None:
    # Given: one materialization identity differs from the frozen manifest.
    fixture = copy_item6_repository(tmp_path)
    _rewrite(fixture.materialization, lambda receipt: _set(receipt, field, value))

    # When/Then: all five identity fields must agree exactly and by primitive type.
    with pytest.raises(ValueError, match=message):
        validate(fixture.frozen, fixture.manifest, fixture.audit)


def _rewrite(path: Path, mutate: Callable[[dict], None]) -> None:
    receipt = json.loads(path.read_text(encoding="utf-8"))
    mutate(receipt)
    path.write_text(json.dumps(receipt), encoding="utf-8")


def _set(receipt: dict, field: str, value: str | int | bool) -> None:
    receipt[field] = value
