from __future__ import annotations

import hashlib
import json
from typing import TYPE_CHECKING

from mcpack_evidence.item2 import (
    BaselineIdentity,
    build_baseline_manifest,
    validate_baseline_evidence,
)

if TYPE_CHECKING:
    from pathlib import Path


def _write_fixture(tmp_path: Path) -> tuple[Path, Path]:
    baseline_root = tmp_path / "baseline"
    baseline_root.mkdir()
    (baseline_root / "mods").mkdir()
    server_properties = baseline_root / "server.properties"
    _ = server_properties.write_text("level-name=world\n", encoding="utf-8")
    payload = server_properties.read_bytes()
    manifest_path = tmp_path / "baseline-manifest.json"
    _ = manifest_path.write_text(
        json.dumps(
            {
                "schema_version": "item2-baseline-v1",
                "minecraft": "1.21.1",
                "neoforge": "21.1.249",
                "java_vendor": "Eclipse Adoptium",
                "java_version": "21.0.12.1+1-LTS",
                "enabled_artifacts": [],
                "disabled_artifacts": [],
                "directories": ["mods"],
                "files": [
                    {
                        "path": "server.properties",
                        "size_bytes": len(payload),
                        "sha256": hashlib.sha256(payload).hexdigest(),
                    }
                ],
            }
        ),
        encoding="utf-8",
    )
    return manifest_path, baseline_root


def test_builds_deterministic_manifest_with_empty_directories(tmp_path: Path) -> None:
    # Given
    _, baseline_root = _write_fixture(tmp_path)

    # When
    manifest = build_baseline_manifest(
        baseline_root=baseline_root,
        identity=BaselineIdentity(
            minecraft="1.21.1",
            neoforge="21.1.249",
            java_vendor="Eclipse Adoptium",
            java_version="21.0.12.1+1-LTS",
            enabled_artifacts=(),
            disabled_artifacts=(),
        ),
    )

    # Then
    assert manifest.directories == ("mods",)
    assert tuple(record.path for record in manifest.files) == ("server.properties",)
    assert manifest.files[0].sha256 == hashlib.sha256(b"level-name=world\n").hexdigest()


def test_accepts_tree_when_every_manifest_identity_matches(tmp_path: Path) -> None:
    # Given
    manifest_path, baseline_root = _write_fixture(tmp_path)

    # When
    issues = validate_baseline_evidence(manifest_path, baseline_root)

    # Then
    assert issues == ()


def test_reports_hash_mismatch_when_frozen_file_changes(tmp_path: Path) -> None:
    # Given
    manifest_path, baseline_root = _write_fixture(tmp_path)
    _ = (baseline_root / "server.properties").write_text(
        "level-name=changed\n",
        encoding="utf-8",
    )

    # When
    issues = validate_baseline_evidence(manifest_path, baseline_root)

    # Then
    assert tuple(issue.code for issue in issues) == ("size_mismatch", "sha256_mismatch")


def test_reports_missing_empty_directory_when_frozen_tree_is_incomplete(tmp_path: Path) -> None:
    # Given
    manifest_path, baseline_root = _write_fixture(tmp_path)
    (baseline_root / "mods").rmdir()

    # When
    issues = validate_baseline_evidence(manifest_path, baseline_root)

    # Then
    assert tuple(issue.code for issue in issues) == ("missing_directory",)


def test_reports_unexpected_file_when_tree_contains_unmanifested_state(tmp_path: Path) -> None:
    # Given
    manifest_path, baseline_root = _write_fixture(tmp_path)
    _ = (baseline_root / "unexpected.txt").write_text("not frozen\n", encoding="utf-8")

    # When
    issues = validate_baseline_evidence(manifest_path, baseline_root)

    # Then
    assert tuple(issue.code for issue in issues) == ("unexpected_file",)


def test_rejects_manifest_path_that_escapes_frozen_root(tmp_path: Path) -> None:
    # Given
    manifest_path, baseline_root = _write_fixture(tmp_path)
    _ = (tmp_path / "outside.txt").write_text("level-name=world\n", encoding="utf-8")
    unsafe_manifest = manifest_path.read_text(encoding="utf-8").replace(
        '"path": "server.properties"',
        '"path": "../outside.txt"',
    )
    _ = manifest_path.write_text(unsafe_manifest, encoding="utf-8")

    # When
    issues = validate_baseline_evidence(manifest_path, baseline_root)

    # Then
    assert tuple(issue.code for issue in issues) == ("unsafe_path", "unexpected_file")


def test_reports_unexpected_empty_directory_when_tree_has_unfrozen_state(tmp_path: Path) -> None:
    # Given
    manifest_path, baseline_root = _write_fixture(tmp_path)
    (baseline_root / "unrecorded").mkdir()

    # When
    issues = validate_baseline_evidence(manifest_path, baseline_root)

    # Then
    assert tuple(issue.code for issue in issues) == ("unexpected_directory",)


def test_preserves_declared_then_unexpected_issue_order_when_failures_coexist(
    tmp_path: Path,
) -> None:
    # Given
    manifest_path, baseline_root = _write_fixture(tmp_path)
    _ = (baseline_root / "server.properties").write_text(
        "level-name=changed\n",
        encoding="utf-8",
    )
    (baseline_root / "mods").rmdir()
    _ = (baseline_root / "unexpected.txt").write_text("not frozen\n", encoding="utf-8")
    (baseline_root / "unrecorded").mkdir()

    # When
    issues = validate_baseline_evidence(manifest_path, baseline_root)

    # Then
    assert tuple(issue.code for issue in issues) == (
        "size_mismatch",
        "sha256_mismatch",
        "missing_directory",
        "unexpected_file",
        "unexpected_directory",
    )
