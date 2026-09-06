from __future__ import annotations

import gzip
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import TYPE_CHECKING, cast
from zipfile import ZipFile

from mcpack_evidence.item8_registry import read_registry
from mcpack_evidence.item8_sources import retained_sources

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_deep_aether_nested_runtime_selection() -> None:
    raw = Path("evidence/raw/item8/registry-r1/debug.log").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "e5b47378d791027242ba28dd36c999c07ae4e01a1b90e1534e66bcd42c1e694b"
    )
    lines = raw.decode().splitlines()
    assert any("JarSelector/" in line and "passed in as source: terrablender" in line
               and line.endswith("/mods/TerraBlender-neoforge-1.21.1-4.1.0.8.jar")
               for line in lines)
    assert "\t\tTerraBlender 4.1.0.8 (terrablender)" in lines
    assert "\t\tTerraBlender 4.1.0.3 (terrablender)" not in lines
    assert any('Found mod file "aeroblender-1.21.1-1.0.0-neoforge.jar"' in line
               and "[parent: deep_aether-1.21.1-1.1.5.1.jar, locator: jarinjar," in line
               for line in lines)
    assert "\t\tAeroBlender 1.0.0 (aeroblender)" in lines


def test_deep_aether_packaged_candidate_partition() -> None:
    source = next(s for s in retained_sources(Path.cwd())
                  if s.name == "deep_aether-1.21.1-1.1.5.1.jar")
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == (
        "0f55ad970715bb933344e785b2c35a7354dfba25ffd426c0b68921d08bbe0ce5"
    )
    raw = Path("evidence/item-8/sources/packaged-json-redacted.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "a5279d453f32edf7b1adc5c06b09953785b990b4b01c362b1423ed2f88930fdd"
    )
    catalog = cast("dict[str, list[dict[str, JsonValue]]]", json.loads(gzip.decompress(raw)))
    rows = {str(r["path"]): cast("dict[str, JsonValue]", r["document"])
            for r in catalog["resources"] if r["archive"] == source.name}
    prefix = "data/deep_aether/worldgen/"
    roots = {p.removeprefix(prefix + "structure/").removesuffix(".json"): d
             for p, d in rows.items() if p.startswith(prefix + "structure/")}
    assert set(roots) == {"altar_camp", "brass_dungeon", "campfire", "combiner_corridor"}
    registry = read_registry(Path(
        "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
    ))
    assert {"deep_aether:" + n for n in roots} == {
        n for n in registry if n.startswith("deep_aether:")
    }
    for name in ("altar_camp", "campfire", "combiner_corridor"):
        assert roots[name]["biomes"] == "deep_aether:sacred_lands"
        assert roots[name]["start_pool"] == "deep_aether:" + name
        assert roots[name]["type"] == "deep_aether:deep_aether_jigsaw"
    assert roots["brass_dungeon"]["type"] == "deep_aether:brass_dungeon"
    assert Counter(str(d["type"]) for p, d in rows.items()
                   if p.startswith(prefix + "configured_feature/")) == {
        "minecraft:tree": 11, "minecraft:flower": 10, "minecraft:random_selector": 9,
        "minecraft:random_patch": 5, "minecraft:simple_block": 4, "minecraft:ore": 4,
        "deep_aether:aercloud_cloud": 2, "minecraft:vegetation_patch": 2,
        "deep_aether:fallen_tree": 2, "deep_aether:improved_mushroom_feature": 2,
        "aether:lake": 1, "deep_aether:rain_aercloud_cloud": 1, "deep_aether:aercloud_roots": 1,
        "minecraft:huge_red_mushroom": 1, "deep_aether:poison_lake": 1,
        "minecraft:spring_feature": 1, "aether:aercloud": 1, "deep_aether:totem": 1,
        "aether:shelf": 1,
    }
    with ZipFile(source.path) as archive:
        names = {n for n in archive.namelist() if not n.endswith("/")}
        assert len(names) == 4136
        expected = {f"brass_dungeon/brass_dungeon_room_{i}{suffix}.nbt"
                    for i in range(5) for suffix in ("", "_boss")}
        expected |= {"brass_dungeon/door.nbt", "brass_dungeon/room_part_up.nbt"}
        expected |= {"sacred_lands/" + name + ".nbt"
                     for name in ("altar_camp", "campfire", "combiner_corridor")}
        assert {n for n in names if n.endswith(".nbt")} == {
            "data/deep_aether/structure/" + n for n in expected
        }
        nested = {
            "aeroblender-1.21.1-1.0.0-neoforge.jar":
            "85739c5737ae2d3a289022aaa2834c4889838a3e6c53125a5334535c12ae7588",
            "TerraBlender-neoforge-1.21.1-4.1.0.3.jar":
            "4ea41173bcce99915427cac633a08cbe4256ea990801b8319fcc617076d453cd",
        }
        assert {n for n in names if n.endswith(".jar")} == {
            "META-INF/jarjar/" + n for n in nested
        }
        for name, digest in nested.items():
            assert hashlib.sha256(archive.read("META-INF/jarjar/" + name)).hexdigest() == digest
