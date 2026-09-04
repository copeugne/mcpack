from __future__ import annotations

from typing import cast

import pytest

from mcpack_evidence.item7_nbt_models import ChunkRecord, StructureBox, StructureStart
from mcpack_evidence.item8_world_bounds import observed_bounds


def record(boxes: tuple[StructureBox, ...]) -> ChunkRecord:
    return ChunkRecord(
        dimension="minecraft:overworld",
        region="region/r.0.0.mca",
        slot=0,
        timestamp=0,
        chunk_x=0,
        chunk_z=0,
        data_version=3955,
        status="minecraft:structure_starts",
        full=False,
        compression="zlib",
        external=False,
        heightmaps=(),
        biome_sections=(),
        structure_starts=(
            StructureStart(structure_id="example:tower", start_id="example:piece", boxes=boxes),
        ),
    )


def test_envelope_uses_all_pieces_inclusive_extents_and_preserves_nonfull_status() -> None:
    chunk = record(
        (
            StructureBox(bounds=(-10, -2, 5, 0, 4, 7)),
            StructureBox(bounds=(2, 3, -1, 8, 14, 6)),
        )
    )
    result = cast("dict[str, object]", observed_bounds(chunk)[0])
    assert result["envelope"] == [-10, -2, -1, 8, 14, 7]
    assert result["size_xyz"] == [19, 17, 9]
    assert result["chunk_full"] is False
    assert result["piece_boxes"] == [[-10, -2, 5, 0, 4, 7], [2, 3, -1, 8, 14, 6]]


def test_empty_start_remains_unknown_and_reversed_bounds_fail() -> None:
    result = cast("dict[str, object]", observed_bounds(record(()))[0])
    assert result["envelope"] is None
    assert result["size_xyz"] is None
    with pytest.raises(ValueError, match="reversed"):
        _ = observed_bounds(record((StructureBox(bounds=(2, 0, 0, 1, 1, 1)),)))
