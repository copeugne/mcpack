from __future__ import annotations

import hashlib
import json
import re
import tomllib
from collections import Counter
from pathlib import Path
from typing import TYPE_CHECKING, cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_farmers_delight_full_payload() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name.startswith("FarmersDelight-"))
    assert source.sha256 == "8ff438d62e1fce61542945faae45975d823e04bd6e73a07a121ea05ce2f03de7"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        names = [n for n in archive.namelist() if not n.endswith("/")]
        assert len(names) == len(set(names)) == 2220
        classes = {n for n in names if n.endswith(".class")}
        assets = {n for n in names if n.startswith("assets/")}
        data = {n for n in names if n.startswith("data/")}
        assert (len(classes), len(assets), len(data)) == (292, 995, 927)
        assert set(names) - classes - assets - data == {
            "META-INF/MANIFEST.MF", "META-INF/accesstransformer.cfg",
            "META-INF/enumextensions.json", "META-INF/neoforge.mods.toml",
            "farmersdelight.mixins.json", "logo.png",
        }
        assert all(n.endswith((".json", ".png", ".ogg", ".mcmeta")) for n in assets)
        assert Counter(n.split("/")[2] for n in data) == {
            "recipe": 333, "advancement": 218, "tags": 178, "loot_table": 112,
            "loot_modifiers": 38, "worldgen": 19, "neoforge": 9, "create": 7,
            "structure": 5, "scripts": 3, "data_maps": 2, "damage_type": 1,
            "enchantment": 1, "weapon_attributes": 1,
        }
        assert {n for n in data if not n.endswith(".json")} == {
            *(f"data/farmersdelight/structure/village/houses/{b}_compost_pile.nbt"
              for b in ("desert", "plains", "savanna", "snowy", "taiga")),
            *(f"data/farmersdelight/scripts/{n}.zs"
              for n in ("cooking_pot", "cutting_board", "replacer_testing")),
        }


def test_farmers_delight_declared_entries_match_inspected_sources() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name.startswith("FarmersDelight-"))
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        captured: set[str] = set()
        for label, count, expected_sha in (
            ("farmers-delight-provider", 43,
             "f8c36ff1189315631d10c8f4e11d7c3d107f25dcc6c134cd1e716ae123e89d79"),
            ("farmers-delight-setup", 1,
             "d112ad28ee2983a420b8432cf1f1fe82686a297437bc089968d5fa32d55e5918"),
            ("farmers-delight-packet", 1,
             "084b325b82dc81640f4abd651edc56c91e260c1972f816298c57f6996b9f8fb2"),
        ):
            directory = Path("evidence/item-8/sources") / label
            raw = (directory / "identities.json").read_bytes()
            assert hashlib.sha256(raw).hexdigest() == expected_sha
            rows = cast("list[dict[str, str]]", json.loads(raw))
            assert len(rows) == len({r["class"] for r in rows}) == count
            for row in rows:
                captured.add(row["class"])
                assert row["archive"] == source.name
                assert row["archive_sha256"] == source.sha256
                assert hashlib.sha256(archive.read(row["class"])).hexdigest() == row["class_sha256"]
                raw = (directory / row["disassembly"]).read_bytes()
                assert hashlib.sha256(raw).hexdigest() == row["disassembly_sha256"]
        classes = {n for n in archive.namelist() if n.endswith(".class")}
        entries = {n for n in classes if any(
            tag in archive.read(n) for tag in (
                b"Lnet/neoforged/fml/common/Mod;",
                b"Lnet/neoforged/fml/common/EventBusSubscriber;",
            )
        )}
        assert len(entries) == 19
        assert entries <= captured
        assert {n for n in classes if "/common/world/" in n} <= captured
        metadata = tomllib.loads(archive.read("META-INF/neoforge.mods.toml").decode())
        assert metadata["modLoader"] == "javafml"
        assert metadata["mixins"] == [{"config": "farmersdelight.mixins.json"}]
        mixins = cast("dict[str, JsonValue]", json.loads(
            archive.read("farmersdelight.mixins.json")
        ))
        common = cast("list[str]", mixins["mixins"])
        assert len(common) == 12
        assert {str(mixins["package"]).replace(".", "/") + "/" + n.replace(".", "/") + ".class"
                for n in common} <= captured
        assert not mixins.get("plugin")
        assert mixins["client"] == ["CanvasSignEditScreenMixin", "HideBlockBreakProgressMixin"]


def test_farmers_delight_component_and_vegetation_consumers() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name.startswith("FarmersDelight-"))
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    directory = Path("evidence/item-8/sources/farmers-delight-provider") / source.name
    village_path = directory / "vectorwing.farmersdelight.common.world.VillageStructures.txt"
    village = village_path.read_text()
    strings = set(re.findall(r"// String (.+)", village))
    with ZipFile(source.path) as archive:
        templates = {n for n in archive.namelist() if n.endswith(".nbt")}
        linked: set[str] = set()
        for biome in ("desert", "plains", "savanna", "snowy", "taiga"):
            component = f"village/houses/{biome}_compost_pile"
            assert "farmersdelight:" + component in strings
            assert f"minecraft:village/{biome}/houses" in strings
            assert "minecraft:farm_" + biome in strings
            linked.add("data/farmersdelight/structure/" + component + ".nbt")
        assert linked == templates
        configured: set[str] = set()
        placed: set[str] = set()
        consumed: set[str] = set()
        feature_types: Counter[str] = Counter()
        blocks: set[str] = set()
        for name in archive.namelist():
            if not name.endswith(".json") or not any(part in name for part in (
                "/configured_feature/", "/placed_feature/", "/biome_modifier/",
            )):
                continue
            doc = cast("dict[str, JsonValue]", json.loads(archive.read(name)))
            identity = "farmersdelight:" + Path(name).stem
            if "/configured_feature/" in name:
                configured.add(identity)
                feature_types[str(doc["type"])] += 1
                pending: list[JsonValue] = [doc]
                while pending:
                    node = pending.pop()
                    if isinstance(node, dict):
                        if "Name" in node:
                            blocks.add(str(node["Name"]))
                        pending.extend(node.values())
                    elif isinstance(node, list):
                        pending.extend(node)
            elif "/placed_feature/" in name:
                placed.add(identity)
                assert doc["feature"] == identity
            else:
                assert doc["type"] == "farmersdelight:add_features_by_filter"
                assert doc["step"] == "vegetal_decoration"
                consumed.add(str(doc["features"]))
        assert len(configured) == 10
        assert len(placed) == 9
        assert placed == consumed == configured - {"farmersdelight:patch_sandy_shrub"}
        assert feature_types == {
            "farmersdelight:wild_crop": 8, "farmersdelight:wild_rice": 1,
            "minecraft:random_patch": 1,
        }
        assert blocks == {
            *("farmersdelight:wild_" + crop for crop in (
                "beetroots", "cabbages", "carrots", "onions", "potatoes", "rice", "tomatoes",
            )),
            "farmersdelight:brown_mushroom_colony", "farmersdelight:red_mushroom_colony",
            "farmersdelight:sandy_shrub", "minecraft:brown_mushroom", "minecraft:red_mushroom",
            "minecraft:allium", "minecraft:coarse_dirt", "minecraft:short_grass",
            "minecraft:fern", "minecraft:dead_bush",
        }
