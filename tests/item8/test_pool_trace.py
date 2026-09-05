from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from mcpack_evidence.item8_pool_trace import alias_targets, trace_pool

if TYPE_CHECKING:
    from pydantic import JsonValue


def link(identifier: str, edges: list[JsonValue]) -> dict[str, JsonValue]:
    return {"id": identifier, "edges": edges, "unresolved_elements": []}


def test_random_entries_trace_uses_merged_tags_without_flattening_raw_bindings() -> None:
    bindings: JsonValue = [{
        "type": "lithostitched:internal/random_entries",
        "aliases": ["example:ranged", "example:slow"],
        "pools": ["#example:ranged", "#example:slow"],
    }]
    tags = {"example:ranged": ["example:skeleton", "example:stray"],
            "example:slow": ["example:slow_skeleton", "example:slow_stray"]}
    assert alias_targets(bindings, tags) == {
        "example:ranged": {"example:skeleton", "example:stray"},
        "example:slow": {"example:slow_skeleton", "example:slow_stray"},
    }
    result = trace_pool("example:ranged", [], [], bindings, tags)
    assert result["missing"] == [
        {"kind": "pool", "id": "example:skeleton"},
        {"kind": "pool", "id": "example:stray"},
    ]
    assert bindings == [{
        "type": "lithostitched:internal/random_entries",
        "aliases": ["example:ranged", "example:slow"],
        "pools": ["#example:ranged", "#example:slow"],
    }]
    with pytest.raises(ValueError, match="missing or empty"):
        _ = alias_targets(bindings, {})
    with pytest.raises(ValueError, match="unequal lengths"):
        _ = alias_targets(bindings, {**tags, "example:slow": ["example:slow_skeleton"]})


def test_cycles_versions_missing_and_non_template_content_are_preserved() -> None:
    pools: list[JsonValue] = [
        link(
            "example:start",
            [
                {"kind": "pool", "id": "example:start"},
                {"kind": "template", "id": "example:old", "selected": False},
                {"kind": "template", "id": "example:current", "selected": True},
                {"kind": "processor_list", "id": "example:processor"},
                {"kind": "inline_placed_feature", "document": {"type": "example:boat"}},
            ],
        )
    ]
    templates: list[JsonValue] = [
        link(
            "example:current",
            [
                {"kind": "pool", "id": "example:start"},
                {"kind": "pool", "id": "example:alias"},
            ],
        )
    ]
    result = trace_pool("example:start", pools, templates)
    assert result["pools"] == ["example:start"]
    assert result["templates"] == ["example:current"]
    assert result["missing"] == [{"kind": "pool", "id": "example:alias"}]
    assert result["terminal_edges"] == [
        {
            "kind": "pool",
            "id": "example:start",
            "edge": {"kind": "processor_list", "id": "example:processor"},
        },
        {
            "kind": "pool",
            "id": "example:start",
            "edge": {"kind": "inline_placed_feature", "document": {"type": "example:boat"}},
        },
    ]


def test_competing_resources_and_unknown_codecs_cannot_silently_pass() -> None:
    pool = link("example:start", [])
    pool["unresolved_elements"] = [{"reason": "custom codec"}]
    result = trace_pool("example:start", [pool], [])
    assert result["unresolved_elements"] == [
        {"kind": "pool", "id": "example:start", "problem": {"reason": "custom codec"}}
    ]
    with pytest.raises(ValueError, match="duplicate"):
        _ = trace_pool("example:start", [pool, pool], [])


def test_aliases_preserve_possible_group_targets_without_counting_aliases_as_pools() -> None:
    bindings: list[JsonValue] = [
        {
            "type": "minecraft:random_group",
            "groups": [
                {
                    "weight": 1,
                    "data": [
                        {"type": "minecraft:direct", "alias": "example:a", "target": "example:b"}
                    ],
                },
                {
                    "weight": 2,
                    "data": [
                        {"type": "minecraft:direct", "alias": "example:a", "target": "example:c"}
                    ],
                },
            ],
        },
        {
            "type": "minecraft:random",
            "alias": "example:d",
            "targets": [
                {"data": "example:c", "weight": 1},
                {"data": "example:disabled", "weight": 0},
            ],
        },
    ]
    assert alias_targets(bindings) == {
        "example:a": {"example:b", "example:c"},
        "example:d": {"example:c"},
    }
    result = trace_pool(
        "example:a",
        [
            link("example:a", [{"kind": "template", "id": "example:shadowed"}]),
            link("example:b", [{"kind": "pool", "id": "example:d"}]),
            link("example:c", [{"kind": "pool", "id": "example:a"}]),
        ],
        [],
        bindings,
    )
    assert result["pools"] == ["example:b", "example:c"]
    assert result["resolved_aliases"] == {
        "example:a": ["example:b", "example:c"],
        "example:d": ["example:c"],
    }
    assert result["missing"] == []


def test_unknown_alias_shape_fails_instead_of_omitting_targets() -> None:
    with pytest.raises(ValueError, match="unsupported pool alias"):
        _ = alias_targets([{"type": "custom:alias", "alias": "example:a"}])
