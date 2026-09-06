from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import TYPE_CHECKING, cast
from zipfile import ZipFile

from mcpack_evidence.item8_registry import read_registry
from mcpack_evidence.item8_sources import retained_sources

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_better_caves_provider_payload_and_carvers() -> None:
    # One frozen provider and its existing terrain entry paths.
    source = next(
        s for s in retained_sources(Path.cwd()) if s.name.startswith("YungsBetterCaves-")
    )
    assert source.sha256 == "aa94ae3e7fdacb469459bf45be60c35bebfebe0488a79e31c7686d746939701d"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    base = Path("evidence/item-8/sources/better-caves-provider")
    raw = (base / "identities.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "8edcd258cbb0e0133a0595cc6da3eade478e5ab662c246ab441469442f9af988"
    )
    rows = cast("list[dict[str, str]]", json.loads(raw))
    captured = {r["class"] for r in rows}
    assert len(captured) == len(rows) == 23
    with ZipFile(source.path) as archive:
        names = [n for n in archive.namelist() if not n.endswith("/")]
        assert len(names) == len(set(names)) == 64
        for row in rows:
            assert row["archive"] == source.name
            assert row["archive_sha256"] == source.sha256
            assert hashlib.sha256(archive.read(row["class"])).hexdigest() == row["class_sha256"]
            assert hashlib.sha256((base / row["disassembly"]).read_bytes()).hexdigest() == (
                row["disassembly_sha256"]
            )
        classes = {n for n in names if n.endswith(".class")}
        assert len(classes) == 49
        prefix = "com/yungnickyoung/minecraft/bettercaves/"
        for name in classes - captured:
            assert name.startswith(tuple(prefix + n for n in (
                "BCConstants", "config/", "duck/", "json/", "module/ConfigModule.class",
                "noise/", "worldgen/BetterCavesWorldCarverConfig", "worldgen/carver/Carver",
                "worldgen/carver/CaveCarver$Builder", "worldgen/carver/CavernCarver$Builder",
                "worldgen/liquidregion/",
            ))), name
            for marker in (b"EventBusSubscriber;", b"Lnet/neoforged/fml/common/Mod;",
                           b"Lorg/spongepowered/asm/mixin/Mixin;", b"YungAutoRegister;"):
                assert marker not in archive.read(name), (name, marker)
        mixins = cast("dict[str, list[str]]", json.loads(archive.read("bettercaves.mixins.json")))
        assert len(mixins["mixins"]) == 7
        assert {prefix + "mixin/" + n.replace(".", "/") + ".class"
                for n in mixins["mixins"]} <= captured
        service = "com.yungnickyoung.minecraft.bettercaves.services."
        assert archive.read(
            "META-INF/services/" + service + "IPlatformHelper"
        ).decode().strip() == service + "NeoForgePlatformHelper"
        data = {
            "data/bettercaves/neoforge/biome_modifier/add_carvers.json",
            "data/bettercaves/neoforge/biome_modifier/remove_carvers.json",
            "data/bettercaves/worldgen/configured_carver/better_cave.json",
            "data/bettercaves/worldgen/configured_carver/surface_cave.json",
        }
        assert set(names) - classes == data | {
            "META-INF/MANIFEST.MF", "META-INF/neoforge.mods.toml", "pack.mcmeta",
            "assets/bettercaves/lang/en_us.json", "bettercaves.mixins.json",
            "catalogue_background.png", "catalogue_icon.png", "icon.png", "logo.png",
            "LICENSE_YungsBetterCaves", "META-INF/services/" + service + "IPlatformHelper",
        }
        add = cast("dict[str, JsonValue]", json.loads(archive.read(
            "data/bettercaves/neoforge/biome_modifier/add_carvers.json"
        )))
        assert add == {
            "type": "neoforge:add_carvers", "biomes": "#minecraft:is_overworld", "step": "air",
            "carvers": ["bettercaves:better_cave", "bettercaves:surface_cave"],
        }
        remove = cast("dict[str, JsonValue]", json.loads(archive.read(
            "data/bettercaves/neoforge/biome_modifier/remove_carvers.json"
        )))
        assert remove == {
            "type": "neoforge:remove_carvers", "biomes": "#minecraft:is_overworld",
            "carvers": ["minecraft:cave", "minecraft:cave_extra_underground"],
        }
        for name, kind in (("better_cave", "bettercaves:better_cave"),
                           ("surface_cave", "minecraft:cave")):
            document = cast("dict[str, JsonValue]", json.loads(archive.read(
                f"data/bettercaves/worldgen/configured_carver/{name}.json"
            )))
            assert document["type"] == kind
            if name == "better_cave":
                config = cast("dict[str, JsonValue]", document["config"])
                assert config["debug_settings"] == {"enabled": False, "top_y": 128}
    registry = read_registry(Path(
        "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
    ))
    assert not {r for r in registry if r.startswith("bettercaves:")}
    raw = Path(
        "evidence/item-6/frozen/config/bettercaves/neoforge-1_21_1/liquidregions.json"
    ).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "ad0e43cd1d8fff16d76ff6036699bd67598ff8bc18220b7e8e951245c92cf139"
    )
    assert json.loads(raw) == {"liquidRegions": {"minecraft:overworld": {
        "liquid_region_size": 0.001, "water_region_spawn_chance": 40.0, "liquid_altitude": -55,
    }}}
