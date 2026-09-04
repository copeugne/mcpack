"""Typed records emitted by the Item 7 NBT decoder."""

from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar, Literal

from pydantic import BaseModel, ConfigDict


class _FrozenModel(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")


class Heightmap(_FrozenModel):
    """One named decoded chunk heightmap."""

    name: str
    values: tuple[int, ...]


class BiomeSection(_FrozenModel):
    """One decoded vertical biome palette section."""

    section_y: int
    palette: tuple[str, ...]
    indices: tuple[int, ...]


class StructureBox(_FrozenModel):
    """One structure-piece bounding box."""

    bounds: tuple[int, int, int, int, int, int]


class StructureStart(_FrozenModel):
    """One decoded structure start and its piece boxes."""

    structure_id: str
    start_id: str
    boxes: tuple[StructureBox, ...]


class ChunkRecord(_FrozenModel):
    """One normalized Item 7 Anvil chunk record."""

    schema_version: Literal["item7-anvil-chunk-v1"] = "item7-anvil-chunk-v1"
    dimension: str
    region: str
    slot: int
    timestamp: int
    chunk_x: int
    chunk_z: int
    data_version: int | None
    status: str
    full: bool
    compression: Literal["gzip", "zlib", "raw", "lz4"]
    external: bool
    heightmaps: tuple[Heightmap, ...]
    biome_sections: tuple[BiomeSection, ...]
    structure_starts: tuple[StructureStart, ...]


@dataclass(frozen=True, slots=True)
class ChunkSource:
    """Transport identity and build geometry for one chunk payload."""

    dimension: str
    region: str
    slot: int
    timestamp: int
    compression: Literal["gzip", "zlib", "raw", "lz4"]
    external: bool
    min_y: int
    build_height: int
