from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from typing import TYPE_CHECKING, cast
from zipfile import ZipFile

from mcpack_evidence.item8_registry import read_registry
from mcpack_evidence.item8_sources import retained_sources

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_bop_named_candidates_bind_packaged_routes_and_live_biomes() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name.startswith("BiomesOPlenty-"))
    assert source.sha256 == "07f449b7766845883523ffadb8fb706ec011c1212aa378b48bea5841188f0b04"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    candidates = {"anomaly", "monolith", "bone_spine", "nether_bone_spine",
                  "big_pumpkin", "pumpkin_patch"}
    with ZipFile(source.path) as archive:
        data = {
            n: cast("dict[str, JsonValue]", json.loads(archive.read(n)))
            for n in archive.namelist() if n.startswith("data/") and n.endswith(".json")
        }
        prefix = "data/biomesoplenty/worldgen/"
        for name in candidates:
            assert data[prefix + "configured_feature/" + name + ".json"] == {
                "type": "biomesoplenty:" + ("bone_spine" if name == "nether_bone_spine" else name),
                "config": {},
            }
        placed = {n: d for n, d in data.items() if n.startswith(prefix + "placed_feature/")}
        assert len(placed) == 321
        assert all(isinstance(d["feature"], str) for d in placed.values())
        assert {n.removeprefix(prefix + "placed_feature/").removesuffix(".json")
                for n, d in placed.items()
                if d["feature"] in {"biomesoplenty:" + c for c in candidates}} == {
            "anomaly", "monolith", "nether_bone_spine", "big_pumpkin", "pumpkin_patch",
        }
        for name, chance in (
            ("anomaly", 2), ("monolith", 4), ("big_pumpkin", 1), ("pumpkin_patch", 1),
        ):
            assert placed[prefix + "placed_feature/" + name + ".json"] == {
                "feature": "biomesoplenty:" + name,
                "placement": [
                    {"type": "minecraft:rarity_filter", "chance": chance},
                    {"type": "minecraft:in_square"},
                    {"type": "minecraft:heightmap", "heightmap": "MOTION_BLOCKING"},
                    {"type": "minecraft:biome"},
                ],
            }
        consumers: dict[str, set[str]] = {name: set() for name in candidates}
        for path, definition in data.items():
            if path.startswith(prefix + "biome/"):
                for stage in cast("list[list[str]]", definition["features"]):
                    for feature in stage:
                        if feature.removeprefix("biomesoplenty:") in consumers:
                            consumers[feature.removeprefix("biomesoplenty:")].add(
                                path.removeprefix(prefix + "biome/").removesuffix(".json"))
        assert consumers == {
            "anomaly": {"end_corruption"}, "monolith": {"end_corruption"},
            "nether_bone_spine": {"visceral_heap"}, "bone_spine": set(),
            "big_pumpkin": {"pumpkin_patch"}, "pumpkin_patch": {"pumpkin_patch"},
        }
        directory = Path("evidence/item-8/sources/bop-feature-scope")
        raw = (directory / "identities.json").read_bytes()
        assert hashlib.sha256(raw).hexdigest() == (
            "784dbe3703e88c8720cacd937195f867735f3b13c892d755cb0aaff389f18296"
        )
        rows = cast("list[dict[str, str]]", json.loads(raw))
        assert len(rows) == 3
        for row in rows:
            assert row["archive"] == source.name
            assert row["archive_sha256"] == source.sha256
            assert hashlib.sha256(archive.read(row["class"])).hexdigest() == row["class_sha256"]
            assert hashlib.sha256((directory / row["disassembly"]).read_bytes()).hexdigest() == (
                row["disassembly_sha256"]
            )
    runtime = Path("evidence/item-8/runtime/registry-r1/dumps/registry/minecraft")
    assert {"biomesoplenty:" + name for name in candidates} <= set(read_registry(
        runtime / "worldgen_configured_feature.txt"))
    assert {"biomesoplenty:" + name for name in candidates - {"bone_spine"}} <= set(read_registry(
        runtime / "worldgen_placed_feature.txt"))
    raw = Path("evidence/item-8/runtime/dimension-r3/dimension-biomes.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "08fa8185cd2c3f54b5255b2e8f86946c4b37ed471fb1991d0f82c835ffe20c7c"
    )
    dimensions = cast("dict[str, list[str]]", json.loads(raw))
    assert "biomesoplenty:end_corruption" in dimensions["minecraft:the_end"]
    assert "biomesoplenty:visceral_heap" in dimensions["minecraft:the_nether"]
    assert "biomesoplenty:pumpkin_patch" in dimensions["minecraft:overworld"]


