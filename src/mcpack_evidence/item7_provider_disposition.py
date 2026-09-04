"""Close Item 7 provider observations without creating Item 8 families."""

from __future__ import annotations

from typing import TYPE_CHECKING, Final

from mcpack_evidence.item7_coverage_models import CoverageReport, Observation
from mcpack_evidence.item7_provider_disposition_gap_evidence import (
    GapEvidence,
    ProviderDispositionError,
    binding,
    load_gap,
    parse,
    resolve,
)
from mcpack_evidence.item7_provider_disposition_models import (
    DispositionComponent,
    DispositionLabel,
    DispositionStatus,
    DispositionTotals,
    ProviderDispositionReport,
    SavedStart,
)
from mcpack_evidence.item7_provider_models import ProviderCatalog

if TYPE_CHECKING:
    from pathlib import Path

_INDIRECT_MARKERS: Final[dict[str, str]] = {
    "tectonic": "Found new data pack tectonic, loading it automatically",
    "terrablender": "Registered region minecraft:overworld to index 0 for type OVERWORLD",
    "lithostitched": "Refreshed Lithostitched biome cache",
    "yungsapi": "YUNG's API 1.21.1-NeoForge-5.1.6 (yungsapi)",
    "betterendisland": "YUNG's Better End Island 1.21.1-NeoForge-3.1.2 (betterendisland)",
    "integrated_api": "Integrated API 1.7.3+1.21.1-neoforge (integrated_api)",
    "moogs_structures": "Moog's Structure Lib 3.0.0 (moogs_structures)",
}
_LIMITED: Final = frozenset({"yungsbridges", "yungsextras"})


# Seven explicit paths keep the acceptance boundary visible to CLI callers.
def build_disposition(  # noqa: PLR0913
    repository: Path,
    raw_root: Path,
    *,
    catalog_relative: Path,
    coverage_relative: Path,
    runtime_log_relative: Path,
    gap_a_relative: Path,
    gap_b_relative: Path,
) -> ProviderDispositionReport:
    """Produce a complete evidence-bound final disposition for every catalog component."""
    catalog_path = resolve(repository, catalog_relative)
    coverage_path = resolve(raw_root, coverage_relative)
    runtime_log_path = resolve(raw_root, runtime_log_relative)
    catalog = parse(ProviderCatalog, catalog_path)
    coverage = parse(CoverageReport, coverage_path)
    catalog_binding = binding(catalog_path, f"repository/{catalog_relative}", 1)
    coverage_binding = binding(coverage_path, f"raw/{coverage_relative}", 1)
    if coverage.provider_catalog_sha256 != catalog_binding.sha256:
        detail = "coverage catalog identity differs"
        raise ProviderDispositionError(detail)
    if tuple(label.label for label in coverage.labels) != tuple(catalog.labels):
        detail = "coverage labels differ from catalog"
        raise ProviderDispositionError(detail)
    gap_a = load_gap(raw_root, gap_a_relative, "gap-a")
    gap_b = load_gap(raw_root, gap_b_relative, "gap-b")
    if gap_a.preflight != gap_b.preflight:
        detail = "gap preflight identities differ"
        raise ProviderDispositionError(detail)
    log_content = runtime_log_path.read_text(encoding="utf-8")
    log_binding = binding(
        runtime_log_path, f"raw/{runtime_log_relative}", len(log_content.splitlines())
    )
    coverage_rows = {
        (label.label, component.mod_id): component
        for label in coverage.labels
        for component in label.components
    }
    labels: list[DispositionLabel] = []
    for label_name, label in catalog.labels.items():
        components: list[DispositionComponent] = []
        for component in label.components:
            source = coverage_rows.get((label_name, component.mod_id))
            if source is None or source.sha256 != component.sha256:
                detail = f"coverage component identity differs: {component.mod_id}"
                raise ProviderDispositionError(detail)
            status, starts, limitation, action = classify(
                component.mod_id, source.observations, gap_a, gap_b, log_content
            )
            components.append(
                DispositionComponent(
                    candidate_filename=component.candidate_filename,
                    mod_id=component.mod_id,
                    role=component.role.value,
                    sha256=component.sha256,
                    disposition=status,
                    direct_observations=source.observations,
                    targeted_starts=starts,
                    limitation=limitation,
                    downstream_action=action,
                )
            )
        labels.append(DispositionLabel(label=label_name, components=tuple(components)))
    result = ProviderDispositionReport(
        schema_version="item7-provider-disposition-v1",
        catalog_path=catalog_binding.path,
        catalog_sha256=catalog_binding.sha256,
        coverage_path=coverage_binding.path,
        coverage_sha256=coverage_binding.sha256,
        inputs=(catalog_binding, coverage_binding, log_binding, *gap_a.inputs, *gap_b.inputs),
        labels=tuple(labels),
        totals=DispositionTotals(
            direct_observed=23,
            targeted_observed=4,
            observed_generation_failure=1,
            indirect_observed=7,
            not_observed_with_limit=2,
            total_components=37,
        ),
    )
    _validate_totals(result)
    return result


