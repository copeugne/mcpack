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


def _build_probe(tmp_path: Path) -> Path:
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
    return agent


def test_probe_preserves_original_write_calls_results_and_exceptions(tmp_path: Path) -> None:
    agent = _build_probe(tmp_path)
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
    for mode, calls in [("normal", 5), ("early", 0), ("exception", 3), ("isolated", 5)]:
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


def test_template_probe_preserves_calls_and_records_only_content(tmp_path: Path) -> None:
    agent = _build_probe(tmp_path)
    command = [str(JDK / "java"), "--add-exports", EXPORT, "-classpath", str(tmp_path)]
    for mode in ("normal", "early", "empty", "refused", "exception", "isolated", "outside"):
        trace = tmp_path / f"template-{mode}.jsonl"
        ordinary = subprocess.run(
            [*command, "TemplateFixture", mode],
            check=True,
            capture_output=True,
            text=True,
            timeout=30,
        )
        observed = subprocess.run(
            [*command, f"-javaagent:{agent}={trace}", "TemplateFixture", mode],
            check=True,
            capture_output=True,
            text=True,
            timeout=30,
        )
        assert observed.stdout == ordinary.stdout
        rows = [
            cast("dict[str, object]", json.loads(line)) for line in trace.read_text().splitlines()
        ]
        for row in rows:
            if row["kind"] == "feature_installed":
                class_name = cast("str", row["class"])
                incoming = trace.with_name(trace.name + ".classes") / (class_name + ".class")
                assert (
                    hashlib.sha256(incoming.read_bytes()).hexdigest() == row["input_class_sha256"]
                )
        writes = [row for row in rows if row["kind"] in {"write", "write_exception"}]
        assert len(writes) == (0 if mode in {"early", "empty", "outside"} else 2)
        assert rows[-1]["unfinished_attempts"] == (1 if mode == "exception" else 0)
        ground = [row for row in rows if row["kind"] == "ground"]
        assert len(ground) == (0 if mode in {"early", "outside"} else 1)
        if ground:
            assert ground[0]["position"] == [1, -5, 3]
            assert ground[0]["attempt"] == 1
        placements = [row for row in rows if row["kind"] == "template_begin"]
        if mode not in {"early", "outside"}:
            assert len(placements) == 1
            assert placements[0]["path"] == "original.nbt"
        if mode == "refused":
            assert all(row["returned"] is False for row in writes)
        elif mode in {"normal", "isolated"}:
            assert [row["returned"] for row in writes] == [False, True]
            assert all("content" in cast("str", row["state"]) for row in writes)

    sources = ROOT / "evidence/item-8/sources"
    targets = (
        ("bop-feature-scope", "biomesoplenty/worldgen/feature/misc/AnomalyFeature.class"),
        ("bop-feature-scope", "biomesoplenty/worldgen/feature/misc/MonolithFeature.class"),
        (
            "betterend-entry-template-consumers",
            "org/betterx/betterend/world/features/NBTFeature.class",
        ),
        (
            "betterend-entry-template-consumers",
            "org/betterx/betterend/world/features/BuildingListFeature$StructureInfo.class",
        ),
        (
            "betterend-feature-scope",
            "org/betterx/betterend/world/features/CrashedShipFeature.class",
        ),
        (
            "missing-template-code",
            "net/minecraft/world/level/levelgen/structure/templatesystem/StructureTemplate.class",
        ),
    )
    for group, name in targets:
        identities = cast(
            "list[dict[str, str]]", json.loads((sources / group / "identities.json").read_text())
        )
        identity = next(row for row in identities if row["class"] == name)
        archive = ROOT / "downloads/item3/candidates" / identity["archive"]
        if group == "missing-template-code":
            archive = (
                ROOT
                / "instances/item10/scarecrow-probe-r3/libraries/net/minecraft/server"
                / "1.21.1-20240808.144430"
                / identity["archive"]
            )
        assert hashlib.sha256(archive.read_bytes()).hexdigest() == identity["archive_sha256"]
        with zipfile.ZipFile(archive) as jar:
            payload = jar.read(name)
        assert hashlib.sha256(payload).hexdigest() == identity["class_sha256"]
        original = tmp_path / "template-original.class"
        transformed = tmp_path / "template-transformed.class"
        _ = original.write_bytes(payload)
        _ = subprocess.run(
            [
                *command,
                "TemplateFixture",
                "transform",
                name.removesuffix(".class"),
                str(original),
                str(transformed),
            ],
            check=True,
            capture_output=True,
            text=True,
            timeout=30,
        )
        assert transformed.read_bytes() != payload


