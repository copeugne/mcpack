# pyright: standard
"""Item 5 strict contract and deterministic analyzer tests."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import cast

import pytest
from pydantic import ValidationError

from mcpack_evidence.item5 import SAMPLE_UNITS, MeasurementProtocol, PilotRun, analyze_samples

ROOT = Path(__file__).parents[2]


def sample(metric_id: str, value: str, **extra: str) -> dict[str, str]:
    """Build one dimension-complete sample row."""
    return {
        "metric_id": metric_id,
        "seed_case": "ordinary",
        "player_case": "solo",
        "repetition": "1",
        "value": value,
        "unit": min(SAMPLE_UNITS.get(metric_id, {"unknown"})),
        **extra,
    }


def test_committed_protocol_has_exact_required_coverage() -> None:
    """The committed protocol covers all metrics and player cases."""
    protocol = MeasurementProtocol.model_validate_json(
        (ROOT / "measurement/item5/protocol-v1.json").read_bytes()
    )
    assert len(protocol.metrics) == 24
    assert len(protocol.player_cases) == 6
    assert protocol.player_cases[0].case_id == "zero"


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
    payload["player_cases"][-1] = dict(payload["player_cases"][1])
    with pytest.raises(ValidationError, match="protocol must cover"):
        MeasurementProtocol.model_validate(payload)


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("seed_cases", ["ordinary"], "every required seed case"),
        ("player_cases", ["solo"], "every required player case"),
        ("required_environment_hashes", [], "every environment hash"),
    ],
)
def test_each_metric_requires_complete_cases_and_hashes(
    field: str, value: list[str], message: str
) -> None:
    """A metric cannot narrow the protocol-wide environment coverage."""
    payload = json.loads((ROOT / "measurement/item5/protocol-v1.json").read_bytes())
    payload["metrics"][0][field] = value
    with pytest.raises(ValidationError, match=message):
        MeasurementProtocol.model_validate(payload)


def test_player_case_labels_have_fixed_counts() -> None:
    """Named load cases cannot silently change their player counts."""
    payload = json.loads((ROOT / "measurement/item5/protocol-v1.json").read_bytes())
    payload["player_cases"][-1]["players"] = 1
    with pytest.raises(ValidationError, match="peak must contain 10 players"):
        MeasurementProtocol.model_validate(payload)


def test_idle_metric_includes_zero_player_case() -> None:
    """The empty-server baseline has a distinct representable dimension."""
    protocol = MeasurementProtocol.model_validate_json(
        (ROOT / "measurement/item5/protocol-v1.json").read_bytes()
    )
    idle = next(metric for metric in protocol.metrics if metric.metric_id == "idle_mspt")
    assert idle.player_cases[0] == "zero"


def test_analyzer_is_order_independent_and_deterministic() -> None:
    """Long-form aggregation has stable keys and statistics."""
    rows = [
        sample("tps", "19"),
        sample("idle_mspt", "8"),
        sample("tps", "20"),
    ]
    expected = {
        "groups": [
            {
                "metric_id": "idle_mspt",
                "seed_case": "ordinary",
                "player_case": "solo",
                "repetition": 1,
                "unit": "milliseconds per tick",
                "statistics": {
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
            },
            {
                "metric_id": "tps",
                "seed_case": "ordinary",
                "player_case": "solo",
                "repetition": 1,
                "unit": "ticks per second",
                "statistics": {
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
            },
        ]
    }
    assert analyze_samples(rows) == expected
    assert analyze_samples(reversed(rows)) == expected


@pytest.mark.parametrize(
    "rows",
    [[], [sample("tps", "NaN")], [sample("tps", "Infinity")]],
)
def test_analyzer_rejects_empty_and_nonfinite_samples(rows: list[dict[str, str]]) -> None:
    """Missing and non-finite samples cannot produce accepted JSON."""
    assert not rows or not math.isfinite(float(rows[0]["value"]))
    with pytest.raises(ValueError, match=r"no data|finite"):
        analyze_samples(rows)


def test_ratio_metrics_retain_numerators_and_denominators() -> None:
    """Processed rate evidence keeps its auditable exposure inputs."""
    result = analyze_samples(
        [
            sample("structures_per_1000_chunks", "2.0", numerator="8", denominator="4000"),
            sample("structures_per_1000_chunks", "3.0", numerator="12", denominator="4000"),
        ]
    )
    groups = result["groups"]
    assert isinstance(groups, list)
    summary = groups[0]["statistics"]
    assert isinstance(summary, dict)
    assert summary["numerators"] == [8.0, 12.0]
    assert summary["denominators"] == [4000.0, 4000.0]
    assert summary["numerator_sum"] == 20.0
    assert summary["denominator_sum"] == 8000.0


def test_ratio_metric_requires_exposure_inputs() -> None:
    """A precomputed rate without its exposure base is invalid."""
    with pytest.raises(ValueError, match="requires numerator and denominator"):
        analyze_samples([sample("death_rate", "0.5", component="per_player_hour")])


def test_ratio_metric_rejects_value_inconsistent_with_operands() -> None:
    """A plausible-looking derived value cannot contradict its exposure inputs."""
    row = sample("structures_per_1000_chunks", "999", numerator="1", denominator="1000")
    with pytest.raises(ValueError, match="does not match its operands"):
        analyze_samples([row])


def test_analyzer_separates_experimental_dimensions() -> None:
    """Seeds, player cases, and repetitions never share a distribution."""
    rows = [
        sample("tps", "20"),
        {**sample("tps", "19"), "seed_case": "mountainous"},
        {**sample("tps", "18"), "player_case": "two"},
        {**sample("tps", "17"), "repetition": "2"},
    ]
    result = analyze_samples(rows)
    groups = result["groups"]
    assert isinstance(groups, list)
    assert len(groups) == 4


def test_analyzer_rejects_unknown_metric_id() -> None:
    """Misspelled and invented metric identifiers cannot be summarized."""
    with pytest.raises(ValueError, match="unknown metric_id"):
        analyze_samples([sample("tpz", "20")])


def test_loot_value_components_are_never_pooled() -> None:
    """Incomparable loot-vector axes retain separate statistics."""
    rows = [
        {**sample("loot_value", "2"), "component": "utility"},
        {**sample("loot_value", "200"), "component": "replacement_cost"},
    ]
    groups = analyze_samples(rows)["groups"]
    assert isinstance(groups, list)
    assert [group["component"] for group in groups] == ["replacement_cost", "utility"]


@pytest.mark.parametrize("metric_id", ["memory", "garbage_collection", "entity_count"])
def test_multi_axis_metrics_require_components(metric_id: str) -> None:
    """Measurements with incomparable quantities cannot be pooled into one group."""
    with pytest.raises(ValueError, match="require a nonempty component"):
        analyze_samples([sample(metric_id, "1")])


@pytest.mark.parametrize(
    "row",
    [
        sample(
            "death_rate",
            "-1",
            numerator="-1",
            denominator="1",
            component="per_player_hour",
        ),
        sample("adventure_activity_ratio", "2", numerator="2", denominator="1"),
    ],
)
def test_ratio_metrics_reject_impossible_operands(row: dict[str, str]) -> None:
    """Counts cannot be negative and proportions cannot exceed their exposure."""
    with pytest.raises(ValueError, match=r"nonnegative finite|bounded proportion operands"):
        analyze_samples([row])


def test_death_rate_can_exceed_one_per_exposure() -> None:
    """Rates are not incorrectly constrained as probabilities."""
    row = sample("death_rate", "2", numerator="2", denominator="1", component="per_player_hour")
    groups = cast("list[dict[str, object]]", analyze_samples([row])["groups"])
    statistics = cast("dict[str, object]", groups[0]["statistics"])
    assert statistics["mean"] == 2.0


def test_pathfinding_components_are_never_pooled() -> None:
    """Pathfinding time and CPU attribution remain distinct quantities."""
    rows = [
        sample("pathfinding_cost", "5", component="wall_time", unit="milliseconds"),
        sample("pathfinding_cost", "25", component="cpu_share", unit="percent CPU"),
    ]
    groups = cast("list[dict[str, object]]", analyze_samples(rows)["groups"])
    assert len(groups) == 2


@pytest.mark.parametrize(
    "row",
    [
        {key: value for key, value in sample("travel_time", "2").items() if key != "unit"},
        sample("travel_time", "2", unit="minutes"),
    ],
)
def test_samples_require_protocol_units(row: dict[str, str]) -> None:
    """Missing or incompatible units cannot enter canonical summaries."""
    with pytest.raises(ValueError, match=r"require metric_id|invalid unit"):
        analyze_samples([row])


def test_negative_physical_measurements_are_rejected() -> None:
    """Finite but impossible negative observations cannot be summarized."""
    with pytest.raises(ValueError, match="nonnegative finite"):
        analyze_samples([sample("tps", "-1")])


def test_ratio_operand_output_is_order_independent() -> None:
    """Canonical summaries do not depend on equivalent input row order."""
    rows = [
        sample("death_rate", "0.5", numerator="1", denominator="2", component="per_player_hour"),
        sample("death_rate", "0.5", numerator="2", denominator="4", component="per_player_hour"),
    ]
    assert analyze_samples(rows) == analyze_samples(reversed(rows))


def test_combat_contract_names_executable_fixture() -> None:
    """Combat workload commands and cadence live in a versioned fixture."""
    fixture = json.loads((ROOT / "measurement/item5/combat-fixture-v1.json").read_bytes())
    assert fixture["wave"]["count"] == 20
    assert len(fixture["wave"]["commands"]) == 3
    protocol = json.loads((ROOT / "measurement/item5/protocol-v1.json").read_bytes())
    combat = next(row for row in protocol["metrics"] if row["metric_id"] == "active_combat_mspt")
    assert any("combat-fixture-v1.json" in step for step in combat["collection_procedure"])


def test_accepted_pilot_requires_processed_and_environment_evidence() -> None:
    """Accepted receipts cannot omit processing or input identities."""
    payload = json.loads((ROOT / "evidence/item-5/pilots/accepted.json").read_bytes())
    payload["processed_artifacts"] = []
    with pytest.raises(ValidationError, match="processed evidence"):
        PilotRun.model_validate(payload)
    payload = json.loads((ROOT / "evidence/item-5/pilots/accepted.json").read_bytes())
    payload["environment"]["world_snapshot_sha256"] = None
    with pytest.raises(ValidationError, match="every environment and Spark hash"):
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
