"""Run the fixed fresh-world scarecrow instrumentation diagnostic or its control."""

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


def main() -> None:
    """Record the observational overlay, then use the established lifecycle unchanged."""
    parser = argparse.ArgumentParser(description=__doc__)
    _ = parser.add_argument("--name", required=True)
    _ = parser.add_argument("--mode", choices=("probe", "control"), required=True)
    _ = parser.add_argument("--preset", choices=("pilot", "run"), default="run")
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
        run = execute(request, java_tool_options=options)
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
