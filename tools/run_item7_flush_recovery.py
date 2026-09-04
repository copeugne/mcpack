#!/usr/bin/env python3
"""Run one source-bound Item 7 correlated flush recovery."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import ClassVar

from pydantic import BaseModel, ConfigDict

from mcpack_evidence.item7_completion_io import write_atomic
from mcpack_evidence.item7_flush_recovery import FlushRecoveryRequest, execute_recovery
from mcpack_evidence.item7_flush_recovery_models import RuntimeKind  # noqa: TC001
from mcpack_evidence.item7_runtime import WorldgenRequest
from mcpack_evidence.item7_selections import PILOT_SELECTIONS


class _Arguments(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    runtime_kind: RuntimeKind
    role: str
    world_key: str
    pristine: Path
    artifact_manifest: Path
    retained_manifest: Path
    seed_suite: Path
    frozen_config: Path
    frozen_manifest: Path
    config_audit: Path
    java_home: Path
    source_world: Path
    world_inventory: Path
    target: Path
    console_log: Path
    receipt: Path
    timeout_seconds: int


def build_parser() -> argparse.ArgumentParser:
    """Build the explicit single-world recovery surface."""
    parser = argparse.ArgumentParser(description=__doc__)
    _ = parser.add_argument("--runtime-kind", choices=("retained", "instrumented"), required=True)
    _ = parser.add_argument("--role", required=True)
    _ = parser.add_argument("--world-key", required=True)
    for name in (
        "pristine",
        "artifact-manifest",
        "retained-manifest",
        "seed-suite",
        "frozen-config",
        "frozen-manifest",
        "config-audit",
        "java-home",
        "source-world",
        "world-inventory",
        "target",
        "console-log",
        "receipt",
    ):
        _ = parser.add_argument(f"--{name}", type=Path, required=True)
    _ = parser.add_argument("--timeout-seconds", type=int, default=900)
    return parser


def main() -> int:
    """Execute and atomically preserve one accepted or rejected receipt."""
    arguments = _Arguments.model_validate(vars(build_parser().parse_args()))
    runtime = WorldgenRequest(
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
        log_path=arguments.console_log,
        captured_config=arguments.target.with_name(f"{arguments.target.name}-captured-unused"),
        mode="pilot",
        selections=PILOT_SELECTIONS,
        timeout_seconds=arguments.timeout_seconds,
    )
    receipt = execute_recovery(
        FlushRecoveryRequest(
            runtime=runtime,
            world_key=arguments.world_key,
            runtime_kind=arguments.runtime_kind,
            source_world=arguments.source_world,
            world_inventory=arguments.world_inventory,
            console_log=arguments.console_log,
        )
    )
    write_atomic(arguments.receipt, receipt)
    print(receipt.model_dump_json(indent=2))
    return 0 if receipt.rejection_reason is None else 1


if __name__ == "__main__":
    raise SystemExit(main())
