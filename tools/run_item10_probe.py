"""Run a declared fresh-world placement diagnostic or its control."""

from __future__ import annotations

import argparse
import json
import os
import re
import shlex
import subprocess
from pathlib import Path
from typing import Literal, cast

from tools.run_item7_worldgen import execute

from mcpack_evidence.item7_runtime import WorldgenRequest, sha256_file, validate_java_runtime
from mcpack_evidence.item7_selections import PILOT_SELECTIONS, RUN_SELECTIONS


def main() -> None:  # noqa: PLR0915 - keep the one fixed diagnostic workflow together.
    """Record the observational overlay, then use the established lifecycle unchanged."""
    parser = argparse.ArgumentParser(description=__doc__)
    _ = parser.add_argument("--name", required=True)
    _ = parser.add_argument("--mode", choices=("probe", "control"), required=True)
    _ = parser.add_argument("--preset", choices=("pilot", "run"), default="run")
    _ = parser.add_argument("--betterend-fixture", action="store_true")
    _ = parser.add_argument(
        "--role",
        choices=("ordinary", "mountainous", "ocean-heavy", "biome-diverse"),
        default="ordinary",
    )
    args = parser.parse_args()
    instance_name = cast("str", args.name)
    mode = cast("str", args.mode)
    role = cast("str", args.role)
    preset = cast("Literal['pilot', 'run']", args.preset)
    fixture = cast("bool", args.betterend_fixture)
    if fixture and (mode != "probe" or preset != "pilot"):
        parser.error("the BetterEnd placement fixture requires probe mode and the pilot preset")
    before_generation = (
        ("execute in minecraft:the_end run forceload add -32 -32 47 47",) if fixture else ()
    )
    after_generation = (
        (
            "execute in minecraft:the_end run fill 0 80 0 15 80 15 minecraft:end_stone",
            "execute in minecraft:the_end if block 8 81 8 minecraft:air "
            "run say item10-fixture-air-true",
            "execute in minecraft:the_end unless block 8 81 8 minecraft:air "
            "run say item10-fixture-air-false",
            "execute in minecraft:the_end if block 8 80 8 #wover:surfaces/terrain "
            "run say item10-fixture-terrain-true",
            "execute in minecraft:the_end unless block 8 80 8 #wover:surfaces/terrain "
            "run say item10-fixture-terrain-false",
            (
                "execute in minecraft:the_end run place feature "
                "betterend:blossoming_spires_structures 8 81 8"
            ),
        )
        if fixture
        else ()
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
        "scope": "instrument diagnostic only; not density acceptance",
        "source_revision": subprocess.check_output(
            ["/usr/bin/git", "rev-parse", "HEAD"], text=True
        ).strip(),
        "mode": mode,
        "preset": preset,
        "fixture_commands": after_generation,
        "before_generation_commands": before_generation,
        "java_version": version,
        "java_tool_options": "",
    }
    try:
        options = ""
        if mode == "probe":
            classes = output / "classes"
            classes.mkdir()
            source = Path("tools/Item10PlacementProbe.java")
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
            selections=PILOT_SELECTIONS if preset == "pilot" else RUN_SELECTIONS,
            timeout_seconds=900,
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