def test_bop_plain_bone_spine_has_no_packaged_selector_reference() -> None:
    decisions = cast("dict[str, JsonValue]", json.loads(Path(
        "evidence/item-8/family-decisions.json").read_bytes()))
    content = cast("dict[str, JsonValue]", decisions["non_registry_content"])
    contributions = cast("dict[str, dict[str, JsonValue]]", content["contributions"])
    for name in ("anomaly", "monolith", "bone_spine", "big_pumpkin", "pumpkin_patch"):
        key = "biomesoplenty:" + name
        decision = contributions[key]
        assert decision["families"] == ([key] if name in {"anomaly", "monolith"} else [])
        if name != "bone_spine":
            assert decision["configured_feature"] == decision["placed_feature"] == key
            assert decision["packaged_biome_consumer"] == (
                "biomesoplenty:end_corruption" if name in {"anomaly", "monolith"}
                else "biomesoplenty:pumpkin_patch")
        for path, digest in cast("dict[str, str]", decision["evidence"]).items():
            assert hashlib.sha256(Path(path).read_bytes()).hexdigest() == digest
    source = next(s for s in retained_sources(Path.cwd()) if s.name.startswith("BiomesOPlenty-"))
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        prefix = "data/biomesoplenty/worldgen/"
        data = {
            n: cast("dict[str, JsonValue]", json.loads(archive.read(n)))
            for n in archive.namelist() if n.startswith("data/") and n.endswith(".json")
        }
        # Exact value search includes selectors and other packaged data, not only direct routes.
        references: set[str] = set()
        for path, definition in data.items():
            pending: list[JsonValue] = [definition]
            while pending:
                value = pending.pop()
                if isinstance(value, dict):
                    pending.extend(value.values())
                elif isinstance(value, list):
                    pending.extend(value)
                elif value == "biomesoplenty:bone_spine":
                    references.add(path)
        assert references == {
            prefix + "configured_feature/bone_spine.json",
            prefix + "configured_feature/nether_bone_spine.json",
        }


def test_bop_generation_entry_capture_covers_configured_type_registrations() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name.startswith("BiomesOPlenty-"))
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    directory = Path("evidence/item-8/sources/bop-generation-entries")
    raw = (directory / "identities.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "e39ce1ed03f04e960d04b689e6843a27be532200b5b7c523162564b489ddcaed"
    )
    rows = cast("list[dict[str, str]]", json.loads(raw))
    assert len(rows) == 9
    with ZipFile(source.path) as archive:
        for row in rows:
            assert row["archive"] == source.name
            assert row["archive_sha256"] == source.sha256
            assert hashlib.sha256(archive.read(row["class"])).hexdigest() == row["class_sha256"]
            assert hashlib.sha256((directory / row["disassembly"]).read_bytes()).hexdigest() == (
                row["disassembly_sha256"]
            )
        types = {
            str(cast("dict[str, JsonValue]", json.loads(archive.read(n)))["type"])
            for n in archive.namelist()
            if n.startswith("data/biomesoplenty/worldgen/configured_feature/")
            and n.endswith(".json")
        }
    custom = {t for t in types if t.startswith("biomesoplenty:")}
    assert len(custom) == 78
    assert len(types - custom) == 13
    path = directory / source.name / "biomesoplenty.worldgen.feature.BOPBaseFeatures.txt"
    text = path.read_text()
    registration = text.split("public static void registerFeatures(", 1)[1].split(
        "private static", 1)[0]
    names = cast("list[str]", re.findall(r"// String (\w+)", registration))
    registered = {"biomesoplenty:" + name for name in names}
    assert len(registered) == 81
    assert custom <= registered
    assert registered - custom == {
        "biomesoplenty:dead_coral_claw", "biomesoplenty:dead_coral_mushroom",
        "biomesoplenty:dead_coral_tree",
    }


