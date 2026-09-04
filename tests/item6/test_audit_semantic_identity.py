# pyright: standard
"""Seal the canonical Item 6 audit semantics against tampering."""

from __future__ import annotations

import json
from copy import deepcopy
from typing import TYPE_CHECKING, Literal, assert_never

import pytest

from tests.item6.helpers import AUDIT, FROZEN, MANIFEST, validate, write_audit

if TYPE_CHECKING:
    from pathlib import Path

AUDIT_DATA = json.loads(AUDIT.read_text(encoding="utf-8"))
Mutation = Literal[
    "setting-key",
    "remove-setting",
    "duplicate-setting",
    "system-label",
    "finding-summary",
    "leaf-line",
]


def test_canonical_audit_and_format_only_rewrite_pass(tmp_path: Path) -> None:
    # Given: the canonical audit and a whitespace/key-order-only rewrite.
    rewritten = tmp_path / "format-only.json"
    rewritten.write_text(json.dumps(AUDIT_DATA, indent=2, sort_keys=True), encoding="utf-8")

    # When/Then: canonical parsed semantics, not serialization layout, are sealed.
    validate(FROZEN, MANIFEST, AUDIT)
    validate(FROZEN, MANIFEST, rewritten)


@pytest.mark.parametrize(
    "mutation",
    [
        "setting-key",
        "remove-setting",
        "duplicate-setting",
        "system-label",
        "finding-summary",
        "leaf-line",
    ],
)
def test_validator_rejects_audit_semantic_tampering(tmp_path: Path, mutation: Mutation) -> None:
    # Given: one audit semantic element is changed while configuration identity remains valid.
    audit = deepcopy(AUDIT_DATA)
    match mutation:
        case "setting-key":
            audit["settings"][0]["key"] = "renamed.setting"
        case "remove-setting":
            audit["settings"].pop(0)
        case "duplicate-setting":
            audit["settings"].append(deepcopy(audit["settings"][0]))
        case "system-label":
            audit["systems"][0]["system"] = "renamed system"
        case "finding-summary":
            audit["findings"][0]["summary"] = "renamed finding summary"
        case "leaf-line":
            audit["setting_surfaces"][0]["leaves"][0]["line"] += 1
        case unreachable:
            assert_never(unreachable)

    # When/Then: every semantic change fails validation, even with a valid configuration identity.
    with pytest.raises(ValueError, match=r"audit semantic identity|setting surface"):
        validate(FROZEN, MANIFEST, write_audit(tmp_path, audit))
