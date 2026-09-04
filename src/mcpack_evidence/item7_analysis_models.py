"""Typed identity and output models for Item 7 world analysis."""

from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar, Final, Literal, final, override

from pydantic import BaseModel, ConfigDict

type Status = Literal["observed", "method-limited", "unresolved"]


@final
class AnalysisError(Exception):
    """Decoded evidence cannot support the requested analysis."""

    __slots__: tuple[str, ...] = ("reason",)

    def __init__(self, reason: str) -> None:
        """Initialize the boundary failure with its audit-safe reason."""
        super().__init__(reason)
        self.reason: str = reason

    @override
    def __str__(self) -> str:
        return self.reason


@dataclass(frozen=True, slots=True)
class AnalysisIdentity:
    """Controlled-run identity for one analyzed selection."""

    run_id: str
    seed_role: str
    selection: str
    dimension: str


class _Frozen(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(extra="forbid", frozen=True, strict=True)


class Candidate(_Frozen):
    """One candidate signature, its measured value, and declared threshold."""

    identifier: str
    value: int
    threshold: int


class AnomalyMetric(_Frozen):
    """Candidate accounting for one anomaly class required by Item 7."""

    key: str
    status: Status
    candidate_count: int | None
    denominator_name: str | None
    denominator: int | None
    method: str
    candidates: tuple[Candidate, ...]


class BiomeMetric(_Frozen):
    """Surface-quart observations and component sizes for one biome."""

    biome: str
    quart_cells: int
    component_sizes: tuple[int, ...]


class Denominators(_Frozen):
    """Exact populations against which every candidate count is interpreted."""

    input_chunk_records: int
    chunk_count: int
    other_selection_chunk_records: int
    extra_chunk_records: int
    surface_block_cells: int
    surface_quart_cells: int
    void_surface_quart_cells: int
    height_adjacencies: int
    structure_starts: int
    structure_boxes: int
    structure_start_pairs: int
    cross_start_box_pairs: int
    structure_terrain_complete_starts: int
    structure_terrain_excluded_starts: int
    structure_modification_complete_starts: int
    structure_modification_excluded_starts: int


class WorldAnalysis(_Frozen):
    """Deterministic, input-bound metrics for one dimension selection."""

    schema_version: Literal["item7-world-analysis-v1"] = "item7-world-analysis-v1"
    input_protocol: Literal["item7-anvil-chunk-v1"] = "item7-anvil-chunk-v1"
    input_sha256: str
    run_id: str
    seed_role: str
    selection: str
    dimension: str
    denominators: Denominators
    biomes: tuple[BiomeMetric, ...]
    anomalies: tuple[AnomalyMetric, ...]


@dataclass(frozen=True, slots=True)
class AnomalySpec:
    """Stable protocol label, denominator, method, and coverage status."""

    key: str
    denominator_name: str
    method: str
    status: Status = "observed"


ANOMALY_SPECS: Final = (
    AnomalySpec(
        "fragmented_biomes",
        "biome_ids",
        "Biome IDs with multiple four-neighbor surface-quart components.",
    ),
    AnomalySpec(
        "tiny_biomes",
        "surface_quart_components",
        "Surface-quart components of four cells or fewer.",
    ),
    AnomalySpec(
        "unnatural_terrain_transitions",
        "height_adjacencies",
        "Orthogonal WORLD_SURFACE neighbors differing by at least 16 blocks.",
    ),
    AnomalySpec(
        "buried_structures",
        "complete_structure_footprints",
        "Structure top below median WORLD_SURFACE across its complete footprint.",
    ),
    AnomalySpec(
        "floating_structures",
        "complete_structure_footprints",
        "Post-placement WORLD_SURFACE cannot prove an air gap below a structure footprint.",
        "method-limited",
    ),
    AnomalySpec(
        "cliff_intersections",
        "complete_structure_footprints",
        "WORLD_SURFACE span across a complete structure footprint is at least 16 blocks.",
    ),
    AnomalySpec(
        "bad_underwater_placement",
        "complete_structure_footprints",
        "Child boxes intersect water columns from OCEAN_FLOOR through WORLD_SURFACE exclusive.",
    ),
    AnomalySpec(
        "overlapping_structures",
        "cross_start_box_pairs",
        "Exact inclusive three-dimensional child-box overlap volume.",
    ),
    AnomalySpec(
        "overlapping_villages",
        "structure_start_pairs",
        "Exact overlap where both IDs contain village, town, or ctov.",
    ),
    AnomalySpec(
        "failed_placements",
        "emitted_structure_starts",
        "Emitted INVALID or boxless starts; decoder omission of INVALID starts limits coverage.",
        "method-limited",
    ),
    AnomalySpec(
        "excessive_terrain_modification",
        "complete_structure_footprints_and_perimeters",
        "Complete-footprint to one-block-perimeter median WORLD_SURFACE delta of at least 16.",
    ),
)
