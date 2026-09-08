from pathlib import Path

import pytest
from tools.analyze_structure_density import census, generation_digest

from mcpack_evidence.item7_anvil import decode_region_payloads
from tests.item7 import anvil_support
from tests.item10.test_density_census import make_region


def test_generation_projection_excludes_ticks_but_detects_blocks_and_biomes() -> None:
    original = anvil_support.chunk_nbt(0, 0)
    position = anvil_support.integer("xPos", 0)
    changed_time = original.replace(position, position + anvil_support.integer("LastUpdate", 100))
    assert generation_digest(original) == generation_digest(changed_time)
    changed_biome = original.replace(
        anvil_support.named("minecraft:forest"), anvil_support.named("minecraft:desert")
    )
    assert generation_digest(original) != generation_digest(changed_biome)
    section_y = anvil_support.tag(1, "Y", b"\x00")
    palette = anvil_support.list_tag(
        "palette", 10, (anvil_support.string("Name", "minecraft:stone") + b"\x00",)
    )
    block_states = anvil_support.compound("block_states", (palette,))
    stone = original.replace(section_y, section_y + block_states)
    dirt = stone.replace(
        anvil_support.named("minecraft:stone"), anvil_support.named("minecraft:dirt")
    )
    assert generation_digest(stone) != generation_digest(dirt)


def test_projection_is_optional_and_bound_to_selected_chunk(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    region = make_region(tmp_path, monkeypatch)
    ((_, payload),) = tuple(decode_region_payloads(region))
    ordinary = census(tmp_path, "minecraft:overworld", (0, 0, 0, 0), {})
    projected = census(tmp_path, "minecraft:overworld", (0, 0, 0, 0), {}, include_generation=True)
    assert projected.pop("generation_content") == [
        {"chunk_x": 0, "chunk_z": 0, "sha256": generation_digest(payload)}
    ]
    assert projected == ordinary
