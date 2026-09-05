from __future__ import annotations

import gzip
import hashlib
import json
from pathlib import Path
from typing import TYPE_CHECKING, cast

from mcpack_evidence.item8_resource_selection import select_resources

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_bronze_selected_components() -> None:
    """Bind direct template candidates, not assembled geometry or spawn counts."""
    raw = Path("evidence/item-8/sources/templates-redacted.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "b4a2ed8ff0d16ff06c224119f623f248e75e9c8c838fbf2455bf37936c6d3705")
    catalog = cast("dict[str, list[JsonValue]]", json.loads(gzip.decompress(raw)))
    selected, _ = select_resources(catalog["resources"], "structure",
                                  enabled_packs=["vanilla", "mod_data"],
                                  lithostitched_overlay=True)
    sizes = {"boss_room": [16, 14, 16], "chest_room": [12, 8, 12],
             "end_corridor": [6, 8, 5], "entrance": [6, 8, 1],
             "lobby": [12, 12, 12], "square_tunnel": [6, 6, 6]}
    for suffix, size in sizes.items():
        row = selected[f"aether:bronze_dungeon/{suffix}"]
        assert row["archive"] == "aether-1.21.1-1.5.10-neoforge.jar"
        document = cast("dict[str, JsonValue]", row["document"])
        assert document["size"] == size
        entities = cast("list[dict[str, JsonValue]]", document["entities"])
        assert [cast("dict[str, JsonValue]", e["nbt"])["id"] for e in entities] == (
            ["aether:slider"] if suffix == "boss_room" else [])
        blocks = cast("list[dict[str, JsonValue]]", document["block_entities"])
        nbts = [cast("dict[str, JsonValue]", b["nbt"]) for b in blocks]
        assert [nbt["id"] for nbt in nbts] == (
            ["aether:treasure_chest", "minecraft:structure_block"]
            if suffix == "boss_room" else
            ["minecraft:structure_block"] if suffix == "chest_room" else [])
        markers = [nbt["metadata"] for nbt in nbts
                   if nbt["id"] == "minecraft:structure_block"]
        assert markers == (["Treasure Chest"] if suffix == "boss_room" else
                           ["Chest"] if suffix == "chest_room" else [])


def test_bronze_selected_processor_inputs() -> None:
    raw = Path("evidence/item-8/sources/packaged-json-redacted.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "a5279d453f32edf7b1adc5c06b09953785b990b4b01c362b1423ed2f88930fdd")
    catalog = cast("dict[str, list[JsonValue]]", json.loads(gzip.decompress(raw)))
    selected, _ = select_resources(catalog["resources"], "worldgen/structure",
                                  enabled_packs=["vanilla", "mod_data"],
                                  lithostitched_overlay=True)
    document = cast("dict[str, JsonValue]", selected["aether:bronze_dungeon"]["document"])
    settings = {"boss_room_processors": "aether:bronze_boss_room",
                "generic_room_processors": "aether:bronze_room",
                "tunnel_processors": "aether:bronze_tunnel"}
    assert document["processor_settings"] == settings
    assert document["maxrooms"] == 8
    assert document["aboveBottom"] == 32
    assert document["belowTop"] == 24
    overrides = cast("dict[str, JsonValue]", document["spawn_overrides"])
    assert len(overrides) == 12
    assert all(v == {"bounding_box": "piece", "spawns": []} for v in overrides.values())
    # Select only current consumers; unrelated provider collisions are separate gaps.
    candidates: list[JsonValue] = [
        row for row in catalog["resources"] if isinstance(row, dict)
        and "data/aether/worldgen/processor_list/bronze_" in str(row.get("path"))]
    processors, _ = select_resources(candidates, "worldgen/processor_list",
                                    enabled_packs=["vanilla", "mod_data"],
                                    lithostitched_overlay=True)
    assert set(processors) == set(settings.values())
    expected_types = {
        "aether:bronze_boss_room": ["minecraft:rule", "aether:boss_room"],
        "aether:bronze_room": ["minecraft:rule", "minecraft:rule",
                              "minecraft:protected_blocks", "aether:double_drops"],
        "aether:bronze_tunnel": ["minecraft:protected_blocks", "minecraft:rule",
                                "aether:double_drops"],
    }
    for key, types in expected_types.items():
        doc = cast("dict[str, JsonValue]", processors[key]["document"])
        entries = cast("list[dict[str, JsonValue]]", doc["processors"])
        assert [entry["processor_type"] for entry in entries] == types
