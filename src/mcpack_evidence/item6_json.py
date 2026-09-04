"""Strict full-document JSON decoding for Item 6 evidence boundaries."""

from __future__ import annotations

import json
from math import isfinite
from typing import Final, Never, Self

from pydantic import JsonValue, TypeAdapter

_JSON_VALUE_ADAPTER: Final[TypeAdapter[JsonValue]] = TypeAdapter(JsonValue)


class StrictJsonError(ValueError):
    """Raised when evidence bytes are not strict JSON."""

    @classmethod
    def invalid(cls) -> Self:
        """Create the shared strict JSON diagnostic."""
        return cls("JSON is not strict")


def parse_strict_json(source: bytes) -> JsonValue:
    """Decode UTF-8 JSON while rejecting ambiguous object and number representations."""
    try:
        text = source.decode("utf-8")
    except UnicodeDecodeError as error:
        raise StrictJsonError.invalid() from error
    try:
        return _JSON_VALUE_ADAPTER.validate_python(
            json.loads(
                text,
                object_pairs_hook=_reject_duplicate_keys,
                parse_constant=_reject_nonstandard_constant,
                parse_float=_parse_finite_float,
            ),
            strict=True,
        )
    except (json.JSONDecodeError, StrictJsonError) as error:
        raise StrictJsonError.invalid() from error


def _reject_duplicate_keys(pairs: list[tuple[str, JsonValue]]) -> dict[str, JsonValue]:
    result: dict[str, JsonValue] = {}
    for key, value in pairs:
        if key in result:
            raise StrictJsonError.invalid()
        result[key] = value
    return result


def _reject_nonstandard_constant(value: str) -> Never:
    raise StrictJsonError.invalid() from ValueError(value)


def _parse_finite_float(value: str) -> float:
    parsed = float(value)
    if not isfinite(parsed):
        raise StrictJsonError.invalid()
    return parsed
