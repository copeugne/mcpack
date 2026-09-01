from __future__ import annotations

import json
from typing import TYPE_CHECKING

from mcpack_evidence.item3 import (
    build_search_queries,
    find_exact_modrinth_file,
    validate_candidate_matrix,
)

if TYPE_CHECKING:
    from pathlib import Path


def test_builds_search_queries_without_loader_or_version_noise() -> None:
    # Given
    filename = "DungeonsAriseSevenSeas-1.21.x-1.0.4-neoforge.jar"

    # When
    queries = build_search_queries(filename)

    # Then
    assert queries[0] == "DungeonsAriseSevenSeas"
    assert "Dungeons Arise Seven Seas" in queries


def test_splits_acronym_from_following_project_word() -> None:
    # Given
    filename = "EMIProfessions-neoforge-1.21.1-1.0.3.jar"

    # When
    queries = build_search_queries(filename)

    # Then
    assert "EMI Professions" in queries


def test_finds_only_the_exact_candidate_filename() -> None:
    # Given
    versions = [
        {
            "id": "wrong",
            "files": [{"filename": "DungeonsAriseSevenSeas-1.21.x-1.0.3-neoforge.jar"}],
        },
        {
            "id": "exact",
            "files": [{"filename": "DungeonsAriseSevenSeas-1.21.x-1.0.4-neoforge.jar"}],
        },
    ]

    # When
    match = find_exact_modrinth_file(
        "DungeonsAriseSevenSeas-1.21.x-1.0.4-neoforge.jar",
        versions,
    )

    # Then
    assert match is not None
    assert match.version_id == "exact"


def test_accepts_disabled_suffix_when_matching_upstream_filename() -> None:
    # Given
    versions = [
        {
            "id": "exact",
            "files": [{"filename": "DistantHorizons-3.0.3-b-1.21.1-fabric-neoforge.jar"}],
        }
    ]

    # When
    match = find_exact_modrinth_file(
        "DistantHorizons-3.0.3-b-1.21.1-fabric-neoforge.jar.disabled",
        versions,
    )

    # Then
    assert match is not None
    assert match.filename.endswith(".jar")


def test_rejects_matrix_with_missing_candidate(tmp_path: Path) -> None:
    # Given
    inventory = tmp_path / "candidates.txt"
    _ = inventory.write_text("one.jar\ntwo.jar\n", encoding="utf-8")
    matrix = tmp_path / "matrix.json"
    _ = matrix.write_text(
        json.dumps(
            {
                "schema_version": "item3-compatibility-matrix-v1",
                "target": {"minecraft": "1.21.1", "loader": "neoforge"},
                "baseline_enabled_artifacts": [],
                "candidates": [_candidate_row("one.jar")],
            }
        ),
        encoding="utf-8",
    )

    # When
    issues = validate_candidate_matrix(matrix, inventory)

    # Then
    assert tuple(issue.code for issue in issues) == ("candidate_set_mismatch",)


def test_rejects_unsupported_artifact_admitted_to_baseline(tmp_path: Path) -> None:
    # Given
    inventory = tmp_path / "candidates.txt"
    _ = inventory.write_text("wrong-point-release.jar\n", encoding="utf-8")
    row = _candidate_row("wrong-point-release.jar", minecraft="fail")
    row["disposition"] = "reject_unsupported"
    matrix = tmp_path / "matrix.json"
    _ = matrix.write_text(
        json.dumps(
            {
                "schema_version": "item3-compatibility-matrix-v1",
                "target": {"minecraft": "1.21.1", "loader": "neoforge"},
                "baseline_enabled_artifacts": ["wrong-point-release.jar"],
                "candidates": [row],
            }
        ),
        encoding="utf-8",
    )

    # When
    issues = validate_candidate_matrix(matrix, inventory)

    # Then
    assert tuple(issue.code for issue in issues) == ("unsupported_enabled",)


def _candidate_row(filename: str, *, minecraft: str = "pass") -> dict[str, object]:
    return {
        "candidate_filename": filename,
        "proposed_state": "enabled",
        "source": {
            "platform": "modrinth",
            "project_id": "project",
            "version_id": "version",
            "file_id": None,
            "source_url": "https://api.modrinth.com/v2/version/version",
            "retrieved_at": "2026-09-01T00:00:00Z",
        },
        "artifact": {
            "exact_filename": filename,
            "size_bytes": 1,
            "publisher_hashes": {"sha512": "a" * 128},
            "computed_sha256": None,
        },
        "declared": {
            "game_versions": ["1.21.1"],
            "loaders": ["neoforge"],
            "client_side": "unknown",
            "server_side": "unknown",
            "dependencies": [],
        },
        "embedded": None,
        "hazards": [],
        "compatibility": {
            "minecraft": minecraft,
            "loader": "pass",
            "dependencies": "pass",
            "side": "unverified",
            "embedded_overlap": "unverified",
        },
        "disposition": "defer_not_admitted",
        "rationale": "Candidate is audited but not admitted to the zero-mod control.",
        "limitations": [],
    }
