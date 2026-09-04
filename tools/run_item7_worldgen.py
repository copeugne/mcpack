#!/usr/bin/env python3
"""Run one isolated Item 7 Chunky world-generation lifecycle."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import ClassVar, Literal

from pydantic import BaseModel, ConfigDict

from mcpack_evidence.item7_config import ConfigCaptureReceipt, capture_runtime_configuration
from mcpack_evidence.item7_lifecycle import LifecycleReceipt, run_lifecycle
from mcpack_evidence.item7_runtime import (
    Item7RuntimeError,
    PreflightReceipt,
    WorldgenRequest,
    prepare_worldgen,
    validate_java_runtime,
)
from mcpack_evidence.item7_selections import PILOT_SELECTIONS, RUN_SELECTIONS


class _Arguments(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    mode: Literal["pilot", "run"]
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
    role: str
    timeout_seconds: int


class RunReceipt(BaseModel):
    """Complete accepted or rejected receipt for one seed run."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True)

    schema_version: Literal["item7-worldgen-run-v1"] = "item7-worldgen-run-v1"
    preflight: PreflightReceipt | None
    lifecycle: LifecycleReceipt | None
    configuration: ConfigCaptureReceipt | None
    rejection_reason: str | None


def execute(request: WorldgenRequest) -> RunReceipt:
    """Run preflight, lifecycle, and sanitized configuration capture."""
    try:
        preflight = prepare_worldgen(request)
    except Item7RuntimeError as error:
        return RunReceipt(
            preflight=None,
            lifecycle=None,
            configuration=None,
            rejection_reason=str(error),
        )
    try:
        java_executable, _ = validate_java_runtime(request.java_home)
        lifecycle = run_lifecycle(request, java_executable)
    except Item7RuntimeError as error:
        return RunReceipt(
            preflight=preflight,
            lifecycle=None,
            configuration=None,
            rejection_reason=str(error),
        )
    if not lifecycle.clean_stop:
        return RunReceipt(
            preflight=preflight,
            lifecycle=lifecycle,
            configuration=None,
            rejection_reason=lifecycle.rejection_reason,
        )
    try:
        configuration = capture_runtime_configuration(request)
    except Item7RuntimeError as error:
        return RunReceipt(
            preflight=preflight,
            lifecycle=lifecycle,
            configuration=None,
            rejection_reason=str(error),
        )
    return RunReceipt(
        preflight=preflight,
        lifecycle=lifecycle,
        configuration=configuration,
        rejection_reason=None,
    )


def main() -> int:
    """Parse one run request and always preserve its receipt."""
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="mode", required=True)
    for mode in ("pilot", "run"):
        command_parser = subparsers.add_parser(mode)
        _add_run_arguments(command_parser)
    arguments = _Arguments.model_validate(vars(parser.parse_args()))
    selections = PILOT_SELECTIONS if arguments.mode == "pilot" else RUN_SELECTIONS
    request = WorldgenRequest(
        pristine=arguments.pristine,
        artifact_manifest=arguments.artifact_manifest,
        retained_manifest=arguments.retained_manifest,
        seed_suite=arguments.seed_suite,
        frozen_config=arguments.frozen_config,
        frozen_manifest=arguments.frozen_manifest,
        config_audit=arguments.config_audit,
        java_home=arguments.java_home,
        role=arguments.role,
        target=arguments.target,
        log_path=arguments.log_path,
        captured_config=arguments.captured_config,
        mode=arguments.mode,
        selections=selections,
        timeout_seconds=arguments.timeout_seconds,
    )
    try:
        receipt = execute(request)
    except Item7RuntimeError as error:
        receipt = RunReceipt(
            preflight=None,
            lifecycle=None,
            configuration=None,
            rejection_reason=str(error),
        )
    arguments.receipt.parent.mkdir(parents=True, exist_ok=True)
    _ = arguments.receipt.write_text(receipt.model_dump_json(indent=2) + "\n", encoding="utf-8")
    print(receipt.model_dump_json(indent=2))
    return 0 if receipt.rejection_reason is None else 1


def _add_run_arguments(parser: argparse.ArgumentParser) -> None:
    """Add the shared evidence-bound inputs for one preset."""
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
    _ = parser.add_argument("--role", required=True)
    _ = parser.add_argument("--timeout-seconds", type=int, default=900)


if __name__ == "__main__":
    raise SystemExit(main())
