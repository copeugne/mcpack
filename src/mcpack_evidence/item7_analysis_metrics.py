"""Pure grid and structure metrics for Item 7 evidence analysis."""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from statistics import median_low
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Mapping

type Point = tuple[int, int]
type Bounds = tuple[int, int, int, int, int, int]
_HEIGHT_DELTA = 16
_TINY_COMPONENT = 4


@dataclass(frozen=True, slots=True)
class MetricCandidate:
    """One threshold crossing with its stable evidence identifier."""

    identifier: str
    value: int
    threshold: int


@dataclass(frozen=True, slots=True)
class BiomeCount:
    """Surface-quart count and connected-component sizes for one biome."""

    biome: str
    quart_cells: int
    component_sizes: tuple[int, ...]


@dataclass(frozen=True, slots=True)
class ObservedStart:
    """One decoded structure start and its child bounding boxes."""

    identifier: str
    structure_id: str
    start_id: str
    boxes: tuple[Bounds, ...]


@dataclass(frozen=True, slots=True)
class ComputedMetrics:
    """Complete deterministic metric set consumed by the evidence boundary."""

    biomes: tuple[BiomeCount, ...]
    height_adjacencies: int
    cross_start_box_pairs: int
    complete_terrain_starts: int
    complete_modification_starts: int
    fragmented: tuple[MetricCandidate, ...]
    tiny: tuple[MetricCandidate, ...]
    discontinuities: tuple[MetricCandidate, ...]
    buried: tuple[MetricCandidate, ...]
    floating: tuple[MetricCandidate, ...]
    cliffs: tuple[MetricCandidate, ...]
    underwater: tuple[MetricCandidate, ...]
    overlaps: tuple[MetricCandidate, ...]
    village_overlaps: tuple[MetricCandidate, ...]
    failed: tuple[MetricCandidate, ...]
    modification: tuple[MetricCandidate, ...]


def _candidate(identifier: str, value: int, threshold: int) -> MetricCandidate:
    return MetricCandidate(identifier, value, threshold)


def _components(cells: Mapping[Point, str]) -> tuple[BiomeCount, ...]:
    by_biome: dict[str, set[Point]] = defaultdict(set)
    for point, biome in cells.items():
        by_biome[biome].add(point)
    rows: list[BiomeCount] = []
    for biome in sorted(by_biome):
        pending = set(by_biome[biome])
        sizes: list[int] = []
        while pending:
            first = min(pending)
            pending.remove(first)
            frontier = [first]
            size = 0
            while frontier:
                x, z = frontier.pop()
                size += 1
                for neighbor in ((x - 1, z), (x + 1, z), (x, z - 1), (x, z + 1)):
                    if neighbor in pending:
                        pending.remove(neighbor)
                        frontier.append(neighbor)
            sizes.append(size)
        ordered = tuple(sorted(sizes))
        rows.append(BiomeCount(biome, sum(ordered), ordered))
    return tuple(rows)


def _covered_points(
    heights: Mapping[Point, int], boxes: tuple[Bounds, ...]
) -> tuple[set[Point], bool]:
    covered: set[Point] = set()
    complete = bool(boxes)
    for box in boxes:
        if any(box[index] > box[index + 3] for index in range(3)):
            complete = False
            continue
        for x in range(box[0], box[3] + 1):
            for z in range(box[2], box[5] + 1):
                point = (x, z)
                if point in heights:
                    covered.add(point)
                else:
                    complete = False
    return covered, complete


def _water_points(
    start: ObservedStart,
    heights: Mapping[Point, int],
    floors: Mapping[Point, int],
) -> set[Point]:
    points: set[Point] = set()
    for box in start.boxes:
        for x in range(box[0], box[3] + 1):
            for z in range(box[2], box[5] + 1):
                point = (x, z)
                if (
                    heights[point] > floors[point]
                    and box[1] < heights[point]
                    and box[4] >= floors[point]
                ):
                    points.add(point)
    return points


