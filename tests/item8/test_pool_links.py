from __future__ import annotations

import gzip
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import TYPE_CHECKING, cast

import pytest

from mcpack_evidence.item8_pool_links import add_pool_elements, pool_links, template_links
from mcpack_evidence.item8_pool_trace import trace_pool
from tests.item8.test_inventory_sources import row

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_pool_additions_preserve_delegate_provenance_and_constraints() -> None:
    pools = pool_links([row("data/example/worldgen/template_pool/houses.json", {"elements": []})])
    modifier = row("data/example/lithostitched/worldgen_modifier/tavern.json", {
        "type": "lithostitched:add_template_pool_elements",
        "template_pools": "example:houses",
        "elements": [{"weight": 5, "element": {
            "element_type": "lithostitched:limited", "limit": 1,
            "delegate": {"element_type": "minecraft:single_pool_element",
                         "location": "example:tavern", "processors": "minecraft:empty"},
        }}],
    })
    add_pool_elements(pools, [modifier])
    result = trace_pool("example:houses", pools, [])
    assert result["missing"] == [{"kind": "template", "id": "example:tavern"}]
    terminal = cast("list[dict[str, JsonValue]]", result["terminal_edges"])
    edges = [cast("dict[str, JsonValue]", entry["edge"]) for entry in terminal]
    addition = next(edge for edge in edges if edge["kind"] == "pool_addition")
    assert addition["document"] == modifier["document"]
    assert addition["source"] == {key: modifier[key] for key in ("archive", "path", "sha256")}
    constraint = next(edge for edge in edges if edge["kind"] == "pool_element_constraint")
    assert constraint["document"] == {"element_type": "lithostitched:limited", "limit": 1}
    assert constraint["source"] == addition["source"]
    document = cast("dict[str, JsonValue]", modifier["document"])
    document["template_pools"] = ["example:missing"]
    with pytest.raises(ValueError, match="unresolved pool modifier target"):
        add_pool_elements(pools, [modifier])


def test_frozen_trace_reaches_all_selected_village_additions() -> None:
    root = Path(__file__).resolve().parents[2]
    raw = (root / "evidence/item-8/sources/pool-traces-content.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "703eed7b5d558b54a62985c7f919d0254e8de613292364c514c5b47b298accc5"
    )
    trace = cast("dict[str, JsonValue]", json.loads(gzip.decompress(raw)))
    report = cast("dict[str, JsonValue]", trace["pool_modifiers"])
    dispositions = cast("list[dict[str, JsonValue]]", report["dispositions"])
    selected = {
        (str(row["archive"]), str(row["path"]), str(row["sha256"]))
        for row in dispositions if row["status"] == "included in potential pool reachability"
    }
    assert len(selected) == 68
    excluded = sum(row["status"] == "excluded by NeoForge mod conditions" for row in dispositions)
    assert excluded == 956
    assert all(row["status"] != "untraced modifier type" for row in dispositions)
    inspected = [entry for entry in dispositions
                 if entry["status"] == "inspected non-family contribution"]
    assert Counter(str(row["type"]) for row in inspected) == {
        "lithostitched:add_features": 30, "lithostitched:remove_features": 4,
        "lithostitched:add_processor_list_processors": 1,
        "lithostitched:add_surface_rule": 1,
        "lithostitched:internal/compile_raw_templates": 1,
    }
    for entry in inspected:
        assert cast("dict[str, JsonValue]", entry["document"])["type"] == entry["type"]
        assert entry["contribution"]
    assert len(cast("list[JsonValue]", report["excluded_resource_layers"])) == 6
    structures = cast("dict[str, dict[str, JsonValue]]", trace["structures"])
    reached: set[tuple[str, str, str]] = set()
    for structure in structures.values():
        for terminal in cast("list[dict[str, JsonValue]]", structure["terminal_edges"]):
            edge = cast("dict[str, JsonValue]", terminal["edge"])
            if edge["kind"] == "pool_addition":
                source = cast("dict[str, str]", edge["source"])
                reached.add((source["archive"], source["path"], source["sha256"]))
    assert reached == selected
    trial = structures["minecraft:trial_chambers"]
    assert "regions_unexplored:trial_chambers/ashen" in cast("list[str]", trial["templates"])
    replacement = cast("dict[str, JsonValue]", trial["alias_replacement"])
    definition = cast("dict[str, JsonValue]", replacement["document"])
    assert definition["append"] is False
    assert trial["pool_aliases"] == definition["pool_aliases"]
    assert trial["packaged_pool_aliases"] != trial["pool_aliases"]
    tags = cast("dict[str, dict[str, JsonValue]]", trace["pool_alias_tags"])
    melee = tags["lithostitched:trial_spawner/melee"]
    assert "regions_unexplored:trial_chambers/ashen" in cast("list[str]", melee["values"])
    assert len(cast("list[JsonValue]", melee["sources"])) == 2
    content = cast("dict[str, dict[str, JsonValue]]", trace["template_contents"])
    ashen = content["regions_unexplored:trial_chambers/ashen"]
    spawner = cast("list[dict[str, JsonValue]]", ashen["spawner_blocks"])[0]
    nbt = cast("dict[str, JsonValue]", spawner["nbt"])
    for mode in ("normal_config", "ominous_config"):
        config = cast("dict[str, JsonValue]", nbt[mode])
        potentials = cast("list[dict[str, JsonValue]]", config["spawn_potentials"])
        data = cast("dict[str, JsonValue]", potentials[0]["data"])
        assert data["entity"] == {"id": "regions_unexplored:ashen"}
    for biome in ("desert", "plains", "savanna", "snowy", "taiga"):
        templates = cast("list[str]", structures[f"minecraft:village_{biome}"]["templates"])
        assert f"village_taverns:village/{biome}/tavern" in templates


