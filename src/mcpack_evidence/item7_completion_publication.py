"""Durable release acceptance for Item 7 completion."""

from __future__ import annotations

from pathlib import Path  # noqa: TC003
from typing import ClassVar, Final, Literal

from pydantic import BaseModel, ConfigDict, Field

from mcpack_evidence.item7_archive import ArchiveManifest
from mcpack_evidence.item7_completion_io import fail, identity, portable_path, strict_model
from mcpack_evidence.item7_completion_models import ArtifactIdentity  # noqa: TC001

_ARCHIVE_COUNT: Final = 4
_REPOSITORY: Final = "copeugne/mcpack"
_VERIFICATION_TOOL: Final = "tools/verify_item7_release.sh"


class _Strict(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid", strict=True)


class _PublishedAsset(_Strict):
    name: str
    size_bytes: int = Field(ge=0)
    sha256: str = Field(pattern=r"^[0-9a-f]{64}$")
    manifest: str
    restore_receipt: str
    url: str


class _Publication(_Strict):
    schema_version: Literal["item7-raw-evidence-publication-v1"]
    repository: Literal["copeugne/mcpack"]
    release_url: str
    tag: str = Field(min_length=1)
    tag_object_sha: str = Field(pattern=r"^[0-9a-f]{40}$")
    source_revision: str = Field(pattern=r"^[0-9a-f]{40}$")
    published_at: str = Field(min_length=1)
    verified_at: str = Field(min_length=1)
    verification_tool: str
    verification_command: str = Field(min_length=1)
    downloaded_bytes_verified: Literal[True]
    assets: tuple[_PublishedAsset, ...]


def validate_publication(
    path: Path,
    manifest_paths: tuple[Path, ...],
) -> tuple[ArtifactIdentity, str]:
    """Bind the remote release receipt to all archive manifests and downloaded bytes."""
    if len(manifest_paths) != _ARCHIVE_COUNT:
        fail("publication archive count", len(manifest_paths))
    manifests = tuple(strict_model(item, ArchiveManifest) for item in manifest_paths)
    revisions = {manifest.revision for manifest in manifests}
    publication = strict_model(path, _Publication)
    _ = portable_path(publication.verification_tool)
    if (
        revisions != {publication.source_revision}
        or publication.repository != _REPOSITORY
        or publication.verification_tool != _VERIFICATION_TOOL
        or publication.release_url
        != f"https://github.com/{_REPOSITORY}/releases/tag/{publication.tag}"
    ):
        fail("publication release identity", path)
    expected = {
        manifest.archive_name: (
            manifest.archive_size_bytes,
            manifest.archive_sha256,
            f"evidence/item-7/archive/{manifest_path.name}",
            (
                "evidence/item-7/archive/"
                f"{manifest_path.name.removesuffix('-manifest.json')}-restore.json"
            ),
            (
                f"https://github.com/{_REPOSITORY}/releases/download/"
                f"{publication.tag}/{manifest.archive_name}"
            ),
        )
        for manifest, manifest_path in zip(manifests, manifest_paths, strict=True)
    }
    observed = {
        asset.name: (
            asset.size_bytes,
            asset.sha256,
            portable_path(asset.manifest),
            portable_path(asset.restore_receipt),
            asset.url,
        )
        for asset in publication.assets
    }
    if len(observed) != len(publication.assets) or observed != expected:
        fail("publication asset identities", path)
    return identity(path, "archive/publication.json"), publication.release_url
