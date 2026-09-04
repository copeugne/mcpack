# pyright: standard
from __future__ import annotations

import json
from copy import deepcopy
from typing import TYPE_CHECKING

import pytest

from tests.item6.helpers import AUDIT, FROZEN, MANIFEST, validate, write_audit

if TYPE_CHECKING:
    from pathlib import Path

AUDIT_DATA = json.loads(AUDIT.read_text(encoding="utf-8"))
SYSTEM = "Repurposed Structures"
FILE = "config/repurposed_structures-neoforge/modded_loot.toml"
EXPECTED = {
    "Repurposed Structures.modded_loot.importModdedItems": True,
    "Repurposed Structures.modded_loot.blacklistedRSLoottablesFromImportingModdedItems": "",
}


def test_repurposed_direct_settings_bind_both_loot_controls() -> None:
    # Given: the direct Repurposed Structures modded-loot configuration.
    settings = [
        setting
        for setting in AUDIT_DATA["settings"]
        if setting["system"] == SYSTEM and setting["file"] == FILE
    ]

    # When/Then: both source values and their exact lines are explicitly audited.
    assert {setting["key"]: setting["generated_default"] for setting in settings} == EXPECTED
    assert {setting["key"]: setting["effective_value"] for setting in settings} == EXPECTED
    assert [setting["evidence"]["observations"][0]["line"] for setting in settings] == [3, 7]


def test_repurposed_direct_file_is_system_owned_and_audited() -> None:
    # Given: the direct file and committed system/accounting records.
    system = next(system for system in AUDIT_DATA["systems"] if system["system"] == SYSTEM)
    audited = next(
        row["files"] for row in AUDIT_DATA["file_accounting"] if row["classification"] == "audited"
    )
    excluded = next(
        row["files"]
        for row in AUDIT_DATA["file_accounting"]
        if row["classification"] == "out-of-scope"
    )

    # When/Then: the loot-control file is owned and audited outside the exclusion set.
    assert FILE in system["files"]
    assert FILE in audited
    assert FILE not in excluded


@pytest.mark.parametrize(("key", "changed"), [(key, "mutated") for key in EXPECTED])
def test_repurposed_direct_setting_mutations_are_rejected(
    tmp_path: Path, key: str, changed: str
) -> None:
    # Given: one direct loot-control claim is changed without changing the source.
    audit = deepcopy(AUDIT_DATA)
    setting = next(setting for setting in audit["settings"] if setting["key"] == key)
    setting["effective_value"] = changed

    # When/Then: exact source validation rejects each false direct claim.
    with pytest.raises(ValueError, match="setting claimed value does not match source"):
        validate(FROZEN, MANIFEST, write_audit(tmp_path, audit))
