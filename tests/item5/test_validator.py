# pyright: standard
"""Item 5 cross-artifact validator regression tests."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
from typing import TYPE_CHECKING, cast

import pytest

from mcpack_evidence.item5 import PilotRun

if TYPE_CHECKING:
    from collections.abc import Callable
    from types import ModuleType

    from mcpack_evidence.item5 import MeasurementProtocol

ROOT = Path(__file__).parents[2]


def load_validator_module() -> ModuleType:
    """Load the executable validator module."""
    path = ROOT / "tools/validate_item5.py"
    spec = importlib.util.spec_from_file_location("validate_item5", path)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_validator() -> Callable[[Path, list[Path], Path], MeasurementProtocol]:
    """Return the cross-artifact validator helper."""
    return cast(
        "Callable[[Path, list[Path], Path], MeasurementProtocol]",
        load_validator_module().validate_pilots,
    )


def test_pilot_protocol_hash_must_match_validated_protocol(tmp_path: Path) -> None:
    """A valid-looking but unrelated protocol digest rejects the receipt."""
    receipt = json.loads((ROOT / "evidence/item-5/pilots/accepted.json").read_bytes())
    receipt["environment"]["protocol_sha256"] = "0" * 64
    changed = tmp_path / "wrong-protocol.json"
    changed.write_text(json.dumps(receipt), encoding="utf-8")
    with pytest.raises(ValueError, match="pilot protocol hash mismatch"):
        load_validator()(ROOT / "measurement/item5/protocol-v1.json", [changed], ROOT)


@pytest.mark.parametrize(
    ("field", "message"),
    [
        ("retained_manifest_sha256", "retained manifest hash mismatch"),
        ("host_evidence_sha256", "host evidence hash mismatch"),
        ("java_archive_sha256", "Java archive hash mismatch"),
    ],
)
def test_pilot_committed_environment_hashes_are_recomputed(
    tmp_path: Path, field: str, message: str
) -> None:
    """Receipts cannot substitute unrelated committed environment identities."""
    receipt = json.loads((ROOT / "evidence/item-5/pilots/accepted.json").read_bytes())
    receipt["environment"][field] = "0" * 64
    changed = tmp_path / f"wrong-{field}.json"
    changed.write_text(json.dumps(receipt), encoding="utf-8")
    with pytest.raises(ValueError, match=message):
        load_validator()(ROOT / "measurement/item5/protocol-v1.json", [changed], ROOT)


def test_pilot_artifact_paths_cannot_escape_repository(tmp_path: Path) -> None:
    """Even an existing absolute artifact cannot satisfy a receipt identity."""
    receipt = json.loads((ROOT / "evidence/item-5/pilots/accepted.json").read_bytes())
    receipt["raw_artifacts"][0]["path"] = str(
        ROOT / "evidence/item-5/pilots/raw/accepted/lifecycle.json"
    )
    changed = tmp_path / "absolute-artifact.json"
    changed.write_text(json.dumps(receipt), encoding="utf-8")
    with pytest.raises(ValueError, match="artifact path escapes repository"):
        load_validator()(ROOT / "measurement/item5/protocol-v1.json", [changed], ROOT)


def test_pilot_environment_hashes_must_match_lifecycle(tmp_path: Path) -> None:
    """Accepted semantic identities are bound to the raw lifecycle receipt."""
    receipt = json.loads((ROOT / "evidence/item-5/pilots/accepted.json").read_bytes())
    receipt["environment"]["configuration_sha256"] = "0" * 64
    changed = tmp_path / "wrong-configuration.json"
    changed.write_text(json.dumps(receipt), encoding="utf-8")
    with pytest.raises(ValueError, match="configuration_sha256 does not match"):
        load_validator()(ROOT / "measurement/item5/protocol-v1.json", [changed], ROOT)


@pytest.mark.parametrize(("field", "value"), [("seed", 999), ("player_case", "peak")])
def test_pilot_case_labels_must_match_raw_samples(
    tmp_path: Path, field: str, value: object
) -> None:
    """Receipts cannot relabel preserved measurements to another condition."""
    receipt = json.loads((ROOT / "evidence/item-5/pilots/accepted.json").read_bytes())
    receipt[field] = value
    changed = tmp_path / f"wrong-{field}.json"
    changed.write_text(json.dumps(receipt), encoding="utf-8")
    with pytest.raises(ValueError, match=r"seed|player case"):
        load_validator()(ROOT / "measurement/item5/protocol-v1.json", [changed], ROOT)


@pytest.mark.parametrize("field", ["minecraft_version", "neoforge_version", "java_version"])
def test_pilot_versions_must_match_runtime_log(tmp_path: Path, field: str) -> None:
    """Declared runtime versions are observations rather than free-form labels."""
    receipt = json.loads((ROOT / "evidence/item-5/pilots/accepted.json").read_bytes())
    receipt["environment"][field] = "invented"
    changed = tmp_path / f"wrong-{field}.json"
    changed.write_text(json.dumps(receipt), encoding="utf-8")
    with pytest.raises(ValueError, match=f"{field} does not match"):
        load_validator()(ROOT / "measurement/item5/protocol-v1.json", [changed], ROOT)


def test_accepted_pilot_requires_successful_lifecycle(tmp_path: Path) -> None:
    """Matching identities cannot turn a failed lifecycle into accepted evidence."""
    pilot = PilotRun.model_validate_json(
        (ROOT / "evidence/item-5/pilots/accepted.json").read_bytes()
    )
    lifecycle_relative = Path("evidence/item-5/pilots/raw/accepted/lifecycle.json")
    lifecycle_target = tmp_path / lifecycle_relative
    lifecycle_target.parent.mkdir(parents=True)
    lifecycle = json.loads((ROOT / lifecycle_relative).read_bytes())
    lifecycle["clean_stop"] = False
    lifecycle_target.write_text(json.dumps(lifecycle), encoding="utf-8")
    overlay_target = tmp_path / "measurement/item5/spark-overlay.json"
    overlay_target.parent.mkdir(parents=True)
    overlay_target.write_bytes((ROOT / "measurement/item5/spark-overlay.json").read_bytes())
    validator = cast(
        "Callable[[PilotRun, Path], None]", load_validator_module().validate_lifecycle_identities
    )
    with pytest.raises(ValueError, match="complete success"):
        validator(pilot, tmp_path)


def test_rejected_pilot_requires_machine_observable_failure(tmp_path: Path) -> None:
    """Changing an accepted receipt's status cannot prove rejection handling."""
    receipt = json.loads((ROOT / "evidence/item-5/pilots/accepted.json").read_bytes())
    receipt["status"] = "rejected"
    receipt["rejection_reasons"] = ["claimed failure"]
    receipt["processed_artifacts"] = []
    changed = tmp_path / "false-rejection.json"
    changed.write_text(json.dumps(receipt), encoding="utf-8")
    with pytest.raises(ValueError, match="no machine-observable lifecycle failure"):
        load_validator()(
            ROOT / "measurement/item5/protocol-v1.json",
            [ROOT / "evidence/item-5/pilots/accepted.json", changed],
            ROOT,
        )


