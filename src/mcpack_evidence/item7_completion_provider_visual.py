"""Provider and visual acceptance checks for Item 7 completion."""

from __future__ import annotations

import csv
from pathlib import Path  # noqa: TC003
from typing import Final

from mcpack_evidence.item7_completion_io import (
    CompletionError,
    fail,
    portable_path,
    sha256_file,
    strict_model,
)
from mcpack_evidence.item7_completion_models import (
    ProviderDisposition,
    ProviderSummary,
    VisualReview,
    VisualSummary,
)
from mcpack_evidence.item7_completion_provider_checks import (
    validate_provider_evidence_shape,
    validate_provider_inputs,
)
from mcpack_evidence.item7_coverage_models import CoverageReport
from mcpack_evidence.item7_provider_models import ProviderCatalog

_FINAL_PROVIDER_TOTALS: Final = (23, 4, 1, 7, 2)
_FINAL_PROVIDER_COUNT: Final = 37
_FINAL_CAPTURE_COUNT: Final = 128
_REVIEW_COUNT: Final = 2
_CAPTURE_ROW_FIELDS: Final = 4
_PROVIDER_LABELS: Final = 17
_PNG_HEADER_BYTES: Final = 24


def validate_provider_disposition(
    catalog_path: Path,
    disposition_path: Path,
    coverage_path: Path | None = None,
    *,
    expected_count: int = 37,
    raw_root: Path | None = None,
) -> ProviderSummary:
    """Bind final component dispositions exactly once to the retained catalog."""
    catalog = strict_model(catalog_path, ProviderCatalog)
    report = strict_model(disposition_path, ProviderDisposition)
    _ = portable_path(report.catalog_path)
    _ = portable_path(report.coverage_path)
    if report.catalog_sha256 != sha256_file(catalog_path):
        fail("provider catalog identity", disposition_path)
    if coverage_path is not None:
        coverage = strict_model(coverage_path, CoverageReport)
        coverage_count = sum(len(label.components) for label in coverage.labels)
        if (
            report.coverage_sha256 != sha256_file(coverage_path)
            or coverage.provider_catalog_sha256 != report.catalog_sha256
            or len(coverage.labels) != _PROVIDER_LABELS
            or coverage_count != expected_count
        ):
            fail("provider coverage identity or accounting", disposition_path)
    expected = {
        component.candidate_filename: (label, component.mod_id, component.role, component.sha256)
        for label, group in catalog.labels.items()
        for component in group.components
    }
    observed = {
        component.candidate_filename: (
            label.label,
            component.mod_id,
            component.role,
            component.sha256,
        )
        for label in report.labels
        for component in label.components
    }
    observed_count = sum(len(label.components) for label in report.labels)
    label_names = tuple(label.label for label in report.labels)
    if (
        expected != observed
        or observed_count != expected_count
        or len(observed) != observed_count
        or len(label_names) != len(set(label_names))
        or (expected_count == _FINAL_PROVIDER_COUNT and len(label_names) != _PROVIDER_LABELS)
    ):
        fail("provider component accounting", disposition_path)
    totals = report.totals
    values = (
        totals.direct_observed,
        totals.targeted_observed,
        totals.observed_generation_failure,
        totals.indirect_observed,
        totals.not_observed_with_limit,
    )
    if totals.total_components != expected_count or sum(values) != expected_count:
        fail("provider disposition totals", disposition_path)
    actual_counts = tuple(
        sum(
            component.disposition == status
            for label in report.labels
            for component in label.components
        )
        for status in (
            "direct_observed",
            "targeted_observed",
            "observed_generation_failure",
            "indirect_observed",
            "not_observed_with_limit",
        )
    )
    if actual_counts != values:
        fail("provider disposition row totals", disposition_path)
    validate_provider_evidence_shape(report, disposition_path, expected_count)
    if expected_count == _FINAL_PROVIDER_COUNT and values != _FINAL_PROVIDER_TOTALS:
        fail("provider final disposition totals", disposition_path)
    if raw_root is not None:
        if coverage_path is None:
            fail("provider coverage path is required", disposition_path)
        validate_provider_inputs(report, catalog_path, coverage_path, raw_root, disposition_path)
    return ProviderSummary(total_components=expected_count, disposition_counts=totals)


def validate_visual_evidence(
    manifest_path: Path,
    review_paths: tuple[Path, ...],
    *,
    expected_count: int = 128,
) -> VisualSummary:
    """Verify every capture byte and two independent exact-provenance reviews."""
    rows = _capture_rows(manifest_path)
    if len(rows) != expected_count or len({row[0] for row in rows}) != expected_count:
        fail("visual capture accounting", manifest_path)
    for relative, _source, expected_sha, expected_size in rows:
        capture = manifest_path.parent / portable_path(relative)
        if (
            capture.stat().st_size != expected_size
            or sha256_file(capture) != expected_sha
            or _png_dimensions(capture) != (1440, 1200)
        ):
            fail("capture identity", relative)
    reviews = tuple(strict_model(path, VisualReview) for path in review_paths)
    if len(reviews) != _REVIEW_COUNT or {review.lane for review in reviews} != {
        "capture-and-source-integrity",
        "visual-fidelity",
    }:
        fail("visual review accounting", len(reviews))
    manifest_sha = sha256_file(manifest_path)
    provenance = {
        (
            review.capture_manifest.sha256,
            review.capture_manifest.size_bytes,
            review.capture_manifest.capture_count,
            review.renderer_commit,
            review.capture_tool_commit,
        )
        for review in reviews
    }
    expected = {(manifest_sha, manifest_path.stat().st_size, expected_count, "b" * 40, "c" * 40)}
    if expected_count == _FINAL_CAPTURE_COUNT:
        expected = {
            (
                manifest_sha,
                manifest_path.stat().st_size,
                expected_count,
                "6a3a997517974b0b6ca01906638b02228c320110",
                "81b39a6e5eb4c2ed5d2a57525e385b8c83aad34a",
            )
        }
    if provenance != expected:
        fail("visual review provenance", manifest_path)
    review = reviews[0]
    return VisualSummary(
        capture_count=expected_count,
        review_count=2,
        renderer_commit=review.renderer_commit,
        capture_tool_commit=review.capture_tool_commit,
    )


def _capture_rows(path: Path) -> tuple[tuple[str, str, str, int], ...]:
    try:
        with path.open(encoding="utf-8", newline="") as stream:
            raw = tuple(csv.reader(stream, delimiter="\t"))
        if raw and tuple(raw[0]) == ("path", "url", "sha256", "size_bytes"):
            raw = raw[1:]
        if any(len(row) != _CAPTURE_ROW_FIELDS for row in raw):
            fail("invalid capture manifest row", path)
        return tuple((row[0], row[1], row[2], int(row[3])) for row in raw)
    except (OSError, UnicodeError, ValueError, IndexError) as error:
        issue = "invalid capture manifest"
        raise CompletionError(issue, str(path)) from error


def _png_dimensions(path: Path) -> tuple[int, int]:
    try:
        header = path.read_bytes()[:_PNG_HEADER_BYTES]
    except OSError as error:
        issue = "cannot read capture"
        raise CompletionError(issue, str(path)) from error
    if len(header) != _PNG_HEADER_BYTES or header[:16] != b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR":
        fail("capture is not PNG", path)
    return int.from_bytes(header[16:20], "big"), int.from_bytes(header[20:24], "big")
