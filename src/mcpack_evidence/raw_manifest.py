"""Deterministic content manifests for raw evidence retained outside Git."""

from __future__ import annotations

import hashlib
from typing import TYPE_CHECKING, ClassVar, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from pathlib import Path


class RawFileIdentity(BaseModel):
    """Content identity for one regular raw-evidence file."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    relative_path: str
    size_bytes: int = Field(ge=0)
    sha256: str = Field(pattern=r"^[0-9a-f]{64}$")


class RawEvidenceManifest(BaseModel):
    """Deterministic inventory of a raw-evidence directory tree."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    schema_version: Literal["raw-evidence-manifest-v1"]
    root: str
    file_count: int = Field(ge=0)
    total_size_bytes: int = Field(ge=0)
    files: tuple[RawFileIdentity, ...]


def build_raw_manifest(root: Path) -> RawEvidenceManifest:
    """Hash every regular file below a root in stable path order."""
    paths = (path for path in root.rglob("*") if path.is_file())
    files = tuple(
        RawFileIdentity(
            relative_path=path.relative_to(root).as_posix(),
            size_bytes=path.stat().st_size,
            sha256=_sha256(path),
        )
        for path in sorted(paths, key=lambda candidate: candidate.relative_to(root).as_posix())
    )
    return RawEvidenceManifest(
        schema_version="raw-evidence-manifest-v1",
        root=root.as_posix(),
        file_count=len(files),
        total_size_bytes=sum(row.size_bytes for row in files),
        files=files,
    )


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        while block := stream.read(1024 * 1024):
            digest.update(block)
    return digest.hexdigest()
