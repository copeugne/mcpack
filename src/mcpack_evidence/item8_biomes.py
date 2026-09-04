"""Resolve structure biome references without concealing uncertain tag contributions."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

from .item7_restrictions import resolve_biome_tag
from .item8_inventory import resource_identity

if TYPE_CHECKING:
    from pydantic import JsonValue


def supplementaries_tag_inputs(
    config: dict[str, JsonValue], evidence: dict[str, str]
) -> dict[str, JsonValue]:
    """Derive the two inspected dynamic tags, including parent feature toggles."""
    paths = {
        "supplementaries:has_road_signs": (
            "minecraft:is_overworld",
            ("building.way_sign.enabled", "building.way_sign.road_signs.enabled"),
        ),
        "supplementaries:has_galleons": (
            "minecraft:is_ocean",
            (
                "functional.cannon.enabled",
                "functional.cannon.plunderer.enabled",
                "functional.cannon.plunderer.galleon",
            ),
        ),
    }
    result: dict[str, JsonValue] = {}
    for identifier, (target, switches) in paths.items():
        enabled = True
        for path in switches:
            value: JsonValue = config
            for part in path.split("."):
                if not isinstance(value, dict) or part not in value:
                    message = f"missing Supplementaries feature setting: {path}"
                    raise ValueError(message)
                value = value[part]
            if type(value) is not bool:
                message = f"non-boolean Supplementaries feature setting: {path}"
                raise TypeError(message)
            enabled = enabled and value
        result[identifier] = {
            "sources": [{"kind": "derived_dynamic_tag", "evidence": dict(evidence)}],
            "values": [f"#{target}"] if enabled else [],
            "unresolved": [],
            "feature_settings": cast("JsonValue", list(switches)),
        }
    return result


def structure_biomes(
    registry: tuple[str, ...],
    resources: list[JsonValue],
    tag_inputs: dict[str, JsonValue],
    registered_biomes: frozenset[str],
) -> dict[str, JsonValue]:
    """Resolve uniquely packaged registered definitions against the frozen biome registry."""
    result: dict[str, JsonValue] = {}
    for raw in resources:
        row = cast("dict[str, JsonValue]", raw)
        identity = resource_identity(str(row["path"]), "worldgen/structure")
        if identity is None or identity[0] not in registry:
            continue
        identifier, prefix = identity
        if prefix or identifier in result:
            message = f"structure biome resolution needs a unique root definition: {identifier}"
            raise ValueError(message)
        document = cast("dict[str, JsonValue]", row["document"])
        result[identifier] = biome_constraint(document["biomes"], tag_inputs, registered_biomes)
    if set(result) != set(registry):
        message = "structure biome resolution lacks registered definitions"
        raise ValueError(message)
    return result


def biome_constraint(  # noqa: C901 - explicit unknown contribution and missing registry handling.
    reference: JsonValue, tag_inputs: dict[str, JsonValue], registered_biomes: frozenset[str]
) -> dict[str, JsonValue]:
    """Keep missing required values distinct from unknown optional tag contributions."""
    entries = [reference] if isinstance(reference, str) else reference
    if not isinstance(entries, list) or any(not isinstance(item, str) for item in entries):
        message = "unsupported structure biome reference"
        raise TypeError(message)
    pending = [str(item)[1:] for item in entries if str(item).startswith("#")]
    visited: set[str] = set()
    unresolved: set[str] = set()
    tags: dict[str, list[object]] = {}
    while pending:
        tag = pending.pop()
        if tag in visited:
            continue
        visited.add(tag)
        if tag not in tag_inputs:
            continue  # The existing resolver distinguishes missing required/optional tags.
        row = cast("dict[str, JsonValue]", tag_inputs[tag])
        if row["unresolved"] or row["values"] is None:
            unresolved.add(tag)
            continue
        values = cast("list[object]", row["values"])
        tags[tag] = values
        for value in values:
            member = (
                cast("dict[str, object]", value).get("id") if isinstance(value, dict) else value
            )
            if isinstance(member, str) and member.startswith("#"):
                pending.append(member[1:])
    biomes: set[str] = set()
    missing: set[str] = set()
    if not unresolved:
        for item in entries:
            value = str(item)
            if value.startswith("#"):
                resolved, absent = resolve_biome_tag(
                    value[1:], tags, registered_biomes=registered_biomes
                )
                biomes.update(resolved)
                missing.update(absent)
            elif value in registered_biomes:
                biomes.add(value)
            else:
                missing.add(value)
    return {
        "reference": reference,
        "biomes": cast("JsonValue", sorted(biomes)) if not (missing or unresolved) else None,
        "missing_required": cast("JsonValue", sorted(missing)),
        "unresolved_tags": cast("JsonValue", sorted(unresolved)),
        "referenced_tags": cast("JsonValue", sorted(visited)),
    }
