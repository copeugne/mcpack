"""Source relationships used by the canonical Item 8 inventory."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pydantic import JsonValue


def resource_identity(path: str, kind: str, extension: str = ".json") -> tuple[str, str] | None:
    """Identify a resource exactly, preserving any optional-pack prefix."""
    parts = path.split("/")
    if "data" not in parts or not path.endswith(extension):
        return None
    anchor = parts.index("data")
    marker = kind.split("/")
    start = anchor + 2
    end = start + len(marker)
    if len(parts) <= end or parts[start:end] != marker:
        return None
    return (
        f"{parts[anchor + 1]}:{'/'.join(parts[end:]).removesuffix(extension)}",
        "/".join(parts[:anchor]),
    )


def structure_inputs(registry: tuple[str, ...], resources: list[JsonValue]) -> dict[str, JsonValue]:
    """Link each runtime structure to all packaged candidates, without choosing precedence."""
    definitions: dict[str, list[JsonValue]] = {}
    placements: dict[str, list[JsonValue]] = {}
    for resource in resources:
        if not isinstance(resource, dict) or not isinstance(resource.get("path"), str):
            message = "source catalog has an invalid resource row"
            raise TypeError(message)
        path = resource["path"]
        assert isinstance(path, str)  # noqa: S101 - explicit check above.
        identity = resource_identity(path, "worldgen/structure")
        if identity is not None:
            definitions.setdefault(identity[0], []).append(_reference(resource, identity))
        identity = resource_identity(path, "worldgen/structure_set")
        if identity is not None:
            _placements(resource, identity, placements)
    missing = set(registry) - definitions.keys()
    if missing:
        message = f"runtime structures lack packaged definitions: {sorted(missing)}"
        raise ValueError(message)
    rows: dict[str, JsonValue] = {
        identifier: {
            "packaged_definitions": definitions[identifier],
            "packaged_placement_sets": placements.get(identifier, []),
        }
        for identifier in registry
    }
    return {
        "registered_structures": rows,
        "unregistered_definitions": {
            identifier: definitions[identifier]
            for identifier in sorted(definitions.keys() - registry)
        },
    }


def _reference(resource: dict[str, JsonValue], identity: tuple[str, str]) -> dict[str, JsonValue]:
    return {
        "resource_id": identity[0],
        "pack_prefix": identity[1],
        "archive": resource["archive"],
        "path": resource["path"],
        "sha256": resource["sha256"],
    }


def _placements(
    resource: dict[str, JsonValue],
    identity: tuple[str, str],
    placements: dict[str, list[JsonValue]],
) -> None:
    document = resource["document"]
    if not isinstance(document, dict) or not isinstance(document.get("structures"), list):
        message = f"structure set has no usable structures list: {resource['path']}"
        raise TypeError(message)
    entries = document["structures"]
    assert isinstance(entries, list)  # noqa: S101 - explicit check above.
    for entry in entries:
        if not isinstance(entry, dict) or not isinstance(entry.get("structure"), str):
            message = f"structure set has an invalid member: {resource['path']}"
            raise TypeError(message)
        identifier = entry["structure"]
        assert isinstance(identifier, str)  # noqa: S101 - explicit check above.
        reference = _reference(resource, identity)
        reference["member"] = entry
        placements.setdefault(identifier, []).append(reference)


def size_variant_groups(registry: tuple[str, ...], resources: list[JsonValue]) -> list[JsonValue]:
    """Find same-provider jigsaw definitions differing only in expansion size."""
    candidates: dict[str, list[dict[str, JsonValue]]] = {}
    for resource in resources:
        if not isinstance(resource, dict) or not isinstance(resource.get("path"), str):
            message = "source catalog has an invalid resource row"
            raise TypeError(message)
        path = resource["path"]
        assert isinstance(path, str)  # noqa: S101 - explicit check above.
        identity = resource_identity(path, "worldgen/structure")
        if identity is not None and identity[0] in registry:
            candidates.setdefault(identity[0], []).append(resource)
    signatures: dict[str, list[dict[str, JsonValue]]] = {}
    for identifier, rows in sorted(candidates.items()):
        if len(rows) != 1:
            continue  # Competing definitions require effective-resource resolution first.
        row = rows[0]
        document = row["document"]
        if (
            not isinstance(document, dict)
            or type(document.get("size")) is not int
            or not isinstance(document.get("start_pool"), str)
        ):
            continue
        comparable = {key: value for key, value in document.items() if key != "size"}
        signature = json.dumps(
            [identifier.split(":")[0], row["archive"], comparable], sort_keys=True
        )
        signatures.setdefault(signature, []).append(
            {"structure_id": identifier, "size": document["size"], "source": row["path"]}
        )
    return [
        list(members)
        for members in signatures.values()
        if len({str(member["size"]) for member in members}) > 1
    ]
