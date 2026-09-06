from __future__ import annotations

import hashlib
import json
import tomllib
from collections import Counter
from pathlib import Path
from typing import TYPE_CHECKING, cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_aethers_delight_payload_and_entries() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name.startswith("aethersdelight-"))
    assert source.sha256 == "11b07fce5c69682290106fc1c79fc447606791239a18965f71114f360e8a947e"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    directory = Path("evidence/item-8/sources/aethers-delight-provider")
    raw = (directory / "identities.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "d81bb46059e7f892de6c77b74ef25b553a9f3400d45d6ebb7efe5304e4263000"
    )
    rows = cast("list[dict[str, str]]", json.loads(raw))
    captured = {r["class"] for r in rows}
    assert len(rows) == len(captured) == 6
    with ZipFile(source.path) as archive:
        names = [n for n in archive.namelist() if not n.endswith("/")]
        assert len(names) == len(set(names)) == 748
        assert Counter("classes" if n.endswith(".class") else n.split("/")[0]
                       for n in names) == {
            "classes": 58, "assets": 294, "data": 362, "packs": 23, ".cache": 7,
            "META-INF": 2, "logo.png": 1, "pack.mcmeta": 1,
        }
        assert {n for n in names if n.startswith("META-INF/")} == {
            "META-INF/MANIFEST.MF", "META-INF/neoforge.mods.toml",
        }
        assert all(n.endswith((".json", ".png", ".mcmeta"))
                   for n in names if n.startswith("assets/"))
        assert all(n.endswith(".json") for n in names if n.startswith("data/"))
        assert all(n.endswith((".json", "/pack.mcmeta"))
                   for n in names if n.startswith("packs/"))
        assert Counter(n.split("/")[2] for n in names if n.startswith("data/")) == {
            "advancement": 105, "recipe": 125, "recipes": 3, "tags": 76,
            "loot_modifiers": 11, "loot_table": 26, "neoforge": 5, "worldgen": 10,
            "data_maps": 1,
        }
        for row in rows:
            assert row["archive"] == source.name
            assert row["archive_sha256"] == source.sha256
            assert hashlib.sha256(archive.read(row["class"])).hexdigest() == row["class_sha256"]
            assert hashlib.sha256((directory / row["disassembly"]).read_bytes()).hexdigest() == (
                row["disassembly_sha256"]
            )
        classes = {n for n in names if n.endswith(".class")}
        assert {n for n in classes if any(tag in archive.read(n) for tag in (
            b"Lnet/neoforged/fml/common/Mod;", b"Lnet/neoforged/fml/common/EventBusSubscriber;",
        ))} == captured
        assert {n for n in classes
                if b"net/neoforged/neoforge/common/NeoForge" in archive.read(n)} == {
            "net/zjjohn121110/aethersdelight/AethersDelight.class",
        }
        metadata = tomllib.loads(archive.read("META-INF/neoforge.mods.toml").decode())
        assert set(metadata) == {"modLoader", "loaderVersion", "license", "mods", "dependencies"}
        assert metadata["modLoader"] == "javafml"


def test_aethers_delight_five_ore_and_plant_chains() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name.startswith("aethersdelight-"))
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        consumed: set[str] = set()
        for name in ("arkenium_ore", "peppermint_bush", "wild_ginger", "wild_leek", "wild_parsnip"):
            prefix = "data/aethersdelight/"
            doc = cast("dict[str, JsonValue]", json.loads(archive.read(
                prefix + f"worldgen/configured_feature/{name}.json"
            )))
            assert doc["type"] == (
                "minecraft:ore" if name == "arkenium_ore" else "minecraft:random_patch"
                if name == "peppermint_bush" else "minecraft:no_bonemeal_flower"
            )
            states: set[str] = set()
            pending: list[JsonValue] = [doc]
            while pending:
                node = pending.pop()
                if isinstance(node, dict):
                    if "Name" in node:
                        states.add(str(node["Name"]))
                    pending.extend(node.values())
                elif isinstance(node, list):
                    pending.extend(node)
            assert states == {"aethersdelight:" + name}
            placed = cast("dict[str, JsonValue]", json.loads(archive.read(
                prefix + f"worldgen/placed_feature/{name}_placed.json"
            )))
            assert placed["feature"] == "aethersdelight:" + name
            modifier = cast("dict[str, JsonValue]", json.loads(archive.read(
                prefix + f"neoforge/biome_modifier/add_{name}.json"
            )))
            assert modifier["type"] == "neoforge:add_features"
            assert modifier["features"] == f"aethersdelight:{name}_placed"
            assert modifier["step"] == (
                "underground_ores" if name == "arkenium_ore" else "vegetal_decoration"
            )
            consumed.update({
                prefix + f"worldgen/configured_feature/{name}.json",
                prefix + f"worldgen/placed_feature/{name}_placed.json",
                prefix + f"neoforge/biome_modifier/add_{name}.json",
            })
        assert consumed == {n for n in archive.namelist() if n.startswith("data/")
                            and n.endswith(".json")
                            and any(k in n for k in ("/worldgen/", "/biome_modifier/"))
                            and "/tags/" not in n}


def test_aethers_delight_packaged_compatibility_data_roles() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name.startswith("aethersdelight-"))
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        packs = {n for n in archive.namelist() if n.startswith("packs/") and not n.endswith("/")}
        assert {n.split("/")[2] for n in packs} == {"aether_redux_compat", "ancient_aether_compat"}
        for pack, expected in (
            ("aether_redux_compat", {"recipes": 3, "loot_modifiers": 4, "pack.mcmeta": 1}),
            ("ancient_aether_compat", {
                "forge": 1, "loot_modifiers": 3, "recipes": 6,
                "worldgen": 3, "tags": 1, "pack.mcmeta": 1,
            }),
        ):
            prefix = f"packs/compat/{pack}/"
            assert Counter(
                n.removeprefix(prefix).split("/")[2] if "/data/" in n else n.removeprefix(prefix)
                for n in packs if n.startswith(prefix)
            ) == expected
        prefix = "packs/compat/ancient_aether_compat/data/aethersdelight/"
        ore = cast("dict[str, JsonValue]", json.loads(archive.read(
            prefix + "worldgen/configured_feature/wynd_arkenium_ore.json"
        )))
        assert ore == {"type": "minecraft:ore", "config": {
            "discard_chance_on_air_exposure": 0.0, "size": 9, "targets": [{
                "state": {"Name": "aethersdelight:arkenium_ore"},
                "target": {"predicate_type": "minecraft:tag_match", "tag": "aether:holystone"},
            }],
        }}
        for name in ("arkenium_ore_placed", "wynd_arkenium_ore_placed"):
            placed = cast("dict[str, JsonValue]", json.loads(archive.read(
                prefix + f"worldgen/placed_feature/{name}.json"
            )))
            assert placed["feature"] == "aethersdelight:arkenium_ore"
        assert json.loads(archive.read(
            prefix + "forge/biome_modifier/add_wynd_arkenium_ore.json"
        )) == {
            "type": "forge:add_features", "biomes": "ancient_aether:wyndcap_peaks",
            "features": "aethersdelight:wynd_arkenium_ore_placed", "step": "underground_ores",
        }
