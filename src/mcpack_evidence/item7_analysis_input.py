"""Fail-closed aggregate input collection for Item 7 selection analysis."""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from typing import TYPE_CHECKING, final

from pydantic import ValidationError

from mcpack_evidence.item7_analysis_metrics import ObservedStart
from mcpack_evidence.item7_analysis_models import AnalysisError, AnalysisIdentity
from mcpack_evidence.item7_nbt import ChunkRecord
from mcpack_evidence.item7_selections import RUN_SELECTIONS

if TYPE_CHECKING:
    from pathlib import Path

    from mcpack_evidence.item7_selections import WorldgenSelection

type Point = tuple[int, int]
_BLOCK_CELLS = 256
_BIOME_CELLS = 64


@dataclass(frozen=True, slots=True)
class AnalysisInput:
    """One hash-bound fixed selection collected from aggregate decoded rows."""

    heights: dict[Point, int]
    floors: dict[Point, int]
    biomes: dict[Point, str]
    starts: tuple[ObservedStart, ...]
    chunks: frozenset[Point]
    input_sha256: str
    input_chunk_records: int
    other_selection_chunk_records: int
    extra_chunk_records: int
    void_surface_quart_cells: int


@final
class _Accumulator:
    """Accumulate one streaming parse through intentional local mutation."""

    __slots__ = (
        "biomes",
        "chunks",
        "extra_count",
        "floors",
        "heights",
        "input_count",
        "other_count",
        "seen",
        "starts",
        "void_quart_count",
    )

    def __init__(self) -> None:
        self.heights: dict[Point, int] = {}
        self.floors: dict[Point, int] = {}
        self.biomes: dict[Point, str] = {}
        self.starts: list[ObservedStart] = []
        self.chunks: set[Point] = set()
        self.seen: set[tuple[str, int, int]] = set()
        self.input_count = 0
        self.other_count = 0
        self.extra_count = 0
        self.void_quart_count = 0


def _requested(identity: AnalysisIdentity) -> WorldgenSelection:
    matches = tuple(row for row in RUN_SELECTIONS if row.label == identity.selection)
    if len(matches) != 1 or matches[0].dimension != identity.dimension:
        message = "analysis identity does not match a frozen selection"
        raise AnalysisError(message)
    return matches[0]


