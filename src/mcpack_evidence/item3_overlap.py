"""Classify embedded-library overlap and nested mod-ID collisions for Item 3."""

from __future__ import annotations

from collections import defaultdict
from typing import TYPE_CHECKING, ClassVar, Literal

from pydantic import BaseModel, ConfigDict

if TYPE_CHECKING:
    from mcpack_evidence.item3_jar_models import JarInspectionReport


class EmbeddedOccurrence(BaseModel):
    """One embedded artifact occurrence inside an outer candidate."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    candidate_filename: str
    path: str
    identifier: str | None
    artifact_version: str | None
    version_range: str | None
    sha256: str
    nested_mod_ids: tuple[str, ...]


class OverlapGroup(BaseModel):
    """All occurrences and applicable overlap classes for one coordinate."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    identifier: str
    occurrences: tuple[EmbeddedOccurrence, ...]
    classifications: tuple[
        Literal["identical_bytes", "same_version_different_bytes", "multiple_versions"], ...
    ]


class ModIdCollision(BaseModel):
    """A mod ID provided by multiple outer or nested providers."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    mod_id: str
    providers: tuple[str, ...]


class OverlapReport(BaseModel):
    """Complete embedded-overlap report for a candidate inspection."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    schema_version: Literal["item3-embedded-overlap-v1"]
    candidate_count: int
    embedded_occurrence_count: int
    coordinate_groups: tuple[OverlapGroup, ...]
    mod_id_collisions: tuple[ModIdCollision, ...]
    limitations: tuple[str, ...]


def build_overlap_report(inspection: JarInspectionReport) -> OverlapReport:
    """Group embedded coordinates and identify deterministic overlap hazards."""
    occurrences = tuple(
        EmbeddedOccurrence(
            candidate_filename=candidate.candidate_filename,
            path=library.path,
            identifier=library.identifier,
            artifact_version=library.artifact_version,
            version_range=library.version_range,
            sha256=library.sha256,
            nested_mod_ids=library.nested_mod_ids,
        )
        for candidate in inspection.candidates
        for library in candidate.embedded_libraries
    )
    coordinates: dict[str, list[EmbeddedOccurrence]] = defaultdict(list)
    for occurrence in occurrences:
        if occurrence.identifier is not None:
            coordinates[occurrence.identifier].append(occurrence)
    groups = tuple(
        _group(identifier, tuple(rows))
        for identifier, rows in sorted(coordinates.items())
        if len(rows) > 1
    )
    providers: dict[str, set[str]] = defaultdict(set)
    for candidate in inspection.candidates:
        for mod in candidate.mods:
            if mod.source_path == "META-INF/neoforge.mods.toml":
                providers[mod.mod_id].add(f"outer:{candidate.candidate_filename}")
        for library in candidate.embedded_libraries:
            if "META-INF/neoforge.mods.toml" not in library.nested_metadata_paths:
                continue
            for mod_id in library.nested_mod_ids:
                providers[mod_id].add(f"nested:{candidate.candidate_filename}!/{library.path}")
    collisions = tuple(
        ModIdCollision(mod_id=mod_id, providers=tuple(sorted(rows)))
        for mod_id, rows in sorted(providers.items())
        if len(rows) > 1
    )
    return OverlapReport(
        schema_version="item3-embedded-overlap-v1",
        candidate_count=inspection.candidate_count,
        embedded_occurrence_count=len(occurrences),
        coordinate_groups=groups,
        mod_id_collisions=collisions,
        limitations=(
            "Negotiated Jar-in-Jar selection requires the focused runtime cluster tests.",
            (
                "Artifacts without JarJar coordinates are inventoried but cannot be grouped "
                "by coordinate."
            ),
        ),
    )


def _group(identifier: str, rows: tuple[EmbeddedOccurrence, ...]) -> OverlapGroup:
    classifications: list[
        Literal["identical_bytes", "same_version_different_bytes", "multiple_versions"]
    ] = []
    versions: dict[str | None, set[str]] = defaultdict(set)
    for row in rows:
        versions[row.artifact_version].add(row.sha256)
    if len({row.sha256 for row in rows}) < len(rows):
        classifications.append("identical_bytes")
    if any(len(hashes) > 1 for hashes in versions.values()):
        classifications.append("same_version_different_bytes")
    if len(versions) > 1:
        classifications.append("multiple_versions")
    return OverlapGroup(
        identifier=identifier,
        occurrences=rows,
        classifications=tuple(classifications),
    )
