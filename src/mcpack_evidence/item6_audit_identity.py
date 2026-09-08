# ruff: noqa: EM101, TRY003
"""Seal Item 6 audit semantics independently from configuration identity."""

from __future__ import annotations

import hashlib
import json
from typing import TYPE_CHECKING, Final

from mcpack_evidence.item6_json import parse_strict_json

if TYPE_CHECKING:
    from collections.abc import Mapping

    from mcpack_evidence.item6_provenance import RepositoryReferences

AUDIT_SEMANTIC_SHA256: Final = "9669dde1b969b69556a6669650df9085dca6751e5127e1000c774d2a2b039a52"


def validate_chunky_disposition(references: RepositoryReferences) -> None:
    """Bind the one current correction without rewriting the historical audit."""
    expected: dict[str, object] = {
        "system": "Chunky",
        "candidate": "Chunky-NeoForge-1.4.23.jar",
        "snapshot_path": "evidence/item-6/config-audit.json",
        "snapshot_sha256": "181e0c299f44ded319d93c84f7b983738364b4090286251b00421fa041b989dd",
        "recorded_status": "retained-but-no-config-generated",
        "current_status": "not-retained-no-config-generated",
        "files": [],
        "retained_manifest_path": "evidence/item-3/runtime/retained-server-candidates.txt",
        "retained_manifest_sha256": (
            "78e5bdc0697299782a535400ad5b313c088e8db10cfe075085ae4c8a531e30cb"
        ),
    }
    if parse_strict_json(references.chunky_disposition.read_bytes()) != expected:
        raise ValueError("current Chunky disposition differs from the accepted correction")
    if (
        hashlib.sha256(references.audit_snapshot.read_bytes()).hexdigest()
        != expected["snapshot_sha256"]
    ):
        raise ValueError("current Chunky disposition does not bind the historical snapshot")
    retained = references.retained_manifest.read_bytes()
    if (
        hashlib.sha256(retained).hexdigest() != expected["retained_manifest_sha256"]
        or b"Chunky-NeoForge-1.4.23.jar" in retained.splitlines()
    ):
        raise ValueError("current Chunky disposition contradicts retained membership")


def validate_audit_semantic_identity(audit: Mapping[str, object]) -> None:
    """Seal historical snapshot semantics; current Chunky disposition is checked separately."""
    semantics = dict(audit)
    del semantics["configuration_identity"]
    canonical = json.dumps(semantics, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
    digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    if digest != AUDIT_SEMANTIC_SHA256:
        raise ValueError("audit semantic identity does not match committed seal")
