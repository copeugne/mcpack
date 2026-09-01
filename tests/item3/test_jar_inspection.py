from __future__ import annotations

import hashlib
import io
import zipfile
from typing import TYPE_CHECKING

from mcpack_evidence.item3_jar import inspect_candidate_jar

if TYPE_CHECKING:
    from pathlib import Path


def test_extracts_neoforge_dependencies_and_embedded_identity(tmp_path: Path) -> None:
    # Given
    artifact = tmp_path / "candidate.jar"
    nested = _nested_jar()
    metadata = b"""
modLoader = "javafml"
loaderVersion = "[4,)"
[[mods]]
modId = "example"
version = "1.0"
[[dependencies.example]]
modId = "minecraft"
type = "required"
versionRange = "[1.21,1.22)"
side = "BOTH"
[[dependencies.example]]
modId = "helper"
type = "optional"
versionRange = "[2,)"
side = "SERVER"
"""
    jarjar = b"""{
      "jars": [{
        "identifier": {"group": "example.group", "artifact": "nested"},
        "version": {"range": "[1.0,)", "artifactVersion": "1.0"},
        "path": "META-INF/jarjar/nested-1.0.jar"
      }]
    }"""
    with zipfile.ZipFile(artifact, "w") as archive:
        archive.writestr("META-INF/neoforge.mods.toml", metadata)
        archive.writestr("META-INF/jarjar/metadata.json", jarjar)
        archive.writestr("META-INF/jarjar/nested-1.0.jar", nested)

    # When
    result = inspect_candidate_jar(
        "candidate.jar",
        artifact,
        hashlib.sha256(artifact.read_bytes()).hexdigest(),
    )

    # Then
    assert result.inspection_status == "pass"
    assert tuple(mod.mod_id for mod in result.mods) == ("example",)
    assert result.minecraft_ranges == ("[1.21,1.22)",)
    assert tuple(dependency.mod_id for dependency in result.dependencies) == (
        "minecraft",
        "helper",
    )
    assert result.embedded_libraries[0].identifier == "example.group:nested"
    assert len(result.embedded_libraries[0].sha256) == 64
    assert result.embedded_libraries[0].nested_mod_ids == ("nested_mod",)


def test_extracts_fabric_environment_and_dependency_ranges(tmp_path: Path) -> None:
    # Given
    artifact = tmp_path / "fabric.jar"
    metadata = b"""{
      "schemaVersion": 1,
      "id": "fabric_example",
      "version": "1.0",
      "name": "Fabric Example",
      "environment": "client",
      "depends": {"minecraft": [">=1.21", "<1.22"], "fabricloader": ">=0.16"},
      "suggests": {"helper": "*"}
    }"""
    with zipfile.ZipFile(artifact, "w") as archive:
        archive.writestr("fabric.mod.json", metadata)

    # When
    result = inspect_candidate_jar(
        "fabric.jar",
        artifact,
        hashlib.sha256(artifact.read_bytes()).hexdigest(),
    )

    # Then
    assert result.inspection_status == "pass"
    assert result.fabric_environment == "client"
    assert result.minecraft_ranges == (">=1.21", "<1.22")
    assert tuple(dependency.kind for dependency in result.dependencies) == (
        "required",
        "required",
        "suggested",
    )


def test_records_corrupt_archive_as_failed_inspection(tmp_path: Path) -> None:
    # Given
    artifact = tmp_path / "corrupt.jar"
    _ = artifact.write_bytes(b"not a zip archive")

    # When
    result = inspect_candidate_jar("corrupt.jar", artifact, "c" * 64)

    # Then
    assert result.inspection_status == "fail"
    assert result.zip_integrity == "fail"
    assert result.issues == ("bad_zip_file",)


def test_preserves_unquoted_dotted_dependency_owner(tmp_path: Path) -> None:
    # Given
    artifact = tmp_path / "dotted.jar"
    metadata = b"""
modLoader = "javafml"
loaderVersion = "[4,)"
[[mods]]
modId = "modelfix"
version = "1.21-1.10"
[[dependencies.1.21-1.10]]
modId = "minecraft"
mandatory = true
versionRange = "[1.21,1.22)"
side = "CLIENT"
"""
    with zipfile.ZipFile(artifact, "w") as archive:
        archive.writestr("META-INF/neoforge.mods.toml", metadata)

    # When
    result = inspect_candidate_jar(
        "dotted.jar",
        artifact,
        hashlib.sha256(artifact.read_bytes()).hexdigest(),
    )

    # Then
    assert result.inspection_status == "pass"
    assert result.dependencies[0].owner_mod_id == "1.21-1.10"


def test_accepts_fml_library_without_mod_declaration(tmp_path: Path) -> None:
    # Given
    artifact = tmp_path / "library.jar"
    nested = _nested_jar()
    jarjar = b"""{
      "jars": [{
        "identifier": {"group": "example", "artifact": "library"},
        "version": {"range": "[1,)", "artifactVersion": "1"},
        "path": "META-INF/jarjar/library.jar"
      }]
    }"""
    with zipfile.ZipFile(artifact, "w") as archive:
        archive.writestr("META-INF/MANIFEST.MF", b"Manifest-Version: 1.0\nFMLModType: LIBRARY\n")
        archive.writestr("META-INF/jarjar/metadata.json", jarjar)
        archive.writestr("META-INF/jarjar/library.jar", nested)

    # When
    result = inspect_candidate_jar(
        "library.jar",
        artifact,
        hashlib.sha256(artifact.read_bytes()).hexdigest(),
    )

    # Then
    assert result.inspection_status == "pass"
    assert result.archive_role == "library"
    assert result.mods == ()


def _nested_jar() -> bytes:
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w") as archive:
        archive.writestr(
            "META-INF/neoforge.mods.toml",
            b"""modLoader="javafml"
loaderVersion="[4,)"
[[mods]]
modId="nested_mod"
version="1"
""",
        )
    return buffer.getvalue()
