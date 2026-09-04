from __future__ import annotations

import tarfile
from typing import TYPE_CHECKING, cast

import pytest

import mcpack_evidence.item7_archive as archive
from mcpack_evidence.item7_archive_io import (
    duplicate_stream as open_descriptor_stream,
)
from mcpack_evidence.item7_stage_output import StagingTree

if TYPE_CHECKING:
    from collections.abc import Callable
    from pathlib import Path, PurePosixPath
    from typing import IO, BinaryIO

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
        "Callable[[StagingTree, PurePosixPath, IO[bytes], int], None]",
        StagingTree.write,
    )
    created_target = False

    def inject_competing_target(
        tree: StagingTree,
        relative: PurePosixPath,
        source: IO[bytes],
        size: int,
    ) -> None:
        nonlocal created_target
        if not created_target:
            request.target.mkdir()
            created_target = True
        original_write(tree, relative, source, size)

    monkeypatch.setattr(StagingTree, "write", inject_competing_target)

    with pytest.raises(FileExistsError):
        _ = archive.restore_archive(request)

    assert created_target
    assert request.target.is_dir()
    assert not request.receipt.exists()


def test_manifest_binds_bytes_archived_after_source_change(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    raw = tmp_path / "raw"
    raw.mkdir()
    source = raw / "evidence.bin"
    _ = source.write_bytes(b"first")
    mutated = False

    def mutate_before_read(descriptor: int) -> BinaryIO:
        nonlocal mutated
        if not mutated:
            source.unlink()
            source.symlink_to(tmp_path / "outside")
            mutated = True
        return open_descriptor_stream(descriptor)

    monkeypatch.setattr(archive, "duplicate_stream", mutate_before_read)
    request = archive.ArchiveRequest(
        raw, tmp_path / "item7-raw-race.tar.gz", tmp_path / "manifest.json", "qa-item7"
    )

    _ = archive.create_archive(request)
    restore = _restore_request(tmp_path, request)
    _ = archive.restore_archive(restore)

    assert (restore.target / "evidence.bin").read_bytes() == b"first"


def test_archive_keeps_nested_directory_identity_after_path_swap(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    raw = tmp_path / "raw"
    nested = raw / "nested"
    nested.mkdir(parents=True)
    _ = (nested / "evidence.bin").write_bytes(b"trusted")
    external = tmp_path / "external"
    external.mkdir()
    _ = (external / "evidence.bin").write_bytes(b"outside")
    displaced = tmp_path / "displaced"
    mutated = False

    def swap_parent(descriptor: int) -> BinaryIO:
        nonlocal mutated
        if not mutated:
            _ = nested.rename(displaced)
            nested.symlink_to(external, target_is_directory=True)
            mutated = True
        return open_descriptor_stream(descriptor)

    monkeypatch.setattr(archive, "duplicate_stream", swap_parent)
    request = archive.ArchiveRequest(
        raw, tmp_path / "item7-raw-parent-race.tar.gz", tmp_path / "manifest.json", "qa-item7"
    )

    _ = archive.create_archive(request)
    restore = _restore_request(tmp_path, request)
    _ = archive.restore_archive(restore)

    assert (restore.target / "nested/evidence.bin").read_bytes() == b"trusted"


def test_archive_rejects_root_beneath_symlink_parent(tmp_path: Path) -> None:
    actual = tmp_path / "actual"
    raw = actual / "raw"
    raw.mkdir(parents=True)
    _ = (raw / "evidence.bin").write_bytes(b"trusted")
    alias = tmp_path / "alias"
    alias.symlink_to(actual, target_is_directory=True)
    request = archive.ArchiveRequest(
        alias / "raw",
        tmp_path / "item7-raw-symlink-parent.tar.gz",
        tmp_path / "manifest.json",
        "qa-item7",
    )

    with pytest.raises(archive.ArchiveValidationError, match="symlink"):
        _ = archive.create_archive(request)

    assert not request.archive.exists()
    assert not request.manifest.exists()


def test_restore_rejects_archive_beneath_symlink_parent(tmp_path: Path) -> None:
    created = _create_request(tmp_path / "created", "item7-raw-symlink-input.tar.gz")
    _ = archive.create_archive(created)
    alias = tmp_path / "archive-alias"
    alias.symlink_to(created.archive.parent, target_is_directory=True)
    request = archive.RestoreRequest(
        alias / created.archive.name,
        created.manifest,
        tmp_path / "restored",
        tmp_path / "receipt.json",
    )

    with pytest.raises(archive.ArchiveValidationError, match="unsafe"):
        _ = archive.restore_archive(request)

    assert not request.target.exists()
    assert not request.receipt.exists()


def test_restore_rejects_target_beneath_symlink_parent(tmp_path: Path) -> None:
    created = _create_request(tmp_path / "created", "item7-raw-symlink-output.tar.gz")
    _ = archive.create_archive(created)
    actual = tmp_path / "actual"
    actual.mkdir()
    alias = tmp_path / "target-alias"
    alias.symlink_to(actual, target_is_directory=True)
    request = archive.RestoreRequest(
        created.archive,
        created.manifest,
        alias / "restored",
        tmp_path / "receipt.json",
    )

    with pytest.raises(archive.ArchiveValidationError, match="unsafe"):
        _ = archive.restore_archive(request)

    assert not (actual / "restored").exists()
    assert not request.receipt.exists()


def test_restore_rejects_target_replaced_before_receipt_publication(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    created = _create_request(tmp_path / "created", "item7-raw-target-swap.tar.gz")
    _ = archive.create_archive(created)
    target_parent = tmp_path / "target-parent"
    target_parent.mkdir()
    request = archive.RestoreRequest(
        created.archive,
        created.manifest,
        target_parent / "restored",
        tmp_path / "receipt.json",
    )
    displaced = target_parent / "verified"
    original_stage = cast(
        "Callable[[int, bytes], TemporaryFile]",
        archive.__dict__["stage_bytes"],
    )
    swapped = False

    def replace_target(directory: int, body: bytes) -> TemporaryFile:
        nonlocal swapped
        temporary = original_stage(directory, body)
        _ = request.target.rename(displaced)
        request.target.mkdir()
        _ = (request.target / "evidence.txt").write_bytes(b"attacker")
        swapped = True
        return temporary

    monkeypatch.setitem(archive.__dict__, "stage_bytes", replace_target)

    with pytest.raises(archive.ArchiveValidationError, match="unsafe"):
        _ = archive.restore_archive(request)

    assert swapped
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
        created.archive,
        created.manifest,
        tmp_path / "restored",
        receipt_parent / "restore.json",
    )
    displaced = tmp_path / "verified-receipts"
    original_stage = cast(
        "Callable[[int, bytes], TemporaryFile]",
        archive.__dict__["stage_bytes"],
    )
    swapped = False

    def replace_parent(directory: int, body: bytes) -> TemporaryFile:
        nonlocal swapped
        temporary = original_stage(directory, body)
        _ = receipt_parent.rename(displaced)
        receipt_parent.mkdir()
        swapped = True
        return temporary

    monkeypatch.setitem(archive.__dict__, "stage_bytes", replace_parent)

    with pytest.raises(archive.ArchiveValidationError, match="unsafe"):
        _ = archive.restore_archive(request)

    assert swapped
    assert not request.receipt.exists()
    assert not (displaced / request.receipt.name).exists()


def test_restore_uses_verified_archive_descriptor_after_path_replacement(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    created = _create_request(tmp_path, "item7-raw-replaced-input.tar.gz")
    _ = archive.create_archive(created)
    calls = 0

    def replace_after_hash(descriptor: int) -> BinaryIO:
        nonlocal calls
        calls += 1
        if calls == 3:
            created.archive.unlink()
            _ = created.archive.write_bytes(b"unverified replacement")
        return open_descriptor_stream(descriptor)

    monkeypatch.setattr(archive, "duplicate_stream", replace_after_hash)
    request = _restore_request(tmp_path, created)

    _ = archive.restore_archive(request)

    assert (request.target / "evidence.txt").read_bytes() == b"evidence"


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
