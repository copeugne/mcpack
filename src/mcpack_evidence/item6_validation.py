# ruff: noqa: EM101, EM102, TRY003
"""Item 6 frozen configuration and audit validation."""

from __future__ import annotations

import hashlib
from typing import TYPE_CHECKING, Final, TypedDict

from pydantic import TypeAdapter

from mcpack_evidence.item6_audit_identity import validate_audit_semantic_identity
from mcpack_evidence.item6_file_accounting import Classification, validate_file_accounting
from mcpack_evidence.item6_json import StrictJsonError, parse_strict_json
from mcpack_evidence.item6_legacy_settings import Setting, validate_legacy_settings
from mcpack_evidence.item6_manifest import (
    parse_manifest,
    validate_manifest_contract,
    validate_manifest_inventory,
)
from mcpack_evidence.item6_materialization import validate_materialization
from mcpack_evidence.item6_provenance import validate_lifecycle, validate_repository_references
from mcpack_evidence.item6_sanitization import validate_sanitization_binding
from mcpack_evidence.item6_surface_validation import SettingSurface, validate_setting_surfaces

if TYPE_CHECKING:
    from pathlib import Path


class _System(TypedDict):
    system: str
    status: str
    files: list[str]


class _Finding(TypedDict):
    id: str
    classification: str
    summary: str
    files: list[str]
    confidence: str


class Audit(TypedDict):
    """Strict machine-readable Item 6 configuration audit."""

    schema_version: str
    configuration_identity: str
    scope: str
    tuning_performed: bool
    systems: list[_System]
    settings: list[Setting]
    setting_surfaces: list[SettingSurface]
    findings: list[_Finding]
    file_accounting: list[Classification]
    limitations: list[str]


_AUDIT_ADAPTER: Final[TypeAdapter[Audit]] = TypeAdapter(Audit)
_FROZEN_MANIFEST_IDENTITY: Final = (
    "sha256:2e0aaeb0f84747a3cb17146eb435d34cc7d6703b9372211e8fc8cff2df2b436f"
)


class _AuditValidationError(ValueError):
    pass


def sha256(path: Path) -> str:
    """Return a file's SHA-256 digest."""
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate(root: Path, manifest_path: Path, audit_path: Path) -> None:
    """Fail unless the frozen tree, manifest, and audit agree exactly."""
    manifest = parse_manifest(manifest_path)
    try:
        document = parse_strict_json(audit_path.read_bytes())
    except StrictJsonError:
        raise _AuditValidationError("audit is not strict JSON") from None
    audit = _AUDIT_ADAPTER.validate_python(document, strict=True, extra="forbid")
    if manifest["schema_version"] != "item6-frozen-config-manifest-v2":
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
    validate_sanitization_binding(manifest_path, root, manifest["sanitization"])

    covered = _collect_system_files(audit["systems"], expected)
    declared_systems = {system["system"] for system in audit["systems"]}
    covered.update(validate_legacy_settings(root, expected, audit["settings"]))
    surface_files = validate_setting_surfaces(
        root, expected, declared_systems, audit["setting_surfaces"]
    )
    legacy_setting_files = {setting["file"] for setting in audit["settings"]}
    if surface_files & legacy_setting_files:
        raise _AuditValidationError("file is claimed by both legacy and grouped setting evidence")
    covered.update(surface_files)
    covered.update(_collect_finding_files(audit["findings"], expected))
    if any(setting["non_default"] for setting in audit["settings"]):
        raise _AuditValidationError("untouched generated baseline unexpectedly reports tuning")
    validate_file_accounting(expected, covered, audit["file_accounting"])
    validate_audit_semantic_identity(audit)
    if identity != _FROZEN_MANIFEST_IDENTITY:
        raise _AuditValidationError("manifest identity does not match frozen baseline")


def _collect_system_files(systems: list[_System], expected: set[str]) -> set[str]:
    return _collect_cited_files(systems, expected, "system")


def _collect_finding_files(findings: list[_Finding], expected: set[str]) -> set[str]:
    return _collect_cited_files(findings, expected, "finding")


def _collect_cited_files(
    claims: list[_System] | list[_Finding], expected: set[str], claim_type: str
) -> set[str]:
    covered: set[str] = set()
    for claim in claims:
        for relative in claim["files"]:
            if relative not in expected:
                raise _AuditValidationError(f"{claim_type} cites an unpreserved file: {relative}")
            covered.add(relative)
    return covered