def test_direct_feature_helper_preserves_writes(tmp_path: Path) -> None:
    agent = _build_probe(tmp_path)
    command = [str(JDK / "java"), "--add-exports", EXPORT, "-classpath", str(tmp_path)]
    for feature in ("anomaly", "monolith"):
        for mode in ("normal", "early", "refused", "exception", "isolated", "outside"):
            arguments = ["DirectFixture", feature, mode]
            vanilla = subprocess.run(
                [*command, *arguments], check=True, capture_output=True, text=True, timeout=30
            )
            trace = tmp_path / f"{feature}-{mode}.jsonl"
            observed = subprocess.run(
                [*command, f"-javaagent:{agent}={trace}", *arguments],
                check=True,
                capture_output=True,
                text=True,
                timeout=30,
            )
            assert observed.stdout == vanilla.stdout
            rows = [
                cast("dict[str, object]", json.loads(line))
                for line in trace.read_text().splitlines()
            ]
            assert not any(r["kind"] == "installation_failed" for r in rows)
            assert any(
                r.get("class") == "net/minecraft/world/level/levelgen/feature/Feature" for r in rows
            )
            writes = [r for r in rows if r["kind"] in {"write", "write_exception"}]
            expected_writes = 4 if feature == "anomaly" and mode != "exception" else 3
            assert len(writes) == (0 if mode in {"early", "outside"} else expected_writes)
            assert rows[-1]["unfinished_attempts"] == (1 if mode == "exception" else 0)
            if mode in {"normal", "isolated"}:
                assert [r["returned"] for r in writes] == (
                    [True, False, True, True] if feature == "anomaly" else [True, False, True]
                )
                assert [r["flags"] for r in writes] == (
                    [3, 3, 3, 2] if feature == "anomaly" else [3, 3, 3]
                )
            if mode == "refused":
                assert all(r["returned"] is False for r in writes)

    archive = (
        ROOT
        / "instances/item10/scarecrow-probe-r3/libraries/net/minecraft/server"
        / "1.21.1-20240808.144430/server-1.21.1-20240808.144430-srg.jar"
    )
    assert hashlib.sha256(archive.read_bytes()).hexdigest() == (
        "26ca9c40d7e1681190b428583c38816852218e78df3f8bdb60a59a78503aec71"
    )
    name = "net/minecraft/world/level/levelgen/feature/Feature"
    with zipfile.ZipFile(archive) as jar:
        payload = jar.read(name + ".class")
    original = tmp_path / "feature-original.class"
    transformed = tmp_path / "feature-transformed.class"
    _ = original.write_bytes(payload)
    _ = subprocess.run(
        [*command, "TemplateFixture", "transform", name, str(original), str(transformed)],
        check=True,
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert transformed.read_bytes() != payload


def test_monster_box_void_generator_preserves_write_result(tmp_path: Path) -> None:
    agent = _build_probe(tmp_path)
    command = [str(JDK / "java"), "--add-exports", EXPORT, "-classpath", str(tmp_path)]
    name = "org/violetmoon/quark/content/world/gen/MonsterBoxGenerator"
    for mode in ("normal", "early", "refused", "exception", "isolated", "outside"):
        arguments = ["GeneratorFixture", mode]
        ordinary = subprocess.run(
            [*command, *arguments], check=True, capture_output=True, text=True, timeout=30
        )
        trace = tmp_path / f"generator-{mode}.jsonl"
        observed = subprocess.run(
            [*command, f"-javaagent:{agent}={trace}", *arguments],
            check=True,
            capture_output=True,
            text=True,
            timeout=30,
        )
        assert observed.stdout == ordinary.stdout
        rows = [
            cast("dict[str, object]", json.loads(line)) for line in trace.read_text().splitlines()
        ]
        assert not any(r["kind"] == "installation_failed" for r in rows)
        assert any(r.get("class") == name and r["kind"] == "feature_installed" for r in rows)
        writes = [r for r in rows if r["kind"] in {"write", "write_exception"}]
        assert len(writes) == (0 if mode in {"early", "outside"} else 1)
        ends = [r for r in rows if r["kind"] == "generator_end"]
        assert len(ends) == (0 if mode in {"outside", "exception"} else 1)
        assert all(set(r) == {"kind", "attempt"} for r in ends)
        assert rows[-1]["unfinished_attempts"] == (1 if mode == "exception" else 0)
        if mode in {"normal", "refused", "isolated"}:
            assert writes[0]["returned"] is (mode != "refused")
            assert writes[0]["flags"] == 0
            assert writes[0]["position"] == [1, -5, 3]
    archive = ROOT / "downloads/item3/candidates/Quark-4.1-480.jar"
    assert (
        hashlib.sha256(archive.read_bytes()).hexdigest()
        == "989c465df2e4cb9f602840c2eec143358bf11462cc19dc0b0c7c9f17449e75a5"
    )
    with zipfile.ZipFile(archive) as jar:
        payload = jar.read(name + ".class")
    assert (
        hashlib.sha256(payload).hexdigest()
        == "bffcb41fcefa591835aff3ca7efc8ded0ba971bb409ab9a751dbede417c62eb8"
    )
    original = tmp_path / "monster-original.class"
    transformed = tmp_path / "monster-transformed.class"
    _ = original.write_bytes(payload)
    _ = subprocess.run(
        [*command, "TemplateFixture", "transform", name, str(original), str(transformed)],
        check=True,
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert transformed.read_bytes() != payload


def test_nether_spike_static_generator_preserves_all_write_sites(tmp_path: Path) -> None:
    agent = _build_probe(tmp_path)
    command = [str(JDK / "java"), "--add-exports", EXPORT, "-classpath", str(tmp_path)]
    name = "org/violetmoon/quark/content/world/gen/ObsidianSpikeGenerator"
    for mode in ("normal", "early", "refused", "exception", "isolated", "outside"):
        args = ["GeneratorFixture", mode, "spike"]
        ordinary = subprocess.run(
            [*command, *args], check=True, capture_output=True, text=True, timeout=30
        )
        trace = tmp_path / f"spike-{mode}.jsonl"
        observed = subprocess.run(
            [*command, f"-javaagent:{agent}={trace}", *args],
            check=True,
            capture_output=True,
            text=True,
            timeout=30,
        )
        assert ordinary.stdout == observed.stdout
        rows = [
            cast("dict[str, object]", json.loads(line)) for line in trace.read_text().splitlines()
        ]
        assert not any(r["kind"] == "installation_failed" for r in rows)
        assert any(r.get("class") == name and r["kind"] == "feature_installed" for r in rows)
        writes = [r for r in rows if r["kind"] in {"write", "write_exception"}]
        expected = 0 if mode in {"early", "outside"} else 3 if mode == "exception" else 7
        assert len(writes) == expected
        assert rows[-1]["unfinished_attempts"] == (1 if mode == "exception" else 0)
        if mode != "outside":
            feature = next(r for r in rows if r["kind"] == "feature")
            assert feature["class"] == name.replace("/", ".")
        if mode in {"normal", "refused", "isolated"}:
            assert all(r["flags"] == 0 and r["returned"] is (mode != "refused") for r in writes)
            assert len([r for r in rows if r["kind"] == "generator_end"]) == 1
    archive = ROOT / "downloads/item3/candidates/Quark-4.1-480.jar"
    assert (
        hashlib.sha256(archive.read_bytes()).hexdigest()
        == "989c465df2e4cb9f602840c2eec143358bf11462cc19dc0b0c7c9f17449e75a5"
    )
    with zipfile.ZipFile(archive) as jar:
        payload = jar.read(name + ".class")
    assert (
        hashlib.sha256(payload).hexdigest()
        == "509ca413b7bdaae9659a3dae7c6e730e650a11750f53acef592a3fc63d8fc90a"
    )
    original = tmp_path / "spike-original.class"
    transformed = tmp_path / "spike-transformed.class"
    _ = original.write_bytes(payload)
    _ = subprocess.run(
        [*command, "TemplateFixture", "transform", name, str(original), str(transformed)],
        check=True,
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert transformed.read_bytes() != payload


def test_spiral_preserves_source_parts_and_outside_calls(tmp_path: Path) -> None:
    agent = _build_probe(tmp_path)
    command = [str(JDK / "java"), "--add-exports", EXPORT, "-classpath", str(tmp_path)]
    name = "org/violetmoon/quark/content/world/gen/SpiralSpireGenerator"
    modes = ("normal", "early", "refused", "exception", "isolated", "outside", "outside-exception")
    for mode in modes:
        args = ["GeneratorFixture", mode, "spiral"]
        ordinary = subprocess.run(
            [*command, *args], check=True, capture_output=True, text=True, timeout=30
        )
        trace = tmp_path / f"spiral-{mode}.jsonl"
        observed = subprocess.run(
            [*command, f"-javaagent:{agent}={trace}", *args],
            check=True,
            capture_output=True,
            text=True,
            timeout=30,
        )
        assert ordinary.stdout == observed.stdout
        rows = [
            cast("dict[str, object]", json.loads(line)) for line in trace.read_text().splitlines()
        ]
        assert not any(r["kind"] == "installation_failed" for r in rows)
        assert any(r.get("class") == name and r["kind"] == "feature_installed" for r in rows)
        attempts = [r for r in rows if r["kind"] == "begin"]
        parts = [r for r in rows if r["kind"] == "part"]
        writes = [r for r in rows if r["kind"] in {"write", "write_exception"}]
        outside = mode.startswith("outside")
        assert len(attempts) == (0 if outside else 1 if mode == "exception" else 3)
        assert len(parts) == len(attempts)
        assert len(writes) == (0 if outside or mode == "early" else 1 if mode == "exception" else 6)
        assert rows[-1]["unfinished_attempts"] == (1 if mode == "exception" else 0)
        if mode in {"normal", "refused", "isolated", "early"}:
            assert [r["origin"] for r in attempts] == [[1, -5, 3], [1, -5, 3], [64, 0, 64]]
            assert [r["position"] for r in parts] == [[16, 0, 16], [32, 0, 16], [48, 0, 16]]
            assert (
                len({(r["dimension"], tuple(cast("list[int]", r["origin"]))) for r in attempts})
                == 2
            )
            assert len([r for r in rows if r["kind"] == "generator_end"]) == 3
            assert all(r["returned"] is (mode != "refused") for r in writes)
    archive = ROOT / "downloads/item3/candidates/Quark-4.1-480.jar"
    assert hashlib.sha256(archive.read_bytes()).hexdigest() == (
        "989c465df2e4cb9f602840c2eec143358bf11462cc19dc0b0c7c9f17449e75a5"
    )
    with zipfile.ZipFile(archive) as jar:
        payload = jar.read(name + ".class")
    assert hashlib.sha256(payload).hexdigest() == (
        "dd57fdac61e67cece06adc078a4538e3949573baff8f65df9819218bd282b771"
    )
    original = tmp_path / "spiral-original.class"
    transformed = tmp_path / "spiral-transformed.class"
    _ = original.write_bytes(payload)
    _ = subprocess.run(
        [*command, "TemplateFixture", "transform", name, str(original), str(transformed)],
        check=True,
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert transformed.read_bytes() != payload


def test_fairy_keeps_delegate_result_separate_from_origin_content(tmp_path: Path) -> None:
    agent = _build_probe(tmp_path)
    command = [str(JDK / "java"), "--add-exports", EXPORT, "-classpath", str(tmp_path)]
    name = "org/violetmoon/quark/content/world/gen/FairyRingGenerator"
    for mode in (
        "normal",
        "true-air",
        "refused",
        "early",
        "exception",
        "flower-exception",
        "isolated",
    ):
        args = ["GeneratorFixture", mode, "fairy"]
        ordinary = subprocess.run(
            [*command, *args], check=True, capture_output=True, text=True, timeout=30
        )
        trace = tmp_path / f"fairy-{mode}.jsonl"
        observed = subprocess.run(
            [*command, f"-javaagent:{agent}={trace}", *args],
            check=True,
            capture_output=True,
            text=True,
            timeout=30,
        )
        assert ordinary.stdout == observed.stdout
        rows = [
            cast("dict[str, object]", json.loads(line)) for line in trace.read_text().splitlines()
        ]
        assert not any(r["kind"] == "installation_failed" for r in rows)
        assert any(r.get("class") == name and r["kind"] == "feature_installed" for r in rows)
        assert next(r for r in rows if r["kind"] == "begin")["origin"] == [1, -5, 3]
        assert rows[-1]["unfinished_attempts"] == (1 if "exception" in mode else 0)
        if mode in {"normal", "true-air", "refused", "isolated"}:
            assert [r["site"] for r in rows if r["kind"] == "writer"] == [1, 2, 3, 4]
            assert len([r for r in rows if r["kind"] == "write"]) == 4
            assert next(r for r in rows if r["kind"] == "flower_end")["returned"] is (
                mode == "true-air"
            )
            state = next(r for r in rows if r["kind"] == "flower_state")["state"]
            assert state == (
                "BlockState[name=air]" if mode == "true-air" else "BlockState[name=flower]"
            )
            assert all(r["returned"] is (mode != "refused") for r in rows if r["kind"] == "write")
            assert "reads=5" in observed.stdout
        elif mode == "flower-exception":
            assert len([r for r in rows if r["kind"] == "flower_exception"]) == 1
            assert not any(r["kind"] == "flower_state" for r in rows)
        elif mode == "early":
            assert not any(r["kind"] in {"writer", "flower_begin", "write"} for r in rows)
    archive = ROOT / "downloads/item3/candidates/Quark-4.1-480.jar"
    assert hashlib.sha256(archive.read_bytes()).hexdigest() == (
        "989c465df2e4cb9f602840c2eec143358bf11462cc19dc0b0c7c9f17449e75a5"
    )
    with zipfile.ZipFile(archive) as jar:
        payload = jar.read(name + ".class")
    assert hashlib.sha256(payload).hexdigest() == (
        "3a30145aaad2e116ab762a6c090659a3f02f125dfd98972c3df72f4319691a74"
    )
    original = tmp_path / "fairy-original.class"
    transformed = tmp_path / "fairy-transformed.class"
    _ = original.write_bytes(payload)
    _ = subprocess.run(
        [*command, "TemplateFixture", "transform", name, str(original), str(transformed)],
        check=True,
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert transformed.read_bytes() != payload


@pytest.mark.parametrize(
    "mode", ["normal", "refused", "exception", "galleon", "absent", "unrelated", "isolated"]
)
def test_urn_patch_parent_writes_and_exception_cleanup(tmp_path: Path, mode: str) -> None:
    agent = _build_probe(tmp_path)
    command = [str(JDK / "java"), "--add-exports", EXPORT, "-classpath", str(tmp_path)]
    ordinary = subprocess.run(
        [*command, "UrnFixture", mode], check=True, capture_output=True, text=True
    )
    trace = tmp_path / "urn.jsonl"
    observed = subprocess.run(
        [*command, f"-javaagent:{agent}={trace}", "UrnFixture", mode],
        check=True,
        capture_output=True,
        text=True,
    )
    assert observed.stdout == ordinary.stdout
    rows = [cast("dict[str, object]", json.loads(line)) for line in trace.read_text().splitlines()]
    assert not any(row["kind"] == "installation_failed" for row in rows)
    assert rows[-1]["unfinished_attempts"] == 0
    parents = [row for row in rows if row["kind"] == "urn_parent"]
    if mode == "unrelated":
        assert not parents
        assert not any(row["kind"] == "write" for row in rows)
        return
    assert len(parents) == 2
    expected = (
        None
        if mode == "absent"
        else "test:galleon_component"
        if mode == "galleon"
        else "supplementaries:cave_urns"
    )
    assert all(row["placed_feature"] == expected for row in parents)
    writes = [row for row in rows if row["kind"] == "write"]
    assert len(writes) == (1 if mode == "exception" else 2)
    assert all(row["flags"] == 2 and row["returned"] == (mode != "refused") for row in writes)
    ends = [row for row in rows if row["kind"] == "end"]
    assert len(ends) == (1 if mode == "exception" else 2)
    assert all(row["returned"] is True for row in ends)
    assert sum(row["kind"] == "attempt_exception" for row in rows) == (mode == "exception")


def test_urn_hooks_transform_hash_verified_retained_classes(tmp_path: Path) -> None:
    _ = _build_probe(tmp_path)
    archive = (
        ROOT
        / "instances/pristine-baseline-v0/libraries/net/minecraft/server"
        / "1.21.1-20240808.144430/server-1.21.1-20240808.144430-srg.jar"
    )
    assert (
        hashlib.sha256(archive.read_bytes()).hexdigest()
        == "26ca9c40d7e1681190b428583c38816852218e78df3f8bdb60a59a78503aec71"
    )
    classes = {
        "net/minecraft/world/level/levelgen/placement/PlacedFeature": (
            "bb5076d73ed849bfb377ffe117575ab98a3cef8134c674de7b39a8eab62e1f9d"
        ),
        "net/minecraft/world/level/levelgen/feature/SimpleBlockFeature": (
            "17907c21c8e522ac39fa9dcc838dd8f4afdcd7bcfc200480b14187b7a01875e2"
        ),
    }
    with zipfile.ZipFile(archive) as source:
        for name, digest in classes.items():
            content = source.read(name + ".class")
            assert hashlib.sha256(content).hexdigest() == digest
            original = tmp_path / "original.class"
            transformed = tmp_path / "transformed.class"
            _ = original.write_bytes(content)
            _ = subprocess.run(
                [
                    str(JDK / "java"),
                    "--add-exports",
                    EXPORT,
                    "-classpath",
                    str(tmp_path),
                    "TemplateFixture",
                    "transform",
                    name,
                    str(original),
                    str(transformed),
                ],
                check=True,
                capture_output=True,
                text=True,
            )
            assert transformed.read_bytes() != content


@pytest.mark.parametrize(
    "mode",
    [
        "normal",
        "refused",
        "exception",
        "early",
        "outside",
        "outside-template",
        "isolated",
        "configured",
    ],
)
@pytest.mark.parametrize("extras", [False, True])
def test_bridge_template_and_processor_phases_preserve_original(
    tmp_path: Path, mode: str, extras: bool
) -> None:
    fixture = "ExtrasFixture" if extras else "BridgeFixture"
    prefix = "extras" if extras else "bridge"
    agent = _build_probe(tmp_path)
    command = [str(JDK / "java"), "--add-exports", EXPORT, "-classpath", str(tmp_path)]
    original = subprocess.run(
        [*command, fixture, mode], check=True, capture_output=True, text=True, timeout=30
    )
    trace = tmp_path / "bridge.jsonl"
    observed = subprocess.run(
        [*command, f"-javaagent:{agent}={trace}", fixture, mode],
        check=True,
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert observed.stdout == original.stdout
    rows = [cast("dict[str, object]", json.loads(line)) for line in trace.read_text().splitlines()]
    assert not any(row["kind"] == "installation_failed" for row in rows)
    templates = [row for row in rows if row["kind"] == "template_begin"]
    markers = [row for row in rows if row["kind"] == f"{prefix}_processor"]
    variants = [row for row in rows if row["kind"] == f"{prefix}_configured"]
    if mode not in {"outside", "outside-template"}:
        assert len(variants) == 1
        assert variants[0]["configured_feature"] == (
            ("yungsextras:desert/wells/desert_well_sm" if extras else "yungsbridges:wood_17_0")
            if mode == "configured"
            else None
        )
    else:
        assert not variants
    if mode in {"early", "outside", "outside-template"}:
        assert not templates
        assert not markers
    else:
        assert len(templates) == 1
        assert templates[0]["path"] == (
            "yungsextras:desert/wells/well_sm" if extras else "yungsbridges:bridge/wood/17_0"
        )
        assert templates[0]["rotation"] == "NONE"
        assert len(markers) == (1 if mode == "exception" else 3)
        end = next(i for i, row in enumerate(rows) if row["kind"] == "template_end")
        assert all(row["kind"] != f"{prefix}_processor" for row in rows[:end])
        writes = [row for row in rows if row["kind"] == "write"]
        assert len(writes) == (2 if mode == "exception" else 5)
        assert writes[0]["returned"] is False  # Shared fixture refuses the first content write.
        assert all(row["returned"] == (mode != "refused") for row in writes[1:])
    assert rows[-1]["unfinished_attempts"] == 0
    failures = [row for row in rows if row["kind"] == "attempt_exception"]
    assert len(failures) == (1 if mode == "exception" else 0)


@pytest.mark.parametrize("extras", [False, True])
def test_bridge_hooks_cover_retained_template_and_all_processor_sites(
    tmp_path: Path, extras: bool
) -> None:
    _ = _build_probe(tmp_path)
    archive = (
        ROOT
        / "downloads/item3/candidates"
        / (
            "YungsExtras-1.21.1-NeoForge-5.1.1.jar"
            if extras
            else "YungsBridges-1.21.1-NeoForge-5.1.1.jar"
        )
    )
    assert hashlib.sha256(archive.read_bytes()).hexdigest() == (
        "0cd26474e514f5dc3114aaf5ec7e049bcd285f0c5db191bb45223193f35df70d"
        if extras
        else "bf93a85422a6b457358c3b56352641a97ec09cc37dec18b2cedcac2bd1ff9bec"
    )
    entries: list[dict[str, str]] = []
    sources = (
        ("yungs-extras-generators", "yungs-extras-desert-code")
        if extras
        else ("yungs-bridge-generation", "yungs-bridge-processors")
    )
    for source in sources:
        entries.extend(
            cast(
                "list[dict[str, str]]",
                json.loads(
                    (ROOT / "evidence/item-8/sources" / source / "identities.json").read_text()
                ),
            )
        )
    selected = [
        row
        for row in entries
        if (
            "/world/processor/" in row["class"]
            and not row["class"].endswith("/DynamicLegProcessor.class")
        )
        or row["class"].endswith(("/BridgeFeature.class", "/AbstractTemplateFeature.class"))
    ]
    if extras:
        selected = [
            row
            for row in entries
            if not row["class"].endswith(("/FeatureModule.class", "/AbstractSwampFeature.class"))
        ]
    assert len(selected) == (15 if extras else 14)
    with zipfile.ZipFile(archive) as jar:
        for row in selected:
            content = jar.read(row["class"])
            assert hashlib.sha256(content).hexdigest() == row["class_sha256"]
            original = tmp_path / "original.class"
            transformed = tmp_path / "transformed.class"
            _ = original.write_bytes(content)
            _ = subprocess.run(
                [
                    str(JDK / "java"),
                    "--add-exports",
                    EXPORT,
                    "-classpath",
                    str(tmp_path),
                    "TemplateFixture",
                    "transform",
                    row["class"][:-6],
                    str(original),
                    str(transformed),
                ],
                check=True,
                capture_output=True,
                text=True,
                timeout=30,
            )
            assert transformed.read_bytes() != content


@pytest.mark.parametrize("mode", ["recover", "template-recover"])
@pytest.mark.parametrize("extras", [False, True])
def test_bridge_caught_exception_allows_next_placement(
    tmp_path: Path, mode: str, extras: bool
) -> None:
    fixture = "ExtrasFixture" if extras else "BridgeFixture"
    agent = _build_probe(tmp_path)
    command = [str(JDK / "java"), "--add-exports", EXPORT, "-classpath", str(tmp_path)]
    original = subprocess.run(
        [*command, fixture, mode], check=True, capture_output=True, text=True, timeout=30
    )
    trace = tmp_path / "recovery.jsonl"
    observed = subprocess.run(
        [*command, f"-javaagent:{agent}={trace}", fixture, mode],
        check=True,
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert observed.stdout == original.stdout
    assert "recovered=true" in observed.stdout
    if mode == "recover":
        assert "same=true" in observed.stdout
    rows = [cast("dict[str, object]", json.loads(line)) for line in trace.read_text().splitlines()]
    assert not any(row["kind"] == "installation_failed" for row in rows)
    starts = [row["attempt"] for row in rows if row["kind"] == "begin"]
    assert len(starts) == 2
    failures = [row for row in rows if row["kind"] == "attempt_exception"]
    assert failures == [
        {
            "kind": "attempt_exception",
            "attempt": starts[0],
            "exception": "java.lang.IllegalStateException",
        }
    ]
    ends = [row for row in rows if row["kind"] == "end"]
    assert ends == [{"kind": "end", "attempt": starts[1], "returned": True}]
    assert rows[-1]["unfinished_attempts"] == 0
