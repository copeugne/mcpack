"""Run and preserve an ordinary-seed Item 7 structure-gap experiment."""

from __future__ import annotations

import argparse
import os
import tempfile
from pathlib import Path
from typing import TYPE_CHECKING, ClassVar, Literal

from pydantic import BaseModel, ConfigDict

from mcpack_evidence.item7_config import (
    OVERWORLD_CHUNKY_PATHS,
    ConfigCaptureReceipt,
    capture_runtime_configuration,
)
from mcpack_evidence.item7_gap import (
    GAP_TARGETS,
    GapError,
    GapLifecycleReceipt,
    GapRequest,
    GapTarget,
    run_gap_lifecycle,
)
from mcpack_evidence.item7_runtime import (
    Item7RuntimeError,
    PreflightReceipt,
    WorldgenRequest,
    prepare_worldgen,
    validate_java_runtime,
)
from mcpack_evidence.item7_selections import PILOT_SELECTIONS

if TYPE_CHECKING:
    from collections.abc import Sequence


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
    structure: list[str] | None = None


class GapRunReceipt(BaseModel):
    """Complete accepted or rejected structure-gap receipt."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True)
    schema_version: Literal["item7-gap-run-v1"] = "item7-gap-run-v1"
    preflight: PreflightReceipt | None
    lifecycle: GapLifecycleReceipt | None
    configuration: ConfigCaptureReceipt | None
    rejection_reason: str | None


def execute(request: GapRequest) -> GapRunReceipt:
    """Run the exact instrumented boundary and preserve each rejected state."""
    try:
        preflight = prepare_worldgen(request.runtime)
    except Item7RuntimeError as error:
        return GapRunReceipt(
            preflight=None, lifecycle=None, configuration=None, rejection_reason=str(error)
        )
    try:
        java_executable, _ = validate_java_runtime(request.runtime.java_home)
        lifecycle = run_gap_lifecycle(request, java_executable)
    except GapError as error:
        return GapRunReceipt(
            preflight=preflight, lifecycle=None, configuration=None, rejection_reason=str(error)
        )
    if not lifecycle.clean_stop:
        return GapRunReceipt(
            preflight=preflight,
            lifecycle=lifecycle,
            configuration=None,
            rejection_reason=lifecycle.rejection_reason,
        )
    try:
        configuration = capture_runtime_configuration(
            request.runtime, chunky_paths=OVERWORLD_CHUNKY_PATHS
        )
    except Item7RuntimeError as error:
        return GapRunReceipt(
            preflight=preflight,
            lifecycle=lifecycle,
            configuration=None,
            rejection_reason=str(error),
        )
    return GapRunReceipt(
        preflight=preflight, lifecycle=lifecycle, configuration=configuration, rejection_reason=None
    )


def build_parser() -> argparse.ArgumentParser:
    """Build the explicit ordinary-seed gap-run command surface."""
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
    _ = parser.add_argument(
        "--structure", action="append", help="Explicit target ID; repeat for each structure"
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Parse, execute, atomically publish, and print one receipt."""
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
    targets = (
        tuple(GapTarget(structure=identifier) for identifier in arguments.structure)
        if arguments.structure is not None
        else GAP_TARGETS
    )
    receipt = execute(GapRequest(runtime=runtime, targets=targets))
    _atomic_write(arguments.receipt, receipt.model_dump_json(indent=2) + "\n")
    print(receipt.model_dump_json(indent=2))
    return 0 if receipt.rejection_reason is None else 1


def _atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent, text=True)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
            _ = stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
        _ = Path(temporary).replace(path)
    except OSError:
        Path(temporary).unlink(missing_ok=True)
        raise


if __name__ == "__main__":
    raise SystemExit(main())
