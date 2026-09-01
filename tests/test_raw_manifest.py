from __future__ import annotations

import hashlib
from typing import TYPE_CHECKING

from mcpack_evidence.raw_manifest import build_raw_manifest

if TYPE_CHECKING:
    from pathlib import Path


def test_builds_sorted_content_identity_manifest(tmp_path: Path) -> None:
    # Given
    nested = tmp_path / "nested"
    nested.mkdir()
    _ = (nested / "b.json").write_bytes(b"beta")
    _ = (tmp_path / "a.json").write_bytes(b"alpha")
    _ = (tmp_path / "nested-extra.json").write_bytes(b"gamma")

    # When
    manifest = build_raw_manifest(tmp_path)

    # Then
    assert tuple(row.relative_path for row in manifest.files) == (
        "a.json",
        "nested-extra.json",
        "nested/b.json",
    )
    assert manifest.total_size_bytes == 14
    assert manifest.files[0].sha256 == hashlib.sha256(b"alpha").hexdigest()
