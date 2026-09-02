# pyright: standard
"""Spark lifecycle output-integrity regression tests."""

from __future__ import annotations

import importlib.util
from pathlib import Path
from typing import TYPE_CHECKING, cast

if TYPE_CHECKING:
    from collections.abc import Callable
    from types import ModuleType


ROOT = Path(__file__).parents[2]


def load_pilot_module() -> ModuleType:
    """Load the executable pilot harness for focused helper testing."""
    path = ROOT / "tools/run_item5_spark_pilot.py"
    spec = importlib.util.spec_from_file_location("run_item5_spark_pilot", path)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_only_new_nonempty_profiles_are_accepted(tmp_path: Path) -> None:
    """A stale or empty profile cannot satisfy the lifecycle contract."""
    module = load_pilot_module()
    find_new_profiles = cast(
        "Callable[[Path, dict[Path, tuple[int, int]]], list[Path]]", module.find_new_profiles
    )
    stale = tmp_path / "stale.sparkprofile"
    stale.write_bytes(b"old")
    empty = tmp_path / "empty.sparkprofile"
    empty.touch()
    prior = {stale.resolve(): (stale.stat().st_size, stale.stat().st_mtime_ns)}
    assert find_new_profiles(tmp_path, prior) == []

    created = tmp_path / "created.sparkprofile"
    created.write_bytes(b"new profile")
    assert find_new_profiles(tmp_path, prior) == [created]
