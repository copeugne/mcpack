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


@pytest.mark.parametrize(("profile_count", "expected"), [(0, False), (1, True), (2, False)])
def test_clean_stop_requires_exactly_one_profile(profile_count: int, expected: bool) -> None:
    """A lifecycle cannot report success with missing or ambiguous profiler output."""
    clean_stop_succeeded = cast("Callable[..., bool]", load_pilot_module().clean_stop_succeeded)
    assert (
        clean_stop_succeeded(
            return_code=0,
            ready=True,
            profile_saved=True,
            flushed=True,
            profile_count=profile_count,
            console_pipe_failed=False,
        )
        is expected
    )


def test_clean_stop_requires_all_probe_confirmations() -> None:
    """Successful profiling cannot conceal a failed mandatory Spark probe."""
    assert not load_pilot_module().clean_stop_succeeded(
        return_code=0,
        ready=True,
        profile_saved=True,
        flushed=True,
        profile_count=1,
        console_pipe_failed=False,
        probes_confirmed=False,
    )


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


def test_launch_failure_has_rejection_receipt() -> None:
    """A missing run script remains a machine-readable failed lifecycle."""
    receipt = load_pilot_module().launch_failure_receipt(FileNotFoundError("run.sh"))
    assert receipt["clean_stop"] is False
    assert receipt["rejection_reason"] == "Server launch failed: run.sh"


def test_missing_requested_java_is_a_preflight_failure(tmp_path: Path) -> None:
    """The harness cannot silently fall through to a system Java executable."""
    with pytest.raises(ValueError, match="requested Java runtime is unavailable"):
        load_pilot_module().validate_java_runtime(tmp_path / "missing-java-home")


def test_validated_java_path_is_absolute(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Changing the server cwd cannot invalidate the selected Java PATH entry."""
    java = tmp_path / "relative-home/bin/java"
    java.parent.mkdir(parents=True)
    java.write_text("#!/bin/sh\necho 'openjdk version \"21.0.12.1\" Temurin' >&2\n")
    java.chmod(0o755)
    monkeypatch.chdir(tmp_path)
    executable, _ = load_pilot_module().validate_java_runtime(Path("relative-home"))
    assert executable.is_absolute()
    assert executable == java.resolve()


def test_runtime_io_failure_has_cleanup_receipt() -> None:
    """Post-launch I/O is distinguished from failure to create the JVM."""
    receipt = load_pilot_module().runtime_failure_receipt(OSError("disk full"))
    assert receipt["clean_stop"] is False
    assert receipt["rejection_reason"] == (
        "Pilot runtime I/O failed after server cleanup: disk full"
    )


def test_runtime_mod_preflight_rejects_extra_jar(tmp_path: Path) -> None:
    """Profiling cannot proceed with an added gameplay artifact."""
    module = load_pilot_module()
    mods = tmp_path / "mods"
    mods.mkdir()
    (mods / "game.jar").write_bytes(b"game")
    (mods / "spark.jar").write_bytes(b"spark")
    (mods / "extra.jar").write_bytes(b"extra")

    def digest(value: bytes) -> str:
        return hashlib.sha256(value).hexdigest()

    retained = tmp_path / "retained.txt"
    retained.write_text("game.jar\n", encoding="utf-8")
    acquisition = tmp_path / "acquisition.json"
    acquisition.write_text(
        json.dumps(
            {
                "artifacts": [
                    {
                        "candidate_filename": "game.jar",
                        "identity": {"computed_sha256": digest(b"game")},
                    }
                ]
            }
        ),
        encoding="utf-8",
    )
    overlay = tmp_path / "overlay.json"
    overlay.write_text(
        json.dumps({"overlay": {"filename": "spark.jar", "sha256": digest(b"spark")}}),
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="filenames do not match"):
        module.validate_runtime_mods(tmp_path, overlay, retained, acquisition)
