#!/usr/bin/env python3
# ruff: noqa: EM101
"""Run the retained-136 Item 7 instrumentation control."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path
from typing import TYPE_CHECKING, ClassVar, Literal

from pydantic import BaseModel, ConfigDict

from mcpack_evidence.item6_validation import validate
from mcpack_evidence.item7_config import ConfigCaptureReceipt  # noqa: TC001
from mcpack_evidence.item7_control import (
    ControlError,
    ControlLifecycleReceipt,
    ControlRequest,
    capture_control_configuration,
    run_control_lifecycle,
)
from mcpack_evidence.item7_runtime import (
    CHUNKY_FILENAME,
    CONFIG_AUDIT_SHA256,
    FROZEN_MANIFEST_SHA256,
    RETAINED_COUNT,
    RETAINED_MANIFEST_SHA256,
    SEED_SUITE_SHA256,
    ArtifactHash,
    Item7RuntimeError,
    WorldgenRequest,
    replace_property,
    sha256_file,
    validate_java_runtime,
)
from mcpack_evidence.item7_selections import PILOT_SELECTIONS

if TYPE_CHECKING:
    from collections.abc import Sequence

_ROOT = Path(__file__).parents[1]


class ControlPreflightReceipt(BaseModel):
    """Frozen retained-runtime identity."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True)
    schema_version: Literal["item7-control-preflight-v1"] = "item7-control-preflight-v1"
    seed: Literal["42"]
    java_version: str
    candidate_count: Literal[136]
    runtime_sha256: str
    retained_manifest_sha256: str
    frozen_manifest_sha256: str
    config_audit_sha256: str
    seed_suite_sha256: str


class _Materialization(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="ignore")
    seed: Literal["42"]