def test_pool_uses_path_identity_and_preserves_nested_links() -> None:
    resource = row(
        "data/example/worldgen/template_pool/start.json",
        {
            "name": "example:misleading_name",
            "fallback": "empty",
            "elements": [
                {
                    "weight": 2,
                    "element": {
                        "element_type": "minecraft:list_pool_element",
                        "elements": [
                            {
                                "element_type": "minecraft:single_pool_element",
                                "location": "example:tower",
                                "processors": "example:weathering",
                            },
                            {
                                "element_type": "minecraft:feature_pool_element",
                                "feature": "example:tree",
                            },
                        ],
                    },
                }
            ],
        },
    )
    result = cast("dict[str, JsonValue]", pool_links([resource])[0])
    assert result["id"] == "example:start"
    edges = cast("list[dict[str, JsonValue]]", result["edges"])
    assert [(edge["kind"], edge["id"]) for edge in edges] == [
        ("pool", "minecraft:empty"),
        ("template", "example:tower"),
        ("processor_list", "example:weathering"),
        ("placed_feature", "example:tree"),
    ]
    assert edges[1]["pointer"] == "/elements/0/element/elements/0/location"


def test_unknown_elements_remain_explicit() -> None:
    resource = row(
        "data/example/worldgen/template_pool/start.json",
        {"elements": [{"weight": 1, "element": {"element_type": "example:custom"}}]},
    )
    result = cast("dict[str, JsonValue]", pool_links([resource])[0])
    assert result["edges"] == []
    assert result["unresolved_elements"]


def test_template_connectors_preserve_optional_pack_and_duplicate_connections() -> None:
    blocks: list[JsonValue] = [
        {"nbt": {"id": "minecraft:jigsaw", "pool": "example:roads"}},
        {"nbt": {"id": "minecraft:jigsaw", "pool": "example:roads"}},
        {"nbt": {"id": "minecraft:chest", "LootTable": "example:loot"}},
    ]
    resource = row("optional/data/example/structures/tower.nbt", {"block_entities": blocks})
    result = cast("dict[str, JsonValue]", template_links([resource])[0])
    assert result["id"] == "example:tower"
    assert result["pack_prefix"] == "optional"
    edges = cast("list[dict[str, JsonValue]]", result["edges"])
    assert len(edges) == 2
    assert edges[0]["pointer"] != edges[1]["pointer"]
    assert edges[0]["id"] == edges[1]["id"] == "example:roads"


def test_frozen_version_selection_preserves_unselected_alternatives() -> None:
    resource = row(
        "data/example/worldgen/template_pool/start.json",
        {
            "elements": [
                {
                    "element": {
                        "element_type": "moogs_structures:versioned_single_pool_element",
                        "location": "example:default",
                        "locations": {"1.21-1.21.8": "example:old", "26.1": "example:new"},
                        "processors": "minecraft:empty",
                    },
                    "weight": 1,
                }
            ]
        },
    )
    result = cast("dict[str, JsonValue]", pool_links([resource])[0])
    edges = cast("list[dict[str, JsonValue]]", result["edges"])
    conditional = [edge for edge in edges if "version_range" in edge]
    assert [(edge["id"], edge["version_range"]) for edge in conditional] == [
        ("example:old", "1.21-1.21.8"),
        ("example:new", "26.1"),
    ]
    assert [edge["selected"] for edge in conditional] == [True, False]
    assert edges[0]["selected"] is False
    assert result["unresolved_elements"] == []


