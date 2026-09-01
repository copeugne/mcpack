from __future__ import annotations

import subprocess
import sys
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path


def test_range_request_and_evaluator_tools_round_trip(tmp_path: Path) -> None:
    inspection = tmp_path / "inspection.json"
    requests = tmp_path / "requests.tsv"
    results = tmp_path / "results.tsv"
    output = tmp_path / "compatibility.json"
    _ = inspection.write_text(_inspection_json(), encoding="utf-8")
    _run(
        "tools/build_maven_range_requests.py",
        "--inspection",
        str(inspection),
        "--output",
        str(requests),
    )
    request_lines = requests.read_text(encoding="utf-8").splitlines()
    assert request_lines == ["range_0001\t4.0\t[4,)"]
    _ = results.write_text("range_0001\tpass\t[4,)\n", encoding="utf-8")

    _run(
        "tools/evaluate_candidate_compatibility.py",
        "--inspection",
        str(inspection),
        "--oracle-requests",
        str(requests),
        "--oracle-results",
        str(results),
        "--output",
        str(output),
    )

    assert '"static_status": "compatible"' in output.read_text(encoding="utf-8")


def _run(script: str, *arguments: str) -> None:
    _ = subprocess.run([sys.executable, script, *arguments], check=True)  # noqa: S603


def _inspection_json() -> str:
    return """{
      "schema_version": "item3-jar-inspection-v1",
      "generated_at": "2026-09-01T00:00:00Z",
      "candidate_count": 1,
      "all_inspections_passed": true,
      "candidates": [{
        "candidate_filename": "example.jar",
        "expected_sha256": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        "computed_sha256": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        "zip_integrity": "pass", "inspection_status": "pass", "archive_role": "mod",
        "entry_count": 1, "duplicate_entry_count": 0, "unsafe_entries": [],
        "metadata_documents": [{"path": "META-INF/neoforge.mods.toml", "size_bytes": 1,
          "sha256": "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"}],
        "manifest_implementation_version": null,
        "mod_loaders": ["javafml"], "loader_ranges": ["[4,)"],
        "mods": [{"mod_id": "example", "version": "1.0", "display_name": null,
          "source_path": "META-INF/neoforge.mods.toml"}],
        "dependencies": [], "minecraft_ranges": [], "neoforge_ranges": [],
        "fabric_environment": null, "embedded_libraries": [], "issues": []
      }]
    }"""
