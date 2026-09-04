# ruff: noqa: EM101, TRY003
"""Validate repository-bound provenance for the Item 6 frozen baseline."""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import TYPE_CHECKING

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