def test_custom_single_and_inline_entity_feature_keep_distinct_sources() -> None:
    feature: JsonValue = {
        "feature": {
            "type": "supplementaries:spawn_entity_with_passengers",
            "config": {"entity": "minecraft:boat", "passengers": ["minecraft:pillager"]},
        },
        "placement": [],
    }
    resource = row(
        "data/example/worldgen/template_pool/start.json",
        {
            "elements": [
                {
                    "weight": 1,
                    "element": {
                        "element_type": "yungsapi:yung_single_element",
                        "location": "example:tower",
                        "processors": "example:processor",
                    },
                },
                {
                    "weight": 1,
                    "element": {
                        "element_type": "minecraft:feature_pool_element",
                        "feature": feature,
                    },
                },
            ]
        },
    )
    result = cast("dict[str, JsonValue]", pool_links([resource])[0])
    edges = cast("list[dict[str, JsonValue]]", result["edges"])
    assert edges[0]["id"] == "example:tower"
    assert edges[-1]["kind"] == "inline_placed_feature"
    assert edges[-1]["document"] == feature
    assert result["unresolved_elements"] == []


@pytest.mark.parametrize(
    "locations",
    [
        {"1.21-1.21.8": "example:a", "1.21.1": "example:b"},
        {"1.21.9-1.21.11": "example:newer"},
    ],
)
def test_ambiguous_or_nonmatching_version_maps_fail(locations: dict[str, str]) -> None:
    resource = row(
        "data/example/worldgen/template_pool/start.json",
        {
            "elements": [
                {
                    "element": {
                        "element_type": "moogs_structures:versioned_single_pool_element",
                        "location": "example:fallback",
                        "locations": dict(locations),
                    }
                }
            ]
        },
    )
    with pytest.raises(ValueError, match="does not uniquely select"):
        _ = pool_links([resource])


def test_frozen_catalog_has_no_unresolved_pool_codecs_or_version_selections() -> None:
    root = Path(__file__).resolve().parents[2]
    path = root / "evidence/item-8/sources/packaged-json-redacted.json.gz"
    raw = path.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "a5279d453f32edf7b1adc5c06b09953785b990b4b01c362b1423ed2f88930fdd"
    )
    catalog = cast("dict[str, JsonValue]", json.loads(gzip.decompress(raw)))
    resources = cast("list[JsonValue]", catalog["resources"])
    records = cast("list[dict[str, JsonValue]]", pool_links(resources))
    assert all(record["unresolved_elements"] == [] for record in records)
    selected = [
        edge
        for record in records
        for edge in cast("list[dict[str, JsonValue]]", record["edges"])
        if edge.get("selected") is True
    ]
    assert len(selected) == 212
    assert all(edge["runtime_version"] == "1.21.1" for edge in selected)


def test_limited_delegate_preserves_constraints_and_nested_source_links() -> None:
    element: dict[str, JsonValue] = {
        "element_type": "lithostitched:limited",
        "limit": 1,
        "min_depth": 2,
        "delegate": {
            "element_type": "minecraft:single_pool_element",
            "location": "village_taverns:village/plains/tavern",
            "processors": "minecraft:empty",
            "projection": "rigid",
        },
    }
    resource = row(
        "data/example/worldgen/template_pool/houses.json",
        {
            "elements": [{"weight": 5, "element": element}],
        },
    )
    result = cast("dict[str, JsonValue]", pool_links([resource])[0])
    pointer = "/elements/0/element"
    assert result["unresolved_elements"] == []
    assert result["edges"] == [
        {
            "kind": "pool_element_constraint",
            "pointer": pointer,
            "document": {
                "element_type": "lithostitched:limited",
                "limit": 1,
                "min_depth": 2,
            },
        },
        {
            "kind": "template",
            "id": "village_taverns:village/plains/tavern",
            "pointer": pointer + "/delegate/location",
        },
        {
            "kind": "processor_list",
            "id": "minecraft:empty",
            "pointer": pointer + "/delegate/processors",
        },
    ]
    trace = trace_pool("example:houses", [result], [])
    terminal = cast("list[dict[str, JsonValue]]", trace["terminal_edges"])
    assert terminal[0]["edge"] == cast("list[JsonValue]", result["edges"])[0]
    assert trace["missing"] == [
        {
            "kind": "template",
            "id": "village_taverns:village/plains/tavern",
        }
    ]
    element["delegate"] = {"element_type": "example:unsupported"}
    result = cast("dict[str, JsonValue]", pool_links([resource])[0])
    assert result["unresolved_elements"] == [
        {
            "pointer": pointer + "/delegate",
            "element_type": "example:unsupported",
            "reason": "unresolved element",
        }
    ]
    del element["delegate"]
    with pytest.raises(TypeError, match=r"invalid pool element.*delegate"):
        _ = pool_links([resource])