class _Arguments(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")
    pristine: Path
    artifact_manifest: Path
    retained_manifest: Path
    seed_suite: Path
    frozen_config: Path
    frozen_manifest: Path
    config_audit: Path
    java_home: Path
    target: Path
    log_path: Path
    captured_config: Path
    receipt: Path
    timeout_seconds: int
    settle_seconds: float


class ControlRunReceipt(BaseModel):
    """Complete accepted or rejected control receipt."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True)
    schema_version: str = "item7-control-run-v1"
    preflight: ControlPreflightReceipt | None
    lifecycle: ControlLifecycleReceipt | None
    configuration: ConfigCaptureReceipt | None
    rejection_reason: str | None


def prepare_control(request: ControlRequest) -> ControlPreflightReceipt:
    """Materialize the exact retained set and apply the frozen configuration."""
    run = request.runtime
    if run.target.exists() or run.target.is_symlink():
        raise ControlError("preflight", f"target must be absent: {run.target}")
    try:
        identities = (
            _identity(run.retained_manifest, RETAINED_MANIFEST_SHA256, "retained manifest"),
            _identity(run.frozen_manifest, FROZEN_MANIFEST_SHA256, "frozen manifest"),
            _identity(run.config_audit, CONFIG_AUDIT_SHA256, "config audit"),
            _identity(run.seed_suite, SEED_SUITE_SHA256, "seed suite"),
        )
        retained = _retained_names(run.retained_manifest)
        _, java_version = validate_java_runtime(run.java_home)
        validate(run.frozen_config, run.frozen_manifest, run.config_audit)
        seed = _materialize(run).seed
        _apply_frozen(run, seed)
        hashes = _hash_mods(run.target / "mods", retained)
    except ControlError as error:
        raise ControlError("preflight", error.detail) from error
    except (OSError, ValueError) as error:
        raise ControlError("preflight", str(error)) from error
    return ControlPreflightReceipt(
        seed=seed,
        java_version=java_version,
        candidate_count=RETAINED_COUNT,
        runtime_sha256=_hash_rows(hashes),
        retained_manifest_sha256=identities[0],
        frozen_manifest_sha256=identities[1],
        config_audit_sha256=identities[2],
        seed_suite_sha256=identities[3],
    )


def _materialize(run: WorldgenRequest) -> _Materialization:
    command = [sys.executable, str(_ROOT / "tools/manage_item4_environment.py"), "materialize"]
    for flag, value in (
        ("--pristine", run.pristine),
        ("--artifact-manifest", run.artifact_manifest),
        ("--retained-manifest", run.retained_manifest),
        ("--seed-suite", run.seed_suite),
        ("--role", run.role),
        ("--target", run.target),
    ):
        command.extend((flag, str(value)))
    completed = subprocess.run(  # noqa: S603
        command, cwd=_ROOT, capture_output=True, text=True, check=False
    )
    if completed.returncode != 0:
        raise ControlError("preflight", completed.stderr.strip())
    return _Materialization.model_validate_json(completed.stdout)


def _retained_names(path: Path) -> tuple[str, ...]:
    names = tuple(path.read_text(encoding="utf-8").splitlines())
    if len(names) != RETAINED_COUNT or len(set(names)) != RETAINED_COUNT:
        raise ControlError("preflight", "retained manifest must contain exactly 136 unique JARs")
    return names


def _apply_frozen(run: WorldgenRequest, seed: str) -> None:
    def omit_secret(directory: str, names: list[str]) -> set[str]:
        del names
        source = run.frozen_config / "config"
        return {"resourceful-config-web.json"} if Path(directory) == source else set()

    for name in ("config", "defaultconfigs"):
        destination = run.target / name
        if destination.exists():
            shutil.rmtree(destination)
        _ = shutil.copytree(run.frozen_config / name, destination, ignore=omit_secret)
    content = run.frozen_config.joinpath("server.properties").read_bytes()
    _ = run.target.joinpath("server.properties").write_bytes(
        replace_property(content, "level-seed", seed)
    )


def _identity(path: Path, expected: str, label: str) -> str:
    try:
        observed = sha256_file(path)
    except OSError as error:
        raise ControlError("preflight", f"{label} identity could not be read: {error}") from error
    if observed != expected:
        raise ControlError("preflight", f"{label} identity differs from the frozen Item 7 input")
    return observed


def _hash_mods(mods: Path, expected: tuple[str, ...]) -> tuple[ArtifactHash, ...]:
    names = tuple(sorted(path.name for path in mods.glob("*.jar")))
    if names != tuple(sorted(expected)) or CHUNKY_FILENAME in names:
        raise ControlError("preflight", "runtime JAR filenames differ from retained identity")
    return tuple(ArtifactHash(path=name, sha256=sha256_file(mods / name)) for name in names)


def _hash_rows(rows: tuple[ArtifactHash, ...]) -> str:
    payload = tuple((row.path, row.sha256) for row in rows)
    return hashlib.sha256(json.dumps(payload, separators=(",", ":")).encode()).hexdigest()


def execute(request: ControlRequest) -> ControlRunReceipt:
    """Run the three evidence boundaries without losing a rejected receipt."""
    try:
        preflight = prepare_control(request)
    except ControlError as error:
        return ControlRunReceipt(
            preflight=None, lifecycle=None, configuration=None, rejection_reason=str(error)
        )
    try:
        java, _ = validate_java_runtime(request.runtime.java_home)
        lifecycle = run_control_lifecycle(request, java)
    except Item7RuntimeError as error:
        return ControlRunReceipt(
            preflight=preflight, lifecycle=None, configuration=None, rejection_reason=str(error)
        )
    if not lifecycle.clean_stop:
        return ControlRunReceipt(
            preflight=preflight,
            lifecycle=lifecycle,
            configuration=None,
            rejection_reason=lifecycle.rejection_reason,
        )
    try:
        configuration = capture_control_configuration(request)
    except ControlError as error:
        return ControlRunReceipt(
            preflight=preflight,
            lifecycle=lifecycle,
            configuration=None,
            rejection_reason=str(error),
        )
    return ControlRunReceipt(
        preflight=preflight,
        lifecycle=lifecycle,
        configuration=configuration,
        rejection_reason=None,
    )


def build_parser() -> argparse.ArgumentParser:
    """Build the pilot-only command surface."""
    parser = argparse.ArgumentParser()
    for name in (
        "pristine",
        "artifact-manifest",
        "retained-manifest",
        "seed-suite",
        "frozen-config",
        "frozen-manifest",
        "config-audit",
        "java-home",
        "target",
        "log-path",
        "captured-config",
        "receipt",
    ):
        _ = parser.add_argument(f"--{name}", type=Path, required=True)
    _ = parser.add_argument("--timeout-seconds", type=int, default=900)
    _ = parser.add_argument("--settle-seconds", type=float, default=30)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Parse, execute, and durably write the receipt."""
    arguments = _Arguments.model_validate(vars(build_parser().parse_args(argv)))
    runtime = WorldgenRequest(
        pristine=arguments.pristine,
        artifact_manifest=arguments.artifact_manifest,
        retained_manifest=arguments.retained_manifest,
        seed_suite=arguments.seed_suite,
        frozen_config=arguments.frozen_config,
        frozen_manifest=arguments.frozen_manifest,
        config_audit=arguments.config_audit,
        java_home=arguments.java_home,
        role="ordinary",
        target=arguments.target,
        log_path=arguments.log_path,
        captured_config=arguments.captured_config,
        selections=PILOT_SELECTIONS,
        timeout_seconds=arguments.timeout_seconds,
    )
    receipt = execute(ControlRequest(runtime=runtime, settle_seconds=arguments.settle_seconds))
    arguments.receipt.parent.mkdir(parents=True, exist_ok=True)
    _ = arguments.receipt.write_text(receipt.model_dump_json(indent=2) + "\n", encoding="utf-8")
    print(receipt.model_dump_json(indent=2))
    return 0 if receipt.rejection_reason is None else 1


if __name__ == "__main__":
    raise SystemExit(main())
