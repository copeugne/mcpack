from __future__ import annotations

import json
from typing import TYPE_CHECKING

from mcpack_evidence.item6_json import parse_strict_json
from mcpack_evidence.item7_control_compare import ControlComparisonInputs, compare_control

if TYPE_CHECKING:
    from pathlib import Path

    from pydantic import JsonValue


def _receipt(path: Path, *, pilot: bool) -> None:
    preflight: dict[str, JsonValue] = {
        "seed": "42",
        "java_version": "Temurin-21.0.12.1+1-LTS",
        "retained_manifest_sha256": (
            "78e5bdc0697299782a535400ad5b313c088e8db10cfe075085ae4c8a531e30cb"
        ),
        "frozen_manifest_sha256": (
            "2e0aaeb0f84747a3cb17146eb435d34cc7d6703b9372211e8fc8cff2df2b436f"
        ),
        "config_audit_sha256": ("181e0c299f44ded319d93c84f7b983738364b4090286251b00421fa041b989dd"),
        "seed_suite_sha256": ("de5e5e89bd04b6f75dac4eab2e84524956f46faa91660b5315c8eade269d39ae"),
    }
    payload: dict[str, JsonValue] = {
        "preflight": preflight,
        "lifecycle": {
            "ready": True,
            "save_all_flush": True,
            "clean_stop": True,
            "return_code": 0,
            "process_group_killed": False,
            "rejection_reason": None,
        },
        "rejection_reason": None,
    }
    if pilot:
        preflight.update(
            {
                "retained_candidate_count": 136,
                "instrumented_candidate_count": 137,
                "retained_runtime_sha256": "a" * 64,
                "instrumented_runtime_sha256": "b" * 64,
                "chunky_sha256": "d72f235cf1f56f2c374f52c00bdda5034524b28142305a84cfc123a3f92ad274",
            }
        )
    else:
        preflight.update({"candidate_count": 136, "runtime_sha256": "a" * 64})
    _ = path.write_text(json.dumps(payload), encoding="utf-8")


def _chunks(path: Path, *, changed: bool) -> None:
    rows: list[str] = []
    for x in range(-4, 5):
        for z in range(-4, 5):
            row: dict[str, JsonValue] = {
                "schema_version": "item7-anvil-chunk-v1",
                "dimension": "minecraft:overworld",
                "region": "region/r.0.0.mca",
                "slot": 0,
                "timestamp": 1,
                "chunk_x": x,
                "chunk_z": z,
                "data_version": 4000 if changed and (x, z) == (0, 0) else 3955,
                "status": "minecraft:full",
                "full": True,
                "compression": "zlib",
                "external": False,
                "heightmaps": [],
                "biome_sections": [],
                "structure_starts": [],
            }
            rows.append(json.dumps(row, separators=(",", ":")))
    _ = path.write_text("\n".join(rows) + "\n", encoding="utf-8")


def test_compare_control_reports_inconclusive_difference_when_repeat_is_nondeterministic(
    tmp_path: Path,
) -> None:
    control, pilot = tmp_path / "control", tmp_path / "pilot"
    control.mkdir()
    pilot.mkdir()
    for root, changed in ((control, False), (pilot, True)):
        _receipt(root / "run-receipt.json", pilot=changed)
        _chunks(root / "chunks.jsonl", changed=changed)
    repeat = tmp_path / "repeat.json"
    _ = repeat.write_text(
        '{"schema_version":"item7-repeat-comparison-v1","equal":false}', encoding="utf-8"
    )
    output = tmp_path / "comparison.json"

    equal = compare_control(ControlComparisonInputs(control, pilot, repeat, output))

    payload = parse_strict_json(output.read_bytes())
    assert isinstance(payload, dict)
    counts = payload["field_mismatch_counts"]
    assert isinstance(counts, dict)
    assert equal is False
    assert payload["disposition"] == "not_attributable_due_to_measured_stack_nondeterminism"
    assert counts["data_version"] == 1
