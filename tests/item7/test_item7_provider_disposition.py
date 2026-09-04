from __future__ import annotations

from typing import Literal

import pytest

from mcpack_evidence.item7_provider_disposition import classify
from mcpack_evidence.item7_provider_disposition_gap_evidence import (
    GapEvidence,
    ProviderDispositionError,
)
from mcpack_evidence.item7_provider_disposition_models import DispositionStatus, SavedStart
from mcpack_evidence.item7_runtime import PreflightReceipt


def _preflight() -> PreflightReceipt:
    return PreflightReceipt.model_validate(
        {
            "schema_version": "item7-worldgen-preflight-v1",
            "seed_role": "ordinary",
            "seed": "42",
            "java_version": "Temurin-21.0.12.1+1-LTS",
            "retained_candidate_count": 136,
            "instrumented_candidate_count": 137,
            "retained_runtime_sha256": "0" * 64,
            "instrumented_runtime_sha256": "1" * 64,
            "retained_manifest_sha256": "2" * 64,
            "frozen_manifest_sha256": "3" * 64,
            "config_audit_sha256": "4" * 64,
            "seed_suite_sha256": "5" * 64,
            "chunky_sha256": "6" * 64,
        }
    )


def _gap(run: Literal["gap-a", "gap-b"], log: str) -> GapEvidence:
    starts = {
        "betterstrongholds:stronghold": SavedStart(
            run=run,
            structure_id="betterstrongholds:stronghold",
            chunk_x=1,
            chunk_z=2,
        )
    }
    return GapEvidence(starts=starts, inputs=(), preflight=_preflight(), log=log)


def test_targeted_component_requires_both_saved_starts() -> None:
    gap_a = _gap("gap-a", "")
    gap_b = _gap("gap-b", "")

    status, starts, _, action = classify("betterstrongholds", (), gap_a, gap_b, "")

    assert status is DispositionStatus.TARGETED_OBSERVED
    assert tuple(start.run for start in starts) == ("gap-a", "gap-b")
    assert action is None


def test_better_caves_requires_the_accepted_compatibility_errors_in_both_runs() -> None:
    caves = "Better Caves"
    aquifer_prefix = "Failed to fetch the AquiferContext. Liquid Regions for YUNG's"
    aquifer = f"{aquifer_prefix} {caves} may not generate properly."
    report_prefix = "This is a mod compatibility issue. Please report it to the"
    compatibility = f"{report_prefix} {caves} GitHub issue tracker!"
    complete = f"{aquifer}\n{compatibility}"
    gap_a = _gap("gap-a", complete)
    gap_b = _gap("gap-b", complete)

    status, _, _, action = classify("bettercaves", (), gap_a, gap_b, "")

    assert status is DispositionStatus.OBSERVED_GENERATION_FAILURE
    assert action is not None
    with pytest.raises(ProviderDispositionError, match="compatibility error"):
        _ = classify("bettercaves", (), gap_a, _gap("gap-b", ""), "")
