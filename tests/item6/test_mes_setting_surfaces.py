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
SYSTEM = "Moog structure families"
FILES = [
    "config/cristellib/mes/structure_placement_config.json5",
    "config/cristellib/mes/structure_toggle_config.json5",
]


def test_mes_surfaces_reproduce_all_100_source_leaves() -> None:
    # Given: both committed MES configuration surfaces.
    surfaces = [surface for surface in AUDIT_DATA["setting_surfaces"] if surface["file"] in FILES]

    # When/Then: generator output exactly covers 75 placement and 25 toggle leaves.
    assert surfaces == [
        build_setting_surface(SYSTEM, relative, FROZEN / relative) for relative in FILES
    ]
    assert [len(surface["leaves"]) for surface in surfaces] == [75, 25]


def test_mes_files_are_system_owned_and_audited() -> None:
    # Given: the two MES files and the committed audit classifications.
    system = next(system for system in AUDIT_DATA["systems"] if system["system"] == SYSTEM)
    audited = next(
        row["files"] for row in AUDIT_DATA["file_accounting"] if row["classification"] == "audited"
    )
    excluded = next(
        row["files"]
        for row in AUDIT_DATA["file_accounting"]
        if row["classification"] == "out-of-scope"
    )

    # When/Then: both files are owned and audited exactly outside the exclusion set.
    assert set(FILES) <= set(system["files"])
    assert set(FILES) <= set(audited)
    assert set(FILES).isdisjoint(excluded)


def test_mes_surface_mutation_is_rejected(tmp_path: Path) -> None:
    # Given: one MES leaf line is changed without changing the frozen source.
    audit = deepcopy(AUDIT_DATA)
    surface = next(surface for surface in audit["setting_surfaces"] if surface["file"] == FILES[0])
    surface["leaves"][0]["line"] += 1_000

    # When/Then: exact source validation rejects the false MES claim.
    with pytest.raises(ValueError, match="line evidence does not match source"):
        validate(FROZEN, MANIFEST, write_audit(tmp_path, audit))
