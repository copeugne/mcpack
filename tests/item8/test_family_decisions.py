from __future__ import annotations

import gzip
import hashlib
import json
from pathlib import Path
from typing import TYPE_CHECKING, cast

import pytest
from tools.build_item8_inventory import assemble

from mcpack_evidence.item8_inventory import resource_identity, size_variant_groups
from mcpack_evidence.item8_registry import read_registry
from mcpack_evidence.item8_resource_selection import runtime_mod_ids

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_better_village_contributes_templates_without_an_extra_family() -> None:
    root = Path(__file__).resolve().parents[2]
    decisions = cast("dict[str, list[dict[str, JsonValue]]]", json.loads(
        (root / "evidence/item-8/family-decisions.json").read_bytes()
    ))
    village = next(row for row in decisions["groups"] if row["family_id"] == "minecraft:village")
    documents: dict[str, bytes] = {}
    for path, digest in cast("dict[str, str]", village["evidence"]).items():
        payload = (root / path).read_bytes()
        assert hashlib.sha256(payload).hexdigest() == digest
        documents[path] = payload
    traces = cast("dict[str, JsonValue]", json.loads(gzip.decompress(documents[
        "evidence/item-8/sources/pool-traces-content.json.gz"
    ])))
    templates = cast("dict[str, list[dict[str, JsonValue]]]", json.loads(gzip.decompress(documents[
        "evidence/item-8/sources/templates-redacted.json.gz"
    ])))
    structures = cast("dict[str, dict[str, JsonValue]]", traces["structures"])
    contents = cast("dict[str, dict[str, JsonValue]]", traces["template_contents"])
    archive = "bettervillage-neoforge-1.21.1-3.3.1.jar"
    packaged = {
        identity[0]: row["sha256"]
        for row in templates["resources"] if row["archive"] == archive
        if (identity := resource_identity(str(row["path"]), "structure", ".nbt")) is not None
    }
    assert len(packaged) == 246
    reached: set[str] = set()
    counts = {"desert": 44, "plains": 55, "savanna": 54, "snowy": 47, "taiga": 44}
    for biome, count in counts.items():
        identifier = f"minecraft:village_{biome}"
        assert identifier in cast("list[str]", village["structure_ids"])
        contributed = set(cast("list[str]", structures[identifier]["templates"])) & packaged.keys()
        assert len(contributed) == count
        reached.update(contributed)
        for template in contributed:
            source = cast("dict[str, JsonValue]", contents[template]["source"])
            assert source["archive"] == archive
            assert source["sha256"] == packaged[template]
    assert len(reached) == 244
    assert set(packaged) - reached == {
        "minecraft:village/snowy/streets/crossroad_01",
        "minecraft:village/snowy/streets/straight_05",
    }
    assert not any(
        str(row["family_id"]).startswith("bettervillage:") for row in decisions["groups"]
    )
    catalog = cast("dict[str, list[dict[str, JsonValue]]]", json.loads(gzip.decompress(documents[
        "evidence/item-8/sources/packaged-json-redacted.json.gz"
    ])))
    compat = [cast("dict[str, JsonValue]", row["document"]) for row in catalog["resources"]
              if "/bettervillage_compat/" in str(row["path"])]
    log = documents["evidence/raw/item8/registry-r1/debug.log"].decode()
    mods = runtime_mod_ids(log)
    assert {str(row["mod_id"]) for row in compat} == {
        "bountiful", "iceandfire", "immersiveengineering", "morevillagers"
    }
    assert all(row["enabled"] is False and str(row["mod_id"]) not in mods for row in compat)
    assert "StructureSet modified for minecraft:village" in log.splitlines()[18028]
    config = documents["evidence/item-6/frozen/config/bettervillage_1.properties"].decode()
    assert {line for line in config.splitlines() if not line.startswith("#")} == {
        "boolean.villages.enabled_custom_config=true", "int.villages.salt=10387312",
        "int.villages.separation=20", "int.villages.spacing=45",
    }


@pytest.mark.parametrize(
    "namespace",
    [
        "integrated_villages:",
        "dungeons_arise:",
        "explorations:",
        "explorify:",
        "betterdeserttemples:",
        "betterdungeons:",
        "betterfortresses:",
        "betterjungletemples:",
        "betteroceanmonuments:",
        "betterstrongholds:",
        "betterwitchhuts:",
        "mes:",
        "mss:",
        "mns:",
        "mvs:",
        "aether:",
        "deep_aether:",
        "betterend:",
    ],
)
def test_authored_designs_bind_roots_settings_and_missing_components(
    namespace: str,
) -> None:
    root = Path(__file__).resolve().parents[2]
    decisions = cast(
        "dict[str, JsonValue]",
        json.loads((root / "evidence/item-8/family-decisions.json").read_bytes()),
    )
    groups = [
        row
        for row in cast("list[dict[str, JsonValue]]", decisions["groups"])
        if str(row["family_id"]).startswith(namespace)
        and len(cast("list[str]", row["structure_ids"])) == 1
    ]
    registry = read_registry(
        root / "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
    )
    members = [member for row in groups for member in cast("list[str]", row["structure_ids"])]
    assert len(members) == len(set(members))
    expected = {key for key in registry if key.startswith(namespace)}
    # Variant groups have separate coverage tests.
    excluded_prefixes = {
        "explorify:": ("explorify:supply_cache/", "explorify:watchtower/", "explorify:guide_post_"),
        "mes:": ("mes:mega_ship",),
        "mss:": ("mss:tree_", "mss:birch_river", "mss:cherry_river"),
    }.get(namespace, ())
    expected = {key for key in expected if not key.startswith(excluded_prefixes)}
    if namespace in {"mns:", "mvs:"}:
        variants = [
            member
            for row in cast("list[dict[str, JsonValue]]", decisions["groups"])
            if str(row["family_id"]).startswith(namespace)
            and len(cast("list[str]", row["structure_ids"])) > 1
            for member in cast("list[str]", row["structure_ids"])
        ]
        assert (
            len(members + variants)
            == len(set(members + variants))
            == {"mns:": 52, "mvs:": 129}[namespace]
        )
        expected -= set(variants)
    assert members
    assert set(members) == expected
    catalog = cast(
        "dict[str, JsonValue]",
        json.loads(
            gzip.decompress(
                (root / "evidence/item-8/sources/packaged-json-redacted.json.gz").read_bytes()
            )
        ),
    )
    definitions: dict[str, dict[str, JsonValue]] = {}
    for resource in cast("list[dict[str, JsonValue]]", catalog["resources"]):
        identity = resource_identity(str(resource["path"]), "worldgen/structure")
        if identity is not None and identity[0] in members:
            assert identity[1] == ""
            assert identity[0] not in definitions
            definitions[identity[0]] = cast("dict[str, JsonValue]", resource["document"])
    assert set(definitions) == set(members)
    traces = cast(
        "dict[str, JsonValue]",
        json.loads(
            gzip.decompress(
                (root / "evidence/item-8/sources/pool-traces-content.json.gz").read_bytes()
            )
        ),
    )
    structures = cast("dict[str, dict[str, JsonValue]]", traces["structures"])
    if namespace in ("dungeons_arise:", "mes:", "mss:"):
        seen: set[str] = set()
        for identifier in sorted(expected):
            templates = set(cast("list[str]", structures[identifier]["templates"]))
            assert templates
            assert not seen.intersection(templates)
            seen.update(templates)
    direct = [row for row in groups if row["start_pool"] is not None]
    assert len({str(row["start_pool"]) for row in direct}) == len(direct)
    for row in groups:
        identifier = str(row["family_id"])
        assert row["structure_ids"] == [identifier]
        definition = definitions[identifier]
        custom_keys = {
            "mes:": {"allowed_terrain_height_range", "terrain_height_radius_check", "y_allowance"},
            "mns:": set(definition)
            - {
                "type",
                "start_height",
                "project_start_to_heightmap",
                "required_mods",
                "target_biomes",
                "target_biome_radius_check_blocks",
                "cannot_spawn_in_liquid",
                "start_pool",
                "biomes",
            },
        }
        custom_keys["mvs:"] = custom_keys["aether:"] = custom_keys["deep_aether:"] = custom_keys[
            "betterend:"
        ] = custom_keys["mns:"]
        if namespace in custom_keys:
            assert row["custom_generation_settings"] == {
                key: definition[key] for key in custom_keys[namespace] if key in definition
            }
        assert row["start_pool"] == definition.get("start_pool")
        if "start_pool" in definition:
            assert row["start_pool"] == structures[identifier]["start_pool"]
            assert row["missing_components"] == structures[identifier]["missing"]
        else:
            assert identifier in cast("dict[str, JsonValue]", traces["untraced_structures"])
            assert (
                row["missing_components"]
                == "UNKNOWN: custom generation is outside current pool trace"
            )
        assert row["generation_settings"] == {
            key: definition[key]
            for key in (
                "type",
                "start_height",
                "project_start_to_heightmap",
                "required_mods",
                "target_biomes",
                "target_biome_radius_check_blocks",
                "cannot_spawn_in_liquid",
            )
            if key in definition
        }
        for path, digest in cast("dict[str, str]", row["evidence"]).items():
            assert hashlib.sha256((root / path).read_bytes()).hexdigest() == digest


