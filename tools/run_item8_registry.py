"""Materialize and capture Item 8 registry evidence. Run with uv run -m tools.run_item8_registry."""

from __future__ import annotations

import argparse
import json
import shutil
import socket
import subprocess
from datetime import UTC, datetime
from pathlib import Path
from typing import ClassVar

from pydantic import BaseModel, ConfigDict, Field, JsonValue
from tools.run_item7_control import prepare_control

from mcpack_evidence.item7_control import ControlRequest, capture_control_configuration
from mcpack_evidence.item7_runtime import (
    Item7RuntimeError,
    WorldgenRequest,
    sha256_file,
    validate_java_runtime,
)
from mcpack_evidence.item7_selections import PILOT_SELECTIONS
from mcpack_evidence.item8_registry import (
    REGISTRIES,
    read_registry,
    registry_relative_path,
    run_registry_lifecycle,
)

ROOT = Path(__file__).resolve().parents[1]


class Arguments(BaseModel):
    """Explicit, disposable runtime paths."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid", strict=True)
    pristine: Path
    java_home: Path
    target: Path
    output: Path
    timeout_seconds: int = Field(gt=0)
    exit_timeout_seconds: int = Field(default=120, gt=0)
    dimension_biomes: bool = False


def check_ports(properties: Path) -> None:
    """Refuse a conflicting game port without changing the frozen network configuration."""
    values = dict(
        line.split("=", 1)
        for line in properties.read_text(encoding="utf-8").splitlines()
        if line and not line.startswith("#") and "=" in line
    )
    if values.get("enable-rcon") != "false" or values.get("enable-query") != "false":
        message = "Item 8 expects the frozen disabled RCON and query interfaces"
        raise ValueError(message)
    port = int(values["server-port"])
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as probe:
        probe.bind(("0.0.0.0", port))  # noqa: S104 - availability check only; never listens.


def capture(arguments: Arguments) -> dict[str, JsonValue]:  # noqa: C901, PLR0915 - probe build and receipt share capture cleanup.
    """Reuse the retained-136 preflight and configuration audit, preserving failures."""
    if any(path.is_symlink() for path in (arguments.output, *arguments.output.parents)):
        message = "capture output must not traverse a symlink"
        raise ValueError(message)
    output = arguments.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    report: dict[str, JsonValue] = {
        "schema_version": "item8-registry-capture-v1",
        "started_at": datetime.now(UTC).isoformat(),
        "source_revision": subprocess.check_output(
            ["git", "rev-parse", "HEAD"],  # noqa: S607 - fixed read-only Git.
            cwd=ROOT,
            text=True,
        ).strip(),
        "preflight": None,
        "lifecycle": None,
        "configuration": None,
        "registries": {},
        "rejection_reason": "capture did not finish",
        "timeout_seconds": arguments.timeout_seconds,
        "exit_timeout_seconds": arguments.exit_timeout_seconds,
    }
    request = ControlRequest(
        runtime=WorldgenRequest(
            pristine=arguments.pristine.resolve(),
            artifact_manifest=ROOT / "evidence/item-3/artifact-acquisition-manifest.json",
            retained_manifest=ROOT / "evidence/item-3/runtime/retained-server-candidates.txt",
            seed_suite=ROOT / "test-environment/seed-suite.json",
            frozen_config=ROOT / "evidence/item-6/frozen",
            frozen_manifest=ROOT / "evidence/item-6/generated-config-manifest.json",
            config_audit=ROOT / "evidence/item-6/config-audit.json",
            java_home=arguments.java_home.resolve(),
            role="ordinary",
            target=arguments.target.resolve(),
            log_path=output / "console.log",
            captured_config=output / "configuration",
            selections=PILOT_SELECTIONS,
            timeout_seconds=arguments.timeout_seconds,
        ),
        settle_seconds=0,
    )
    try:
        dirty = subprocess.check_output(
            ["git", "status", "--porcelain", "--untracked-files=no"],  # noqa: S607
            cwd=ROOT,
            text=True,
        ).strip()
        if dirty:
            message = "commit tracked changes before collecting runtime evidence"
            raise ValueError(message)  # noqa: TRY301 - preserve a rejected receipt.
        preflight = prepare_control(request)
        report["preflight"] = json.loads(preflight.model_dump_json())
        check_ports(request.runtime.target / "server.properties")
        java, _ = validate_java_runtime(request.runtime.java_home)
        probe: Path | None = None
        if arguments.dimension_biomes:
            classes = output / "dimension-probe-classes"
            classes.mkdir()
            probe = output / "dimension-probe.jar"
            source = ROOT / "tools/Item8DimensionProbe.java"
            manifest = ROOT / "tools/Item8DimensionProbe.mf"
            report["dimension_probe"] = {
                "source_sha256": sha256_file(source),
                "manifest_sha256": sha256_file(manifest),
            }
            with (output / "dimension-probe-build.log").open("x", encoding="utf-8") as build_log:
                for command in (
                    [str(java.with_name("javac")), "-classpath", str(classes), "-Xlint:all",
                     "-Werror", "-d", str(classes), str(source)],
                    [str(java.with_name("jar")), "--create", "--file", str(probe),
                     "--manifest", str(manifest), "--date=2026-09-05T00:00:00Z",
                     "-C", str(classes), "."],
                ):
                    _ = subprocess.run(  # noqa: S603 - pinned JDK, tracked source, fresh output.
                        command, stdout=build_log, stderr=subprocess.STDOUT, check=True, timeout=45
                    )
            report["dimension_probe"] = {
                "source_sha256": sha256_file(source),
                "manifest_sha256": sha256_file(manifest),
                "jar_sha256": sha256_file(probe),
            }
        lifecycle = run_registry_lifecycle(
            request.runtime.target,
            java,
            request.runtime.log_path,
            arguments.timeout_seconds,
            arguments.exit_timeout_seconds,
            dimension_probe=probe,
        )
        report["lifecycle"] = json.loads(lifecycle.model_dump_json())
        if not lifecycle.clean_stop:
            message = lifecycle.rejection_reason or "registry lifecycle rejected"
            raise ValueError(message)  # noqa: TRY301 - emit the rejected capture receipt.
        if arguments.dimension_biomes:
            report["dimension_biomes_sha256"] = sha256_file(output / "dimension-biomes.json")
        configuration = capture_control_configuration(request)
        report["configuration"] = json.loads(configuration.model_dump_json())
        registries: dict[str, JsonValue] = {}
        for registry in REGISTRIES:
            relative = registry_relative_path(registry)
            source = request.runtime.target / relative
            entries = read_registry(source)
            destination = output / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            _ = shutil.copyfile(source, destination)
            registries[registry] = {
                "path": relative,
                "count": len(entries),
                "size_bytes": destination.stat().st_size,
                "sha256": sha256_file(destination),
            }
        report["registries"] = registries
        report["rejection_reason"] = None
    except (OSError, ValueError, Item7RuntimeError, subprocess.SubprocessError) as error:
        report["rejection_reason"] = str(error)
    finally:
        for name in ("latest.log", "debug.log"):
            source = request.runtime.target / "logs" / name
            if report["preflight"] is not None and source.is_file():
                _ = shutil.copyfile(source, output / name)
        report["finished_at"] = datetime.now(UTC).isoformat()
        _ = (output / "capture.json").write_text(
            json.dumps(report, indent=2) + "\n", encoding="utf-8"
        )
    return report


def main() -> int:
    """Capture a fresh runtime; refuse output or instance reuse."""
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("pristine", "java-home", "target", "output"):
        _ = parser.add_argument(f"--{name}", type=Path, required=True)
    _ = parser.add_argument("--timeout-seconds", type=int, default=900)
    _ = parser.add_argument("--exit-timeout-seconds", type=int, default=120)
    _ = parser.add_argument("--dimension-biomes", action="store_true")
    arguments = Arguments.model_validate(vars(parser.parse_args()), strict=True)
    report = capture(arguments)
    print(json.dumps(report, indent=2))
    return 0 if report["rejection_reason"] is None else 1


if __name__ == "__main__":
    raise SystemExit(main())
