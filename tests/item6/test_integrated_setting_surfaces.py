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
SYSTEM = "Integrated structures"
FILES = [
    "config/cristellib/integrated_stronghold/structure_placement_config.json5",
    "config/cristellib/integrated_stronghold/structure_toggle_config.json5",
    "config/cristellib/integrated_villages/structure_placement_config.json5",
    "config/cristellib/integrated_villages/structure_toggle_config.json5",
]
DIRECT_KEYS = {
    "Integrated Villages.General.Disable Vanilla Villages",
    "Integrated Villages.General.Activate Create Contraptions",
}


def test_integrated_surfaces_reproduce_all_22_source_leaves() -> None:
    # Given: committed Integrated Stronghold and Integrated Villages surfaces.
    surfaces = [
        surface for surface in AUDIT_DATA["setting_surfaces"] if surface["system"] == SYSTEM
    ]

    # When/Then: generator output exactly covers 4 Stronghold and 18 Villages leaves.
    assert surfaces == [
        build_setting_surface(SYSTEM, relative, FROZEN / relative) for relative in FILES
    ]
    assert [len(surface["leaves"]) for surface in surfaces] == [3, 1, 6, 12]


def test_integrated_system_and_accounting_cover_every_relevant_file() -> None:
    # Given: the five Integrated configuration files in the frozen inventory.
    expected = {"config/integrated_villages-neoforge-1_21.toml", *FILES}
    system = next(system for system in AUDIT_DATA["systems"] if system["system"] == SYSTEM)
    audited = next(
        row["files"] for row in AUDIT_DATA["file_accounting"] if row["classification"] == "audited"
    )
    excluded = next(
        row["files"]
        for row in AUDIT_DATA["file_accounting"]
        if row["classification"] == "out-of-scope"
    )
    direct = [setting for setting in AUDIT_DATA["settings"] if setting["system"] == SYSTEM]

    # When/Then: all files are system-owned and audited, with both direct values present.
    assert set(system["files"]) == expected
    assert expected <= set(audited)
    assert expected.isdisjoint(excluded)
    assert {setting["key"] for setting in direct} == DIRECT_KEYS
    assert all(setting["generated_default"] is True for setting in direct)
    assert all(setting["effective_value"] is True for setting in direct)


def test_integrated_surface_mutation_is_rejected(tmp_path: Path) -> None:
    # Given: one Integrated Stronghold leaf value changed without changing the source.
    audit = deepcopy(AUDIT_DATA)
    surface = next(surface for surface in audit["setting_surfaces"] if surface["file"] == FILES[0])
    surface["leaves"][0]["generated_default"] = False

    # When/Then: exact source validation rejects the false grouped claim.
    with pytest.raises(ValueError, match="generated value does not match source"):
        validate(FROZEN, MANIFEST, write_audit(tmp_path, audit))


def test_integrated_direct_mutation_is_rejected(tmp_path: Path) -> None:
    # Given: the omitted direct Create-contraption value is changed in audit only.
    audit = deepcopy(AUDIT_DATA)
    setting = next(
        setting
        for setting in audit["settings"]
        if setting["key"] == "Integrated Villages.General.Activate Create Contraptions"
    )
    setting["effective_value"] = False

    # When/Then: exact source validation rejects the false direct claim.
    with pytest.raises(ValueError, match="setting claimed value does not match source"):
        validate(FROZEN, MANIFEST, write_audit(tmp_path, audit))