def test_explorify_variants_bind_definitions_templates_and_complete_namespace() -> None:
    root = Path(__file__).resolve().parents[2]
    decisions = cast(
        "dict[str, JsonValue]",
        json.loads((root / "evidence/item-8/family-decisions.json").read_bytes()),
    )
    groups = {
        str(row["family_id"]): row
        for row in cast("list[dict[str, JsonValue]]", decisions["groups"])
        if str(row["family_id"]).startswith("explorify:")
    }
    registry = read_registry(
        root / "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
    )
    members = [
        member for row in groups.values() for member in cast("list[str]", row["structure_ids"])
    ]
    assert len(members) == len(set(members)) == 23
    assert set(members) == {key for key in registry if key.startswith("explorify:")}
    catalog = cast(
        "dict[str, JsonValue]",
        json.loads(
            gzip.decompress(
                (root / "evidence/item-8/sources/packaged-json-redacted.json.gz").read_bytes()
            )
        ),
    )
    definitions: dict[str, dict[str, JsonValue]] = {}
    for resource in cast("list[dict[str, JsonValue]]", catalog["resources"]):
        identity = resource_identity(str(resource["path"]), "worldgen/structure")
        if identity is not None and identity[0] in members:
            assert identity[1] == ""
            assert identity[0] not in definitions
            definitions[identity[0]] = cast("dict[str, JsonValue]", resource["document"])
    traces = cast(
        "dict[str, JsonValue]",
        json.loads(
            gzip.decompress(
                (root / "evidence/item-8/sources/pool-traces-content.json.gz").read_bytes()
            )
        ),
    )
    structures = cast("dict[str, dict[str, JsonValue]]", traces["structures"])
    contents = cast("dict[str, dict[str, JsonValue]]", traces["template_contents"])
    variants = {
        "guide_post": (["guide_post_cold", "guide_post_warm"], [11, 25, 11], "whole"),
        "supply_cache": (
            [
                "supply_cache/" + key
                for key in ("birch", "dark", "desert", "forest", "jungle", "mangrove", "taiga")
            ],
            [3, 4, 4],
            "01",
        ),
        "watchtower": (
            ["watchtower/" + key for key in ("plains", "savanna", "taiga")],
            [9, 25, 9],
            "main",
        ),
    }
    for family, (names, size, suffix) in variants.items():
        group = groups["explorify:" + family]
        assert group["structure_ids"] == ["explorify:" + name for name in names]
        for member in cast("list[str]", group["structure_ids"]):
            definition = definitions[member]
            assert group["common_generation_definition"] == {
                key: value
                for key, value in definition.items()
                if key not in ("biomes", "start_pool")
            }
            trace = structures[member]
            assert (
                cast("dict[str, JsonValue]", group["start_pools"])[member]
                == definition["start_pool"]
                == trace["start_pool"]
            )
            assert (
                cast("dict[str, JsonValue]", group["missing_components"])[member]
                == trace["missing"]
                == []
            )
            assert trace["templates"] == [str(definition["start_pool"]) + "/" + suffix]
            content = contents[cast("list[str]", trace["templates"])[0]]
            assert content["template_size_xyz"] == size
            assert content["authored_entities"] == content["spawner_blocks"] == []
            loot = [
                row["value"]
                for row in cast("list[dict[str, JsonValue]]", content["loot_references"])
            ]
            if family == "guide_post":
                assert loot == []
            elif family == "supply_cache":
                assert loot == ["explorify:chest/supply_cache"] * 2
            else:
                biome = member.rsplit("/", 1)[1]
                assert loot == [f"minecraft:chests/village/village_{biome}_house"]
        for path, digest in cast("dict[str, str]", group["evidence"]).items():
            assert hashlib.sha256((root / path).read_bytes()).hexdigest() == digest


def test_mega_ship_variants_preserve_definitions_modules_and_mes_coverage() -> None:
    root = Path(__file__).resolve().parents[2]
    decisions = cast(
        "dict[str, JsonValue]",
        json.loads((root / "evidence/item-8/family-decisions.json").read_bytes()),
    )
    groups = [
        row
        for row in cast("list[dict[str, JsonValue]]", decisions["groups"])
        if str(row["family_id"]).startswith("mes:")
    ]
    members = [member for row in groups for member in cast("list[str]", row["structure_ids"])]
    registry = read_registry(
        root / "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
    )
    assert len(members) == len(set(members)) == 25
    assert set(members) == {key for key in registry if key.startswith("mes:")}
    group = next(row for row in groups if row["family_id"] == "mes:mega_ship")
    variants = cast("dict[str, dict[str, JsonValue]]", group["variants"])
    assert group["structure_ids"] == sorted(variants)
    assert set(variants) == {key for key in registry if key.startswith("mes:mega_ship")}
    for path, digest in cast("dict[str, str]", group["evidence"]).items():
        assert hashlib.sha256((root / path).read_bytes()).hexdigest() == digest
    catalog = cast(
        "dict[str, JsonValue]",
        json.loads(
            gzip.decompress(
                (root / "evidence/item-8/sources/packaged-json-redacted.json.gz").read_bytes()
            )
        ),
    )
    resources = cast("list[dict[str, JsonValue]]", catalog["resources"])
    traces = cast(
        "dict[str, JsonValue]",
        json.loads(
            gzip.decompress(
                (root / "evidence/item-8/sources/pool-traces-content.json.gz").read_bytes()
            )
        ),
    )
    structures = cast("dict[str, dict[str, JsonValue]]", traces["structures"])
    contents = cast("dict[str, dict[str, JsonValue]]", traces["template_contents"])
    for identifier, variant in variants.items():
        name = identifier.split(":")[1]
        definitions = [
            row["document"]
            for row in resources
            if row["path"] == f"data/mes/worldgen/structure/{name}.json"
        ]
        assert definitions == [variant["definition"]]
        definition = cast("dict[str, JsonValue]", variant["definition"])
        trace = structures[identifier]
        assert trace["start_pool"] == definition["start_pool"]
        assert variant["missing_components"] == trace["missing"] == []
        for suffix, size in (("", [48, 48, 48]), ("_middle", [48, 48, 48]), ("_end", [35, 20, 23])):
            template = f"mes:mega_ship/{name}{suffix}"
            assert template in cast("list[str]", trace["templates"])
            assert contents[template]["template_size_xyz"] == size
        if name.startswith("mega_ship_crashed"):
            assert variant["placement_form"] == "wreck"
            assert definition["start_height"] == {"absolute": 0}
            assert definition["terrain_adaptation"] == "beard_thin"
        else:
            assert variant["placement_form"] == "airborne"
            height = cast("dict[str, JsonValue]", definition["start_height"])
            assert height["min_inclusive"] == {"absolute": 30}
            assert definition["terrain_adaptation"] == "none"


@pytest.mark.parametrize(
    ("family", "suffix", "member_count", "template_count"),
    [("mvs:living_tree", "_tree", 9, 15), ("mvs:well", "well", 17, 20)],
)
def test_voyager_trees_and_wells_preserve_definitions_and_template_content(
    family: str, suffix: str, member_count: int, template_count: int
) -> None:
    root = Path(__file__).resolve().parents[2]
    decisions = cast(
        "dict[str, list[dict[str, JsonValue]]]",
        json.loads((root / "evidence/item-8/family-decisions.json").read_bytes()),
    )
    group = next(row for row in decisions["groups"] if row["family_id"] == family)
    for path, digest in cast("dict[str, str]", group["evidence"]).items():
        assert hashlib.sha256((root / path).read_bytes()).hexdigest() == digest
    catalog = cast(
        "dict[str, list[dict[str, JsonValue]]]",
        json.loads(
            gzip.decompress(
                (root / "evidence/item-8/sources/packaged-json-redacted.json.gz").read_bytes()
            )
        ),
    )
    traces = cast(
        "dict[str, dict[str, dict[str, JsonValue]]]",
        json.loads(
            gzip.decompress(
                (root / "evidence/item-8/sources/pool-traces-content.json.gz").read_bytes()
            )
        ),
    )
    registry = read_registry(
        root / "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
    )
    expected = sorted(
        key
        for key in registry
        if key.startswith("mvs:") and key.endswith(suffix) and "dead_tree" not in key
    )
    variants = cast("dict[str, dict[str, JsonValue]]", group["variants"])
    assert group["structure_ids"] == sorted(variants) == expected
    assert len(variants) == member_count
    sizes: list[list[int]] = []
    excluded = {
        "biomes",
        "start_pool",
        "allowed_terrain_height_range",
        "terrain_height_radius_check",
    }
    if family == "mvs:well":
        excluded.update({"type", "land_search_direction"})
    loot_by_template: dict[str, list[JsonValue]] = {
        "mvs:nature/big_oak_tree": [
            {"path": "/block_entities/0/nbt/LootTable", "value": "mvs:general"}
        ],
        "mvs:well/well_lower": [
            {"path": "/block_entities/0/nbt/LootTable", "value": "mvs:houses_uncommon"}
        ],
        "mvs:well/rare_well/rare_well_lower": [
            {"path": "/block_entities/1/nbt/LootTable", "value": "mvs:houses_rare"}
        ],
        "mvs:1_21_4/small_tower_well": [
            {"path": "/block_entities/3/nbt/LootTable", "value": "mvs:empty"}
        ],
    }
    for identifier, variant in variants.items():
        name = identifier.split(":")[1]
        definitions = [
            cast("dict[str, JsonValue]", row["document"])
            for row in catalog["resources"]
            if row["path"] == f"data/mvs/worldgen/structure/{name}.json"
        ]
        assert definitions == [variant["definition"]]
        definition = definitions[0]
        assert group["common_generation_definition"] == {
            k: v for k, v in definition.items() if k not in excluded
        }
        assert (
            definition.get("allowed_terrain_height_range"),
            definition.get("terrain_height_radius_check"),
        ) == {"big_oak_tree": (4, 2), "rare_well": (3, 2)}.get(name, (None, None))
        assert definition.get("land_search_direction") == (
            "HIGHEST_LAND" if name == "nether_well" else None
        )
        assert definition["type"] == (
            "moogs_structures:moogs_structures_generic_nether_jigsaw_structure"
            if name == "nether_well"
            else "moogs_structures:moogs_structures_generic_jigsaw_structure"
        )
        trace = traces["structures"][identifier]
        templates = cast("dict[str, list[int]]", variant["templates"])
        assert trace["templates"] == sorted(templates)
        assert trace["missing"] == trace["unresolved_elements"] == []
        for template, dimensions in templates.items():
            content = traces["template_contents"][template]
            assert content["template_size_xyz"] == dimensions
            sizes.append(dimensions)
            assert content["authored_entities"] == content["unresolved_entities"] == []
            assert content["spawner_blocks"] == content["generation_markers"] == []
            assert content["loot_references"] == loot_by_template.get(template, [])
    assert len(sizes) == template_count
    if family == "mvs:well":
        return
    attrs = cast("dict[str, dict[str, JsonValue]]", group["attributes"])
    assert attrs["approximate_footprint"]["packaged_template_xz_blocks"] == [
        list(pair) for pair in sorted({(s[0], s[2]) for s in sizes})
    ]
    assert attrs["approximate_vertical_size"]["packaged_template_y_blocks"] == sorted(
        {s[1] for s in sizes}
    )


