from __future__ import annotations

import hashlib
import json
from typing import TYPE_CHECKING

import pytest
from tools.manage_item4_environment import backup, materialize, restore

if TYPE_CHECKING:
    from pathlib import Path


def test_backup_and_restore_round_trip_is_hash_verified(tmp_path: Path) -> None:
    world = tmp_path / "source-world"
    (world / "region").mkdir(parents=True)
    _ = (world / "level.dat").write_bytes(b"level")
    _ = (world / "region" / "r.0.0.mca").write_bytes(b"region")
    archive = tmp_path / "world.tar.gz"
    receipt_path = tmp_path / "receipt.json"

    receipt = backup(world, archive, receipt_path)
    restored = restore(archive, receipt["archive_sha256"], tmp_path / "restore")

    assert json.loads(receipt_path.read_text()) == receipt
    assert restored["world_file_count"] == 2
    assert (tmp_path / "restore/world/level.dat").read_bytes() == b"level"
    assert (tmp_path / "restore/world/region/r.0.0.mca").read_bytes() == b"region"


def test_restore_rejects_wrong_hash_and_existing_target(tmp_path: Path) -> None:
    world = tmp_path / "world"
    world.mkdir()
    _ = (world / "level.dat").write_bytes(b"level")
    archive = tmp_path / "world.tar.gz"
    receipt = backup(world, archive, tmp_path / "receipt.json")

    with pytest.raises(ValueError, match="SHA-256 mismatch"):
        _ = restore(archive, "0" * 64, tmp_path / "wrong-hash")
    existing = tmp_path / "existing"
    existing.mkdir()
    with pytest.raises(ValueError, match="target must be absent"):
        _ = restore(archive, receipt["archive_sha256"], existing)


def test_backup_refuses_non_world_and_existing_archive(tmp_path: Path) -> None:
    empty = tmp_path / "empty"
    empty.mkdir()
    with pytest.raises(ValueError, match=r"level\.dat"):
        _ = backup(empty, tmp_path / "backup.tar.gz", tmp_path / "receipt.json")

    _ = (empty / "level.dat").write_bytes(b"level")
    archive = tmp_path / "backup.tar.gz"
    _ = archive.write_bytes(b"preserve")
    with pytest.raises(ValueError, match="target must be absent"):
        _ = backup(empty, archive, tmp_path / "receipt.json")


def test_materialize_accepts_existing_empty_pristine_mods(tmp_path: Path) -> None:
    pristine = tmp_path / "pristine"
    _ = (pristine / "mods").mkdir(parents=True)
    _ = (pristine / "server.properties").write_text("level-name=old\n")
    artifact = tmp_path / "example.jar"
    _ = artifact.write_bytes(b"artifact")
    artifact_hash = hashlib.sha256(b"artifact").hexdigest()
    acquisition = tmp_path / "acquisition.json"
    _ = acquisition.write_text(
        json.dumps(
            {
                "artifacts": [
                    {
                        "candidate_filename": "example.jar",
                        "local_path": str(artifact),
                        "identity": {"size_bytes": 8, "computed_sha256": artifact_hash},
                    }
                ]
            }
        )
    )
    retained = tmp_path / "retained.txt"
    _ = retained.write_text("example.jar\n")
    seeds = tmp_path / "seeds.json"
    _ = seeds.write_text(json.dumps({"seeds": [{"role": "ordinary", "seed": "42"}]}))

    receipt = materialize(pristine, acquisition, retained, seeds, "ordinary", tmp_path / "out")

    assert receipt["retained_candidate_count"] == 1
    assert (tmp_path / "out/mods/example.jar").read_bytes() == b"artifact"