def test_rejected_pilot_rejects_empty_lifecycle_document(tmp_path: Path) -> None:
    """Missing lifecycle fields are malformed evidence, not observable failures."""
    pilot = PilotRun.model_validate_json(
        (ROOT / "evidence/item-5/pilots/rejected.json").read_bytes()
    )
    relative = Path("evidence/item-5/pilots/raw/rejected/lifecycle.json")
    target = tmp_path / relative
    target.parent.mkdir(parents=True)
    target.write_text("{}\n", encoding="utf-8")
    validator = cast(
        "Callable[[PilotRun, Path], None]", load_validator_module().validate_rejected_lifecycle
    )
    with pytest.raises(ValueError, match="incomplete or malformed"):
        validator(pilot, tmp_path)


def test_runtime_sample_values_must_match_preserved_log(tmp_path: Path) -> None:
    """Rehashing invented CSV values cannot manufacture accepted observations."""
    pilot = PilotRun.model_validate_json(
        (ROOT / "evidence/item-5/pilots/accepted.json").read_bytes()
    )
    log_relative = Path("evidence/item-5/pilots/raw/accepted/debug.log.gz")
    log_target = tmp_path / log_relative
    log_target.parent.mkdir(parents=True)
    log_target.write_bytes((ROOT / log_relative).read_bytes())
    csv_relative = Path("evidence/item-5/pilots/raw/accepted/samples.csv")
    csv_target = tmp_path / csv_relative
    csv_target.write_text(
        (ROOT / csv_relative)
        .read_text(encoding="utf-8")
        .replace("tps,ordinary,solo,1,,20.0", "tps,ordinary,solo,1,,19.0"),
        encoding="utf-8",
    )
    seed_suite = tmp_path / "test-environment/seed-suite.json"
    seed_suite.parent.mkdir()
    seed_suite.write_bytes((ROOT / "test-environment/seed-suite.json").read_bytes())
    validator = cast(
        "Callable[[PilotRun, Path], None]", load_validator_module().validate_runtime_provenance
    )
    with pytest.raises(ValueError, match="does not match preserved runtime output"):
        validator(pilot, tmp_path)


def test_processed_summary_must_match_raw_samples(tmp_path: Path) -> None:
    """A stale or arbitrary processed artifact cannot satisfy the pilot gate."""
    pilot = PilotRun.model_validate_json(
        (ROOT / "evidence/item-5/pilots/accepted.json").read_bytes()
    )
    raw_relative = Path("evidence/item-5/pilots/raw/accepted/samples.csv")
    raw_target = tmp_path / raw_relative
    raw_target.parent.mkdir(parents=True)
    raw_target.write_bytes((ROOT / raw_relative).read_bytes())
    processed_relative = Path("evidence/item-5/pilots/processed/summary.json")
    processed_target = tmp_path / processed_relative
    processed_target.parent.mkdir(parents=True)
    processed_target.write_text('{"unrelated": true}\n', encoding="utf-8")
    validator = cast(
        "Callable[[PilotRun, Path], None]", load_validator_module().validate_processed_samples
    )
    with pytest.raises(ValueError, match="does not match"):
        validator(pilot, tmp_path)
