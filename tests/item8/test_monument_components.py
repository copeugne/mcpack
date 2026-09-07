from __future__ import annotations

import gzip
import hashlib
import json
from pathlib import Path
from typing import TYPE_CHECKING, cast

from mcpack_evidence.item8_resource_selection import select_resources

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_monument_candidate_component_resources() -> None:
    """Join captured call-site candidates, without simulating graph reachability."""
    raw = Path("evidence/item-8/sources/packaged-json-redacted.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "a5279d453f32edf7b1adc5c06b09953785b990b4b01c362b1423ed2f88930fdd")
    catalog = cast("dict[str, list[JsonValue]]", json.loads(gzip.decompress(raw)))
    pools, _ = select_resources(catalog["resources"], "worldgen/template_pool",
                               enabled_packs=["vanilla", "mod_data"],
                               lithostitched_overlay=True)
    # MonumentBuilding and the eight Fit*Room captures bind these suffixes.
    suffixes = {
        "body/ne_corner", "body/nw_corner", "body/se_corner", "body/sw_corner",
        "rooms/core", "rooms/double_x", "rooms/double_xy", "rooms/double_y",
        "rooms/double_yz", "rooms/double_z", "rooms/simple", "rooms/simple_pillar",
        "rooms/simple_top", "openings/entrance_wall", "openings/floor",
        "openings/wall_1", "openings/wall_3", "openings/arch", "openings/wall_shelf",
    }
    keys = {f"repurposed_structures:monuments/{v}/{s}"
            for v in ("desert", "icy", "jungle", "nether") for s in suffixes}
    assert len(keys) == 76
    assert keys <= pools.keys()
    template_ids: set[str] = set()
    processor_ids: set[str] = set()
    for key in keys:
        document = cast("dict[str, JsonValue]", pools[key]["document"])
        assert document["fallback"] == "minecraft:empty"
        for row in cast("list[dict[str, JsonValue]]", document["elements"]):
            assert cast("int", row["weight"]) > 0
            element = cast("dict[str, JsonValue]", row["element"])
            assert element["element_type"] == "minecraft:single_pool_element"
            template_ids.add(str(element["location"]))
            processor_ids.add(str(element["processors"]))
    assert len(template_ids) == 88
    assert processor_ids == {
        "minecraft:empty", "repurposed_structures:monuments/nether_openings",
        *(f"repurposed_structures:monuments/{v}_randomize"
          for v in ("desert", "icy", "jungle", "nether")),
    }
    raw = Path("evidence/item-8/sources/templates-redacted.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "b4a2ed8ff0d16ff06c224119f623f248e75e9c8c838fbf2455bf37936c6d3705")
    templates = cast("dict[str, list[JsonValue]]", json.loads(gzip.decompress(raw)))
    selected, _ = select_resources(templates["resources"], "structure",
                                  enabled_packs=["vanilla", "mod_data"],
                                  lithostitched_overlay=True)
    assert template_ids <= selected.keys()
    extra_pools = {k for k in pools if k.startswith("repurposed_structures:monuments/")} - keys
    assert extra_pools == {f"repurposed_structures:monuments/{v}/openings/wall_2"
                           for v in ("desert", "icy", "jungle", "nether")}
    assert {k for k in selected if k.startswith("repurposed_structures:monuments/")} == (
        template_ids | extra_pools
    )
    for key in extra_pools:
        pool = cast("dict[str, JsonValue]", pools[key]["document"])
        assert pool["fallback"] == "minecraft:empty"
        rows = cast("list[dict[str, JsonValue]]", pool["elements"])
        assert len(rows) == 1
        element = cast("dict[str, JsonValue]", rows[0]["element"])
        assert element["element_type"] == "minecraft:single_pool_element"
        assert element["location"] == key
        assert selected[key]["document"] == {
            "block_entities": [], "data_version": 3953, "entities": [],
            "palette": [{"Name": "minecraft:air"}], "palettes": None,
            "size": [4, 3, 1], "state_counts": {"0": 12},
        }
    expected_entities = {
        "desert": {"minecraft:skeleton", "minecraft:creeper", "minecraft:husk",
                   "minecraft:guardian"},
        "icy": {"minecraft:stray", "minecraft:vex", "minecraft:guardian"},
        "jungle": {"minecraft:skeleton", "minecraft:creeper", "minecraft:husk",
                   "minecraft:guardian"},
        "nether": {"minecraft:wither_skeleton", "minecraft:magma_cube", "minecraft:strider"},
    }
    for variant, expected in expected_entities.items():
        documents = [cast("dict[str, JsonValue]", selected[key]["document"])
                     for key in template_ids
                     if key.startswith(f"repurposed_structures:monuments/{variant}/")]
        assert len(documents) == 22
        entities = [cast("dict[str, JsonValue]", entity["nbt"])
                    for doc in documents
                    for entity in cast("list[dict[str, JsonValue]]", doc["entities"])]
        assert {str(entity["id"]) for entity in entities} == expected
        blocks = [cast("dict[str, JsonValue]", block["nbt"])
                  for doc in documents
                  for block in cast("list[dict[str, JsonValue]]", doc["block_entities"])]
        assert {str(block["id"]) for block in blocks} == {"minecraft:chest"}
        assert {str(block["LootTable"]) for block in blocks} == {
            f"repurposed_structures:chests/monuments/{variant}"}


def test_monument_processor_loot_references() -> None:
    raw = Path("evidence/item-8/sources/packaged-json-redacted.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "a5279d453f32edf7b1adc5c06b09953785b990b4b01c362b1423ed2f88930fdd")
    catalog = cast("dict[str, list[JsonValue]]", json.loads(gzip.decompress(raw)))
    candidates: list[JsonValue] = [
        row for row in catalog["resources"] if isinstance(row, dict)
        and "data/repurposed_structures/worldgen/processor_list/monuments/"
        in str(row.get("path"))
    ]
    selected, _ = select_resources(candidates, "worldgen/processor_list",
                                  enabled_packs=["vanilla", "mod_data"],
                                  lithostitched_overlay=True)
    assert set(selected) == {f"repurposed_structures:monuments/{name}" for name in (
        "desert_randomize", "icy_randomize", "jungle_randomize", "nether_randomize",
        "nether_openings")}
    jungle = cast("dict[str, list[dict[str, JsonValue]]]",
                  selected["repurposed_structures:monuments/jungle_randomize"]["document"])
    surface = jungle["processors"][0]
    assert surface["processor_type"] == "repurposed_structures:structure_surface_processor"
    delegate = cast("dict[str, JsonValue]", surface["delegate"])
    assert delegate["processor_type"] == "minecraft:rule"
    rules = cast("list[dict[str, JsonValue]]", delegate["rules"])
    modifiers = [r["block_entity_modifier"] for r in rules if "block_entity_modifier" in r]
    assert modifiers == [{"loot_table": "repurposed_structures:archaeology/monument_jungle",
                          "type": "minecraft:append_loot"}] * 4
    loot, _ = select_resources(catalog["resources"], "loot_table",
                              enabled_packs=["vanilla", "mod_data"],
                              lithostitched_overlay=True)
    assert "repurposed_structures:archaeology/monument_jungle" in loot
    assert {f"repurposed_structures:chests/monuments/{v}"
            for v in ("desert", "icy", "jungle", "nether")} <= loot.keys()
