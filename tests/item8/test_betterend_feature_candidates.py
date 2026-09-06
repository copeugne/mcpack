from __future__ import annotations

import gzip
import hashlib
import json
from collections import Counter
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


def test_betterend_extra_biome_templates_and_direct_list_consumer() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name == "BetterEnd-21.0.31.jar")
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    directory = Path("evidence/item-8/sources/betterend-entry-template-consumers")
    raw = (directory / "identities.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "22dee10074c502f7026b266335c5d2966a47374504ae836d2f1da17e79a895d8"
    )
    with ZipFile(source.path) as archive:
        for row in cast("list[dict[str, str]]", json.loads(raw)):
            assert row["archive"] == source.name
            assert row["archive_sha256"] == source.sha256
            assert hashlib.sha256(archive.read(row["class"])).hexdigest() == row["class_sha256"]
            assert hashlib.sha256((directory / row["disassembly"]).read_bytes()).hexdigest() == (
                row["disassembly_sha256"]
            )
        selected: set[str] = set()
        for name in archive.namelist():
            if name.startswith("data/betterend/worldgen/configured_feature/") and name.endswith(
                "_structures.json"
            ):
                config = cast("dict[str, dict[str, list[dict[str, str]]]]",
                              json.loads(archive.read(name)))
                selected.update(row["path"].removeprefix("/")
                                for row in config["config"]["structures"])
        prefix = "data/betterend/structure/biome/"
        templates = {n for n in archive.namelist() if n.startswith(prefix) and n.endswith(".nbt")}
        extra = {prefix + "blossoming_spires/house.nbt"} | {
            f"{prefix}old_bulbis_gardens/{kind}_{i}.nbt"
            for kind in ("fallen_tree", "tree_stump") for i in range(1, 4)
        }
        assert templates - selected == extra
        legacy = {n for n in archive.namelist() if n.startswith(prefix) and n.endswith(".json")}
        assert legacy == {prefix + biome + "/structures.json" for biome in (
            "blossoming_spires", "chorus_forest", "foggy_mushroomland", "lantern_woods",
            "shadow_forest", "umbrella_jungle", "old_bulbis_gardens",
        )}
        for path in legacy:
            rows = cast("dict[str, list[dict[str, JsonValue]]]", json.loads(archive.read(path)))
            assert set(rows) == {"structures"}
            assert all(set(row) == {"nbt", "offsetY", "terrainMerge"}
                       for row in rows["structures"])
        for path in extra:
            template = template_summary(archive.read(path))
            if "/old_bulbis_gardens/" in path:
                assert template["entities"] == []
                assert template["block_entities"] == []
                palette = cast("list[dict[str, str]]", template["palette"])
                assert {state["Name"] for state in palette} <= {
                    "betterend:ivis_moss", "betterend:ivis_vine", "betterend:purple_polypore",
                    "byg:bulbis_stem", "byg:bulbis_wood", "minecraft:air",
                }
            else:
                assert template["size"] == [21, 32, 21]
                assert template["block_entities"]


def test_betterend_pillar_candidates_and_existing_end_components() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name == "BetterEnd-21.0.31.jar")
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    directory = Path("evidence/item-8/sources/betterend-pillar-end-hooks")
    raw = (directory / "identities.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "f39ee57a16f67349f29e98bfdd3fe2acf567b39b9d56f737f9d8d3655f860e04"
    )
    registry = Path("evidence/item-8/runtime/registry-r1/dumps/registry/minecraft")
    placed = read_registry(registry / "worldgen_placed_feature.txt")
    with ZipFile(source.path) as archive:
        identities = cast("list[dict[str, str]]", json.loads(raw))
        assert len(identities) == 8
        declarations = cast("dict[str, list[str]]", json.loads(
            archive.read("betterend.mixins.common.json")))
        for row in identities:
            assert row["archive"] == source.name
            assert row["archive_sha256"] == source.sha256
            assert hashlib.sha256(archive.read(row["class"])).hexdigest() == row["class_sha256"]
            assert hashlib.sha256((directory / row["disassembly"]).read_bytes()).hexdigest() == (
                row["disassembly_sha256"]
            )
            if "/mixin/common/" in row["class"]:
                assert Path(row["class"]).stem in declarations["mixins"]
        for name, chance in (("fallen_pillar", 20), ("obsidian_pillar_basement", 8)):
            identifier = "betterend:" + name
            assert identifier in placed
            definition = cast("dict[str, JsonValue]", json.loads(archive.read(
                f"data/betterend/worldgen/placed_feature/{name}.json")))
            assert definition == {
                "feature": {"type": identifier, "config": {}},
                "placement": [{"type": "minecraft:rarity_filter", "chance": chance},
                              {"type": "minecraft:in_square"}, {"type": "minecraft:biome"}],
            }
            consumers: set[str] = set()
            for path in archive.namelist():
                if path.startswith("data/betterend/worldgen/biome/") and path.endswith(".json"):
                    biome = cast("dict[str, list[list[str]]]", json.loads(archive.read(path)))
                    if any(identifier in group for group in biome["features"]):
                        consumers.add(Path(path).stem)
            assert consumers == {"dragon_graveyards"}
        pillars = {n for n in archive.namelist()
                   if n.startswith("data/betterend/structure/pillars/") and not n.endswith("/")}
        assert pillars == {
            f"data/betterend/structure/pillars/pillar_{part}_{i}{suffix}.nbt"
            for i in range(1, 5) for part, suffix in (("base", ""), ("top", ""), ("top", "_cage"))
        }
        for name in pillars | {
            "data/betterend/structure/portal/end_portal_active.nbt",
            "data/betterend/structure/portal/end_portal_inactive.nbt",
        }:
            assert template_summary(archive.read(name))["size"]


