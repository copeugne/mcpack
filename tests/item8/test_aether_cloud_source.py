from __future__ import annotations

import gzip
import hashlib
import io
import json
import tomllib
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
        for name in names:
            if name.startswith(prefix) and name.endswith(".json"):
                assert json.loads(archive.read(name))["type"] == "aether:ruined_portal"
        portal_prefix = "data/aether/structure/ruined_portal/"
        assert {n.removeprefix(portal_prefix).removesuffix(".nbt")
                for n in templates if n.startswith(portal_prefix)} == (
            {f"portal_{i}" for i in range(1, 11)}
            | {f"giant_portal_{i}" for i in range(1, 4)}
        )
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
            if name.startswith(("cumulus_menus-", "nitrogen_internals-")):
                with ZipFile(io.BytesIO(archive.read("META-INF/jarjar/" + name))) as library:
                    files = {n for n in library.namelist() if not n.endswith("/")}
                    assert not any(n.startswith(("data/", "packs/"))
                                   or n.endswith(".jar") for n in files)
                    services = {n: library.read(n).decode().strip() for n in files
                                if n.startswith("META-INF/services/")}
                    assert services == ({
                        "META-INF/services/com.aetherteam.cumulus.platform.services.IPlatformHelper":
                        "com.aetherteam.cumulus.platform.NeoForgePlatformHelper",
                    } if name.startswith("cumulus_") else {})
                    common_mixins: list[str] = []
                    for file in files:
                        if file.endswith("mixins.json"):
                            config = cast("dict[str, JsonValue]", json.loads(library.read(file)))
                            common_mixins.extend(cast("list[str]", config.get("mixins", [])))
                    assert common_mixins == (
                        ["client.LevelStorageSourceMixin"] if name.startswith("cumulus_") else []
                    )


def test_aether_nested_runtime_selection() -> None:
    raw = Path("evidence/raw/item8/registry-r1/debug.log").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "e5b47378d791027242ba28dd36c999c07ae4e01a1b90e1534e66bcd42c1e694b"
    )
    lines = raw.decode().splitlines()
    assert any("JarSelector/" in line and "passed in as source: accessories" in line
               and line.endswith("/mods/accessories-neoforge-1.1.0-beta.53+1.21.1.jar")
               for line in lines)
    assert "\t\tAccessories 1.1.0-beta.53+1.21.1 (accessories)" in lines
    assert "\t\tAccessories 1.1.0-beta.48+1.21.1 (accessories)" not in lines
    for archive, mod in (
        ("cumulus_menus-1.21.1-2.0.7-neoforge.jar", "Cumulus 2.0.7 (cumulus_menus)"),
        ("nitrogen_internals-1.21.1-1.1.25-neoforge.jar", "Nitrogen 1.1.25 (nitrogen_internals)"),
    ):
        assert any(f'Found mod file "{archive}"' in line
                   and "[parent: aether-1.21.1-1.5.10-neoforge.jar, locator: jarinjar," in line
                   for line in lines)
        assert "\t\t" + mod in lines


