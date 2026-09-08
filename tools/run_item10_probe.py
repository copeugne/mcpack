"""Run a fresh placement diagnostic or one declared Item 10 sampling arm."""

from __future__ import annotations

import argparse
import json
import os
import re
import shlex
import subprocess
from pathlib import Path
from typing import Final, Literal, cast

from tools.run_item7_worldgen import execute

from mcpack_evidence.item7_runtime import WorldgenRequest, sha256_file, validate_java_runtime
from mcpack_evidence.item7_selections import ITEM10_SELECTIONS, PILOT_SELECTIONS, RUN_SELECTIONS

COLLECTOR_SOURCE_SHA256: Final = "b07ebcacb9043ee7d1fb187a7d93e5b788d890ccd8edc3decc07060609a74396"
COLLECTOR_JAR_SHA256: Final = "d2051d5d5eb38aeda3dfc5c1d61d11ebf2e18a1fb3222ac46c12863556c5a782"


def main() -> None:  # noqa: C901, PLR0912, PLR0915 - keep the bounded collection workflow together.
    """Record the observational overlay, then use the established lifecycle unchanged."""
    parser = argparse.ArgumentParser(description=__doc__)
    _ = parser.add_argument("--name", required=True)
    _ = parser.add_argument("--mode", choices=("probe", "control"), required=True)
    _ = parser.add_argument("--preset", choices=("pilot", "run", "item10"), default="run")
    _ = parser.add_argument("--arm", choices=("baseline", "without-sparse"))
    _ = parser.add_argument("--repetition", type=int, choices=(1, 2))
    _ = parser.add_argument("--attempt", type=int, choices=(1, 2, 3))
    fixtures = parser.add_mutually_exclusive_group()
    _ = fixtures.add_argument("--betterend-fixture", action="store_true")
    _ = fixtures.add_argument("--bop-fixture", action="store_true")
    _ = parser.add_argument(
        "--role",
        choices=("ordinary", "mountainous", "ocean-heavy", "biome-diverse"),
        default="ordinary",
    )
    args = parser.parse_args()
    instance_name = cast("str", args.name)
    mode = cast("str", args.mode)
    role = cast("str", args.role)
    preset = cast("Literal['pilot', 'run', 'item10']", args.preset)
    arm = cast("str | None", args.arm)
    repetition = cast("int | None", args.repetition)
    declared_attempt = cast("int | None", args.attempt)
    attempt = declared_attempt if declared_attempt is not None else 1
    fixture = cast("bool", args.betterend_fixture)
    bop_fixture = cast("bool", args.bop_fixture)
    if (fixture or bop_fixture) and (mode != "probe" or preset != "pilot"):
        parser.error("placement fixtures require probe mode and the pilot preset")
    if preset == "item10":
        if mode != "probe" or arm is None or repetition is None:
            parser.error("Item 10 sampling requires probe mode, an explicit arm and repetition")
        if attempt == 3 and (role, repetition, arm) != ("ocean-heavy", 2, "without-sparse"):  # noqa: PLR2004 - exact authorized final attempt.
            parser.error("attempt 3 is authorized only for ocean-heavy repetition-2 control")
        expected_name = f"full-{role}-r{repetition}-{arm}"
        if attempt != 1:
            expected_name += f"-attempt{attempt}"
        if instance_name != expected_name:
            parser.error("Item 10 name must match role, repetition, arm and attempt")
    elif arm is not None or repetition is not None or declared_attempt is not None:
        parser.error("arm, repetition and attempt apply only to the Item 10 sampling preset")
    before_generation = (
        ("execute in minecraft:the_end run forceload add -32 -32 47 47",)
        if fixture or bop_fixture
        else ()
    )
    after_generation = (
        (
            "execute in minecraft:the_end run fill 0 80 0 15 80 15 minecraft:end_stone",
            (
                "execute in minecraft:the_end if block 8 81 8 minecraft:air "
                "run say item10-fixture-air-true"
            ),
            (
                "execute in minecraft:the_end unless block 8 81 8 minecraft:air "
                "run say item10-fixture-air-false"
            ),
            (
                "execute in minecraft:the_end if block 8 80 8 #wover:surfaces/terrain "
                "run say item10-fixture-terrain-true"
            ),
            (
                "execute in minecraft:the_end unless block 8 80 8 #wover:surfaces/terrain "
                "run say item10-fixture-terrain-false"
            ),
            (
                "execute in minecraft:the_end run place feature "
                "betterend:blossoming_spires_structures 8 81 8"
            ),
        )
        if fixture
        else ()
    )
    if bop_fixture:
        after_generation = (
            "execute in minecraft:the_end run fill 0 80 0 15 80 15 minecraft:end_stone",
            (
                "execute in minecraft:the_end run fill 32 80 0 47 80 15 "
                "biomesoplenty:unmapped_end_stone"
            ),
            "execute in minecraft:the_end run place feature biomesoplenty:anomaly 8 81 8",
            "execute in minecraft:the_end run place feature biomesoplenty:monolith 36 81 8",
        )
    if not re.fullmatch(r"[a-z][a-z0-9-]*", instance_name):
        parser.error("name must contain only lowercase letters, digits and hyphens")
    output = Path("evidence/raw/item10") / instance_name
    target = Path("instances/item10") / instance_name
    if output.exists() or target.exists():
        parser.error("diagnostic output and instance must both be absent")
    for name in ("JAVA_TOOL_OPTIONS", "JDK_JAVA_OPTIONS", "_JAVA_OPTIONS"):
        if os.environ.get(name):
            parser.error(f"undeclared inherited JVM options: {name}")
    java_home = Path("downloads/item2/temurin/extracted/jdk-21.0.12.1+1")
    java, version = validate_java_runtime(java_home)
    output.mkdir(parents=True)
    report: dict[str, object] = {
        "scope": (
            "full Item 10 collection; acceptance requires downstream validation"
            if preset == "item10"
            else "instrument diagnostic only; not density acceptance"
        ),
        "source_revision": subprocess.check_output(
            ["/usr/bin/git", "rev-parse", "HEAD"], text=True
        ).strip(),
        "mode": mode,
        "preset": preset,
        "arm": arm,
        "repetition": repetition,
        "fixture_commands": after_generation,
        "before_generation_commands": before_generation,
        "java_version": version,
        "java_tool_options": "",
    }
    if preset == "item10":
        report["attempt"] = attempt
    try:
        options = ""
        if mode == "probe":
            classes = output / "classes"
            classes.mkdir()
            source = Path("tools/Item10PlacementProbe.java")
            if preset == "item10" and sha256_file(source) != COLLECTOR_SOURCE_SHA256:
                detail = "full collection source differs from the frozen observer"
                raise ValueError(detail)  # noqa: TRY301 - retain the rejected build in the report.
            manifest = output / "probe.mf"
            _ = manifest.write_text(
                "Manifest-Version: 1.0\nPremain-Class: Item10PlacementProbe\n\n"
            )
            agent = output / "probe.jar"
            with (output / "build.log").open("x", encoding="utf-8") as log:
                _ = subprocess.run(  # noqa: S603 - pinned JDK, tracked source, fresh output.
                    [
                        str(java.with_name("javac")),
                        "--add-exports",
                        "java.base/jdk.internal.org.objectweb.asm=ALL-UNNAMED",
                        "-classpath",
                        str(classes),
                        "-Xlint:all",
                        "-Werror",
                        "-d",
                        str(classes),
                        str(source),
                    ],
                    check=True,
                    stdout=log,
                    stderr=subprocess.STDOUT,
                    timeout=45,
                )
                _ = subprocess.run(  # noqa: S603 - pinned JDK, tracked source, fresh output.
                    [
                        str(java.with_name("jar")),
                        "--create",
                        "--file",
                        str(agent),
                        "--manifest",
                        str(manifest),
                        "--date=2026-09-08T00:00:00Z",
                        "-C",
                        str(classes),
                        ".",
                    ],
                    check=True,
                    stdout=log,
                    stderr=subprocess.STDOUT,
                    timeout=45,
                )
            options = shlex.join(
                [
                    "--add-exports=java.base/jdk.internal.org.objectweb.asm=ALL-UNNAMED",
                    (
                        f"-javaagent:{os.path.relpath(agent, target)}="
                        f"{os.path.relpath(output / 'trace.jsonl', target)}"
                    ),
                ]
            )
            report["probe"] = {
                "source_sha256": sha256_file(source),
                "manifest_sha256": sha256_file(manifest),
                "jar_sha256": sha256_file(agent),
            }
            if preset == "item10" and sha256_file(agent) != COLLECTOR_JAR_SHA256:
                detail = "full collection JAR differs from the frozen observer"
                raise ValueError(detail)  # noqa: TRY301 - retain the rejected build in the report.
        report["java_tool_options"] = options
        request = WorldgenRequest(
            pristine=Path("instances/pristine-baseline-v0"),
            artifact_manifest=Path("evidence/item-3/artifact-acquisition-manifest.json"),
            retained_manifest=Path("evidence/item-3/runtime/retained-server-candidates.txt"),
            seed_suite=Path("test-environment/seed-suite.json"),
            frozen_config=Path("evidence/item-6/frozen"),
            frozen_manifest=Path("evidence/item-6/generated-config-manifest.json"),
            config_audit=Path("evidence/item-6/config-audit.json"),
            java_home=java_home,
            role=role,
            target=target,
            log_path=output / "console.log",
            captured_config=output / "captured-config",
            mode=preset,
            omit_sparse_structures=arm == "without-sparse",
            selections={
                "pilot": PILOT_SELECTIONS,
                "run": RUN_SELECTIONS,
                "item10": ITEM10_SELECTIONS,
            }[preset],
            timeout_seconds=14400 if preset == "item10" else 900,
        )
        run = execute(
            request,
            java_tool_options=options,
            after_generation=after_generation,
            before_generation=before_generation,
        )
        report["run"] = json.loads(run.model_dump_json())
        if run.rejection_reason:
            raise RuntimeError(run.rejection_reason)  # noqa: TRY301 - retain failure in report.
    except Exception as error:
        report["rejection_reason"] = f"{type(error).__name__}: {error}"
        raise
    finally:
        _ = (output / "diagnostic.json").write_text(json.dumps(report, indent=2) + "\n")


if __name__ == "__main__":
    main()
