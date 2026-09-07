from __future__ import annotations

import hashlib
import json
from collections import Counter
from io import BytesIO
from pathlib import Path
from typing import TYPE_CHECKING, cast
from zipfile import ZipFile

import pytest

from mcpack_evidence.item8_sources import retained_sources

if TYPE_CHECKING:
    from pydantic import JsonValue


@pytest.mark.parametrize("nested", [False, True])
def test_ubes_delight_payload_and_inspected_entries(nested: bool) -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name.startswith("ubesdelight-"))
    assert source.sha256 == "abbdf3927b17aef8a44a418c6f292e584a61d1fab4115d33a71c3d0a35b1e2b4"
    raw = source.path.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == source.sha256
    archive_id = source.name
    if nested:
        member = "META-INF/jars/midnightlib-1.9.2+1.21.1-neoforge.jar"
        with ZipFile(BytesIO(raw)) as parent:
            raw = parent.read(member)
        archive_id += "!/" + member
        assert hashlib.sha256(raw).hexdigest() == (
            "5dc6cc72e507c3fb5b5bac59e79da2aee74a9d1345dbc48e0ccecd608ac9286a"
        )
    archive_sha = hashlib.sha256(raw).hexdigest()
    with ZipFile(BytesIO(raw)) as archive:
        names = [n for n in archive.namelist() if not n.endswith("/")]
        assert len(names) == len(set(names)) == (45 if nested else 1336)
        assert Counter("classes" if n.endswith(".class") else n.split("/")[0]
                       for n in names) == ({
            "classes": 24, "assets": 16, "META-INF": 3,
            "midnightlib.mixins.json": 1, "midnightlib.png": 1,
        } if nested else {
            "classes": 140, "assets": 729, "data": 448, ".cache": 7, "META-INF": 4,
            "resourcepacks": 3, "pack.mcmeta": 1, "ubesdelight-common.mixins.json": 1,
            "ubesdelight.mixins.json": 1, "ubesdelight.accesswidener": 1, "waila_plugins.json": 1,
        })
        assert {n for n in names if n.startswith("META-INF/")} == {
            "META-INF/MANIFEST.MF", "META-INF/neoforge.mods.toml",
            *(["META-INF/architectury-loom-nesting-metadata.json"] if nested else [
                "META-INF/jarjar/metadata.json",
                "META-INF/jars/midnightlib-1.9.2+1.21.1-neoforge.jar",
            ]),
        }
        assert all(n.endswith((".json", ".png", ".mcmeta"))
                   for n in names if n.startswith("assets/"))
        captures = (
            ("ubes-midnightlib", 3,
             "41ab47040644ab1dfc3ec5b67c1ccb679960c8df1fde22fa992b70a85cb293cc"),
            ("ubes-midnightlib-delegates", 2,
             "7452a1b57ebcff8b9aedde0c4bde57d6db5c7a661a08cf7219896d4e2c3dc817"),
        ) if nested else (
            ("ubes-delight-provider", 17,
             "9d54b85bb4428a9f5bcfe691d8760fffff0bd768d88bff4757dd0584e284dc9c"),
            ("ubes-config-delegates", 2,
             "7f66a6ae89d97fd1e117a53a6b86fad2e8d45ad83a5fd0228ce83acf77fbef41"),
        )
        captured: set[str] = set()
        for label, count, digest in captures:
            directory = Path("evidence/item-8/sources") / label
            raw = (directory / "identities.json").read_bytes()
            assert hashlib.sha256(raw).hexdigest() == digest
            rows = cast("list[dict[str, str]]", json.loads(raw))
            assert len(rows) == len({r["class"] for r in rows}) == count
            for row in rows:
                captured.add(row["class"])
                assert row["archive"] == archive_id
                assert row["archive_sha256"] == archive_sha
                assert hashlib.sha256(archive.read(row["class"])).hexdigest() == row["class_sha256"]
                disassembly = (directory / row["disassembly"]).read_bytes()
                assert hashlib.sha256(disassembly).hexdigest() == row["disassembly_sha256"]
        classes = {n for n in names if n.endswith(".class")}
        entries = {n for n in classes if any(tag in archive.read(n) for tag in (
            b"Lnet/neoforged/fml/common/Mod;", b"Lnet/neoforged/fml/common/EventBusSubscriber;",
        ))}
        assert len(entries) == (3 if nested else 4)
        assert entries <= captured
        for name in (["midnightlib.mixins.json"] if nested else [
            "ubesdelight.mixins.json", "ubesdelight-common.mixins.json",
        ]):
            mixins = cast("dict[str, JsonValue]", json.loads(archive.read(name)))
            assert not mixins.get("mixins")
            assert not mixins.get("plugin")
            assert mixins["client"] == (["MixinOptionsScreen"] if nested else [])


def test_ubes_delight_data_is_food_and_four_crop_chains() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name.startswith("ubesdelight-"))
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        names = [n for n in archive.namelist() if not n.endswith("/")]
        assert all(n.endswith(".json") for n in names if n.startswith("data/"))
        assert Counter(n.split("/")[2] for n in names if n.startswith("data/")) == {
            "tags": 75, "data_maps": 1, "loot_modifiers": 2, "advancement": 134,
            "create": 9, "damage_type": 1, "loot_table": 37, "neoforge": 4,
            "recipe": 172, "weapon_attributes": 5, "worldgen": 8,
        }
        assert {n for n in names if n.startswith("resourcepacks/")} == {
            "resourcepacks/udpresencefootsteps/assets/presencefootsteps/config/blockmap.json",
            "resourcepacks/udpresencefootsteps/pack.mcmeta",
            "resourcepacks/udpresencefootsteps/pack.png",
        }
        for crop, flower in (
            ("garlic", "pink_tulip"), ("ginger", "lily_of_the_valley"),
            ("lemongrass", "azure_bluet"), ("ube", "cornflower"),
        ):
            prefix = "data/ubesdelight/"
            doc = cast("dict[str, JsonValue]", json.loads(archive.read(
                prefix + f"worldgen/configured_feature/patch_wild_{crop}.json"
            )))
            assert doc["type"] == "ubesdelight:wild_tertiary_crop"
            states: set[str] = set()
            types: set[str] = set()
            pending: list[JsonValue] = [doc]
            while pending:
                node = pending.pop()
                if isinstance(node, dict):
                    if "Name" in node:
                        states.add(str(node["Name"]))
                    if "type" in node:
                        types.add(str(node["type"]))
                    pending.extend(node.values())
                elif isinstance(node, list):
                    pending.extend(node)
            assert states == {"ubesdelight:wild_" + crop, "minecraft:" + flower,
                              "minecraft:tall_grass"}
            assert types == {
                "ubesdelight:wild_tertiary_crop", "minecraft:simple_block",
                "minecraft:simple_state_provider", "minecraft:block_predicate_filter",
                "minecraft:all_of", "minecraft:matching_block_tag", "minecraft:matching_blocks",
            }
            assert json.loads(archive.read(
                prefix + f"neoforge/biome_modifier/wild_{crop}.json"
            )) == {
                "type": "ubesdelight:add_features_by_filter", "allowed_biomes": "#c:is_jungle",
                "denied_biomes": ["#c:is_underground"],
                "features": f"ubesdelight:patch_wild_{crop}", "step": "vegetal_decoration",
            }
            placed = cast("dict[str, JsonValue]", json.loads(archive.read(
                prefix + f"worldgen/placed_feature/patch_wild_{crop}.json"
            )))
            assert placed["feature"] == f"ubesdelight:patch_wild_{crop}"