def test_bop_registered_features_have_complete_contribution_roles() -> None:
    roles = {
        "landmark_families": {"anomaly", "monolith"},
        "excluded_pumpkin_decorations": {"big_pumpkin", "pumpkin_patch"},
        "terrain_and_minerals": {
            "black_sand_splatter", "bone_spine", "crag_moss", "crag_splatter",
            "dripstone_splatter", "hot_spring_vents", "inferno_splatter", "jagged_sandstone",
            "lake", "large_fumarole", "large_rose_quartz", "moss_splatter",
            "mossy_black_sand_splatter", "mud_splatter", "mycelium_splatter",
            "obsidian_splatter", "origin_gravel_cliffs", "scattered_rocks",
            "small_crystal", "small_fumarole", "tidepool",
        },
        "vegetation_and_ecological_decorations": {
            "barnacles", "basic_tree", "bayou_tree", "big_dripleaf", "big_tree", "bramble",
            "bush_tree", "corner_cobwebs", "cypress_tree", "dead_coral_claw",
            "dead_coral_mushroom", "dead_coral_patch", "dead_coral_tree", "empyreal_tree",
            "extra_glow_lichen", "fallen_birch_log", "fallen_fir_log", "fallen_jacaranda_log",
            "fallen_log", "flesh_tendon", "giant_glowshroom", "hanging_flesh_tendon",
            "high_grass", "huge_clover", "huge_glowshroom", "huge_lily_pad", "huge_toadstool",
            "lumaloop", "magic_tree", "mahogany_tree", "medium_glowshroom", "nether_vines",
            "orange_maple_leaf_pile", "palm_tree", "pine_tree", "rainforest_cliffs_vines",
            "red_maple_leaf_pile", "redwood_tree", "rooted_stump", "scrub", "short_bamboo",
            "small_brown_mushroom", "small_dripleaf", "small_glowshroom", "small_red_mushroom",
            "small_toadstool", "sparse_dune_grass", "stringy_cobweb", "taiga_tree",
            "termite_mound", "thin_bamboo", "twiglet_tree", "umbran_tree", "webbing",
            "wispjelly", "yellow_maple_leaf_pile",
        },
    }
    names = [name for group in roles.values() for name in group]
    assert len(names) == len(set(names)) == 81
    source = next(s for s in retained_sources(Path.cwd()) if s.name.startswith("BiomesOPlenty-"))
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    base = Path("evidence/item-8/sources")
    registration = (base / "bop-generation-entries" / source.name
                    / "biomesoplenty.worldgen.feature.BOPBaseFeatures.txt").read_text()
    pairs = cast("list[tuple[str, str]]", re.findall(
        r"// String ([^\n]+).*?// class (biomesoplenty/worldgen/feature/[^\n]+)",
        registration, re.DOTALL))
    assert set(names) == {name for name, _ in pairs}
    captured: set[str] = set()
    with ZipFile(source.path) as archive:
        for directory, digest in {
            "bop-feature-scope": "784dbe3703e88c8720cacd937195f867735f3b13c892d755cb0aaff389f18296",
            "bop-remaining-features":
                "8ef880a70fed808b321b66d876ad5e5d9932096df455aa67dc2b2f25e153bfb0",
            "bop-delegated-material-writers":
                "fbb0dcdc15d9fd3f38663af03a7db1d3f942b01f0f8c243cfb3ed032ec647080",
        }.items():
            raw = (base / directory / "identities.json").read_bytes()
            assert hashlib.sha256(raw).hexdigest() == digest
            for row in cast("list[dict[str, str]]", json.loads(raw)):
                assert row["archive"] == source.name
                assert row["archive_sha256"] == source.sha256
                assert hashlib.sha256(archive.read(row["class"])).hexdigest() == row["class_sha256"]
                raw = (base / directory / row["disassembly"]).read_bytes()
                assert hashlib.sha256(raw).hexdigest() == row["disassembly_sha256"]
                assert row["class"] not in captured
                captured.add(row["class"])
        assert captured == {name + ".class" for _, name in pairs} | {
            "biomesoplenty/worldgen/feature/tree/BOPTreeFeature.class",
            "biomesoplenty/worldgen/feature/misc/LargeRoseQuartzFeature$LargeRoseQuartz.class",
            "biomesoplenty/util/biome/RoseQuartzUtils.class",
        }
        coral = cast("dict[str, JsonValue]", json.loads(archive.read(
            "data/biomesoplenty/worldgen/configured_feature/dead_coral.json")))
        assert coral == {"type": "minecraft:simple_random_selector", "config": {"features": [
            {"feature": {"type": "biomesoplenty:dead_coral_" + shape, "config": {}},
             "placement": []} for shape in ("tree", "claw", "mushroom")
        ]}}


