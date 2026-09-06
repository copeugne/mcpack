from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import TYPE_CHECKING, cast
from zipfile import ZipFile

from mcpack_evidence.item8_registry import read_registry
from mcpack_evidence.item8_sources import retained_sources
from mcpack_evidence.item8_templates import template_summary

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_betterend_building_lists_partition_exact_template_candidates() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name == "BetterEnd-21.0.31.jar")
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    # Explicit inspected choices, not automatic family grouping by filename.
    choices: dict[str, tuple[int, set[str], set[str]]] = {
        "blossoming_spires": (8, set(), set()),
        "chorus_forest": (8, set(), {
            *(f"fallen_tree_{i}" for i in range(1, 5)),
            *(f"stump_{i}" for i in range(1, 4)),
        }),
        "foggy_mushroomland": (3, {"library", "tree_house"}, {
            "fallen_tree_1", "fallen_tree_2", "stump_1", "stump_2",
        }),
        "lantern_woods": (2, {"cabin", "light_1"}, {
            "log_1", "log_2", "stump_1", "stump_2", "stump_3",
        }),
        "shadow_forest": (8, {"small_mansion"}, {
            "stump_1", "stump_2", "fallen_log_1", "fallen_log_2",
        }),
        "umbrella_jungle": (6, {"house_1", "house_2"}, {"jellyshroom_cluster"}),
    }
    vegetation_blocks = {
        "purple_polypore", "pythadendron_bark", "pythadendron_log", "tail_moss",
        "pythadendron_leaves", "cyan_moss", "dense_vine", "mossy_glowshroom_bark",
        "mossy_glowshroom_fur", "mossy_glowshroom_log", "mossy_glowshroom_cap",
        "mossy_glowshroom_hymenophore", "aurant_polypore", "lucernia_leaves",
        "lucernia_log", "lucernia_outer_leaves", "ruscus", "filalux", "lucernia_bark",
        "dragon_tree_log", "twisted_vine", "jellyshroom_bark", "jellyshroom_cap_purple",
        "jellyshroom_stripped_bark", "jungle_grass", "jungle_moss", "small_jellyshroom",
        "twisted_umbrella_moss",
    }
    registry = Path("evidence/item-8/runtime/registry-r1/dumps/registry/minecraft")
    configured = read_registry(registry / "worldgen_configured_feature.txt")
    placed = read_registry(registry / "worldgen_placed_feature.txt")
    dimensions_raw = Path("evidence/item-8/runtime/dimension-r3/dimension-biomes.json").read_bytes()
    assert hashlib.sha256(dimensions_raw).hexdigest() == (
        "08fa8185cd2c3f54b5255b2e8f86946c4b37ed471fb1991d0f82c835ffe20c7c"
    )
    dimensions = cast("dict[str, list[str]]", json.loads(dimensions_raw))
    with ZipFile(source.path) as archive:
        definitions = {
            Path(n).stem: cast("dict[str, JsonValue]", json.loads(archive.read(n)))
            for n in archive.namelist()
            if n.startswith("data/betterend/worldgen/configured_feature/") and n.endswith(".json")
        }
        assert {k for k, v in definitions.items()
                if v["type"] == "betterend:building_list_feature"} == {
            name + "_structures" for name in choices
        }
        all_paths: set[str] = set()
        vegetation_paths: set[str] = set()
        for biome, (ruin_count, buildings, vegetation) in choices.items():
            identifier = "betterend:" + biome + "_structures"
            assert identifier in configured
            assert identifier in placed
            assert "betterend:" + biome in dimensions["minecraft:the_end"]
            definition = definitions[biome + "_structures"]
            config = cast("dict[str, JsonValue]", definition["config"])
            structures = cast("list[dict[str, JsonValue]]", config["structures"])
            names = {Path(str(row["path"])).stem for row in structures}
            assert len(names) == len(structures)
            assert names == buildings | vegetation | {
                f"ruins_{i}" for i in range(1, ruin_count + 1)
            }
            assert json.loads(archive.read(
                f"data/betterend/worldgen/placed_feature/{biome}_structures.json"
            )) == {"feature": identifier, "placement": [
                {"type": "minecraft:rarity_filter", "chance": 10},
                {"type": "minecraft:in_square"}, {"type": "minecraft:biome"},
            ]}
            biome_data = cast("dict[str, list[list[str]]]", json.loads(archive.read(
                f"data/betterend/worldgen/biome/{biome}.json")))
            assert identifier in biome_data["features"][4]
            for row in structures:
                path = str(row["path"])
                assert path.startswith(f"/data/betterend/structure/biome/{biome}/")
                assert path not in all_paths
                all_paths.add(path)
                template = template_summary(archive.read(path.removeprefix("/")))
                if Path(path).stem in vegetation:
                    vegetation_paths.add(path)
                    assert template["entities"] == []
                    assert template["block_entities"] == []
                    palette = cast("list[dict[str, JsonValue]]", template["palette"])
                    counts = cast("dict[str, int]", template["state_counts"])
                    used = {str(state["Name"]) for i, state in enumerate(palette)
                            if counts.get(str(i), 0)}
                    assert used <= {"minecraft:end_stone"} | {
                        "betterend:" + block for block in vegetation_blocks
                    }
        assert len(all_paths) == 63  # inspected template choices, not families.
        assert len(vegetation_paths) == 21  # explicit vegetation partition.


