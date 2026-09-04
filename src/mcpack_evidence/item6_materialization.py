# ruff: noqa: EM101, TRY003
"""Validate the Item 6 materialization receipt against its frozen manifest."""

from __future__ import annotations

import hashlib
from typing import TYPE_CHECKING, Final, TypedDict

from pydantic import TypeAdapter, ValidationError

from mcpack_evidence.item6_json import StrictJsonError, parse_strict_json

if TYPE_CHECKING:
    from mcpack_evidence.item6_manifest import Manifest
    from mcpack_evidence.item6_provenance import RepositoryReferences


class _MaterializationReceipt(TypedDict):
    schema_version: str
    configuration_version: str
    seed_role: str
    seed: str
    retained_candidate_count: int
    retained_manifest_sha256: str
    pristine_source: str
    production_state_used: bool
    copied_world_removed: bool


_ADAPTER: Final[TypeAdapter[_MaterializationReceipt]] = TypeAdapter(_MaterializationReceipt)
_SCHEMA: Final = "item4-materialization-v1"


class MaterializationValidationError(ValueError):
    """Raised when materialization evidence is malformed or inconsistent."""


def validate_materialization(manifest: Manifest, references: RepositoryReferences) -> None:
    """Require strict materialization isolation and exact manifest identity agreement."""
    try:
        receipt = _ADAPTER.validate_python(
            parse_strict_json(references.materialization.read_bytes()), strict=True, extra="forbid"
        )
    except (StrictJsonError, ValidationError) as error:
        raise MaterializationValidationError("materialization receipt is malformed") from error
    if receipt["schema_version"] != _SCHEMA:
        raise MaterializationValidationError("unsupported materialization receipt schema")
    if receipt["production_state_used"] is not False:
        raise MaterializationValidationError("production_state_used must be false")
    if receipt["copied_world_removed"] is not True:
        raise MaterializationValidationError("copied_world_removed must be true")
    if receipt["configuration_version"] != manifest["configuration_version"]:
        raise MaterializationValidationError("configuration_version does not match manifest")
    if receipt["seed_role"] != manifest["seed_role"]:
        raise MaterializationValidationError("seed_role does not match manifest")
    if receipt["seed"] != manifest["seed"]:
        raise MaterializationValidationError("seed does not match manifest")
    retained = manifest["retained_manifest"]
    if receipt["retained_candidate_count"] != retained["count"]:
        raise MaterializationValidationError("retained_candidate_count does not match manifest")
    if receipt["retained_manifest_sha256"] != retained["sha256"]:
        raise MaterializationValidationError("retained_manifest_sha256 does not match manifest")
    _validate_receipt_digest(manifest, references)


def _validate_receipt_digest(manifest: Manifest, references: RepositoryReferences) -> None:
    digest = hashlib.sha256(references.materialization.read_bytes()).hexdigest()
    if digest != manifest["materialization_sha256"]:
        raise MaterializationValidationError("materialization receipt digest does not match")
