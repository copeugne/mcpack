"""Retained save-sequence acceptance for Item 7 completion."""

from __future__ import annotations

from typing import TYPE_CHECKING

from mcpack_evidence.item7_completion_io import fail, identity, strict_json
from mcpack_evidence.item7_runtime import Item7RuntimeError
from mcpack_evidence.item7_save_sequence import build_save_sequence_audit

if TYPE_CHECKING:
    from pathlib import Path

    from mcpack_evidence.item7_completion_models import ArtifactIdentity


def validate_save_sequence_audit(
    path: Path, raw_root: Path, core_manifest: Path
) -> ArtifactIdentity:
    """Require the committed audit to equal a rebuild from archived console logs."""
    try:
        rebuilt = build_save_sequence_audit(raw_root, core_manifest)
    except Item7RuntimeError as error:
        fail("save sequence audit source binding", error.detail)
    if strict_json(path) != rebuilt:
        fail("save sequence audit source binding", path)
    return identity(path, path.name)