def test_betterend_complete_template_partition_and_village_graph() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name == "BetterEnd-21.0.31.jar")
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    directory = Path("evidence/item-8/sources/betterend-platform-portal-consumers")
    raw = (directory / "identities.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "816d2f16a1da5e6778d7d4f1f5a00104444dc94403d430c752c141926b0f8f0c"
    )
    graph_raw = Path("evidence/item-8/sources/pool-traces-content.json.gz").read_bytes()
    assert hashlib.sha256(graph_raw).hexdigest() == (
        "703eed7b5d558b54a62985c7f919d0254e8de613292364c514c5b47b298accc5"
    )
    graph = cast("dict[str, dict[str, dict[str, JsonValue]]]",
                 json.loads(gzip.decompress(graph_raw)))["structures"]["betterend:end_village"]
    with ZipFile(source.path) as archive:
        for row in cast("list[dict[str, str]]", json.loads(raw)):
            assert row["archive"] == source.name
            assert row["archive_sha256"] == source.sha256
            assert hashlib.sha256(archive.read(row["class"])).hexdigest() == row["class_sha256"]
            assert hashlib.sha256((directory / row["disassembly"]).read_bytes()).hexdigest() == (
                row["disassembly_sha256"]
            )
        templates = {n for n in archive.namelist() if n.endswith(".nbt")}
        assert len(templates) == 128
        assert all(n.startswith("data/betterend/structure/") for n in templates)
        assert Counter(n.split("/")[3] for n in templates) == {
            "biome": 70, "village": 43, "pillars": 12, "portal": 3,
        }
        village = {"betterend:" + n.removeprefix("data/betterend/structure/").removesuffix(".nbt")
                   for n in templates if "/structure/village/" in n}
        connected = set(cast("list[str]", graph["templates"]))
        assert connected <= village
        assert village - connected == {
            "betterend:village/decoration/work_01",
            "betterend:village/terminators/street_terminator_01",
        }
        assert graph["missing"] == [
            {"id": "betterend:village/street_decoration/work_01", "kind": "template"},
            {"id": "betterend:village/terminators/stree_terminator_01", "kind": "template"},
        ]
        assert graph["unresolved_elements"] == []
        pools = {"betterend:" + n.removeprefix(
            "data/betterend/worldgen/template_pool/").removesuffix(".json")
            for n in archive.namelist()
            if n.startswith("data/betterend/worldgen/template_pool/") and n.endswith(".json")}
        assert pools - set(cast("list[str]", graph["pools"])) == {"betterend:village/decorations"}
        assert json.loads(archive.read(
            "data/betterend/worldgen/template_pool/village/decorations.json")) == {
            "elements": [], "fallback": "betterend:village/terminators",
        }
        root = cast("dict[str, JsonValue]", json.loads(archive.read(
            "data/betterend/worldgen/structure/eternal_portal.json")))
        assert root["type"] == "betterend:eternal_portal"
        assert template_summary(archive.read(
            "data/betterend/structure/portal/eternal_portal.nbt"))["size"]
    registry = read_registry(Path(
        "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"))
    assert {"betterend:end_village", "betterend:eternal_portal"} <= set(registry)


def test_betterend_frozen_generator_keys_bind_captured_fields() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name == "BetterEnd-21.0.31.jar")
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    directory = Path("evidence/item-8/sources/betterend-generator-config")
    raw = (directory / "identities.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "ecf9389b2ff32e43bfedd76f5039971e8b4de987b0022373470f61a3b372334e"
    )
    identities = cast("list[dict[str, str]]", json.loads(raw))
    assert len(identities) == 1
    row = identities[0]
    assert row["archive"] == source.name
    assert row["archive_sha256"] == source.sha256
    with ZipFile(source.path) as archive:
        assert hashlib.sha256(archive.read(row["class"])).hexdigest() == row["class_sha256"]
    disassembly = (directory / row["disassembly"]).read_bytes()
    assert hashlib.sha256(disassembly).hexdigest() == row["disassembly_sha256"]
    raw_config = Path("evidence/item-6/frozen/config/betterend/generator.json").read_bytes()
    assert hashlib.sha256(raw_config).hexdigest() == (
        "6f1156606391286f22eda4f84a1101fa9059ca1efdd1b2be49d7ab29a37ffa75"
    )
    config = cast("dict[str, dict[str, JsonValue]]", json.loads(raw_config))
    for key, field in (
        ("generate_central_island", "generateCentralIsland"),
        ("generate_obsidian_platform", "generateObsidianPlatform"),
        ("has_portal", "hasPortal"), ("replace_portal", "replacePortal"),
        ("has_pillars", "hasPillars"), ("replace_pillars", "replacePillars"),
    ):
        assert config["structure"][key] is True
        assert ("// String " + key).encode() in disassembly
        assert ("// Field " + field + ":").encode() in disassembly
    assert config["structure"]["end_city_fail_chance"] == 1
    assert config["generator"]["use_new_generator"] is True
    assert config["entity"]["has_dragon_fights"] is True
    spawn = cast("dict[str, JsonValue]", config["entity"]["spawn"])
    assert spawn["has_spawn"] is False
    for key, field in (
        ("end_city_fail_chance", "endCityFailChance"),
        ("use_new_generator", "newGenerator"),
        ("has_dragon_fights", "hasDragonFights"), ("has_spawn", "changeSpawn"),
    ):
        assert ("// String " + key).encode() in disassembly
        assert ("// Field " + field + ":").encode() in disassembly