def test_voyager_carts_and_igloos_preserve_authored_content_and_shared_pieces() -> None:
    root = Path(__file__).resolve().parents[2]
    decisions = cast(
        "dict[str, list[dict[str, JsonValue]]]",
        json.loads((root / "evidence/item-8/family-decisions.json").read_bytes()),
    )
    catalog = cast(
        "dict[str, list[dict[str, JsonValue]]]",
        json.loads(
            gzip.decompress(
                (root / "evidence/item-8/sources/packaged-json-redacted.json.gz").read_bytes()
            )
        ),
    )
    traces = cast(
        "dict[str, dict[str, dict[str, JsonValue]]]",
        json.loads(
            gzip.decompress(
                (root / "evidence/item-8/sources/pool-traces-content.json.gz").read_bytes()
            )
        ),
    )
    registry = read_registry(
        root / "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
    )
    selected = {
        row["family_id"]: row
        for row in decisions["groups"]
        if row["family_id"] in {"mvs:cart", "mvs:igloo"}
    }
    all_templates: set[str] = set()
    for family, prefixes in {
        "mvs:cart": ("mvs:cart", "mvs:large_cart_", "mvs:medium_bamboo_cart"),
        "mvs:igloo": ("mvs:medium_igloo_", "mvs:small_igloo"),
    }.items():
        group = selected[family]
        variants = cast("dict[str, dict[str, JsonValue]]", group["variants"])
        expected = {
            key for key in registry if key.startswith(prefixes) and key != "mvs:cartographer_tower"
        }
        assert group["structure_ids"] == sorted(variants) == sorted(expected)
        for path, digest in cast("dict[str, str]", group["evidence"]).items():
            assert hashlib.sha256((root / path).read_bytes()).hexdigest() == digest
        for identifier, variant in variants.items():
            name = identifier.split(":")[1]
            assert [
                row["document"]
                for row in catalog["resources"]
                if row["path"] == f"data/mvs/worldgen/structure/{name}.json"
            ] == [variant["definition"]]
            templates = cast("dict[str, list[int]]", variant["templates"])
            trace = traces["structures"][identifier]
            assert trace["templates"] == sorted(templates)
            assert trace["missing"] == trace["unresolved_elements"] == []
            all_templates.update(templates)
            for template, dimensions in templates.items():
                assert traces["template_contents"][template]["template_size_xyz"] == dimensions
    assert len(all_templates) == 10
    authored = {
        "mvs:carts/cart": "minecraft:wandering_trader",
        "mvs:carts/medium_bamboo_cart": "minecraft:wandering_trader",
        **{
            f"minecraft:village/snowy/villagers/{kind}": "minecraft:villager"
            for kind in ("baby", "nitwit", "unemployed")
        },
    }
    loot = {
        "mvs:carts/cart": [(2, "mvs:cart")],
        "mvs:carts/large_cart_1": [(i, "mvs:large_carts") for i in range(1, 6)],
        "mvs:carts/large_cart_2": [(i, "mvs:large_carts") for i in range(1, 5)],
        "mvs:houses/medium_igloo_1": [(i, "mvs:houses_common") for i in (0, 3, 9)],
        "mvs:houses/small_igloo": [(i, "mvs:houses_uncommon") for i in (9, 11)],
    }
    for template in all_templates:
        content = traces["template_contents"][template]
        assert content["authored_entities"] == (
            [{"id": authored[template], "path": "/entities/0/nbt"}] if template in authored else []
        )
        assert content["unresolved_entities"] == []
        assert content["loot_references"] == [
            {"path": f"/block_entities/{i}/nbt/LootTable", "value": value}
            for i, value in loot.get(template, [])
        ]
        markers = cast("list[dict[str, JsonValue]]", content["generation_markers"])
        assert len(markers) == int(template.startswith("mvs:carts/"))
        for marker in markers:
            nbt = cast("dict[str, JsonValue]", marker["nbt"])
            assert (nbt["id"], nbt["mode"], nbt["metadata"]) == (
                "minecraft:structure_block",
                "SAVE",
                "",
            )
        spawners = cast("list[dict[str, JsonValue]]", content["spawner_blocks"])
        assert len(spawners) == int(template == "mvs:houses/small_igloo_lower")
        for spawner in spawners:
            nbt = cast("dict[str, JsonValue]", spawner["nbt"])
            assert nbt["SpawnData"] == {"entity": {"id": "minecraft:stray"}}
            assert nbt["SpawnPotentials"] == []


@pytest.mark.parametrize("namespace", ["repurposed_structures", "minecraft"])
def test_design_groups_cover_registry_and_bind_variant_definitions(namespace: str) -> None:
    root = Path(__file__).resolve().parents[2]
    decisions = cast(
        "dict[str, list[dict[str, JsonValue]]]",
        json.loads((root / "evidence/item-8/family-decisions.json").read_bytes()),
    )
    catalog = cast(
        "dict[str, list[dict[str, JsonValue]]]",
        json.loads(
            gzip.decompress(
                (root / "evidence/item-8/sources/packaged-json-redacted.json.gz").read_bytes()
            )
        ),
    )
    traces = cast(
        "dict[str, dict[str, dict[str, JsonValue]]]",
        json.loads(
            gzip.decompress(
                (root / "evidence/item-8/sources/pool-traces-content.json.gz").read_bytes()
            )
        ),
    )
    groups = [
        row for row in decisions["groups"] if str(row["family_id"]).startswith(namespace + ":")
    ]
    registry = {
        key
        for key in read_registry(
            root
            / "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
        )
        if key.startswith(namespace + ":")
    }
    members = [key for row in groups for key in cast("list[str]", row["structure_ids"])]
    assert (
        len(members)
        == len(set(members))
        == {"repurposed_structures": 107, "minecraft": 34}[namespace]
    )
    assert set(members) == registry
    counts = {
        "ancient_city": 3,
        "bastion": 1,
        "city": 2,
        "fortress": 1,
        "igloo": 4,
        "mansion": 8,
        "mineshaft": 16,
        "monument": 4,
        "outpost": 18,
        "pyramid": 11,
        "ruined_portal": 1,
        "ruins": 5,
        "shipwreck": 4,
        "stronghold": 2,
        "temple": 7,
        "village": 14,
        "witch_hut": 6,
    }
    if namespace == "minecraft":
        counts = {
            "ancient_city": 1,
            "bastion_remnant": 1,
            "buried_treasure": 1,
            "desert_pyramid": 1,
            "end_city": 1,
            "fortress": 1,
            "igloo": 1,
            "jungle_pyramid": 1,
            "mansion": 1,
            "mineshaft": 2,
            "monument": 1,
            "nether_fossil": 1,
            "ocean_ruin": 2,
            "pillager_outpost": 1,
            "ruined_portal": 7,
            "shipwreck": 2,
            "stronghold": 1,
            "swamp_hut": 1,
            "trail_ruins": 1,
            "trial_chambers": 1,
            "village": 5,
        }
    assert {str(row["family_id"]).split(":")[1] for row in groups} == set(counts)
    custom: set[str] = set()
    for row in groups:
        family = str(row["family_id"])
        kind = family.split(":")[1]
        variants = cast("dict[str, dict[str, JsonValue]]", row["variants"])
        assert (
            row["structure_ids"]
            == sorted(variants)
            == sorted(key for key in registry if key == family or key.startswith(family + "_"))
        )
        assert len(variants) == counts[kind]
        for path, digest in cast("dict[str, str]", row["evidence"]).items():
            assert hashlib.sha256((root / path).read_bytes()).hexdigest() == digest
        if kind == "witch_hut":
            continue  # Covered by the common-definition/template variant check.
        for identifier, variant in variants.items():
            name = identifier.split(":")[1]
            definitions = [
                cast("dict[str, JsonValue]", r["document"])
                for r in catalog["resources"]
                if r["path"] == f"data/{namespace}/worldgen/structure/{name}.json"
            ]
            assert definitions == [variant["definition"]]
            definition = definitions[0]
            if "start_pool" in definition:
                trace = traces["structures"][identifier]
                assert trace["start_pool"] == definition["start_pool"]
                assert variant["missing_components"] == trace["missing"]
                assert not trace["missing"] or namespace == "minecraft"
                assert trace["templates"]
                assert trace["unresolved_elements"] == []
            else:
                custom.add(identifier)
                if namespace == "repurposed_structures":
                    assert kind in {"mansion", "monument"}
                    assert definition["type"] == f"repurposed_structures:{kind}_structure"
                    assert definition[f"{kind}_type"] == name.removeprefix(kind + "_")
                assert traces["untraced_structures"][identifier]["type"] == definition["type"]
                assert identifier in traces["untraced_structures"]
                if identifier == "minecraft:end_city":
                    assert variant["missing_components"] == []
                    assert variant["vanilla_code_template_ids"]
                else:
                    assert (
                        variant["missing_components"]
                        == "UNKNOWN: custom generation is outside current pool trace"
                    )
    assert len(custom) == {"repurposed_structures": 12, "minecraft": 24}[namespace]


