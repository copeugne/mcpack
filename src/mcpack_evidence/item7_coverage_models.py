"""Strict models for Item 7 provider observation coverage."""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
from typing import TYPE_CHECKING, ClassVar, Literal

from pydantic import BaseModel, ConfigDict

if TYPE_CHECKING:
    from pathlib import Path

type ProviderRoleValue = Literal["direct_structure", "terrain_biome", "library"]


class CoverageError(ValueError):
    """Coverage evidence failed an identity or schema boundary."""


class CoverageStatus(StrEnum):
    """Evidence state for one exact retained provider component."""

    OBSERVED = "observed"
    UNOBSERVED = "unobserved"
    REQUIRES_TARGET = "requires_targeted_observation"


class FrozenModel(BaseModel):
    """Shared strict immutable evidence model."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid", strict=True)


class FirstCoordinate(FrozenModel):
    """First deterministic decoded coordinate supporting an observation."""

    input_path: str
    dimension: str
    chunk_x: int
    chunk_z: int


class Observation(FrozenModel):
    """One actual generated identifier with its count and first coordinate."""

    identifier: str
    kind: Literal["structure_start", "biome_quart"]
    count: int
    first_coordinate: FirstCoordinate


class ComponentCoverage(FrozenModel):
    """Coverage result for one exact catalog component."""

    candidate_filename: str
    mod_id: str
    role: ProviderRoleValue
    sha256: str
    packaged_structure_ids: tuple[str, ...]
    observations: tuple[Observation, ...]
    status: CoverageStatus
    target_requirement: (
        Literal[
            "catalog_and_targeted_generated_output",
            "catalog_registry_and_generated_consumer_output",
        ]
        | None
    )


class LabelCoverage(FrozenModel):
    """Coverage results for every component under one Item 7 label."""

    label: str
    role: ProviderRoleValue
    components: tuple[ComponentCoverage, ...]


class InputIdentity(FrozenModel):
    """Relative paths and hashes binding one decoded input to its manifest."""

    manifest_path: str
    manifest_sha256: str
    decoded_path: str
    decoded_sha256: str
    record_count: int


class CoverageReport(FrozenModel):
    """Stable coverage evidence for all frozen Item 7 provider components."""

    schema_version: Literal["item7-provider-observation-coverage-v1"]
    provider_catalog_path: str
    provider_catalog_sha256: str
    inputs: tuple[InputIdentity, ...]
    labels: tuple[LabelCoverage, ...]
    missing: tuple[str, ...]


class DecodedSeal(FrozenModel):
    """World-manifest identity for one decoded JSONL."""

    path: str
    size_bytes: int
    sha256: str
    record_count: int


class WorldManifest(BaseModel):
    """Identity-bearing subset of the strict Item 7 world manifest."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="ignore", strict=True)
    schema_version: Literal["item7-world-manifest-v1"]
    decoded: DecodedSeal


@dataclass(frozen=True, slots=True)
class DecodedInput:
    """Resolved decoded input with its public relative identity."""

    path: Path
    display: str
    seal: DecodedSeal
    identity: InputIdentity


@dataclass(frozen=True, slots=True)
class Observed:
    """Mutable dictionaries accumulated only during one streaming summary."""

    structure_counts: dict[str, int]
    structure_first: dict[str, FirstCoordinate]
    biome_counts: dict[str, int]
    biome_first: dict[str, FirstCoordinate]
