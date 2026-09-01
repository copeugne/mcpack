"""Persisted models for exact Item 3 JAR inspection evidence."""

from __future__ import annotations

from typing import ClassVar, Literal

from pydantic import BaseModel, ConfigDict, Field


class MetadataDocument(BaseModel):
    """Identity of one inspected metadata document inside a JAR."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    path: str
    size_bytes: int = Field(ge=0)
    sha256: str = Field(pattern=r"^[0-9a-f]{64}$")


class ModDeclaration(BaseModel):
    """One mod identity declared by top-level archive metadata."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    mod_id: str
    version: str
    display_name: str | None
    source_path: str


class DependencyDeclaration(BaseModel):
    """One normalized dependency edge from top-level archive metadata."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    owner_mod_id: str
    mod_id: str
    kind: str
    mandatory: bool | None
    version_ranges: tuple[str, ...]
    side: str
    ordering: str
    source_path: str


class EmbeddedLibrary(BaseModel):
    """Exact identity and optional JarJar coordinates for an embedded JAR."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    path: str
    size_bytes: int = Field(ge=0)
    sha256: str = Field(pattern=r"^[0-9a-f]{64}$")
    identifier: str | None
    artifact_version: str | None
    version_range: str | None
    nested_zip_integrity: Literal["pass", "fail"]
    nested_metadata_paths: tuple[str, ...]
    nested_mod_ids: tuple[str, ...]
    nested_dependencies: tuple[DependencyDeclaration, ...]
    nested_issues: tuple[str, ...]


class CandidateJarInspection(BaseModel):
    """Archive integrity and normalized metadata for one exact candidate."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    candidate_filename: str
    expected_sha256: str = Field(pattern=r"^[0-9a-f]{64}$")
    computed_sha256: str = Field(pattern=r"^[0-9a-f]{64}$")
    zip_integrity: Literal["pass", "fail"]
    inspection_status: Literal["pass", "fail"]
    archive_role: Literal["mod", "library", "unknown"]
    entry_count: int = Field(ge=0)
    duplicate_entry_count: int = Field(ge=0)
    unsafe_entries: tuple[str, ...]
    metadata_documents: tuple[MetadataDocument, ...]
    mod_loaders: tuple[str, ...]
    loader_ranges: tuple[str, ...]
    mods: tuple[ModDeclaration, ...]
    dependencies: tuple[DependencyDeclaration, ...]
    minecraft_ranges: tuple[str, ...]
    neoforge_ranges: tuple[str, ...]
    fabric_environment: str | None
    embedded_libraries: tuple[EmbeddedLibrary, ...]
    issues: tuple[str, ...]


class JarInspectionReport(BaseModel):
    """Complete Item 3 embedded-metadata inspection result."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    schema_version: Literal["item3-jar-inspection-v1"]
    generated_at: str
    candidate_count: int = Field(gt=0)
    all_inspections_passed: bool
    candidates: tuple[CandidateJarInspection, ...]
