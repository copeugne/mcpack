#!/usr/bin/env python3
# ruff: noqa: EM101, EM102, TRY003
"""Freeze and validate the untouched Item 6 generated configuration baseline."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import tomllib
from math import isfinite
from pathlib import Path
from typing import Any, cast

Scalar = bool | int | float | str
C2ME_KEY = "vanillaWorldGenOptimizations.useEndBiomeCache"
C2ME_OBSERVATIONS = [
    {"line": 80, "prefix": "useEndBiomeCache = ", "suffix": ""},
    {
        "line": 78,
        "prefix": "# Set to false for the following reasons:",
        "suffix": "",
    },
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
            decoded = json.loads(raw)
        elif decoder == "toml":
            decoded = tomllib.loads(f"value = {raw}")["value"]
        elif decoder == "string":
            if not raw or raw != raw.strip() or raw.startswith(('"', "'")):
                raise _AuditValidationError("setting evidence scalar is malformed")
            decoded = raw
        else:
            raise _AuditValidationError("unsupported setting evidence decoder")
    except (json.JSONDecodeError, tomllib.TOMLDecodeError) as error:
        raise _AuditValidationError("setting evidence scalar is malformed") from error
    if type(decoded) not in {bool, int, float, str}:
        raise _AuditValidationError("setting evidence scalar is not a supported scalar")
    if isinstance(decoded, float) and not isfinite(decoded):
        raise _AuditValidationError("setting evidence scalar is malformed")
    return decoded


def _same_typed_value(left: Scalar, right: Scalar) -> bool:
    return type(left) is type(right) and left == right


def validate(  # noqa: C901, PLR0912, PLR0915
    root: Path, manifest_path: Path, audit_path: Path
) -> None:
    """Fail unless the frozen tree, manifest, and audit agree exactly."""
    manifest = cast("dict[str, Any]", json.loads(manifest_path.read_text(encoding="utf-8")))
    audit = cast("dict[str, Any]", json.loads(audit_path.read_text(encoding="utf-8")))
    if manifest["schema_version"] != "item6-frozen-config-manifest-v1":
        raise _AuditValidationError("unsupported manifest schema")
    if audit["schema_version"] != "item6-config-audit-v1":
        raise _AuditValidationError("unsupported audit schema")
    if audit["tuning_performed"] is not False:
        raise _AuditValidationError("baseline must not contain tuning")
    identity = f"sha256:{sha256(manifest_path)}"
    if audit["configuration_identity"] != identity:
        raise _AuditValidationError("audit configuration identity does not match manifest")

    rows = manifest["files"]
    expected = {row["path"] for row in rows}
    actual = {path.relative_to(root).as_posix() for path in root.rglob("*") if path.is_file()}
    if expected != actual or manifest["file_count"] != len(rows):
        raise _AuditValidationError("frozen file inventory does not match manifest")
    for row in rows:
        path = root / row["path"]
        if path.stat().st_size != row["size_bytes"] or sha256(path) != row["sha256"]:
            raise _AuditValidationError(f"frozen file identity mismatch: {row['path']}")
        if row["generation_stage"] not in {
            "installation",
            "first_startup",
            "world_creation",
            "shutdown",
        }:
            raise _AuditValidationError(f"invalid generation stage: {row['path']}")

    covered: set[str] = set()
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
        if not isinstance(evidence, dict) or set(evidence) != {
            "decoder",
            "observations",
            "effective_semantics",
        }:
            raise _AuditValidationError("setting evidence must use the structured contract")
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
        if not isinstance(observations, list) or not observations:
            raise _AuditValidationError("setting evidence observations must be nonempty")
        if "*" in setting["key"] and not observations[1:]:
            raise _AuditValidationError("wildcard setting evidence must enumerate claimed leaves")
        lines = source_path.read_text(encoding="utf-8").splitlines()
        extracted: list[Scalar] = []
        for observation_index, observation in enumerate(observations):
            if not isinstance(observation, dict) or set(observation) != {
                "line",
                "prefix",
                "suffix",
            }:
                raise _AuditValidationError("setting evidence observation is malformed")
            line_number = observation["line"]
            prefix = observation["prefix"]
            suffix = observation["suffix"]
            if type(line_number) is not int or line_number < 1:
                raise _AuditValidationError("setting evidence line must be a positive integer")
            if line_number > len(lines):
                raise _AuditValidationError("setting evidence line is out of range")
            if not isinstance(prefix, str) or not isinstance(suffix, str):
                raise _AuditValidationError("setting evidence prefix and suffix must be strings")
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


def capture(instance: Path, output: Path) -> None:
    """Copy configuration-bearing paths without altering the source instance."""
    if output.exists():
        raise FileExistsError(f"output already exists: {output}")
    output.mkdir(parents=True)
    sources = {
        instance / "config": output / "config",
        instance / "defaultconfigs": output / "defaultconfigs",
        instance / "world" / "serverconfig": output / "world-serverconfig",
    }
    for source, target in sources.items():
        if source.is_dir():
            shutil.copytree(source, target)
    shutil.copy2(instance / "server.properties", output / "server.properties")


def main() -> int:
    """Run capture or validation."""
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    capture_parser = subparsers.add_parser("capture")
    capture_parser.add_argument("--instance", type=Path, required=True)
    capture_parser.add_argument("--output", type=Path, required=True)
    validate_parser = subparsers.add_parser("validate")
    validate_parser.add_argument("--root", type=Path, required=True)
    validate_parser.add_argument("--manifest", type=Path, required=True)
    validate_parser.add_argument("--audit", type=Path, required=True)
    arguments = parser.parse_args()
    if arguments.command == "capture":
        capture(arguments.instance, arguments.output)
    else:
        validate(arguments.root, arguments.manifest, arguments.audit)
        print("validated Item 6 frozen configuration and audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
