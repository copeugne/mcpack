"""Evaluate active NeoForge metadata using exact externally supplied range results."""

from __future__ import annotations

from collections import defaultdict
from typing import TYPE_CHECKING

from mcpack_evidence.item3_compatibility_models import (
    CandidateCompatibility,
    CompatibilityReport,
    DependencyCheck,
    ProvidedMod,
    RangeCheck,
)
from mcpack_evidence.item3_dependency import (
    RangeOracle,
    applies_to_server,
    evaluate_dependency,
    range_check,
    target_range_check,
)

if TYPE_CHECKING:
    from mcpack_evidence.item3_jar_models import (
        CandidateJarInspection,
        DependencyDeclaration,
        JarInspectionReport,
    )

_ACTIVE_PATH = "META-INF/neoforge.mods.toml"


def evaluate_compatibility(
    inspection: JarInspectionReport,
    oracle: RangeOracle,
) -> CompatibilityReport:
    """Evaluate every candidate without promoting static success to runtime approval."""
    provided = _provided_mods(inspection.candidates)
    providers: dict[str, list[ProvidedMod]] = defaultdict(list)
    for mod in provided:
        providers[mod.mod_id].append(mod)
    rows = tuple(
        _evaluate_candidate(candidate, providers, oracle) for candidate in inspection.candidates
    )
    return CompatibilityReport(
        schema_version="item3-static-compatibility-v1",
        target_minecraft="1.21.1",
        target_neoforge="21.1.249",
        physical_side="dedicated_server",
        candidate_count=len(rows),
        candidates=rows,
    )


def _provided_mods(candidates: tuple[CandidateJarInspection, ...]) -> tuple[ProvidedMod, ...]:
    rows: list[ProvidedMod] = []
    for candidate in candidates:
        rows.extend(
            ProvidedMod(
                mod_id=mod.mod_id,
                version=_resolve_version(mod.version, candidate),
                provider_candidate=candidate.candidate_filename,
                origin="outer",
                source_path=mod.source_path,
            )
            for mod in candidate.mods
            if mod.source_path == _ACTIVE_PATH
        )
        rows.extend(
            ProvidedMod(
                mod_id=mod_id,
                version=library.artifact_version or "unknown",
                provider_candidate=candidate.candidate_filename,
                origin="nested",
                source_path=library.path,
            )
            for library in candidate.embedded_libraries
            if _ACTIVE_PATH in library.nested_metadata_paths
            for mod_id in library.nested_mod_ids
        )
    return tuple(rows)


def _evaluate_candidate(
    candidate: CandidateJarInspection,
    providers: dict[str, list[ProvidedMod]],
    oracle: RangeOracle,
) -> CandidateCompatibility:
    active_paths = tuple(
        doc.path for doc in candidate.metadata_documents if doc.path == _ACTIVE_PATH
    )
    inactive_paths = tuple(
        doc.path for doc in candidate.metadata_documents if doc.path == "fabric.mod.json"
    )
    own_mods = tuple(
        mod
        for rows in providers.values()
        for mod in rows
        if mod.provider_candidate == candidate.candidate_filename
    )
    loader_checks = tuple(
        range_check("language_loader", "4.0", version_range, oracle)
        for version_range in candidate.loader_ranges
        if candidate.archive_role != "library"
    )
    dependencies = tuple(dep for dep in candidate.dependencies if dep.source_path == _ACTIVE_PATH)
    minecraft = _target_checks(dependencies, "minecraft", "1.21.1", oracle)
    neoforge = _target_checks(dependencies, "neoforge", "21.1.249", oracle)
    dependency_checks = tuple(
        evaluate_dependency(dep, own_mods, providers, oracle) for dep in dependencies
    )
    hazards = _hazards(candidate, own_mods, providers, dependency_checks)
    results = tuple(check.result for check in (*loader_checks, *minecraft, *neoforge))
    dependency_statuses = tuple(check.status for check in dependency_checks)
    incompatible = any(result in {"fail", "invalid"} for result in results) or any(
        status in {"missing_required", "version_mismatch", "incompatible_present", "orphan_owner"}
        for status in dependency_statuses
    )
    unresolved = (
        (not active_paths and candidate.archive_role != "library")
        or "missing_oracle_result" in results
        or "unresolved" in dependency_statuses
    )
    static_status = "incompatible" if incompatible else "unresolved" if unresolved else "compatible"
    disposition = (
        "quarantined" if incompatible else "unresolved" if unresolved else "runtime_test_candidate"
    )
    return CandidateCompatibility(
        candidate_filename=candidate.candidate_filename,
        artifact_sha256=candidate.computed_sha256,
        archive_role=candidate.archive_role,
        active_metadata_paths=active_paths,
        inactive_metadata_paths=inactive_paths,
        provided_mods=own_mods,
        loader_checks=loader_checks,
        minecraft_checks=minecraft,
        neoforge_checks=neoforge,
        dependency_checks=dependency_checks,
        hazard_flags=hazards,
        static_status=static_status,
        disposition=disposition,
        confidence="low" if unresolved else "medium",
        missing_runtime_evidence=("focused_dedicated_server_boot",),
    )


def _target_checks(
    dependencies: tuple[DependencyDeclaration, ...],
    mod_id: str,
    version: str,
    oracle: RangeOracle,
) -> tuple[RangeCheck, ...]:
    return tuple(
        target_range_check(mod_id, version, version_range, oracle)
        for dep in dependencies
        if dep.mod_id == mod_id and applies_to_server(dep.side)
        for version_range in dep.version_ranges
    )


def _resolve_version(version: str, candidate: CandidateJarInspection) -> str:
    if version == "${file.jarVersion}":
        return candidate.manifest_implementation_version or "unknown"
    return version


def _hazards(
    candidate: CandidateJarInspection,
    own_mods: tuple[ProvidedMod, ...],
    providers: dict[str, list[ProvidedMod]],
    dependency_checks: tuple[DependencyCheck, ...],
) -> tuple[str, ...]:
    hazards: list[str] = []
    if any(doc.path == "META-INF/mods.toml" for doc in candidate.metadata_documents):
        hazards.append("legacy_forge_metadata_also_present")
    if any(doc.path == "fabric.mod.json" for doc in candidate.metadata_documents):
        hazards.append("inactive_fabric_metadata_present")
    if any(check.status == "orphan_owner" for check in dependency_checks):
        hazards.append("orphan_dependency_owner")
    hazards.extend(
        f"provided_mod_id_collision:{mod.mod_id}"
        for mod in own_mods
        if len(providers[mod.mod_id]) > 1
    )
    return tuple(dict.fromkeys(hazards))
