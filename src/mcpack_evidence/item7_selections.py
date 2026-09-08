"""Declare the fixed Item 7 Chunky selection presets."""

from __future__ import annotations

from typing import ClassVar, Final, Literal

from pydantic import BaseModel, ConfigDict, Field, computed_field


class WorldgenSelection(BaseModel):
    """One fixed, completion-counted Chunky selection."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    label: Literal[
        "overworld",
        "nether",
        "end-central",
        "end-outer",
        "aether",
        "earth-orbit",
        "mars",
        "mars-orbit",
        "moon-orbit",
        "moon",
        "venus",
    ]
    dimension: Literal[
        "minecraft:overworld",
        "minecraft:the_nether",
        "minecraft:the_end",
        "aether:the_aether",
        "creatingspace:earth_orbit",
        "creatingspace:mars",
        "creatingspace:mars_orbit",
        "creatingspace:moon_orbit",
        "creatingspace:the_moon",
        "creatingspace:venus",
    ]
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

# Chunky uses inclusive odd-width squares. The +32 edge is generation halo,
# not part of Item 10's [-32, 31] census (outer End translates both axes by 512).
ITEM10_SELECTIONS: Final[tuple[WorldgenSelection, ...]] = tuple(
    WorldgenSelection.model_validate(
        {
            "label": label,
            "dimension": dimension,
            "center_x": center,
            "center_z": center,
            "radius_chunks": 32,
        }
    )
    for label, dimension, center in (
        ("aether", "aether:the_aether", 0),
        ("earth-orbit", "creatingspace:earth_orbit", 0),
        ("mars", "creatingspace:mars", 0),
        ("mars-orbit", "creatingspace:mars_orbit", 0),
        ("moon-orbit", "creatingspace:moon_orbit", 0),
        ("moon", "creatingspace:the_moon", 0),
        ("venus", "creatingspace:venus", 0),
        ("overworld", "minecraft:overworld", 0),
        ("end-central", "minecraft:the_end", 0),
        ("end-outer", "minecraft:the_end", 8192),
        ("nether", "minecraft:the_nether", 0),
    )
)
