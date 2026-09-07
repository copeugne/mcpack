"""Focused regressions for the bounded saved-world block projection."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import TYPE_CHECKING, cast

import pytest
from tools.extract_item8_end_blocks import section_counts

from mcpack_evidence.item7_nbt import NbtDecodeError

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_preserved_overworld_sample_has_no_monster_boxes() -> None:
    """Bind the negative result to complete sampled chunks, not unused palettes."""
    raw = Path("evidence/item-8/world-observations/central-overworld/blocks.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "8b19e927b6b5d1a4de5f210eb301402c7f5e9dca4d4eb210b2fa31219cde4d06"
    )
    document = cast("dict[str, JsonValue]", json.loads(raw))
    chunks = cast("list[dict[str, JsonValue]]", document["chunks"])
    assert len(chunks) == 64
    assert {(c["chunk_x"], c["chunk_z"]) for c in chunks} == {
        (x, z) for x in range(-4, 4) for z in range(-4, 4)
    }
    for chunk in chunks:
        assert chunk["status"] == "minecraft:full"
        sections = cast("list[dict[str, JsonValue]]", chunk["sections"])
        assert len(sections) == 24
        assert {cast("int", s["y"]) for s in sections} == set(range(-4, 20))
        for section in sections:
            counts = cast("dict[str, int]", section["block_counts"])
            assert sum(counts.values()) == 4096
            assert counts.get("quark:monster_box", 0) == 0
        entities = cast("list[dict[str, JsonValue]]", chunk["block_entities"])
        assert all(e["id"] != "quark:monster_box" for e in entities)


def test_single_palette_fills_section() -> None:
    """A section without a packed array has one state for all positions."""
    assert section_counts({"block_states": {"palette": [{"Name": "minecraft:air"}]}}) == {
        "minecraft:air": 4096,
    }


def test_actual_indices_exclude_unused_palette_entry() -> None:
    """One nonzero nibble changes one block, not the whole section."""
    assert section_counts({"block_states": {
        "palette": [{"Name": "minecraft:air"}, {"Name": "minecraft:obsidian"},
                    {"Name": "minecraft:bell"}],
        "data": [1, *([0] * 255)],
    }}) == {"minecraft:air": 4095, "minecraft:obsidian": 1}


def test_invalid_packed_data_is_rejected() -> None:
    """Incomplete arrays and invalid state indices cannot become evidence."""
    with pytest.raises(NbtDecodeError):
        _ = section_counts({"block_states": {
            "palette": [{"Name": "a"}, {"Name": "b"}], "data": [],
        }})
    with pytest.raises(ValueError, match="out of range"):
        _ = section_counts({"block_states": {
            "palette": [{"Name": "a"}, {"Name": "b"}], "data": [2, *([0] * 255)],
        }})
