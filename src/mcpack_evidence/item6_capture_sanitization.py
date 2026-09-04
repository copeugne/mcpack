"""Strict byte-preserving sanitization for the captured generated credential."""

from __future__ import annotations

import json
import re
from typing import Final, Self

from pydantic import JsonValue, TypeAdapter, ValidationError

from mcpack_evidence.item6_json import StrictJsonError, parse_strict_json

_PASSWORD_MEMBER: Final = re.compile(r'"password"\s*:\s*("(?:[^"\\]|\\.)*")')
_REDACTION_SENTINEL: Final = "<redacted-generated-secret>"
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

    @classmethod
    def reserved_value(cls) -> Self:
        """Create the reserved redaction-sentinel failure."""
        return cls("generated credential already equals the redaction sentinel")


def redact_generated_credential(source: bytes) -> bytes:
    """Replace exactly one verified canonical credential string token."""
    try:
        text = source.decode("utf-8")
        configuration = parse_strict_json(source)
    except (UnicodeDecodeError, StrictJsonError) as error:
        raise SourceSanitizationError.invalid_json() from error
    password = _require_string_credential(configuration)
    if password == _REDACTION_SENTINEL:
        raise SourceSanitizationError.reserved_value()
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


def _require_string_credential(configuration: JsonValue) -> str:
    """Return the exact nested credential only when it is a string."""
    match configuration:
        case {"validator": {"if": {"password": str() as password}}}:
            return password
        case {"validator": {"if": {"password": _}}}:
            raise SourceSanitizationError.target_type()
        case _:
            raise SourceSanitizationError.target_path()