@pytest.mark.parametrize(
    ("namespace", "count"),
    [
        ("towns_and_towers", 60),
        ("idas", 84),
        ("adorabuild_structures", 106),
        ("terralith", 28),
        ("illagerinvasion", 5),
        ("creatingspace", 4),
        ("supplementaries", 2),
    ],
)
def test_provider_groups_bind_full_definitions_pools_and_registry(
    namespace: str,
    count: int,
) -> None:
    root = Path(__file__).resolve().parents[2]
    decisions = cast(
        "dict[str, list[dict[str, JsonValue]]]",
        json.loads((root / "evidence/item-8/family-decisions.json").read_bytes()),
    )
    catalog = cast(
        "dict[str, list[dict[str, JsonValue]]]",
        json.loads(
            gzip.decompress(
                (root / "evidence/item-8/sources/packaged-json-redacted.json.gz").read_bytes()
            )
        ),
    )
    traces = cast(
        "dict[str, dict[str, dict[str, JsonValue]]]",
        json.loads(
            gzip.decompress(
                (root / "evidence/item-8/sources/pool-traces-content.json.gz").read_bytes()
            )
        ),
    )
    groups = [r for r in decisions["groups"] if str(r["family_id"]).startswith(namespace + ":")]
    registry = {
        k
        for k in read_registry(
            root
            / "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
        )
        if k.startswith(namespace + ":")
    }
    members = [k for r in groups for k in cast("list[str]", r["structure_ids"])]
    assert len(members) == len(set(members)) == count
    assert set(members) == registry
    expected = {
        "outpost_fort": ("kaisyn:outpost/forts/", 9),
        "outpost_tower": ("kaisyn:outpost/towers/", 16),
        "outpost_camp": ("kaisyn:outpost/camps/", 5),
        "village": ("kaisyn:village/", 26),
        "ocean_outpost": ("kaisyn:ships/pillager_outpost_ocean/", 1),
        "ocean_village": ("kaisyn:ships/village_ocean/", 1),
        "ocean_wreckage": ("kaisyn:ships/wreckage_ocean/", 1),
        "desert_mimic": ("kaisyn:other/desert_temple_mimic/", 1),
    }
    if namespace == "idas":
        expected = {
            "ancient_portal": ("idas:ancient_portal/", 2),
            "ancient_statue": ("idas:ancient_statue/", 3),
            "animal_den": ("idas:animal_den/", 3),
            "desert_camp": ("idas:desert_camp/", 4),
            "desert_market": ("idas:desert_market/", 3),
            "dig_site": ("idas:dig_site/", 2),
            "lumber_camp": ("idas:lumber_camp/", 10),
            "sunken_ship": ("idas:sunken_ship/", 2),
            "underground_camp": ("idas:underground_camp/", 2),
        }
        singletons = {
            k.split(":")[1]: ("idas:", 1)
            for k in registry
            if k.split(":")[1].split("/")[0] not in expected
        }
        expected.update(singletons)
        expected["sunken_ship/sunken_ship_ruins"] = ("idas:sunken_ship/", 1)
        assert len(expected) == 62
    if namespace == "adorabuild_structures":
        counts = {
            "acacia_well": 1,
            "ancient_palace": 3,
            "bamboo_campfire": 1,
            "basalt_chambers": 1,
            "birch_beehive": 1,
            "blackstone_bastion": 4,
            "blackstone_temple": 1,
            "buried_sand_castle": 2,
            "dark_oak_mansion": 1,
            "end_bubble": 3,
            "end_gateway": 2,
            "end_ship": 1,
            "end_temple": 2,
            "frozen_shelter": 3,
            "house": 45,
            "library": 2,
            "mountain_mine": 2,
            "mushroom": 1,
            "nether_fortress": 3,
            "nether_fossil": 1,
            "nether_portal": 1,
            "nether_temple": 1,
            "ocean_bubble": 1,
            "ocean_temple": 4,
            "prison": 2,
            "red_sand_temple": 2,
            "sand_castle": 1,
            "sand_pyramid": 1,
            "tree": 3,
            "tree_house": 3,
            "watercraft": 7,
        }
        expected = {key: ("adorabuild_structures:", size) for key, size in counts.items()}
    if namespace == "terralith":
        expected = {
            "desert_outpost": ("terralith:regular/desert_outpost", 1),
            "fortified_village": ("terralith:village/", 2),
            "glacial_hut": ("terralith:ruin/glacial/hut", 1),
            "igloo": ("terralith:regular/igloo", 1),
            "mage_complex": ("terralith:mage/complex_start", 1),
            "mage_tower": ("terralith:mage/", 5),
            "rubble": ("terralith:rubble/", 6),
            "spire": ("terralith:spire/layer2", 1),
            "underground/frosted_dungeon": ("terralith:underground/frosted_dungeon", 1),
            "underground/giant_bee_hive": ("terralith:underground/giant_bee_hive", 1),
            "underground/mining_outpost": ("terralith:underground/mining_outpost", 1),
            "underground/old_refinery": ("terralith:underground/old_refinery", 1),
            "underground/sunken_tower": ("terralith:underground/sunken_tower", 1),
            "underground_cabin": ("terralith:underground/oak_cabin", 2),
            "valley_lodge": ("terralith:regular/valley_lodge", 1),
            "witch_hut": ("terralith:regular/witch_hut", 2),
        }
    if namespace == "illagerinvasion":
        expected = {
            "firecaller_hut": ("illagerinvasion:firecaller_hut/base_plates", 1),
            "illager_fort": ("illagerinvasion:illager_fort/illager_fort", 1),
            "illusioner_tower": ("illagerinvasion:illusioner_tower/illusioner_tower", 1),
            "labyrinth": ("illagerinvasion:labyrinth/towers", 1),
            "sorcerer_hut": ("illagerinvasion:sorcerer_hut/sorcerer_hut", 1),
        }
    if namespace == "creatingspace":
        expected = {
            "mars/underground_outpost_1": (
                "creatingspace:mars/underground_outpost_1/start_pool",
                1,
            ),
            "moon/abandoned_outpost": ("creatingspace:moon/abandoned_outpost/start_pool", 1),
            "moon/crashed_rocket": ("creatingspace:moon/crashed_rocket/start_pool", 1),
            "moon/crashed_ship": ("creatingspace:moon/crashed_ship/start_pool", 1),
        }
    if namespace == "supplementaries":
        expected = {
            "galleon": ("supplementaries:galleon/start_pool", 1),
            "road_sign": ("supplementaries:road_sign/start_pool", 1),
        }
    assert {str(r["family_id"]).split(":")[1] for r in groups} == set(expected)
    for group in groups:
        kind = str(group["family_id"]).split(":")[1]
        prefix, count = expected[kind]
        variants = cast("dict[str, dict[str, JsonValue]]", group["variants"])
        assert group["structure_ids"] == sorted(variants)
        assert len(variants) == count
        for path, digest in cast("dict[str, str]", group["evidence"]).items():
            assert hashlib.sha256((root / path).read_bytes()).hexdigest() == digest
        for identifier, variant in variants.items():
            name = identifier.split(":")[1]
            rows = [
                cast("dict[str, JsonValue]", r["document"])
                for r in catalog["resources"]
                if r["path"] == f"data/{namespace}/worldgen/structure/{name}.json"
            ]
            assert rows == [variant["definition"]]
            assert str(rows[0]["start_pool"]).startswith(prefix)
            trace = traces["structures"][identifier]
            assert trace["start_pool"] == rows[0]["start_pool"]
            assert trace["templates"]
            assert trace["unresolved_elements"] == []
            assert trace["missing"] == variant["missing_components"]
    assert {"id": "minecraft:emptY", "kind": "pool"} in cast(
        "list[JsonValue]",
        traces["structures"]["towns_and_towers:exclusives/pillager_outpost_nilotic"]["missing"],
    )


def test_illager_invasion_hostile_intent_binds_authored_component_entities() -> None:
    root = Path(__file__).resolve().parents[2]
    decisions = cast(
        "dict[str, list[dict[str, JsonValue]]]",
        json.loads((root / "evidence/item-8/family-decisions.json").read_bytes()),
    )
    traces = cast(
        "dict[str, dict[str, dict[str, JsonValue]]]",
        json.loads(
            gzip.decompress(
                (root / "evidence/item-8/sources/pool-traces-content.json.gz").read_bytes()
            )
        ),
    )
    groups = [r for r in decisions["groups"] if str(r["family_id"]).startswith("illagerinvasion:")]
    assert len(groups) == 5
    for group in groups:
        templates = cast("list[str]", traces["structures"][str(group["family_id"])]["templates"])
        entities = {
            str(entity["id"])
            for template in templates
            for entity in cast(
                "list[dict[str, JsonValue]]",
                traces["template_contents"][template]["authored_entities"],
            )
        }
        hostile = {
            entity
            for entity in entities
            if entity.startswith("illagerinvasion:")
            or entity in {"minecraft:evoker", "minecraft:vindicator", "minecraft:illusioner"}
        }
        assert hostile
        attributes = cast("dict[str, dict[str, JsonValue]]", group["attributes"])
        assert attributes["intended_hostility"]["authored_hostile_entity_ids"] == sorted(hostile)


