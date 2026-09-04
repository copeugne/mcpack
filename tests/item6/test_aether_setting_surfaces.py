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
SYSTEM = "Aether"
FILES = [
    "config/cristellib/aether/structure_placement_config.json5",
    "config/cristellib/aether/structure_toggle_config.json5",
]


def test_aether_surfaces_reproduce_all_13_source_leaves() -> None:
    surfaces = [surface for surface in AUDIT_DATA["setting_surfaces"] if surface["file"] in FILES]
    assert surfaces == [
        build_setting_surface(SYSTEM, relative, FROZEN / relative) for relative in FILES
    ]
    assert [len(surface["leaves"]) for surface in surfaces] == [9, 4]


def test_aether_files_are_system_owned_and_audited() -> None:
    system = next(system for system in AUDIT_DATA["systems"] if system["system"] == SYSTEM)
    audited = next(
        row["files"] for row in AUDIT_DATA["file_accounting"] if row["classification"] == "audited"
    )
    excluded = next(
        row["files"]
        for row in AUDIT_DATA["file_accounting"]
        if row["classification"] == "out-of-scope"
    )
    assert set(system["files"]) == set(FILES)
    assert set(FILES) <= set(audited)
    assert set(FILES).isdisjoint(excluded)


def test_aether_surface_mutation_is_rejected(tmp_path: Path) -> None:
    audit = deepcopy(AUDIT_DATA)
    surface = next(surface for surface in audit["setting_surfaces"] if surface["file"] == FILES[0])
    surface["leaves"][0]["effective_value"] = "mutated"
    with pytest.raises(ValueError, match="setting surface effective value does not match source"):
        validate(FROZEN, MANIFEST, write_audit(tmp_path, audit))
