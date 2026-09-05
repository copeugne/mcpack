from __future__ import annotations

import gzip
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import TYPE_CHECKING, cast

from mcpack_evidence.item8_registry import read_registry
from mcpack_evidence.item8_resource_selection import select_resources

if TYPE_CHECKING:
    from pydantic import JsonValue


# Keep the observed feature grammar in one proof, without a new traversal framework.
def test_selected_feature_modifier_references() -> None:  # noqa: C901, PLR0915
    root = Path(__file__).resolve().parents[2]
    raw = (root / "evidence/item-8/sources/packaged-json-redacted.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "a5279d453f32edf7b1adc5c06b09953785b990b4b01c362b1423ed2f88930fdd"
    )
    catalog = cast("dict[str, JsonValue]", json.loads(gzip.decompress(raw)))
    resources = cast("list[JsonValue]", catalog["resources"])
    config_path = root / "evidence/item-6/frozen/config/regions_unexplored/common.json"
    config_raw = config_path.read_bytes()
    assert hashlib.sha256(config_raw).hexdigest() == (
        "300dda462e31f6f1bcce0d67308e4939d1b461a03c8cc92ba805f7ac9d1cb66c"
    )
    # This exact frozen file has standalone // comment lines, not inline comments.
    configuration = cast("dict[str, JsonValue]", json.loads("\n".join(
        line for line in config_raw.decode().splitlines() if not line.lstrip().startswith("//")
    )))
    toggles = configuration["vanilla_changes"]
    assert isinstance(toggles, dict)
    placed_sources, _ = select_resources(
        resources, "worldgen/placed_feature",
        enabled_packs=["vanilla", "mod_data"], lithostitched_overlay=True,
    )
    configured_sources, _ = select_resources(
        resources, "worldgen/configured_feature",
        enabled_packs=["vanilla", "mod_data"], lithostitched_overlay=True,
    )
    modifiers, _ = select_resources(
        resources, "lithostitched/worldgen_modifier",
        enabled_packs=["vanilla", "mod_data"], lithostitched_overlay=True,
    )
    seen: set[tuple[str, str]] = set()
    terminals: set[str] = set()
    component_types: set[str] = set()
    configured_blocks: set[str] = set()
    counts: Counter[str] = Counter()

    def inspect_terminal(value: JsonValue) -> None:
        if isinstance(value, dict):
            kind = value.get("type")
            if kind is not None:
                assert isinstance(kind, str)
                component_types.add(kind)
            for key in ("Name", "block"):
                if key in value:
                    block = value[key]
                    assert isinstance(block, str)
                    configured_blocks.add(block)
            if "blocks" in value:
                blocks = value["blocks"]
                assert isinstance(blocks, list)
                for block in blocks:
                    assert isinstance(block, str)
                    configured_blocks.add(block)
            for child in value.values():
                inspect_terminal(child)
        elif isinstance(value, list):
            for child in value:
                inspect_terminal(child)

    def placed(value: JsonValue) -> None:
        if isinstance(value, str):
            key = ("placed", value)
            if key in seen:
                return
            seen.add(key)
            value = placed_sources[value]["document"]
        assert isinstance(value, dict)
        assert set(value) == {"feature", "placement"}
        configured(value["feature"])

    def configured(value: JsonValue) -> None:
        if isinstance(value, str):
            key = ("configured", value)
            if key in seen:
                return
            seen.add(key)
            value = configured_sources[value]["document"]
        assert isinstance(value, dict)
        assert set(value) == {"type", "config"}
        kind, config = value["type"], value["config"]
        assert isinstance(kind, str)
        assert isinstance(config, dict)
        if kind in {"minecraft:random_patch", "minecraft:flower"}:
            placed(config["feature"])
        elif kind in {"lithostitched:weighted_selector", "lithostitched:composite"}:
            assert isinstance(config["features"], list)
            for feature in config["features"]:
                assert isinstance(feature, dict)
                if "data" in feature:
                    assert kind == "lithostitched:weighted_selector"
                    assert set(feature) == {"data", "weight"}
                    weight = feature["weight"]
                    assert isinstance(weight, int)
                    assert weight > 0
                    placed(feature["data"])
                else:
                    placed(feature)
        elif kind == "minecraft:random_selector":
            placed(config["default"])
            assert isinstance(config["features"], list)
            for feature in config["features"]:
                assert isinstance(feature, dict)
                placed(feature["feature"])
        else:
            # These are implementation endpoints, not absence-of-content claims.
            terminals.add(kind)
            inspect_terminal(config)

    for resource in modifiers.values():
        document = resource["document"]
        assert isinstance(document, dict)
        kind = document["type"]
        if kind not in {"lithostitched:add_features", "lithostitched:remove_features"}:
            continue
        assert isinstance(kind, str)
        assert resource["archive"] == "regions-unexplored-0.6.1-neoforge-21.1.jar"
        predicate = document["predicate"]
        assert isinstance(predicate, dict)
        assert set(predicate) == {"type", "key"}
        assert predicate["type"] == "regions_unexplored:config"
        key = predicate["key"]
        assert isinstance(key, str)
        assert key.startswith("vanilla_changes/")
        assert toggles[key.removeprefix("vanilla_changes/")] is True
        counts[kind] += 1
        # Predicate truth does not prove successful placement in a generated world.
        features = document["features"]
        if isinstance(features, str):
            features = [features]
        assert isinstance(features, list)
        for feature in features:
            placed(feature)
    assert counts == {"lithostitched:add_features": 30, "lithostitched:remove_features": 4}
    assert Counter(kind for kind, _ in seen) == {"placed": 34, "configured": 41}
    assert terminals == {
        "minecraft:simple_block", "minecraft:tree", "regions_unexplored:saguaro_cactus",
        "regions_unexplored:palm_tree", "regions_unexplored:bamboo_tree",
        "regions_unexplored:giant_lily",
    }
    assert component_types == {
        "lithostitched:random_block", "minecraft:blob_foliage_placer",
        "minecraft:leave_vine", "minecraft:pine_foliage_placer",
        "minecraft:simple_state_provider", "minecraft:straight_trunk_placer",
        "minecraft:two_layers_feature_size", "minecraft:uniform",
        "minecraft:weighted_state_provider", "regions_unexplored:randomized_ground_cover",
        "regions_unexplored:willow",
    }
    assert configured_blocks == {
        *("minecraft:" + name for name in (
            "acacia_leaves", "acacia_log", "dirt", "fern", "lily_pad", "oak_leaves",
            "oak_log", "short_grass",
        )),
        *("regions_unexplored:" + name for name in (
            "ash_vent", "bamboo_leaves", "bamboo_log", "birch_shrub", "blue_bioshroom",
            "cattail", "cherry_shrub", "dark_oak_shrub", "day_lily", "dead_steppe_shrub",
            "elephant_ear", "flowering_lily_pad", "flowering_shrub", "frozen_grass",
            "green_bioshroom", "hibiscus", "jungle_shrub", "mangrove_shrub", "meadow_sage",
            "oak_branch", "oak_shrub", "orange_coneflower", "palm_beard", "palm_leaves",
            "palm_log", "pine_shrub", "purple_coneflower", "redwood_branch", "saguaro_cactus",
            "saguaro_cactus_flower", "sandy_grass", "small_desert_shrub", "spruce_shrub",
            "tassel", "willow_leaves", "willow_log",
        )),
    }