def test_aether_silver_gold_component_candidates() -> None:
    source = next(s for s in retained_sources(Path.cwd())
                  if s.name == "aether-1.21.1-1.5.10-neoforge.jar")
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == (
        "a999a9265eb550a46a0f8eedfee7c3c75371d7f6cf34b7c09ff800e48633e9f8"
    )
    with ZipFile(source.path) as archive:
        # Exact captured call-site names, not a simulation of successful assembly.
        expected = {
            "silver_dungeon": {"floor", "door", "wall", "tall_staircase", "boss_door",
                               "staircase", "chest_room", "rear", "boss_room", "skeleton"},
            "gold_dungeon": {"island", "boss_room", "stub", "tunnel"},
        }
        for family, candidates in expected.items():
            prefix = "data/aether/structure/" + family + "/"
            packaged = {n.removeprefix(prefix).removesuffix(".nbt")
                        for n in archive.namelist() if n.startswith(prefix) and n.endswith(".nbt")}
            assert candidates <= packaged
            assert packaged - candidates == ({"test_door"} if family == "silver_dungeon" else set())
        assert not any(b"test_door" in archive.read(n) for n in archive.namelist()
                       if n.endswith(".class"))
        prefix = "com/aetherteam/aether/world/structurepiece/"
        for family, piece in (("silver", "Silver"), ("gold", "Gold")):
            raw = archive.read(prefix + family + "dungeon/" + piece + "DungeonPiece.class")
            assert (family + "_dungeon/\x01").encode() in raw
        for name, digest in (
            ("aether-custom-entry",
             "e33ddae6869cc516beafc2eff72976b2db2ee6d7602443d2af389c2778b01954"),
            ("aether-provider", "917c3ffbb199539bfbe375f4a7381d4498f327a2ce9d5cdc28ad01d978f604ee"),
            ("aether-common-hooks",
             "9c3b21c8bf2eab73550acc646a9c74081c15daac08c941367f298adf0bb8c50f"),
        ):
            folder = Path("evidence/item-8/sources") / name
            raw = (folder / "identities.json").read_bytes()
            assert hashlib.sha256(raw).hexdigest() == digest
            for row in cast("list[dict[str, str]]", json.loads(raw)):
                assert row["archive"] == source.name
                assert row["archive_sha256"] == source.sha256
                assert hashlib.sha256(archive.read(row["class"])).hexdigest() == row["class_sha256"]
                assert hashlib.sha256((folder / row["disassembly"]).read_bytes()).hexdigest() == (
                    row["disassembly_sha256"]
                )


def test_aether_optional_portal_setting() -> None:
    raw = Path("evidence/item-6/frozen/config/aether-common.toml").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "67d50cb36d6b96c7cc47d613012c7d481cb6aef2b67540f8fb0ec5b7b7aa5ef2"
    )
    config = tomllib.loads(raw.decode())
    assert config["Data Pack"]["Add Ruined Portals automatically"] is False


def test_aether_holiday_tree_candidate_inputs() -> None:
    source = next(s for s in retained_sources(Path.cwd())
                  if s.name == "aether-1.21.1-1.5.10-neoforge.jar")
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == (
        "a999a9265eb550a46a0f8eedfee7c3c75371d7f6cf34b7c09ff800e48633e9f8"
    )
    with ZipFile(source.path) as archive:
        prefix = "data/aether/worldgen/"
        config = cast("dict[str, JsonValue]", json.loads(archive.read(
            prefix + "configured_feature/holiday_tree.json"
        )))
        assert config["type"] == "minecraft:tree"
        settings = cast("dict[str, JsonValue]", config["config"])
        decorators = cast("list[dict[str, JsonValue]]", settings["decorators"])
        assert len(decorators) == 1
        assert decorators[0]["type"] == "aether:holiday_tree_decorator"
        provider = cast("dict[str, JsonValue]", decorators[0]["provider"])
        assert provider["type"] == "minecraft:weighted_state_provider"
        assert provider["entries"] == [
            {"data": {"Name": "minecraft:snow", "Properties": {"layers": "1"}}, "weight": 10},
            {"data": {"Name": "aether:present"}, "weight": 1},
        ]
        placed = cast("dict[str, JsonValue]", json.loads(archive.read(
            prefix + "placed_feature/holiday_tree.json"
        )))
        assert placed["feature"] == "aether:holiday_tree"
        assert {"type": "aether:holiday_filter"} in cast("list[JsonValue]", placed["placement"])
        biomes = {n for n in archive.namelist()
                  if n.startswith(prefix + "biome/") and n.endswith(".json")}
        assert biomes == {prefix + "biome/skyroot_" + n + ".json"
                          for n in ("forest", "woodland", "meadow", "grove")}
        for name in biomes:
            biome = cast("dict[str, JsonValue]", json.loads(archive.read(name)))
            assert any("aether:holiday_tree" in layer
                       for layer in cast("list[list[str]]", biome["features"]))
    raw = Path("evidence/item-6/frozen/config/aether-server.toml").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "578abca7702fcecdb39845a7043f6ec1c504f153f6d3b4af45daedb29df931de"
    )
    frozen = cast("dict[str, dict[str, JsonValue]]", tomllib.loads(raw.decode()))
    assert frozen["World Generation"]["Generate Holiday Trees always"] is False
    assert frozen["World Generation"]["Generate Holiday Trees seasonally"] is True
