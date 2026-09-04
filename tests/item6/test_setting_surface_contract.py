# pyright: standard
from __future__ import annotations

import json
from collections import Counter
from copy import deepcopy
from typing import TYPE_CHECKING, Literal, assert_never

import pytest

from mcpack_evidence.item6_surface_validation import build_setting_surface
from tests.item6.helpers import AUDIT, FROZEN, MANIFEST, validate, write_audit

if TYPE_CHECKING:
    from pathlib import Path

    from mcpack_evidence.item6_validation import Audit

AUDIT_DATA = json.loads(AUDIT.read_text(encoding="utf-8"))
SurfaceMutation = Literal[
    "system",
    "file",
    "decoder",
    "empty",
    "omitted",
    "duplicate-file",
    "duplicate-key",
    "duplicate-line",
]
LeafMutation = Literal[
    "key",
    "line",
    "prefix",
    "suffix",
    "generated-value",
    "generated-type",
    "effective-value",
    "non-default",
]


def test_every_cristellib_structure_surface_is_audited_exactly_once() -> None:
    source_files = sorted(
        relative.relative_to(FROZEN).as_posix()
        for pattern in (
            "config/cristellib/*/structure_placement_config.json5",
            "config/cristellib/*/structure_toggle_config.json5",
        )
        for relative in FROZEN.glob(pattern)
    )
    grouped_files = [
        surface["file"]
        for surface in AUDIT_DATA["setting_surfaces"]
        if surface["file"].endswith(
            ("/structure_placement_config.json5", "/structure_toggle_config.json5")
        )
    ]
    legacy_files = {
        setting["file"]
        for setting in AUDIT_DATA["settings"]
        if setting["file"].endswith(
            ("/structure_placement_config.json5", "/structure_toggle_config.json5")
        )
    }
    excluded = next(
        row["files"]
        for row in AUDIT_DATA["file_accounting"]
        if row["classification"] == "out-of-scope"
    )
    assert Counter(grouped_files) == Counter(set(grouped_files))
    assert set(grouped_files).isdisjoint(legacy_files)
    assert set(grouped_files) | legacy_files == set(source_files)
    assert set(source_files).isdisjoint(excluded)

    for relative in legacy_files:
        provider = relative.removeprefix("config/cristellib/").partition("/")[0]
        source_leaves = [
            leaf
            for leaf in build_setting_surface("legacy", relative, FROZEN / relative)["leaves"]
            if not leaf["key"].endswith(".salt")
        ]
        settings = [setting for setting in AUDIT_DATA["settings"] if setting["file"] == relative]
        expected_keys = {f"{provider}.{leaf['key']}" for leaf in source_leaves}
        observation_lines = [
            observation["line"]
            for setting in settings
            for observation in setting["evidence"]["observations"]
        ]
        assert len(settings) == len(source_leaves)
        assert {setting["key"] for setting in settings} == expected_keys
        assert Counter(observation_lines) == Counter(leaf["line"] for leaf in source_leaves)


def audit_with_wda_placement_surface() -> Audit:
    audit = deepcopy(AUDIT_DATA)
    relative = "config/cristellib/dungeons_arise/structure_placement_config.json5"
    audit["settings"] = [setting for setting in audit["settings"] if setting["file"] != relative]
    audit["setting_surfaces"] = [
        build_setting_surface("When Dungeons Arise", relative, FROZEN / relative)
    ]
    return audit


def test_complete_grouped_surface_validates(tmp_path: Path) -> None:
    # Given: one complete surface replaces every legacy row for its source file.
    audit = audit_with_wda_placement_surface()

    # When/Then: exact grouped evidence validates against the preserved source.
    with pytest.raises(ValueError, match="audit semantic identity"):
        validate(FROZEN, MANIFEST, write_audit(tmp_path, audit))


def test_validator_rejects_unknown_surface_fields(tmp_path: Path) -> None:
    # Given: a surface with an undeclared field.
    audit = audit_with_wda_placement_surface()
    encoded_surface = json.loads(json.dumps(audit["setting_surfaces"][0]))
    encoded_surface["unexpected"] = True
    audit["setting_surfaces"] = [encoded_surface]

    # When/Then: strict audit parsing rejects it at the boundary.
    with pytest.raises(ValueError, match="extra_forbidden"):
        validate(FROZEN, MANIFEST, write_audit(tmp_path, audit))


def test_validator_rejects_unknown_surface_leaf_fields(tmp_path: Path) -> None:
    # Given: a grouped leaf with an undeclared field.
    audit = json.loads(json.dumps(audit_with_wda_placement_surface()))
    audit["setting_surfaces"][0]["leaves"][0]["unexpected"] = True

    # When/Then: strict nested audit parsing rejects it at the boundary.
    with pytest.raises(ValueError, match="extra_forbidden"):
        validate(FROZEN, MANIFEST, write_audit(tmp_path, audit))


