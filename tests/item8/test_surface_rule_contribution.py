from __future__ import annotations

import gzip
import hashlib
import json
from pathlib import Path
from typing import TYPE_CHECKING, cast

from mcpack_evidence.item8_resource_selection import select_resources

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_regions_unexplored_surface_references_end_in_terrain_blocks() -> None:
    root = Path(__file__).resolve().parents[2]
    raw = (root / "evidence/item-8/sources/packaged-json-redacted.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "a5279d453f32edf7b1adc5c06b09953785b990b4b01c362b1423ed2f88930fdd"
    )
    catalog = cast("dict[str, JsonValue]", json.loads(gzip.decompress(raw)))
    resources = cast("list[JsonValue]", catalog["resources"])
    rules, _ = select_resources(
        resources, "lithostitched/surface_rule",
        enabled_packs=["vanilla", "mod_data"], lithostitched_overlay=True,
    )
    seen: set[str] = set()
    blocks: set[str] = set()

    def walk(value: JsonValue) -> None:
        assert isinstance(value, dict)
        kind = value["type"]
        if kind == "minecraft:block":
            assert set(value) == {"type", "result_state"}
            state = value["result_state"]
            assert isinstance(state, dict)
            assert isinstance(state["Name"], str)
            assert set(state) <= {"Name", "Properties"}
            blocks.add(state["Name"])
        elif kind == "minecraft:condition":
            assert set(value) == {"type", "if_true", "then_run"}
            walk(value["then_run"])
        elif kind == "minecraft:sequence":
            assert set(value) == {"type", "sequence"}
            assert isinstance(value["sequence"], list)
            for child in value["sequence"]:
                walk(child)
        elif kind == "regions_unexplored:config":
            assert set(value) == {"type", "key", "on_enabled", "on_disabled"}
            walk(value["on_enabled"])
            walk(value["on_disabled"])
        else:
            assert kind == "lithostitched:reference", value
            assert set(value) == {"type", "rules"}
            references = value["rules"]
            if isinstance(references, str):
                references = [references]
            assert isinstance(references, list)
            assert references
            for identifier in references:
                assert isinstance(identifier, str)
                assert identifier.startswith("regions_unexplored:")
                if identifier not in seen:
                    seen.add(identifier)
                    walk(rules[identifier]["document"])

    walk({"type": "lithostitched:reference", "rules": "regions_unexplored:overworld"})
    assert len(seen) == 52
    assert all(rules[key]["archive"] == "regions-unexplored-0.6.1-neoforge-21.1.jar"
               for key in seen)
    assert blocks == {
        *("minecraft:" + name for name in (
            "calcite", "coarse_dirt", "cobblestone", "deepslate", "dirt", "grass_block",
            "gravel", "mud", "mycelium", "packed_ice", "podzol", "powder_snow", "red_sand",
            "red_sandstone", "sand", "sandstone", "snow_block", "stone", "terracotta", "water",
        )),
        *("regions_unexplored:" + name for name in (
            "alpha_grass_block", "argillite", "argillite_grass_block", "ash", "ashen_dirt",
            "chalk", "chalk_grass_block", "deepslate_prismoss", "deepslate_viridescent_nylium",
            "mossy_stone", "peat_coarse_dirt", "peat_dirt", "peat_grass_block", "peat_mud",
            "peat_podzol", "prismoss", "raw_redstone_block", "silt_coarse_dirt", "silt_dirt",
            "silt_grass_block", "silt_podzol", "viridescent_nylium",
        )),
    }