def test_yungs_bridges_non_registry_path_binds_runtime_and_packaged_variants() -> None:
    decisions = cast("dict[str, JsonValue]", json.loads(
        Path("evidence/item-8/family-decisions.json").read_bytes()
    ))
    content = cast("dict[str, JsonValue]", decisions["non_registry_content"])
    contributions = cast("dict[str, dict[str, JsonValue]]", content["contributions"])
    contribution = contributions["yungsbridges:bridges"]
    for path, digest in cast("dict[str, str]", contribution["evidence"]).items():
        assert hashlib.sha256(Path(path).read_bytes()).hexdigest() == digest
    catalog = cast("dict[str, list[dict[str, JsonValue]]]", json.loads(gzip.decompress(Path(
        "evidence/item-8/sources/packaged-json-redacted.json.gz"
    ).read_bytes())))
    resources = {str(r["path"]): cast("dict[str, JsonValue]", r["document"])
                 for r in catalog["resources"]
                 if r["archive"] == "YungsBridges-1.21.1-NeoForge-5.1.1.jar"}
    modifier = resources[str(contribution["biome_modifier"])]
    assert modifier == {"type": "neoforge:add_features", "biomes": contribution["biome_tag"],
                        "features": [contribution["placed_feature"]],
                        "step": contribution["generation_step"]}
    prefix = "data/yungsbridges/worldgen/"
    assert resources[prefix + "placed_feature/bridge_list.json"] == {
        "feature": contribution["configured_feature"], "placement": [{"type": "minecraft:biome"}]
    }
    selector = resources[prefix + "configured_feature/bridge_list.json"]
    assert selector["type"] == "yungsbridges:multiple_attempt_single_random"
    links = cast("dict[str, str]", contribution["configured_to_template"])
    config = cast("dict[str, list[dict[str, JsonValue]]]", selector["config"])
    assert sorted(str(x["feature"]) for x in config["features"]) == sorted(links)
    assert len(links) == 22
    assert len(set(links.values())) == 11
    registry = Path("evidence/item-8/runtime/registry-r1/dumps/registry/minecraft")
    configured = read_registry(registry / "worldgen_configured_feature.txt")
    assert set(links) | {str(contribution["configured_feature"])} <= set(configured)
    assert contribution["placed_feature"] in read_registry(registry / "worldgen_placed_feature.txt")
    assert not any(r.startswith("yungsbridges:") for r in read_registry(
        registry / "worldgen_structure.txt"
    ))
    for rid, template in links.items():
        definition = resources[prefix + "configured_feature/" + rid.split(":")[1] + ".json"]
        assert definition["type"] == "yungsbridges:bridge"
        assert cast("dict[str, JsonValue]", definition["config"])["location"] == template


