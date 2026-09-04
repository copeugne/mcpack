from __future__ import annotations

import hashlib
from typing import TYPE_CHECKING

import pytest

from mcpack_evidence.item7_analysis import analyze_jsonl
from mcpack_evidence.item7_analysis_models import AnalysisError, AnalysisIdentity
from mcpack_evidence.item7_nbt import (
    BiomeSection,
    ChunkRecord,
    Heightmap,
    StructureBox,
    StructureStart,
)

if TYPE_CHECKING:
    from pathlib import Path

type Bounds = tuple[int, int, int, int, int, int]


def _record(
    dimension: str, *, boxes: tuple[Bounds, ...] = (), duplicate_surface: bool = False
) -> ChunkRecord:
    surface = Heightmap(name="WORLD_SURFACE", values=(64,) * 256)
    floor = Heightmap(name="OCEAN_FLOOR", values=(64,) * 256)
    heightmaps = (surface, floor, surface) if duplicate_surface else (surface, floor)
    starts = (
        StructureStart(
            structure_id="example:test",
            start_id="test",
            boxes=tuple(StructureBox(bounds=box) for box in boxes),
        ),
    )
    return ChunkRecord(
        dimension=dimension,
        region="region/r.0.0.mca",
        slot=0,
        timestamp=1,
        chunk_x=0,
        chunk_z=0,
        data_version=4189,
        status="minecraft:full",
        full=True,
        compression="zlib",
        external=False,
        heightmaps=heightmaps,
        biome_sections=(
            BiomeSection(section_y=3, palette=("minecraft:plains",), indices=(0,) * 64),
        ),
        structure_starts=starts,
    )


def _write(path: Path, records: tuple[ChunkRecord, ...]) -> str:
    payload = "".join(f"{record.model_dump_json()}\n" for record in records)
    _ = path.write_text(payload, encoding="utf-8")
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _identity() -> AnalysisIdentity:
    return AnalysisIdentity("run-a", "ordinary", "overworld", "minecraft:overworld")


def test_analysis_validates_mapped_non_target_selection_rows(tmp_path: Path) -> None:
    # Given
    decoded = tmp_path / "chunks.jsonl"
    digest = _write(
        decoded,
        (
            _record("minecraft:overworld"),
            _record("minecraft:the_nether", duplicate_surface=True),
        ),
    )

    # When / Then
    with pytest.raises(AnalysisError, match="exactly one WORLD_SURFACE"):
        _ = analyze_jsonl(decoded, _identity(), digest)


def test_analysis_rejects_reversed_y_structure_bounds(tmp_path: Path) -> None:
    # Given
    decoded = tmp_path / "chunks.jsonl"
    digest = _write(decoded, (_record("minecraft:overworld", boxes=((0, 31, 0, 3, 30, 3),)),))

    # When / Then
    with pytest.raises(AnalysisError, match="reversed structure bounds"):
        _ = analyze_jsonl(decoded, _identity(), digest)
