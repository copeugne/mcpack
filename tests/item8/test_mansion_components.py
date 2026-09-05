from __future__ import annotations

import gzip
import hashlib
import json
from pathlib import Path
from typing import TYPE_CHECKING, cast

from mcpack_evidence.item8_resource_selection import select_resources

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_mansion_candidate_pools_and_child_fallbacks() -> None:  # noqa: PLR0915 - one source chain.
    """Bind source-derived candidate names, not simulated layout reachability."""
    raw = Path("evidence/item-8/sources/packaged-json-redacted.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "a5279d453f32edf7b1adc5c06b09953785b990b4b01c362b1423ed2f88930fdd")
    catalog = cast("dict[str, list[JsonValue]]", json.loads(gzip.decompress(raw)))
    structures, _ = select_resources(catalog["resources"], "worldgen/structure",
                                    enabled_packs=["vanilla", "mod_data"],
                                    lithostitched_overlay=True)
    pools, _ = select_resources(catalog["resources"], "worldgen/template_pool",
                               enabled_packs=["vanilla", "mod_data"],
                               lithostitched_overlay=True)
    variants = {"birch", "desert", "jungle", "mangrove", "oak", "savanna", "snowy", "taiga"}
    for variant in variants:
        definition = cast("dict[str, JsonValue]", structures[
            f"repurposed_structures:mansion_{variant}"]["document"])
        assert definition["type"] == "repurposed_structures:mansion_structure"
        assert definition["mansion_type"] == variant

    # Operands and concat recipes in repurposed-mansion-bindings establish these
    # candidate selectors. Some selectors may be unreachable for a given layout.
    suffixes = {
        "wall_flat", "wall_window", "wall_corner", "entrance", "roof", "roof_front",
        "roof_corner", "roof_inner_corner", "small_wall", "small_wall_corner",
        "carpet_north", "carpet_east", "carpet_south_1", "carpet_south_2",
        "carpet_west_1", "carpet_west_2", "corridor_floor", "corridor_floor_high",
        "indoors_wall_1", "indoors_wall_2", "indoors_door_1", "indoors_door_2",
    }
    room_suffixes = {
        "1x1_rooms", "1x1_secret_rooms", "1x2_rooms", "1x2_alternative_rooms",
        "1x2_secret_rooms", "2x2_rooms", "2x2_secret_rooms",
    }
    suffixes.update(f"{floor}_floor_{room}" for floor in ("first", "second", "third")
                    for room in room_suffixes)
    suffixes.update(f"{floor}_floor_1x2_{side}_stairs"
                    for floor in ("second", "third") for side in ("c", "d"))
    assert len(suffixes) == 47
    roots = {f"repurposed_structures:mansions/{v}/{s}" for v in variants for s in suffixes}
    assert roots <= pools.keys()
    elements: list[dict[str, JsonValue]] = []
    for key in roots:
        document = cast("dict[str, JsonValue]", pools[key]["document"])
        assert document["fallback"] == "minecraft:empty"
        rows = cast("list[dict[str, JsonValue]]", document["elements"])
        assert all(cast("int", row["weight"]) > 0 for row in rows)
        elements.extend(cast("dict[str, JsonValue]", row["element"]) for row in rows)
    assert len(elements) == 848
    assert {str(e["element_type"]) for e in elements} == {"minecraft:single_pool_element"}
    template_ids = {str(e["location"]) for e in elements}
    assert len(template_ids) == 592

    raw = Path("evidence/item-8/sources/templates-redacted.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "b4a2ed8ff0d16ff06c224119f623f248e75e9c8c838fbf2455bf37936c6d3705")
    templates = cast("dict[str, list[dict[str, JsonValue]]]", json.loads(gzip.decompress(raw)))
    by_id: dict[str, dict[str, JsonValue]] = {}
    for row in templates["resources"]:
        path = str(row["path"])
        if path.startswith("data/repurposed_structures/structure/"):
            key = "repurposed_structures:" + path.split("/structure/", 1)[1].removesuffix(".nbt")
            assert key not in by_id
            by_id[key] = cast("dict[str, JsonValue]", row["document"])
    assert template_ids <= by_id.keys()
    child_pools: set[str] = set()
    for key in template_ids:
        assert by_id[key]["entities"] == []
        for block in cast("list[dict[str, JsonValue]]", by_id[key]["block_entities"]):
            nbt = cast("dict[str, JsonValue]", block["nbt"])
            if nbt.get("id") == "minecraft:jigsaw":
                child_pools.add(str(nbt["pool"]))
    assert child_pools == {f"repurposed_structures:mansions/{v}/mobs/{mob}"
                           for v in variants for mob in ("allays", "evokers", "vindicators")}
    child_templates: set[str] = set()
    for key in child_pools:
        document = cast("dict[str, JsonValue]", pools[key]["document"])
        # The custom generator selects fallback raw templates; these are self-fallbacks.
        assert document["fallback"] == key
        for row in cast("list[dict[str, JsonValue]]", document["elements"]):
            assert cast("int", row["weight"]) > 0
            element = cast("dict[str, JsonValue]", row["element"])
            assert element["element_type"] == "minecraft:single_pool_element"
            assert element["processors"] == "minecraft:empty"
            child_templates.add(str(element["location"]))
    assert child_templates == {
        "repurposed_structures:mansions/hostile_mobs/evoker",
        "repurposed_structures:mansions/hostile_mobs/vindicator",
        *(f"repurposed_structures:mansions/allays/{n}_allay{'s' if n > 1 else ''}"
          for n in (1, 2, 3)),
    }
    assert child_templates <= by_id.keys()


def test_mansion_spawner_lists_and_processors() -> None:
    raw = Path("evidence/item-8/sources/packaged-json-redacted.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "a5279d453f32edf7b1adc5c06b09953785b990b4b01c362b1423ed2f88930fdd")
    catalog = cast("dict[str, list[JsonValue]]", json.loads(gzip.decompress(raw)))
    spawners, _ = select_resources(catalog["resources"], "rs_spawners",
                                  enabled_packs=["vanilla", "mod_data"],
                                  lithostitched_overlay=True)
    mansion_processors: list[JsonValue] = [
        row for row in catalog["resources"] if isinstance(row, dict)
        and "data/repurposed_structures/worldgen/processor_list/mansions/"
        in str(row.get("path"))
    ]
    processors, _ = select_resources(mansion_processors, "worldgen/processor_list",
                                    enabled_packs=["vanilla", "mod_data"],
                                    lithostitched_overlay=True)
    for variant in ("birch", "desert", "jungle", "mangrove", "oak", "savanna", "snowy", "taiga"):
        key = f"repurposed_structures:mansions/{variant}"
        row = spawners[key]
        assert row["archive"] == "repurposed_structures-7.5.21+1.21.1-neoforge.jar"
        assert row["sha256"] == "39439a1a2e54f048e0e61d770536233ccf68443f48fb0188fda1d46958bc7dc0"
        assert row["document"] == {"mobs": [{"name": "minecraft:spider", "weight": 100}]}
        assert processors[key + "/spawner"]["document"] == {"processors": [{
            "processor_type": "repurposed_structures:spawner_randomizing_processor",
            "rs_spawner_resourcelocation": key,
            "valid_block_light_level": {"max_inclusive": 7, "min_inclusive": 0},
        }]}
        assert processors[key + "/mushroom"]["document"] == {"processors": [{
            "processor_type": "repurposed_structures:force_place_mushroom_blocks_processor",
        }]}
