# pyright: standard
from __future__ import annotations

from typing import TYPE_CHECKING

from tests.item6.helpers import MODULE

if TYPE_CHECKING:
    from pathlib import Path


def test_facade_exposes_item6_operations() -> None:
    assert all(callable(getattr(MODULE, name)) for name in ("validate", "capture", "sha256"))


def test_facade_sha256_matches_known_digest(tmp_path: Path) -> None:
    source = tmp_path / "source.txt"
    source.write_bytes(b"item-6\n")

    digest = MODULE.sha256(source)

    assert digest == "7fa09e5abb54b7ab25569835fd2a427ed62368358c7094418f7bca61fc77e1db"


def test_facade_exposes_cli_entrypoint() -> None:
    assert callable(MODULE.main)
