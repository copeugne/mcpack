"""Focused regressions for the bounded saved-world block projection."""

from __future__ import annotations

import pytest
from tools.extract_item8_end_blocks import section_counts

from mcpack_evidence.item7_nbt import NbtDecodeError


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
