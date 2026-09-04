# pyright: standard
"""Regression tests for the Item 6 configuration evidence."""

from __future__ import annotations

import json
import shutil
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
YUNG_PROVIDER_NAMES = {
    "betterdeserttemples",
    "betterdungeons",
    "betterfortresses",
    "betterjungletemples",
    "bettermineshafts",
    "betteroceanmonuments",
    "betterstrongholds",
    "betterwitchhuts",
}
YUNG_PROVIDER_FILES = {
    f"config/cristellib/{provider}/structure_{kind}_config.json5"
    for provider in YUNG_PROVIDER_NAMES
    for kind in ("placement", "toggle")
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


def test_yung_cristellib_provider_pairs_are_audited_and_cited() -> None:
    audit = json.loads(AUDIT.read_text(encoding="utf-8"))
    yung = next(row for row in audit["systems"] if row["system"] == "YUNG structure systems")
    audited = next(
        set(row["files"]) for row in audit["file_accounting"] if row["classification"] == "audited"
    )
    out_of_scope = next(
        set(row["files"])
        for row in audit["file_accounting"]
        if row["classification"] == "out-of-scope"
    )
    cited = {
        *(path for system in audit["systems"] for path in system["files"]),
        *(setting["file"] for setting in audit["settings"]),
        *(path for finding in audit["findings"] for path in finding["files"]),
    }
    setting_files = {row["file"] for row in audit["settings"]}
    provider_files_in_system = {
        path
        for path in yung["files"]
        if path.startswith("config/cristellib/better") and path.split("/")[2] in YUNG_PROVIDER_NAMES
    }
    assert len(YUNG_PROVIDER_FILES) == 16
    assert provider_files_in_system == YUNG_PROVIDER_FILES
    assert setting_files >= YUNG_PROVIDER_FILES
    assert cited >= YUNG_PROVIDER_FILES
    assert audited >= YUNG_PROVIDER_FILES
    assert YUNG_PROVIDER_FILES.isdisjoint(out_of_scope)


def test_yung_cristellib_settings_cover_every_placement_and_toggle_leaf() -> None:
    audit = json.loads(AUDIT.read_text(encoding="utf-8"))
    for path in YUNG_PROVIDER_FILES:
        expected_evidence = {
            line.strip().rstrip(",")
            for line in (FROZEN / path).read_text(encoding="utf-8").splitlines()
            if line.strip().startswith('"')
            and not line.strip().endswith("{")
            and not line.strip().startswith('"salt"')
        }
        actual_evidence = set()
        source_lines = (FROZEN / path).read_text(encoding="utf-8").splitlines()
        for row in audit["settings"]:
            if row["file"] != path:
                continue
            evidence = row["evidence"]
            assert evidence["decoder"] == "json"
            assert evidence["effective_semantics"] == "same_as_generated"
            assert len(evidence["observations"]) == 1
            observation = evidence["observations"][0]
            source_line = source_lines[observation["line"] - 1].strip()
            assert source_line == (
                observation["prefix"]
                + json.dumps(row["generated_default"], separators=(",", ":"))
                + observation["suffix"]
            )
            actual_evidence.add(source_line.rstrip(","))
        assert actual_evidence == expected_evidence


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


def test_validator_rejects_yung_out_of_scope_classification(tmp_path: Path) -> None:
    audit = json.loads(AUDIT.read_text(encoding="utf-8"))
    audited = next(row for row in audit["file_accounting"] if row["classification"] == "audited")
    out_of_scope = next(
        row for row in audit["file_accounting"] if row["classification"] == "out-of-scope"
    )
    path = "config/cristellib/betterdeserttemples/structure_placement_config.json5"
    audited["files"].remove(path)
    out_of_scope["files"].append(path)
    with pytest.raises(
        ValueError, match="audited file accounting does not match cited audit evidence"
    ):
        validate(FROZEN, MANIFEST, write_audit(tmp_path, audit))


def test_validator_rejects_changed_content(tmp_path: Path) -> None:
    """Rehashing is required after any preserved-content mutation."""
    instance = tmp_path / "instance"
    for source, target in (
        (FROZEN / "config", instance / "config"),
        (FROZEN / "defaultconfigs", instance / "defaultconfigs"),
        (FROZEN / "world-serverconfig", instance / "world" / "serverconfig"),
    ):
        _ = shutil.copytree(source, target)
    _ = shutil.copy2(FROZEN / "server.properties", instance / "server.properties")
    captured = tmp_path / "frozen"
    capture(instance, captured)
    changed = captured / "config/cupboard.json"
    changed.write_bytes(changed.read_bytes() + b"\n")
    with pytest.raises(ValueError, match="identity mismatch"):
        validate(captured, MANIFEST, AUDIT)


def test_capture_refuses_existing_target(tmp_path: Path) -> None:
    """Baseline capture never overwrites earlier evidence."""
    output = tmp_path / "existing"
    output.mkdir()
    with pytest.raises(FileExistsError):
        capture(FROZEN, output)
