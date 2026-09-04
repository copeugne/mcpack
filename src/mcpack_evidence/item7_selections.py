"""Declare the fixed Item 7 Chunky selection presets."""

from __future__ import annotations

from typing import ClassVar, Final, Literal

from pydantic import BaseModel, ConfigDict, Field, computed_field


class WorldgenSelection(BaseModel):
    """One fixed, completion-counted Chunky selection."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    label: Literal["overworld", "nether", "end-central", "end-outer"]
    dimension: Literal["minecraft:overworld", "minecraft:the_nether", "minecraft:the_end"]
    center_x: int
    center_z: int
    radius_chunks: int = Field(gt=0)

    @computed_field
    @property
    def expected_chunk_count(self) -> int:
        """Return Chunky's inclusive square chunk count."""
        return (self.radius_chunks * 2 + 1) ** 2


PILOT_SELECTIONS: Final[tuple[WorldgenSelection, ...]] = (
    WorldgenSelection(
        label="overworld", dimension="minecraft:overworld", center_x=0, center_z=0, radius_chunks=4
    ),
    WorldgenSelection(
        label="nether", dimension="minecraft:the_nether", center_x=0, center_z=0, radius_chunks=4
    ),
    WorldgenSelection(
        label="end-central", dimension="minecraft:the_end", center_x=0, center_z=0, radius_chunks=4
    ),
    WorldgenSelection(
        label="end-outer",
        dimension="minecraft:the_end",
        center_x=1536,
        center_z=0,
        radius_chunks=4,
    ),
)
CONTROL_SELECTIONS: Final[tuple[WorldgenSelection, ...]] = (PILOT_SELECTIONS[0],)
RUN_SELECTIONS: Final[tuple[WorldgenSelection, ...]] = (
    PILOT_SELECTIONS[0].model_copy(update={"radius_chunks": 31}),
    PILOT_SELECTIONS[1].model_copy(update={"radius_chunks": 15}),
    PILOT_SELECTIONS[2].model_copy(update={"radius_chunks": 15}),
    PILOT_SELECTIONS[3].model_copy(update={"radius_chunks": 15}),
)