def test_soaring_tree_variants_bind_common_definition_and_template_contents() -> None:
    root = Path(__file__).resolve().parents[2]
    decisions = cast(
        "dict[str, JsonValue]",
        json.loads((root / "evidence/item-8/family-decisions.json").read_bytes()),
    )
    group = next(
        row
        for row in cast("list[dict[str, JsonValue]]", decisions["groups"])
        if row["family_id"] == "mss:tree"
    )
    variants = cast("dict[str, dict[str, JsonValue]]", group["variants"])
    registry = read_registry(
        root / "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
    )
    assert group["structure_ids"] == sorted(variants)
    assert set(variants) == {key for key in registry if key.startswith("mss:tree_")}
    assert len(variants) == 8
    for path, digest in cast("dict[str, str]", group["evidence"]).items():
        assert hashlib.sha256((root / path).read_bytes()).hexdigest() == digest
    catalog = cast(
        "dict[str, JsonValue]",
        json.loads(
            gzip.decompress(
                (root / "evidence/item-8/sources/packaged-json-redacted.json.gz").read_bytes()
            )
        ),
    )
    resources = cast("list[dict[str, JsonValue]]", catalog["resources"])
    traces = cast(
        "dict[str, JsonValue]",
        json.loads(
            gzip.decompress(
                (root / "evidence/item-8/sources/pool-traces-content.json.gz").read_bytes()
            )
        ),
    )
    structures = cast("dict[str, dict[str, JsonValue]]", traces["structures"])
    contents = cast("dict[str, dict[str, JsonValue]]", traces["template_contents"])
    for identifier, variant in variants.items():
        name = identifier.split(":")[1]
        definitions = [
            cast("dict[str, JsonValue]", row["document"])
            for row in resources
            if row["path"] == f"data/mss/worldgen/structure/{name}.json"
        ]
        assert len(definitions) == 1
        assert group["common_generation_definition"] == {
            key: value for key, value in definitions[0].items() if key != "start_pool"
        }
        assert variant["start_pool"] == definitions[0]["start_pool"]
        assert variant["template"] == identifier
        pools = [
            row["document"]
            for row in resources
            if row["path"] == f"data/mss/worldgen/template_pool/{name}_start_pool.json"
        ]
        assert pools == [
            {
                "name": variant["start_pool"],
                "fallback": "minecraft:empty",
                "elements": [
                    {
                        "weight": 1,
                        "element": {
                            "element_type": "minecraft:single_pool_element",
                            "location": identifier,
                            "processors": "minecraft:empty",
                            "projection": "rigid",
                        },
                    }
                ],
            }
        ]
        assert structures[identifier]["templates"] == [identifier]
        assert structures[identifier]["missing"] == []
        content = contents[identifier]
        assert variant["template_size_xyz"] == content["template_size_xyz"]
        assert content["authored_entities"] == content["loot_references"] == []
        assert content["spawner_blocks"] == content["generation_markers"] == []


def test_soaring_rivers_preserve_omitted_default_and_complete_namespace() -> None:
    root = Path(__file__).resolve().parents[2]
    decisions = cast(
        "dict[str, JsonValue]",
        json.loads((root / "evidence/item-8/family-decisions.json").read_bytes()),
    )
    groups = [
        row
        for row in cast("list[dict[str, JsonValue]]", decisions["groups"])
        if str(row["family_id"]).startswith("mss:")
    ]
    members = [member for row in groups for member in cast("list[str]", row["structure_ids"])]
    registry = read_registry(
        root / "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
    )
    assert len(members) == len(set(members)) == 35
    assert set(members) == {key for key in registry if key.startswith("mss:")}
    group = next(row for row in groups if row["family_id"] == "mss:river")
    assert group["structure_ids"] == ["mss:birch_river", "mss:cherry_river"]
    code = ""
    for path, digest in cast("dict[str, str]", group["evidence"]).items():
        raw = (root / path).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == digest
        if path.endswith("GenericJigsawStructure.txt"):
            code = raw.decode()
    default = code.split("// String cannot_spawn_in_liquid\n", 1)[1].split("InvokeDynamic", 1)[0]
    assert "PrimitiveCodec.fieldOf:" in default
    assert "iconst_0" in default
    assert "Boolean.valueOf:" in default
    assert "MapCodec.orElse:" in default
    assert group["effective_cannot_spawn_in_liquid"] is False
    variants = cast("dict[str, dict[str, JsonValue]]", group["variants"])
    catalog = cast(
        "dict[str, JsonValue]",
        json.loads(
            gzip.decompress(
                (root / "evidence/item-8/sources/packaged-json-redacted.json.gz").read_bytes()
            )
        ),
    )
    traces = cast(
        "dict[str, JsonValue]",
        json.loads(
            gzip.decompress(
                (root / "evidence/item-8/sources/pool-traces-content.json.gz").read_bytes()
            )
        ),
    )
    resources = cast("list[dict[str, JsonValue]]", catalog["resources"])
    contents = cast("dict[str, dict[str, JsonValue]]", traces["template_contents"])
    normalized: list[dict[str, JsonValue]] = []
    for identifier, variant in variants.items():
        name = identifier.split(":")[1]
        definitions = [
            row["document"]
            for row in resources
            if row["path"] == f"data/mss/worldgen/structure/{name}.json"
        ]
        assert definitions == [variant["definition"]]
        definition = dict(cast("dict[str, JsonValue]", variant["definition"]))
        if name == "cherry_river":
            assert "cannot_spawn_in_liquid" not in definition
        else:
            assert definition["cannot_spawn_in_liquid"] is False
        _ = definition.setdefault("cannot_spawn_in_liquid", False)
        normalized.append(
            {key: value for key, value in definition.items() if key not in ("biomes", "start_pool")}
        )
        assert variant["template"] == identifier
        assert variant["template_size_xyz"] == contents[identifier]["template_size_xyz"]
    assert normalized[0] == normalized[1]


@pytest.mark.parametrize(
    ("family", "prefix", "member_count", "template_count"),
    [
        (
            "mns:ruin_fragments",
            (
                "mns:very_small",
                "mns:large_blackstone_",
                "mns:large_nether_brick",
                "mns:leafy_rubble",
                "mns:medium_blackstone",
                "mns:small_nether_brick",
            ),
            13,
            12,
        ),
        ("mns:bridge", ("mns:bridge_",), 6, 6),
        ("mns:circle_ruin", ("mns:circle_",), 2, 2),
        ("mns:medium_house", ("mns:medium_house",), 2, 2),
        ("repurposed_structures:witch_hut", ("repurposed_structures:witch_hut_",), 6, 6),
        (
            "mvs:stall",
            ("mvs:blue_stall", "mvs:orange_stall", "mvs:pink_stall", "mvs:red_stall"),
            4,
            4,
        ),
        ("mvs:end_scraps", ("mvs:end_scraps_",), 4, 4),
        (
            "mvs:log_pile",
            tuple(
                f"mvs:{wood}_log_pile"
                for wood in ("acacia", "birch", "dark_oak", "jungle", "oak", "spruce")
            ),
            6,
            6,
        ),
        (
            "mvs:lantern",
            (
                "mvs:medium_oak_lantern",
                *tuple(
                    f"mvs:small_{kind}_lantern"
                    for kind in (
                        "acacia",
                        "bamboo",
                        "birch",
                        "campfire",
                        "cherry",
                        "dark_oak",
                        "jungle",
                        "mangrove",
                        "oak",
                        "spruce",
                    )
                ),
            ),
            11,
            11,
        ),
        (
            "mns:medium_fungus",
            ("mns:medium_crimson_fungus", "mns:medium_warped_fungus"),
            4,
            4,
        ),
    ],
)
def test_variants_preserve_definitions_and_template_identity(
    family: str,
    prefix: tuple[str, ...],
    member_count: int,
    template_count: int,
) -> None:
    root = Path(__file__).resolve().parents[2]
    decisions = cast(
        "dict[str, JsonValue]",
        json.loads((root / "evidence/item-8/family-decisions.json").read_bytes()),
    )
    group = next(
        row
        for row in cast("list[dict[str, JsonValue]]", decisions["groups"])
        if row["family_id"] == family
    )
    variants = cast("dict[str, dict[str, JsonValue]]", group["variants"])
    registry = read_registry(
        root / "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
    )
    assert group["structure_ids"] == sorted(variants)
    assert set(variants) == {key for key in registry if key.startswith(prefix)}
    assert len(variants) == member_count
    for path, digest in cast("dict[str, str]", group["evidence"]).items():
        assert hashlib.sha256((root / path).read_bytes()).hexdigest() == digest
    catalog = cast(
        "dict[str, JsonValue]",
        json.loads(
            gzip.decompress(
                (root / "evidence/item-8/sources/packaged-json-redacted.json.gz").read_bytes()
            )
        ),
    )
    traces = cast(
        "dict[str, JsonValue]",
        json.loads(
            gzip.decompress(
                (root / "evidence/item-8/sources/pool-traces-content.json.gz").read_bytes()
            )
        ),
    )
    resources = cast("list[dict[str, JsonValue]]", catalog["resources"])
    structures = cast("dict[str, dict[str, JsonValue]]", traces["structures"])
    contents = cast("dict[str, dict[str, JsonValue]]", traces["template_contents"])
    definitions: dict[str, dict[str, JsonValue]] = {}
    for identifier, variant in variants.items():
        namespace, name = identifier.split(":")
        rows = [
            cast("dict[str, JsonValue]", row["document"])
            for row in resources
            if row["path"] == f"data/{namespace}/worldgen/structure/{name}.json"
        ]
        assert len(rows) == 1
        definitions[identifier] = rows[0]
        excluded = {"start_pool"}
        if "biomes" in variant:
            assert variant["biomes"] == rows[0]["biomes"]
            excluded.add("biomes")
        assert group["common_generation_definition"] == {
            key: value for key, value in rows[0].items() if key not in excluded
        }
        assert variant["start_pool"] == rows[0]["start_pool"]
        assert structures[identifier]["templates"] == [variant["template"]]
        assert structures[identifier]["missing"] == []
        assert (
            variant["template_size_xyz"] == contents[str(variant["template"])]["template_size_xyz"]
        )
    assert len({str(row["template"]) for row in variants.values()}) == template_count
    if family == "repurposed_structures:witch_hut":
        for variant in variants.values():
            content = contents[str(variant["template"])]
            assert content["template_size_xyz"] == [7, 8, 9]
            assert content["authored_entities"] == [
                {"id": "minecraft:witch", "path": "/entities/1/nbt"},
                {"id": "minecraft:cat", "path": "/entities/0/nbt"},
            ]
            assert content["loot_references"] == content["spawner_blocks"] == []
            assert content["generation_markers"] == content["unresolved_entities"] == []
    if family in {
        "mns:bridge",
        "mns:medium_fungus",
        "mns:ruin_fragments",
        "mvs:log_pile",
        "mvs:lantern",
    }:
        for variant in variants.values():
            content = contents[str(variant["template"])]
            assert content["authored_entities"] == content["loot_references"] == []
            assert content["spawner_blocks"] == content["generation_markers"] == []
    if family != "mns:ruin_fragments":
        return
    assert group["duplicate_definition_ids"] == [
        "mns:very_small_blackstone",
        "mns:very_small_nether_brick",
    ]
    assert definitions["mns:very_small_blackstone"] == definitions["mns:very_small_nether_brick"]
    assert variants["mns:very_small_blackstone"] == variants["mns:very_small_nether_brick"]
    assert (
        variants["mns:very_small_nether_brick"]["template"] == "mns:ruins/very_small_blackstone_1"
    )


