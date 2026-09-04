# pyright: standard
from __future__ import annotations

from typing import TYPE_CHECKING, Literal, assert_never

import pytest

from mcpack_evidence.item6_manifest import parse_manifest
from mcpack_evidence.item6_sanitization import validate_sanitization_receipt
from tests.item6.helpers import Item6RepositoryFixture, copy_item6_repository, validate

if TYPE_CHECKING:
    from pathlib import Path

type Boundary = Literal[
    "manifest", "audit", "receipt", "sanitized_target", "lifecycle", "materialization"
]
type Corruption = Literal[
    "top_level_duplicate", "nested_duplicate", "NaN", "Infinity", "-Infinity", "1e309"
]

_BOUNDARIES: tuple[Boundary, ...] = (
    "manifest",
    "audit",
    "receipt",
    "sanitized_target",
    "lifecycle",
    "materialization",
)
_CORRUPTIONS: tuple[Corruption, ...] = (
    "top_level_duplicate",
    "nested_duplicate",
    "NaN",
    "Infinity",
    "-Infinity",
    "1e309",
)


@pytest.mark.parametrize("boundary", _BOUNDARIES)
@pytest.mark.parametrize("corruption", _CORRUPTIONS)
def test_full_document_boundaries_reject_non_strict_json(
    tmp_path: Path, boundary: Boundary, corruption: Corruption
) -> None:
    # Given: one otherwise-valid repository-shaped evidence fixture.
    fixture = copy_item6_repository(tmp_path)
    document = _document(fixture, boundary)
    document.write_text(
        _corrupt(document.read_text(encoding="utf-8"), boundary, corruption), encoding="utf-8"
    )

    # When/Then: parsing fails before schema or identity validation can reinterpret it.
    with pytest.raises(ValueError, match=_failure_message(boundary)):
        _validate_boundary(fixture, boundary)


def _document(fixture: Item6RepositoryFixture, boundary: Boundary) -> Path:
    match boundary:
        case "manifest":
            return fixture.manifest
        case "audit":
            return fixture.audit
        case "receipt":
            return fixture.sanitization
        case "sanitized_target":
            return fixture.frozen / "config/resourceful-config-web.json"
        case "lifecycle":
            return fixture.lifecycle
        case "materialization":
            return fixture.materialization
        case unreachable:
            assert_never(unreachable)


def _corrupt(document: str, boundary: Boundary, corruption: Corruption) -> str:
    match corruption:
        case "top_level_duplicate":
            member = "validator" if boundary == "sanitized_target" else "schema_version"
            return document.replace("{", f'{{\n  "{member}": null,', 1)
        case "nested_duplicate":
            return document.replace("{", '{\n  "strict_json_probe": {"member": 1, "member": 2},', 1)
        case "NaN" | "Infinity" | "-Infinity" | "1e309":
            return document.replace("{", f'{{\n  "strict_json_probe": {corruption},', 1)
        case unreachable:
            assert_never(unreachable)


def _validate_boundary(fixture: Item6RepositoryFixture, boundary: Boundary) -> None:
    match boundary:
        case "manifest":
            _ = parse_manifest(fixture.manifest)
        case "receipt" | "sanitized_target":
            _ = validate_sanitization_receipt(fixture.sanitization, fixture.frozen)
        case "audit" | "lifecycle" | "materialization":
            validate(fixture.frozen, fixture.manifest, fixture.audit)
        case unreachable:
            assert_never(unreachable)


def _failure_message(boundary: Boundary) -> str:
    match boundary:
        case "manifest":
            return "manifest is not strict JSON"
        case "audit":
            return "audit is not strict JSON"
        case "receipt":
            return "sanitization receipt is malformed"
        case "sanitized_target":
            return "sanitized target JSON is malformed"
        case "lifecycle":
            return "lifecycle receipt is malformed"
        case "materialization":
            return "materialization receipt is malformed"
        case unreachable:
            assert_never(unreachable)