def test_yungs_bridge_templates_keep_unreferenced_layouts_separate() -> None:
    decisions = cast("dict[str, JsonValue]", json.loads(
        Path("evidence/item-8/family-decisions.json").read_bytes()
    ))
    non_registry = cast("dict[str, JsonValue]", decisions["non_registry_content"])
    contributions = cast("dict[str, dict[str, JsonValue]]", non_registry["contributions"])
    bridge = contributions["yungsbridges:bridges"]
    content = cast("dict[str, JsonValue]", bridge["template_content"])
    links = cast("dict[str, str]", bridge["configured_to_template"])
    catalog = cast("dict[str, list[dict[str, JsonValue]]]", json.loads(gzip.decompress(Path(
        "evidence/item-8/sources/templates-redacted.json.gz"
    ).read_bytes())))
    templates = {
        str(r["path"]).replace(
            "data/yungsbridges/structure/", "yungsbridges:"
        ).removesuffix(".nbt"):
        cast("dict[str, JsonValue]", r["document"])
        for r in catalog["resources"] if r["archive"] == "YungsBridges-1.21.1-NeoForge-5.1.1.jar"
    }
    assert len(templates) == 14
    assert content["referenced_nominal_xyz_blocks"] == {
        template: templates[template]["size"] for template in sorted(set(links.values()))
    }
    assert content["unreferenced_packaged_templates"] == sorted(
        set(templates) - set(links.values())
    )
    assert len(cast("list[str]", content["unreferenced_packaged_templates"])) == 3
    for document in templates.values():
        assert document["entities"] == content["authored_entity_ids"] == []
        assert document["block_entities"] == content["block_entities"] == []


def test_yungs_bridge_generation_binds_anchor_rotation_and_processor_order() -> None:
    decisions = cast("dict[str, JsonValue]", json.loads(
        Path("evidence/item-8/family-decisions.json").read_bytes()
    ))
    content = cast("dict[str, JsonValue]", decisions["non_registry_content"])
    contributions = cast("dict[str, dict[str, JsonValue]]", content["contributions"])
    generation = cast("dict[str, JsonValue]", contributions["yungsbridges:bridges"]["generation"])
    base = Path("evidence/item-8/sources/yungs-bridge-generation")
    rows = cast("list[dict[str, str]]", json.loads((base / "identities.json").read_bytes()))
    sources: dict[str, str] = {}
    for row in rows:
        raw = (base / row["disassembly"]).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == row["disassembly_sha256"]
        sources[row["class"].split("/")[-1].removesuffix(".class")] = raw.decode()
    bridge = sources["BridgeFeature"]
    assert bridge.index("WorldGenLevel.getSeaLevel:") < bridge.index("createTemplateWithPlacement:")
    assert "Rotation.COUNTERCLOCKWISE_90" in bridge
    order = [line.split("FeatureProcessorModule.")[1].split(":")[0]
             for line in bridge.splitlines()
             if "// Field " in line and "FeatureProcessorModule." in line]
    assert order == generation["processor_order"]
    assert len(order) == 12
    template = sources["AbstractTemplateFeature"]
    assert template.index("StructureTemplate.placeInWorld:") < template.index("List.forEach:")
    following = template.split("StructureTemplate.placeInWorld:")[1].splitlines()[1]
    assert following.strip().endswith("pop")
    selector = sources["MultipleAttemptSingleRandomFeature"]
    assert selector.index("PlacedFeature.place:") < selector.index("List.remove:")
    assert "RandomSource.nextInt:" in selector


