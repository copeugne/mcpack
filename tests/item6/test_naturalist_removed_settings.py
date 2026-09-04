# pyright: standard
from __future__ import annotations

import json
import tomllib
from copy import deepcopy
from typing import TYPE_CHECKING

import pytest

from tests.item6.helpers import AUDIT, FROZEN, MANIFEST, validate, write_audit

if TYPE_CHECKING:
    from pathlib import Path

AUDIT_DATA = json.loads(AUDIT.read_text(encoding="utf-8"))
SYSTEM = "Naturalist"
FILE = "config/naturalist-server.toml"
KEY_PREFIX = "Naturalist.disable_mobs."


def test_naturalist_audits_all_24_removed_booleans_once() -> None:
    source = tomllib.loads((FROZEN / FILE).read_text(encoding="utf-8"))["disable_mobs"]
    expected = {key: value for key, value in source.items() if key.endswith("_removed")}
    settings = [setting for setting in AUDIT_DATA["settings"] if setting["file"] == FILE]
    observed = {setting["key"].removeprefix(KEY_PREFIX): setting for setting in settings}
    assert len(expected) == len(settings) == len(observed) == 24
    assert set(observed) == set(expected)
    assert all(type(value) is bool and value is False for value in expected.values())
    assert all(setting["generated_default"] is False for setting in observed.values())
    assert all(setting["effective_value"] is False for setting in observed.values())


def test_naturalist_removed_evidence_binds_unique_source_lines() -> None:
    source_lines = (FROZEN / FILE).read_text(encoding="utf-8").splitlines()
    expected_lines = {
        line.strip().partition(" = ")[0]: number
        for number, line in enumerate(source_lines, start=1)
        if line.strip().partition(" = ")[0].endswith("_removed")
    }
    settings = [setting for setting in AUDIT_DATA["settings"] if setting["file"] == FILE]
    observed_lines = {
        setting["key"].removeprefix(KEY_PREFIX): setting["evidence"]["observations"][0]["line"]
        for setting in settings
    }
    assert observed_lines == expected_lines
    assert len(set(observed_lines.values())) == 24


def test_naturalist_file_is_owned_and_audited() -> None:
    system = next(system for system in AUDIT_DATA["systems"] if system["system"] == SYSTEM)
    audited = next(
        row["files"] for row in AUDIT_DATA["file_accounting"] if row["classification"] == "audited"
    )
    excluded = next(
        row["files"]
        for row in AUDIT_DATA["file_accounting"]
        if row["classification"] == "out-of-scope"
    )
    assert system["files"] == [FILE]
    assert FILE in audited
    assert FILE not in excluded


def test_naturalist_removed_mutation_is_rejected(tmp_path: Path) -> None:
    audit = deepcopy(AUDIT_DATA)
    setting = next(setting for setting in audit["settings"] if setting["file"] == FILE)
    setting["effective_value"] = True
    with pytest.raises(ValueError, match="setting claimed value does not match source"):
        validate(FROZEN, MANIFEST, write_audit(tmp_path, audit))
