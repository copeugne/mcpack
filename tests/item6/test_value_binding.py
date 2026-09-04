# pyright: standard
from __future__ import annotations

import json
from copy import deepcopy
from typing import TYPE_CHECKING, Literal, assert_never

import pytest

from tests.item6.helpers import AUDIT, FROZEN, MANIFEST, validate, write_audit

if TYPE_CHECKING:
    from pathlib import Path

AUDIT_DATA = json.loads(AUDIT.read_text(encoding="utf-8"))
CLAIM_FIELDS = ("generated_default", "effective_value")
CLAIM_CASES = tuple(
    (index, field) for index in range(len(AUDIT_DATA["settings"])) for field in CLAIM_FIELDS
)
C2ME_KEY = "vanillaWorldGenOptimizations.useEndBiomeCache"
Mutation = Literal[
    "empty",
    "line-zero",
    "line-past-end",
    "wrong-prefix",
    "wrong-suffix",
    "decoder",
    "semantics",
    "malformed-scalar",
]


def changed_claim(value: bool | float | str) -> bool | float | str:
    match value:
        case bool():
            return 1
        case int():
            return value + 1
        case float():
            return value + 0.5
        case str():
            return f"{value}-mutated"
        case unreachable:
            assert_never(unreachable)


@pytest.mark.parametrize(
    ("setting_index", "field"),
    CLAIM_CASES,
    ids=(f"setting-{index}-{field}" for index, field in CLAIM_CASES),
)
def test_claimed_setting_value_is_bound_to_source(
    tmp_path: Path, setting_index: int, field: str
) -> None:
    audit = deepcopy(AUDIT_DATA)
    audit["settings"][setting_index][field] = changed_claim(audit["settings"][setting_index][field])

    with pytest.raises(ValueError, match="setting claimed value does not match source"):
        validate(FROZEN, MANIFEST, write_audit(tmp_path, audit))


def test_claimed_setting_value_cases_cover_every_row_and_field() -> None:
    assert len(CLAIM_CASES) == 2 * len(AUDIT_DATA["settings"])
    assert set(CLAIM_CASES) == {
        (index, field) for index in range(len(AUDIT_DATA["settings"])) for field in CLAIM_FIELDS
    }
    c2me_index = next(
        index for index, setting in enumerate(AUDIT_DATA["settings"]) if setting["key"] == C2ME_KEY
    )
    assert {(c2me_index, field) for field in CLAIM_FIELDS} <= set(CLAIM_CASES)


def test_structured_setting_evidence_is_committed_for_every_setting() -> None:
    for setting in AUDIT_DATA["settings"]:
        evidence = setting["evidence"]
        assert set(evidence) == {"decoder", "observations", "effective_semantics"}
        assert evidence["decoder"] in {"json", "toml", "string"}
        assert evidence["observations"]
        assert all(
            set(observation) == {"line", "prefix", "suffix"} and observation["line"] >= 1
            for observation in evidence["observations"]
        )


def test_committed_setting_keys_do_not_hide_wildcard_leaves() -> None:
    wildcard_rows = [setting for setting in AUDIT_DATA["settings"] if "*" in setting["key"]]
    assert wildcard_rows == []


def test_validator_rejects_wildcard_without_explicit_leaf_observations(
    tmp_path: Path,
) -> None:
    audit = deepcopy(AUDIT_DATA)
    audit["settings"][0]["key"] = "spreadFactor.*"

    with pytest.raises(ValueError, match="wildcard setting evidence must enumerate"):
        validate(FROZEN, MANIFEST, write_audit(tmp_path, audit))


def test_validator_rejects_decoder_that_only_coincidentally_decodes(tmp_path: Path) -> None:
    audit = deepcopy(AUDIT_DATA)
    audit["settings"][0]["evidence"]["decoder"] = "toml"

    with pytest.raises(ValueError, match="decoder does not match source format"):
        validate(FROZEN, MANIFEST, write_audit(tmp_path, audit))


@pytest.mark.parametrize(
    ("mutation", "message"),
    [
        ("empty", "setting evidence observations must be nonempty"),
        ("line-zero", "setting evidence line must be a positive integer"),
        ("line-past-end", "setting evidence line is out of range"),
        ("wrong-prefix", "setting evidence prefix does not match source line"),
        ("wrong-suffix", "setting evidence suffix does not match source line"),
        ("decoder", "unsupported setting evidence decoder"),
        ("semantics", "unsupported setting effective semantics"),
        ("malformed-scalar", "setting evidence scalar is malformed"),
    ],
)
def test_validator_rejects_invalid_observation_contract(
    tmp_path: Path, mutation: Mutation, message: str
) -> None:
    audit = deepcopy(AUDIT_DATA)
    setting = audit["settings"][0]
    observation = setting["evidence"]["observations"][0]
    match mutation:
        case "empty":
            setting["evidence"]["observations"] = []
        case "line-zero":
            observation["line"] = 0
        case "line-past-end":
            observation["line"] = 10_000
        case "wrong-prefix":
            observation["prefix"] = f"x{observation['prefix']}"
        case "wrong-suffix":
            observation["suffix"] = f"{observation['suffix']}x"
        case "decoder":
            setting["evidence"]["decoder"] = "yaml"
        case "semantics":
            setting["evidence"]["effective_semantics"] = "unknown"
        case "malformed-scalar":
            observation.update({"line": 1, "prefix": "", "suffix": ""})
        case unreachable:
            assert_never(unreachable)

    with pytest.raises(ValueError, match=message):
        validate(FROZEN, MANIFEST, write_audit(tmp_path, audit))


def test_validator_rejects_mixed_observation_values(tmp_path: Path) -> None:
    audit = deepcopy(AUDIT_DATA)
    spacing = audit["settings"][2]
    enabled = audit["settings"][3]
    spacing["evidence"]["observations"].append(enabled["evidence"]["observations"][0])

    with pytest.raises(ValueError, match="setting evidence observations disagree"):
        validate(FROZEN, MANIFEST, write_audit(tmp_path, audit))


def test_validator_rejects_c2me_semantics_on_other_key(tmp_path: Path) -> None:
    audit = deepcopy(AUDIT_DATA)
    audit["settings"][0]["evidence"]["effective_semantics"] = "c2me_biolith_runtime_disable"

    with pytest.raises(ValueError, match="C2ME runtime-disable semantics require"):
        validate(FROZEN, MANIFEST, write_audit(tmp_path, audit))


def test_c2me_exception_binds_default_and_biolith_comments() -> None:
    c2me = next(setting for setting in AUDIT_DATA["settings"] if setting["key"] == C2ME_KEY)
    assert c2me["generated_default"] == "default"
    assert c2me["effective_value"] == "compatibility-disabled at runtime"
    assert c2me["evidence"] == {
        "decoder": "toml",
        "effective_semantics": "c2me_biolith_runtime_disable",
        "observations": [
            {
                "line": 80,
                "prefix": "useEndBiomeCache = ",
                "suffix": "",
            },
            {
                "line": 78,
                "prefix": "# Set to false for the following reasons:",
                "suffix": "",
            },
            {
                "line": 79,
                "prefix": "# Incompatible with biolith@3.0.10 (*) (defined in c2me)",
                "suffix": "",
            },
        ],
    }
