"""Strict adapter from decoded Anvil JSONL to Item 7 render records."""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from typing import TYPE_CHECKING, ClassVar, Final, Literal

from pydantic import BaseModel, ConfigDict, ValidationError, field_validator

_CELLS: Final = 16 * 16
_BIOME_CELLS: Final = 4 * 4 * 4
_INPUT_HASH_MESSAGE: Final = "render input hash mismatch"
_DIMENSION_MESSAGE: Final = "decoded input dimension does not match render metadata"
_COORDINATE_MESSAGE: Final = "decoded input repeats a chunk coordinate"
_CHUNKS_MESSAGE: Final = "decoded input requires one or more full chunks"
_HEIGHTMAP_MESSAGE: Final = "decoded input misses required render heightmap"

if TYPE_CHECKING:
    from pathlib import Path


class RenderInputError(ValueError):
    """The decoded evidence cannot support a trustworthy inspection render."""


class _Record(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(extra="allow", frozen=True, strict=True)

    schema_version: Literal["item7-anvil-chunk-v1"]
    dimension: str
    chunk_x: int
    chunk_z: int
    status: Literal["minecraft:full"]
    full: Literal[True]
    heightmaps: tuple[_NamedValues, ...]
    biome_sections: tuple[_BiomeSection, ...]
    structure_starts: tuple[_StructureStart, ...]


class _NamedValues(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(extra="forbid", frozen=True, strict=True)

    name: str
    values: tuple[int, ...]

    @field_validator("values")
    @classmethod
    def _has_block_grid(cls, values: tuple[int, ...]) -> tuple[int, ...]:
        if len(values) != _CELLS:
            message = "heightmap must contain exactly 256 block values"
            raise ValueError(message)
        return values


class _BiomeSection(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(extra="forbid", frozen=True, strict=True)

    section_y: int
    palette: tuple[str, ...]
    indices: tuple[int, ...]

    @field_validator("indices")
    @classmethod
    def _has_quart_grid(cls, values: tuple[int, ...]) -> tuple[int, ...]:
        if len(values) != _BIOME_CELLS:
            message = "biome section must contain exactly 64 quart values"
            raise ValueError(message)
        return values


class _Box(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(extra="forbid", frozen=True, strict=True)

    bounds: tuple[int, int, int, int, int, int]


class _StructureStart(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(extra="forbid", frozen=True, strict=True)

    structure_id: str
    start_id: str
    boxes: tuple[_Box, ...]


@dataclass(frozen=True, slots=True)
class RenderMetadata:
    """Run identity supplied by the controlled runtime protocol."""

    run_id: str
    seed_role: str
    seed: str
    dimension: str
    region_hashes: dict[str, str]


@dataclass(frozen=True, slots=True)
class RenderChunk:
    """Only decoded fields that support an honest elevation or placement view."""

    chunk_x: int
    chunk_z: int
    world_surface: tuple[int, ...]
    ocean_floor: tuple[int, ...]
    biome_sections: tuple[_BiomeSection, ...]
    structures: tuple[_StructureStart, ...]


@dataclass(frozen=True, slots=True)
class RenderInput:
    """A complete rendered selection bound to the raw decoded JSONL hash."""

    metadata: RenderMetadata
    chunks: tuple[RenderChunk, ...]
    chunks_sha256: str


def parse_input(path: Path, metadata: RenderMetadata, expected_sha256: str | None) -> RenderInput:
    """Parse Anvil rows, reject stale JSONL, and require one dimension and coordinate each."""
    actual_sha256 = sha256(path)
    if expected_sha256 is not None and actual_sha256 != expected_sha256:
        raise RenderInputError(_INPUT_HASH_MESSAGE)
    coordinates: set[tuple[int, int]] = set()
    chunks: list[RenderChunk] = []
    try:
        with path.open(encoding="utf-8") as stream:
            for number, line in enumerate(stream, start=1):
                if not line.strip():
                    continue
                try:
                    record = _Record.model_validate_json(line)
                except ValidationError as error:
                    message = f"invalid decoded JSONL record at line {number}"
                    raise RenderInputError(message) from error
                if record.dimension != metadata.dimension:
                    raise RenderInputError(_DIMENSION_MESSAGE)
                coordinate = (record.chunk_x, record.chunk_z)
                if coordinate in coordinates:
                    raise RenderInputError(_COORDINATE_MESSAGE)
                coordinates.add(coordinate)
                chunks.append(_render_chunk(record))
    except (OSError, UnicodeError) as error:
        message = f"cannot read decoded chunks: {path}"
        raise RenderInputError(message) from error
    if not chunks:
        raise RenderInputError(_CHUNKS_MESSAGE)
    return RenderInput(
        metadata, tuple(sorted(chunks, key=lambda row: (row.chunk_z, row.chunk_x))), actual_sha256
    )


def _render_chunk(record: _Record) -> RenderChunk:
    heights = {row.name.lower(): row.values for row in record.heightmaps}
    try:
        world_surface = heights["world_surface"]
        ocean_floor = heights["ocean_floor"]
    except KeyError as error:
        raise RenderInputError(_HEIGHTMAP_MESSAGE) from error
    return RenderChunk(
        record.chunk_x,
        record.chunk_z,
        world_surface,
        ocean_floor,
        tuple(sorted(record.biome_sections, key=lambda row: row.section_y)),
        record.structure_starts,
    )


def sha256(path: Path) -> str:
    """Return a streaming SHA-256 digest for one raw evidence artifact."""
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()
