from __future__ import annotations

from typing import TYPE_CHECKING, cast

from mcpack_evidence.item8_pool_links import pool_links, template_links
from tests.item8.test_inventory_sources import row

if TYPE_CHECKING:
    from pydantic import JsonValue


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
