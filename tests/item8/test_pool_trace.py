from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from mcpack_evidence.item8_pool_trace import trace_pool

if TYPE_CHECKING:
    from pydantic import JsonValue


def link(identifier: str, edges: list[JsonValue]) -> dict[str, JsonValue]:
    return {"id": identifier, "edges": edges, "unresolved_elements": []}


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
