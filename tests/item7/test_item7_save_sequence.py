from __future__ import annotations

import hashlib
from typing import TYPE_CHECKING

import pytest

from mcpack_evidence.item7_archive_models import ArchiveManifest, FileIdentity
from mcpack_evidence.item7_runtime import Item7RuntimeError
from mcpack_evidence.item7_save_sequence import SAVE_SEQUENCE_TARGETS, validate_save_sequences

if TYPE_CHECKING:
    from pathlib import Path


def _write_accepted_logs(root: Path) -> None:
    for relative, marker in SAVE_SEQUENCE_TARGETS:
        console = root / relative / "console.log"
        console.parent.mkdir(parents=True)
        _ = console.write_text(
            f"{marker}\nSaving the game (this may take a moment!)\nSaved the game\n",
            encoding="utf-8",
        )


def _write_manifest(root: Path, output: Path, *, forge_first: bool = False) -> None:
    files: list[FileIdentity] = []
    for index, (relative, _) in enumerate(SAVE_SEQUENCE_TARGETS):
        console = root / relative / "console.log"
        files.append(
            FileIdentity(
                relative_path=f"{relative}/console.log",
                size_bytes=console.stat().st_size,
                sha256=(
                    "b" * 64
                    if forge_first and index == 0
                    else hashlib.sha256(console.read_bytes()).hexdigest()
                ),
            )
        )
    manifest = ArchiveManifest(
        revision="test",
        archive_name="test.tar.gz",
        archive_size_bytes=0,
        archive_sha256="a" * 64,
        file_count=len(files),
        total_size_bytes=sum(row.size_bytes for row in files),
        files=tuple(sorted(files, key=lambda row: row.relative_path)),
    )
    _ = output.write_text(manifest.model_dump_json(), encoding="utf-8")


def test_validate_save_sequences_accepts_post_work_save_protocol(tmp_path: Path) -> None:
    # Given: every accepted lifecycle log has its work marker followed by the save protocol.
    _write_accepted_logs(tmp_path)

    # When: the restored evidence root is validated.
    records = validate_save_sequences(tmp_path)

    # Then: each accepted lifecycle has a strictly ordered save sequence.
    assert len(records) == 12
    assert all(record.work_line < record.saving_line < record.saved_line for record in records)
    assert all(record.size_bytes > 0 and len(record.sha256) == 64 for record in records)


def test_validate_save_sequences_rejects_save_finish_before_save_start(tmp_path: Path) -> None:
    # Given: one accepted lifecycle has a stale generic save finish before its save start.
    _write_accepted_logs(tmp_path)
    console = tmp_path / "run-a/ordinary/console.log"
    _ = console.write_text(
        "Task finished for\nSaved the game\nSaving the game (this may take a moment!)\n",
        encoding="utf-8",
    )

    # When: the restored evidence root is validated.
    with pytest.raises(Item7RuntimeError, match="save sequence differs"):
        _ = validate_save_sequences(tmp_path)

    # Then: no ambiguous generic save finish is accepted.


def test_validate_save_sequences_rejects_log_not_bound_by_archive_manifest(tmp_path: Path) -> None:
    # Given: valid ordered logs and an archive manifest whose hash for one log was forged.
    _write_accepted_logs(tmp_path)
    manifest = tmp_path / "manifest.json"
    _write_manifest(tmp_path, manifest, forge_first=True)

    # When / Then: the accepted sequence must remain bound to its archived source bytes.
    with pytest.raises(Item7RuntimeError, match="console log differs from core manifest"):
        _ = validate_save_sequences(tmp_path, manifest)
