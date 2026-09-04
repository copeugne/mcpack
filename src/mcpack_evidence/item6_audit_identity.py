# ruff: noqa: EM101, TRY003
"""Seal Item 6 audit semantics independently from configuration identity."""

from __future__ import annotations

import hashlib
import json
from typing import TYPE_CHECKING, Final

if TYPE_CHECKING:
    from collections.abc import Mapping

AUDIT_SEMANTIC_SHA256: Final = "2366908adeb4b777020fbbcc9415f831b4ff17e35ab2df1ed5a072db99816ca8"


def validate_audit_semantic_identity(audit: Mapping[str, object]) -> None:
    """Fail unless canonical parsed audit semantics match the committed seal."""
    semantics = dict(audit)
    del semantics["configuration_identity"]
    canonical = json.dumps(semantics, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
    digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    if digest != AUDIT_SEMANTIC_SHA256:
        raise ValueError("audit semantic identity does not match committed seal")
