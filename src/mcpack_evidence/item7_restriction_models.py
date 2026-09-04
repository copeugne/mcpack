"""Strict models for the Item 7 packaged biome-restriction audit."""

from __future__ import annotations

from typing import ClassVar, Literal

from pydantic import BaseModel, ConfigDict


class RestrictionSource(BaseModel):
    """One hash-bound archive inspected by the audit."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid", strict=True)

    name: str
    sha256: str
    nested_archive: str | None


class RestrictionCandidate(BaseModel):
    """One structure whose packaged biome restriction cannot select a biome."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid", strict=True)

    source_archive: str
    structure_id: str
    biome_reference: str
    status: Literal["empty_tag", "missing_tag", "invalid_reference"]
    placement_sets: tuple[str, ...]
    missing_tags: tuple[str, ...]


class RestrictionAudit(BaseModel):
    """Complete retained-provider restriction inspection result."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid", strict=True)

    schema_version: Literal["item7-biome-restriction-audit-v1"]
    provider_catalog_sha256: str
    sources: tuple[RestrictionSource, ...]
    structure_count: int
    resolved_structure_count: int
    candidate_count: int
    active_candidate_count: int
    candidates: tuple[RestrictionCandidate, ...]
    exit_gate: Literal["PASS"]
    limitations: tuple[str, ...]
