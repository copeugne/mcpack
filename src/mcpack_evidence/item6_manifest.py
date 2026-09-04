# ruff: noqa: EM101, EM102, TRY003
"""Parse and validate the frozen Item 6 manifest inventory."""

from __future__ import annotations

import hashlib
from collections import Counter
from pathlib import PurePosixPath
from typing import TYPE_CHECKING, Final, TypedDict

from pydantic import TypeAdapter

from mcpack_evidence.item6_json import StrictJsonError, parse_strict_json

if TYPE_CHECKING:
    from pathlib import Path


class ManifestRow(TypedDict):
    """One hash-bound frozen configuration file."""

    path: str
    size_bytes: int
    sha256: str
    generation_stage: str


class RetainedManifest(TypedDict):
    """Identity of the retained dedicated-server candidate manifest."""

    path: str
    count: int
    sha256: str


class JavaRuntime(TypedDict):
    """Java runtime identity recorded in the frozen manifest."""

    vendor: str
    version: str
    build: str
    archive_sha256: str


class StageNotes(TypedDict):
    """Recorded observation basis for each frozen configuration stage."""

    installation: str
    first_startup: str
    world_creation: str
    shutdown: str


class SanitizationMetadata(TypedDict):
    """Identity and cardinality of the evidence-safe credential redaction receipt."""

    receipt: str
    sha256: str
    sanitized_file_count: int
    redaction_count: int


class Manifest(TypedDict):
    """The Item 6 frozen configuration manifest."""

    schema_version: str
    generated_at: str
    capture_boundary: str
    minecraft_version: str
    neoforge_version: str
    java: JavaRuntime
    configuration_version: str
    seed_role: str
    seed: str
    retained_manifest: RetainedManifest
    capture_command: str
    source_lifecycle: str
    file_count: int
    files: list[ManifestRow]
    stage_notes: StageNotes
    sanitization: SanitizationMetadata


_MANIFEST_ADAPTER: Final[TypeAdapter[Manifest]] = TypeAdapter(Manifest)
_STAGES: Final = {"installation", "first_startup", "world_creation", "shutdown"}
_CAPTURE_BOUNDARY: Final = "after_first_clean_shutdown"
_SANITIZATION_RECEIPT: Final = "evidence/item-6/config-sanitization.json"
_SHA256_HEX_LENGTH: Final = 64
_EXPECTED_STAGE_COUNTS: Final = {
    "installation": 4,
    "first_startup": 223,
    "world_creation": 1,
    "shutdown": 0,
}


class ManifestValidationError(ValueError):
    """Raised when a frozen-manifest inventory is inconsistent."""


def parse_manifest(manifest_path: Path) -> Manifest:
    """Parse the manifest at the untrusted file boundary."""
    try:
        document = parse_strict_json(manifest_path.read_bytes())
    except StrictJsonError:
        raise ManifestValidationError("manifest is not strict JSON") from None
    return _MANIFEST_ADAPTER.validate_python(document, strict=True, extra="forbid")


def validate_manifest_inventory(root: Path, manifest: Manifest) -> set[str]:
    """Return the exact preserved paths after validating manifest inventory hashes."""
    rows = manifest["files"]
    relatives = [_parse_manifest_path(row["path"]) for row in rows]
    paths = [relative.as_posix() for relative in relatives]
    expected = set(paths)
    resolved_files = [_resolve_manifest_file(root, relative) for relative in relatives]
    if any(path.is_symlink() for path in root.rglob("*")):
        raise ManifestValidationError("manifest path components must be real non-symlinks")
    actual = {path.relative_to(root).as_posix() for path in root.rglob("*") if path.is_file()}
    if expected != actual or manifest["file_count"] != len(rows):
        raise ManifestValidationError("frozen file inventory does not match manifest")
    for row, path in zip(rows, resolved_files, strict=True):
        if path.stat().st_size != row["size_bytes"] or _sha256(path) != row["sha256"]:
            raise ManifestValidationError(f"frozen file identity mismatch: {row['path']}")
        if row["generation_stage"] not in _STAGES:
            raise ManifestValidationError(f"invalid generation stage: {row['path']}")
    return expected


def _parse_manifest_path(path: str) -> PurePosixPath:
    relative = PurePosixPath(path)
    if (
        not path
        or "\\" in path
        or relative.is_absolute()
        or relative.as_posix() != path
        or any(part in {".", ".."} for part in relative.parts)
    ):
        raise ManifestValidationError("manifest file path must be a normalized relative POSIX path")
    return relative


def _resolve_manifest_file(root: Path, relative: PurePosixPath) -> Path:
    if root.is_symlink() or not root.is_dir():
        raise ManifestValidationError("frozen root must be a real non-symlink directory")
    root_resolved = root.resolve(strict=True)
    candidate = root
    for part in relative.parts:
        candidate /= part
        if candidate.is_symlink():
            raise ManifestValidationError("manifest path components must be real non-symlinks")
    if not candidate.is_file():
        raise ManifestValidationError("manifest path must name a regular file")
    try:
        resolved_candidate = candidate.resolve(strict=True)
        _ = resolved_candidate.relative_to(root_resolved)
    except ValueError as error:
        raise ManifestValidationError(
            "manifest file path must be a normalized relative POSIX path"
        ) from error
    return candidate


def validate_manifest_contract(manifest: Manifest) -> None:
    """Reject a manifest that is not the deterministic Item 6 capture record."""
    if manifest["schema_version"] != "item6-frozen-config-manifest-v2":
        raise ManifestValidationError("unsupported manifest schema")
    sanitization = manifest["sanitization"]
    if sanitization["receipt"] != _SANITIZATION_RECEIPT:
        raise ManifestValidationError(
            "sanitization receipt must name the canonical repository path"
        )
    if sanitization["sanitized_file_count"] != 1 or sanitization["redaction_count"] != 1:
        raise ManifestValidationError("sanitization receipt counts must each equal one")
    receipt_digest = sanitization["sha256"]
    if len(receipt_digest) != _SHA256_HEX_LENGTH or any(
        character not in "0123456789abcdef" for character in receipt_digest
    ):
        raise ManifestValidationError("sanitization receipt digest must be a lowercase SHA-256")
    paths = [row["path"] for row in manifest["files"]]
    component_paths = [_parse_manifest_path(path).parts for path in paths]
    if component_paths != sorted(component_paths):
        raise ManifestValidationError("manifest paths must be strictly component-ordered")
    if len(paths) != len(set(paths)):
        raise ManifestValidationError("manifest paths must be unique")
    if manifest["file_count"] != len(paths):
        raise ManifestValidationError("frozen file inventory does not match manifest")
    if manifest["capture_boundary"] != _CAPTURE_BOUNDARY:
        raise ManifestValidationError("invalid manifest capture boundary")
    stage_counts = Counter(row["generation_stage"] for row in manifest["files"])
    if any(stage_counts[stage] != count for stage, count in _EXPECTED_STAGE_COUNTS.items()):
        raise ManifestValidationError("manifest generation-stage counts are invalid")


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()
