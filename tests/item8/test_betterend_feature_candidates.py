from __future__ import annotations

import gzip
import hashlib
import json
import re
from collections import Counter
from io import BytesIO
from pathlib import Path
from typing import TYPE_CHECKING, cast
from zipfile import ZipFile

from mcpack_evidence.item8_registry import read_registry
from mcpack_evidence.item8_resource_selection import runtime_mod_ids
from mcpack_evidence.item8_sources import retained_sources
from mcpack_evidence.item8_templates import template_summary

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_betterend_complete_payload_categories_and_carver_consumers() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name == "BetterEnd-21.0.31.jar")
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        files = {n.filename for n in archive.infolist() if not n.is_dir()}
        assert len(files) == 9639
        data = {n for n in files if n.startswith("data/")}
        assert Counter("/".join(n.split("/")[:3]) for n in data) == {
            "data/betterend/advancement": 879, "data/betterend/recipe": 850,
            "data/betterend/loot_table": 655, "data/betterend/worldgen": 253,
            "data/betterend/wover": 160, "data/betterend/structure": 135,
            "data/minecraft/tags": 76, "data/betterend/tags": 55, "data/wover/tags": 29,
            "data/betterend/patchouli_books": 25, "data/c/tags": 21,
            "data/betterend/jukebox_song": 6, "data/betterend/datapacks": 5,
            "data/bclib/tags": 2, "data/betterend/enchantment": 1,
            "data/trinkets/entities": 1, "data/trinkets/tags": 1,
        }
        assets = {n for n in files if n.startswith("assets/")}
        assert Counter(Path(n).suffix for n in assets) == {
            ".json": 4005, ".png": 1686, ".ogg": 45, ".mcmeta": 25,
            ".frag": 19, ".properties": 10, ".vert": 7, ".ini": 1,
        }
        classes = {n for n in files if n.endswith(".class")}
        assert len(classes) == 668
        assert {n for n in classes if b"Lnet/neoforged/fml/common/Mod;" in archive.read(n)} == {
            "org/betterx/betterend/BetterEnd.class",
        }
        cache = {n for n in files if n.startswith(".cache/")}
        assert len(cache) == 10
        assert files - data - assets - classes - cache == {
            "META-INF/MANIFEST.MF", "META-INF/accesstransformer.cfg",
            "META-INF/neoforge.mods.toml", "betterend.accesswidener",
            "betterend.mixins.client.json", "betterend.mixins.common.json",
            "betterend.refmap.json", "LICENSE", "LICENSE.ASSETS",
        }
        prefix = "data/betterend/worldgen/"
        assert Counter(n[len(prefix):].split("/")[0] for n in data if n.startswith(prefix)) == {
            "placed_feature": 147, "configured_feature": 40, "biome": 27,
            "structure": 14, "structure_set": 12, "template_pool": 6,
            "processor_list": 5, "configured_carver": 2,
        }
        carver_types = {"round_cave": "end_round_cave", "tunnel_cave": "end_tunnel_cave"}
        for name, kind in carver_types.items():
            definition = cast("dict[str, JsonValue]", json.loads(archive.read(
                prefix + "configured_carver/" + name + ".json")))
            assert definition["type"] == "betterend:" + kind
        nourishment = "data/betterend/datapacks/nourish_extensions/"
        assert {n for n in data if n.startswith("data/betterend/datapacks/")} == {
            nourishment + "pack.mcmeta",
            *(nourishment + "data/nourish/tags/item/" + name + ".json"
              for name in ("fats", "fruit", "protein", "sweets")),
        }
        directory = Path("evidence/item-8/sources/betterend-configured-carvers")
        raw = (directory / "identities.json").read_bytes()
        assert hashlib.sha256(raw).hexdigest() == (
            "7b8c98b8426309d3b5b6457d99af0a6a4273a16aabf23914bc418360c27223ba"
        )
        rows = cast("list[dict[str, str]]", json.loads(raw))
        assert len(rows) == 8
        for row in rows:
            assert row["archive"] == source.name
            assert row["archive_sha256"] == source.sha256
            assert hashlib.sha256(archive.read(row["class"])).hexdigest() == row["class_sha256"]
            raw = (directory / row["disassembly"]).read_bytes()
            assert hashlib.sha256(raw).hexdigest() == row["disassembly_sha256"]


