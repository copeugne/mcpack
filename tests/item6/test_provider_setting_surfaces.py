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
IDAS_FILES = [
    "config/cristellib/idas/structure_placement_config.json5",
    "config/cristellib/idas/structure_toggle_config.json5",
]
IDAS_DIRECT_KEYS = {
    "IDAS.General.Disable Vanilla Desert Pyramid",
    "IDAS.General.Disable Ice and Fire Structures",
    "IDAS.General.Apply Mining Fatigue",
}


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


def test_idas_surfaces_and_direct_settings_reproduce_all_112_controls() -> None:
    # Given: IDAS has two grouped CristelLib files and one direct TOML file.
    surfaces = [
        surface for surface in AUDIT_DATA["setting_surfaces"] if surface["system"] == "IDAS"
    ]
    direct_settings = [setting for setting in AUDIT_DATA["settings"] if setting["system"] == "IDAS"]

    # When/Then: 109 generated leaves and all 3 direct values are exact and complete.
    assert surfaces == [
        build_setting_surface("IDAS", relative, FROZEN / relative) for relative in IDAS_FILES
    ]
    assert [len(surface["leaves"]) for surface in surfaces] == [24, 85]
    assert sum(len(surface["leaves"]) for surface in surfaces) + len(direct_settings) == 112
    assert {setting["key"] for setting in direct_settings} == IDAS_DIRECT_KEYS
    assert all(setting["generated_default"] is True for setting in direct_settings)
    assert all(setting["effective_value"] is True for setting in direct_settings)


def test_idas_surface_mutation_is_rejected(tmp_path: Path) -> None:
    # Given: one exact IDAS nested key changed without changing its preserved source.
    audit = deepcopy(AUDIT_DATA)
    surface = next(surface for surface in audit["setting_surfaces"] if surface["system"] == "IDAS")
    surface["leaves"][0]["key"] = "idas_common.wrong"

    # When/Then: repository validation rejects the false grouped provider claim.
    with pytest.raises(ValueError, match="line evidence does not match source"):
        validate(FROZEN, MANIFEST, write_audit(tmp_path, audit))


def test_idas_direct_setting_mutation_is_rejected(tmp_path: Path) -> None:
    # Given: one direct IDAS TOML claim changed without changing its preserved source.
    audit = deepcopy(AUDIT_DATA)
    setting = next(
        setting
        for setting in audit["settings"]
        if setting["key"] == "IDAS.General.Apply Mining Fatigue"
    )
    setting["effective_value"] = False

    # When/Then: repository validation rejects the false direct provider claim.
    with pytest.raises(ValueError, match="setting claimed value does not match source"):
        validate(FROZEN, MANIFEST, write_audit(tmp_path, audit))
