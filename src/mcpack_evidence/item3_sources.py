"""Normalize exact primary-platform records for the Item 3 candidate inventory."""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from pydantic import BaseModel, ConfigDict, Field

from mcpack_evidence.item3_source_models import (
    SourceArtifact,
    SourceCandidate,
    SourceDeclaredCompatibility,
    SourceDependency,
    SourceEvidenceError,
    SourceMatrix,
    SourceProject,
    SourceVersion,
)

if TYPE_CHECKING:
    from pathlib import Path


class _License(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(extra="ignore")

    id: str


class _ModrinthProject(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(extra="ignore")

    id: str
    slug: str
    title: str
    license: _License
    client_side: str
    server_side: str


class _ModrinthDependency(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(extra="ignore")

    dependency_type: str
    project_id: str | None = None
    version_id: str | None = None


class _ModrinthVersion(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(extra="ignore")

    id: str
    name: str
    version_number: str
    date_published: str
    version_type: str
    game_versions: tuple[str, ...]
    loaders: tuple[str, ...]
    dependencies: tuple[_ModrinthDependency, ...]


class _ModrinthFile(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(extra="ignore")

    id: str
    filename: str
    size: int
    url: str
    hashes: dict[str, str]


class _ModrinthRow(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(extra="ignore")

    candidate_filename: str
    resolved: bool
    project: _ModrinthProject | None = None
    version: _ModrinthVersion | None = None
    file: _ModrinthFile | None = None


class _ModrinthDiscovery(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(extra="ignore")

    retrieved_at: str
    rows: tuple[_ModrinthRow, ...]


class _CurseRecord(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(extra="ignore")

    id: int
    file_name: str = Field(alias="fileName")
    file_length: int = Field(alias="fileLength")
    game_versions: tuple[str, ...] = Field(alias="gameVersions")
    release_type: int = Field(alias="releaseType")
    date_created: str = Field(alias="dateCreated")


class _CurseRow(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(extra="ignore")

    candidate_filename: str
    project_id: int
    file_id: int
    source_url: str
    file_page_url: str
    cdn_url: str
    record: _CurseRecord


class _CurseDiscovery(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(extra="ignore")

    retrieved_at: str
    rows: tuple[_CurseRow, ...]


_LOADER_LABELS = frozenset({"forge", "neoforge", "fabric", "quilt"})
_RELEASE_TYPES = {1: "release", 2: "beta", 3: "alpha"}


def build_source_matrix(
    inventory_path: Path,
    modrinth_path: Path,
    curseforge_path: Path,
) -> SourceMatrix:
    """Join the inventory to exact Modrinth or CurseForge records once each."""
    inventory = tuple(
        line.strip()
        for line in inventory_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    )
    modrinth = _ModrinthDiscovery.model_validate_json(modrinth_path.read_bytes())
    curseforge = _CurseDiscovery.model_validate_json(curseforge_path.read_bytes())
    resolved_modrinth = {row.candidate_filename: row for row in modrinth.rows if row.resolved}
    resolved_curseforge = {row.candidate_filename: row for row in curseforge.rows}
    resolved_names = set(resolved_modrinth) | set(resolved_curseforge)
    duplicates = set(resolved_modrinth) & set(resolved_curseforge)
    if duplicates or resolved_names != set(inventory) or len(inventory) != len(set(inventory)):
        missing = sorted(set(inventory) - resolved_names)
        extras = sorted(resolved_names - set(inventory))
        message = (
            f"invalid source join; missing={missing}, extras={extras}, "
            f"duplicates={sorted(duplicates)}"
        )
        raise SourceEvidenceError(message)
    candidates = tuple(
        _normalize_modrinth(resolved_modrinth[name], modrinth.retrieved_at)
        if name in resolved_modrinth
        else _normalize_curseforge(resolved_curseforge[name], curseforge.retrieved_at)
        for name in inventory
    )
    return SourceMatrix(
        schema_version="item3-source-identity-matrix-v1",
        target_minecraft="1.21.1",
        target_loader="neoforge",
        inventory_count=len(inventory),
        resolved_count=len(candidates),
        candidates=candidates,
    )


def _normalize_modrinth(row: _ModrinthRow, retrieved_at: str) -> SourceCandidate:
    if row.project is None or row.version is None or row.file is None:
        message = f"incomplete Modrinth row: {row.candidate_filename}"
        raise SourceEvidenceError(message)
    dependencies = tuple(
        SourceDependency(
            dependency_type=dependency.dependency_type,
            project_id=dependency.project_id,
            version_id=dependency.version_id,
        )
        for dependency in row.version.dependencies
    )
    return SourceCandidate(
        candidate_filename=row.candidate_filename,
        platform="modrinth",
        retrieved_at=retrieved_at,
        source_urls=(
            f"https://api.modrinth.com/v2/project/{row.project.id}",
            f"https://api.modrinth.com/v2/version/{row.version.id}",
            row.file.url,
        ),
        project=SourceProject(
            project_id=row.project.id,
            slug=row.project.slug,
            title=row.project.title,
            license_id=row.project.license.id,
            client_side=row.project.client_side,
            server_side=row.project.server_side,
        ),
        version=SourceVersion(
            version_id=row.version.id,
            name=row.version.name,
            version_number=row.version.version_number,
            published_at=row.version.date_published,
            release_type=row.version.version_type,
            dependencies=dependencies,
        ),
        artifact=SourceArtifact(
            file_id=row.file.id,
            exact_filename=row.file.filename,
            size_bytes=row.file.size,
            download_url=row.file.url,
            publisher_hashes=row.file.hashes,
        ),
        declared=SourceDeclaredCompatibility(
            game_versions=row.version.game_versions,
            loaders=row.version.loaders,
        ),
        limitations=(),
    )


def _normalize_curseforge(row: _CurseRow, retrieved_at: str) -> SourceCandidate:
    labels = row.record.game_versions
    loaders = tuple(label.lower() for label in labels if label.lower() in _LOADER_LABELS)
    versions = tuple(label for label in labels if label[0].isdigit())
    return SourceCandidate(
        candidate_filename=row.candidate_filename,
        platform="curseforge",
        retrieved_at=retrieved_at,
        source_urls=(row.source_url, row.file_page_url, row.cdn_url),
        project=SourceProject(
            project_id=str(row.project_id),
            slug=row.file_page_url.split("/files/", maxsplit=1)[0].rsplit("/", maxsplit=1)[-1],
            title=None,
            license_id=None,
            client_side="supported" if "Client" in labels else "unknown",
            server_side="supported" if "Server" in labels else "unknown",
        ),
        version=SourceVersion(
            version_id=str(row.file_id),
            name=row.record.file_name,
            version_number=str(row.file_id),
            published_at=row.record.date_created,
            release_type=_RELEASE_TYPES.get(row.record.release_type, "unknown"),
            dependencies=(),
        ),
        artifact=SourceArtifact(
            file_id=str(row.record.id),
            exact_filename=row.record.file_name,
            size_bytes=row.record.file_length,
            download_url=row.cdn_url,
            publisher_hashes={},
        ),
        declared=SourceDeclaredCompatibility(game_versions=versions, loaders=loaders),
        limitations=(
            "publisher_hashes_unavailable",
            "project_license_unavailable_from_file_endpoint",
            "dependency_metadata_unavailable_from_file_endpoint",
        ),
    )
