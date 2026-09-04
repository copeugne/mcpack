# ruff: noqa: EM101, EM102, TRY003
"""Item 6 frozen configuration and audit validation."""

from __future__ import annotations

import hashlib
import json
import tomllib
from math import isfinite
from typing import TYPE_CHECKING, Final, TypedDict

from pydantic import TypeAdapter, ValidationError

from mcpack_evidence.item6_manifest import (
    parse_manifest,
    validate_manifest_contract,
    validate_manifest_inventory,
)
from mcpack_evidence.item6_materialization import validate_materialization
from mcpack_evidence.item6_provenance import validate_lifecycle, validate_repository_references
from mcpack_evidence.item6_surface_validation import SettingSurface, validate_setting_surfaces

if TYPE_CHECKING:
    from pathlib import Path

Scalar = bool | int | float | str


class _System(TypedDict):
    system: str
    status: str
    files: list[str]


class _Observation(TypedDict):
    line: int
    prefix: str
    suffix: str


class _SettingEvidence(TypedDict):
    decoder: str
    observations: list[_Observation]
    effective_semantics: str


class _Setting(TypedDict):
    system: str
    file: str
    key: str
    scope: str
    owner: str
    interactions: list[str]
    evidence: _SettingEvidence
    generated_default: Scalar
    effective_value: Scalar
    non_default: bool


class _Finding(TypedDict):
    id: str
    classification: str
    summary: str
    files: list[str]
    confidence: str


class _Classification(TypedDict):
    classification: str
    files: list[str]


class Audit(TypedDict):
    """Strict machine-readable Item 6 configuration audit."""

    schema_version: str
    configuration_identity: str
    scope: str
    tuning_performed: bool
    systems: list[_System]
    settings: list[_Setting]
    setting_surfaces: list[SettingSurface]
    findings: list[_Finding]
    file_accounting: list[_Classification]
    limitations: list[str]


_AUDIT_ADAPTER: Final[TypeAdapter[Audit]] = TypeAdapter(Audit)
_JSON_ADAPTER: Final[TypeAdapter[Scalar]] = TypeAdapter(Scalar)
_TOML_ADAPTER: Final[TypeAdapter[dict[str, Scalar]]] = TypeAdapter(dict[str, Scalar])
C2ME_KEY: Final = "vanillaWorldGenOptimizations.useEndBiomeCache"
C2ME_OBSERVATIONS: Final = [
    {"line": 80, "prefix": "useEndBiomeCache = ", "suffix": ""},
    {"line": 78, "prefix": "# Set to false for the following reasons:", "suffix": ""},
    {
        "line": 79,
        "prefix": "# Incompatible with biolith@3.0.10 (*) (defined in c2me)",
        "suffix": "",
    },
]


class _AuditValidationError(ValueError):
    pass


def sha256(path: Path) -> str:
    """Return a file's SHA-256 digest."""
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _decode_setting_scalar(raw: str, decoder: str) -> Scalar:
    try:
        if decoder == "json":
            decoded = _JSON_ADAPTER.validate_json(raw, strict=True)
        elif decoder == "toml":
            values = _TOML_ADAPTER.validate_python(tomllib.loads(f"value = {raw}"), strict=True)
            decoded = values["value"]
        elif decoder == "string":
            if not raw or raw != raw.strip() or raw.startswith(('"', "'")):
                raise _AuditValidationError("setting evidence scalar is malformed")
            decoded = raw
        else:
            raise _AuditValidationError("unsupported setting evidence decoder")
    except (json.JSONDecodeError, tomllib.TOMLDecodeError, ValidationError) as error:
        raise _AuditValidationError("setting evidence scalar is malformed") from error
    if isinstance(decoded, float) and not isfinite(decoded):
        raise _AuditValidationError("setting evidence scalar is malformed")
    return decoded


def _same_typed_value(left: Scalar, right: Scalar) -> bool:
    return type(left) is type(right) and left == right


