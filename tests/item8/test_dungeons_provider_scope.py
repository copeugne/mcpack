from __future__ import annotations

import gzip
import hashlib
import json
import re
from pathlib import Path
from typing import TYPE_CHECKING, cast
from zipfile import ZipFile

from mcpack_evidence.item8_inventory import resource_identity
from mcpack_evidence.item8_registry import read_registry
from mcpack_evidence.item8_sources import retained_sources

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_dungeons_provider_payload_and_components() -> None:  # noqa: C901, PLR0912, PLR0915
    # Keep the single frozen payload and its graph partition in one assertion path.
    source = next(
        s for s in retained_sources(Path.cwd()) if s.name.startswith("YungsBetterDungeons-")
    )
    assert source.sha256 == "61816c3b7c9d92c6b44f93dce87ceb0a22827f20285d5d9c4d10d519d734de04"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    classes: set[str] = set()
    groups: dict[str, set[str]] = {
        k: set() for k in ("worldgen/structure", "worldgen/template_pool", "structure")
    }
    with ZipFile(source.path) as archive:
        names = [n for n in archive.namelist() if not n.endswith("/")]
        assert len(names) == len(set(names)) == 389
        for folder, digest in (
            ("betterdungeons-code",
             "c82c912cff651c87b11db309057ff0cd5c2f00ee5e0e12146ad645ac0f563036"),
            ("dungeons-provider",
             "a5b208a65d4a97e7fb79d6a1211cc90517c7a5dce8d03bfe5c697bdc0392718f"),
        ):
            directory = Path("evidence/item-8/sources") / folder
            raw = (directory / "identities.json").read_bytes()
            assert hashlib.sha256(raw).hexdigest() == digest
            identities = cast("list[dict[str, str]]", json.loads(raw))
            for row in identities:
                assert row["archive"] == source.name
                assert row["archive_sha256"] == source.sha256
                assert row["class"] not in classes
                classes.add(row["class"])
                assert hashlib.sha256(archive.read(row["class"])).hexdigest() == row["class_sha256"]
                assert (
                    hashlib.sha256((directory / row["disassembly"]).read_bytes()).hexdigest()
                    == row["disassembly_sha256"]
                )
        assert len(classes) == 23
        all_classes = {n for n in names if n.endswith(".class")}
        assert len(all_classes) == 64
        prefix = "com/yungnickyoung/minecraft/betterdungeons/"
        for name in all_classes - classes:
            assert name.startswith((prefix + "config/", prefix + "module/ConfigModule",
                                    prefix + "world/processor/")), name
            for marker in (b"EventBusSubscriber;", b"Lnet/neoforged/fml/common/Mod;",
                           b"Lorg/spongepowered/asm/mixin/Mixin;", b"YungAutoRegister;"):
                assert marker not in archive.read(name), (name, marker)
        processor_module = prefix + "module/StructureProcessorTypeModule.class"
        processor_text = (Path("evidence/item-8/sources/dungeons-provider") / source.name / (
            "com.yungnickyoung.minecraft.betterdungeons.module.StructureProcessorTypeModule.txt"
        )).read_text()
        processor_classes = {n + ".class" for n in cast("list[str]", re.findall(
            r"// Field ([^ :]+)\.CODEC:", processor_text
        ))}
        assert len(processor_classes) == 29
        assert {n for n in all_classes if "/world/processor/" in n} == processor_classes | {
            prefix + "world/processor/small_dungeon/SmallDungeonBannerProcessor$1.class",
            prefix + "world/processor/small_nether_dungeon/"
            + "SmallNetherDungeonBannerProcessor$1.class",
        }
        services = "com.yungnickyoung.minecraft.betterdungeons.services."
        for interface, implementation in (
            ("IModulesLoader", "NeoForgeModulesLoader"),
            ("IPlatformHelper", "NeoForgePlatformHelper"),
        ):
            assert archive.read("META-INF/services/" + services + interface).decode().strip() == (
                services + implementation
            )
        for name in names:
            if name in all_classes | {
                "META-INF/MANIFEST.MF", "META-INF/neoforge.mods.toml", "pack.mcmeta",
                "betterdungeons.mixins.json", "LICENSE_YungsBetterDungeons",
                "catalogue_background.png", "catalogue_icon.png", "icon.png", "logo.png",
                "META-INF/services/" + services + "IModulesLoader",
                "META-INF/services/" + services + "IPlatformHelper",
            }:
                continue
            if name.startswith("assets/betterdungeons/lang/"):
                assert name.endswith(".json"), name
                continue
            assert name.startswith((
                "data/betterdungeons/",
                "data/yungsapi/tags/", "data/morevillagers/tags/",
            )), name
            assert name.endswith((".json", ".nbt")), name
            assert name.split("/")[2] in {
                "worldgen", "structure", "tags", "loot_table", "advancement", "forge", "neoforge",
            }, name
            if name.split("/")[2] == "worldgen":
                assert name.split("/")[3] in {
                    "structure", "structure_set", "template_pool", "processor_list",
                }, name
            for kind, ids in groups.items():
                found = resource_identity(name, kind, ".nbt" if kind == "structure" else ".json")
                if found:
                    ids.add(found[0])
        processor_types: set[str] = set()
        for name in names:
            if "/worldgen/processor_list/" not in name:
                continue
            data = cast("dict[str, list[dict[str, JsonValue]]]", json.loads(archive.read(name)))
            processor_types.update(cast("str", p["processor_type"]) for p in data["processors"])
        assert len(processor_types) == 30
        assert "minecraft:rule" in processor_types
        for identifier in processor_types - {"minecraft:rule"}:
            assert identifier.startswith("betterdungeons:")
            assert identifier.split(":")[1].encode() in archive.read(processor_module)
        for loader in ("forge", "neoforge"):
            modifier = cast("dict[str, JsonValue]", json.loads(archive.read(
                f"data/betterdungeons/{loader}/biome_modifier/vanilla_dungeon_removal.json"
            )))
            assert modifier == {
                "type": loader + ":remove_features",
                "biomes": "#betterdungeons:has_structure/small_dungeon",
                "features": ["minecraft:monster_room", "minecraft:monster_room_deep"],
                "steps": "underground_structures",
            }
    assert groups["worldgen/structure"] == {"betterdungeons:" + name for name in (
        "small_dungeon", "small_nether_dungeon", "skeleton_dungeon",
        "zombie_dungeon", "spider_dungeon",
    )}
    registry = read_registry(Path(
        "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
    ))
    assert groups["worldgen/structure"] == {
        r for r in registry if r.startswith("betterdungeons:")
    }
    raw = Path("evidence/item-8/sources/pool-traces-content.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "703eed7b5d558b54a62985c7f919d0254e8de613292364c514c5b47b298accc5"
    )
    document = cast("dict[str, JsonValue]", json.loads(gzip.decompress(raw)))
    traces = cast("dict[str, dict[str, JsonValue]]", document["structures"])
    selected = {k: v for k, v in traces.items() if k.startswith("betterdungeons:")}
    assert set(selected) == groups["worldgen/structure"] - {"betterdungeons:spider_dungeon"}
    reached_pools: set[str] = set()
    reached_templates: set[str] = set()
    for root, trace in selected.items():
        reached_pools.update(cast("list[str]", trace["pools"]))
        reached_templates.update(cast("list[str]", trace["templates"]))
        assert trace["unresolved_elements"] == []
        assert trace["missing"] == ([{
            "id": "betterdungeons:zombie_dungeon/big_stairs_crumbled_0", "kind": "template",
        }] if root == "betterdungeons:zombie_dungeon" else [])
    assert len(groups["worldgen/template_pool"]) == 33
    assert groups["worldgen/template_pool"] | {"minecraft:empty"} == reached_pools
    assert len(groups["structure"]) == 227
    assert groups["structure"] - reached_templates == {
        "betterdungeons:skeleton_dungeon/bridges/bridge_stone_1",
    }