def _terrain(
    heights: Mapping[Point, int],
    floors: Mapping[Point, int],
    starts: tuple[ObservedStart, ...],
) -> tuple[tuple[tuple[MetricCandidate, ...], ...], int, int]:
    groups: tuple[list[MetricCandidate], ...] = ([], [], [], [], [])
    buried, _floating, cliffs, underwater, modification = groups
    complete_count = 0
    modification_count = 0
    for start in starts:
        covered, complete = _covered_points(heights, start.boxes)
        if not complete:
            continue
        complete_count += 1
        values = [heights[point] for point in covered]
        terrain = median_low(values)
        maximum_y = max(box[4] for box in start.boxes)
        if maximum_y < terrain:
            buried.append(_candidate(start.identifier, terrain - maximum_y, 1))
        span = max(values) - min(values)
        if span >= _HEIGHT_DELTA:
            cliffs.append(_candidate(start.identifier, span, _HEIGHT_DELTA))
        water_cells = len(_water_points(start, heights, floors))
        if water_cells:
            underwater.append(_candidate(start.identifier, water_cells, 1))
        ring, ring_complete = _perimeter(heights, covered)
        if ring_complete:
            modification_count += 1
        if ring and ring_complete:
            delta = abs(terrain - median_low([heights[point] for point in ring]))
            if delta >= _HEIGHT_DELTA:
                modification.append(_candidate(start.identifier, delta, _HEIGHT_DELTA))
    return tuple(tuple(rows) for rows in groups), complete_count, modification_count


def _perimeter(heights: Mapping[Point, int], covered: set[Point]) -> tuple[set[Point], bool]:
    ring: set[Point] = set()
    complete = True
    for x, z in covered:
        for neighbor in ((x - 1, z), (x + 1, z), (x, z - 1), (x, z + 1)):
            if neighbor in covered:
                continue
            if neighbor in heights:
                ring.add(neighbor)
            else:
                complete = False
    return ring, complete


def _overlaps(
    starts: tuple[ObservedStart, ...],
) -> tuple[tuple[MetricCandidate, ...], tuple[MetricCandidate, ...], int]:
    overlaps: list[MetricCandidate] = []
    villages: list[MetricCandidate] = []
    box_pairs = 0
    tokens = ("village", "town", "ctov")
    for left_index, left in enumerate(starts):
        for right in starts[left_index + 1 :]:
            box_pairs += len(left.boxes) * len(right.boxes)
            village_like = all(
                any(token in row.structure_id.lower() for token in tokens) for row in (left, right)
            )
            village_volume = 0
            for a_index, a in enumerate(left.boxes):
                for b_index, b in enumerate(right.boxes):
                    lengths = tuple(
                        max(0, min(a[i + 3], b[i + 3]) - max(a[i], b[i]) + 1) for i in range(3)
                    )
                    volume = lengths[0] * lengths[1] * lengths[2]
                    if volume:
                        identifier = f"{left.identifier}#{a_index}|{right.identifier}#{b_index}"
                        overlaps.append(_candidate(identifier, volume, 1))
                        village_volume += volume
            if village_like and village_volume:
                identifier = f"{left.identifier}|{right.identifier}"
                villages.append(_candidate(identifier, village_volume, 1))
    return tuple(overlaps), tuple(villages), box_pairs


def compute_metrics(
    heights: Mapping[Point, int],
    floors: Mapping[Point, int],
    biome_cells: Mapping[Point, str],
    starts: tuple[ObservedStart, ...],
) -> ComputedMetrics:
    """Compute every Item 7 candidate metric without making severity claims."""
    biome_rows = _components(biome_cells)
    fragmented = tuple(
        _candidate(row.biome, len(row.component_sizes), 2)
        for row in biome_rows
        if len(row.component_sizes) > 1
    )
    tiny = tuple(
        _candidate(f"{row.biome}#{index}", size, 4)
        for row in biome_rows
        for index, size in enumerate(row.component_sizes)
        if size <= _TINY_COMPONENT
    )
    discontinuities: list[MetricCandidate] = []
    adjacency_count = 0
    for point, height in sorted(heights.items()):
        for neighbor in ((point[0] + 1, point[1]), (point[0], point[1] + 1)):
            if neighbor in heights:
                adjacency_count += 1
                delta = abs(height - heights[neighbor])
                if delta >= _HEIGHT_DELTA:
                    identifier = f"{point[0]},{point[1]}:{neighbor[0]},{neighbor[1]}"
                    discontinuities.append(_candidate(identifier, delta, _HEIGHT_DELTA))
    ordered_starts = tuple(sorted(starts, key=lambda row: row.identifier))
    terrain_groups, complete_count, modification_count = _terrain(heights, floors, ordered_starts)
    buried, floating, cliffs, underwater, modification = terrain_groups
    overlaps, villages, box_pairs = _overlaps(ordered_starts)
    failed = tuple(
        _candidate(row.identifier, len(row.boxes), 1)
        for row in ordered_starts
        if row.start_id == "INVALID" or not row.boxes
    )
    return ComputedMetrics(
        biome_rows,
        adjacency_count,
        box_pairs,
        complete_count,
        modification_count,
        fragmented,
        tiny,
        tuple(discontinuities),
        buried,
        floating,
        cliffs,
        underwater,
        overlaps,
        villages,
        failed,
        modification,
    )
