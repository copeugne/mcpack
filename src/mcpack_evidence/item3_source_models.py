"""Persisted models for Item 3 exact primary-source evidence."""

from __future__ import annotations

from typing import ClassVar, Literal

from pydantic import BaseModel, ConfigDict, Field


class SourceEvidenceError(ValueError):
    """Primary source records do not resolve the inventory exactly once."""


class SourceDependency(BaseModel):
    """One dependency edge declared by the publishing platform."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    dependency_type: str
    project_id: str | None
    version_id: str | None


class SourceProject(BaseModel):
    """Available publisher-level identity and environment metadata."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    project_id: str
    slug: str | None
    title: str | None
    license_id: str | None
    client_side: str
    server_side: str


class SourceVersion(BaseModel):
    """Available exact publisher-version metadata."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    version_id: str
    name: str
    version_number: str
    published_at: str
    release_type: str
    dependencies: tuple[SourceDependency, ...]


class SourceArtifact(BaseModel):
    """Exact downloadable file identity from its publishing platform."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    file_id: str
    exact_filename: str
    size_bytes: int = Field(ge=0)
    download_url: str
    publisher_hashes: dict[str, str]


class SourceDeclaredCompatibility(BaseModel):
    """Compatibility labels attached to the exact published file or version."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    game_versions: tuple[str, ...]
    loaders: tuple[str, ...]


class SourceCandidate(BaseModel):
    """Normalized exact source identity for one tentative candidate."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    candidate_filename: str
    platform: Literal["modrinth", "curseforge"]
    retrieved_at: str
    source_urls: tuple[str, ...]
    project: SourceProject
    version: SourceVersion
    artifact: SourceArtifact
    declared: SourceDeclaredCompatibility
    limitations: tuple[str, ...]


class SourceMatrix(BaseModel):
    """Complete exact-file primary-source matrix for the candidate inventory."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    schema_version: Literal["item3-source-identity-matrix-v1"]
    target_minecraft: Literal["1.21.1"]
    target_loader: Literal["neoforge"]
    inventory_count: int = Field(gt=0)
    resolved_count: int = Field(gt=0)
    candidates: tuple[SourceCandidate, ...]
