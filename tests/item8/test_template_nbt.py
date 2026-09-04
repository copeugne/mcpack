from __future__ import annotations

import gzip
import struct
from typing import TYPE_CHECKING

import pytest

from mcpack_evidence.item7_nbt import NbtDecodeError, decode_compound_nbt
from mcpack_evidence.item8_templates import template_content, template_summary
from tests.item7.anvil_support import compound, integer, list_tag, string, tag

if TYPE_CHECKING:
    from pydantic import JsonValue


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


def test_content_index_keeps_trial_rewards_and_passengers_separate_from_spawned_mobs() -> None:
    trial: dict[str, JsonValue] = {
        "id": "minecraft:trial_spawner",
        "normal_config": {
            "spawn_potentials": [{"data": {"entity": {"id": "minecraft:skeleton"}}, "weight": 1}],
            "loot_tables_to_eject": [{"data": "example:reward", "weight": 2}],
        },
    }
    document: dict[str, JsonValue] = {
        "block_entities": [
            {"pos": [1, 2, 3], "nbt": trial},
            {"pos": [4, 5, 6], "nbt": {"id": "minecraft:chest", "LootTable": "example:chest"}},
        ],
        "entities": [
            {"nbt": {"id": "minecraft:horse", "Passengers": [{"id": "minecraft:zombie"}]}}
        ],
    }
    result = template_content(document)
    assert result["authored_entities"] == [
        {"path": "/entities/0/nbt", "id": "minecraft:horse"},
        {"path": "/entities/0/nbt/Passengers/0", "id": "minecraft:zombie"},
    ]
    assert result["spawner_blocks"] == [
        {"path": "/block_entities/0", "position": [1, 2, 3], "nbt": trial}
    ]
    assert result["loot_references"] == [
        {
            "path": "/block_entities/0/nbt/normal_config/loot_tables_to_eject",
            "value": [{"data": "example:reward", "weight": 2}],
        },
        {"path": "/block_entities/1/nbt/LootTable", "value": "example:chest"},
    ]


def test_empty_authored_entity_is_retained_as_unresolved() -> None:
    result = template_content({"block_entities": [], "entities": [{"nbt": {}}]})
    assert result["authored_entities"] == []
    assert result["unresolved_entities"] == [
        {"path": "/entities/0/nbt", "reason": "authored entity lacks an ID"}
    ]