def test_betterend_remaining_feature_types_have_explicit_roles() -> None:
    roles = {
        "existing_authored_candidates": {
            "building_list_feature", "crashed_ship", "fallen_pillar", "obsidian_pillar_basement",
        },
        "terrain_and_cave_consumers": {
            "arch_feature", "big_aurora_crystal", "cave_chunk_populator", "desert_lake",
            "floating_spire", "geyser", "ice_star", "obsidian_boulder", "ore_layer",
            "overworld_island", "pond_with_waterfall", "round_cave", "single_block_feature",
            "smaragdant_crystal", "spire", "stalactite_cluster", "stalactite_feature",
            "sulphur_hill", "sulphuric_lake", "surface_vent", "thin_arch_feature", "tunel_cave",
        },
        "vegetation_and_ecological_nest": {
            "amaranita_patch", "blue_vine_feature", "bush_feature", "bush_with_outer_feature",
            "cave_pumpkin", "charnia_feature", "double_plant_feature", "dragon_helix_tree",
            "dragon_tree", "end_lily_feature", "end_lotus_feature", "end_lotus_leaf_feature",
            "filalux_feature", "gigantic_amaranita", "glow_pillar_feature", "helix_tree",
            "hydralux_feature", "jellyshroom", "lacugrove", "lanceleaf_feature",
            "large_amaranita", "lucernia", "lumecorn", "menger_sponge_feature",
            "mossy_glowshroom", "neon_cactus", "pythadendron_tree", "silk_moth_nest",
            "single_inverted_scatter_feature", "single_plant_feature", "tenanea", "tenanea_bush",
            "umbrella_tree", "underwater_plant_feature", "vine_feature", "wall_plant_feature",
            "wall_plant_on_log_feature",
        },
    }
    assigned = [name for names in roles.values() for name in names]
    assert len(assigned) == len(set(assigned)) == 63
    source = next(s for s in retained_sources(Path.cwd()) if s.name == "BetterEnd-21.0.31.jar")
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    types: set[str] = set()
    with ZipFile(source.path) as archive:
        for name in archive.namelist():
            if not name.endswith(".json"):
                continue
            if name.startswith("data/betterend/worldgen/configured_feature/"):
                definition = cast("dict[str, JsonValue]", json.loads(archive.read(name)))
                types.add(str(definition["type"]))
            elif name.startswith("data/betterend/worldgen/placed_feature/"):
                definition = cast("dict[str, JsonValue]", json.loads(archive.read(name)))
                feature = definition["feature"]
                if isinstance(feature, dict):
                    types.add(str(feature["type"]))
    assert types == {"betterend:" + name for name in assigned} | {
        "minecraft:ore", "minecraft:random_patch", "minecraft:vegetation_patch",
        "minecraft:multiface_growth",
    }
    directory = Path("evidence/item-8/sources/betterend-feature-scope/BetterEnd-21.0.31.jar")
    registration = (directory / "org.betterx.betterend.registry.EndFeatures.txt").read_text()
    body = registration.split("  public static void register(", 1)[1].split(
        "  public static void onRegister(", 1)[0]
    registered = set(re.findall(r"// String ([a-z0-9_]+)", body))
    assert set(assigned) <= registered


