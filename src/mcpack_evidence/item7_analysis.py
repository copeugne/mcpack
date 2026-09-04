"""Deterministic analysis of decoded Item 7 world evidence."""

from __future__ import annotations

from typing import TYPE_CHECKING

from mcpack_evidence.item7_analysis_input import collect_analysis_input
from mcpack_evidence.item7_analysis_metrics import (
    ComputedMetrics,
    MetricCandidate,
    compute_metrics,
)
from mcpack_evidence.item7_analysis_models import (
    ANOMALY_SPECS,
    AnalysisError,
    AnalysisIdentity,
    AnomalyMetric,
    BiomeMetric,
    Candidate,
    Denominators,
    WorldAnalysis,
)

if TYPE_CHECKING:
    from pathlib import Path


def _candidate(row: MetricCandidate) -> Candidate:
    return Candidate(identifier=row.identifier, value=row.value, threshold=row.threshold)


def _anomalies(metrics: ComputedMetrics, start_count: int) -> tuple[AnomalyMetric, ...]:
    groups = (
        metrics.fragmented,
        metrics.tiny,
        metrics.discontinuities,
        metrics.buried,
        metrics.floating,
        metrics.cliffs,
        metrics.underwater,
        metrics.overlaps,
        metrics.village_overlaps,
        metrics.failed,
        metrics.modification,
    )
    denominators = (
        len(metrics.biomes),
        sum(len(row.component_sizes) for row in metrics.biomes),
        metrics.height_adjacencies,
        metrics.complete_terrain_starts,
        metrics.complete_terrain_starts,
        metrics.complete_terrain_starts,
        metrics.complete_terrain_starts,
        metrics.cross_start_box_pairs,
        start_count * (start_count - 1) // 2,
        start_count,
        metrics.complete_modification_starts,
    )
    limited_keys: set[str] = set()
    if metrics.complete_terrain_starts != start_count:
        limited_keys.update(
            {
                "buried_structures",
                "floating_structures",
                "cliff_intersections",
                "bad_underwater_placement",
            }
        )
    if metrics.complete_modification_starts != start_count:
        limited_keys.add("excessive_terrain_modification")
    rows = tuple(
        AnomalyMetric(
            key=spec.key,
            status="method-limited" if spec.key in limited_keys else spec.status,
            candidate_count=len(group),
            denominator_name=spec.denominator_name,
            denominator=denominator,
            method=spec.method,
            candidates=tuple(_candidate(row) for row in group),
        )
        for spec, group, denominator in zip(ANOMALY_SPECS, groups, denominators, strict=True)
    )
    unresolved = AnomalyMetric(
        key="impossible_biome_restrictions",
        status="unresolved",
        candidate_count=None,
        denominator_name=None,
        denominator=None,
        method="Requires packaged biome-restriction inputs absent from decoded chunks.",
        candidates=(),
    )
    return (*rows[:10], unresolved, rows[10])


def analyze_jsonl(path: Path, identity: AnalysisIdentity, expected_sha256: str) -> WorldAnalysis:
    """Analyze one dimension selection and bind results to its decoded digest."""
    collected = collect_analysis_input(path, identity)
    if collected.input_sha256 != expected_sha256:
        message = "input hash mismatch"
        raise AnalysisError(message)
    metrics = compute_metrics(
        collected.heights, collected.floors, collected.biomes, collected.starts
    )
    start_count = len(collected.starts)
    pairs = start_count * (start_count - 1) // 2
    return WorldAnalysis(
        input_sha256=collected.input_sha256,
        run_id=identity.run_id,
        seed_role=identity.seed_role,
        selection=identity.selection,
        dimension=identity.dimension,
        denominators=Denominators(
            input_chunk_records=collected.input_chunk_records,
            chunk_count=len(collected.chunks),
            other_selection_chunk_records=collected.other_selection_chunk_records,
            extra_chunk_records=collected.extra_chunk_records,
            surface_block_cells=len(collected.heights),
            surface_quart_cells=len(collected.biomes),
            void_surface_quart_cells=collected.void_surface_quart_cells,
            height_adjacencies=metrics.height_adjacencies,
            structure_starts=start_count,
            structure_boxes=sum(len(row.boxes) for row in collected.starts),
            structure_start_pairs=pairs,
            cross_start_box_pairs=metrics.cross_start_box_pairs,
            structure_terrain_complete_starts=metrics.complete_terrain_starts,
            structure_terrain_excluded_starts=(start_count - metrics.complete_terrain_starts),
            structure_modification_complete_starts=metrics.complete_modification_starts,
            structure_modification_excluded_starts=(
                start_count - metrics.complete_modification_starts
            ),
        ),
        biomes=tuple(
            BiomeMetric(
                biome=row.biome, quart_cells=row.quart_cells, component_sizes=row.component_sizes
            )
            for row in metrics.biomes
        ),
        anomalies=_anomalies(metrics, start_count),
    )
