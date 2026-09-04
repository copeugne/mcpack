from __future__ import annotations

import hashlib
import json
from typing import TYPE_CHECKING

import pytest
from pydantic import JsonValue
from tools.analyze_item7_world import main

from mcpack_evidence.item7_analysis import analyze_jsonl
from mcpack_evidence.item7_analysis_models import AnalysisError, AnalysisIdentity
from mcpack_evidence.item7_nbt import ChunkRecord

if TYPE_CHECKING:
    from collections.abc import Sequence
    from pathlib import Path


def _json_list(values: Sequence[int | str]) -> list[JsonValue]:
    return list[JsonValue](values)


def _structure(structure_id: str, start_id: str, boxes: list[list[int]]) -> JsonValue:
    box_rows: list[JsonValue] = []
    for box in boxes:
        box_row: dict[str, JsonValue] = {"bounds": _json_list(box)}
        box_rows.append(box_row)
    return {
        "structure_id": structure_id,
        "start_id": start_id,
        "boxes": box_rows,
    }


def _record(
    chunk_x: int,
    *,
    dimension: str = "minecraft:overworld",
    malformed: bool = False,
    void: bool = False,
) -> str:
    surface = [-1 if void else 64] * 256
    floor = [64] * 256
    if chunk_x == 0:
        surface[15] = 96
        surface[68] = 96
        surface[17] = 70
        floor[17] = 60
        for z in range(11, 13):
            for x in range(11, 13):
                surface[z * 16 + x] = 96
    palette = ["minecraft:plains", "minecraft:forest", "minecraft:desert"]
    indices = [0] * 64
    if chunk_x == 0:
        indices[0], indices[2], indices[10] = 1, 1, 2
    structures: list[JsonValue] = []
    if chunk_x == 0:
        structures = [
            _structure("example:buried", "buried", [[0, 20, 0, 3, 30, 3]]),
            _structure("example:floating", "floating", [[4, 90, 0, 7, 95, 3]]),
            _structure("ctov:village_a", "village-a", [[1, 60, 1, 5, 75, 5]]),
            _structure("example:village_b", "village-b", [[4, 60, 4, 8, 75, 8]]),
            _structure("example:modified", "modified", [[11, 60, 11, 12, 100, 12]]),
            _structure(
                "example:split",
                "split",
                [[1, 0, 1, 1, 10, 1], [9, 80, 9, 9, 90, 9]],
            ),
            _structure("example:edge", "edge", [[-1, 60, 8, 1, 70, 9]]),
            _structure("example:missing", "missing", []),
        ]
    heightmaps: list[JsonValue] = []
    surface_row: dict[str, JsonValue] = {
        "name": "WORLD_SURFACE",
        "values": _json_list(surface),
    }
    floor_row: dict[str, JsonValue] = {
        "name": "OCEAN_FLOOR",
        "values": _json_list(floor),
    }
    heightmaps.extend((surface_row, floor_row))
    biome_row: dict[str, JsonValue] = {
        "section_y": 0 if void else 4,
        "palette": _json_list(palette),
        "indices": _json_list(indices),
    }
    row: dict[str, JsonValue] = {
        "schema_version": "wrong" if malformed else "item7-anvil-chunk-v1",
        "dimension": dimension,
        "region": "region/r.0.0.mca",
        "slot": chunk_x,
        "timestamp": 1,
        "chunk_x": chunk_x,
        "chunk_z": 0,
        "data_version": 4189,
        "status": "minecraft:full",
        "full": True,
        "compression": "zlib",
        "external": False,
        "heightmaps": heightmaps,
        "biome_sections": [biome_row],
        "structure_starts": structures,
    }
    return json.dumps(row, separators=(",", ":"), sort_keys=True)


def _input(path: Path, *, second_dimension: str = "minecraft:overworld") -> str:
    _ = path.write_text(
        _record(0) + "\n" + _record(1, dimension=second_dimension) + "\n",
        encoding="utf-8",
    )
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _identity() -> AnalysisIdentity:
    return AnalysisIdentity("run-a", "ordinary", "overworld", "minecraft:overworld")


def test_analysis_reports_stable_metrics_and_all_anomaly_methods(tmp_path: Path) -> None:
    # Given
    decoded = tmp_path / "chunks.jsonl"
    expected_hash = _input(decoded)

    # When
    first = analyze_jsonl(decoded, _identity(), expected_hash)
    second = analyze_jsonl(decoded, _identity(), expected_hash)

    # Then
    assert first.model_dump_json() == second.model_dump_json()
    assert (first.input_protocol, first.input_sha256) == ("item7-anvil-chunk-v1", expected_hash)
    d = first.denominators
    assert (d.chunk_count, d.input_chunk_records) == (2, 2)
    assert (d.other_selection_chunk_records, d.extra_chunk_records) == (0, 0)
    assert d.surface_block_cells == 512
    assert d.surface_quart_cells == 32
    assert d.height_adjacencies == 976
    assert d.structure_starts == 8
    assert d.structure_boxes == 8
    assert d.structure_start_pairs == 28
    assert d.cross_start_box_pairs == 27
    assert (d.structure_terrain_complete_starts, d.structure_terrain_excluded_starts) == (6, 2)
    assert d.structure_modification_complete_starts == 4
    assert d.structure_modification_excluded_starts == 4
    assert tuple((row.biome, row.quart_cells, row.component_sizes) for row in first.biomes) == (
        ("minecraft:desert", 1, (1,)),
        ("minecraft:forest", 2, (1, 1)),
        ("minecraft:plains", 29, (29,)),
    )
    anomalies = {row.key: row for row in first.anomalies}
    assert tuple(anomalies) == (
        "fragmented_biomes",
        "tiny_biomes",
        "unnatural_terrain_transitions",
        "buried_structures",
        "floating_structures",
        "cliff_intersections",
        "bad_underwater_placement",
        "overlapping_structures",
        "overlapping_villages",
        "failed_placements",
        "impossible_biome_restrictions",
        "excessive_terrain_modification",
    )
    assert anomalies["tiny_biomes"].candidates
    assert anomalies["unnatural_terrain_transitions"].candidates
    assert anomalies["buried_structures"].candidates
    floating = anomalies["floating_structures"]
    assert (floating.status, floating.candidates) == ("method-limited", ())
    assert anomalies["cliff_intersections"].candidates
    assert anomalies["bad_underwater_placement"].candidates
    assert all(
        "example:split" not in row.identifier
        for row in anomalies["bad_underwater_placement"].candidates
    )
    assert anomalies["overlapping_structures"].candidates
    assert anomalies["overlapping_villages"].candidate_count == 1
    assert anomalies["failed_placements"].status == "method-limited"
    assert anomalies["impossible_biome_restrictions"].status == "unresolved"
    assert anomalies["impossible_biome_restrictions"].candidate_count is None
    modification = anomalies["excessive_terrain_modification"]
    assert modification.candidates
    assert (modification.status, modification.denominator) == ("method-limited", 4)
    assert modification.denominator_name == "complete_structure_footprints_and_perimeters"
    assert anomalies["buried_structures"].status == "method-limited"
    assert anomalies["buried_structures"].denominator == 6


