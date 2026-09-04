# pyright: standard
from __future__ import annotations

import json
from copy import deepcopy
from typing import TYPE_CHECKING

import pytest

from mcpack_evidence.item6_surface_validation import build_setting_surface
from tests.item6.helpers import AUDIT, FROZEN, MANIFEST, validate, write_audit

if TYPE_CHECKING:
    from pathlib import Path

AUDIT_DATA = json.loads(AUDIT.read_text(encoding="utf-8"))
SYSTEM = "Vanilla Structures"
FILE = "config/vanilla_structures/toggle_structure_config.json5"


def test_vanilla_toggle_surface_reproduces_all_34_leaves() -> None:
    surface = next(surface for surface in AUDIT_DATA["setting_surfaces"] if surface["file"] == FILE)
    assert surface == build_setting_surface(SYSTEM, FILE, FROZEN / FILE)
    assert len(surface["leaves"]) == 34
    assert all(type(leaf["effective_value"]) is bool for leaf in surface["leaves"])


def test_vanilla_toggle_file_is_owned_and_audited() -> None:
    system = next(system for system in AUDIT_DATA["systems"] if system["system"] == SYSTEM)
    audited = next(
        row["files"] for row in AUDIT_DATA["file_accounting"] if row["classification"] == "audited"
    )
    excluded = next(
        row["files"]
        for row in AUDIT_DATA["file_accounting"]
        if row["classification"] == "out-of-scope"
    )
    assert FILE in system["files"]
    assert FILE in audited
    assert FILE not in excluded


def test_vanilla_toggle_mutation_is_rejected(tmp_path: Path) -> None:
    audit = deepcopy(AUDIT_DATA)
    surface = next(surface for surface in audit["setting_surfaces"] if surface["file"] == FILE)
    surface["leaves"][0]["effective_value"] = "true"
    with pytest.raises(ValueError, match="effective value does not match source"):
        validate(FROZEN, MANIFEST, write_audit(tmp_path, audit))