@pytest.mark.parametrize(
    ("family", "namespace", "token", "members"),
    [("mns:well", "mns", "well", 3), ("mvs:dead_tree", "mvs", "dead_tree_", 8)],
)
def test_moog_modular_variants_preserve_components_and_definition_differences(
    family: str,
    namespace: str,
    token: str,
    members: int,
) -> None:
    root = Path(__file__).resolve().parents[2]
    decisions = cast(
        "dict[str, list[dict[str, JsonValue]]]",
        json.loads((root / "evidence/item-8/family-decisions.json").read_bytes()),
    )
    group = next(row for row in decisions["groups"] if row["family_id"] == family)
    registry = read_registry(
        root / "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
    )
    assert group["structure_ids"] == sorted(
        key for key in registry if key.startswith(f"{namespace}:") and token in key
    )
    assert len(cast("list[str]", group["structure_ids"])) == members
    for path, digest in cast("dict[str, str]", group["evidence"]).items():
        assert hashlib.sha256((root / path).read_bytes()).hexdigest() == digest
    catalog = cast(
        "dict[str, list[dict[str, JsonValue]]]",
        json.loads(
            gzip.decompress(
                (root / "evidence/item-8/sources/packaged-json-redacted.json.gz").read_bytes()
            )
        ),
    )
    traces = cast(
        "dict[str, dict[str, dict[str, JsonValue]]]",
        json.loads(
            gzip.decompress(
                (root / "evidence/item-8/sources/pool-traces-content.json.gz").read_bytes()
            )
        ),
    )
    normalized: list[dict[str, JsonValue]] = []
    for identifier, variant in cast("dict[str, dict[str, JsonValue]]", group["variants"]).items():
        name = identifier.split(":")[1]
        definitions = [
            cast("dict[str, JsonValue]", row["document"])
            for row in catalog["resources"]
            if row["path"] == f"data/{namespace}/worldgen/structure/{name}.json"
        ]
        assert definitions == [variant["definition"]]
        excluded = {"biomes", "start_pool"}
        if namespace == "mvs":
            excluded.add("cannot_spawn_in_liquid")
            assert definitions[0].get("cannot_spawn_in_liquid") == (
                None if identifier == "mvs:dead_tree_mangrove" else True
            )
        normalized.append({k: v for k, v in definitions[0].items() if k not in excluded})
        trace = traces["structures"][identifier]
        assert trace["missing"] == trace["unresolved_elements"] == []
        assert trace["templates"] == sorted(cast("dict[str, JsonValue]", variant["templates"]))
        for template, dimensions in cast("dict[str, list[int]]", variant["templates"]).items():
            content = traces["template_contents"][template]
            assert content["template_size_xyz"] == dimensions
            assert content["authored_entities"] == content["spawner_blocks"] == []
            markers = cast("list[dict[str, JsonValue]]", content["generation_markers"])
            if template in {
                "mvs:dead_tree/acacia",
                "mvs:dead_tree/acacia_trunk",
                "mvs:dead_tree/birch",
            }:
                assert len(markers) == 1
                marker = cast("dict[str, JsonValue]", markers[0]["nbt"])
                assert marker["id"] == "minecraft:structure_block"
                assert marker["mode"] == "SAVE"
                assert marker["metadata"] == ""
            else:
                assert markers == []
            if template.endswith("_lower"):
                assert dimensions == [9, 8, 9]
                assert content["loot_references"] == [
                    {"path": "/block_entities/0/nbt/LootTable", "value": "mns:chests/uncommon"}
                ]
            else:
                assert content["loot_references"] == []
        expected_count = 1 if identifier == "mns:crimson_lava_well" else 2
        assert len(cast("dict[str, JsonValue]", variant["templates"])) == expected_count
    assert all(row == normalized[0] for row in normalized)


def test_spider_dungeon_attributes_bind_custom_spawners_loot_and_components() -> None:
    root = Path(__file__).resolve().parents[2]
    decisions = cast(
        "dict[str, JsonValue]",
        json.loads((root / "evidence/item-8/family-decisions.json").read_bytes()),
    )
    group = next(
        row
        for row in cast("list[dict[str, JsonValue]]", decisions["groups"])
        if row["family_id"] == "betterdungeons:spider_dungeon"
    )
    texts: dict[str, str] = {}
    for path, digest in cast("dict[str, str]", group["evidence"]).items():
        raw = (root / path).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == digest
        if path.endswith(".txt"):
            texts[Path(path).stem.rsplit(".", 1)[-1]] = raw.decode()
    assert "SpiderDungeonBigTunnelPiece" in texts["SpiderDungeonStructure"]
    assert "addChildren:" in texts["SpiderDungeonStructure"]
    assert group["custom_components"] == [
        "SpiderDungeonBigTunnelPiece",
        "SpiderDungeonSmallTunnelPiece",
        "SpiderDungeonNestPiece",
        "SpiderDungeonEggRoomPiece",
    ]
    for component in (
        "SpiderDungeonBigTunnelPiece",
        "SpiderDungeonSmallTunnelPiece",
        "SpiderDungeonNestPiece",
    ):
        reference = f"spider_dungeon/piece/{component}"
        assert reference in texts["SpiderDungeonBigTunnelPiece"]
    assert "SpiderDungeonEggRoomPiece" in texts["SpiderDungeonSmallTunnelPiece"]
    attrs = cast("dict[str, dict[str, JsonValue]]", group["attributes"])
    spawners = cast("list[dict[str, str]]", attrs["generated_spawners"]["source_components"])
    assert [(row["class"], row["entity_id"]) for row in spawners] == [
        ("SpiderDungeonNestPiece", "minecraft:cave_spider"),
        ("SpiderDungeonEggRoomPiece", "minecraft:spider"),
    ]
    for row in spawners:
        code = texts[row["class"]]
        assert "public void " + row["method"] + "(" in code
        assert "Blocks.SPAWNER:" in code
        assert "EntityType." + row["entity_id"].split(":")[1].upper() + ":" in code
        assert "SpawnerBlockEntity.setEntityId:" in code
    loot = str(attrs["loot_table_source"]["generated_chest_table"])
    namespace, path = loot.split(":")
    assert "// String " + namespace in texts["SpiderDungeonEggRoomPiece"]
    assert "// String " + path in texts["SpiderDungeonEggRoomPiece"]
    assert "Method createChest:" in texts["SpiderDungeonEggRoomPiece"]
    catalog = cast(
        "dict[str, JsonValue]",
        json.loads(
            gzip.decompress(
                (root / "evidence/item-8/sources/packaged-json-redacted.json.gz").read_bytes()
            )
        ),
    )
    resources = cast("list[dict[str, JsonValue]]", catalog["resources"])
    definition = next(
        cast("dict[str, JsonValue]", row["document"])
        for row in resources
        if row["path"] == "data/betterdungeons/worldgen/structure/spider_dungeon.json"
    )
    assert attrs["mob_source"]["structure_spawn_override"] == definition["spawn_overrides"]
    assert definition["step"] == "underground_structures"
    assert any(row["path"] == f"data/{namespace}/loot_table/{path}.json" for row in resources)
    assert attrs["generated_spawners"]["observed_per_structure_counts"] == "UNKNOWN"


def test_integrated_stronghold_keeps_rooms_as_components_and_binds_spawn_override() -> None:
    root = Path(__file__).resolve().parents[2]
    decisions = cast(
        "dict[str, JsonValue]",
        json.loads((root / "evidence/item-8/family-decisions.json").read_bytes()),
    )
    groups = [
        row
        for row in cast("list[dict[str, JsonValue]]", decisions["groups"])
        if str(row["family_id"]).startswith("integrated_stronghold:")
    ]
    assert len(groups) == 1
    group = groups[0]
    identifier = "integrated_stronghold:stronghold"
    registry = read_registry(
        root / "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
    )
    assert (
        group["structure_ids"]
        == [member for member in registry if member.startswith("integrated_stronghold:")]
        == [identifier]
    )
    for path, digest in cast("dict[str, str]", group["evidence"]).items():
        assert hashlib.sha256((root / path).read_bytes()).hexdigest() == digest
    catalog = cast(
        "dict[str, JsonValue]",
        json.loads(
            gzip.decompress(
                (root / "evidence/item-8/sources/packaged-json-redacted.json.gz").read_bytes()
            )
        ),
    )
    definitions = [
        cast("dict[str, JsonValue]", row["document"])
        for row in cast("list[dict[str, JsonValue]]", catalog["resources"])
        if row["path"] == "data/integrated_stronghold/worldgen/structure/stronghold.json"
    ]
    assert len(definitions) == 1
    definition = definitions[0]
    attributes = cast("dict[str, dict[str, JsonValue]]", group["attributes"])
    assert definition["start_pool"] == group["start_pool"]
    assert definition["spawn_overrides"] == attributes["mob_source"]["structure_spawn_override"]
    assert definition["start_height"] == {
        "type": "minecraft:uniform",
        "min_inclusive": {"absolute": 15},
        "max_inclusive": {"absolute": 15},
    }
    assert definition["step"] == "strongholds"
    traces = cast(
        "dict[str, JsonValue]",
        json.loads(
            gzip.decompress(
                (root / "evidence/item-8/sources/pool-traces-content.json.gz").read_bytes()
            )
        ),
    )
    trace = cast("dict[str, dict[str, JsonValue]]", traces["structures"])[identifier]
    assert trace["start_pool"] == group["start_pool"]
    assert group["missing_components"] == [
        row["id"] for row in cast("list[dict[str, str]]", trace["missing"])
    ]