def test_analysis_rejects_hash_mismatch(tmp_path: Path) -> None:
    # Given
    decoded = tmp_path / "chunks.jsonl"
    _ = _input(decoded)

    # When / Then
    with pytest.raises(AnalysisError, match="input hash mismatch"):
        _ = analyze_jsonl(decoded, _identity(), "f" * 64)


def test_analysis_filters_fixed_selections_and_counts_extras(tmp_path: Path) -> None:
    # Given
    decoded = tmp_path / "chunks.jsonl"
    rows = (
        _record(0),
        _record(0, dimension="minecraft:the_nether"),
        _record(0, dimension="minecraft:the_end"),
        _record(96, dimension="minecraft:the_end", void=True),
        _record(1000),
    )
    _ = decoded.write_text("\n".join(rows) + "\n", encoding="utf-8")
    digest = hashlib.sha256(decoded.read_bytes()).hexdigest()

    # When
    report = analyze_jsonl(
        decoded,
        AnalysisIdentity("run-a", "ordinary", "end-outer", "minecraft:the_end"),
        digest,
    )

    # Then
    assert report.denominators.chunk_count == 1
    assert report.denominators.input_chunk_records == 5
    assert report.denominators.other_selection_chunk_records == 3
    assert report.denominators.extra_chunk_records == 1
    assert report.denominators.surface_quart_cells == 0
    assert report.denominators.void_surface_quart_cells == 16


def test_analysis_rejects_unknown_dimension(tmp_path: Path) -> None:
    decoded = tmp_path / "chunks.jsonl"
    digest = _input(decoded, second_dimension="example:moon")

    with pytest.raises(AnalysisError, match="unknown dimension"):
        _ = analyze_jsonl(decoded, _identity(), digest)


def _invalid_rows() -> tuple[str, ...]:
    base = ChunkRecord.model_validate_json(_record(0))
    status = base.model_copy(update={"status": "minecraft:empty", "full": True})
    duplicate_heightmap = base.model_copy(
        update={"heightmaps": (*base.heightmaps, base.heightmaps[0])}
    )
    duplicate_biome = base.model_copy(
        update={"biome_sections": (*base.biome_sections, base.biome_sections[0])}
    )
    section = base.biome_sections[0]
    negative_section = section.model_copy(update={"indices": (-1, *section.indices[1:])})
    negative_palette = base.model_copy(update={"biome_sections": (negative_section,)})
    return tuple(
        row.model_dump_json()
        for row in (status, duplicate_heightmap, duplicate_biome, negative_palette)
    )


@pytest.mark.parametrize("row", _invalid_rows())
def test_analysis_rejects_inconsistent_or_ambiguous_records(tmp_path: Path, row: str) -> None:
    # Given
    decoded = tmp_path / "chunks.jsonl"
    _ = decoded.write_text(row + "\n", encoding="utf-8")
    digest = hashlib.sha256(decoded.read_bytes()).hexdigest()

    # When / Then
    with pytest.raises(AnalysisError):
        _ = analyze_jsonl(decoded, _identity(), digest)


def test_analysis_cli_is_atomic_and_deterministic(tmp_path: Path) -> None:
    # Given
    decoded = tmp_path / "chunks.jsonl"
    expected_hash = _input(decoded)
    first, second = tmp_path / "first.json", tmp_path / "second.json"
    command = [
        str(decoded),
        "--output",
        str(first),
        "--run-id",
        "run-a",
        "--seed-role",
        "ordinary",
        "--selection",
        "overworld",
        "--dimension",
        "minecraft:overworld",
        "--expected-sha256",
        expected_hash,
    ]

    # When
    assert main(tuple(command)) == 0
    command[command.index(str(first))] = str(second)
    assert main(tuple(command)) == 0

    # Then
    assert first.read_bytes() == second.read_bytes()
    _ = first.write_text("sentinel\n", encoding="utf-8")
    _ = decoded.write_text(_record(0, malformed=True) + "\n", encoding="utf-8")
    command[command.index(str(second))] = str(first)
    command[command.index(expected_hash)] = hashlib.sha256(decoded.read_bytes()).hexdigest()
    with pytest.raises(AnalysisError, match="invalid decoded input"):
        _ = main(tuple(command))
    assert first.read_text(encoding="utf-8") == "sentinel\n"
