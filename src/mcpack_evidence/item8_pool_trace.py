"""Trace possible selected pool/template contents without simulating assembly."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

if TYPE_CHECKING:
    from pydantic import JsonValue


def trace_pool(
    start_pool: str,
    pools: list[JsonValue],
    templates: list[JsonValue],
    pool_aliases: JsonValue = None,
    pool_alias_tags: dict[str, list[str]] | None = None,
) -> dict[str, JsonValue]:
    """Walk selected resources, retaining terminal edges and missing references.

    Inputs must already be selected for the frozen runtime. Fallback and jigsaw
    links give possible content, not placement probabilities or assembled bounds.
    Alias alternatives are unioned, not sampled. Correlated groups remain in the
    source definition; this trace makes no joint occurrence or probability claim.
    """
    indexes = {"pool": _index(pools), "template": _index(templates)}
    aliases = alias_targets(pool_aliases, pool_alias_tags)
    pending = [("pool", start_pool)]
    visited: set[tuple[str, str]] = set()
    missing: set[tuple[str, str]] = set()
    terminal: list[JsonValue] = []
    unresolved: list[JsonValue] = []
    while pending:
        kind, identifier = pending.pop()
        if kind == "pool" and identifier in aliases:
            if ("alias", identifier) not in visited:
                visited.add(("alias", identifier))
                pending.extend(("pool", target) for target in sorted(aliases[identifier]))
            continue
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
    result: dict[str, JsonValue] = {
        "start_pool": start_pool,
        "pools": [identifier for kind, identifier in sorted(visited - missing) if kind == "pool"],
        "templates": [
            identifier for kind, identifier in sorted(visited - missing) if kind == "template"
        ],
        "missing": [{"kind": kind, "id": identifier} for kind, identifier in sorted(missing)],
        "terminal_edges": terminal,
        "unresolved_elements": unresolved,
    }
    if aliases:
        result["resolved_aliases"] = {
            identifier: cast("JsonValue", sorted(aliases[identifier]))
            for kind, identifier in sorted(visited)
            if kind == "alias"
        }
    return result


def alias_targets(  # noqa: C901, PLR0912 - explicit observed alias codecs.
    bindings: JsonValue, pool_tags: dict[str, list[str]] | None = None
) -> dict[str, set[str]]:
    """Collect declared positive-weight targets of the packaged vanilla alias shapes."""
    result: dict[str, set[str]] = {}
    if bindings is None:
        return result
    if not isinstance(bindings, list):
        message = "pool aliases must be a list"
        raise TypeError(message)
    for binding in bindings:
        if not isinstance(binding, dict):
            message = "invalid pool alias binding"
            raise TypeError(message)
        kind = binding.get("type")
        if kind == "lithostitched:internal/random_entries":
            for alias, targets in _random_entries(binding, pool_tags or {}).items():
                result.setdefault(alias, set()).update(targets)
            continue
        if kind == "minecraft:random_group":
            for group in _weighted(binding.get("groups")):
                for alias, targets in alias_targets(group, pool_tags).items():
                    result.setdefault(alias, set()).update(targets)
            continue
        alias = binding.get("alias")
        if not isinstance(alias, str):
            message = "pool alias binding lacks its ID"
            raise TypeError(message)
        if kind == "minecraft:direct":
            targets = [binding.get("target")]
        elif kind == "minecraft:random":
            targets = _weighted(binding.get("targets"))
        else:
            message = f"unsupported pool alias binding: {kind}"
            raise ValueError(message)
        for target in targets:
            if not isinstance(target, str):
                message = f"invalid pool alias target: {alias}"
                raise TypeError(message)
            result.setdefault(alias, set()).add(target)
    return result


def _random_entries(
    binding: dict[str, JsonValue], pool_tags: dict[str, list[str]]
) -> dict[str, set[str]]:
    aliases, pools = binding.get("aliases"), binding.get("pools")
    if not isinstance(aliases, list) or not isinstance(pools, list) or len(aliases) != len(pools):
        message = "random_entries requires matching alias and holder-set lists"
        raise ValueError(message)
    result: dict[str, set[str]] = {}
    sizes: set[int] = set()
    for alias, pool in zip(aliases, pools, strict=True):
        if not isinstance(alias, str) or not isinstance(pool, str) or not pool.startswith("#"):
            message = "unsupported random_entries alias or holder-set form"
            raise ValueError(message)
        values = pool_tags.get(pool[1:])
        if not values:
            message = f"missing or empty random_entries pool tag: {pool}"
            raise ValueError(message)
        sizes.add(len(values))
        result[alias] = set(values)
    if len(sizes) != 1:
        message = "random_entries holder sets cannot share an index across unequal lengths"
        raise ValueError(message)
    return result


def _weighted(value: JsonValue) -> list[JsonValue]:
    if not isinstance(value, list):
        message = "weighted alias alternatives must be a list"
        raise TypeError(message)
    result: list[JsonValue] = []
    for entry in value:
        if (
            not isinstance(entry, dict)
            or type(entry.get("weight")) is not int
            or "data" not in entry
        ):
            message = "invalid weighted alias alternative"
            raise TypeError(message)
        weight = cast("int", entry["weight"])
        if weight < 0:
            message = "negative alias weight"
            raise ValueError(message)
        if weight:
            result.append(entry["data"])
    return result


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
