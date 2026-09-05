from __future__ import annotations

import gzip
import hashlib
import json
from pathlib import Path
from typing import TYPE_CHECKING, cast

from mcpack_evidence.item8_resource_selection import select_resources

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_large_aercloud_selected_provider() -> None:
    raw = Path("evidence/item-8/sources/packaged-json-redacted.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "a5279d453f32edf7b1adc5c06b09953785b990b4b01c362b1423ed2f88930fdd")
    catalog = cast("dict[str, list[JsonValue]]", json.loads(gzip.decompress(raw)))
    selected, _ = select_resources(catalog["resources"], "worldgen/structure",
                                  enabled_packs=["vanilla", "mod_data"],
                                  lithostitched_overlay=True)
    row = selected["aether:large_aercloud"]
    assert row["archive"] == "aether-1.21.1-1.5.10-neoforge.jar"
    assert row["sha256"] == "c6590b05dabf5f822bd7447c79efe3801f1426c1437d5fde986d9b620cc43097"
    assert row["document"] == {
        "biomes": "#aether:has_large_aercloud",
        "blocks": {"type": "minecraft:simple_state_provider", "state": {
            "Name": "aether:cold_aercloud", "Properties": {"double_drops": "true"}}},
        "rangeY": 32, "size": 3, "spawn_overrides": {},
        "step": "surface_structures", "type": "aether:large_aercloud",
    }
