"""Trace possible selected pool/template contents without simulating assembly."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

if TYPE_CHECKING:
    from pydantic import JsonValue


def trace_pool(
    start_pool: str,
    pools: list[JsonValue],
    templates: list[JsonValue],
) -> dict[str, JsonValue]:
    """Walk selected resources, retaining terminal edges and missing references.

    Inputs must already be selected for the frozen runtime. Fallback and jigsaw
    links give possible content, not placement probabilities or assembled bounds.
    Alias IDs remain missing until resolved in the owning structure's context.
    """
    indexes = {"pool": _index(pools), "template": _index(templates)}
    pending = [("pool", start_pool)]
    visited: set[tuple[str, str]] = set()
    missing: set[tuple[str, str]] = set()
    terminal: list[JsonValue] = []
    unresolved: list[JsonValue] = []
    while pending:
        kind, identifier = pending.pop()
        if (kind, identifier) in visited:
            continue
        visited.add((kind, identifier))
        resource = indexes[kind].get(identifier)
        if resource is None:
            missing.add((kind, identifier))
            continue
        unresolved.extend(
            {"kind": kind, "id": identifier, "problem": problem}
            for problem in cast("list[JsonValue]", resource["unresolved_elements"])
        )
        for raw_edge in cast("list[JsonValue]", resource["edges"]):
            edge = cast("dict[str, JsonValue]", raw_edge)
            if edge.get("selected") is False:
                continue
            target_kind = str(edge["kind"])
            if target_kind in indexes:
                pending.append((target_kind, str(edge["id"])))
            else:
                terminal.append({"kind": kind, "id": identifier, "edge": edge})
    return {
        "start_pool": start_pool,
        "pools": [identifier for kind, identifier in sorted(visited - missing) if kind == "pool"],
        "templates": [
            identifier for kind, identifier in sorted(visited - missing) if kind == "template"
        ],
        "missing": [{"kind": kind, "id": identifier} for kind, identifier in sorted(missing)],
        "terminal_edges": terminal,
        "unresolved_elements": unresolved,
    }


def _index(resources: list[JsonValue]) -> dict[str, dict[str, JsonValue]]:
    result: dict[str, dict[str, JsonValue]] = {}
    for resource in resources:
        if (
            not isinstance(resource, dict)
            or not isinstance(resource.get("id"), str)
            or not isinstance(resource.get("edges"), list)
            or not isinstance(resource.get("unresolved_elements"), list)
        ):
            message = "trace input is not a pool/template link record"
            raise TypeError(message)
        identifier = str(resource["id"])
        if identifier in result:
            message = f"trace requires selected resources, found duplicate: {identifier}"
            raise ValueError(message)
        result[identifier] = resource
    return result
