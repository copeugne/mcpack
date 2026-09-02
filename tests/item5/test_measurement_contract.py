# pyright: standard
"""Item 5 strict contract and deterministic analyzer tests."""

from __future__ import annotations

import json
import math
from pathlib import Path

import pytest
from pydantic import ValidationError

from mcpack_evidence.item5 import MeasurementProtocol, PilotRun, analyze_samples

ROOT = Path(__file__).parents[2]


def test_committed_protocol_has_exact_required_coverage() -> None:
    """The committed protocol covers all metrics and player cases."""
    protocol = MeasurementProtocol.model_validate_json(
        (ROOT / "measurement/item5/protocol-v1.json").read_bytes()
    )
    assert len(protocol.metrics) == 24
    assert len(protocol.player_cases) == 5


def test_missing_methodology_field_is_rejected() -> None:
    """No prose-default can hide an omitted methodology field."""
    payload = json.loads((ROOT / "measurement/item5/protocol-v1.json").read_bytes())
    del payload["metrics"][0]["uncertainty_treatment"]
    with pytest.raises(ValidationError, match="uncertainty_treatment"):
        MeasurementProtocol.model_validate(payload)


def test_missing_metric_and_duplicate_player_case_are_rejected() -> None:
    """Coverage checks reject subtle omissions and duplicates."""
    payload = json.loads((ROOT / "measurement/item5/protocol-v1.json").read_bytes())
    payload["metrics"].pop()
    payload["player_cases"][-1]["case_id"] = "solo"
    with pytest.raises(ValidationError, match="protocol must cover"):
        MeasurementProtocol.model_validate(payload)


def test_analyzer_is_order_independent_and_deterministic() -> None:
    """Long-form aggregation has stable keys and statistics."""
    rows = [
        {"metric_id": "tps", "value": "19"},
        {"metric_id": "idle_mspt", "value": "8"},
        {"metric_id": "tps", "value": "20"},
    ]
    expected = {
        "idle_mspt": {
            "bootstrap_median_95ci": [8.0, 8.0],
            "bootstrap_resamples": 10_000,
            "count": 1,
            "iqr": 0.0,
            "max": 8.0,
            "mean": 8.0,
            "median": 8.0,
            "min": 8.0,
            "p95": 8.0,
            "p99": 8.0,
            "range": 0.0,
        },
        "tps": {
            "bootstrap_median_95ci": [19.0, 20.0],
            "bootstrap_resamples": 10_000,
            "count": 2,
            "iqr": 0.5,
            "max": 20.0,
            "mean": 19.5,
            "median": 19.5,
            "min": 19.0,
            "p95": 19.95,
            "p99": 19.99,
            "range": 1.0,
        },
    }
    assert analyze_samples(rows) == expected
    assert analyze_samples(reversed(rows)) == expected


@pytest.mark.parametrize(
    "rows",
    [[], [{"metric_id": "tps", "value": "NaN"}], [{"metric_id": "tps", "value": "Infinity"}]],
)
def test_analyzer_rejects_empty_and_nonfinite_samples(rows: list[dict[str, str]]) -> None:
    """Missing and non-finite samples cannot produce accepted JSON."""
    assert not rows or not math.isfinite(float(rows[0]["value"]))
    with pytest.raises(ValueError, match=r"no data|finite"):
        analyze_samples(rows)


def test_accepted_pilot_requires_processed_and_environment_evidence() -> None:
    """Accepted receipts cannot omit processing or input identities."""
    payload = json.loads((ROOT / "evidence/item-5/pilots/accepted.json").read_bytes())
    payload["processed_artifacts"] = []
    with pytest.raises(ValidationError, match="processed evidence"):
        PilotRun.model_validate(payload)
    payload = json.loads((ROOT / "evidence/item-5/pilots/accepted.json").read_bytes())
    payload["environment"]["world_snapshot_sha256"] = None
    with pytest.raises(ValidationError, match="configuration and world snapshot"):
        PilotRun.model_validate(payload)


def test_total_duration_includes_warm_up_and_sample_window() -> None:
    """Every metric duration covers its maximum declared warm-up and capture."""
    protocol = MeasurementProtocol.model_validate_json(
        (ROOT / "measurement/item5/protocol-v1.json").read_bytes()
    )
    assert all(
        metric.total_run_duration_seconds >= metric.warm_up_seconds + metric.sample_window_seconds
        for metric in protocol.metrics
    )


@pytest.mark.parametrize("name", ["accepted.json", "rejected.json"])
def test_committed_pilot_receipts_are_strict(name: str) -> None:
    """Both pilot paths conform to the immutable run receipt."""
    PilotRun.model_validate_json((ROOT / "evidence/item-5/pilots" / name).read_bytes())
