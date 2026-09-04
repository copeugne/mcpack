from __future__ import annotations

from pathlib import Path

import pytest
from pydantic import ValidationError

from mcpack_evidence.item7_protocol import load_protocol

ROOT = Path(__file__).parents[2]
PROTOCOL = ROOT / "evidence/item-7/protocol/worldgen-audit-v1.json"

EXPECTED_SEEDS = (
    ("ordinary", "42"),
    ("mountainous", "6671238423019257953"),
    ("ocean-heavy", "95920844204830198"),
    ("biome-diverse", "-3503646078644842058"),
)
EXPECTED_SELECTIONS = (
    ("overworld", "minecraft:overworld", 0, 0, 31, 3969),
    ("nether", "minecraft:the_nether", 0, 0, 15, 961),
    ("end-central", "minecraft:the_end", 0, 0, 15, 961),
    ("end-outer", "minecraft:the_end", 1536, 0, 15, 961),
)
EXPECTED_PROVIDERS = (
    "Tectonic",
    "Terralith",
    "Biomes O' Plenty",
    "Regions Unexplored",
    "TerraBlender",
    "Lithostitched",
    "BetterEnd",
    "YUNG",
    "WDA",
    "IDAS",
    "Integrated structures",
    "Moog",
    "Explorify",
    "Explorations",
    "Repurposed Structures",
    "CTOV",
    "Towns & Towers",
)


def test_protocol_binds_frozen_identity_runs_seeds_and_selections() -> None:
    # Given: the committed Item 7 protocol.
    # When: the strict boundary parses it.
    protocol = load_protocol(PROTOCOL)

    # Then: it binds every fixed upstream identity and experiment denominator.
    assert protocol.identity.retained_manifest.count == 136
    assert protocol.identity.retained_manifest.sha256 == (
        "78e5bdc0697299782a535400ad5b313c088e8db10cfe075085ae4c8a531e30cb"
    )
    assert protocol.identity.frozen_config_manifest.sha256 == (
        "2e0aaeb0f84747a3cb17146eb435d34cc7d6703b9372211e8fc8cff2df2b436f"
    )
    assert protocol.identity.config_audit.sha256 == (
        "181e0c299f44ded319d93c84f7b983738364b4090286251b00421fa041b989dd"
    )
    assert protocol.identity.seed_suite.sha256 == (
        "de5e5e89bd04b6f75dac4eab2e84524956f46faa91660b5315c8eade269d39ae"
    )
    assert protocol.runs == ("run-a", "run-b")
    assert tuple((row.role, row.seed) for row in protocol.seeds) == EXPECTED_SEEDS
    assert {row.coordinate_unit for row in protocol.selections} == {"block"}
    assert (
        tuple(
            (
                row.label,
                row.dimension,
                row.center_x,
                row.center_z,
                row.radius_chunks,
                row.expected_chunk_count,
            )
            for row in protocol.selections
        )
        == EXPECTED_SELECTIONS
    )
    end_outer = protocol.selections[3]
    assert (end_outer.center_x // 16, end_outer.center_z // 16) == (96, 0)


def test_protocol_covers_providers_anomalies_and_primary_classes_exactly() -> None:
    protocol = load_protocol(PROTOCOL)

    assert tuple(row.label for row in protocol.providers) == EXPECTED_PROVIDERS
    assert tuple(row.label for row in protocol.providers if row.observation_role == "library") == (
        "TerraBlender",
        "Lithostitched",
    )
    assert len(protocol.anomaly_classes) == 12
    assert protocol.primary_classifications == (
        "cosmetic",
        "gameplay",
        "performance",
        "outright_generation_failure",
    )


def test_protocol_fixes_normalization_region_accounting_and_archive_policy() -> None:
    protocol = load_protocol(PROTOCOL)

    assert "timestamp" in protocol.normalization.excluded_transport_fields
    assert "heightmaps" in protocol.normalization.chunk_compare_fields
    assert protocol.regions.account_every_mca_file is True
    assert protocol.regions.kinds == ("anvil", "empty_placeholder")
    assert protocol.regions.empty_placeholder_size_bytes == 0
    assert protocol.regions.unexplained_files_allowed is False
    assert protocol.archive.committed_receipts_root == "evidence/item-7"
    assert protocol.archive.restore_required is True
    assert "session_lock" in protocol.archive.forbidden_contents


@pytest.mark.parametrize(
    ("original", "replacement", "field"),
    [
        (
            "2e0aaeb0f84747a3cb17146eb435d34cc7d6703b9372211e8fc8cff2df2b436f",
            "0" * 64,
            "frozen_config_manifest.sha256",
        ),
        ('"observation_role": "direct"', '"observation_role": "library"', "providers"),
        ('"timestamp"', '"runtime_timestamp"', "normalization"),
        ('      "session_lock",\n', "", "archive"),
    ],
)
def test_protocol_rejects_frozen_value_drift(
    tmp_path: Path, original: str, replacement: str, field: str
) -> None:
    altered = tmp_path / "altered.json"
    _ = altered.write_text(
        PROTOCOL.read_text(encoding="utf-8").replace(original, replacement, 1),
        encoding="utf-8",
    )

    with pytest.raises(ValidationError, match=field):
        _ = load_protocol(altered)


def test_protocol_rejects_unexplained_fields(tmp_path: Path) -> None:
    altered = tmp_path / "altered.json"
    _ = altered.write_text(
        PROTOCOL.read_text(encoding="utf-8").replace("{\n", '{\n  "unexpected": true,\n', 1),
        encoding="utf-8",
    )

    with pytest.raises(ValidationError, match="unexpected"):
        _ = load_protocol(altered)


@pytest.mark.parametrize(
    "injected",
    [
        '"schema_version": "item7-worldgen-audit-v1",',
        '"unexpected_number": NaN,',
    ],
)
def test_protocol_rejects_non_strict_json(tmp_path: Path, injected: str) -> None:
    altered = tmp_path / "altered.json"
    _ = altered.write_text(
        PROTOCOL.read_text(encoding="utf-8").replace("{\n", "{\n  " + injected + "\n", 1),
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="not strict"):
        _ = load_protocol(altered)
