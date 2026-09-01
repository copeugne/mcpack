from __future__ import annotations

from typing import TYPE_CHECKING

from mcpack_evidence.item3_compatibility import evaluate_compatibility
from mcpack_evidence.item3_dependency import target_range_check
from mcpack_evidence.item3_jar_models import JarInspectionReport

if TYPE_CHECKING:
    from mcpack_evidence.item3_compatibility_models import (
        CandidateCompatibility,
        CompatibilityReport,
    )


def test_separates_inactive_fabric_metadata_and_substitutes_manifest_version() -> None:
    report = evaluate_compatibility(
        _inspection(
            _candidate(
                "provider.jar",
                mods=[
                    _mod("provider", "${file.jarVersion}"),
                    _mod("provider", "9", "fabric.mod.json"),
                ],
                implementation_version="2.4.0",
                documents=["META-INF/neoforge.mods.toml", "fabric.mod.json"],
            )
        ),
        _passing_oracle,
    )

    row = report.candidates[0]
    assert tuple(mod.version for mod in row.provided_mods) == ("2.4.0",)
    assert row.active_metadata_paths == ("META-INF/neoforge.mods.toml",)
    assert row.inactive_metadata_paths == ("fabric.mod.json",)
    assert "inactive_fabric_metadata_present" in row.hazard_flags


def test_applies_required_optional_incompatible_discouraged_and_side_semantics() -> None:
    report = evaluate_compatibility(
        _inspection(
            _candidate("helper.jar", mods=[_mod("helper", "2.0")]),
            _candidate(
                "consumer.jar",
                mods=[_mod("consumer", "1.0")],
                dependencies=[
                    _dependency("consumer", "helper", "required", "[2,)"),
                    _dependency("consumer", "absent", "optional", "[1,)"),
                    _dependency("consumer", "helper", "discouraged", "[2,)"),
                    _dependency("consumer", "helper", "incompatible", "[3,)"),
                    _dependency("consumer", "missing_client", "required", "[1,)", "CLIENT"),
                ],
            ),
        ),
        _simple_oracle,
    )

    statuses = tuple(check.status for check in _row(report, "consumer.jar").dependency_checks)
    assert statuses == (
        "pass",
        "optional_absent",
        "discouraged_present",
        "pass",
        "ignored_physical_side",
    )


def test_ignores_orphan_owner_but_quarantines_matching_incompatibility() -> None:
    report = evaluate_compatibility(
        _inspection(
            _candidate("helper.jar", mods=[_mod("helper", "2.0")]),
            _candidate(
                "broken.jar",
                mods=[_mod("broken", "1.0")],
                dependencies=[
                    _dependency("wrong.owner", "minecraft", "required", "[1.21,1.22)"),
                    _dependency("broken", "helper", "incompatible", "[2,)"),
                ],
            ),
        ),
        _simple_oracle,
    )

    row = _row(report, "broken.jar")
    assert tuple(check.status for check in row.dependency_checks) == (
        "orphan_owner_ignored",
        "incompatible_present",
    )
    assert row.static_status == "incompatible"
    assert row.disposition == "quarantined"


def test_uses_support_matrix_fallback_only_after_direct_failure() -> None:
    calls: list[tuple[str, str]] = []

    def oracle(version: str, declared_range: str) -> str:
        calls.append((version, declared_range))
        return "pass" if version == "1.21" else "fail"

    result = target_range_check("minecraft", "1.21.1", "[1.21]", oracle)

    assert calls == [("1.21.1", "[1.21]"), ("1.21", "[1.21]")]
    assert result.result == "pass"
    assert result.fallback_version == "1.21"


def _row(report: CompatibilityReport, filename: str) -> CandidateCompatibility:
    return next(row for row in report.candidates if row.candidate_filename == filename)


def _inspection(*candidates: dict[str, object]) -> JarInspectionReport:
    return JarInspectionReport.model_validate(
        {
            "schema_version": "item3-jar-inspection-v1",
            "generated_at": "2026-09-01T00:00:00Z",
            "candidate_count": len(candidates),
            "all_inspections_passed": True,
            "candidates": candidates,
        }
    )


