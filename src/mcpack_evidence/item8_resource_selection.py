"""Select the known frozen resource layers while retaining excluded candidates."""

from __future__ import annotations

from typing import TYPE_CHECKING, Literal

from .item8_inventory import resource_identity

if TYPE_CHECKING:
    from pydantic import JsonValue

LITHOSTITCHED = "lithostitched-1.7.10+beta4-neoforge-21.1.jar"
_OVERLAY = "overlay.breaks_seed_parity"
_VANILLA = "minecraft-server-1.21.1.jar!/META-INF/versions/1.21.1/server-1.21.1.jar"


def select_resources(
    resources: list[JsonValue],
    kind: Literal["worldgen/structure", "worldgen/template_pool", "structure"],
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
