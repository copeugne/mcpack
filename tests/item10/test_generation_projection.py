import itertools
import struct
from pathlib import Path

import pytest
from tools.analyze_structure_density import census, generation_digest

from mcpack_evidence.item7_anvil import decode_region_payloads
from mcpack_evidence.item7_nbt import decode_compound_nbt
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
    assert projected.pop("generation_encoding") == "typed-nbt-v2"
    assert projected == ordinary


@pytest.mark.parametrize(
    ("left", "right"),
    list(
        itertools.combinations(
            [
                anvil_support.tag(tag, "extra", struct.pack(fmt, 1))
                for tag, fmt in [(1, ">b"), (2, ">h"), (3, ">i"), (4, ">q")]
            ],
            2,
        )
    ),
)
def test_scalar_tag_width_cannot_collide(left: bytes, right: bytes) -> None:
    original = anvil_support.chunk_nbt(0, 0)
    marker = anvil_support.string("id", "minecraft:village_plains")
    a = original.replace(marker, marker + left)
    b = original.replace(marker, marker + right)
    assert decode_compound_nbt(a) == decode_compound_nbt(b)
    assert generation_digest(a) != generation_digest(b)


@pytest.mark.parametrize(
    ("left", "right"),
    [
        *list(
            itertools.combinations(
                [
                    anvil_support.tag(tag, "extra", struct.pack(">i", 1) + struct.pack(fmt, 1))
                    for tag, fmt in [(7, ">b"), (11, ">i"), (12, ">q")]
                ],
                2,
            )
        ),
        (anvil_support.list_tag("extra", 1, ()), anvil_support.list_tag("extra", 3, ())),
    ],
)
def test_array_and_empty_list_types_cannot_collide(left: bytes, right: bytes) -> None:
    original = anvil_support.chunk_nbt(0, 0)
    marker = anvil_support.string("id", "minecraft:village_plains")
    a = original.replace(marker, marker + left)
    b = original.replace(marker, marker + right)
    assert decode_compound_nbt(a) == decode_compound_nbt(b)
    assert generation_digest(a) != generation_digest(b)


def test_typed_compound_key_order_is_canonical() -> None:
    original = anvil_support.chunk_nbt(0, 0)
    marker = anvil_support.string("id", "minecraft:village_plains")
    a, b = anvil_support.integer("a", 1), anvil_support.integer("b", 2)
    assert generation_digest(original.replace(marker, marker + a + b)) == generation_digest(
        original.replace(marker, marker + b + a)
    )


def test_float_and_double_tag_types_cannot_collide() -> None:
    original = anvil_support.chunk_nbt(0, 0)
    marker = anvil_support.string("id", "minecraft:village_plains")
    a = original.replace(marker, marker + anvil_support.tag(5, "extra", struct.pack(">f", 1)))
    b = original.replace(marker, marker + anvil_support.tag(6, "extra", struct.pack(">d", 1)))
    assert decode_compound_nbt(a) == decode_compound_nbt(b)
    assert generation_digest(a) != generation_digest(b)
