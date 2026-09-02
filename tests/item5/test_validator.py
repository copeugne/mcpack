# pyright: standard
"""Item 5 cross-artifact validator regression tests."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
from typing import TYPE_CHECKING, cast

import pytest

if TYPE_CHECKING:
    from collections.abc import Callable

    from mcpack_evidence.item5 import MeasurementProtocol

ROOT = Path(__file__).parents[2]


def load_validator() -> Callable[[Path, list[Path], Path], MeasurementProtocol]:
    """Load the executable validator helper."""
    path = ROOT / "tools/validate_item5.py"
    spec = importlib.util.spec_from_file_location("validate_item5", path)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return cast("Callable[[Path, list[Path], Path], MeasurementProtocol]", module.validate_pilots)


def test_pilot_protocol_hash_must_match_validated_protocol(tmp_path: Path) -> None:
    """A valid-looking but unrelated protocol digest rejects the receipt."""
    receipt = json.loads((ROOT / "evidence/item-5/pilots/accepted.json").read_bytes())
    receipt["environment"]["protocol_sha256"] = "0" * 64
    changed = tmp_path / "wrong-protocol.json"
    changed.write_text(json.dumps(receipt), encoding="utf-8")
    with pytest.raises(ValueError, match="pilot protocol hash mismatch"):
        load_validator()(ROOT / "measurement/item5/protocol-v1.json", [changed], ROOT)
