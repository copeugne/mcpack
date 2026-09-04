# ruff: noqa: EM101, TRY003
"""Seal Item 6 audit semantics independently from configuration identity."""

from __future__ import annotations

import hashlib
import json
from typing import TYPE_CHECKING, Final

if TYPE_CHECKING:
    from collections.abc import Mapping

AUDIT_SEMANTIC_SHA256: Final = "65c0bf42bf714ac626f85d5c662b8b4b1cf611427cb2169940b4f1bb1fbc61f0"


def validate_audit_semantic_identity(audit: Mapping[str, object]) -> None:
    """Fail unless canonical parsed audit semantics match the committed seal."""
    semantics = dict(audit)
    del semantics["configuration_identity"]
    canonical = json.dumps(semantics, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
    digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    if digest != AUDIT_SEMANTIC_SHA256:
        raise ValueError("audit semantic identity does not match committed seal")
