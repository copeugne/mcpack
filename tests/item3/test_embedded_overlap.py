from __future__ import annotations

from mcpack_evidence.item3_jar_models import JarInspectionReport
from mcpack_evidence.item3_overlap import build_overlap_report


def test_classifies_embedded_overlap_and_nested_mod_id_collisions() -> None:
    report = build_overlap_report(
        JarInspectionReport.model_validate(
            {
                "schema_version": "item3-jar-inspection-v1",
                "generated_at": "2026-09-01T00:00:00Z",
                "candidate_count": 3,
                "all_inspections_passed": True,
                "candidates": [
                    _candidate("one.jar", "1.0", "a" * 64),
                    _candidate("two.jar", "1.0", "b" * 64),
                    _candidate("three.jar", "2.0", "b" * 64),
                ],
            }
        )
    )

    assert report.embedded_occurrence_count == 3
    assert report.coordinate_groups[0].classifications == (
        "identical_bytes",
        "same_version_different_bytes",
        "multiple_versions",
    )
    assert report.mod_id_collisions[0].mod_id == "nested"
    assert len(report.mod_id_collisions[0].providers) == 3


def _candidate(filename: str, version: str, digest: str) -> dict[str, object]:
    return {
        "candidate_filename": filename,
        "expected_sha256": "c" * 64,
        "computed_sha256": "c" * 64,
        "zip_integrity": "pass",
        "inspection_status": "pass",
        "archive_role": "mod",
        "entry_count": 1,
        "duplicate_entry_count": 0,
        "unsafe_entries": [],
        "metadata_documents": [],
        "manifest_implementation_version": None,
        "mod_loaders": [],
        "loader_ranges": [],
        "mods": [],
        "dependencies": [],
        "minecraft_ranges": [],
        "neoforge_ranges": [],
        "fabric_environment": None,
        "embedded_libraries": [
            {
                "path": f"META-INF/jarjar/lib-{version}.jar",
                "size_bytes": 1,
                "sha256": digest,
                "identifier": "group:lib",
                "artifact_version": version,
                "version_range": "[1,)",
                "nested_zip_integrity": "pass",
                "nested_metadata_paths": ["META-INF/neoforge.mods.toml"],
                "nested_mod_ids": ["nested"],
                "nested_dependencies": [],
                "nested_issues": [],
            }
        ],
        "issues": [],
    }