def classify(
    mod_id: str,
    observations: tuple[Observation, ...],
    gap_a: GapEvidence,
    gap_b: GapEvidence,
    runtime_log: str,
) -> tuple[DispositionStatus, tuple[SavedStart, ...], str, str | None]:
    """Map one catalog component to an evidence-honest final disposition."""
    if observations:
        return (
            DispositionStatus.DIRECT_OBSERVED,
            (),
            "Decoded Item 7 selections directly contain this catalog component output.",
            None,
        )
    if mod_id in _TARGETS_BY_MOD:
        target = _TARGETS_BY_MOD[mod_id]
        return (
            DispositionStatus.TARGETED_OBSERVED,
            (gap_a.starts[target], gap_b.starts[target]),
            (
                "Two accepted ordinary-seed targeted runs each saved exactly one start. "
                "This is not a frequency estimate."
            ),
            None,
        )
    if mod_id == "bettercaves":
        markers = (
            (
                "Failed to fetch the AquiferContext. Liquid Regions for YUNG's Better "
                "Caves may not generate properly."
            ),
            (
                "This is a mod compatibility issue. Please report it to the Better Caves "
                "GitHub issue tracker!"
            ),
        )
        if any(marker not in gap_a.log or marker not in gap_b.log for marker in markers):
            detail = "required Better Caves compatibility error is absent"
            raise ProviderDispositionError(detail)
        return (
            DispositionStatus.OBSERVED_GENERATION_FAILURE,
            (),
            (
                "Accepted gap logs report AquiferContext failure and say Liquid Regions may "
                "not generate properly. No successful Better Caves generation is claimed."
            ),
            "Resolve the compatibility failure before treating Better Caves output as usable.",
        )
    if mod_id in _INDIRECT_MARKERS:
        marker = _INDIRECT_MARKERS[mod_id]
        if marker not in runtime_log:
            detail = f"required runtime marker missing: {mod_id}"
            raise ProviderDispositionError(detail)
        return (
            DispositionStatus.INDIRECT_OBSERVED,
            (),
            (
                "Runtime evidence confirms a loaded or executed consumer path, but does not "
                "attribute a direct saved start or biome to this component."
            ),
            None,
        )
    if mod_id in _LIMITED:
        return (
            DispositionStatus.NOT_OBSERVED_WITH_LIMIT,
            (),
            (
                "No direct saved start was observed and the catalog supplies no canonical "
                "structure identifier."
            ),
            "Item 8 must resolve canonical registry identifiers before a targeted observation.",
        )
    detail = f"unclassified catalog component: {mod_id}"
    raise ProviderDispositionError(detail)


_TARGETS_BY_MOD: Final = {
    "betterdeserttemples": "betterdeserttemples:desert_temple",
    "betterstrongholds": "betterstrongholds:stronghold",
    "betterwitchhuts": "betterwitchhuts:witch_hut",
    "integrated_stronghold": "integrated_stronghold:stronghold",
}
_EXPECTED_LABELS: Final = 17
_EXPECTED_COMPONENTS: Final = 37
_EXPECTED_DISPOSITION_COUNTS: Final = (23, 4, 1, 7, 2)


def _validate_totals(report: ProviderDispositionReport) -> None:
    rows = tuple(component for label in report.labels for component in label.components)
    if (
        len(report.labels) != _EXPECTED_LABELS
        or len(rows) != _EXPECTED_COMPONENTS
        or len({row.candidate_filename for row in rows}) != _EXPECTED_COMPONENTS
    ):
        detail = "provider labels or component identities are incomplete"
        raise ProviderDispositionError(detail)
    counts = {
        status: sum(row.disposition is status for row in rows) for status in DispositionStatus
    }
    actual = tuple(counts[status] for status in DispositionStatus)
    if actual != _EXPECTED_DISPOSITION_COUNTS or sum(actual) != _EXPECTED_COMPONENTS:
        detail = "provider disposition totals differ"
        raise ProviderDispositionError(detail)