def test_validator_rejects_file_claimed_by_legacy_and_grouped_evidence(tmp_path: Path) -> None:
    # Given: a complete grouped surface for a file that still has a legacy setting row.
    audit = deepcopy(AUDIT_DATA)
    relative = "config/cristellib/dungeons_arise/structure_placement_config.json5"
    audit["setting_surfaces"] = [
        surface for surface in audit["setting_surfaces"] if surface["file"] != relative
    ]
    audit["setting_surfaces"].append(
        build_setting_surface("When Dungeons Arise", relative, FROZEN / relative)
    )
    audit["settings"].append(
        {
            "system": "When Dungeons Arise",
            "file": relative,
            "key": "major_structures.spacing",
            "scope": "major structures",
            "owner": "dungeons_arise",
            "interactions": [],
            "evidence": {
                "decoder": "json",
                "observations": [{"line": 8, "prefix": '"spacing": ', "suffix": ""}],
                "effective_semantics": "same_as_generated",
            },
            "generated_default": 50,
            "effective_value": 50,
            "non_default": False,
        }
    )

    # When/Then: validation rejects two competing evidence representations for one file.
    with pytest.raises(ValueError, match="both legacy and grouped"):
        validate(FROZEN, MANIFEST, write_audit(tmp_path, audit))


@pytest.mark.parametrize(
    ("mutation", "message"),
    [
        ("system", "system is not declared"),
        ("file", "unpreserved file"),
        ("decoder", "decoder does not match"),
        ("empty", "leaves must be nonempty"),
        ("omitted", "enumerate every source leaf"),
        ("duplicate-file", "file must be unique"),
        ("duplicate-key", "keys and lines must be unique"),
        ("duplicate-line", "keys and lines must be unique"),
    ],
)
def test_validator_rejects_inexact_surface_contract(
    tmp_path: Path, mutation: SurfaceMutation, message: str
) -> None:
    # Given: a complete surface with one surface-level dimension corrupted.
    audit = audit_with_wda_placement_surface()
    surface = audit["setting_surfaces"][0]
    match mutation:
        case "system":
            surface["system"] = "undeclared"
        case "file":
            surface["file"] = "config/missing.json5"
        case "decoder":
            surface["decoder"] = "json"
        case "empty":
            surface["leaves"] = []
        case "omitted":
            _ = surface["leaves"].pop()
        case "duplicate-file":
            audit["setting_surfaces"].append(deepcopy(surface))
        case "duplicate-key":
            surface["leaves"][1]["key"] = surface["leaves"][0]["key"]
        case "duplicate-line":
            surface["leaves"][1]["line"] = surface["leaves"][0]["line"]
        case unreachable:
            assert_never(unreachable)

    # When/Then: strict validation rejects that exact corruption.
    with pytest.raises(ValueError, match=message):
        validate(FROZEN, MANIFEST, write_audit(tmp_path, audit))


@pytest.mark.parametrize(
    ("mutation", "message"),
    [
        ("key", "line evidence does not match"),
        ("line", "line evidence does not match"),
        ("prefix", "line evidence does not match"),
        ("suffix", "line evidence does not match"),
        ("generated-value", "generated value does not match"),
        ("generated-type", "generated value does not match"),
        ("effective-value", "effective value does not match"),
        ("non-default", "non-default flag does not match declared default"),
    ],
)
def test_validator_rejects_inexact_leaf_contract(
    tmp_path: Path, mutation: LeafMutation, message: str
) -> None:
    # Given: a complete surface with one leaf-level dimension corrupted.
    audit = audit_with_wda_placement_surface()
    leaf = audit["setting_surfaces"][0]["leaves"][0]
    match mutation:
        case "key":
            leaf["key"] = f"wrong.{leaf['key']}"
        case "line":
            leaf["line"] += 1_000
        case "prefix":
            leaf["prefix"] = f"wrong{leaf['prefix']}"
        case "suffix":
            leaf["suffix"] = "wrong"
        case "generated-value":
            leaf["generated_default"] = False
        case "generated-type":
            leaf["generated_default"] = str(leaf["generated_default"])
        case "effective-value":
            leaf["effective_value"] = False
        case "non-default":
            leaf["non_default"] = True
        case unreachable:
            assert_never(unreachable)

    # When/Then: strict validation rejects that exact corruption.
    with pytest.raises(ValueError, match=message):
        validate(FROZEN, MANIFEST, write_audit(tmp_path, audit))
