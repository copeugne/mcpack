from pathlib import Path
from typing import cast

import pytest
from tools.analyze_structure_density import (
    census,
    chunk_biome_column,
    occurrence_biomes,
    summarize_biomes,
)

from mcpack_evidence.item7_anvil import decode_region
from mcpack_evidence.item7_nbt_models import BiomeSection, StructureBox
from tests.item10.test_density_census import make_region


def test_column_uses_saved_quart_order_and_negative_heights(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    (record,) = tuple(decode_region(make_region(tmp_path, monkeypatch)))
    indices = [0] * 64
    indices[2 + 4 * 2 + 16] = 1
    section = BiomeSection(section_y=-1, palette=("test:a", "test:b"), indices=tuple(indices))
    record = record.model_copy(update={"biome_sections": (section,)})
    assert chunk_biome_column(record, -16, 16) == {
        -4: "test:a",
        -3: "test:b",
        -2: "test:a",
        -1: "test:a",
    }


def test_actual_anchor_uses_its_own_quart_with_negative_chunk_coordinates(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    (record,) = tuple(decode_region(make_region(tmp_path, monkeypatch)))
    indices = [0] * 64
    indices[3 + 4 + 16] = 1
    section = BiomeSection(
        section_y=-1, palette=("test:center", "test:anchor"), indices=tuple(indices)
    )
    record = record.model_copy(update={"chunk_x": -1, "chunk_z": -2, "biome_sections": (section,)})
    assert chunk_biome_column(record, -16, 16)[-3] == "test:center"
    assert chunk_biome_column(record, -16, 16, anchor=(-1, -27))[-3] == "test:anchor"
    assert chunk_biome_column(record, -16, 16, anchor=(-4, -28))[-3] == "test:anchor"


@pytest.mark.parametrize("anchor", [(16, 0), (0, -1), (True, 0)])
def test_biome_anchor_cannot_use_a_different_chunk_or_coerced_coordinate(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, anchor: tuple[int, int]
) -> None:
    (record,) = tuple(decode_region(make_region(tmp_path, monkeypatch)))
    with pytest.raises(ValueError, match="biome anchor"):
        _ = chunk_biome_column(record, 0, 16, anchor=anchor)


@pytest.mark.parametrize("defect", ["missing", "duplicate", "bad-index"])
def test_incomplete_or_invalid_biomes_cannot_shrink_exposure(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, defect: str
) -> None:
    (record,) = tuple(decode_region(make_region(tmp_path, monkeypatch)))
    section = record.biome_sections[0]
    if defect == "missing":
        sections = ()
    elif defect == "duplicate":
        sections = (section, section)
    else:
        sections = (section.model_copy(update={"indices": (99,) * 64}),)
    record = record.model_copy(update={"biome_sections": sections})
    with pytest.raises(ValueError, match="biome section"):
        _ = chunk_biome_column(record, 0, 16)


def test_census_retains_independent_complete_height_denominators(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _ = make_region(tmp_path, monkeypatch)
    result = census(
        tmp_path,
        "minecraft:overworld",
        (0, 0, 0, 0),
        {"minecraft:overworld": (0, 16)},
        include_biomes=True,
    )
    exposure = cast("dict[str, object]", result["biome_exposure"])
    assert exposure["rows"] == [
        {"quart_y": y, "biome": "minecraft:plains", "full_chunks": 1} for y in range(4)
    ]


def test_occurrence_uses_piece_height_and_retains_unavailable_attribution(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    (record,) = tuple(decode_region(make_region(tmp_path, monkeypatch)))
    start = record.structure_starts[0]
    start = start.model_copy(
        update={
            "boxes": (
                StructureBox(bounds=(0, -12, 0, 15, -4, 15)),
                StructureBox(bounds=(-5, -8, 2, 22, 0, 17)),
            )
        }
    )
    record = record.model_copy(update={"structure_starts": (start,)})
    (row,) = occurrence_biomes(record, {-2: "test:underground"})
    assert row["envelope"] == [-5, -12, 0, 22, 0, 17]
    assert row["anchor_y"] == -6
    assert row["quart_y"] == -2
    assert row["biome"] == "test:underground"
    assert row["unavailable_reason"] is None
    (missing_height,) = occurrence_biomes(record, {0: "test:surface"})
    assert missing_height["biome"] is None
    assert missing_height["unavailable_reason"] == "anchor outside stored biome height"
    record = record.model_copy(
        update={"structure_starts": (start.model_copy(update={"boxes": ()}),)}
    )
    (no_bounds,) = occurrence_biomes(record, {})
    assert no_bounds["unavailable_reason"] == "no stored piece bounds"


def test_inverted_piece_bounds_reject_biome_attribution(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    (record,) = tuple(decode_region(make_region(tmp_path, monkeypatch)))
    start = record.structure_starts[0].model_copy(
        update={"boxes": (StructureBox(bounds=(0, 9, 0, 15, 8, 15)),)}
    )
    record = record.model_copy(update={"structure_starts": (start,)})
    with pytest.raises(ValueError, match="inverted structure"):
        _ = occurrence_biomes(record, {})


def biome_comparison_input() -> dict[str, object]:
    return {
        "biome_exposure": {
            "rows": [
                {"quart_y": -2, "biome": "test:cave", "full_chunks": 4},
                {"quart_y": 4, "biome": "test:cave", "full_chunks": 20},
                {"quart_y": 4, "biome": "test:empty", "full_chunks": 5},
            ]
        },
        "occurrence_biomes": [
            {
                "registry_id": "test:dungeon",
                "chunk_x": -1,
                "chunk_z": 0,
                "quart_y": -2,
                "biome": "test:cave",
                "unavailable_reason": None,
            }
        ],
        "classification": {
            "occurrences": [
                {
                    "registry_id": "test:dungeon",
                    "chunk_x": -1,
                    "chunk_z": 0,
                    "role": "T2",
                    "comparison_groups": [],
                },
                {
                    "candidate_id": 1,
                    "quart_y": 4,
                    "biome": "test:cave",
                    "biome_unavailable_reason": None,
                    "role": "C",
                    "comparison_groups": ["village"],
                },
                {
                    "candidate_id": 2,
                    "quart_y": 4,
                    "biome": "test:off-center",
                    "biome_unavailable_reason": None,
                    "role": "T1",
                    "comparison_groups": [],
                },
                {
                    "candidate_id": 3,
                    "quart_y": None,
                    "biome": None,
                    "biome_unavailable_reason": "NO_LOCATION_HEIGHT",
                    "role": "T4",
                    "comparison_groups": [],
                },
            ]
        },
    }


def test_biome_comparison_preserves_height_zero_exposure_and_unavailable_locations() -> None:
    summary = summarize_biomes(biome_comparison_input())
    rows = cast("list[dict[str, object]]", summary["rows"])
    by_key = {(row["quart_y"], row["biome"]): row for row in rows}
    underground = by_key[-2, "test:cave"]
    surface = by_key[4, "test:cave"]
    assert underground["full_chunks"] == 4
    assert surface["full_chunks"] == 20
    assert cast("dict[str, float]", underground["per_1000_chunks"])["T2"] == 250
    assert cast("dict[str, float]", surface["per_1000_chunks"])["villages"] == 50
    assert cast("dict[str, int]", surface["counts"])["encounter_sites"] == 0
    assert cast("dict[str, int]", surface["counts"])["actionable_candidates"] == 1
    empty = by_key[4, "test:empty"]
    assert set(cast("dict[str, int]", empty["counts"]).values()) == {0}
    assert set(cast("dict[str, float]", empty["per_1000_chunks"]).values()) == {0}
    off_center = by_key[4, "test:off-center"]
    assert off_center["full_chunks"] == 0
    assert cast("dict[str, int]", off_center["counts"])["T1"] == 1
    assert set(cast("dict[str, float | None]", off_center["per_1000_chunks"]).values()) == {None}
    unavailable = cast("list[dict[str, object]]", summary["unavailable_anchors"])
    assert len(unavailable) == 1
    assert unavailable[0]["candidate_id"] == 3
    assert unavailable[0]["biome_unavailable_reason"] == "NO_LOCATION_HEIGHT"


@pytest.mark.parametrize("defect", ["duplicate-exposure", "duplicate-anchor", "missing-anchor"])
def test_biome_comparison_rejects_ambiguous_or_missing_registry_joins(defect: str) -> None:
    result = biome_comparison_input()
    exposure = cast("dict[str, list[dict[str, object]]]", result["biome_exposure"])["rows"]
    anchors = cast("list[dict[str, object]]", result["occurrence_biomes"])
    if defect == "duplicate-exposure":
        exposure.append(exposure[0])
    elif defect == "duplicate-anchor":
        anchors.append(anchors[0])
    else:
        anchors.clear()
    with pytest.raises(ValueError, match=r"duplicate|no biome anchor"):
        _ = summarize_biomes(result)
