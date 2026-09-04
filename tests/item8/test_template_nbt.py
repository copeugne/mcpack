from __future__ import annotations

import gzip
import struct

import pytest

from mcpack_evidence.item7_nbt import NbtDecodeError, decode_compound_nbt
from mcpack_evidence.item8_templates import template_summary
from tests.item7.anvil_support import compound, integer, list_tag, string, tag


def test_template_nbt_preserves_nested_compounds_and_arrays() -> None:
    body = compound(
        "",
        (
            tag(9, "size", b"\x03" + struct.pack(">iiii", 3, 4, 8, 12)),
            compound("entity", (string("id", "minecraft:zombie"),)),
            tag(11, "position", struct.pack(">iiii", 3, -1, 64, 2)),
            tag(7, "bytes", struct.pack(">i", 2) + b"\x00\xff"),
        ),
    )
    assert decode_compound_nbt(body) == {
        "size": [4, 8, 12],
        "entity": {"id": "minecraft:zombie"},
        "position": [-1, 64, 2],
        "bytes": [0, 255],
    }


def test_template_decoder_rejects_truncated_or_trailing_bytes() -> None:
    for payload in (b"\x0a\x00\x00", b"\x0a\x00\x00\x00extra"):
        with pytest.raises(NbtDecodeError):
            _ = decode_compound_nbt(payload)


def test_template_summary_preserves_spawner_loot_and_authored_entities() -> None:
    spawner = compound(
        "",
        (
            integer("state", 0),
            compound("nbt", (string("id", "minecraft:mob_spawner"),)),
        ),
    )[3:]
    chest = compound(
        "",
        (
            integer("state", 1),
            compound("nbt", (string("LootTable", "example:chests/tower"),)),
        ),
    )[3:]
    entity = compound("", (compound("nbt", (string("id", "minecraft:zombie"),)),))[3:]
    root = compound(
        "",
        (
            tag(9, "size", b"\x03" + struct.pack(">iiii", 3, 4, 8, 12)),
            list_tag("blocks", 10, (spawner, chest)),
            list_tag("entities", 10, (entity,)),
        ),
    )
    summary = template_summary(root)
    assert template_summary(gzip.compress(root, mtime=0)) == summary
    assert summary["size"] == [4, 8, 12]
    assert summary["state_counts"] == {"0": 1, "1": 1}
    assert summary["block_entities"] == [
        {"state": 0, "nbt": {"id": "minecraft:mob_spawner"}},
        {"state": 1, "nbt": {"LootTable": "example:chests/tower"}},
    ]
    assert summary["entities"] == [{"nbt": {"id": "minecraft:zombie"}}]


def test_template_summary_rejects_non_template_nbt() -> None:
    with pytest.raises(ValueError, match="missing valid size or blocks"):
        _ = template_summary(compound("", ()))
