from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import cast

import pytest
from tools import run_item10_probe as runner
from tools.run_item7_worldgen import RunReceipt

from mcpack_evidence.item7_runtime import WorldgenRequest, sha256_file, validate_java_runtime
from mcpack_evidence.item7_selections import ITEM10_SELECTIONS


@pytest.mark.parametrize(
    ("arm", "attempt", "role", "repetition"),
    [
        ("baseline", 1, "ordinary", 1),
        ("without-sparse", 1, "ordinary", 1),
        ("baseline", 2, "ordinary", 1),
        ("without-sparse", 2, "ordinary", 1),
        ("without-sparse", 3, "ocean-heavy", 2),
    ],
)
def test_full_runner_builds_observer_for_both_arms(  # noqa: PLR0913, PLR0917 - explicit sampling cases.
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    arm: str,
    attempt: int,
    role: str,
    repetition: int,
) -> None:
    root = Path(__file__).parents[2]
    java_home = root / "downloads/item2/temurin/extracted/jdk-21.0.12.1+1"
    if not (java_home / "bin/javac").is_file():
        pytest.skip("Pinned Temurin compiler is required")
    java, version = validate_java_runtime(java_home)
    (tmp_path / "tools").mkdir()
    _ = (tmp_path / "tools/Item10PlacementProbe.java").write_bytes(
        (root / "tools/Item10PlacementProbe.java").read_bytes()
    )
    monkeypatch.chdir(tmp_path)
    for name in ("JAVA_TOOL_OPTIONS", "JDK_JAVA_OPTIONS", "_JAVA_OPTIONS"):
        monkeypatch.delenv(name, raising=False)

    def validated_java(path: Path) -> tuple[Path, str]:
        del path
        return java, version

    def revision(*args: object, **kwargs: object) -> str:
        del args, kwargs
        return "test-revision\n"

    monkeypatch.setattr(runner, "validate_java_runtime", validated_java)
    monkeypatch.setattr(subprocess, "check_output", revision)
    calls: list[WorldgenRequest] = []

    def execute(
        request: WorldgenRequest,
        *,
        java_tool_options: str,
        before_generation: tuple[str, ...],
        after_generation: tuple[str, ...],
    ) -> RunReceipt:
        calls.append(request)
        assert "-javaagent:" in java_tool_options
        assert "trace.jsonl" in java_tool_options
        assert before_generation == after_generation == ()
        return RunReceipt(preflight=None, lifecycle=None, configuration=None, rejection_reason=None)

    monkeypatch.setattr(runner, "execute", execute)
    name = f"full-{role}-r{repetition}-{arm}"
    preserved: list[Path] = []
    if attempt > 1:
        for suffix in ("", "-attempt2")[: attempt - 1]:
            for parent in ("evidence/raw/item10", "instances/item10"):
                original = tmp_path / parent / (name + suffix)
                original.mkdir(parents=True)
                sentinel = original / "retained-failure.txt"
                _ = sentinel.write_text("preserve failed attempt\n")
                preserved.append(sentinel)
        name += f"-attempt{attempt}"
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "run_item10_probe",
            "--name",
            name,
            "--mode",
            "probe",
            "--preset",
            "item10",
            "--arm",
            arm,
            "--repetition",
            str(repetition),
            "--role",
            role,
            *(["--attempt", str(attempt)] if attempt > 1 else []),
        ],
    )
    runner.main()
    assert len(calls) == 1
    assert calls[0].selections == ITEM10_SELECTIONS
    assert calls[0].mode == "item10"
    assert calls[0].omit_sparse_structures == (arm == "without-sparse")
    assert calls[0].timeout_seconds == 14400
    output = tmp_path / "evidence/raw/item10" / name
    report = cast("dict[str, object]", json.loads((output / "diagnostic.json").read_text()))
    assert report["arm"] == arm
    assert report["repetition"] == repetition
    assert report["attempt"] == attempt
    assert calls[0].target == Path("instances/item10") / name
    assert all(path.read_text() == "preserve failed attempt\n" for path in preserved)
    probe = cast("dict[str, str]", report["probe"])
    assert probe["jar_sha256"] == sha256_file(output / "probe.jar")
    assert probe["source_sha256"] == sha256_file(root / "tools/Item10PlacementProbe.java")


def test_changed_collector_source_is_rejected_before_build_or_launch(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(tmp_path)
    for name in ("JAVA_TOOL_OPTIONS", "JDK_JAVA_OPTIONS", "_JAVA_OPTIONS"):
        monkeypatch.delenv(name, raising=False)
    (tmp_path / "tools").mkdir()
    _ = (tmp_path / "tools/Item10PlacementProbe.java").write_text("changed source")

    def java(path: Path) -> tuple[Path, str]:
        del path
        return tmp_path / "unavailable-java", "test"

    def revision(*args: object, **kwargs: object) -> str:
        del args, kwargs
        return "test-revision\n"

    monkeypatch.setattr(runner, "validate_java_runtime", java)
    monkeypatch.setattr(subprocess, "check_output", revision)
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "run_item10_probe",
            "--name",
            "full-ordinary-r1-baseline",
            "--mode",
            "probe",
            "--preset",
            "item10",
            "--arm",
            "baseline",
            "--repetition",
            "1",
        ],
    )
    with pytest.raises(ValueError, match="source differs from the frozen observer"):
        runner.main()
    output = tmp_path / "evidence/raw/item10/full-ordinary-r1-baseline"
    report = cast("dict[str, object]", json.loads((output / "diagnostic.json").read_text()))
    assert "source differs from the frozen observer" in str(report["rejection_reason"])
    assert not (output / "probe.jar").exists()
    assert not (tmp_path / "instances").exists()


@pytest.mark.parametrize(
    "arguments",
    [
        ["--mode", "control", "--preset", "item10", "--arm", "baseline", "--repetition", "1"],
        ["--mode", "probe", "--preset", "item10"],
        ["--mode", "probe", "--preset", "pilot", "--arm", "baseline"],
        ["--mode", "probe", "--preset", "pilot", "--attempt", "2"],
        ["--mode", "probe", "--preset", "item10", "--attempt", "4"],
        [
            "--mode",
            "probe",
            "--preset",
            "item10",
            "--attempt",
            "3",
            "--arm",
            "baseline",
            "--repetition",
            "2",
            "--role",
            "ocean-heavy",
        ],
        [
            "--mode",
            "probe",
            "--preset",
            "item10",
            "--arm",
            "baseline",
            "--repetition",
            "1",
            "--bop-fixture",
        ],
        ["--mode", "probe", "--preset", "item10", "--arm", "baseline", "--repetition", "1"],
    ],
)
def test_invalid_sampling_combinations_fail_before_output_creation(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    arguments: list[str],
) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(sys, "argv", ["run_item10_probe", "--name", "invalid", *arguments])
    with pytest.raises(SystemExit) as error:
        runner.main()
    assert error.value.code == 2
    assert not (tmp_path / "evidence").exists()
