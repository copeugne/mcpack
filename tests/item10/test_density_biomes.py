from pathlib import Path
from typing import cast

import pytest
from tools.analyze_structure_density import census, chunk_biome_column

from mcpack_evidence.item7_anvil import decode_region
from mcpack_evidence.item7_nbt_models import BiomeSection
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
