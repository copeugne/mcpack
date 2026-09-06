from __future__ import annotations

import gzip
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import TYPE_CHECKING, cast
from zipfile import ZipFile

from mcpack_evidence.item8_registry import read_registry
from mcpack_evidence.item8_resource_selection import select_resources
from mcpack_evidence.item8_sources import retained_sources

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


def test_aether_packaged_candidate_partition() -> None:
    source = next(s for s in retained_sources(Path.cwd())
                  if s.name == "aether-1.21.1-1.5.10-neoforge.jar")
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == (
        "a999a9265eb550a46a0f8eedfee7c3c75371d7f6cf34b7c09ff800e48633e9f8"
    )
    with ZipFile(source.path) as archive:
        names = {n for n in archive.namelist() if not n.endswith("/")}
        assert len(names) == 4514
        templates = {n for n in names if n.endswith(".nbt")}
        assert all(n.startswith("data/aether/structure/") for n in templates)
        assert Counter(n.split("/")[3] for n in templates) == {
            "bronze_dungeon": 6, "silver_dungeon": 11, "gold_dungeon": 4,
            "ruined_portal": 13,
        }
        prefix = "data/aether/worldgen/structure/"
        roots = {"aether:" + n.removeprefix(prefix).removesuffix(".json")
                 for n in names if n.startswith(prefix)}
        assert roots == {"aether:" + n for n in (
            "bronze_dungeon", "silver_dungeon", "gold_dungeon", "large_aercloud",
        )}
        registry = read_registry(Path(
            "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
        ))
        assert roots == {n for n in registry if n.startswith("aether:")}
        prefix = "packs/ruined_portal/data/aether/worldgen/structure/"
        optional_roots = {"aether:" + n.removeprefix(prefix).removesuffix(".json")
                          for n in names if n.startswith(prefix)}
        assert optional_roots == {"aether:ruined_portal" + suffix for suffix in (
            "", "_aether", "_desert", "_jungle", "_mountain", "_swamp",
        )}
        assert optional_roots.isdisjoint(registry)
        configured = {n: cast("dict[str, JsonValue]", json.loads(archive.read(n)))
                      for n in names if n.startswith("data/aether/worldgen/configured_feature/")}
        assert Counter(str(d["type"]) for d in configured.values()) == {
            "minecraft:ore": 6, "minecraft:tree": 4, "minecraft:random_patch": 3,
            "aether:aercloud": 3, "minecraft:random_selector": 2, "minecraft:flower": 2,
            "minecraft:simple_block": 1, "minecraft:spring_feature": 1,
            "aether:crystal_island": 1, "aether:shelf": 1, "aether:lake": 1,
        }
        nested = {n for n in names if n.endswith(".jar")}
        expected = {
            "cumulus_menus-1.21.1-2.0.7-neoforge.jar":
            "2518abccb1a012bb63b5b3ea14b8ed93c82fb5002105c86afadadf518bf149a1",
            "accessories-neoforge-1.1.0-beta.48+1.21.1.jar":
            "a66d62a241c53478a1dfc68381f8476cfb8a6107c2c190b7710f0cdadd839405",
            "nitrogen_internals-1.21.1-1.1.25-neoforge.jar":
            "00cf0e032076f1220c4a8c760a392e12aacb52e4d8e779b9aaf63cd561b40341",
        }
        assert nested == {"META-INF/jarjar/" + n for n in expected}
        for name, digest in expected.items():
            assert hashlib.sha256(archive.read("META-INF/jarjar/" + name)).hexdigest() == digest