def test_betterend_complete_feature_package_and_delegated_growth_are_preserved() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name == "BetterEnd-21.0.31.jar")
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    directories = {
        "betterend-feature-scope":
            "7a3fe03fddacad093573ad808d94b41463643acf11df321dc2b7a6fdeb5dd30d",
        "betterend-entry-template-consumers":
            "22dee10074c502f7026b266335c5d2966a47374504ae836d2f1da17e79a895d8",
        "betterend-pillar-end-hooks":
            "f39ee57a16f67349f29e98bfdd3fe2acf567b39b9d56f737f9d8d3655f860e04",
        "betterend-platform-portal-consumers":
            "816d2f16a1da5e6778d7d4f1f5a00104444dc94403d430c752c141926b0f8f0c",
        "betterend-remaining-root-consumers":
            "eb0d8ea37b2766dc0081c0e84035d9c37168758023bb33400d3028ef73363dbd",
        "betterend-remaining-features":
            "8ff7d86a2ca142e9a4fc4eac7bfee020c9e5301be3cb894ad7b42015578d0254",
        "betterend-delegated-plants":
            "2252cf72f8e265ab1b314a98677c758eb0735264a09707e1d5595a8b1e908d16",
    }
    captured: set[str] = set()
    prefix = "org/betterx/betterend/world/features/"
    with ZipFile(source.path) as archive:
        for name, digest in directories.items():
            directory = Path("evidence/item-8/sources") / name
            raw = (directory / "identities.json").read_bytes()
            assert hashlib.sha256(raw).hexdigest() == digest
            for row in cast("list[dict[str, str]]", json.loads(raw)):
                assert row["archive"] == source.name
                assert row["archive_sha256"] == source.sha256
                assert hashlib.sha256(archive.read(row["class"])).hexdigest() == (
                    row["class_sha256"]
                )
                raw = (directory / row["disassembly"]).read_bytes()
                assert hashlib.sha256(raw).hexdigest() == row["disassembly_sha256"]
                if row["class"].startswith(prefix):
                    assert row["class"] not in captured
                    captured.add(row["class"])
        assert len(captured) == 94
        assert captured == {n for n in archive.namelist()
                            if n.startswith(prefix) and n.endswith(".class")}


def test_betterend_biome_modifiers_bind_existing_candidate_consumers() -> None:
    sources = retained_sources(Path.cwd())
    betterend = next(s for s in sources if s.name == "BetterEnd-21.0.31.jar")
    wover = next(s for s in sources if s.name == "worldweaver-21.0.24.jar")
    for source in (betterend, wover):
        assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    modifiers = {
        "defaults": "01a91be1e3ff0ca9f3991494df804b2bd44ac7eabf07738fb016c582a1808681",
        "eternal_portals": "b8a7f3de02012a9d9661e33b95ee7d9c699d00b29c471a05c2f70cdf153506f6",
    }
    with ZipFile(betterend.path) as archive:
        prefix = "data/betterend/wover/worldgen/biome_modifications/"
        assert {n.filename for n in archive.infolist()
                if n.filename.startswith(prefix) and not n.is_dir()} == {
            prefix + name + ".json" for name in modifiers
        }
        for name, digest in modifiers.items():
            assert hashlib.sha256(archive.read(prefix + name + ".json")).hexdigest() == digest
        default = cast("dict[str, JsonValue]", json.loads(archive.read(prefix + "defaults.json")))
        assert default["features"] == [[], [], [], [], ["betterend:crashed_ship"], [], [
            "betterend:flavolite_layer", "betterend:thallasium_ore", "betterend:ender_ore",
        ]]
        portal = cast("dict[str, JsonValue]", json.loads(archive.read(
            prefix + "eternal_portals.json")))
        assert portal["biome_tags"] == ["betterend:has_structure/eternal_portal"]
    directories = {
        "wover-biome-modifier-consumers":
            "a369761c4511706e0486eae7465fb74d379e4dc97f91dd74113c206b71d55868",
        "wover-biome-modifier-codec":
            "dfea087f9938a66807e94d9d2f9a46d110e82dae07092fde2777780979299cbf",
    }
    with ZipFile(wover.path) as archive:
        for name, digest in directories.items():
            directory = Path("evidence/item-8/sources") / name
            raw = (directory / "identities.json").read_bytes()
            assert hashlib.sha256(raw).hexdigest() == digest
            for row in cast("list[dict[str, str]]", json.loads(raw)):
                assert row["archive"] == wover.name
                assert row["archive_sha256"] == wover.sha256
                assert hashlib.sha256(archive.read(row["class"])).hexdigest() == (
                    row["class_sha256"]
                )
                raw = (directory / row["disassembly"]).read_bytes()
                assert hashlib.sha256(raw).hexdigest() == row["disassembly_sha256"]


