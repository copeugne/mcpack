"""Select the known frozen resource layers while retaining excluded candidates."""

from __future__ import annotations

import re
from typing import TYPE_CHECKING, Literal

from .item8_inventory import resource_identity

if TYPE_CHECKING:
    from pydantic import JsonValue

LITHOSTITCHED = "lithostitched-1.7.10+beta4-neoforge-21.1.jar"
_OVERLAY = "overlay.breaks_seed_parity"
_VANILLA = "minecraft-server-1.21.1.jar!/META-INF/versions/1.21.1/server-1.21.1.jar"


def runtime_mod_ids(log: str) -> dict[str, int]:
    """Read the captured NeoForge mod list, retaining one-based source lines."""
    lines = log.splitlines()
    headers = [i for i, line in enumerate(lines) if line.strip() == "Mod List:"]
    if len(headers) != 1:
        message = "expected exactly one NeoForge Mod List block"
        raise ValueError(message)
    result: dict[str, int] = {}
    for index in range(headers[0] + 1, len(lines)):
        line = lines[index]
        if not line.strip() or line.strip() == "Name Version (Mod Id)":
            continue
        if line.startswith("["):
            break
        match = re.fullmatch(r"\t\t.+ \(([a-z0-9_]+)\)", line)
        if match is None or match[1] in result:
            message = f"invalid or duplicate NeoForge mod-list row at line {index + 1}"
            raise ValueError(message)
        result[match[1]] = index + 1
    else:
        message = "unterminated NeoForge Mod List block"
        raise ValueError(message)
    if not result:
        message = "empty NeoForge Mod List block"
        raise ValueError(message)
    return result


def mod_conditions_match(conditions: JsonValue, loaded_mods: set[str]) -> bool:
    """Evaluate the two observed NeoForge conditions; reject unsupported forms.

    Semantics are retained in evidence/item-8/sources/neoforge-condition-code.
    Evaluate every branch so an unknown condition cannot hide behind a true OR.
    """
    if not isinstance(conditions, list):
        message = "NeoForge conditions must be a list"
        raise TypeError(message)
    matches: list[bool] = []
    for condition in conditions:
        if not isinstance(condition, dict):
            message = "invalid NeoForge condition"
            raise TypeError(message)
        if condition.get("type") == "neoforge:mod_loaded" and set(condition) == {"type", "modid"}:
            identifier = condition["modid"]
            if not isinstance(identifier, str):
                message = "mod_loaded condition requires a string modid"
                raise TypeError(message)
            matches.append(identifier in loaded_mods)
        elif condition.get("type") == "neoforge:or" and set(condition) == {"type", "values"}:
            values = condition["values"]
            if not isinstance(values, list):
                message = "NeoForge OR values must be a list"
                raise TypeError(message)
            branches = [mod_conditions_match([value], loaded_mods) for value in values]
            matches.append(any(branches))
        else:
            message = f"unsupported NeoForge condition: {condition}"
            raise ValueError(message)
    return all(matches)


def select_resources(
    resources: list[JsonValue],
    kind: Literal[
        "worldgen/structure",
        "worldgen/template_pool",
        "structure",
        "lithostitched/worldgen_modifier",
        "lithostitched/surface_rule",
        "worldgen/placed_feature",
        "worldgen/configured_feature",
        "loot_table",
    ],
    *,
    enabled_packs: list[str],
    lithostitched_overlay: bool,
) -> tuple[dict[str, dict[str, JsonValue]], list[JsonValue]]:
    """Select root resources and the verified Lithostitched overlay; reject unknown collisions."""
    if not {"vanilla", "mod_data"}.issubset(enabled_packs) or enabled_packs.index(
        "vanilla"
    ) >= enabled_packs.index("mod_data"):
        message = "resource selection requires the recorded mod_data priority after vanilla"
        raise ValueError(message)
    candidates: dict[str, list[dict[str, JsonValue]]] = {}
    excluded: list[JsonValue] = []
    extension = ".nbt" if kind == "structure" else ".json"
    for row in resources:
        if not isinstance(row, dict) or not isinstance(row.get("path"), str):
            message = "invalid packaged resource row"
            raise TypeError(message)
        path = row["path"]
        assert isinstance(path, str)  # noqa: S101 - explicit validation above.
        identity = resource_identity(path, kind, extension)
        if identity is None:
            continue
        identifier, prefix = identity
        if prefix:
            if row["archive"] != LITHOSTITCHED or prefix != _OVERLAY:
                excluded.append(_excluded(identifier, row, "unresolved non-root pack prefix"))
                continue
            if not lithostitched_overlay:
                excluded.append(_excluded(identifier, row, "Lithostitched overlay disabled"))
                continue
        candidates.setdefault(identifier, []).append(row)
    selected: dict[str, dict[str, JsonValue]] = {}
    for identifier, rows in sorted(candidates.items()):
        if len(rows) == 1:
            selected[identifier] = rows[0]
            continue
        chosen = _override(identifier, rows, kind)
        selected[identifier] = chosen
        excluded.extend(
            _excluded(identifier, row, "overridden by mod_data")
            for row in rows
            if row is not chosen
        )
    return selected, excluded


def _override(identifier: str, rows: list[dict[str, JsonValue]], kind: str) -> dict[str, JsonValue]:
    owners = {str(row["archive"]) for row in rows}
    if len(rows) == 2 and len(owners) == 2 and _VANILLA in owners:  # noqa: PLR2004 - one mod replaces vanilla.
        return next(row for row in rows if row["archive"] != _VANILLA)
    message = f"unresolved competing resource definitions: {kind} {identifier}"
    raise ValueError(message)


def _excluded(identifier: str, row: dict[str, JsonValue], reason: str) -> dict[str, JsonValue]:
    return {
        "id": identifier,
        "archive": row["archive"],
        "path": row["path"],
        "sha256": row["sha256"],
        "reason": reason,
    }