def test_bop_full_payload_has_no_unaccounted_generation_resources() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name.startswith("BiomesOPlenty-"))
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        files = {n.filename for n in archive.infolist() if not n.is_dir()}
        assert len(files) == 4542
        data = {n for n in files if n.startswith("data/")}
        assert Counter("/".join(n.split("/")[:3]) for n in data) == {
            "data/biomesoplenty/worldgen": 670, "data/biomesoplenty/loot_table": 401,
            "data/biomesoplenty/advancement": 310, "data/biomesoplenty/recipe": 308,
            "data/minecraft/tags": 123, "data/c/tags": 52, "data/biomesoplenty/tags": 41,
            "data/sereneseasons/tags": 13, "data/toughasnails/tags": 11,
            "data/minecraft/wolf_variant": 9, "data/biomesoplenty/trim_material": 2,
            "data/biomesoplenty/damage_type": 2, "data/biomesoplenty/wolf_variant": 1,
            "data/biomesoplenty/jukebox_song": 1, "data/neoforge/data_maps": 1,
        }
        prefix = "data/biomesoplenty/worldgen/"
        assert Counter(n[len(prefix):].split("/")[0] for n in data if n.startswith(prefix)) == {
            "placed_feature": 321, "configured_feature": 279, "biome": 69, "configured_carver": 1,
        }
        assets = {n for n in files if n.startswith("assets/")}
        assert Counter(Path(n).suffix for n in assets) == {
            ".json": 1690, ".png": 560, ".mcmeta": 12, ".ogg": 6, ".properties": 1,
        }
        classes = {n for n in files if n.endswith(".class")}
        assert len(classes) == 317
        assert {n for n in classes if any(annotation in archive.read(n) for annotation in (
            b"Lnet/neoforged/fml/common/Mod;", b"Lnet/neoforged/fml/common/EventBusSubscriber;",
        ))} == {
            "biomesoplenty/neoforge/core/BiomesOPlentyNeoForge.class",
            "biomesoplenty/neoforge/datagen/DataGenerationHandler.class",
        }
        assert files - data - assets - classes == {
            ".cache/103d9f3f36b01595f1aa5172191e60eff02e6924",
            ".cache/59eb3dbb5f86130e09b3c62d89b9525ee01cf52d",
            ".cache/9fb1092f32d4fcbf9e061ffd718d4ec689c6c95e",
            "META-INF/MANIFEST.MF", "META-INF/accesstransformer.cfg", "META-INF/neoforge.mods.toml",
            "biomesoplenty.accesswidener", "biomesoplenty.mixins.json",
            "biomesoplenty.neoforge.mixins.json", "biomesoplenty_logo.png", "pack.mcmeta",
        }
    roots = read_registry(Path(
        "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"))
    assert not any(name.startswith("biomesoplenty:") for name in roots)
