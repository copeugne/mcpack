from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from typing import TYPE_CHECKING, TextIO, cast

import pytest
import tools.manage_item4_environment as environment_manager
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
    _ = (pristine / "world").mkdir()
    _ = (pristine / "world/level.dat").write_bytes(b"copied baseline world")
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
    assert receipt["copied_world_removed"] is True
    assert (tmp_path / "out/mods/example.jar").read_bytes() == b"artifact"
    assert not (tmp_path / "out/world").exists()


def test_backup_refuses_minecraft_compatible_posix_record_lock(tmp_path: Path) -> None:
    world = tmp_path / "world"
    world.mkdir()
    _ = (world / "level.dat").write_bytes(b"level")
    lock_path = world / "session.lock"
    _ = lock_path.write_bytes(b"lock")
    locker: subprocess.Popen[str] = subprocess.Popen(  # noqa: S603
        [
            sys.executable,
            "-c",
            (
                "import fcntl,sys,time; "
                "f=open(sys.argv[1], 'r+b'); "
                "fcntl.lockf(f, fcntl.LOCK_EX); "
                "print('locked', flush=True); "
                "time.sleep(30)"
            ),
            str(lock_path),
        ],
        stdout=subprocess.PIPE,
        text=True,
    )
    stdout = cast("TextIO", locker.stdout)
    try:
        assert stdout.readline().strip() == "locked"
        with pytest.raises(ValueError, match="world is active"):
            _ = backup(world, tmp_path / "backup.tar.gz", tmp_path / "receipt.json")
    finally:
        locker.terminate()
        _ = locker.wait(timeout=5)
        stdout.close()


def test_backup_holds_record_lock_through_receipt_hashing(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    world = tmp_path / "world"
    world.mkdir()
    _ = (world / "level.dat").write_bytes(b"level")
    observed: list[str] = []
    original = environment_manager._file_row  # pyright: ignore[reportPrivateUsage]

    def observe_lock(path: Path, root: Path) -> dict[str, object]:
        if not observed:
            probe = subprocess.run(  # noqa: S603
                [
                    sys.executable,
                    "-c",
                    (
                        "import fcntl,sys; f=open(sys.argv[1], 'r+b'); "
                        "\ntry: fcntl.lockf(f, fcntl.LOCK_EX | fcntl.LOCK_NB); print('acquired')"
                        "\nexcept BlockingIOError: print('blocked')"
                    ),
                    str(world / "session.lock"),
                ],
                check=True,
                capture_output=True,
                text=True,
            )
            observed.append(probe.stdout.strip())
        return original(path, root)

    monkeypatch.setattr(environment_manager, "_file_row", observe_lock)

    _ = backup(world, tmp_path / "backup.tar.gz", tmp_path / "receipt.json")

    assert observed == ["blocked"]
