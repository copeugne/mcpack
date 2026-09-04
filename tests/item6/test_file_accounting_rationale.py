# pyright: standard
"""Lock the Item 6 file-accounting rationale contract."""

from __future__ import annotations

import json
from copy import deepcopy
from typing import TYPE_CHECKING, Literal, assert_never

import pytest

from mcpack_evidence.item6_file_accounting import RATIONALES
from tests.item6.helpers import AUDIT, FROZEN, MANIFEST, validate, write_audit

if TYPE_CHECKING:
    from pathlib import Path

AUDIT_DATA = json.loads(AUDIT.read_text(encoding="utf-8"))
Mutation = Literal["missing", "blank", "unknown", "altered"]


def test_file_accounting_uses_canonical_rationales() -> None:
    # Given: the committed Item 6 file-accounting classifications.
    rationales = {
        row["classification"]: row.get("rationale") for row in AUDIT_DATA["file_accounting"]
    }

    # When/Then: each classification states its stable, machine-enforced scope rule.
    assert rationales == RATIONALES
    validate(FROZEN, MANIFEST, AUDIT)


@pytest.mark.parametrize("mutation", ["missing", "blank", "unknown", "altered"])
def test_validator_rejects_invalid_file_accounting_rationale(
    tmp_path: Path, mutation: Mutation
) -> None:
    # Given: one committed file-accounting rationale is invalidated.
    audit = deepcopy(AUDIT_DATA)
    row = audit["file_accounting"][0]
    match mutation:
        case "missing":
            row.pop("rationale", None)
        case "blank":
            row["rationale"] = ""
        case "unknown":
            row["rationale"] = "not a canonical scope rule"
        case "altered":
            row["rationale"] = RATIONALES["audited"].replace("directly", "indirectly")
        case unreachable:
            assert_never(unreachable)

    # When/Then: strict validation rejects omissions, blanks, unknowns, and semantic drift.
    with pytest.raises((ValueError, KeyError)):
        validate(FROZEN, MANIFEST, write_audit(tmp_path, audit))
