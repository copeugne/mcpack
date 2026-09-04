from __future__ import annotations

from typing import TYPE_CHECKING, cast

from mcpack_evidence.item8_inventory import biome_tag_inputs

if TYPE_CHECKING:
    from pydantic import JsonValue

VANILLA = "minecraft-server-1.21.1.jar!/META-INF/versions/1.21.1/server-1.21.1.jar"


def source(archive: str, document: dict[str, JsonValue]) -> dict[str, JsonValue]:
    return {
        "archive": archive,
        "path": "data/example/tags/worldgen/biome/test.json",
        "sha256": "a" * 64,
        "document": document,
    }


def test_additive_sources_and_vanilla_replacement_do_not_depend_on_catalog_order() -> None:
    vanilla = source(VANILLA, {"values": ["minecraft:plains"]})
    mod = source("mod.jar", {"replace": True, "values": ["minecraft:desert"]})
    result = biome_tag_inputs([mod, vanilla])
    assert result == biome_tag_inputs([vanilla, mod])
    row = cast("dict[str, JsonValue]", result["example:test"])
    assert row["values"] == ["minecraft:desert"]
    assert row["unresolved"] == []
    additive = source("second.jar", {"values": ["minecraft:forest"]})
    row = cast("dict[str, JsonValue]", biome_tag_inputs([vanilla, additive])["example:test"])
    assert row["values"] == ["minecraft:plains", "minecraft:forest"]


def test_replacement_among_multiple_mods_remains_unresolved() -> None:
    result = biome_tag_inputs(
        [
            source("a.jar", {"replace": True, "values": ["minecraft:plains"]}),
            source("b.jar", {"values": ["minecraft:desert"]}),
        ]
    )
    row = cast("dict[str, JsonValue]", result["example:test"])
    assert row["values"] is None
    assert row["unresolved"]


def test_condition_removal_and_optional_pack_are_not_silently_merged() -> None:
    for field in ("neoforge:conditions", "remove"):
        row = source("a.jar", {"values": ["minecraft:plains"], field: []})
        result = cast("dict[str, JsonValue]", biome_tag_inputs([row])["example:test"])
        assert result["values"] is None
        assert result["unresolved"]
    row = source("a.jar", {"values": ["minecraft:plains"]})
    row["path"] = "optional/data/example/tags/worldgen/biome/test.json"
    result = cast("dict[str, JsonValue]", biome_tag_inputs([row])["example:test"])
    assert result["values"] is None
