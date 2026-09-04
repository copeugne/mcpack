"""Strict byte-preserving sanitization for the captured generated credential."""

from __future__ import annotations

import json
import re
from math import isfinite
from typing import Final, Never, Self

from pydantic import JsonValue, TypeAdapter, ValidationError

_PASSWORD_MEMBER: Final = re.compile(r'"password"\s*:\s*("(?:[^"\\]|\\.)*")')
_REDACTION_SENTINEL: Final = "<redacted-generated-secret>"
_JSON_VALUE_ADAPTER: Final[TypeAdapter[JsonValue]] = TypeAdapter(JsonValue)
_JSON_STRING_ADAPTER: Final = TypeAdapter(str)


class SourceSanitizationError(ValueError):
    """Raised when source JSON cannot be safely redacted in place."""

    @classmethod
    def invalid_json(cls) -> Self:
        """Create the strict source JSON failure."""
        return cls("source configuration is not strict JSON")

    @classmethod
    def lexical_target(cls) -> Self:
        """Create the noncanonical password-token failure."""
        return cls("generated credential has no sole canonical password token")

    @classmethod
    def target_type(cls) -> Self:
        """Create the target type failure."""
        return cls("generated credential must be a JSON string")

    @classmethod
    def target_path(cls) -> Self:
        """Create the required target path failure."""
        return cls("generated credential path is absent")


def redact_generated_credential(source: bytes) -> bytes:
    """Replace exactly one verified canonical credential string token."""
    try:
        text = source.decode("utf-8")
        configuration = _parse_strict_json(text)
    except (UnicodeDecodeError, json.JSONDecodeError, ValueError) as error:
        raise SourceSanitizationError.invalid_json() from error
    password = _require_string_credential(configuration)
    matches = tuple(_PASSWORD_MEMBER.finditer(text))
    if len(matches) != 1:
        raise SourceSanitizationError.lexical_target()
    match = matches[0]
    try:
        matched_password = _JSON_STRING_ADAPTER.validate_json(match.group(1))
    except ValidationError as error:
        raise SourceSanitizationError.lexical_target() from error
    if matched_password != password:
        raise SourceSanitizationError.lexical_target()
    start, end = match.span(1)
    replacement = json.dumps(_REDACTION_SENTINEL, ensure_ascii=False).encode()
    return source[:start] + replacement + source[end:]


def _parse_strict_json(source: str) -> JsonValue:
    """Parse JSON while rejecting duplicate keys, constants, and float overflow."""
    return _JSON_VALUE_ADAPTER.validate_python(
        json.loads(
            source,
            object_pairs_hook=_reject_duplicate_keys,
            parse_constant=_reject_nonstandard_constant,
            parse_float=_parse_finite_float,
        ),
        strict=True,
    )


def _reject_duplicate_keys(pairs: list[tuple[str, JsonValue]]) -> dict[str, JsonValue]:
    """Construct one object only when every JSON member name is unique."""
    result: dict[str, JsonValue] = {}
    for key, value in pairs:
        if key in result:
            raise SourceSanitizationError.invalid_json()
        result[key] = value
    return result


def _reject_nonstandard_constant(value: str) -> Never:
    """Reject JavaScript-style numeric constants not permitted by JSON."""
    raise SourceSanitizationError.invalid_json() from ValueError(value)


def _parse_finite_float(value: str) -> float:
    """Parse one JSON floating number only when it stays finite."""
    parsed = float(value)
    if not isfinite(parsed):
        raise SourceSanitizationError.invalid_json()
    return parsed


def _require_string_credential(configuration: JsonValue) -> str:
    """Return the exact nested credential only when it is a string."""
    match configuration:
        case {"validator": {"if": {"password": str() as password}}}:
            return password
        case {"validator": {"if": {"password": _}}}:
            raise SourceSanitizationError.target_type()
        case _:
            raise SourceSanitizationError.target_path()
