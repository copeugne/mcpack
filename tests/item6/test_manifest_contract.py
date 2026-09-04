# pyright: standard
"""Characterize and harden the Item 6 manifest contract."""

from __future__ import annotations

from mcpack_evidence.item6_manifest import parse_manifest, validate_manifest_inventory
from tests.item6.helpers import FROZEN, MANIFEST


def test_committed_manifest_inventory_is_valid() -> None:
    # Given: the committed frozen tree and its manifest.
    manifest = parse_manifest(MANIFEST)

    # When: the manifest inventory is checked directly.
    expected = validate_manifest_inventory(FROZEN, manifest)

    # Then: every recorded path is present exactly once in the frozen tree.
    assert len(expected) == manifest["file_count"]
