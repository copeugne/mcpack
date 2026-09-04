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
}
Mutation = Literal["missing", "value", "line", "non-default"]


def test_towns_and_towers_separations_bind_declared_defaults() -> None:
    # Given: the committed Towns and Towers grouped configuration surface.
    surface = _towns_surface(AUDIT_DATA)
    leaves = {leaf["key"]: leaf for leaf in surface["leaves"]}

    # When: its two generated separation claims are inspected.
    separations = {key: leaves[key] for key in DEFAULTS}

    # Then: frozen values remain 12 while source-declared defaults bind to 24 without tuning.
    assert {key: leaf["generated_default"] for key, leaf in separations.items()} == dict.fromkeys(
        DEFAULTS, 12
    )
    assert {key: leaf["effective_value"] for key, leaf in separations.items()} == dict.fromkeys(
        DEFAULTS, 12
    )
    assert {key: leaf["upstream_default"] for key, leaf in separations.items()} == DEFAULTS
    assert all(leaf["non_default"] is False for leaf in separations.values())
    validate(FROZEN, MANIFEST, AUDIT)


@pytest.mark.parametrize(
    ("mutation", "message"),
    [
        ("missing", "requires declared default evidence"),
        ("value", "declared default evidence does not match source"),
        ("line", "declared default evidence does not match source"),
        ("non-default", "unexpectedly reports tuning"),
    ],
)
def test_validator_rejects_inexact_towns_and_towers_default_claim(
    tmp_path: Path, mutation: Mutation, message: str
) -> None:
    # Given: one committed declared-default claim is corrupted.
    audit = deepcopy(AUDIT_DATA)
    leaf = next(
        leaf
        for leaf in _towns_surface(audit)["leaves"]
        if leaf["key"] == "towers.separation"
    )
    match mutation:
        case "missing":
            del leaf["upstream_default"]
        case "value":
            leaf["upstream_default"]["value"] = 23
        case "line":
            leaf["upstream_default"]["line"] = 29
        case "non-default":
            leaf["non_default"] = True
        case unreachable:
            assert_never(unreachable)

    # When/Then: validation rejects missing, malformed, or falsely tuned evidence.
    with pytest.raises(ValueError, match=message):
        validate(FROZEN, MANIFEST, write_audit(tmp_path, audit))


def _towns_surface(audit: dict) -> dict:
    return next(surface for surface in audit["setting_surfaces"] if surface["file"] == FILE)
