from __future__ import annotations

import gzip
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


def test_committed_cross_item_identity_bindings() -> None:
    """Reproduce the post-delivery audit's Item 7 and eighteen-attempt comparisons."""
    root = Path(__file__).parents[2]
    protocol = cast(
        "dict[str, dict[str, object]]",
        json.loads((root / "evidence/item-7/protocol/worldgen-audit-v1.json").read_bytes()),
    )
    identity = protocol["identity"]
    bindings = {
        "retained_manifest_sha256": (
            "retained_manifest",
            "evidence/item-3/runtime/retained-server-candidates.txt",
        ),
        "frozen_manifest_sha256": (
            "frozen_config_manifest",
            "evidence/item-6/generated-config-manifest.json",
        ),
        "config_audit_sha256": ("config_audit", "evidence/item-6/config-audit.json"),
        "seed_suite_sha256": ("seed_suite", "test-environment/seed-suite.json"),
    }
    digests: dict[str, str] = {}
    for field, (key, path) in bindings.items():
        reference = cast("dict[str, str]", identity[key])
        assert reference["path"] == path, key
        digests[field] = sha256_file(root / path)
        assert digests[field] == reference["sha256"], key
    seeds = {
        "ordinary": "42",
        "mountainous": "6671238423019257953",
        "ocean-heavy": "95920844204830198",
        "biome-diverse": "-3503646078644842058",
    }
    cells: dict[str, tuple[str, int, str]] = {}
    for role in seeds:
        for repetition in (1, 2):
            for arm in ("baseline", "without-sparse"):
                name = f"full-{role}-r{repetition}-{arm}"
                if (role, repetition, arm) == ("ocean-heavy", 2, "without-sparse"):
                    name += "-attempt3"
                cells[name] = (role, repetition, arm)
    comparison = cast(
        "dict[str, object]",
        json.loads(
            gzip.decompress(
                (root / "evidence/item-10/accepted-biome-comparisons.json.gz").read_bytes()
            )
        ),
    )
    assert len(cells) == 16
    assert set(comparison) == set(cells)
    for suffix in ("", "-attempt2"):
        cells["full-ocean-heavy-r2-without-sparse" + suffix] = ("ocean-heavy", 2, "without-sparse")
    assert len(cells) == 18
    for name, (role, repetition, arm) in cells.items():
        document = cast(
            "dict[str, object]",
            json.loads((root / f"evidence/item-10/{name}/run.json").read_bytes()),
        )
        assert (document["arm"], document["repetition"]) == (arm, repetition), name
        run = cast("dict[str, object]", document["run"])
        preflight = cast("dict[str, object]", run["preflight"])
        assert all(preflight[field] == digest for field, digest in digests.items()), name
        assert preflight["java_version"] == identity["java_build"], name
        assert (preflight["seed_role"], preflight["seed"]) == (role, seeds[role]), name
        assert preflight["retained_candidate_count"] == 136, name
        assert preflight["instrumented_candidate_count"] == (137 if arm == "baseline" else 136), (
            name
        )
        assert preflight["sparse_structures_omitted"] is (arm == "without-sparse"), name
        assert preflight["retained_runtime_sha256"] == (
            "4062d6179218916c703269f113663b1e078adebbf6d43a691e692d972e07ac50"
        ), name
        assert (
            preflight["instrumented_runtime_sha256"]
            == {
                "baseline": "e2dab4c80cff137d747bd035588882797f85fa8d4d5b6ccb98a5d717fa0749c8",
                "without-sparse": (
                    "84a884f99e4ac48defb9ea0b2c9e45bf3d0f4f6e881a4be4d8968dc2be14d4da"
                ),
            }[arm]
        ), name
        assert preflight["chunky_sha256"] == (
            "d72f235cf1f56f2c374f52c00bdda5034524b28142305a84cfc123a3f92ad274"
        ), name
        probe = cast("dict[str, str]", document["probe"])
        assert probe["source_sha256"] == runner.COLLECTOR_SOURCE_SHA256, name
        assert probe["jar_sha256"] == runner.COLLECTOR_JAR_SHA256, name


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