def test_yungs_bridge_supports_stop_at_zero_or_non_air_non_liquid() -> None:
    base = Path("evidence/item-8/sources/yungs-bridge-processors")
    rows = cast("list[dict[str, str]]", json.loads((base / "identities.json").read_bytes()))
    sources: dict[str, str] = {}
    for row in rows:
        raw = (base / row["disassembly"]).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == row["disassembly_sha256"]
        sources[row["class"].split("/")[-1].removesuffix(".class")] = raw.decode()
    assert "generatePillarDown:" in sources["DynamicLegProcessor"]
    helper = sources["ITemplateFeatureProcessor"]
    pillar = helper.split("public default void generatePillarDown(")[1].split(
        "public default net.minecraft.world.level.block.state.BlockState"
    )[0]
    assert "42: ifle          103" in pillar
    assert "BlockState.isAir:" in pillar
    assert "BlockState.liquid:" in pillar
    assert "Direction.DOWN:" in pillar
    assert "getMinBuildHeight" not in pillar
    assert "BlockPos.below:" in pillar
    assert pillar.count("WorldGenLevel.setBlock:") == 2


def test_yungs_bridge_processors_have_no_direct_encounter_or_loot_calls() -> None:
    base = Path("evidence/item-8/sources/yungs-bridge-processors")
    manifest = (base / "identities.json").read_bytes()
    assert hashlib.sha256(manifest).hexdigest() == (
        "97da8471a115645afe18fee88f98407410097d244ed1d43d2a25ae4a6ad0bfaf"
    )
    rows = cast("list[dict[str, str]]", json.loads(manifest))
    assert len(rows) == 14
    for row in rows:
        raw = (base / row["disassembly"]).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == row["disassembly_sha256"]
        source = raw.decode()
        # A scoped direct-reference check, not proof about delegated or external code.
        for token in (
            "world/entity/", "addFreshEntity", "setLootTable", "LootTable",
            "BaseSpawner", "SpawnerBlockEntity", "Blocks.SPAWNER:",
            "Blocks.TRIAL_SPAWNER:", "Blocks.CHEST:", "Blocks.BARREL:",
        ):
            assert token not in source, (row["class"], token)


def test_yungs_bridge_placement_checks_liquid_and_both_banks() -> None:
    base = Path("evidence/item-8/sources/yungs-bridge-generation")
    manifest = (base / "identities.json").read_bytes()
    assert hashlib.sha256(manifest).hexdigest() == (
        "2e6f68933e8b02e097901bb8db1afb3d277be7204e31574d44e66445696552da"
    )
    rows = cast("list[dict[str, str]]", json.loads(manifest))
    row = next(row for row in rows if row["class"].endswith("/BridgePlacement.class"))
    raw = (base / row["disassembly"]).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == row["disassembly_sha256"]
    source = raw.decode().split("public java.util.stream.Stream")[1].split(
        "public net.minecraft.world.level.levelgen.placement.PlacementModifierType"
    )[0]
    assert "WorldGenLevel.getSeaLevel:" in source
    assert "15: iconst_1" in source
    assert "16: isub" in source
    assert source.count("BlockState.canOcclude:") == 4
    assert source.count("Heightmap$Types.WORLD_SURFACE:") == 4
    assert source.count("Field numSolidBlocksNeeded:I") == 2
    assert "BlockState.liquid:" in source
    assert "FluidTags.WATER" not in source
    assert "Blocks.WATER" not in source
    assert "Stream.empty:" in source
    assert "875: areturn" in source
