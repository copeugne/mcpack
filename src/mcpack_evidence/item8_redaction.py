"""Omit authored identities and credentials from publishable source catalogs."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pydantic import JsonValue

_OMITTED = "<redacted-authored-identity-or-credential>"
_FIELDS = frozenset(
    {"owner", "ownername", "skullowner", "profile", "minecraft:profile", "password"}
)


def redact_authored_fields(value: JsonValue, paths: list[str], path: str = "") -> JsonValue:
    """Retain field presence and omission paths without publishing identity values."""
    if isinstance(value, dict):
        result: dict[str, JsonValue] = {}
        for key, child in value.items():
            pointer = path + "/" + key.replace("~", "~0").replace("/", "~1")
            if key.lower() in _FIELDS or "uuid" in key.lower():
                result[key] = _OMITTED
                paths.append(pointer)
            else:
                result[key] = redact_authored_fields(child, paths, pointer)
        return result
    if isinstance(value, list):
        return [
            redact_authored_fields(child, paths, f"{path}/{index}")
            for index, child in enumerate(value)
        ]
    return value
