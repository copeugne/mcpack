"""Inspect archive integrity and embedded metadata in exact candidate JARs."""

from __future__ import annotations

import hashlib
import zipfile
from pathlib import Path, PurePosixPath
from typing import Literal

from mcpack_evidence.item3_jar_metadata import (
    FABRIC_PATH,
    JARJAR_PATH,
    TOML_PATHS,
    JarCoordinate,
    parse_fabric_metadata,
    parse_jarjar_metadata,
    parse_toml_metadata,
)
from mcpack_evidence.item3_jar_models import (
    CandidateJarInspection,
    DependencyDeclaration,
    EmbeddedLibrary,
    MetadataDocument,
    ModDeclaration,
)
from mcpack_evidence.item3_nested_jar import inspect_nested_jar

_MANIFEST_PATH = "META-INF/MANIFEST.MF"


def inspect_candidate_jar(
    candidate_filename: str,
    path: Path,
    expected_sha256: str,
) -> CandidateJarInspection:
    """Verify one archive and normalize all supported top-level metadata."""
    computed_sha256 = _sha256(path)
    try:
        archive = zipfile.ZipFile(path)
    except zipfile.BadZipFile:
        return _failed(candidate_filename, expected_sha256, computed_sha256, "bad_zip_file")
    with archive:
        names = tuple(info.filename for info in archive.infolist())
        issues = _integrity_issues(archive, names, expected_sha256, computed_sha256)
        documents = tuple(
            _document_identity(metadata_path, archive.read(metadata_path))
            for metadata_path in (*TOML_PATHS, FABRIC_PATH, JARJAR_PATH, _MANIFEST_PATH)
            if metadata_path in names
        )
        mods: list[ModDeclaration] = []
        dependencies: list[DependencyDeclaration] = []
        loaders: list[str] = []
        loader_ranges: list[str] = []
        fabric_environment: str | None = None
        embedded_paths = {
            name
            for name in names
            if name.endswith(".jar") and name.startswith(("META-INF/jars/", "META-INF/jarjar/"))
        }
        for metadata_path in TOML_PATHS:
            if metadata_path in names:
                parsed = parse_toml_metadata(archive.read(metadata_path), metadata_path)
                mods.extend(parsed.mods)
                dependencies.extend(parsed.dependencies)
                loaders.append(parsed.mod_loader)
                loader_ranges.append(parsed.loader_range)
        if FABRIC_PATH in names:
            parsed = parse_fabric_metadata(archive.read(FABRIC_PATH))
            mods.extend(parsed.mods)
            dependencies.extend(parsed.dependencies)
            loaders.append(parsed.mod_loader)
            fabric_environment = parsed.fabric_environment
            embedded_paths.update(parsed.embedded_paths)
        coordinates: dict[str, JarCoordinate] = {}
        if JARJAR_PATH in names:
            coordinates = parse_jarjar_metadata(archive.read(JARJAR_PATH))
            embedded_paths.update(coordinates)
        archive_role = _archive_role(archive, names, bool(mods))
        if archive_role == "library":
            loaders.append("fml_library")
        missing = sorted(embedded_paths - set(names))
        issues.extend(f"missing_embedded_path:{name}" for name in missing)
        embedded = tuple(
            _embedded_identity(name, archive.read(name), coordinates.get(name))
            for name in sorted(embedded_paths & set(names))
        )
        issues.extend(
            f"embedded:{row.path}:{issue}" for row in embedded for issue in row.nested_issues
        )
        issues.extend(
            "missing_supported_mod_metadata" for _ in [0] if not mods and archive_role != "library"
        )
        return CandidateJarInspection(
            candidate_filename=candidate_filename,
            expected_sha256=expected_sha256,
            computed_sha256=computed_sha256,
            zip_integrity="fail" if any(issue.startswith("zip_") for issue in issues) else "pass",
            inspection_status="fail" if issues else "pass",
            archive_role=archive_role,
            entry_count=len(names),
            duplicate_entry_count=len(names) - len(set(names)),
            unsafe_entries=tuple(name for name in names if _unsafe(name)),
            metadata_documents=documents,
            mod_loaders=tuple(dict.fromkeys(value for value in loaders if value)),
            loader_ranges=tuple(dict.fromkeys(value for value in loader_ranges if value)),
            mods=tuple(mods),
            dependencies=tuple(dependencies),
            minecraft_ranges=_dependency_ranges(dependencies, "minecraft"),
            neoforge_ranges=_dependency_ranges(dependencies, "neoforge"),
            fabric_environment=fabric_environment,
            embedded_libraries=embedded,
            issues=tuple(issues),
        )


