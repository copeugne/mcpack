# pyright: standard
"""Bind Towns and Towers generated values to its declared defaults."""

from __future__ import annotations

import json
from copy import deepcopy
from typing import TYPE_CHECKING, Literal, assert_never

import pytest

from tests.item6.helpers import AUDIT, FROZEN, MANIFEST, validate, write_audit

if TYPE_CHECKING:
    from pathlib import Path

AUDIT_DATA = json.loads(AUDIT.read_text(encoding="utf-8"))
FILE = "config/towns_and_towers/structure_rarity_new.json5"
DEFAULTS = {
    "towers.separation": {"value": 24, "line": 30, "prefix": "// DEFAULT ", "suffix": ""},
    "towns.separation": {"value": 24, "line": 38, "prefix": "// DEFAULT ", "suffix": ""},
    "towns.spacing": {"value": 48, "line": 40, "prefix": "// DEFAULT ", "suffix": ""},
}
Mutation = Literal["missing", "value", "line", "false-flag"]


def test_towns_and_towers_changes_bind_declared_defaults() -> None:
    # Given: the committed Towns and Towers grouped configuration surface.
    surface = _towns_surface(AUDIT_DATA)
    leaves = {leaf["key"]: leaf for leaf in surface["leaves"]}

    # When: its three source-declared changes are inspected.
    changes = {key: leaves[key] for key in DEFAULTS}

    # Then: effective values differ from bound upstream defaults and carry exact flags.
    assert {key: leaf["generated_default"] for key, leaf in changes.items()} == {
        "towers.separation": 12,
        "towns.separation": 12,
        "towns.spacing": 51,
    }
    assert {key: leaf["effective_value"] for key, leaf in changes.items()} == {
        "towers.separation": 12,
        "towns.separation": 12,
        "towns.spacing": 51,
    }
    assert {key: leaf["upstream_default"] for key, leaf in changes.items()} == DEFAULTS
    assert {leaf["key"] for leaf in surface["leaves"] if leaf["non_default"]} == set(DEFAULTS)
    validate(FROZEN, MANIFEST, AUDIT)


@pytest.mark.parametrize(
    ("mutation", "message"),
    [
        ("missing", "requires declared default evidence"),
        ("value", "declared default evidence does not match source"),
        ("line", "declared default evidence does not match source"),
        ("false-flag", "non-default flag does not match declared default"),
    ],
)
@pytest.mark.parametrize("key", DEFAULTS)
def test_validator_rejects_inexact_towns_and_towers_default_claim(
    tmp_path: Path, key: str, mutation: Mutation, message: str
) -> None:
    # Given: one committed declared-default claim is corrupted.
    audit = deepcopy(AUDIT_DATA)
    leaf = next(leaf for leaf in _towns_surface(audit)["leaves"] if leaf["key"] == key)
    match mutation:
        case "missing":
            del leaf["upstream_default"]
        case "value":
            leaf["upstream_default"]["value"] = -1
        case "line":
            leaf["upstream_default"]["line"] = 1
        case "false-flag":
            leaf["non_default"] = False
        case unreachable:
            assert_never(unreachable)

    # When/Then: validation rejects missing, malformed, or falsely tuned evidence.
    with pytest.raises(ValueError, match=message):
        validate(FROZEN, MANIFEST, write_audit(tmp_path, audit))


def _towns_surface(audit: dict) -> dict:
    return next(surface for surface in audit["setting_surfaces"] if surface["file"] == FILE)
