from __future__ import annotations

import hashlib
import json
import tomllib
from collections import Counter
from pathlib import Path
from typing import cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources


def test_coffee_delight_payload_and_entries() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name == "coffee_delight-1.4.1.jar")
    assert source.sha256 == "86ff8637d157a723f4d790e2478fa50f87a2e7b7c4b4ed6a64fb3d69a0219082"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    directory = Path("evidence/item-8/sources/coffee-delight-provider")
    raw = (directory / "identities.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "4c0bf1002f4b2838cb7e2b4938aa5a9b964266defbb604acb874d47927ef84ee"
    )
    rows = cast("list[dict[str, str]]", json.loads(raw))
    captured = {r["class"] for r in rows}
    assert len(rows) == len(captured) == 5
    with ZipFile(source.path) as archive:
        names = [n for n in archive.namelist() if not n.endswith("/")]
        assert len(names) == len(set(names)) == 295
        classes = {n for n in names if n.endswith(".class")}
        assets = {n for n in names if n.startswith("assets/")}
        data = {n for n in names if n.startswith("data/")}
        assert (len(classes), len(assets), len(data)) == (30, 167, 90)
        assert set(names) - classes - assets - data == {
            "META-INF/MANIFEST.MF", "META-INF/neoforge.mods.toml", "logo.png",
            *(".cache/" + digest for digest in (
                "103d9f3f36b01595f1aa5172191e60eff02e6924",
                "40493a8b4bce06269f70628070ba8b72849b7951",
                "59eb3dbb5f86130e09b3c62d89b9525ee01cf52d",
                "9fb1092f32d4fcbf9e061ffd718d4ec689c6c95e",
                "b805d01d5e28abcf6718aac064e821f49f096256",
            )),
        }
        assert all(n.endswith((".json", ".png")) for n in assets)
        assert all(n.endswith(".json") for n in data)
        assert Counter(n.split("/")[2] for n in data) == {
            "advancement": 20, "loot_table": 44, "recipe": 23, "worldgen": 2, "neoforge": 1,
        }
        for row in rows:
            assert row["archive"] == source.name
            assert row["archive_sha256"] == source.sha256
            assert hashlib.sha256(archive.read(row["class"])).hexdigest() == row["class_sha256"]
            assert hashlib.sha256((directory / row["disassembly"]).read_bytes()).hexdigest() == (
                row["disassembly_sha256"]
            )
        assert {n for n in classes if b"Lnet/neoforged/fml/common/Mod;" in archive.read(n)} == {
            "lcyzsdh/coffee_delight/CoffeeDelight.class",
        }
        assert {n for n in classes
                if b"Lnet/neoforged/fml/common/EventBusSubscriber;" in archive.read(n)} == {
            "lcyzsdh/coffee_delight/data/ModDataGenerator.class",
        }
        assert not any(
            b"net/neoforged/neoforge/common/NeoForge" in archive.read(n) for n in classes
        )
        assert {n for n in classes if "/worldgen/" in n} <= captured
        metadata = tomllib.loads(archive.read("META-INF/neoforge.mods.toml").decode())
        assert set(metadata) == {
            "modLoader", "loaderVersion", "license", "issueTrackerURL", "mods", "dependencies",
        }
        assert metadata["modLoader"] == "javafml"


def test_coffee_delight_generation_is_a_vanilla_plant_patch() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name == "coffee_delight-1.4.1.jar")
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        assert json.loads(archive.read(
            "data/coffee_delight/neoforge/biome_modifier/add_coffee_bush.json"
        )) == {
            "type": "neoforge:add_features", "biomes": "#minecraft:has_structure/desert_pyramid",
            "features": "coffee_delight:coffee_bush", "step": "vegetal_decoration",
        }
        assert json.loads(archive.read(
            "data/coffee_delight/worldgen/placed_feature/coffee_bush.json"
        )) == {
            "feature": "coffee_delight:coffee_bush", "placement": [
                {"type": "minecraft:rarity_filter", "chance": 15},
                {"type": "minecraft:in_square"},
                {"type": "minecraft:heightmap", "heightmap": "MOTION_BLOCKING"},
            ],
        }
        assert json.loads(archive.read(
            "data/coffee_delight/worldgen/configured_feature/coffee_bush.json"
        )) == {
            "type": "minecraft:random_patch", "config": {
                "tries": 96, "xz_spread": 7, "y_spread": 3, "feature": {
                    "feature": {
                        "type": "minecraft:simple_block", "config": {"to_place": {
                            "type": "minecraft:simple_state_provider", "state": {
                                "Name": "coffee_delight:coffee_bush", "Properties": {"age": "3"},
                            },
                        }},
                    },
                    "placement": [{"type": "minecraft:block_predicate_filter", "predicate": {
                        "type": "minecraft:all_of", "predicates": [
                            {"type": "minecraft:matching_blocks", "blocks": "minecraft:air"},
                            {"type": "minecraft:matching_blocks", "blocks": "minecraft:sand",
                             "offset": [0, -1, 0]},
                        ],
                    }}],
                },
            },
        }