def _owner(record: ChunkRecord) -> WorldgenSelection | None:
    dimensions = {row.dimension for row in RUN_SELECTIONS}
    if record.dimension not in dimensions:
        message = f"unknown dimension: {record.dimension}"
        raise AnalysisError(message)
    matches = tuple(
        row
        for row in RUN_SELECTIONS
        if row.dimension == record.dimension
        and abs(record.chunk_x - row.center_x // 16) <= row.radius_chunks
        and abs(record.chunk_z - row.center_z // 16) <= row.radius_chunks
    )
    if len(matches) > 1:
        message = f"chunk {record.chunk_x},{record.chunk_z} maps to overlapping selections"
        raise AnalysisError(message)
    return matches[0] if matches else None


def _heightmap(record: ChunkRecord, name: str) -> tuple[int, ...]:
    matches = tuple(row.values for row in record.heightmaps if row.name == name)
    if len(matches) != 1 or len(matches[0]) != _BLOCK_CELLS:
        message = f"chunk {record.chunk_x},{record.chunk_z} requires exactly one {name}"
        raise AnalysisError(message)
    return matches[0]


def _surface_biome(record: ChunkRecord, height: int, quart_x: int, quart_z: int) -> str | None:
    surface_y = height - 1
    section_y = surface_y // 16
    matches = tuple(row for row in record.biome_sections if row.section_y == section_y)
    minimum_section = min((row.section_y for row in record.biome_sections), default=section_y)
    if not matches and section_y < minimum_section:
        return None
    if len(matches) != 1 or len(matches[0].indices) != _BIOME_CELLS:
        message = f"chunk {record.chunk_x},{record.chunk_z} requires biome section {section_y}"
        raise AnalysisError(message)
    section = matches[0]
    if any(index < 0 or index >= len(section.palette) for index in section.indices):
        message = f"chunk {record.chunk_x},{record.chunk_z} has invalid biome index"
        raise AnalysisError(message)
    index = ((surface_y % 16) // 4) * 16 + quart_z * 4 + quart_x
    return section.palette[section.indices[index]]


def _validate_mapped(record: ChunkRecord) -> None:
    surface = _heightmap(record, "WORLD_SURFACE")
    _ = _heightmap(record, "OCEAN_FLOOR")
    for z in range(4):
        for x in range(4):
            height = surface[(z * 4 + 2) * 16 + x * 4 + 2]
            _ = _surface_biome(record, height, x, z)
    for start in record.structure_starts:
        for box in start.boxes:
            if any(box.bounds[index] > box.bounds[index + 3] for index in range(3)):
                message = f"chunk {record.chunk_x},{record.chunk_z} has reversed structure bounds"
                raise AnalysisError(message)


def _add_selected(record: ChunkRecord, rows: _Accumulator) -> None:
    rows.chunks.add((record.chunk_x, record.chunk_z))
    surface, floor = _heightmap(record, "WORLD_SURFACE"), _heightmap(record, "OCEAN_FLOOR")
    for z in range(16):
        for x in range(16):
            point = (record.chunk_x * 16 + x, record.chunk_z * 16 + z)
            rows.heights[point], rows.floors[point] = surface[z * 16 + x], floor[z * 16 + x]
    for z in range(4):
        for x in range(4):
            point = (record.chunk_x * 4 + x, record.chunk_z * 4 + z)
            height = surface[(z * 4 + 2) * 16 + x * 4 + 2]
            biome = _surface_biome(record, height, x, z)
            if biome is None:
                rows.void_quart_count += 1
            else:
                rows.biomes[point] = biome
    for start in record.structure_starts:
        identifier = f"{record.chunk_x},{record.chunk_z}:{start.structure_id}:{start.start_id}"
        rows.starts.append(
            ObservedStart(
                identifier,
                start.structure_id,
                start.start_id,
                tuple(box.bounds for box in start.boxes),
            )
        )


def _add_record(
    record: ChunkRecord, number: int, selected: WorldgenSelection, rows: _Accumulator
) -> None:
    key = (record.dimension, record.chunk_x, record.chunk_z)
    if key in rows.seen:
        message = f"line {number} repeats chunk {key}"
        raise AnalysisError(message)
    rows.seen.add(key)
    rows.input_count += 1
    owner = _owner(record)
    if owner is None:
        rows.extra_count += 1
        return
    if record.status != "minecraft:full" or not record.full:
        message = f"line {number} maps to a selection but is not a full chunk"
        raise AnalysisError(message)
    _validate_mapped(record)
    if owner.label != selected.label:
        rows.other_count += 1
        return
    _add_selected(record, rows)


def collect_analysis_input(path: Path, identity: AnalysisIdentity) -> AnalysisInput:
    """Hash every aggregate byte while collecting one exact frozen selection."""
    rows = _Accumulator()
    digest = hashlib.sha256()
    selected = _requested(identity)
    try:
        with path.open("rb") as stream:
            for number, raw_line in enumerate(stream, start=1):
                digest.update(raw_line)
                if not raw_line.strip():
                    continue
                _add_record(ChunkRecord.model_validate_json(raw_line), number, selected, rows)
    except (OSError, ValidationError) as error:
        message = f"invalid decoded input: {path}"
        raise AnalysisError(message) from error
    if not rows.chunks:
        message = "decoded input contains no selected chunks"
        raise AnalysisError(message)
    return AnalysisInput(
        rows.heights,
        rows.floors,
        rows.biomes,
        tuple(rows.starts),
        frozenset(rows.chunks),
        digest.hexdigest(),
        rows.input_count,
        rows.other_count,
        rows.extra_count,
        rows.void_quart_count,
    )
