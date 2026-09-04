from __future__ import annotations

from typing import TYPE_CHECKING, cast

import pytest

from mcpack_evidence.item8_inventory import resource_identity, size_variant_groups, structure_inputs

if TYPE_CHECKING:
    from pydantic import JsonValue


def row(path: str, document: JsonValue = None) -> dict[str, JsonValue]:
    return {"archive": "test.jar", "path": path, "sha256": "a" * 64, "document": document}


def test_resource_identity_does_not_confuse_tags_pools_or_pieces() -> None:
    for path in (
        "data/example/tags/worldgen/structure/tower.json",
        "data/example/worldgen/template_pool/tower.json",
        "data/example/structure/tower.nbt",
    ):
        assert resource_identity(path, "worldgen/structure") is None
    assert resource_identity(
        "optional/data/example/worldgen/structure/nested/tower.json", "worldgen/structure"
    ) == ("example:nested/tower", "optional")


def test_preserves_competing_optional_and_unregistered_definitions() -> None:
    resources: list[JsonValue] = [
        row("data/example/worldgen/structure/tower.json", {}),
        row("optional/data/example/worldgen/structure/tower.json", {}),
        row("data/example/worldgen/structure/unused.json", {}),
        row(
            "data/example/worldgen/structure_set/towers.json",
            {"structures": [{"structure": "example:tower", "weight": 2}]},
        ),
    ]
    result = structure_inputs(("example:tower",), resources)
    registered = cast("dict[str, dict[str, JsonValue]]", result["registered_structures"])
    definitions = cast(
        "list[dict[str, JsonValue]]", registered["example:tower"]["packaged_definitions"]
    )
    assert [definition["pack_prefix"] for definition in definitions] == ["", "optional"]
    placements = cast(
        "list[dict[str, JsonValue]]", registered["example:tower"]["packaged_placement_sets"]
    )
    assert placements[0]["member"] == {"structure": "example:tower", "weight": 2}
    assert "example:unused" in cast("dict[str, JsonValue]", result["unregistered_definitions"])


def test_missing_runtime_structure_is_not_silently_omitted() -> None:
    with pytest.raises(ValueError, match="lack packaged definitions"):
        _ = structure_inputs(("example:missing",), [])


def test_size_grouping_requires_same_content_and_unambiguous_sources() -> None:
    resources: list[JsonValue] = [
        row(f"data/example/worldgen/structure/{name}.json", cast("JsonValue", document))
        for name, document in (
            ("small", {"size": 4, "start_pool": "example:town", "biomes": "#example:plains"}),
            ("large", {"size": 6, "start_pool": "example:town", "biomes": "#example:plains"}),
            ("other", {"size": 6, "start_pool": "example:town", "biomes": "#example:desert"}),
        )
    ]
    registry = ("example:small", "example:large", "example:other")
    groups = size_variant_groups(registry, resources)
    assert len(groups) == 1
    members = cast("list[dict[str, JsonValue]]", groups[0])
    assert {str(member["structure_id"]) for member in members} == {"example:small", "example:large"}
    resources.append(row("optional/data/example/worldgen/structure/small.json", {}))
    assert size_variant_groups(registry, resources) == []
