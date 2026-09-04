from __future__ import annotations

import hashlib
import os
import shutil
import tarfile
from pathlib import Path

import pytest
from tools.archive_item7_evidence import run

import mcpack_evidence.item7_archive as archive


def _write_case(
    root: Path,
    members: tuple[tuple[str, bytes], ...],
    identities: tuple[tuple[str, bytes], ...],
    *,
    file_count: int | None = None,
) -> tuple[Path, Path]:
    archive_path = root / "item7-raw-case.tar.gz"
    with tarfile.open(archive_path, "w:gz") as bundle:
        for name, body in members:
            source = root / "source"
            _ = source.write_bytes(body)
            bundle.add(source, arcname=name)
    rows = tuple(
        archive.FileIdentity.model_construct(
            relative_path=name,
            size_bytes=len(body),
            sha256=hashlib.sha256(body).hexdigest(),
        )
        for name, body in identities
    )
    manifest = archive.ArchiveManifest.model_construct(
        schema_version="item7-raw-evidence-archive-v1",
        revision="qa-item7",
        archive_name=archive_path.name,
        archive_size_bytes=archive_path.stat().st_size,
        archive_sha256=hashlib.sha256(archive_path.read_bytes()).hexdigest(),
        file_count=len(rows) if file_count is None else file_count,
        total_size_bytes=sum(row.size_bytes for row in rows),
        files=rows,
    )
    manifest_path = root / "manifest.json"
    _ = manifest_path.write_text(manifest.model_dump_json(indent=2), encoding="utf-8")
    return archive_path, manifest_path


def _restore_request(root: Path, archive_path: Path, manifest_path: Path) -> archive.RestoreRequest:
    return archive.RestoreRequest(
        archive_path, manifest_path, root / "restored", root / "restore.json"
    )


def _arguments(command: str, **options: Path | str) -> tuple[str, ...]:
    parts = (part for name, value in options.items() for part in (f"--{name}", str(value)))
    return (command, *parts)


def _create_request(root: Path, archive_name: str) -> archive.ArchiveRequest:
    raw = root / "raw"
    raw.mkdir()
    _ = (raw / "evidence.txt").write_bytes(b"evidence")
    return archive.ArchiveRequest(raw, root / archive_name, root / "manifest.json", "qa-item7")


def test_archive_restore_round_trip(tmp_path: Path) -> None:
    # Given
    raw = tmp_path / "raw"
    (raw / "nested").mkdir(parents=True)
    (raw / "world").mkdir()
    _ = (raw / "a.txt").write_bytes(b"alpha")
    _ = (raw / "nested" / "b.bin").write_bytes(b"beta")
    _ = (raw / "world" / "session.lock").write_bytes(b"excluded")
    archive_path = tmp_path / "item7-raw-demo.tar.gz"
    manifest_path = tmp_path / "manifest.json"
    restore_request = _restore_request(tmp_path, archive_path, manifest_path)

    # When
    manifest = archive.create_archive(
        archive.ArchiveRequest(
            root=raw,
            archive=archive_path,
            manifest=manifest_path,
            revision="qa-item7",
        )
    )
    receipt = archive.restore_archive(restore_request)

    # Then
    assert manifest.archive_name == "item7-raw-demo.tar.gz"
    assert manifest.archive_sha256 == hashlib.sha256(archive_path.read_bytes()).hexdigest()
    assert manifest.archive_size_bytes == archive_path.stat().st_size
    assert manifest.file_count == 2
    assert tuple(row.relative_path for row in manifest.files) == ("a.txt", "nested/b.bin")
    assert receipt.verified is True
    assert (restore_request.target / "a.txt").read_bytes() == b"alpha"
    assert (restore_request.target / "nested" / "b.bin").read_bytes() == b"beta"
    assert not (restore_request.target / "world" / "session.lock").exists()


def test_archive_bytes_are_deterministic_for_identical_content(tmp_path: Path) -> None:
    # Given
    archives: list[Path] = []
    for index in (1, 2):
        root = tmp_path / str(index) / "raw"
        root.mkdir(parents=True)
        source = root / "evidence.json"
        _ = source.write_bytes(b'{"pass":true}\n')
        os.utime(source, (index, index))
        archive_path = tmp_path / str(index) / "item7-raw-same.tar.gz"
        archives.append(archive_path)
        _ = archive.create_archive(
            archive.ArchiveRequest(
                root, archive_path, tmp_path / str(index) / "manifest.json", "qa-item7"
            )
        )

    # When
    contents = tuple(path.read_bytes() for path in archives)

    # Then
    assert contents[0] == contents[1]


@pytest.mark.parametrize("entry_kind", ["symlink", "fifo"])
def test_create_rejects_nonregular_source_entries(tmp_path: Path, entry_kind: str) -> None:
    # Given
    raw = tmp_path / "raw"
    raw.mkdir()
    external = tmp_path / "external"
    _ = external.write_bytes(b"outside")
    entry = raw / "unsafe"
    if entry_kind == "symlink":
        entry.symlink_to(external)
    else:
        os.mkfifo(entry)
    request = archive.ArchiveRequest(
        root=raw,
        archive=tmp_path / "item7-raw-unsafe.tar.gz",
        manifest=tmp_path / "unsafe-manifest.json",
        revision="qa-item7",
    )

    # When
    with pytest.raises(archive.ArchiveValidationError):
        _ = archive.create_archive(request)

    # Then
    assert not request.archive.exists()
    assert not request.manifest.exists()


