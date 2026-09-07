from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from mcpack_evidence.item8_biomes import (
    biome_constraint,
    structure_biomes,
    supplementaries_tag_inputs,
)

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_unresolved_optional_contribution_propagates_to_structure() -> None:
    tags: dict[str, JsonValue] = {
        "example:root": {
            "values": ["minecraft:plains", {"id": "#example:conditional", "required": False}],
            "unresolved": [],
        },
        "example:conditional": {"values": None, "unresolved": ["unverified condition"]},
    }
    result = biome_constraint("#example:root", tags, frozenset({"minecraft:plains"}))
    assert result["biomes"] is None
    assert result["unresolved_tags"] == ["example:conditional"]


def test_known_tag_filters_optional_biomes_and_invalid_required_values_fail() -> None:
    tags: dict[str, JsonValue] = {
        "example:root": {
            "values": ["minecraft:plains", {"id": "absent:forest", "required": False}],
            "unresolved": [],
        }
    }
    registered = frozenset({"minecraft:plains"})
    assert biome_constraint("#example:root", tags, registered)["biomes"] == ["minecraft:plains"]
    result = biome_constraint(["minecraft:plains", "absent:forest"], tags, registered)
    assert result["biomes"] is None
    assert result["missing_required"] == ["absent:forest"]


def test_registered_structure_requires_unique_definition_and_complete_coverage() -> None:
    row: JsonValue = {
        "path": "data/example/worldgen/structure/tower.json",
        "document": {"biomes": "minecraft:plains"},
    }
    registered = frozenset({"minecraft:plains"})
    result = structure_biomes(("example:tower",), [row], {}, registered)
    assert set(result) == {"example:tower"}
    with pytest.raises(ValueError, match="unique"):
        _ = structure_biomes(("example:tower",), [row, row], {}, registered)
    with pytest.raises(ValueError, match="lacks"):
        _ = structure_biomes(("example:tower",), [], {}, registered)


@pytest.mark.parametrize("parents_enabled", [True, False])
def test_dynamic_tags_require_parent_features_and_publish_empty_tags_when_disabled(
    parents_enabled: bool,
) -> None:
    config: dict[str, JsonValue] = {
        "building": {"way_sign": {"enabled": parents_enabled, "road_signs": {"enabled": True}}},
        "functional": {
            "cannon": {
                "enabled": parents_enabled,
                "plunderer": {"enabled": True, "galleon": True},
            }
        },
    }
    tags = supplementaries_tag_inputs(config, {"config": "a" * 64})
    registered = frozenset({"minecraft:plains", "minecraft:ocean"})
    tags["minecraft:is_overworld"] = {"values": ["minecraft:plains"], "unresolved": []}
    tags["minecraft:is_ocean"] = {"values": ["minecraft:ocean"], "unresolved": []}
    assert biome_constraint("#supplementaries:has_road_signs", tags, registered)["biomes"] == (
        ["minecraft:plains"] if parents_enabled else []
    )
    assert biome_constraint("#supplementaries:has_galleons", tags, registered)["biomes"] == (
        ["minecraft:ocean"] if parents_enabled else []
    )
