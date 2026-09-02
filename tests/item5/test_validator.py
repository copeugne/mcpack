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


def test_pilot_environment_hashes_must_match_lifecycle(tmp_path: Path) -> None:
    """Accepted semantic identities are bound to the raw lifecycle receipt."""
    receipt = json.loads((ROOT / "evidence/item-5/pilots/accepted.json").read_bytes())
    receipt["environment"]["configuration_sha256"] = "0" * 64
    changed = tmp_path / "wrong-configuration.json"
    changed.write_text(json.dumps(receipt), encoding="utf-8")
    with pytest.raises(ValueError, match="configuration_sha256 does not match"):
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