def validate(  # noqa: C901, PLR0912, PLR0915
    root: Path, manifest_path: Path, audit_path: Path
) -> None:
    """Fail unless the frozen tree, manifest, and audit agree exactly."""
    manifest = parse_manifest(manifest_path)
    audit = _AUDIT_ADAPTER.validate_json(audit_path.read_bytes(), strict=True, extra="forbid")
    if manifest["schema_version"] != "item6-frozen-config-manifest-v1":
        raise _AuditValidationError("unsupported manifest schema")
    if audit["schema_version"] != "item6-config-audit-v2":
        raise _AuditValidationError("unsupported audit schema")
    if audit["tuning_performed"] is not False:
        raise _AuditValidationError("baseline must not contain tuning")
    identity = f"sha256:{sha256(manifest_path)}"
    if audit["configuration_identity"] != identity:
        raise _AuditValidationError("audit configuration identity does not match manifest")

    validate_manifest_contract(manifest)
    references = validate_repository_references(manifest_path, manifest)
    validate_lifecycle(manifest, references)
    validate_materialization(manifest, references)
    expected = validate_manifest_inventory(root, manifest)

    covered: set[str] = set()
    declared_systems = {system["system"] for system in audit["systems"]}
    for system in audit["systems"]:
        for relative in system["files"]:
            if relative not in expected:
                raise _AuditValidationError(f"system cites an unpreserved file: {relative}")
            covered.add(relative)
    for setting in audit["settings"]:
        relative = setting["file"]
        if relative not in expected:
            raise _AuditValidationError(f"setting cites an unpreserved file: {relative}")
        evidence = setting["evidence"]
        decoder = evidence["decoder"]
        if decoder not in {"json", "toml", "string"}:
            raise _AuditValidationError("unsupported setting evidence decoder")
        source_path = root / relative
        expected_decoder = (
            "toml"
            if source_path.suffix == ".toml"
            else "string"
            if source_path.suffix == ".properties" or source_path.name == "server.properties"
            else "json"
        )
        if decoder != expected_decoder:
            raise _AuditValidationError("setting evidence decoder does not match source format")
        observations = evidence["observations"]
        if not observations:
            raise _AuditValidationError("setting evidence observations must be nonempty")
        if "*" in setting["key"] and not observations[1:]:
            raise _AuditValidationError("wildcard setting evidence must enumerate claimed leaves")
        lines = source_path.read_text(encoding="utf-8").splitlines()
        extracted: list[Scalar] = []
        for observation_index, observation in enumerate(observations):
            line_number = observation["line"]
            prefix = observation["prefix"]
            suffix = observation["suffix"]
            if type(line_number) is not int or line_number < 1:
                raise _AuditValidationError("setting evidence line must be a positive integer")
            prior_lines = (prior["line"] for prior in observations[:observation_index])
            if "*" in setting["key"] and line_number in prior_lines:
                raise _AuditValidationError("wildcard setting evidence repeats a source leaf")
            if line_number > len(lines):
                raise _AuditValidationError("setting evidence line is out of range")
            source_line = lines[line_number - 1].strip()
            if not source_line.startswith(prefix):
                raise _AuditValidationError("setting evidence prefix does not match source line")
            if not source_line.endswith(suffix):
                raise _AuditValidationError("setting evidence suffix does not match source line")
            scalar_end = len(source_line) - len(suffix) if suffix else len(source_line)
            if len(prefix) > scalar_end:
                raise _AuditValidationError("setting evidence prefix and suffix overlap")
            if (
                evidence["effective_semantics"] == "c2me_biolith_runtime_disable"
                and observation_index > 0
            ):
                if suffix or source_line != prefix:
                    raise _AuditValidationError(
                        "C2ME runtime-disable comment does not match exact source line"
                    )
            else:
                extracted.append(
                    _decode_setting_scalar(source_line[len(prefix) : scalar_end], decoder)
                )
        semantics = evidence["effective_semantics"]
        if semantics == "same_as_generated":
            first = extracted[0]
            if any(not _same_typed_value(first, value) for value in extracted[1:]):
                raise _AuditValidationError("setting evidence observations disagree")
            if not _same_typed_value(setting["generated_default"], first) or not _same_typed_value(
                setting["effective_value"], first
            ):
                raise _AuditValidationError("setting claimed value does not match source")
        elif semantics == "c2me_biolith_runtime_disable":
            if setting["key"] != C2ME_KEY:
                raise _AuditValidationError("C2ME runtime-disable semantics require the C2ME key")
            if relative != "config/c2me.toml" or observations != C2ME_OBSERVATIONS:
                raise _AuditValidationError(
                    "C2ME runtime-disable evidence does not match exact source lines"
                )
            if (
                setting["generated_default"] != "default"
                or setting["effective_value"] != "compatibility-disabled at runtime"
                or not _same_typed_value(extracted[0], "default")
            ):
                raise _AuditValidationError("setting claimed value does not match source")
        else:
            raise _AuditValidationError("unsupported setting effective semantics")
        covered.add(relative)
    surface_files = validate_setting_surfaces(
        root, expected, declared_systems, audit["setting_surfaces"]
    )
    legacy_setting_files = {setting["file"] for setting in audit["settings"]}
    if surface_files & legacy_setting_files:
        raise _AuditValidationError("file is claimed by both legacy and grouped setting evidence")
    covered.update(surface_files)
    for finding in audit["findings"]:
        for relative in finding["files"]:
            if relative not in expected:
                raise _AuditValidationError(f"finding cites an unpreserved file: {relative}")
            covered.add(relative)
    if any(setting["non_default"] for setting in audit["settings"]):
        raise _AuditValidationError("untouched generated baseline unexpectedly reports tuning")
    accounted: set[str] = set()
    for classification in audit["file_accounting"]:
        if classification["classification"] not in {"audited", "out-of-scope"}:
            raise _AuditValidationError("invalid file-accounting classification")
        for relative in classification["files"]:
            if relative in accounted:
                raise _AuditValidationError(f"file is classified more than once: {relative}")
            accounted.add(relative)
    if accounted != expected:
        missing = sorted(expected - accounted)
        extra = sorted(accounted - expected)
        raise _AuditValidationError(
            f"file accounting does not match manifest: missing={missing}, extra={extra}"
        )
    audited = {
        relative
        for classification in audit["file_accounting"]
        if classification["classification"] == "audited"
        for relative in classification["files"]
    }
    if audited != covered:
        raise _AuditValidationError("audited file accounting does not match cited audit evidence")
