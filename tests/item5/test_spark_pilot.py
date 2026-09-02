# pyright: standard
"""Spark lifecycle output-integrity regression tests."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
from typing import TYPE_CHECKING, cast

import pytest

if TYPE_CHECKING:
    from collections.abc import Callable
    from types import ModuleType
    from typing import Protocol

    class Writable(Protocol):
        """Minimal text pipe used by the command writer."""

        def write(self, value: str) -> int: ...
        def flush(self) -> None: ...


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


def test_unrelated_save_cannot_confirm_requested_flush() -> None:
    """A save before Spark completion cannot advance lifecycle shutdown."""
    module = load_pilot_module()
    confirms_profile_save = cast("Callable[..., bool]", module.confirms_profile_save)
    confirms_requested_flush = cast("Callable[..., bool]", module.confirms_requested_flush)
    assert not confirms_profile_save("Saved the game", stop_requested=True)
    assert not confirms_requested_flush("Saved the game", flush_requested=False)
    assert confirms_profile_save("Profiler stopped & save complete!", stop_requested=True)
    assert confirms_requested_flush("Saved the game", flush_requested=True)


def test_broken_console_pipe_is_reported_without_raising() -> None:
    """A closed JVM stdin remains representable in a lifecycle receipt."""
    module = load_pilot_module()
    send_console_command = cast("Callable[[Writable, str], bool]", module.send_console_command)

    class ClosedPipe:
        def write(self, value: str) -> int:
            del value
            raise BrokenPipeError

        def flush(self) -> None:
            raise AssertionError

    assert not send_console_command(ClosedPipe(), "stop")


def test_spark_overlay_binds_the_runtime_artifact(tmp_path: Path) -> None:
    """The pilot refuses instrumentation that differs from the audited overlay."""
    module = load_pilot_module()
    validate_spark_overlay = cast(
        "Callable[[Path, Path], tuple[str, str]]", module.validate_spark_overlay
    )
    artifact = tmp_path / "mods/spark.jar"
    artifact.parent.mkdir()
    artifact.write_bytes(b"audited spark")
    artifact_sha256 = hashlib.sha256(artifact.read_bytes()).hexdigest()
    overlay = tmp_path / "overlay.json"
    overlay.write_text(
        json.dumps({"overlay": {"filename": "spark.jar", "sha256": artifact_sha256}}),
        encoding="utf-8",
    )
    _, observed_artifact_sha256 = validate_spark_overlay(tmp_path, overlay)
    assert observed_artifact_sha256 == artifact_sha256
    artifact.write_bytes(b"replaced")
    with pytest.raises(ValueError, match="Spark artifact hash mismatch"):
        validate_spark_overlay(tmp_path, overlay)


def test_overlay_preflight_failure_has_rejection_receipt() -> None:
    """An invalid profiler identity remains machine-readable evidence."""
    module = load_pilot_module()
    preflight_failure_receipt = cast(
        "Callable[[Exception], dict[str, object]]", module.preflight_failure_receipt
    )
    receipt = preflight_failure_receipt(ValueError("wrong digest"))
    assert receipt["clean_stop"] is False
    assert receipt["commands"] == []
    assert receipt["rejection_reason"] == "Spark overlay preflight failed: wrong digest"
