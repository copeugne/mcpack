from __future__ import annotations

import gzip
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import TYPE_CHECKING, cast

from mcpack_evidence.item8_resource_selection import select_resources

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_slime_cave_template_markers_and_loot() -> None:
    raw = Path("evidence/item-8/sources/templates-redacted.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "b4a2ed8ff0d16ff06c224119f623f248e75e9c8c838fbf2455bf37936c6d3705")
    catalog = cast("dict[str, list[dict[str, JsonValue]]]", json.loads(gzip.decompress(raw)))
    candidates = [row for row in catalog["resources"]
                  if str(row["path"]).endswith("data/explorations/structure/slime_cave.nbt")]
    assert len(candidates) == 1
    row = candidates[0]
    assert row["archive"] == "explorations-neoforge-1.21.1-1.6.2.jar"
    assert row["sha256"] == "02f9dc19b1fd4cf766ff772961298ab96049d1353a765889260f0e78953119d3"
    document = cast("dict[str, JsonValue]", row["document"])
    assert document["size"] == [15, 12, 15]
    assert document["entities"] == []
    blocks = cast("list[dict[str, JsonValue]]", document["block_entities"])
    nbts = [cast("dict[str, JsonValue]", block["nbt"]) for block in blocks]
    assert Counter(str(nbt["id"]) for nbt in nbts) == {
        "minecraft:structure_block": 7, "minecraft:chest": 1}
    markers = [nbt for nbt in nbts if nbt["id"] == "minecraft:structure_block"]
    assert all(nbt["mode"] == "DATA" for nbt in markers)
    assert Counter(str(nbt["metadata"]) for nbt in markers) == {"slime": 6, "spawner": 1}
    assert next(nbt for nbt in nbts if nbt["id"] == "minecraft:chest")["LootTable"] == (
        "explorations:chests/slime_cave")

    raw = Path("evidence/item-8/sources/packaged-json-redacted.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "a5279d453f32edf7b1adc5c06b09953785b990b4b01c362b1423ed2f88930fdd")
    sources = cast("dict[str, JsonValue]", json.loads(gzip.decompress(raw)))
    selected, _ = select_resources(
        cast("list[JsonValue]", sources["resources"]), "loot_table",
        enabled_packs=["vanilla", "mod_data"], lithostitched_overlay=True)
    loot = selected["explorations:chests/slime_cave"]
    assert loot["archive"] == row["archive"]
    assert loot["sha256"] == "b818aa4f22d55c2065e1eaeb8cb22cdb268e9685ccd697a4f60b22789892a9a7"

    decisions = cast("dict[str, list[dict[str, JsonValue]]]", json.loads(
        Path("evidence/item-8/family-decisions.json").read_bytes()))
    group = next(g for g in decisions["groups"] if g["family_id"] == "explorations:slime_cave")
    assert group["custom_template_ids"] == ["explorations:slime_cave"]
    assert group["missing_components"] == []
    attrs = cast("dict[str, dict[str, JsonValue]]", group["attributes"])
    assert attrs["generated_spawners"]["template_marker_count"] == 1
    assert attrs["mob_source"]["template_slime_marker_count"] == 6
