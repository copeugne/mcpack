# ruff: noqa: EM101, EM102, TRY003
"""Validate Item 6's direct legacy setting evidence."""

from __future__ import annotations

import json
import tomllib
from math import isfinite
from typing import TYPE_CHECKING, Final, TypedDict

from pydantic import TypeAdapter, ValidationError

if TYPE_CHECKING:
    from pathlib import Path

Scalar = bool | int | float | str


class Observation(TypedDict):
    """One exact source-line observation for a legacy setting."""

    line: int
    prefix: str
    suffix: str


class SettingEvidence(TypedDict):
    """Decoder and observations defining one legacy setting value."""

    decoder: str
    observations: list[Observation]
    effective_semantics: str


class Setting(TypedDict):
    """One direct non-grouped Item 6 setting claim."""

    system: str
    file: str
    key: str
    scope: str
    owner: str
    interactions: list[str]
    evidence: SettingEvidence
    generated_default: Scalar
    effective_value: Scalar
    non_default: bool


_JSON_ADAPTER: Final[TypeAdapter[Scalar]] = TypeAdapter(Scalar)
_TOML_ADAPTER: Final[TypeAdapter[dict[str, Scalar]]] = TypeAdapter(dict[str, Scalar])
_C2ME_KEY: Final = "vanillaWorldGenOptimizations.useEndBiomeCache"
_C2ME_OBSERVATIONS: Final = [
    {"line": 80, "prefix": "useEndBiomeCache = ", "suffix": ""},
    {"line": 78, "prefix": "# Set to false for the following reasons:", "suffix": ""},
    {
        "line": 79,
        "prefix": "# Incompatible with biolith@3.0.10 (*) (defined in c2me)",
        "suffix": "",
    },
]


class LegacySettingValidationError(ValueError):
    """Raised when direct legacy setting evidence disagrees with frozen source."""


def validate_legacy_settings(root: Path, expected: set[str], settings: list[Setting]) -> set[str]:
    """Validate every direct setting claim and return its source-file coverage."""
    covered: set[str] = set()
    for setting in settings:
        _validate_setting(root, expected, setting)
        covered.add(setting["file"])
    return covered


def _validate_setting(root: Path, expected: set[str], setting: Setting) -> None:
    relative = setting["file"]
    if relative not in expected:
        raise LegacySettingValidationError(f"setting cites an unpreserved file: {relative}")
    evidence = setting["evidence"]
    decoder = evidence["decoder"]
    if decoder not in {"json", "toml", "string"}:
        raise LegacySettingValidationError("unsupported setting evidence decoder")
    source_path = root / relative
    if decoder != _expected_decoder(source_path):
        raise LegacySettingValidationError("setting evidence decoder does not match source format")
    observations = evidence["observations"]
    if not observations:
        raise LegacySettingValidationError("setting evidence observations must be nonempty")
    if "*" in setting["key"] and not observations[1:]:
        raise LegacySettingValidationError(
            "wildcard setting evidence must enumerate claimed leaves"
        )
    extracted = _extract_observations(source_path, setting["key"], evidence)
    _validate_effective_value(relative, setting, extracted)


def _expected_decoder(source_path: Path) -> str:
    if source_path.suffix == ".toml":
        return "toml"
    if source_path.suffix == ".properties" or source_path.name == "server.properties":
        return "string"
    return "json"


def _extract_observations(source_path: Path, key: str, evidence: SettingEvidence) -> list[Scalar]:
    lines = source_path.read_text(encoding="utf-8").splitlines()
    extracted: list[Scalar] = []
    for index, observation in enumerate(evidence["observations"]):
        source_line = _source_line(lines, key, evidence, index, observation)
        if evidence["effective_semantics"] == "c2me_biolith_runtime_disable" and index > 0:
            if observation["suffix"] or source_line != observation["prefix"]:
                raise LegacySettingValidationError(
                    "C2ME runtime-disable comment does not match exact source line"
                )
        else:
            end = (
                len(source_line) - len(observation["suffix"])
                if observation["suffix"]
                else len(source_line)
            )
            extracted.append(
                _decode_scalar(source_line[len(observation["prefix"]) : end], evidence["decoder"])
            )
    return extracted


def _source_line(
    lines: list[str], key: str, evidence: SettingEvidence, index: int, observation: Observation
) -> str:
    line_number = observation["line"]
    if type(line_number) is not int or line_number < 1:
        raise LegacySettingValidationError("setting evidence line must be a positive integer")
    if "*" in key and line_number in (row["line"] for row in evidence["observations"][:index]):
        raise LegacySettingValidationError("wildcard setting evidence repeats a source leaf")
    if line_number > len(lines):
        raise LegacySettingValidationError("setting evidence line is out of range")
    source_line = lines[line_number - 1].strip()
    prefix = observation["prefix"]
    suffix = observation["suffix"]
    if not source_line.startswith(prefix):
        raise LegacySettingValidationError("setting evidence prefix does not match source line")
    if not source_line.endswith(suffix):
        raise LegacySettingValidationError("setting evidence suffix does not match source line")
    end = len(source_line) - len(suffix) if suffix else len(source_line)
    if len(prefix) > end:
        raise LegacySettingValidationError("setting evidence prefix and suffix overlap")
    return source_line


def _decode_scalar(raw: str, decoder: str) -> Scalar:
    try:
        if decoder == "json":
            decoded = _JSON_ADAPTER.validate_json(raw, strict=True)
        elif decoder == "toml":
            decoded = _TOML_ADAPTER.validate_python(tomllib.loads(f"value = {raw}"), strict=True)[
                "value"
            ]
        elif decoder == "string" and raw and raw == raw.strip() and not raw.startswith(('"', "'")):
            decoded = raw
        else:
            raise LegacySettingValidationError("setting evidence scalar is malformed")
    except (json.JSONDecodeError, tomllib.TOMLDecodeError, ValidationError) as error:
        raise LegacySettingValidationError("setting evidence scalar is malformed") from error
    if isinstance(decoded, float) and not isfinite(decoded):
        raise LegacySettingValidationError("setting evidence scalar is malformed")
    return decoded


def _validate_effective_value(relative: str, setting: Setting, extracted: list[Scalar]) -> None:
    semantics = setting["evidence"]["effective_semantics"]
    if semantics == "same_as_generated":
        first = extracted[0]
        if any(not _same_type(first, value) for value in extracted[1:]):
            raise LegacySettingValidationError("setting evidence observations disagree")
        if not _same_type(setting["generated_default"], first) or not _same_type(
            setting["effective_value"], first
        ):
            raise LegacySettingValidationError("setting claimed value does not match source")
    elif semantics == "c2me_biolith_runtime_disable":
        if setting["key"] != _C2ME_KEY:
            raise LegacySettingValidationError(
                "C2ME runtime-disable semantics require the C2ME key"
            )
        if (
            relative != "config/c2me.toml"
            or setting["evidence"]["observations"] != _C2ME_OBSERVATIONS
        ):
            raise LegacySettingValidationError(
                "C2ME runtime-disable evidence does not match exact source lines"
            )
        if (
            setting["generated_default"] != "default"
            or setting["effective_value"] != "compatibility-disabled at runtime"
            or not _same_type(extracted[0], "default")
        ):
            raise LegacySettingValidationError("setting claimed value does not match source")
    else:
        raise LegacySettingValidationError("unsupported setting effective semantics")


def _same_type(left: Scalar, right: Scalar) -> bool:
    return type(left) is type(right) and left == right