def _candidate(
    filename: str,
    *,
    mods: list[dict[str, object]],
    dependencies: list[dict[str, object]] | None = None,
    documents: list[str] | None = None,
    implementation_version: str | None = None,
) -> dict[str, object]:
    metadata_paths = documents or ["META-INF/neoforge.mods.toml"]
    return {
        "candidate_filename": filename,
        "expected_sha256": "a" * 64,
        "computed_sha256": "a" * 64,
        "zip_integrity": "pass",
        "inspection_status": "pass",
        "archive_role": "mod",
        "entry_count": 1,
        "duplicate_entry_count": 0,
        "unsafe_entries": [],
        "metadata_documents": [
            {"path": path, "size_bytes": 1, "sha256": "b" * 64} for path in metadata_paths
        ],
        "manifest_implementation_version": implementation_version,
        "mod_loaders": ["javafml"],
        "loader_ranges": ["[4,)"],
        "loader_declarations": [
            {
                "mod_loader": "javafml",
                "version_range": "[4,)",
                "source_path": "META-INF/neoforge.mods.toml",
            }
        ],
        "mods": mods,
        "dependencies": dependencies or [],
        "minecraft_ranges": [],
        "neoforge_ranges": [],
        "fabric_environment": None,
        "embedded_libraries": [],
        "issues": [],
    }


def _mod(mod_id: str, version: str, path: str = "META-INF/neoforge.mods.toml") -> dict[str, object]:
    return {"mod_id": mod_id, "version": version, "display_name": None, "source_path": path}


def _dependency(
    owner: str,
    mod_id: str,
    kind: str,
    version_range: str,
    side: str = "BOTH",
) -> dict[str, object]:
    return {
        "owner_mod_id": owner,
        "mod_id": mod_id,
        "kind": kind,
        "mandatory": None,
        "version_ranges": [version_range],
        "side": side,
        "ordering": "NONE",
        "source_path": "META-INF/neoforge.mods.toml",
    }


def _passing_oracle(_version: str, _declared_range: str) -> str:
    return "pass"


def _simple_oracle(version: str, declared_range: str) -> str:
    if declared_range == "[3,)" and version == "2.0":
        return "fail"
    return "pass"


def test_ignores_legacy_forge_loader_range_when_neoforge_metadata_is_active() -> None:
    candidate = _candidate("dual.jar", mods=[_mod("dual", "1.0")])
    candidate["loader_ranges"] = ["[1,)", "[40,)"]
    candidate["loader_declarations"] = [
        {
            "mod_loader": "javafml",
            "version_range": "[1,)",
            "source_path": "META-INF/neoforge.mods.toml",
        },
        {
            "mod_loader": "lowcodefml",
            "version_range": "[40,)",
            "source_path": "META-INF/mods.toml",
        },
    ]

    report = evaluate_compatibility(_inspection(candidate), _simple_oracle)

    assert tuple(check.declared_range for check in report.candidates[0].loader_checks) == ("[1,)",)


def test_evaluates_active_nested_mod_dependencies() -> None:
    bundled = _candidate("bundle.jar", mods=[_mod("outer", "1.0")])
    bundled["embedded_libraries"] = [
        {
            "path": "META-INF/jarjar/nested.jar",
            "size_bytes": 1,
            "sha256": "d" * 64,
            "identifier": "example:nested",
            "artifact_version": "1.0",
            "version_range": "[1,)",
            "nested_zip_integrity": "pass",
            "nested_metadata_paths": ["META-INF/neoforge.mods.toml"],
            "nested_mod_ids": ["nested"],
            "nested_dependencies": [_dependency("nested", "helper", "required", "[2,)")],
            "nested_issues": [],
        }
    ]

    report = evaluate_compatibility(
        _inspection(_candidate("helper.jar", mods=[_mod("helper", "2.0")]), bundled),
        _simple_oracle,
    )

    row = _row(report, "bundle.jar")
    assert tuple(check.dependency_mod_id for check in row.dependency_checks) == ("helper",)
    assert row.dependency_checks[0].status == "pass"


def test_evaluates_dependencies_against_explicit_installed_provider_scope() -> None:
    report = evaluate_compatibility(
        _inspection(
            _candidate(
                "consumer.jar",
                mods=[_mod("consumer", "1.0")],
                dependencies=[
                    _dependency("consumer", "optional_helper", "optional", "[1,)"),
                    _dependency("consumer", "required_helper", "required", "[1,)"),
                    _dependency("consumer", "conflict", "incompatible", "[1,)"),
                ],
            ),
            _candidate("optional.jar", mods=[_mod("optional_helper", "1.0")]),
            _candidate("required.jar", mods=[_mod("required_helper", "1.0")]),
            _candidate("conflict.jar", mods=[_mod("conflict", "1.0")]),
        ),
        _simple_oracle,
        frozenset({"consumer.jar", "required.jar"}),
    )

    row = _row(report, "consumer.jar")
    assert tuple(check.status for check in row.dependency_checks) == (
        "optional_absent",
        "pass",
        "optional_absent",
    )
    assert row.dependency_checks[0].provider_candidates == ()
    assert row.dependency_checks[1].provider_candidates == ("required.jar",)
