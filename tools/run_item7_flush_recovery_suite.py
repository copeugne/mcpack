#!/usr/bin/env python3
"""Run the complete source-bound Item 7 flush recovery suite."""

from __future__ import annotations

import argparse
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path
from typing import ClassVar

from pydantic import BaseModel, ConfigDict, Field

from mcpack_evidence.item7_flush_recovery_models import RECOVERY_TARGETS, RecoveryTarget


class _Arguments(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    project: Path
    restored: Path
    pristine: Path
    java_home: Path
    output: Path
    workers: int = Field(ge=1, le=4)
    timeout_seconds: int = Field(gt=0)


@dataclass(frozen=True, slots=True)
class _Result:
    key: str
    return_code: int
    stdout: str
    stderr: str


def build_parser() -> argparse.ArgumentParser:
    """Build the explicit 12-world suite surface."""
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("project", "restored", "pristine", "java-home", "output"):
        _ = parser.add_argument(f"--{name}", type=Path, required=True)
    _ = parser.add_argument("--workers", type=int, default=2)
    _ = parser.add_argument("--timeout-seconds", type=int, default=900)
    return parser


def _source_world(restored: Path, target: RecoveryTarget) -> Path:
    return restored / target.archive_group / target.archive_prefix.removesuffix("/")


def _run(arguments: _Arguments, target: RecoveryTarget) -> _Result:
    evidence = arguments.output / "raw" / target.evidence_root
    instance = arguments.output / "instances" / target.key.replace("/", "-")
    evidence.mkdir(parents=True)
    common = (
        "--pristine",
        arguments.pristine,
        "--artifact-manifest",
        arguments.project / "evidence/item-3/artifact-acquisition-manifest.json",
        "--retained-manifest",
        arguments.project / "evidence/item-3/runtime/retained-server-candidates.txt",
        "--seed-suite",
        arguments.project / "test-environment/seed-suite.json",
        "--frozen-config",
        arguments.project / "evidence/item-6/frozen",
        "--frozen-manifest",
        arguments.project / "evidence/item-6/generated-config-manifest.json",
        "--config-audit",
        arguments.project / "evidence/item-6/config-audit.json",
        "--java-home",
        arguments.java_home,
        "--source-world",
        _source_world(arguments.restored, target),
        "--world-inventory",
        arguments.project / "evidence/item-7/world-archive-inventory.json",
        "--target",
        instance,
        "--console-log",
        evidence / "console.log",
        "--receipt",
        evidence / "run-receipt.json",
    )
    command = [
        sys.executable,
        str(arguments.project / "tools/run_item7_flush_recovery.py"),
        "--runtime-kind",
        target.runtime_kind,
        "--role",
        target.role,
        "--world-key",
        target.key,
        *(str(value) for value in common),
        "--timeout-seconds",
        str(arguments.timeout_seconds),
    ]
    completed = subprocess.run(  # noqa: S603 - command is this repository's evidence tool.
        command,
        cwd=arguments.project,
        capture_output=True,
        text=True,
        check=False,
    )
    return _Result(target.key, completed.returncode, completed.stdout, completed.stderr)


def main() -> int:
    """Execute every declared recovery and fail if any receipt is rejected."""
    arguments = _Arguments.model_validate(vars(build_parser().parse_args()))
    if arguments.output.exists() or arguments.output.is_symlink():
        print(f"output must be absent: {arguments.output}", file=sys.stderr)
        return 2
    arguments.output.mkdir(parents=True)
    results: list[_Result] = []
    with ThreadPoolExecutor(max_workers=arguments.workers) as executor:
        futures = {executor.submit(_run, arguments, target): target for target in RECOVERY_TARGETS}
        for future in as_completed(futures):
            result = future.result()
            results.append(result)
            print(f"{result.key}: {'PASS' if result.return_code == 0 else 'FAIL'}", flush=True)
    failed = tuple(result for result in results if result.return_code != 0)
    for result in sorted(failed, key=lambda row: row.key):
        print(f"{result.key}\n{result.stdout}\n{result.stderr}", file=sys.stderr)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
