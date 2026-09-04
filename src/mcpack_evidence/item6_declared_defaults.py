# ruff: noqa: EM101, TRY003
"""Validate source-declared defaults that differ from frozen generated values."""

from __future__ import annotations

import json
from math import isfinite
from typing import Final, TypedDict

from pydantic import TypeAdapter, ValidationError

Scalar = bool | int | float | str


class UpstreamDefault(TypedDict):
    """One source-declared default bound to an exact comment line."""

    value: Scalar
    line: int
    prefix: str
    suffix: str


_SCALAR_ADAPTER: Final[TypeAdapter[Scalar]] = TypeAdapter(Scalar)
_REQUIRED: Final = {
    ("config/towns_and_towers/structure_rarity_new.json5", "towers.separation"): 24,
    ("config/towns_and_towers/structure_rarity_new.json5", "towns.separation"): 24,
    ("config/towns_and_towers/structure_rarity_new.json5", "towns.spacing"): 48,
}


class DeclaredDefaultValidationError(ValueError):
    """Raised when source-declared default evidence is incomplete or inconsistent."""


def _decode_default_scalar(raw: str) -> Scalar:
    """Decode one finite strict JSON scalar."""
    try:
        decoded = _SCALAR_ADAPTER.validate_json(raw, strict=True)
    except (json.JSONDecodeError, ValidationError) as error:
        raise DeclaredDefaultValidationError(
            "declared default evidence does not match source"
        ) from error
    if isinstance(decoded, float) and not isfinite(decoded):
        raise DeclaredDefaultValidationError("declared default evidence does not match source")
    return decoded


def validate_upstream_default(
    upstream_default: UpstreamDefault | None,
    relative: str,
    key: str,
    source_lines: list[str],
) -> Scalar | None:
    """Bind one required or supplied upstream default to preserved source text."""
    required = _REQUIRED.get((relative, key))
    if required is not None and upstream_default is None:
        raise DeclaredDefaultValidationError("setting surface requires declared default evidence")
    if upstream_default is None:
        return None
    line = upstream_default["line"]
    if line < 1 or line > len(source_lines):
        raise DeclaredDefaultValidationError("declared default evidence does not match source")
    source = source_lines[line - 1].strip()
    prefix = upstream_default["prefix"]
    suffix = upstream_default["suffix"]
    end = len(source) - len(suffix) if suffix else len(source)
    if not source.startswith(prefix) or not source.endswith(suffix) or len(prefix) > end:
        raise DeclaredDefaultValidationError("declared default evidence does not match source")
    declared = _decode_default_scalar(source[len(prefix) : end])
    if (
        type(declared) is not type(upstream_default["value"])
        or declared != upstream_default["value"]
    ):
        raise DeclaredDefaultValidationError("declared default evidence does not match source")
    if required is not None and declared != required:
        raise DeclaredDefaultValidationError("declared default evidence does not match source")
    return declared