def _integrity_issues(
    archive: zipfile.ZipFile,
    names: tuple[str, ...],
    expected_sha256: str,
    computed_sha256: str,
) -> list[str]:
    issues: list[str] = []
    if expected_sha256 != computed_sha256:
        issues.append("artifact_sha256_mismatch")
    bad_member = archive.testzip()
    if bad_member is not None:
        issues.append(f"zip_crc_failure:{bad_member}")
    if len(names) != len(set(names)):
        issues.append("zip_duplicate_entries")
    if any(_unsafe(name) for name in names):
        issues.append("zip_unsafe_entries")
    return issues


def _archive_role(
    archive: zipfile.ZipFile,
    names: tuple[str, ...],
    has_mods: bool,
) -> Literal["mod", "library", "unknown"]:
    if _MANIFEST_PATH in names:
        manifest_lines = archive.read(_MANIFEST_PATH).decode(errors="replace").splitlines()
        if any(line.strip().upper() == "FMLMODTYPE: LIBRARY" for line in manifest_lines):
            return "library"
    return "mod" if has_mods else "unknown"


def _unsafe(name: str) -> bool:
    path = PurePosixPath(name)
    return path.is_absolute() or ".." in path.parts


def _document_identity(path: str, body: bytes) -> MetadataDocument:
    return MetadataDocument(
        path=path,
        size_bytes=len(body),
        sha256=hashlib.sha256(body).hexdigest(),
    )


def _embedded_identity(path: str, body: bytes, entry: JarCoordinate | None) -> EmbeddedLibrary:
    nested = inspect_nested_jar(body)
    return EmbeddedLibrary(
        path=path,
        size_bytes=len(body),
        sha256=hashlib.sha256(body).hexdigest(),
        identifier=entry.identifier if entry else None,
        artifact_version=entry.artifact_version if entry else None,
        version_range=entry.version_range if entry else None,
        nested_zip_integrity=nested.zip_integrity,
        nested_metadata_paths=nested.metadata_paths,
        nested_mod_ids=tuple(dict.fromkeys(mod.mod_id for mod in nested.mods)),
        nested_dependencies=nested.dependencies,
        nested_issues=nested.issues,
    )


def _dependency_ranges(rows: list[DependencyDeclaration], mod_id: str) -> tuple[str, ...]:
    return tuple(
        dict.fromkeys(value for row in rows if row.mod_id == mod_id for value in row.version_ranges)
    )


def _failed(
    candidate_filename: str,
    expected_sha256: str,
    computed_sha256: str,
    issue: str,
) -> CandidateJarInspection:
    return CandidateJarInspection(
        candidate_filename=candidate_filename,
        expected_sha256=expected_sha256,
        computed_sha256=computed_sha256,
        zip_integrity="fail",
        inspection_status="fail",
        archive_role="unknown",
        entry_count=0,
        duplicate_entry_count=0,
        unsafe_entries=(),
        metadata_documents=(),
        mod_loaders=(),
        loader_ranges=(),
        mods=(),
        dependencies=(),
        minecraft_ranges=(),
        neoforge_ranges=(),
        fabric_environment=None,
        embedded_libraries=(),
        issues=(issue,),
    )


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        while block := stream.read(1024 * 1024):
            digest.update(block)
    return digest.hexdigest()
