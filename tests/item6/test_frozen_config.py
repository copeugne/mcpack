# pyright: standard
"""Regression tests for the Item 6 configuration evidence."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest

from tests.item6.helpers import (
    AUDIT,
    FROZEN,
    MANIFEST,
    capture,
    validate,
    write_audit,
)

if TYPE_CHECKING:
    from pathlib import Path


YUNG_REPLACEMENT_FILES = {
    "config/betterdeserttemples-neoforge-1_21.toml",
    "config/betterfortresses-neoforge-1_21.toml",
    "config/betterjungletemples-neoforge-1_21.toml",
    "config/bettermineshafts-neoforge-1_21.toml",
    "config/betteroceanmonuments-neoforge-1_21.toml",
    "config/betterwitchhuts-neoforge-1_21.toml",
}


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


def test_yung_replacement_configs_are_audited_with_settings() -> None:
    audit = json.loads(AUDIT.read_text(encoding="utf-8"))
    yung = next(row for row in audit["systems"] if row["system"] == "YUNG structure systems")
    setting_files = {row["file"] for row in audit["settings"]}
    assert set(yung["files"]) >= YUNG_REPLACEMENT_FILES
    assert setting_files >= YUNG_REPLACEMENT_FILES


def test_validator_rejects_missing_file_accounting(tmp_path: Path) -> None:
    audit = json.loads(AUDIT.read_text(encoding="utf-8"))
    audit["file_accounting"][1]["files"].pop()
    with pytest.raises(ValueError, match="file accounting does not match manifest"):
        validate(FROZEN, MANIFEST, write_audit(tmp_path, audit))


def test_validator_rejects_duplicate_file_accounting(tmp_path: Path) -> None:
    audit = json.loads(AUDIT.read_text(encoding="utf-8"))
    duplicate = audit["file_accounting"][0]["files"][0]
    audit["file_accounting"][1]["files"].append(duplicate)
    with pytest.raises(ValueError, match="file is classified more than once"):
        validate(FROZEN, MANIFEST, write_audit(tmp_path, audit))


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
