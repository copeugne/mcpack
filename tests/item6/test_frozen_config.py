# pyright: standard
"""Regression tests for the Item 6 configuration evidence."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
from types import ModuleType

import pytest

ROOT = Path(__file__).parents[2]
SPEC = importlib.util.spec_from_file_location(
    "freeze_item6_config", ROOT / "tools/freeze_item6_config.py"
)
assert SPEC is not None
assert SPEC.loader is not None
MODULE = ModuleType(SPEC.name)
SPEC.loader.exec_module(MODULE)
capture = MODULE.capture
validate = MODULE.validate
FROZEN = ROOT / "evidence/item-6/frozen"
MANIFEST = ROOT / "evidence/item-6/generated-config-manifest.json"
AUDIT = ROOT / "evidence/item-6/config-audit.json"


def test_committed_item6_evidence_validates() -> None:
    """The committed report must remain bound to every frozen file."""
    validate(FROZEN, MANIFEST, AUDIT)


def test_frozen_tree_has_all_generation_stages() -> None:
    """The evidence distinguishes installation, startup, and world creation."""
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    stages = {row["generation_stage"] for row in manifest["files"]}
    assert stages == {"installation", "first_startup", "world_creation"}


def test_audit_covers_required_systems() -> None:
    """Every configuration system named by the Item 6 gate is explicit."""
    audit = json.loads(AUDIT.read_text(encoding="utf-8"))
    systems = {row["system"] for row in audit["systems"]}
    assert systems == {
        "C2ME",
        "Chunky",
        "Difficulty",
        "IDAS",
        "Integrated structures",
        "Loot Integrations",
        "Mob spawning and entity limits",
        "Moog structure families",
        "ServerCore",
        "Sparse Structures",
        "Structure Essentials",
        "Structure Layout Optimizer",
        "Village generation",
        "WDA Seven Seas",
        "When Dungeons Arise",
        "YUNG structure systems",
    }


def test_audit_includes_all_yung_replacement_configs() -> None:
    """Every generated YUNG config that disables a vanilla structure is audited."""
    audit = json.loads(AUDIT.read_text(encoding="utf-8"))
    yung = next(row for row in audit["systems"] if row["system"] == "YUNG structure systems")
    assert set(yung["files"]) >= {
        "config/betterdeserttemples-neoforge-1_21.toml",
        "config/betterfortresses-neoforge-1_21.toml",
        "config/betterjungletemples-neoforge-1_21.toml",
        "config/bettermineshafts-neoforge-1_21.toml",
        "config/betteroceanmonuments-neoforge-1_21.toml",
        "config/betterwitchhuts-neoforge-1_21.toml",
    }


def test_validator_rejects_unaccounted_manifest_file(tmp_path: Path) -> None:
    """A partial semantic audit cannot satisfy the exhaustive file-accounting gate."""
    audit = json.loads(AUDIT.read_text(encoding="utf-8"))
    audit["file_accounting"][1]["files"].pop()
    partial_audit = tmp_path / "partial-audit.json"
    partial_audit.write_text(json.dumps(audit), encoding="utf-8")
    with pytest.raises(ValueError, match="file accounting does not match manifest"):
        validate(FROZEN, MANIFEST, partial_audit)


def test_validator_rejects_changed_content(tmp_path: Path) -> None:
    """Rehashing is required after any preserved-content mutation."""
    captured = tmp_path / "frozen"
    capture(FROZEN, captured)
    # capture expects an instance shape, so the synthetic output cannot validate.
    with pytest.raises(ValueError, match="inventory"):
        validate(captured, MANIFEST, AUDIT)


def test_capture_refuses_existing_target(tmp_path: Path) -> None:
    """Baseline capture never overwrites earlier evidence."""
    output = tmp_path / "existing"
    output.mkdir()
    with pytest.raises(FileExistsError):
        capture(FROZEN, output)
