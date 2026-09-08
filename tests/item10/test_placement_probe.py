# ruff: noqa: S603
# Subprocesses use the pinned local JDK, tracked fixtures and temporary outputs, without a shell.
import hashlib
import json
import subprocess
import zipfile
from pathlib import Path
from typing import cast

import pytest

ROOT = Path(__file__).resolve().parents[2]
JDK = ROOT / "downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin"
EXPORT = "java.base/jdk.internal.org.objectweb.asm=ALL-UNNAMED"


def test_probe_preserves_original_write_calls_results_and_exceptions(tmp_path: Path) -> None:
    if not (JDK / "javac").exists():
        pytest.skip("Pinned Temurin compiler is required for the placement-probe fixture")
    sources = sorted((ROOT / "tests/item10/probe-fixture").rglob("*.java"))
    sources.append(ROOT / "tools/Item10PlacementProbe.java")
    _ = subprocess.run(
        [
            str(JDK / "javac"),
            "--add-exports",
            EXPORT,
            "-classpath",
            str(tmp_path),
            "-Xlint:all",
            "-Werror",
            "-d",
            str(tmp_path),
            *map(str, sources),
        ],
        check=True,
        capture_output=True,
        text=True,
        timeout=45,
    )
    manifest = tmp_path / "probe.mf"
    _ = manifest.write_text("Manifest-Version: 1.0\nPremain-Class: Item10PlacementProbe\n\n")
    agent = tmp_path / "probe.jar"
    probe_classes = sorted(tmp_path.glob("Item10PlacementProbe*.class"))
    _ = subprocess.run(
        [
            str(JDK / "jar"),
            "--create",
            "--file",
            str(agent),
            "--manifest",
            str(manifest),
            "--date=2026-09-08T00:00:00Z",
            *[arg for path in probe_classes for arg in ("-C", str(tmp_path), path.name)],
        ],
        check=True,
        capture_output=True,
        text=True,
        timeout=45,
    )
    archive = ROOT / "downloads/item3/candidates/explorations-neoforge-1.21.1-1.6.2.jar"
    assert hashlib.sha256(archive.read_bytes()).hexdigest() == (
        "420d0373711877a5e1a86b7f9b4f54848f3debb2f116c2509a5cc4eb496c979e"
    )
    with zipfile.ZipFile(archive) as source:
        original_class = source.read(
            "com/tristankechlo/explorations/worldgen/features/ScarecrowFeature.class"
        )
    assert hashlib.sha256(original_class).hexdigest() == (
        "6d959a626cd2b3011adb2e2571bb74d3a7b49aaa2f0f259a287439787a2a763a"
    )
    retained_class = tmp_path / "retained.class"
    transformed_class = tmp_path / "transformed.class"
    _ = retained_class.write_bytes(original_class)
    _ = subprocess.run(
        [
            str(JDK / "java"),
            "--add-exports",
            EXPORT,
            "-classpath",
            str(tmp_path),
            "ProbeFixture",
            "transform",
            str(retained_class),
            str(transformed_class),
        ],
        check=True,
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert transformed_class.read_bytes() != original_class
    for mode, calls in [("normal", 5), ("early", 0), ("exception", 3)]:
        trace = tmp_path / f"{mode}.jsonl"
        command = [str(JDK / "java"), "--add-exports", EXPORT, "-classpath", str(tmp_path)]
        ordinary = subprocess.run(
            [*command, "ProbeFixture", mode], check=True, capture_output=True, text=True, timeout=30
        )
        observed = subprocess.run(
            [*command, f"-javaagent:{agent}={trace}", "ProbeFixture", mode],
            check=True,
            capture_output=True,
            text=True,
            timeout=30,
        )
        assert observed.stdout == ordinary.stdout
        rows = [
            cast("dict[str, object]", json.loads(line)) for line in trace.read_text().splitlines()
        ]
        assert rows[0]["kind"] == "installed"
        assert sum(row["kind"] in {"write", "write_exception"} for row in rows) == calls
        assert rows[-1]["installed"] is True
        assert rows[-1]["unfinished_attempts"] == (1 if mode == "exception" else 0)
        assert rows[1]["origin"] == [1, -5, 3]
        if mode == "normal":
            assert [row["returned"] for row in rows if row["kind"] == "write"] == [
                True,
                False,
                True,
                True,
                True,
            ]