def test_betterend_all_declared_common_mixin_consumers_are_preserved() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name == "BetterEnd-21.0.31.jar")
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    directories = {
        "betterend-pillar-end-hooks":
            "f39ee57a16f67349f29e98bfdd3fe2acf567b39b9d56f737f9d8d3655f860e04",
        "betterend-common-mixins":
            "5dd3d155fcd660a11f2950742cffce16b67fba212735daa59ef83c8948d7d9a1",
    }
    captured: set[str] = set()
    with ZipFile(source.path) as archive:
        for name, digest in directories.items():
            directory = Path("evidence/item-8/sources") / name
            raw = (directory / "identities.json").read_bytes()
            assert hashlib.sha256(raw).hexdigest() == digest
            for row in cast("list[dict[str, str]]", json.loads(raw)):
                assert row["archive"] == source.name
                assert row["archive_sha256"] == source.sha256
                assert hashlib.sha256(archive.read(row["class"])).hexdigest() == (
                    row["class_sha256"]
                )
                disassembly = (directory / row["disassembly"]).read_bytes()
                assert hashlib.sha256(disassembly).hexdigest() == row["disassembly_sha256"]
                if "/mixin/common/" in row["class"]:
                    assert row["class"] not in captured
                    captured.add(row["class"])
        declared = cast("dict[str, JsonValue]", json.loads(
            archive.read("betterend.mixins.common.json")))
        prefix = str(declared["package"]).replace(".", "/") + "/"
        names = cast("list[str]", declared["mixins"])
        assert len(names) == len(set(names)) == 32
        assert captured == {prefix + name.replace(".", "/") + ".class" for name in names}


def test_betterend_retained_plugin_and_compatibility_inputs() -> None:
    log = Path("evidence/raw/item8/registry-r1/debug.log").read_bytes()
    assert hashlib.sha256(log).hexdigest() == (
        "e5b47378d791027242ba28dd36c999c07ae4e01a1b90e1534e66bcd42c1e694b"
    )
    loaded = runtime_mod_ids(log.decode())
    assert {"betterend", "bclib"} <= loaded.keys()
    assert {"byg", "flamboyant", "dye_depot"}.isdisjoint(loaded)
    sources = retained_sources(Path.cwd())[2:]
    assert len(sources) == 136
    service = "META-INF/services/org.betterx.betterend.api.BetterEndPlugin"
    # ServiceLoader providers must be declared. Include nested and modular declarations.
    for source in sources:
        raw = source.path.read_bytes()
        assert hashlib.sha256(raw).hexdigest() == source.sha256
        pending = [(source.name, raw)]
        while pending:
            label, payload = pending.pop()
            with ZipFile(BytesIO(payload)) as archive:
                names = archive.namelist()
                assert service not in names, label
                for name in names:
                    if name.endswith(".jar"):
                        pending.append((label + "!/" + name, archive.read(name)))
                    elif name.endswith("module-info.class"):
                        assert b"org/betterx/betterend/api/BetterEndPlugin" not in (
                            archive.read(name)
                        ), label + "!/" + name
    source = next(s for s in sources if s.name == "bclib-21.0.24.jar")
    directory = Path("evidence/item-8/sources/bclib-integration-dispatch")
    raw = (directory / "identities.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "d085183016dd793119d9f8bbab449fbbc791851dce4ea8244e18da2e9aa4af2c"
    )
    with ZipFile(source.path) as archive:
        for row in cast("list[dict[str, str]]", json.loads(raw)):
            assert row["archive"] == source.name
            assert row["archive_sha256"] == source.sha256
            assert hashlib.sha256(archive.read(row["class"])).hexdigest() == row["class_sha256"]
            assert hashlib.sha256((directory / row["disassembly"]).read_bytes()).hexdigest() == (
                row["disassembly_sha256"]
            )


