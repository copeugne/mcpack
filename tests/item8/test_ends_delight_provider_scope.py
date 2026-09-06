from __future__ import annotations

import hashlib
import json
import tomllib
from collections import Counter
from pathlib import Path
from typing import cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources


def test_ends_delight_payload_and_entry_coverage() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name.startswith("ends_delight-"))
    assert source.sha256 == "65277056eb9ee9e1025633b83cb1b2568ec846dacd16507a35698244f4196881"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    directory = Path("evidence/item-8/sources/ends-delight-provider")
    raw = (directory / "identities.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "0d79af565f8cceb48e26c0de90084c58745981bd48de092aaed4580d324093a5"
    )
    rows = cast("list[dict[str, str]]", json.loads(raw))
    captured = {r["class"] for r in rows}
    assert len(rows) == len(captured) == 5
    with ZipFile(source.path) as archive:
        names = [n for n in archive.namelist() if not n.endswith("/")]
        assert len(names) == len(set(names)) == 373
        classes = {n for n in names if n.endswith(".class")}
        assets = {n for n in names if n.startswith("assets/")}
        data = {n for n in names if n.startswith("data/")}
        assert (len(classes), len(assets), len(data)) == (44, 201, 124)
        assert set(names) - classes - assets - data == {
            "META-INF/MANIFEST.MF", "META-INF/neoforge.mods.toml", "logo.png", "pack.mcmeta",
        }
        assert all(n.endswith((".json", ".png", ".mcmeta")) for n in assets)
        assert all(n.endswith(".json") for n in data)
        assert Counter(n.split("/")[2] for n in data) == {
            "tags": 16, "advancement": 12, "damage_type": 1, "loot_modifiers": 10,
            "loot_table": 7, "neoforge": 1, "recipe": 75, "worldgen": 2,
        }
        for row in rows:
            assert row["archive"] == source.name
            assert row["archive_sha256"] == source.sha256
            assert hashlib.sha256(archive.read(row["class"])).hexdigest() == row["class_sha256"]
            assert hashlib.sha256((directory / row["disassembly"]).read_bytes()).hexdigest() == (
                row["disassembly_sha256"]
            )
        entries = {n for n in classes if any(tag in archive.read(n) for tag in (
            b"Lnet/neoforged/fml/common/Mod;", b"Lnet/neoforged/fml/common/EventBusSubscriber;",
        ))}
        assert len(entries) == 3
        assert entries <= captured
        assert {n for n in classes if "/worldgen/" in n} == {
            "cn/foggyhillside/ends_delight/worldgen/ChorusSucculentFeature.class",
        }
        assert not any(
            b"net/neoforged/neoforge/common/NeoForge" in archive.read(n) for n in classes
        )
        metadata = tomllib.loads(archive.read("META-INF/neoforge.mods.toml").decode())
        assert set(metadata) == {"modLoader", "loaderVersion", "license", "mods", "dependencies"}
        assert metadata["modLoader"] == "javafml"


def test_ends_delight_single_crop_generator_consumers() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name.startswith("ends_delight-"))
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        assert json.loads(archive.read(
            "data/ends_delight/neoforge/biome_modifier/add_chorus_succulent.json"
        )) == {
            "type": "neoforge:add_features", "biomes": "minecraft:end_highlands",
            "features": "ends_delight:chorus_succulent", "step": "vegetal_decoration",
        }
        assert json.loads(archive.read(
            "data/ends_delight/worldgen/configured_feature/chorus_succulent.json"
        )) == {"type": "ends_delight:chorus_succulent", "config": {"count": 20}}
        assert json.loads(archive.read(
            "data/ends_delight/worldgen/placed_feature/chorus_succulent.json"
        )) == {
            "feature": "ends_delight:chorus_succulent", "placement": [
                {"type": "minecraft:rarity_filter", "chance": 8},
                {"type": "minecraft:in_square"},
                {"type": "minecraft:heightmap", "heightmap": "WORLD_SURFACE"},
                {"type": "minecraft:biome"},
            ],
        }
