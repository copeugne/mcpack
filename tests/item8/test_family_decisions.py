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

if TYPE_CHECKING:
    from pydantic import JsonValue


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
    if namespace == "mns:":
        variants = [
            member
            for row in cast("list[dict[str, JsonValue]]", decisions["groups"])
            if str(row["family_id"]).startswith(namespace)
            and len(cast("list[str]", row["structure_ids"])) > 1
            for member in cast("list[str]", row["structure_ids"])
        ]
        assert len(members + variants) == len(set(members + variants)) == 52
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
    assert len({str(row["start_pool"]) for row in groups}) == len(groups)
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
def test_moog_variants_preserve_definitions_and_template_identity(
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
        if str(row["family_id"]).startswith("ctov:")
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