def test_mineshaft_group_covers_its_runtime_variants_and_preserved_specialized_generator() -> None:
    root = Path(__file__).resolve().parents[2]
    decisions = cast(
        "dict[str, JsonValue]",
        json.loads((root / "evidence/item-8/family-decisions.json").read_bytes()),
    )
    decision = cast("list[dict[str, JsonValue]]", decisions["groups"])[0]
    evidence = cast("dict[str, str]", decision["evidence"])
    for path, digest in evidence.items():
        assert hashlib.sha256((root / path).read_bytes()).hexdigest() == digest
    registry = read_registry(
        root / "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
    )
    members = cast("list[str]", decision["structure_ids"])
    assert len(members) == len(set(members))
    assert set(members) == {
        identifier for identifier in registry if identifier.startswith("bettermineshafts:")
    }
    raw = (root / "evidence/item-8/sources/packaged-json-redacted.json.gz").read_bytes()
    catalog = cast("dict[str, JsonValue]", json.loads(gzip.decompress(raw)))
    definitions: dict[str, dict[str, JsonValue]] = {}
    for resource in cast("list[dict[str, JsonValue]]", catalog["resources"]):
        identity = resource_identity(str(resource["path"]), "worldgen/structure")
        if identity is not None and identity[0] in members:
            assert identity[1] == ""
            assert identity[0] not in definitions
            definitions[identity[0]] = cast("dict[str, JsonValue]", resource["document"])
    assert set(definitions) == set(members)
    for document in definitions.values():
        assert {
            key: value for key, value in document.items() if key not in {"biomes", "config"}
        } == {
            "type": "bettermineshafts:mineshaft",
            "spawn_overrides": {},
            "step": "underground_structures",
        }
    code_root = root / "evidence/item-8/sources/mineshafts-code"
    identities = cast(
        "list[dict[str, str]]", json.loads((code_root / "identities.json").read_bytes())
    )
    for row in identities:
        assert (
            hashlib.sha256((code_root / row["disassembly"]).read_bytes()).hexdigest()
            == row["disassembly_sha256"]
        )


def test_ctov_size_decisions_exactly_cover_source_proven_variant_groups() -> None:
    root = Path(__file__).resolve().parents[2]
    decisions = cast(
        "dict[str, JsonValue]",
        json.loads((root / "evidence/item-8/family-decisions.json").read_bytes()),
    )
    groups = [
        row
        for row in cast("list[dict[str, JsonValue]]", decisions["groups"])
        if str(row["family_id"]).startswith("ctov:") and row["family_id"] != "ctov:pillager_outpost"
    ]
    registry = read_registry(
        root / "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
    )
    raw = (root / "evidence/item-8/sources/packaged-json-redacted.json.gz").read_bytes()
    catalog = cast("dict[str, JsonValue]", json.loads(gzip.decompress(raw)))
    proven = size_variant_groups(registry, cast("list[JsonValue]", catalog["resources"]))
    expected = {
        tuple(str(member["structure_id"]) for member in cast("list[dict[str, JsonValue]]", group))
        for group in proven
    }
    actual = [tuple(cast("list[str]", row["structure_ids"])) for row in groups]
    assert len(actual) == len(set(actual))
    assert set(actual) == expected
    members = [identifier for group in actual for identifier in group]
    assert len(members) == len(set(members))
    assert set(members) == {
        identifier
        for identifier in registry
        if identifier.startswith(("ctov:small/", "ctov:medium/", "ctov:large/"))
    }
    for row in groups:
        assert {
            identifier.split("/", 1)[1] for identifier in cast("list[str]", row["structure_ids"])
        } == {str(row["family_id"]).split(":", 1)[1]}
        for path, digest in cast("dict[str, str]", row["evidence"]).items():
            assert hashlib.sha256((root / path).read_bytes()).hexdigest() == digest


def test_ctov_outposts_preserve_duplicate_roots_and_missing_components() -> None:
    root = Path(__file__).resolve().parents[2]
    decisions = cast(
        "dict[str, list[dict[str, JsonValue]]]",
        json.loads((root / "evidence/item-8/family-decisions.json").read_bytes()),
    )
    group = next(row for row in decisions["groups"] if row["family_id"] == "ctov:pillager_outpost")
    for path, digest in cast("dict[str, str]", group["evidence"]).items():
        assert hashlib.sha256((root / path).read_bytes()).hexdigest() == digest
    catalog = cast(
        "dict[str, list[dict[str, JsonValue]]]",
        json.loads(
            gzip.decompress(
                (root / "evidence/item-8/sources/packaged-json-redacted.json.gz").read_bytes()
            )
        ),
    )
    traces = cast(
        "dict[str, dict[str, dict[str, JsonValue]]]",
        json.loads(
            gzip.decompress(
                (root / "evidence/item-8/sources/pool-traces-content.json.gz").read_bytes()
            )
        ),
    )
    registry = {
        k
        for k in read_registry(
            root
            / "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
        )
        if k.startswith("ctov:")
    }
    members = [
        k
        for row in decisions["groups"]
        if str(row["family_id"]).startswith("ctov:")
        for k in cast("list[str]", row["structure_ids"])
    ]
    assert set(members) == registry
    assert len(members) == len(set(members)) == 78
    variants = cast("dict[str, dict[str, JsonValue]]", group["variants"])
    assert (
        group["structure_ids"]
        == sorted(variants)
        == sorted(k for k in registry if k.startswith("ctov:pillager_outpost_"))
    )
    assert len(variants) == 12
    definitions: dict[str, dict[str, JsonValue]] = {}
    for identifier, variant in variants.items():
        name = identifier.split(":")[1]
        rows = [
            cast("dict[str, JsonValue]", r["document"])
            for r in catalog["resources"]
            if r["path"] == f"data/ctov/worldgen/structure/{name}.json"
        ]
        assert len(rows) == 1
        definition = rows[0]
        definitions[identifier] = definition
        assert group["common_generation_definition"] == {
            k: v for k, v in definition.items() if k not in ("biomes", "size", "start_pool")
        }
        for field in ("biomes", "size", "start_pool"):
            assert variant[field] == definition[field]
        trace = traces["structures"][identifier]
        assert trace["start_pool"] == variant["start_pool"]
        assert trace["missing"] == variant["missing_components"]
        assert {
            "id": "savage_and_ravage:pillager_outpost/feature_targets_arrow",
            "kind": "template",
        } in cast("list[JsonValue]", trace["missing"])
        assert trace["unresolved_elements"] == []
    assert group["duplicate_definition_ids"] == [
        "ctov:pillager_outpost_badlands",
        "ctov:pillager_outpost_mesa",
    ]
    assert (
        definitions["ctov:pillager_outpost_badlands"] == definitions["ctov:pillager_outpost_mesa"]
    )
    assert variants["ctov:pillager_outpost_badlands"] == variants["ctov:pillager_outpost_mesa"]


def test_working_inventory_keeps_unassigned_ids_and_rejects_double_counting() -> None:
    decision: dict[str, JsonValue] = {
        "family_id": "example:family",
        "name": "Example",
        "structure_ids": ["example:a"],
    }
    sources: dict[str, JsonValue] = {"structure_biomes": {"example:a": {"biomes": []}}}
    traces: dict[str, JsonValue] = {
        "structures": {},
        "untraced_structures": {"example:a": {"reason": "custom"}},
        "template_contents": {},
    }
    bounds: dict[str, JsonValue] = {"observations": []}
    result = assemble(("example:a", "example:b"), [decision], sources, traces, bounds)
    assert result["status"] == "INCOMPLETE"
    assert result["unassigned_registry_ids"] == ["example:b"]
    conflicting = dict(decision, family_id="example:second")
    with pytest.raises(ValueError, match="multiply assigned"):
        _ = assemble(("example:a",), [decision, conflicting], sources, traces, bounds)
    with pytest.raises(ValueError, match="unregistered"):
        _ = assemble(("example:b",), [decision], sources, traces, bounds)
    decision["attributes"] = {"intended_hostility": {"value": "hostile", "basis": "source"}}
    result = assemble(("example:a",), [decision], sources, traces, bounds)
    families = cast("dict[str, dict[str, JsonValue]]", result["families"])
    assert families["example:family"]["intended_hostility"] == {
        "value": "hostile",
        "basis": "source",
    }
    assert families["example:family"]["status"] == "INCOMPLETE"
    decision["attributes"] = {"status": "COMPLETE"}
    with pytest.raises(ValueError, match="protected family attribute"):
        _ = assemble(("example:a",), [decision], sources, traces, bounds)