def test_betterend_crashed_ship_inline_configuration_and_biome_routes() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name == "BetterEnd-21.0.31.jar")
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    directory = Path("evidence/item-8/sources/betterend-feature-scope")
    raw = (directory / "identities.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "7a3fe03fddacad093573ad808d94b41463643acf11df321dc2b7a6fdeb5dd30d"
    )
    with ZipFile(source.path) as archive:
        for row in cast("list[dict[str, str]]", json.loads(raw)):
            assert row["archive"] == source.name
            assert row["archive_sha256"] == source.sha256
            assert hashlib.sha256(archive.read(row["class"])).hexdigest() == row["class_sha256"]
            assert hashlib.sha256((directory / row["disassembly"]).read_bytes()).hexdigest() == (
                row["disassembly_sha256"]
            )
        assert json.loads(archive.read(
            "data/betterend/worldgen/placed_feature/crashed_ship.json")) == {
            "feature": {"type": "betterend:crashed_ship", "config": {
                "default": {"Name": "minecraft:end_stone"},
            }}, "placement": [{"type": "minecraft:rarity_filter", "chance": 500},
                              {"type": "minecraft:in_square"}, {"type": "minecraft:biome"}],
        }
        consumers: set[str] = set()
        for path in archive.namelist():
            if path.startswith("data/betterend/worldgen/biome/") and path.endswith(".json"):
                biome = cast("dict[str, list[list[str]]]", json.loads(archive.read(path)))
                if any("betterend:crashed_ship" in group for group in biome["features"]):
                    consumers.add(Path(path).stem)
        assert consumers == {
            "amber_land", "blossoming_spires", "chorus_forest", "crystal_mountains",
            "dragon_graveyards", "dry_shrubland", "dust_wastelands", "empty_aurora_cave",
            "empty_end_cave", "empty_smaragdant_cave", "flower_islets", "foggy_mushroomland",
            "glowing_grasslands", "ice_starfield", "jade_cave", "lantern_woods",
            "lush_aurora_cave", "lush_smaragdant_cave", "megalake", "megalake_grove", "neon_oasis",
            "painted_mountains", "shadow_forest", "sulphur_springs", "umbra_valley",
            "umbrella_jungle", "waterfall_ponds",
        }
    registry = Path("evidence/item-8/runtime/registry-r1/dumps/registry/minecraft")
    assert "betterend:crashed_ship" in read_registry(registry / "worldgen_placed_feature.txt")
    # No separate configured ID is needed for an inline configured feature.
    assert "betterend:crashed_ship" not in read_registry(
        registry / "worldgen_configured_feature.txt")
    dimensions = cast("dict[str, list[str]]", json.loads(Path(
        "evidence/item-8/runtime/dimension-r3/dimension-biomes.json").read_bytes()))
    assert {name for name in consumers
            if "betterend:" + name not in dimensions["minecraft:the_end"]} == {
        "empty_aurora_cave", "empty_end_cave", "empty_smaragdant_cave", "jade_cave",
        "lush_aurora_cave", "lush_smaragdant_cave",
    }
