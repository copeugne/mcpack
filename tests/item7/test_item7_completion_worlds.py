from __future__ import annotations

import hashlib
import json
from typing import TYPE_CHECKING

import pytest

from mcpack_evidence.item7_completion_io import CompletionError
from mcpack_evidence.item7_completion_other import validate_archives
from mcpack_evidence.item7_world_archive_inventory import (
    WorldArchiveSource,
    build_world_archive_inventory,
)

if TYPE_CHECKING:
    from pathlib import Path

    from pydantic import JsonValue


def _archive_pair(
    root: Path,
    index: int,
    name: str,
    relative_path: str | None,
) -> tuple[Path, Path]:
    manifest = root / f"manifest-{index}.json"
    files: list[JsonValue] = []
    if relative_path is not None:
        files.append(
            {
                "relative_path": relative_path,
                "size_bytes": 8192,
                "sha256": "c" * 64,
            }
        )
    payload: dict[str, JsonValue] = {
        "schema_version": "item7-raw-evidence-archive-v1",
        "revision": "a" * 40,
        "archive_name": name,
        "archive_size_bytes": 0,
        "archive_sha256": "b" * 64,
        "file_count": len(files),
        "total_size_bytes": 8192 * len(files),
        "files": files,
    }
    _ = manifest.write_text(json.dumps(payload), encoding="utf-8")
    receipt = root / f"receipt-{index}.json"
    _ = receipt.write_text(
        json.dumps(
            {
                "schema_version": "item7-raw-evidence-restore-v1",
                "revision": "a" * 40,
                "archive_name": name,
                "archive_sha256": "b" * 64,
                "manifest_sha256": hashlib.sha256(manifest.read_bytes()).hexdigest(),
                "restored_target": str(root / f"restore-{index}"),
                "file_count": len(files),
                "total_size_bytes": 8192 * len(files),
                "verified": True,
            }
        ),
        encoding="utf-8",
    )
    return manifest, receipt


def test_world_archive_inventory_hashes_every_staged_file(tmp_path: Path) -> None:
    sources: list[WorldArchiveSource] = []
    for index, label in enumerate(("run-a", "run-b", "auxiliary")):
        root = tmp_path / label
        file = root / f"world-{index}/region/r.0.0.mca"
        file.parent.mkdir(parents=True)
        _ = file.write_bytes(label.encode())
        sources.append(WorldArchiveSource(root, f"mcpack-item7-raw-{label}-worlds-r4.tar.gz"))

    report = build_world_archive_inventory((sources[0], sources[1], sources[2]))

    assert tuple(row.archive_name for row in report.archives) == tuple(
        source.archive_name for source in sources
    )
    assert tuple(row.files[0].sha256 for row in report.archives) == tuple(
        hashlib.sha256(label.encode()).hexdigest() for label in ("run-a", "run-b", "auxiliary")
    )
    assert build_world_archive_inventory((sources[0], sources[1], sources[2])) == report


def test_completion_rejects_world_archive_missing_expected_region(tmp_path: Path) -> None:
    definitions = (
        ("mcpack-item7-raw-core-r4.tar.gz", None),
        (
            "mcpack-item7-raw-run-a-worlds-r4.tar.gz",
            "run-a-ordinary/world/region/r.1.0.mca",
        ),
        (
            "mcpack-item7-raw-run-b-worlds-r4.tar.gz",
            "run-b-ordinary/world/region/r.0.0.mca",
        ),
        (
            "mcpack-item7-raw-auxiliary-worlds-r4.tar.gz",
            "control/world/region/r.0.0.mca",
        ),
    )
    pairs = tuple(
        _archive_pair(tmp_path, index, name, relative_path)
        for index, (name, relative_path) in enumerate(definitions)
    )
    inventory = tmp_path / "world-archive-inventory.json"
    _ = inventory.write_text(
        json.dumps(
            {
                "schema_version": "item7-world-archive-inventory-v1",
                "archives": [
                    {
                        "archive_name": "mcpack-item7-raw-run-a-worlds-r4.tar.gz",
                        "files": [
                            {
                                "relative_path": "run-a-ordinary/world/region/r.0.0.mca",
                                "size_bytes": 8192,
                                "sha256": "c" * 64,
                            }
                        ],
                    },
                    {
                        "archive_name": "mcpack-item7-raw-run-b-worlds-r4.tar.gz",
                        "files": [
                            {
                                "relative_path": "run-b-ordinary/world/region/r.0.0.mca",
                                "size_bytes": 8192,
                                "sha256": "c" * 64,
                            }
                        ],
                    },
                    {
                        "archive_name": "mcpack-item7-raw-auxiliary-worlds-r4.tar.gz",
                        "files": [
                            {
                                "relative_path": "control/world/region/r.0.0.mca",
                                "size_bytes": 8192,
                                "sha256": "c" * 64,
                            }
                        ],
                    },
                ],
            }
        ),
        encoding="utf-8",
    )

    with pytest.raises(
        CompletionError,
        match=r"world archive inventory: mcpack-item7-raw-run-a-worlds-r4\.tar\.gz",
    ):
        _ = validate_archives(
            tuple(pair[0] for pair in pairs),
            tuple(pair[1] for pair in pairs),
            (),
            inventory,
        )
