from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from mcpack_evidence.item8_biomes import biome_constraint, structure_biomes

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
