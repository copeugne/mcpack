from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest

from mcpack_evidence.item3_source_models import SourceEvidenceError
from mcpack_evidence.item3_sources import build_source_matrix

if TYPE_CHECKING:
    from pathlib import Path


def test_builds_complete_cross_platform_source_matrix(tmp_path: Path) -> None:
    # Given
    inventory = _write(tmp_path / "inventory.txt", "alpha.jar\nbeta.jar\n")
    modrinth = _write_json(
        tmp_path / "modrinth.json",
        {
            "retrieved_at": "2026-09-01T00:00:00Z",
            "rows": [
                {
                    "candidate_filename": "alpha.jar",
                    "resolved": True,
                    "project": {
                        "id": "project-a",
                        "slug": "alpha",
                        "title": "Alpha",
                        "license": {"id": "MIT", "name": "MIT", "url": None},
                        "client_side": "optional",
                        "server_side": "required",
                    },
                    "version": {
                        "id": "version-a",
                        "name": "Alpha 1",
                        "version_number": "1",
                        "date_published": "2026-01-01T00:00:00Z",
                        "version_type": "release",
                        "game_versions": ["1.21.1"],
                        "loaders": ["neoforge"],
                        "dependencies": [],
                    },
                    "file": {
                        "id": "file-a",
                        "filename": "alpha.jar",
                        "size": 10,
                        "url": "https://cdn.modrinth.com/alpha.jar",
                        "hashes": {"sha1": "a" * 40, "sha512": "b" * 128},
                    },
                }
            ],
        },
    )
    curseforge = _write_json(
        tmp_path / "curseforge.json",
        {
            "retrieved_at": "2026-09-01T01:00:00Z",
            "rows": [
                {
                    "candidate_filename": "beta.jar",
                    "project_id": 2,
                    "file_id": 3,
                    "source_url": "https://www.curseforge.com/api/v1/mods/2/files/3",
                    "file_page_url": ("https://www.curseforge.com/minecraft/mc-mods/beta/files/3"),
                    "cdn_url": "https://edge.forgecdn.net/files/0/003/beta.jar",
                    "record": {
                        "id": 3,
                        "fileName": "beta.jar",
                        "fileLength": 20,
                        "gameVersions": ["1.21.1", "NeoForge", "Client", "Server"],
                        "releaseType": 1,
                        "dateCreated": "2026-01-02T00:00:00Z",
                    },
                }
            ],
        },
    )

    # When
    matrix = build_source_matrix(inventory, modrinth, curseforge)

    # Then
    assert matrix.inventory_count == 2
    assert tuple(row.candidate_filename for row in matrix.candidates) == (
        "alpha.jar",
        "beta.jar",
    )
    assert matrix.candidates[0].artifact.publisher_hashes["sha512"] == "b" * 128
    assert matrix.candidates[1].declared.loaders == ("neoforge",)
    assert matrix.candidates[1].artifact.publisher_hashes == {}
    assert "publisher_hashes_unavailable" in matrix.candidates[1].limitations


def test_rejects_unresolved_candidate(tmp_path: Path) -> None:
    # Given
    inventory = _write(tmp_path / "inventory.txt", "missing.jar\n")
    modrinth = _write_json(
        tmp_path / "modrinth.json",
        {
            "retrieved_at": "2026-09-01T00:00:00Z",
            "rows": [{"candidate_filename": "missing.jar", "resolved": False}],
        },
    )
    curseforge = _write_json(
        tmp_path / "curseforge.json",
        {"retrieved_at": "2026-09-01T00:00:00Z", "rows": []},
    )

    # When / Then
    with pytest.raises(SourceEvidenceError, match=r"missing\.jar"):
        _ = build_source_matrix(inventory, modrinth, curseforge)


def _write(path: Path, content: str) -> Path:
    _ = path.write_text(content, encoding="utf-8")
    return path


def _write_json(path: Path, content: object) -> Path:
    return _write(path, json.dumps(content))
