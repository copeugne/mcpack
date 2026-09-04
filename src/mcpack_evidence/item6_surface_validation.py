# ruff: noqa: EM101, EM102, TRY003
"""Parse and validate complete grouped Item 6 setting surfaces."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, replace
from math import isfinite
from typing import TYPE_CHECKING, Final, TypedDict

from pydantic import TypeAdapter, ValidationError

if TYPE_CHECKING:
    from pathlib import Path

Scalar = bool | int | float | str
type JsonValue = bool | int | float | str | list[JsonValue] | dict[str, JsonValue] | None


class SurfaceLeaf(TypedDict):
    """One scalar claim bound to one exact source line."""

    key: str
    line: int
    prefix: str
    suffix: str
    generated_default: Scalar
    effective_value: Scalar
    non_default: bool


class SettingSurface(TypedDict):
    """All scalar leaves from one structured configuration file."""

    system: str
    file: str
    decoder: str
    leaves: list[SurfaceLeaf]


@dataclass(frozen=True, slots=True)
class ParsedLeaf:
    """A scalar extracted from one CristelLib JSON5 source line."""

    key: str
    line: int
    prefix: str
    suffix: str
    value: Scalar


@dataclass(frozen=True, slots=True)
class _ParserState:
    stack: tuple[str, ...]
    leaves: tuple[ParsedLeaf, ...]
    seen_paths: frozenset[str]
    root_open: bool = False
    root_closed: bool = False
    in_block_comment: bool = False


_JSON_ADAPTER: Final[TypeAdapter[JsonValue]] = TypeAdapter(JsonValue)
_KEY_ADAPTER: Final[TypeAdapter[str]] = TypeAdapter(str)
_OPEN_OBJECT: Final = re.compile(r'^\s*("(?:[^"\\]|\\.)+")\s*:\s*\{\s*,?\s*$')
_CLOSE_OBJECT: Final = re.compile(r"^\s*}\s*,?\s*$")
_SCALAR_START: Final = r'^(?P<indent>\s*)(?P<key>"(?:[^"\\]|\\.)+")(?P<separator>\s*:\s*)'
_SCALAR_VALUE: Final = r'(?P<value>"(?:[^"\\]|\\.)*"|true|false|-?(?:0|[1-9]\d*)'
_SCALAR_END: Final = r"(?:\.\d+)?(?:[eE][+-]?\d+)?)(?P<suffix>\s*,?\s*)$"
_SCALAR_PATTERN: Final = f"{_SCALAR_START}{_SCALAR_VALUE}{_SCALAR_END}"
_SCALAR: Final = re.compile(_SCALAR_PATTERN)


class SurfaceValidationError(ValueError):
    """Raised when grouped setting evidence is incomplete or inconsistent."""


def decode_scalar(raw: str) -> Scalar:
    """Decode one finite strict JSON scalar."""
    try:
        decoded = _JSON_ADAPTER.validate_json(raw, strict=True)
    except (json.JSONDecodeError, ValidationError) as error:
        raise SurfaceValidationError("CristelLib scalar is malformed") from error
    if not isinstance(decoded, (bool, int, float, str)):
        raise SurfaceValidationError("CristelLib value is not a supported scalar")
    if isinstance(decoded, float) and not isfinite(decoded):
        raise SurfaceValidationError("CristelLib scalar is malformed")
    return decoded


def _decode_key(raw: str) -> str:
    try:
        decoded = _KEY_ADAPTER.validate_json(raw, strict=True)
    except (json.JSONDecodeError, ValidationError) as error:
        raise SurfaceValidationError("CristelLib key is malformed") from error
    if not decoded:
        raise SurfaceValidationError("CristelLib key is malformed")
    return decoded


def _new_path(state: _ParserState, key: str) -> str:
    path_key = ".".join((*state.stack, key))
    if path_key in state.seen_paths:
        raise SurfaceValidationError("CristelLib document repeats a key path")
    return path_key


def _consume_content(state: _ParserState, source_line: str, line_number: int) -> _ParserState:
    stripped = source_line.strip()
    if not state.root_open:
        if stripped != "{":
            raise SurfaceValidationError("CristelLib document must start with an object")
        return replace(state, root_open=True)
    if state.root_closed:
        raise SurfaceValidationError("CristelLib document has content after the root object")
    opened = _OPEN_OBJECT.fullmatch(source_line)
    if opened is not None:
        key = _decode_key(opened.group(1))
        path_key = _new_path(state, key)
        return replace(
            state,
            stack=(*state.stack, key),
            seen_paths=state.seen_paths | {path_key},
        )
    scalar = _SCALAR.fullmatch(source_line)
    if scalar is not None:
        if not state.stack:
            raise SurfaceValidationError("CristelLib scalar must belong to a named object")
        path_key = _new_path(state, _decode_key(scalar.group("key")))
        leaf = ParsedLeaf(
            key=path_key,
            line=line_number,
            prefix=f"{scalar.group('key')}{scalar.group('separator')}",
            suffix=scalar.group("suffix").strip(),
            value=decode_scalar(scalar.group("value")),
        )
        return replace(
            state,
            leaves=(*state.leaves, leaf),
            seen_paths=state.seen_paths | {path_key},
        )
    if _CLOSE_OBJECT.fullmatch(source_line) is not None:
        if state.stack:
            return replace(state, stack=state.stack[:-1])
        return replace(state, root_closed=True)
    raise SurfaceValidationError(f"unsupported CristelLib JSON5 syntax on line {line_number}")


def _consume_line(state: _ParserState, source_line: str, line_number: int) -> _ParserState:
    stripped = source_line.strip()
    if state.in_block_comment:
        return replace(state, in_block_comment=not stripped.endswith("*/"))
    if stripped.startswith("/*"):
        return replace(state, in_block_comment=not stripped.endswith("*/"))
    if stripped and not stripped.startswith("//"):
        return _consume_content(state, source_line, line_number)
    return state


def parse_cristellib_json5(path: Path) -> tuple[ParsedLeaf, ...]:
    """Parse the strict line-oriented subset emitted by CristelLib."""
    state = _ParserState(stack=(), leaves=(), seen_paths=frozenset())
    for line_number, source_line in enumerate(
        path.read_text(encoding="utf-8").splitlines(), start=1
    ):
        state = _consume_line(state, source_line, line_number)
    if state.in_block_comment or not state.root_open or not state.root_closed or state.stack:
        raise SurfaceValidationError("CristelLib document is incomplete")
    if not state.leaves:
        raise SurfaceValidationError("CristelLib document has no scalar leaves")
    return tuple(state.leaves)


def build_setting_surface(system: str, relative: str, source: Path) -> SettingSurface:
    """Build deterministic same-as-generated evidence for one CristelLib file."""
    return {
        "system": system,
        "file": relative,
        "decoder": "cristellib-json5",
        "leaves": [
            {
                "key": leaf.key,
                "line": leaf.line,
                "prefix": leaf.prefix,
                "suffix": leaf.suffix,
                "generated_default": leaf.value,
                "effective_value": leaf.value,
                "non_default": False,
            }
            for leaf in parse_cristellib_json5(source)
        ],
    }


def _validate_leaf(claim: SurfaceLeaf, source_leaf: ParsedLeaf) -> None:
    evidence = (claim["key"], claim["line"], claim["prefix"], claim["suffix"])
    observed = (source_leaf.key, source_leaf.line, source_leaf.prefix, source_leaf.suffix)
    if evidence != observed:
        raise SurfaceValidationError("setting surface line evidence does not match source")
    if type(claim["generated_default"]) is not type(source_leaf.value) or (
        claim["generated_default"] != source_leaf.value
    ):
        raise SurfaceValidationError("setting surface generated value does not match source")
    if type(claim["effective_value"]) is not type(source_leaf.value) or (
        claim["effective_value"] != source_leaf.value
    ):
        raise SurfaceValidationError("setting surface effective value does not match source")
    if claim["non_default"]:
        raise SurfaceValidationError("untouched generated baseline unexpectedly reports tuning")


def _validate_surface(
    root: Path,
    expected_files: set[str],
    declared_systems: set[str],
    covered: set[str],
    surface: SettingSurface,
) -> None:
    relative = surface["file"]
    if surface["system"] not in declared_systems:
        raise SurfaceValidationError("setting surface system is not declared")
    if relative in covered:
        raise SurfaceValidationError("setting surface file must be unique")
    if relative not in expected_files:
        raise SurfaceValidationError(f"setting surface cites an unpreserved file: {relative}")
    if surface["decoder"] != "cristellib-json5" or not relative.endswith(".json5"):
        raise SurfaceValidationError("setting surface decoder does not match source format")
    leaves = surface["leaves"]
    if not leaves:
        raise SurfaceValidationError("setting surface leaves must be nonempty")
    parsed = parse_cristellib_json5(root / relative)
    if len(leaves) != len(parsed):
        raise SurfaceValidationError("setting surface does not enumerate every source leaf")
    keys = [leaf["key"] for leaf in leaves]
    lines = [leaf["line"] for leaf in leaves]
    if len(keys) != len(set(keys)) or len(lines) != len(set(lines)):
        raise SurfaceValidationError("setting surface leaf keys and lines must be unique")
    for claim, source_leaf in zip(leaves, parsed, strict=True):
        _validate_leaf(claim, source_leaf)
    covered.add(relative)


def validate_setting_surfaces(
    root: Path,
    expected_files: set[str],
    declared_systems: set[str],
    surfaces: list[SettingSurface],
) -> set[str]:
    """Validate complete exact grouped surfaces and return their covered files."""
    covered: set[str] = set()
    for surface in surfaces:
        _validate_surface(root, expected_files, declared_systems, covered, surface)
    return covered
