from __future__ import annotations

import gzip
import hashlib
import json
from pathlib import Path
from typing import TYPE_CHECKING, cast

from mcpack_evidence.item8_resource_selection import select_resources

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_injected_house_content() -> None:
    raw = Path("evidence/item-8/sources/templates-redacted.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "b4a2ed8ff0d16ff06c224119f623f248e75e9c8c838fbf2455bf37936c6d3705")
    catalog = cast("dict[str, list[JsonValue]]", json.loads(gzip.decompress(raw)))
    selected, _ = select_resources(catalog["resources"], "structure",
                                  enabled_packs=["vanilla", "mod_data"],
                                  lithostitched_overlay=True)
    for variant in ("plains", "desert", "taiga", "savanna", "snowy"):
        for role in ("cook", "chef"):
            key = f"chefsdelight:{variant}_{role}_house"
            row = selected[key]
            assert row["archive"] == "chefsdelight-1.0.5-neoforge-1.21.1.jar"
            doc = cast("dict[str, JsonValue]", row["document"])
            assert doc["entities"] == []
            nbts = [cast("dict[str, JsonValue]", block["nbt"]) for block in
                    cast("list[dict[str, JsonValue]]", doc["block_entities"])]
            assert {cast("str", nbt["LootTable"]) for nbt in nbts if "LootTable" in nbt} == {
                "chefsdelight:chests/cooker"}
            assert not any(nbt["id"] in ("minecraft:mob_spawner", "minecraft:spawner",
                                         "minecraft:trial_spawner") for nbt in nbts)
            pools = [nbt["pool"] for nbt in nbts if nbt["id"] == "minecraft:jigsaw"]
            expected = ["minecraft:empty"]
            if role == "cook" and variant in ("plains", "desert", "taiga"):
                expected = ["minecraft:village/plains/streets"]
            if role == "cook" and variant == "snowy":
                expected.append("minecraft:village/snowy/villagers")
            assert pools == expected
    raw = Path("evidence/item-8/sources/packaged-json-redacted.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "a5279d453f32edf7b1adc5c06b09953785b990b4b01c362b1423ed2f88930fdd")
    catalog = cast("dict[str, list[JsonValue]]", json.loads(gzip.decompress(raw)))
    loot, _ = select_resources(catalog["resources"], "loot_table",
                              enabled_packs=["vanilla", "mod_data"],
                              lithostitched_overlay=True)
    assert "chefsdelight:chests/cooker" in loot