@pytest.mark.parametrize(
    ("members", "identities", "message"),
    [
        ((("../escape.txt", b"escape"),), (("../escape.txt", b"escape"),), "unsafe"),
        (
            (("expected.txt", b"expected"), ("extra.txt", b"extra")),
            (("expected.txt", b"expected"),),
            "members",
        ),
        (
            (("expected.txt", b"expected"),),
            (("expected.txt", b"expected"), ("missing.txt", b"missing")),
            "members",
        ),
        ((("expected.txt", b"expected"),), (("expected.txt", b"differnt"),), "mismatch"),
    ],
)
def test_restore_rejects_invalid_archive(
    tmp_path: Path,
    members: tuple[tuple[str, bytes], ...],
    identities: tuple[tuple[str, bytes], ...],
    message: str,
) -> None:
    # Given
    archive_path, manifest_path = _write_case(tmp_path, members, identities)
    request = _restore_request(tmp_path, archive_path, manifest_path)

    # When
    with pytest.raises(ValueError, match=message):
        _ = archive.restore_archive(request)

    # Then
    assert not request.target.exists()
    assert not (tmp_path / "escape.txt").exists()


def test_restore_rejects_inconsistent_manifest_count(tmp_path: Path) -> None:
    # Given
    archive_path, manifest_path = _write_case(
        tmp_path,
        (("expected.txt", b"expected"),),
        (("expected.txt", b"expected"),),
        file_count=2,
    )
    request = _restore_request(tmp_path, archive_path, manifest_path)

    # When
    with pytest.raises(ValueError, match="file count"):
        _ = archive.restore_archive(request)

    # Then
    assert not request.target.exists()
    assert not request.receipt.exists()


def test_refuses_existing_archive_manifest_target_and_receipt(tmp_path: Path) -> None:
    # Given
    request = _create_request(tmp_path, "item7-raw-existing.tar.gz")
    _ = request.archive.write_bytes(b"preserve")

    # When / Then
    with pytest.raises(FileExistsError):
        _ = archive.create_archive(request)


@pytest.mark.parametrize("competing_manifest", [False, True])
def test_archive_publication_failure_preserves_only_competing_manifest(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, competing_manifest: bool
) -> None:
    # Given
    request = _create_request(tmp_path, "item7-raw-failure.tar.gz")
    original_link = os.link
    failure = "injected archive publication failure"
    replacement = b"competing manifest"

    def fail_archive_link(source: Path, target: Path) -> None:
        if Path(target) == request.archive:
            if competing_manifest:
                request.manifest.unlink()
                _ = request.manifest.write_bytes(replacement)
            raise OSError(failure)
        original_link(source, target)

    monkeypatch.setattr(os, "link", fail_archive_link)

    # When
    with pytest.raises(OSError, match=failure):
        _ = archive.create_archive(request)

    # Then
    assert not request.archive.exists()
    if competing_manifest:
        assert request.manifest.read_bytes() == replacement
    else:
        assert not request.manifest.exists()


def test_restore_refuses_concurrently_created_target(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    # Given
    created = _create_request(tmp_path, "item7-raw-race.tar.gz")
    _ = archive.create_archive(created)
    request = _restore_request(tmp_path, created.archive, created.manifest)
    original_copytree = shutil.copytree

    def inject_competing_target(source: Path, target: Path) -> Path:
        request.target.mkdir()
        return original_copytree(source, target)

    monkeypatch.setattr(shutil, "copytree", inject_competing_target)

    # When
    with pytest.raises(FileExistsError):
        _ = archive.restore_archive(request)

    # Then
    assert request.target.is_dir()
    assert not request.receipt.exists()


def test_manifest_binds_bytes_archived_after_source_change(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    # Given
    raw = tmp_path / "raw"
    raw.mkdir()
    source = raw / "evidence.bin"
    _ = source.write_bytes(b"first")

    def mutate_before_build(root: Path, output: Path, files: tuple[Path, ...]) -> Path:
        _ = source.write_bytes(b"later")
        temporary = output.parent / ".injected.tar.gz"
        with tarfile.open(temporary, "w:gz") as bundle:
            for path in files:
                bundle.add(path, arcname=path.relative_to(root))
        return temporary

    monkeypatch.setattr(archive, "_build_tar", mutate_before_build)
    request = archive.ArchiveRequest(
        raw, tmp_path / "item7-raw-race.tar.gz", tmp_path / "manifest.json", "qa-item7"
    )

    # When
    _ = archive.create_archive(request)

    # Then
    restore = archive.RestoreRequest(
        request.archive, request.manifest, tmp_path / "restored", tmp_path / "receipt"
    )
    _ = archive.restore_archive(restore)


def test_archive_cli_creates_and_restores_verified_evidence(tmp_path: Path) -> None:
    # Given
    raw = tmp_path / "raw"
    raw.mkdir()
    _ = (raw / "evidence.json").write_bytes(b'{"pass":true}\n')
    archive_path = tmp_path / "item7-raw-cli.tar.gz"
    manifest = tmp_path / "manifest.json"
    target = tmp_path / "restored"
    receipt = tmp_path / "restore.json"
    # When
    create_arguments = _arguments(
        "create", root=raw, archive=archive_path, manifest=manifest, revision="qa-item7"
    )
    restore_arguments = _arguments(
        "restore", archive=archive_path, manifest=manifest, target=target, receipt=receipt
    )
    _ = run(create_arguments)
    _ = run(restore_arguments)

    # Then
    assert archive.ArchiveManifest.model_validate_json(manifest.read_bytes()).revision == "qa-item7"
    assert archive.RestoreReceipt.model_validate_json(receipt.read_bytes()).verified is True
    assert (target / "evidence.json").read_bytes() == b'{"pass":true}\n'
