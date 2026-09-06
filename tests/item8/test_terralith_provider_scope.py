from __future__ import annotations

import gzip
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import TYPE_CHECKING, cast
from zipfile import ZipFile

from mcpack_evidence.item8_inventory import resource_identity

if TYPE_CHECKING:
    from pydantic import JsonValue

from mcpack_evidence.item8_sources import retained_sources


def test_terralith_provider_payload_and_components() -> None:  # noqa: PLR0915
    source = next(s for s in retained_sources(Path.cwd()) if s.name.startswith("Terralith_"))
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    directory = Path("evidence/item-8/sources/terralith-provider")
    raw = (directory / "identities.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "cf0cdfa21a06651e123ae119eadc733c62cc9457fc1131311aac614d5148b1c9"
    )
    identities = cast("list[dict[str, str]]", json.loads(raw))
    with ZipFile(source.path) as archive:
        names = [n for n in archive.namelist() if not n.endswith("/")]
        assert len(names) == len(set(names)) == 2075
        classes = {row["class"] for row in identities}
        assert len(classes) == 11
        assert {n for n in names if n.endswith(".class")} == classes
        for row in identities:
            assert row["archive"] == source.name
            assert row["archive_sha256"] == source.sha256
            assert hashlib.sha256(archive.read(row["class"])).hexdigest() == row["class_sha256"]
            assert hashlib.sha256((directory / row["disassembly"]).read_bytes()).hexdigest() == (
                row["disassembly_sha256"]
            )
        groups = Counter(
            "/".join(n.split("/")[:4]) if n.startswith("data/") and "/worldgen/" in n
            else "/".join(n.split("/")[:3]) if n.startswith("data/")
            else n.split("/")[0]
            for n in names if n not in classes
        )
        assert groups == {
            "META-INF": 3, "assets": 24,
            "data/biome_tag_villagers/tags/worldgen": 6,
            "data/c/tags": 2, "data/c/tags/worldgen": 63,
            "data/c/worldgen/biome_colors.json": 1,
            "data/c/worldgen/structure_icons.json": 1,
            "data/minecraft/advancement": 5, "data/minecraft/dimension": 2,
            "data/minecraft/tags": 14, "data/minecraft/tags/worldgen": 55,
            "data/minecraft/wolf_variant": 9, "data/minecraft/worldgen/biome": 35,
            "data/minecraft/worldgen/configured_carver": 1,
            "data/minecraft/worldgen/configured_feature": 1,
            "data/minecraft/worldgen/density_function": 26,
            "data/minecraft/worldgen/multi_noise_biome_source_parameter_list": 1,
            "data/minecraft/worldgen/noise": 16, "data/minecraft/worldgen/noise_settings": 1,
            "data/minecraft/worldgen/placed_feature": 18,
            "data/sereneseasons/tags/worldgen": 1,
            "data/terralith/advancement": 1, "data/terralith/function": 4,
            "data/terralith/loot_table": 53, "data/terralith/predicate": 1,
            "data/terralith/recipe": 6, "data/terralith/structure": 173,
            "data/terralith/tags": 32, "data/terralith/tags/worldgen": 59,
            "data/terralith/worldgen/biome": 95,
            "data/terralith/worldgen/configured_carver": 1,
            "data/terralith/worldgen/configured_feature": 480,
            "data/terralith/worldgen/density_function": 78,
            "data/terralith/worldgen/noise": 116,
            "data/terralith/worldgen/placed_feature": 547,
            "data/terralith/worldgen/processor_list": 7,
            "data/terralith/worldgen/structure": 28,
            "data/terralith/worldgen/structure_set": 7,
            "data/terralith/worldgen/template_pool": 49,
            "disable.custom_structures": 7, "disable.intro_message": 1,
            "disable.skylands": 4, "disable.terrain_slabs": 5,
            "enable.recipe_changes": 14, "enable.vanilla_stone_gen": 6,
            "license.txt": 1, "pack.mcmeta": 1, "pack.png": 1,
            "patrons.txt": 1, "terralith.mixins.json": 1,
        }
        data = {n: cast("dict[str, JsonValue]", json.loads(archive.read(n)))
                for n in names if n.endswith(".json")}
        components = {
            kind: {found[0] for n in names
                   if (found := resource_identity(n, kind, extension)) and not found[1]}
            for kind, extension in (
                ("worldgen/structure", ".json"), ("worldgen/template_pool", ".json"),
                ("structure", ".nbt"),
            )
        }
        assert tuple(map(len, components.values())) == (28, 49, 173)
        assert {str(d["type"]) for n, d in data.items()
                if n.startswith("data/terralith/worldgen/structure/")} == {"minecraft:jigsaw"}
        pack = cast("dict[str, dict[str, list[dict[str, JsonValue]]]]",
                    json.loads(archive.read("pack.mcmeta")))
        config = cast("dict[str, dict[str, bool]]", json.loads(
            Path("evidence/item-6/frozen/config/terralith.json").read_bytes()
        ))
        assert config["modules"] == {
            "custom_structures": True, "intro_message": True, "recipe_changes": False,
            "skylands": True, "terrain_slabs": True, "vanilla_stone_gen": False,
        }
        overlays = pack["neoforge:overlays"]["entries"]
        assert len(overlays) == 6
        assert pack["overlays"]["entries"] == []
        for overlay in overlays:
            conditions = cast("list[dict[str, JsonValue]]", overlay["neoforge:conditions"])
            assert len(conditions) == 1
            condition = conditions[0]
            assert condition["type"] == "terralith:config"
            assert config["modules"][str(condition["key"])] == condition.get("invert", False)
        assert data["terralith.mixins.json"]["mixins"] == []
        assert archive.read("META-INF/accesstransformer.cfg") == b""
        functions = {n: archive.read(n).decode() for n in names if n.endswith(".mcfunction")}
        assert set(functions) == {
            "data/terralith/function/" + name + ".mcfunction"
            for name in ("setup", "toast", "enable_bundle", "rtp_testing")
        } | {"disable.intro_message/data/terralith/function/toast.mcfunction"}
        assert functions["disable.intro_message/data/terralith/function/toast.mcfunction"] == ""
        assert functions["data/terralith/function/rtp_testing.mcfunction"] == (
            "spreadplayers 0 0 1000000 1000000 under 128 false @s"
        )
        assert data["data/minecraft/tags/function/load.json"]["values"] == [
            {"id": "terralith:setup", "required": False}
        ]
    raw = Path("evidence/item-8/sources/pool-traces-content.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "703eed7b5d558b54a62985c7f919d0254e8de613292364c514c5b47b298accc5"
    )
    graph = cast("dict[str, dict[str, dict[str, JsonValue]]]", json.loads(gzip.decompress(raw)))
    traces = graph["structures"]
    roots = components["worldgen/structure"]
    assert roots == {r for r in traces if r.startswith("terralith:")}
    assert components["worldgen/template_pool"] - {
        p for r in roots for p in cast("list[str]", traces[r]["pools"])
    } == {"terralith:nothing", "terralith:spire", "terralith:village/baby_villager"}
    unused = components["structure"] - {
        t for r in roots for t in cast("list[str]", traces[r]["templates"])
    }
    assert unused == {"terralith:" + name for name in (
        "cave/dungeon1", "highlands/ruin1", "null_structure",
        "small_decoration/boulder", "small_decoration/candle_1",
        "small_decoration/crumbling_tower", "small_decoration/farm_1",
        "small_decoration/frog_fountain", "small_decoration/giant_bee_hive",
        "small_decoration/old_well", "small_decoration/poppy_circle",
        "unsorted/brick_chimney_1", "unsorted/brick_chimney_2", "unsorted/brick_chimney_3",
        "unsorted/cobble_chimney_1", "unsorted/cobble_chimney_2", "unsorted/cobble_chimney_3",
        "unsorted/cobble_tower_ruin", "unsorted/cobble_wash-house", "unsorted/giant_pumpkin",
        "unsorted/giant_watermelon", "unsorted/nostalgic_ruin", "unsorted/ruined_dark_oak_house",
        "unsorted/stone_brick_pillars_ruins_1", "unsorted/stone_brick_pillars_ruins_2",
        "unsorted/stone_brick_pillars_ruins_3", "unsorted/stone_brick_pillars_ruins_4",
        "unsorted/stone_brick_sun_dial", "unsorted/stonebricks_tower_ruin",
        "unsorted/vc_camp_campfire", "unsorted/vc_camp_cw", "unsorted/vc_camp_haybale",
        "unsorted/vc_camp_storage", "unsorted/vc_camp_tracks", "unsorted/vc_camp_tracks_corner",
        "unsorted/vc_camp_tracks_small", "unsorted/vc_cart", "unsorted/vc_trackend",
        "unsorted/vc_trackend_bl", "unsorted/vc_trackend_br", "unsorted/villager_outpost",
        "unsorted/wood_barn_ruin", "village/desert/houses/farm1", "village/desert/houses/tanner1",
        "village/fortified/houses/big1", "village/fortified/houses/large_house_rework",
        "village/fortified/houses/stable",
    )}
    assert {r: traces[r]["missing"] for r in roots if traces[r]["missing"]} == {
        "terralith:fortified_desert_village": [
            {"id": "terralith:village/desert/houses/farmer", "kind": "template"},
            {"id": "terralith:village/desert/houses/toolsmith1", "kind": "template"},
        ]
    }
    assert all(not traces[r]["unresolved_elements"] for r in roots)