def test_betterend_packaged_roots_and_remaining_consumers() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name == "BetterEnd-21.0.31.jar")
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    roots = {
        "end_bridge", "end_lake", "end_lake_normal", "end_lake_rare", "end_village",
        "eternal_portal", "giant_ice_star", "giant_mossy_glowshroom", "megalake",
        "megalake_small", "mountain", "painted_mountain", "small_island", "sulphuric_cave",
    }
    directory = Path("evidence/item-8/sources/betterend-remaining-root-consumers")
    raw = (directory / "identities.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "eb0d8ea37b2766dc0081c0e84035d9c37168758023bb33400d3028ef73363dbd"
    )
    with ZipFile(source.path) as archive:
        rows = cast("list[dict[str, str]]", json.loads(raw))
        assert len(rows) == 18
        for row in rows:
            assert row["archive"] == source.name
            assert row["archive_sha256"] == source.sha256
            assert hashlib.sha256(archive.read(row["class"])).hexdigest() == row["class_sha256"]
            assert hashlib.sha256((directory / row["disassembly"]).read_bytes()).hexdigest() == (
                row["disassembly_sha256"]
            )
        prefix = "data/betterend/worldgen/structure/"
        assert {n.filename for n in archive.infolist()
                if n.filename.startswith(prefix) and not n.is_dir()} == {
            prefix + name + ".json" for name in roots
        }
        for name in roots:
            definition = cast("dict[str, JsonValue]", json.loads(
                archive.read(prefix + name + ".json")))
            assert definition["type"] == (
                "minecraft:jigsaw" if name == "end_village" else "betterend:" + name
            )
        village_feature = cast("dict[str, JsonValue]", json.loads(archive.read(
            "data/betterend/worldgen/placed_feature/village_chorus.json")))
        assert village_feature["feature"] == "minecraft:chorus_plant"
    live = read_registry(Path(
        "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"))
    assert {name for name in live if name.startswith("betterend:")} == {
        "betterend:" + name for name in roots
    }


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
    decisions = cast("dict[str, JsonValue]", json.loads(Path(
        "evidence/item-8/family-decisions.json").read_bytes()))
    content = cast("dict[str, JsonValue]", decisions["non_registry_content"])
    contributions = cast("dict[str, dict[str, JsonValue]]", content["contributions"])
    ship = contributions["betterend:crashed_ship"]
    assert ship["placed_feature"] == "betterend:crashed_ship"
    assert ship["class_to_template"] == {"CrashedShipFeature": "minecraft:end_city/ship"}
    for path, digest in cast("dict[str, str]", ship["evidence"]).items():
        assert hashlib.sha256(Path(path).read_bytes()).hexdigest() == digest
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
    decisions = cast("dict[str, JsonValue]", json.loads(Path(
        "evidence/item-8/family-decisions.json").read_bytes()))
    content = cast("dict[str, JsonValue]", decisions["non_registry_content"])
    contributions = cast("dict[str, dict[str, JsonValue]]", content["contributions"])
    for name in ("lantern_woods/light_1", "blossoming_spires/house"):
        decision = contributions["betterend:" + name]
        assert decision["families"] == []
        assert decision["template"] == f"data/betterend/structure/biome/{name}.nbt"
        for path, digest in cast("dict[str, str]", decision["evidence"]).items():
            assert hashlib.sha256(Path(path).read_bytes()).hexdigest() == digest
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
        light = prefix + "lantern_woods/light_1.nbt"
        assert light in selected
        fixture = template_summary(archive.read(light))
        assert fixture["size"] == [1, 5, 3]
        assert {state["Name"] for state in cast("list[dict[str, str]]", fixture["palette"])} == {
            "betterend:filalux", "betterend:flavolite_pedestal", "betterend:flavolite_wall",
            "betterend:lucernia_fence", "betterend:thallasium_chain",
        }
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
    decisions = cast("dict[str, JsonValue]", json.loads(Path(
        "evidence/item-8/family-decisions.json").read_bytes()))
    content = cast("dict[str, JsonValue]", decisions["non_registry_content"])
    contributions = cast("dict[str, dict[str, JsonValue]]", content["contributions"])
    decision = contributions["betterend:ruined_obsidian_pillar"]
    assert decision["families"] == ["betterend:ruined_obsidian_pillar"]
    assert set(cast("dict[str, JsonValue]", decision["variants"])) == {
        "betterend:fallen_pillar", "betterend:obsidian_pillar_basement",
    }
    assert decision["placed_features"] == sorted(cast("dict[str, JsonValue]", decision["variants"]))
    assert decision["packaged_biome_consumer"] == "betterend:dragon_graveyards"
    for path, digest in cast("dict[str, str]", decision["evidence"]).items():
        assert hashlib.sha256(Path(path).read_bytes()).hexdigest() == digest
    dimensions = cast("dict[str, list[str]]", json.loads(Path(
        "evidence/item-8/runtime/dimension-r3/dimension-biomes.json").read_bytes()))
    assert decision["packaged_biome_consumer"] in dimensions["minecraft:the_end"]
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
