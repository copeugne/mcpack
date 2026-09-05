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
