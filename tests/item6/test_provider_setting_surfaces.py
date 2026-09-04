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
WDA_FILES = [
    "config/cristellib/dungeons_arise/structure_placement_config.json5",
    "config/cristellib/dungeons_arise/structure_toggle_config.json5",
]
SEVEN_SEAS_FILES = [
    "config/cristellib/dungeons_arise_seven_seas/structure_placement_config.json5",
    "config/cristellib/dungeons_arise_seven_seas/structure_toggle_config.json5",
]


def test_wda_surfaces_reproduce_all_44_source_leaves() -> None:
    # Given: the two committed WDA grouped surfaces.
    surfaces = [
        surface
        for surface in AUDIT_DATA["setting_surfaces"]
        if surface["system"] == "When Dungeons Arise"
    ]

    # When/Then: generator output matches exactly, with all 6 placement and 38 toggle leaves.
    assert surfaces == [
        build_setting_surface("When Dungeons Arise", relative, FROZEN / relative)
        for relative in WDA_FILES
    ]
    assert [len(surface["leaves"]) for surface in surfaces] == [6, 38]
    assert not [
        setting for setting in AUDIT_DATA["settings"] if setting["system"] == "When Dungeons Arise"
    ]


def test_wda_surface_mutation_is_rejected(tmp_path: Path) -> None:
    # Given: one exact WDA leaf claim changed without changing its preserved source.
    audit = deepcopy(AUDIT_DATA)
    surface = next(
        surface
        for surface in audit["setting_surfaces"]
        if surface["system"] == "When Dungeons Arise"
    )
    surface["leaves"][0]["effective_value"] += 1

    # When/Then: repository validation rejects the false provider claim.
    with pytest.raises(ValueError, match="effective value does not match source"):
        validate(FROZEN, MANIFEST, write_audit(tmp_path, audit))


def test_seven_seas_surfaces_reproduce_all_eight_source_leaves() -> None:
    # Given: the two committed WDA Seven Seas grouped surfaces.
    surfaces = [
        surface
        for surface in AUDIT_DATA["setting_surfaces"]
        if surface["system"] == "WDA Seven Seas"
    ]

    # When/Then: generator output matches exactly, with all 3 placement and 5 toggle leaves.
    assert surfaces == [
        build_setting_surface("WDA Seven Seas", relative, FROZEN / relative)
        for relative in SEVEN_SEAS_FILES
    ]
    assert [len(surface["leaves"]) for surface in surfaces] == [3, 5]
    assert not [
        setting for setting in AUDIT_DATA["settings"] if setting["system"] == "WDA Seven Seas"
    ]


def test_seven_seas_surface_mutation_is_rejected(tmp_path: Path) -> None:
    # Given: one exact Seven Seas leaf line changed without changing its preserved source.
    audit = deepcopy(AUDIT_DATA)
    surface = next(
        surface for surface in audit["setting_surfaces"] if surface["system"] == "WDA Seven Seas"
    )
    surface["leaves"][0]["line"] += 1_000

    # When/Then: repository validation rejects the false provider evidence.
    with pytest.raises(ValueError, match="line evidence does not match source"):
        validate(FROZEN, MANIFEST, write_audit(tmp_path, audit))