def test_inventory_geometry_keeps_paired_extents_and_excludes_partial_starts() -> None:
    decision: dict[str, JsonValue] = {
        "family_id": "example:family",
        "name": "Example",
        "structure_ids": ["example:a"],
    }
    sources: dict[str, JsonValue] = {"structure_biomes": {"example:a": {}}}
    traces: dict[str, JsonValue] = {
        "structures": {},
        "untraced_structures": {},
        "template_contents": {},
    }
    observations = cast(
        "list[JsonValue]",
        [
            {
                "structure_id": identifier,
                "dimension": "minecraft:overworld",
                "chunk_full": full,
                "size_xyz": size,
            }
            for identifier, full, size in [
                ("example:a", True, [11, 14, 19]),
                ("example:a", True, [19, 14, 11]),
                ("example:a", True, [11, 14, 19]),
                ("example:a", False, [100, 200, 300]),
                ("example:other", True, [400, 500, 600]),
            ]
        ],
    )
    result = assemble(("example:a",), [decision], sources, traces, {"observations": observations})
    row = cast("dict[str, dict[str, JsonValue]]", result["families"])["example:family"]
    footprint = cast("dict[str, JsonValue]", row["approximate_footprint"])
    height = cast("dict[str, JsonValue]", row["approximate_vertical_size"])
    assert footprint["observed_envelope_xz_blocks"] == [[11, 19], [19, 11]]
    assert height["observed_envelope_y_blocks"] == [14]
    assert "not family-wide bounds or occupied geometry" in str(footprint["basis"])
    assert row["status"] == "INCOMPLETE"
    result = assemble(("example:a",), [decision], sources, traces, {"observations": []})
    row = cast("dict[str, dict[str, JsonValue]]", result["families"])["example:family"]
    assert str(row["approximate_footprint"]).startswith("UNKNOWN:")
    assert str(row["approximate_vertical_size"]).startswith("UNKNOWN:")
    decision["attributes"] = {"approximate_footprint": "explicit source assessment"}
    result = assemble(("example:a",), [decision], sources, traces, {"observations": observations})
    row = cast("dict[str, dict[str, JsonValue]]", result["families"])["example:family"]
    assert row["approximate_footprint"] == "explicit source assessment"


def test_inventory_preserves_loot_kinds_and_rejects_missing_template_content() -> None:
    references: list[JsonValue] = [
        {"path": "/block_entities/0/nbt/LootTable", "value": "example:chest"},
        {"path": "/entities/0/nbt/DeathLootTable", "value": "example:chest"},
        {"path": "/block_entities/1/nbt/LootTable", "value": "example:chest"},
        {"path": "/block_entities/2/nbt/loot_tables_to_eject", "value": ["example:reward"]},
    ]
    decision: dict[str, JsonValue] = {
        "family_id": "example:family",
        "name": "Example",
        "structure_ids": ["example:a"],
    }
    sources: dict[str, JsonValue] = {"structure_biomes": {"example:a": {"biomes": []}}}
    contents: dict[str, JsonValue] = {
        "example:room": {
            "loot_references": references,
            "authored_entities": [
                {"id": "example:animal", "path": "/entities/0/nbt"},
                {"id": "example:animal", "path": "/entities/1/nbt"},
                {"id": "example:rider", "path": "/entities/1/nbt/Passengers/0"},
            ],
            "unresolved_entities": [{"path": "/entities/2/nbt", "reason": "missing ID"}],
            "spawner_blocks": [
                {
                    "path": "/block_entities/0",
                    "nbt": {
                        "id": "minecraft:mob_spawner",
                        "SpawnData": {"entity": {"id": "minecraft:zombie"}},
                        "SpawnPotentials": [],
                    },
                },
                {"path": "/block_entities/1", "nbt": {"id": "example:custom_spawner"}},
            ],
            "generation_markers": [{"path": "/block_entities/2"}],
        },
        "example:empty": {
            "loot_references": [],
            "authored_entities": [],
            "unresolved_entities": [],
            "spawner_blocks": [],
            "generation_markers": [],
        },
    }
    traces: dict[str, JsonValue] = {
        "structures": {"example:a": {"templates": ["example:room", "example:empty"]}},
        "untraced_structures": {},
        "template_contents": contents,
    }
    bounds: dict[str, JsonValue] = {"observations": []}
    result = assemble(("example:a",), [decision], sources, traces, bounds)
    families = cast("dict[str, dict[str, JsonValue]]", result["families"])
    loot = cast("dict[str, JsonValue]", families["example:family"]["loot_table_source"])
    mobs = cast("dict[str, JsonValue]", families["example:family"]["mob_source"])
    spawners = cast("dict[str, JsonValue]", families["example:family"]["generated_spawners"])
    assert spawners["packaged_entity_sources"] == [
        {
            "spawner_id": "minecraft:mob_spawner",
            "mode": "ordinary",
            "entity_id": "minecraft:zombie",
            "templates": ["example:room"],
        }
    ]
    assert spawners["unresolved_sources"] == {
        "example:room": [
            {
                "block_path": "/block_entities/1",
                "mode": "custom",
                "path": "",
                "unresolved": "custom spawner semantics",
                "source_value": "example:custom_spawner",
            }
        ]
    }
    assert spawners["generation_marker_templates"] == ["example:room"]
    assert mobs["packaged_authored_entity_templates"] == {
        "example:animal": ["example:room"],
        "example:rider": ["example:room"],
    }
    assert mobs["unresolved_authored_entities"] == {
        "example:room": [{"path": "/entities/2/nbt", "reason": "missing ID"}]
    }
    assert loot["packaged_references"] == [
        {"field": "DeathLootTable", "value": "example:chest", "templates": ["example:room"]},
        {"field": "LootTable", "value": "example:chest", "templates": ["example:room"]},
        {
            "field": "loot_tables_to_eject",
            "value": ["example:reward"],
            "templates": ["example:room"],
        },
    ]
    assert (
        loot["status"] == "packaged possibilities; effective generation and injections unresolved"
    )
    assert families["example:family"]["status"] == "INCOMPLETE"
    del contents["example:room"]
    with pytest.raises(KeyError, match="example:room"):
        _ = assemble(("example:a",), [decision], sources, traces, bounds)


def test_seven_seas_groups_cover_registered_roots_without_counting_spawner_components() -> None:
    root = Path(__file__).resolve().parents[2]
    decisions = cast(
        "dict[str, JsonValue]",
        json.loads((root / "evidence/item-8/family-decisions.json").read_bytes()),
    )
    groups = [
        row
        for row in cast("list[dict[str, JsonValue]]", decisions["groups"])
        if str(row["family_id"]).startswith("dungeons_arise_seven_seas:")
    ]
    registry = read_registry(
        root / "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
    )
    raw = (root / "evidence/item-8/sources/pool-traces-content.json.gz").read_bytes()
    traces = cast("dict[str, JsonValue]", json.loads(gzip.decompress(raw)))
    structures = cast("dict[str, dict[str, JsonValue]]", traces["structures"])
    templates = cast("dict[str, dict[str, JsonValue]]", traces["template_contents"])
    members = [member for row in groups for member in cast("list[str]", row["structure_ids"])]
    assert len(members) == len(set(members))
    assert set(members) == {key for key in registry if key.startswith("dungeons_arise_seven_seas:")}
    for row in groups:
        identifier = str(row["family_id"])
        assert row["structure_ids"] == [identifier]
        assert row["start_pool"] == structures[identifier]["start_pool"]
        main = str(row["main_template"])
        assert main in cast("list[str]", structures[identifier]["templates"])
        assert main in templates
        attributes = cast("dict[str, dict[str, JsonValue]]", row["attributes"])
        dimensions = cast("list[int]", templates[main]["template_size_xyz"])
        assert attributes["approximate_footprint"]["main_template_xz_blocks"] == [
            dimensions[0],
            dimensions[2],
        ]
        assert attributes["approximate_vertical_size"]["main_template_y_blocks"] == dimensions[1]
        loot = cast("list[dict[str, JsonValue]]", templates[main]["loot_references"])
        assert set(
            cast("list[str]", attributes["loot_table_source"]["packaged_container_tables"])
        ) == {str(reference["value"]) for reference in loot}
        initial_types: set[str] = set()
        potential_types: set[str] = set()
        for template in cast("list[str]", structures[identifier]["templates"]):
            for block in cast("list[dict[str, JsonValue]]", templates[template]["spawner_blocks"]):
                nbt = cast("dict[str, JsonValue]", block["nbt"])
                initial_types.add(
                    cast("dict[str, dict[str, str]]", nbt["SpawnData"])["entity"]["id"]
                )
                for potential in cast("list[dict[str, JsonValue]]", nbt["SpawnPotentials"]):
                    if cast("int", potential["weight"]) > 0:
                        potential_types.add(
                            cast("dict[str, dict[str, str]]", potential["data"])["entity"]["id"]
                        )
        assert (
            initial_types
            == potential_types
            == set(cast("list[str]", attributes["mob_source"]["authored_spawner_types"]))
        )
        assert initial_types == set(
            cast("list[str]", attributes["generated_spawners"]["authored_types"])
        )
        missing = cast("list[dict[str, str]]", structures[identifier]["missing"])
        assert attributes["generated_spawners"]["missing_components"] == [
            entry["id"] for entry in missing
        ]
        for path, digest in cast("dict[str, str]", row["evidence"]).items():
            assert hashlib.sha256((root / path).read_bytes()).hexdigest() == digest


def test_all_runtime_structure_ids_have_exactly_one_working_group() -> None:
    root = Path(__file__).resolve().parents[2]
    decisions = cast(
        "dict[str, list[dict[str, JsonValue]]]",
        json.loads((root / "evidence/item-8/family-decisions.json").read_bytes()),
    )
    registry = read_registry(
        root / "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
    )
    members = [
        identifier
        for group in decisions["groups"]
        for identifier in cast("list[str]", group["structure_ids"])
    ]
    assert len(members) == len(set(members)) == len(registry) == 887
    assert set(members) == set(registry)
