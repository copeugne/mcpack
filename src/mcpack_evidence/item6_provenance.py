# ruff: noqa: EM101, TRY003
"""Validate repository-bound provenance for the Item 6 frozen baseline."""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import TYPE_CHECKING, Final, TypedDict

from pydantic import TypeAdapter, ValidationError

if TYPE_CHECKING:
    from mcpack_evidence.item6_manifest import Manifest


class ProvenanceValidationError(ValueError):
    """Raised when an Item 6 provenance reference is unsafe or inconsistent."""


@dataclass(frozen=True, slots=True)
class RepositoryReferences:
    """Resolved regular files referenced by the Item 6 manifest."""

    root: Path
    retained_manifest: Path
    source_lifecycle: Path


class _LifecycleReceipt(TypedDict):
    schema_version: str
    instance: str
    ready: bool
    save_all_flush: bool
    clean_stop: bool
    return_code: int
    duration_seconds: float
    log: str


_LIFECYCLE_ADAPTER: Final[TypeAdapter[_LifecycleReceipt]] = TypeAdapter(_LifecycleReceipt)
_LIFECYCLE_PATH: Final = "evidence/item-6/first-boot-lifecycle.json"


def validate_repository_references(manifest_path: Path, manifest: Manifest) -> RepositoryReferences:
    """Resolve and verify the manifest's repository file references."""
    repository = manifest_path.parent.parent.parent
    retained = _resolve_regular_file(repository, manifest["retained_manifest"]["path"])
    lifecycle = _resolve_regular_file(repository, manifest["source_lifecycle"])
    retained_identity = manifest["retained_manifest"]
    if len(retained.read_bytes().splitlines()) != retained_identity["count"]:
        raise ProvenanceValidationError("retained manifest count does not match referenced file")
    if _sha256(retained) != retained_identity["sha256"]:
        raise ProvenanceValidationError("retained manifest digest does not match referenced file")
    return RepositoryReferences(
        root=repository.resolve(strict=True),
        retained_manifest=retained,
        source_lifecycle=lifecycle,
    )


def validate_lifecycle(manifest: Manifest, references: RepositoryReferences) -> None:
    """Require a successful lifecycle receipt under its canonical repository identity."""
    if manifest["source_lifecycle"] != _LIFECYCLE_PATH:
        raise ProvenanceValidationError("source_lifecycle must name the canonical receipt")
    try:
        receipt = _LIFECYCLE_ADAPTER.validate_json(
            references.source_lifecycle.read_bytes(), strict=True, extra="forbid"
        )
    except ValidationError as error:
        raise ProvenanceValidationError("lifecycle receipt is malformed") from error
    if receipt["schema_version"] != "item4-server-lifecycle-v1":
        raise ProvenanceValidationError("unsupported lifecycle receipt schema")
    for field in ("ready", "save_all_flush", "clean_stop"):
        if receipt[field] is not True:
            message = f"lifecycle {field} must be true"
            raise ProvenanceValidationError(message)
    if receipt["return_code"] != 0:
        raise ProvenanceValidationError("lifecycle return_code must be zero")


def _resolve_regular_file(repository: Path, reference: str) -> Path:
    relative = PurePosixPath(reference)
    if (
        not reference
        or "\\" in reference
        or relative.is_absolute()
        or relative.as_posix() != reference
        or ".." in relative.parts
    ):
        raise ProvenanceValidationError("reference must be a repository-relative POSIX path")
    repository_resolved = repository.resolve(strict=True)
    candidate = repository
    for part in relative.parts:
        candidate /= part
        if candidate.is_symlink():
            raise ProvenanceValidationError("referenced path must be a regular non-symlink file")
    if not candidate.is_file():
        raise ProvenanceValidationError("referenced path must be a regular non-symlink file")
    try:
        _ = candidate.resolve(strict=True).relative_to(repository_resolved)
    except ValueError as error:
        raise ProvenanceValidationError(
            "reference must be a repository-relative POSIX path"
        ) from error
    return candidate


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()
