"""Run the bounded saved-view collision probe on a fresh frozen runtime."""

# pyright: standard
# ruff: noqa: D103, EM101, TRY003, INP001, S603, S607, TRY301
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import time
from pathlib import Path

from tools.run_item7_control import prepare_control
from tools.run_item8_registry import check_ports

from mcpack_evidence.item7_control import ControlRequest, capture_control_configuration
from mcpack_evidence.item7_runtime import WorldgenRequest, sha256_file, validate_java_runtime
from mcpack_evidence.item7_selections import PILOT_SELECTIONS
from mcpack_evidence.item8_registry import run_registry_lifecycle

ROOT = Path(__file__).resolve().parents[3]
INPUT = ROOT / "evidence/item-13/fixed-blocks/mns-medium-house.json.gz"
INPUT_HASH = "a61dc454a22b0058d765da277fbd6c7e450dc597f1ff8b42da66b288247e7496"


def run(  # noqa: C901 - preserve one experiment and its failure.
    output: Path, target: Path, *, spawner_lookup: bool = False, second_house: bool = False
) -> None:
    input_file = (
        ROOT / "evidence/item-13/fixed-blocks/mns-medium_house_2.json.gz" if second_house else INPUT
    )
    input_hash = (
        "c1fa53cbbae3cc48f56a48baacdfd80746bd937662a57db35d49f98b698447a6"
        if second_house
        else INPUT_HASH
    )
    for path in (output, target):
        if path.exists() or any(part.is_symlink() for part in (path, *path.parents)):
            raise ValueError("Output and instance must be new paths without symlinks")
    if sha256_file(input_file) != input_hash:
        raise ValueError("Saved house input hash mismatch")
    if shutil.disk_usage(ROOT).free < 5 * 1024**3:
        raise ValueError("Probe requires at least 5 GiB free")
    dirty = subprocess.check_output(
        ["git", "status", "--porcelain", "--untracked-files=no"], cwd=ROOT, text=True
    ).strip()
    if dirty:
        raise ValueError("Commit tracked changes before runtime evidence collection")
    output.mkdir(parents=True)
    started = time.monotonic()
    report: dict[str, object] = {
        "source_revision": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
        ).strip(),
        "input_sha256": input_hash,
        "rejection_reason": "capture did not finish",
    }
    request = ControlRequest(
        runtime=WorldgenRequest(
            pristine=ROOT / "instances/pristine-baseline-v0",
            artifact_manifest=ROOT / "evidence/item-3/artifact-acquisition-manifest.json",
            retained_manifest=ROOT / "evidence/item-3/runtime/retained-server-candidates.txt",
            seed_suite=ROOT / "test-environment/seed-suite.json",
            frozen_config=ROOT / "evidence/item-6/frozen",
            frozen_manifest=ROOT / "evidence/item-6/generated-config-manifest.json",
            config_audit=ROOT / "evidence/item-6/config-audit.json",
            java_home=ROOT / "downloads/item2/temurin/extracted/jdk-21.0.12.1+1",
            role="ordinary",
            target=target,
            log_path=output / "console.log",
            captured_config=output / "configuration",
            selections=PILOT_SELECTIONS,
            timeout_seconds=600,
        ),
        settle_seconds=0,
    )
    try:
        report["preflight"] = json.loads(prepare_control(request).model_dump_json())
        check_ports(target / "server.properties")
        java, _ = validate_java_runtime(request.runtime.java_home)
        classes = output / "classes"
        classes.mkdir()
        probe = output / "probe.jar"
        sources = [
            ROOT / "tools/Item8DimensionProbe.java",
            Path(__file__).with_name("Item13CollisionProbe.java"),
        ]
        manifest = Path(__file__).with_name("manifest.mf")
        with (output / "build.log").open("x") as log:
            for command in (
                [
                    str(java.with_name("javac")),
                    "-classpath",
                    str(classes),
                    "-Xlint:all",
                    "-Werror",
                    "-d",
                    str(classes),
                    *(str(source) for source in sources),
                ],
                [
                    str(java.with_name("jar")),
                    "--create",
                    "--file",
                    str(probe),
                    "--manifest",
                    str(manifest),
                    "--date=2026-09-09T00:00:00Z",
                    "-C",
                    str(classes),
                    ".",
                ],
            ):
                subprocess.run(
                    command, stdout=log, stderr=subprocess.STDOUT, check=True, timeout=45
                )
        report["probe_sha256"] = sha256_file(probe)
        shutil.copyfile(input_file, output / "input.json.gz")
        projection = "spawners.json" if spawner_lookup else "collision.json"
        lifecycle = run_registry_lifecycle(
            target,
            java,
            output / "console.log",
            600,
            dimension_probe=probe,
            registries=(),
            probe_output_name=projection,
        )
        report["lifecycle"] = json.loads(lifecycle.model_dump_json())
        if not lifecycle.clean_stop:
            raise ValueError(lifecycle.rejection_reason or "Unclean collision capture")
        report["configuration"] = json.loads(
            capture_control_configuration(request).model_dump_json()
        )
        report["spawners_sha256" if spawner_lookup else "collision_sha256"] = sha256_file(
            output / projection
        )
        report["rejection_reason"] = None
    except Exception as error:
        report["rejection_reason"] = str(error)
        raise
    finally:
        report["elapsed_seconds"] = round(time.monotonic() - started, 3)
        for name in ("latest.log", "debug.log"):
            source = target / "logs" / name
            if source.is_file():
                shutil.copyfile(source, output / name)
        (output / "capture.json").write_text(json.dumps(report, indent=2) + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    parser.add_argument("target", type=Path)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--spawner-lookup", action="store_true")
    mode.add_argument("--second-house", action="store_true")
    args = parser.parse_args()
    run(
        args.output.absolute(),
        args.target.absolute(),
        spawner_lookup=args.spawner_lookup,
        second_house=args.second_house,
    )
