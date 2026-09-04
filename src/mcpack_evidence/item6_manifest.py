# ruff: noqa: EM101, EM102, TRY003
"""Parse and validate the frozen Item 6 manifest inventory."""

from __future__ import annotations

import hashlib
from collections import Counter
from pathlib import PurePosixPath
from typing import TYPE_CHECKING, Final, TypedDict

from pydantic import TypeAdapter

if TYPE_CHECKING:
    from pathlib import Path


class ManifestRow(TypedDict):
    """One hash-bound frozen configuration file."""

    path: str
    size_bytes: int
    sha256: str
    generation_stage: str


class Manifest(TypedDict):
    """The Item 6 frozen configuration manifest."""

    schema_version: str
    capture_boundary: str
    file_count: int
    files: list[ManifestRow]


_MANIFEST_ADAPTER: Final[TypeAdapter[Manifest]] = TypeAdapter(Manifest)
_STAGES: Final = {"installation", "first_startup", "world_creation", "shutdown"}
_CAPTURE_BOUNDARY: Final = "after_first_clean_shutdown"
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
    return _MANIFEST_ADAPTER.validate_json(manifest_path.read_bytes(), strict=True, extra="allow")


def validate_manifest_inventory(root: Path, manifest: Manifest) -> set[str]:
    """Return the exact preserved paths after validating manifest inventory hashes."""
    rows = manifest["files"]
    expected = {row["path"] for row in rows}
    actual = {path.relative_to(root).as_posix() for path in root.rglob("*") if path.is_file()}
    if expected != actual or manifest["file_count"] != len(rows):
        raise ManifestValidationError("frozen file inventory does not match manifest")
    for row in rows:
        path = root / row["path"]
        if path.stat().st_size != row["size_bytes"] or _sha256(path) != row["sha256"]:
            raise ManifestValidationError(f"frozen file identity mismatch: {row['path']}")
        if row["generation_stage"] not in _STAGES:
            raise ManifestValidationError(f"invalid generation stage: {row['path']}")
    return expected


def validate_manifest_contract(manifest: Manifest) -> None:
    """Reject a manifest that is not the deterministic Item 6 capture record."""
    paths = [row["path"] for row in manifest["files"]]
    component_paths = [PurePosixPath(path).parts for path in paths]
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
