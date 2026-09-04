from __future__ import annotations

from typing import TYPE_CHECKING, cast

import pytest
from tools.build_item8_structure_inputs import runtime_order

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


def test_verified_order_discards_only_contributions_before_replacement() -> None:
    rows: list[JsonValue] = [
        source("a.jar", {"values": ["minecraft:forest"]}),
        source("b.jar", {"replace": True, "values": ["minecraft:plains"]}),
        source("c.jar", {"values": ["minecraft:desert"]}),
    ]
    result = biome_tag_inputs(rows, ("a.jar", "b.jar", "c.jar"))
    row = cast("dict[str, JsonValue]", result["example:test"])
    assert row["values"] == ["minecraft:plains", "minecraft:desert"]
    assert row["unresolved"] == []
    result = biome_tag_inputs(rows, ("a.jar", "c.jar", "b.jar"))
    assert cast("dict[str, JsonValue]", result["example:test"])["values"] == ["minecraft:plains"]
    result = biome_tag_inputs(rows, ("a.jar", "b.jar"))
    assert cast("dict[str, JsonValue]", result["example:test"])["values"] is None
    with pytest.raises(ValueError, match="duplicate archive"):
        _ = biome_tag_inputs(rows, ("a.jar", "a.jar"))


def test_runtime_order_uses_last_expanded_record_and_preserves_its_line() -> None:
    marker = "[net.fabricmc.fabric.impl.resource.loader.ModResourcePackUtil/]: "
    marker += "[Fabric] Final sorting result: "
    first = f"{marker}[mod/b, mod/a]"
    last = f"{marker}[vanilla, mod/a, mod/b]"
    mapping = {"a.jar": "mod/a", "b.jar": "mod/b"}
    result = runtime_order(f"{first}\nunrelated\n{last}\n", mapping)
    assert result["archives"] == ["a.jar", "b.jar"]
    assert result["line"] == 3
    assert result["record"] == last
    for payload in ("[mod/a]", "[mod/a, mod/a, mod/b]", "mod/a, mod/b"):
        with pytest.raises(ValueError, match=r"expanded.*sorting"):
            _ = runtime_order(marker + payload, mapping)
    with pytest.raises(ValueError, match="lacks final expanded"):
        _ = runtime_order("unrelated", mapping)
