"""Inspect one level of embedded JAR metadata and integrity."""

from __future__ import annotations

import io
import zipfile
from dataclasses import dataclass
from pathlib import PurePosixPath
from typing import TYPE_CHECKING, Literal

from mcpack_evidence.item3_jar_metadata import (
    FABRIC_PATH,
    TOML_PATHS,
    parse_fabric_metadata,
    parse_toml_metadata,
)

if TYPE_CHECKING:
    from mcpack_evidence.item3_jar_models import DependencyDeclaration, ModDeclaration


@dataclass(frozen=True)
class NestedJarDetails:
    """Normalized integrity and metadata from one embedded JAR."""

    zip_integrity: Literal["pass", "fail"]
    metadata_paths: tuple[str, ...]
    mods: tuple[ModDeclaration, ...]
    dependencies: tuple[DependencyDeclaration, ...]
    issues: tuple[str, ...]


def inspect_nested_jar(body: bytes) -> NestedJarDetails:
    """Verify and inspect an in-memory embedded JAR without extracting it."""
    try:
        archive = zipfile.ZipFile(io.BytesIO(body))
    except zipfile.BadZipFile:
        return NestedJarDetails(
            zip_integrity="fail",
            metadata_paths=(),
            mods=(),
            dependencies=(),
            issues=("bad_zip_file",),
        )
    with archive:
        names = tuple(info.filename for info in archive.infolist())
        issues: list[str] = []
        bad_member = archive.testzip()
        if bad_member is not None:
            issues.append(f"zip_crc_failure:{bad_member}")
        if len(names) != len(set(names)):
            issues.append("zip_duplicate_entries")
        if any(_unsafe(name) for name in names):
            issues.append("zip_unsafe_entries")
        metadata_paths = tuple(
            metadata_path for metadata_path in (*TOML_PATHS, FABRIC_PATH) if metadata_path in names
        )
        mods: list[ModDeclaration] = []
        dependencies: list[DependencyDeclaration] = []
        for metadata_path in TOML_PATHS:
            if metadata_path in names:
                parsed = parse_toml_metadata(archive.read(metadata_path), metadata_path)
                mods.extend(parsed.mods)
                dependencies.extend(parsed.dependencies)
        if FABRIC_PATH in names:
            parsed = parse_fabric_metadata(archive.read(FABRIC_PATH))
            mods.extend(parsed.mods)
            dependencies.extend(parsed.dependencies)
        return NestedJarDetails(
            zip_integrity="fail" if issues else "pass",
            metadata_paths=metadata_paths,
            mods=tuple(mods),
            dependencies=tuple(dependencies),
            issues=tuple(issues),
        )


def _unsafe(name: str) -> bool:
    path = PurePosixPath(name)
    return path.is_absolute() or ".." in path.parts
