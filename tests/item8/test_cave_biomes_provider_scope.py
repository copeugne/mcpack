from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import TYPE_CHECKING, cast
from zipfile import ZipFile

from mcpack_evidence.item8_registry import read_registry
from mcpack_evidence.item8_sources import (
    _parse_json,  # pyright: ignore[reportPrivateUsage]
    retained_sources,
)

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_cave_biomes_provider_payload_and_feature_consumers() -> None:  # noqa: PLR0915
    # Reuse the packaged parser, including comment handling, without a duplicate decoder.
    # One frozen provider: account for payload and bind the existing source capture.
    source = next(
        s for s in retained_sources(Path.cwd()) if s.name.startswith("YungsCaveBiomes-")
    )
    assert source.sha256 == "7585587e5cb7859e26189c6ec0a5b829c5c228f095e4e843fa3add61f817dd20"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    base = Path("evidence/item-8/sources/cave-biomes-provider")
    raw = (base / "identities.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "1ec5f0431d582630998de60efd72392cc3ca711047f093fdefcc9250884a225d"
    )
    rows = cast("list[dict[str, str]]", json.loads(raw))
    captured = {r["class"] for r in rows}
    assert len(rows) == len(captured) == 55
    prefix = "com/yungnickyoung/minecraft/yungscavebiomes/"
    with ZipFile(source.path) as archive:
        names = [n for n in archive.namelist() if not n.endswith("/")]
        assert len(names) == len(set(names)) == 581
        classes = {n for n in names if n.endswith(".class")}
        assert len(classes) == 187
        for row in rows:
            assert row["archive"] == source.name
            assert row["archive_sha256"] == source.sha256
            assert hashlib.sha256(archive.read(row["class"])).hexdigest() == row["class_sha256"]
            assert hashlib.sha256((base / row["disassembly"]).read_bytes()).hexdigest() == (
                row["disassembly_sha256"]
            )
        categories = Counter("/".join(n.split("/")[:3]) for n in names
                             if n.startswith(("assets/", "data/")))
        expected = {
            "assets/yungscavebiomes/" + k: v for k, v in {
                "animations": 1, "blockstates": 28, "geo": 1, "lang": 5, "models": 82,
                "particles": 4, "sounds": 17, "sounds.json": 1, "textures": 51,
            }.items()
        } | {
            "data/c/tags": 17, "data/forge/tags": 5, "data/minecraft/tags": 26,
            "data/travelerstitles/tags": 1, "data/yungscavebiomes/advancement": 39,
            "data/yungscavebiomes/damage_type": 2, "data/yungscavebiomes/loot_table": 26,
            "data/yungscavebiomes/recipe": 32, "data/yungscavebiomes/tags": 4,
            "data/yungscavebiomes/trim_pattern": 1, "data/yungscavebiomes/worldgen": 38,
        }
        assert categories == expected
        service = "com.yungnickyoung.minecraft.yungscavebiomes.services."
        assert set(names) - classes - {
            n for n in names if n.startswith(("assets/", "data/"))
        } == {
            "META-INF/MANIFEST.MF", "META-INF/neoforge.mods.toml",
            "META-INF/accesstransformer.cfg", "META-INF/services/" + service + "IPlatformHelper",
            "catalogue_background.png", "catalogue_icon.png", "icon.png", "logo.png",
            "pack.mcmeta", "yungscavebiomes.accesswidener", "yungscavebiomes.mixins.json",
            "yungscavebiomes_neoforge.mixins.json", "LICENSE_YungsCaveBiomes",
        }
        service_text = archive.read("META-INF/services/" + service + "IPlatformHelper")
        assert service_text.decode().strip() == (
            service + "NeoForgePlatformHelper"
        )
        mixins = cast("dict[str, JsonValue]", json.loads(
            archive.read("yungscavebiomes.mixins.json")
        ))
        common = cast("list[str]", mixins["mixins"])
        client = cast("list[str]", mixins["client"])
        assert len(common) == 29
        assert len(client) == 9
        assert "plugin" not in mixins
        assert {prefix + "mixin/" + n.replace(".", "/") + ".class" for n in common} <= captured
        neo = cast("dict[str, JsonValue]", json.loads(
            archive.read("yungscavebiomes_neoforge.mixins.json")
        ))
        assert neo["mixins"] == neo["client"] == []
        assert "plugin" not in neo
        assert {n for n in classes if b"Lnet/neoforged/fml/common/Mod;" in archive.read(n)} == {
            prefix + "YungsCaveBiomesNeoForge.class",
            prefix + "client/YungsCaveBiomesClientNeoForge.class",
        }
        assert not {n for n in classes if b"EventBusSubscriber;" in archive.read(n)}
        feature_classes = {n for n in classes if n.startswith(prefix + "world/feature/")
                           and n.endswith("Feature.class") and "$" not in n}
        assert len(feature_classes) == 12
        assert feature_classes <= captured
        worldgen = "data/yungscavebiomes/worldgen/"
        assert Counter(n.removeprefix(worldgen).split("/")[0] for n in names
                       if n.startswith(worldgen)) == {
            "biome": 2, "configured_feature": 16, "placed_feature": 20,
        }
        configured: dict[str, dict[str, JsonValue]] = {}
        placed: dict[str, dict[str, JsonValue]] = {}
        biomes: list[dict[str, JsonValue]] = []
        for name in names:
            if not name.startswith(worldgen):
                continue
            kind, relative = name.removeprefix(worldgen).split("/", 1)
            document = cast("dict[str, JsonValue]", _parse_json(archive.read(name), name)[0])
            identity = "yungscavebiomes:" + relative.removesuffix(".json")
            if kind == "configured_feature":
                configured[identity] = document
            elif kind == "placed_feature":
                placed[identity] = document
            else:
                biomes.append(document)
        assert {cast("str", d["type"]) for d in configured.values()} == {
            "minecraft:simple_block", "minecraft:vegetation_patch", "minecraft:block_column",
            "minecraft:multiface_growth", "yungscavebiomes:ice_sheet_replace",
            "yungscavebiomes:icicle_cluster", "yungscavebiomes:large_icicle",
            "yungscavebiomes:water_surface_ice_fragment", "yungscavebiomes:ceiling_replace",
            "yungscavebiomes:cactus_patch", "yungscavebiomes:pillar_rock",
            "yungscavebiomes:lost_caves_surface_replace",
            "yungscavebiomes:prickly_peach_cactus_patch",
        }
        assert {cast("str", d["feature"]) for d in placed.values()} == (
            set(configured) | {"minecraft:patch_dead_bush"}
        )
        used = {f for d in biomes for stage in cast("list[list[str]]", d["features"])
                for f in stage}
        assert {f for f in used if f.startswith("yungscavebiomes:")} == set(placed)
        assert {"minecraft:monster_room", "minecraft:monster_room_deep"} <= used
        for structure in ("mineshaft", "stronghold"):
            name = f"data/minecraft/tags/worldgen/biome/has_structure/{structure}.json"
            assert json.loads(archive.read(name)) == {
                "replace": False, "values": ["#yungscavebiomes:cave_biomes"],
            }
    registry = read_registry(Path(
        "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
    ))
    assert not {r for r in registry if r.startswith("yungscavebiomes:")}
    config = Path(
        "evidence/item-6/frozen/config/yungscavebiomes-neoforge-1_21_1.toml"
    ).read_bytes()
    assert hashlib.sha256(config).hexdigest() == (
        "3be6874eada8f1920b8dc30f9345c07afc7d5a7d4621f642f78c57cbe1756b27"
    )
