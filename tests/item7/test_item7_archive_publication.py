from __future__ import annotations

import tarfile
from typing import TYPE_CHECKING, cast

import pytest

import mcpack_evidence.item7_archive as archive
import mcpack_evidence.item7_archive_restore as archive_restore
from mcpack_evidence.item7_stage_output import StagingTree

if TYPE_CHECKING:
    from collections.abc import Callable
    from pathlib import Path, PurePosixPath
    from typing import IO

    from mcpack_evidence.item7_archive_io import OpenedFile
    from mcpack_evidence.item7_archive_publish import TemporaryFile


def _create_request(root: Path, archive_name: str) -> archive.ArchiveRequest:
    raw = root / "raw"
    raw.mkdir(parents=True)
    _ = (raw / "evidence.txt").write_bytes(b"evidence")
    return archive.ArchiveRequest(raw, root / archive_name, root / "manifest.json", "qa-item7")


def _restore_request(root: Path, created: archive.ArchiveRequest) -> archive.RestoreRequest:
    return archive.RestoreRequest(
        created.archive, created.manifest, root / "restored", root / "restore.json"
    )


def test_restore_refuses_concurrently_created_target(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    created = _create_request(tmp_path, "item7-raw-race.tar.gz")
    _ = archive.create_archive(created)
    request = _restore_request(tmp_path, created)
    original_write = cast(
        "Callable[[StagingTree, PurePosixPath, IO[bytes], int], None]", StagingTree.write
    )
    created_target = False

    def inject_target(
        tree: StagingTree, relative: PurePosixPath, source: IO[bytes], size: int
    ) -> None:
        nonlocal created_target
        if not created_target:
            request.target.mkdir()
            created_target = True
        original_write(tree, relative, source, size)

    monkeypatch.setattr(StagingTree, "write", inject_target)

    with pytest.raises(FileExistsError):
        _ = archive.restore_archive(request)

    assert created_target
    assert request.target.is_dir()
    assert not request.receipt.exists()


@pytest.mark.parametrize("destination", ["target", "receipt"])
def test_restore_does_not_create_nested_parent_through_symlink(
    tmp_path: Path, destination: str
) -> None:
    created = _create_request(tmp_path / "created", f"item7-raw-nested-{destination}.tar.gz")
    _ = archive.create_archive(created)
    external = tmp_path / "external"
    external.mkdir()
    alias = tmp_path / "output-alias"
    alias.symlink_to(external, target_is_directory=True)
    escaped = external / "created-outside"
    target = alias / escaped.name / "restored" if destination == "target" else tmp_path / "restored"
    receipt = (
        alias / escaped.name / "restore.json"
        if destination == "receipt"
        else tmp_path / "receipt.json"
    )
    request = archive.RestoreRequest(created.archive, created.manifest, target, receipt)

    with pytest.raises(archive.ArchiveValidationError, match="unsafe"):
        _ = archive.restore_archive(request)

    assert not escaped.exists()
    assert not receipt.exists()


def test_restore_rejects_target_replaced_before_receipt_publication(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    created = _create_request(tmp_path / "created", "item7-raw-target-swap.tar.gz")
    _ = archive.create_archive(created)
    target_parent = tmp_path / "target-parent"
    target_parent.mkdir()
    request = archive.RestoreRequest(
        created.archive, created.manifest, target_parent / "restored", tmp_path / "receipt.json"
    )
    displaced = target_parent / "verified"
    original_stage = cast(
        "Callable[[int, bytes], TemporaryFile]",
        archive_restore.__dict__["stage_bytes"],
    )

    def replace_target(directory: int, body: bytes) -> TemporaryFile:
        temporary = original_stage(directory, body)
        _ = request.target.rename(displaced)
        request.target.mkdir()
        _ = (request.target / "evidence.txt").write_bytes(b"attacker")
        return temporary

    monkeypatch.setattr(archive_restore, "stage_bytes", replace_target)

    with pytest.raises(archive.ArchiveValidationError, match="unsafe"):
        _ = archive.restore_archive(request)

    assert (request.target / "evidence.txt").read_bytes() == b"attacker"
    assert (displaced / "evidence.txt").read_bytes() == b"evidence"
    assert not request.receipt.exists()


def test_restore_rejects_receipt_parent_replaced_during_publication(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    created = _create_request(tmp_path / "created", "item7-raw-receipt-swap.tar.gz")
    _ = archive.create_archive(created)
    receipt_parent = tmp_path / "receipts"
    receipt_parent.mkdir()
    request = archive.RestoreRequest(
        created.archive, created.manifest, tmp_path / "restored", receipt_parent / "restore.json"
    )
    displaced = tmp_path / "verified-receipts"
    original_stage = cast(
        "Callable[[int, bytes], TemporaryFile]",
        archive_restore.__dict__["stage_bytes"],
    )

    def replace_parent(directory: int, body: bytes) -> TemporaryFile:
        temporary = original_stage(directory, body)
        _ = receipt_parent.rename(displaced)
        receipt_parent.mkdir()
        return temporary

    monkeypatch.setattr(archive_restore, "stage_bytes", replace_parent)

    with pytest.raises(archive.ArchiveValidationError, match="unsafe"):
        _ = archive.restore_archive(request)

    assert not request.receipt.exists()
    assert not (displaced / request.receipt.name).exists()


def test_create_rejects_output_parent_replaced_after_tar_build(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    output_parent = tmp_path / "output"
    request = _create_request(output_parent, "item7-raw-output-race.tar.gz")
    displaced = tmp_path / "displaced-output"
    original_build = cast(
        "Callable[[int, tuple[OpenedFile, ...]], TemporaryFile]",
        archive.__dict__["build_tar"],
    )

    def replace_parent(directory: int, files: tuple[OpenedFile, ...]) -> TemporaryFile:
        temporary = original_build(directory, files)
        _ = output_parent.rename(displaced)
        output_parent.mkdir()
        attacker = output_parent / "attacker"
        _ = attacker.write_bytes(b"attacker")
        with tarfile.open(output_parent / temporary.name, "w:gz") as bundle:
            bundle.add(attacker, arcname="evil")
        return temporary

    monkeypatch.setattr(archive, "build_tar", replace_parent)

    with pytest.raises(archive.ArchiveValidationError, match="unsafe"):
        _ = archive.create_archive(request)

    assert not request.archive.exists()
    assert not request.manifest.exists()


@pytest.mark.parametrize("output", ["archive", "manifest"])
def test_create_does_not_create_nested_output_parent_through_symlink(
    tmp_path: Path, output: str
) -> None:
    raw = tmp_path / "raw"
    raw.mkdir()
    _ = (raw / "evidence.txt").write_bytes(b"evidence")
    external = tmp_path / "external"
    external.mkdir()
    alias = tmp_path / "output-alias"
    alias.symlink_to(external, target_is_directory=True)
    escaped = external / "created-outside"
    archive_path = tmp_path / "item7-safe.tar.gz"
    manifest_path = tmp_path / "safe-manifest.json"
    if output == "archive":
        archive_path = alias / escaped.name / "item7-unsafe.tar.gz"
    else:
        manifest_path = alias / escaped.name / "unsafe-manifest.json"
    request = archive.ArchiveRequest(raw, archive_path, manifest_path, "qa-item7")

    with pytest.raises(archive.ArchiveValidationError, match="symlink"):
        _ = archive.create_archive(request)

    assert not escaped.exists()
    assert not archive_path.exists()
    assert not manifest_path.exists()