def test_terralith_feature_routes_and_named_decoration_candidate() -> None:
    decisions = cast("dict[str, JsonValue]", json.loads(Path(
        "evidence/item-8/family-decisions.json").read_bytes()))
    content = cast("dict[str, JsonValue]", decisions["non_registry_content"])
    contributions = cast("dict[str, dict[str, JsonValue]]", content["contributions"])
    fixture = contributions["terralith:cave/frostfire/frostfire_ceiling"]
    assert fixture["families"] == []
    assert fixture["configured_resource"] == (
        "data/terralith/worldgen/configured_feature/cave/frostfire/frostfire_ceiling.json"
    )
    for path, digest in cast("dict[str, str]", fixture["evidence"]).items():
        assert hashlib.sha256(Path(path).read_bytes()).hexdigest() == digest
    source = next(s for s in retained_sources(Path.cwd()) if s.name.startswith("Terralith_"))
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        data = {n: cast("dict[str, JsonValue]", json.loads(archive.read(n)))
                for n in archive.namelist() if n.endswith(".json")}
    features = {n: d for n, d in data.items()
                if resource_identity(n, "worldgen/configured_feature")}
    assert Counter(str(d["type"]) for d in features.values()) == {
        "minecraft:ore": 20, "minecraft:random_patch": 36,
        "minecraft:random_selector": 65, "minecraft:tree": 186,
        "minecraft:disk": 23, "minecraft:simple_random_selector": 15,
        "minecraft:simple_block": 41, "minecraft:geode": 6,
        "minecraft:vegetation_patch": 34, "minecraft:flower": 7,
        "minecraft:block_column": 9, "minecraft:netherrack_replace_blobs": 12,
        "minecraft:large_dripstone": 2, "minecraft:sculk_patch": 1,
        "minecraft:multiface_growth": 4, "random_selector": 1,
        "minecraft:spring_feature": 2, "minecraft:forest_rock": 1,
        "minecraft:nether_forest_vegetation": 1,
        "minecraft:waterlogged_vegetation_patch": 4, "minecraft:block_pile": 2,
        "minecraft:vines": 2, "minecraft:huge_brown_mushroom": 1,
        "minecraft:huge_red_mushroom": 1, "minecraft:no_op": 6,
        "minecraft:bamboo": 1, "minecraft:dripstone_cluster": 2,
        "minecraft:underwater_magma": 1,
    }
    pending: list[JsonValue] = list(features.values())
    while pending:
        value = pending.pop()
        if isinstance(value, dict):
            if "type" in value:
                kind = str(value["type"])
                assert ":" not in kind or kind.startswith("minecraft:"), kind
            pending.extend(value.values())
        elif isinstance(value, list):
            pending.extend(value)
    # These vanilla feature codecs also author a visible ornament. Retain its
    # candidate identity instead of treating a vanilla type as absence proof.
    frost = "cave/frostfire/frostfire_ceiling"
    config = cast("dict[str, JsonValue]", features[
        f"data/terralith/worldgen/configured_feature/{frost}.json"
    ]["config"])
    vegetation = cast("dict[str, dict[str, JsonValue]]", config["vegetation_feature"])
    selector = cast("dict[str, JsonValue]", vegetation["feature"]["config"])
    choices = cast("list[dict[str, JsonValue]]", selector["features"])
    assert len(choices) == 1
    assert choices[0]["chance"] == 0.07
    placed = cast("dict[str, dict[str, JsonValue]]", choices[0]["feature"])
    column = cast("dict[str, JsonValue]", placed["feature"]["config"])
    assert column["direction"] == "down"
    layers = cast("list[dict[str, JsonValue]]", column["layers"])
    assert [cast("dict[str, dict[str, str]]", layer["provider"])["state"]["Name"]
            for layer in layers] == ["minecraft:chain", "minecraft:soul_lantern"]
    assert data[f"data/terralith/worldgen/placed_feature/{frost}.json"]["feature"] == (
        "terralith:" + frost
    )
    assert any("terralith:" + frost in step for step in cast("list[list[str]]", data[
        "data/terralith/worldgen/biome/cave/frostfire_caves.json"
    ]["features"]))
    # Vents use single campfires below magma/water. They are geothermal terrain
    # effects, not an independently authored campsite layout.
    vent = "data/terralith/worldgen/"
    assert features[vent + "configured_feature/yellowstone/vents.json"]["type"] == (
        "minecraft:simple_block"
    )
    placements = cast("list[dict[str, JsonValue]]", data[
        vent + "placed_feature/yellowstone/vents.json"
    ]["placement"])
    scan = next(p for p in placements if p["type"] == "minecraft:environment_scan")
    assert scan["direction_of_search"] == "down"
    assert scan["target_condition"] == {
        "type": "minecraft:all_of", "predicates": [
            {"type": "minecraft:matching_blocks", "blocks": ["minecraft:magma_block"],
             "offset": [0, 1, 0]},
            {"type": "minecraft:matching_blocks", "blocks": ["minecraft:water"],
             "offset": [0, 2, 0]},
            {"type": "minecraft:matching_blocks", "blocks": ["minecraft:air"],
             "offset": [0, 5, 0]},
        ],
    }
    for biome in ("caldera", "yellowstone"):
        assert any("terralith:yellowstone/vents" in step for step in cast(
            "list[list[str]]", data[vent + f"biome/{biome}.json"]["features"]
        ))
