"""Reopen archived Item 7 worlds and prove one correlated flush."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path, PurePosixPath
from typing import ClassVar

from pydantic import BaseModel, ConfigDict, model_validator

from mcpack_evidence.item7_archive_io import (
    OpenedFile,
    UnsafeFilesystemError,
    duplicate_stream,
    open_tree,
    sha256_descriptor,
)
from mcpack_evidence.item7_archive_models import FileIdentity
from mcpack_evidence.item7_flush_recovery_lifecycle import run_recovery_lifecycle
from mcpack_evidence.item7_flush_recovery_models import (
    FlushRecoveryReceipt,
    RuntimeIdentity,
    RuntimeKind,
    WorldSourceIdentity,
    recovery_target,
    world_source_identity,
)
from mcpack_evidence.item7_runtime import (
    CHUNKY_FILENAME,
    Item7RuntimeError,
    PreflightReceipt,
    WorldgenRequest,
    prepare_worldgen,
    sha256_file,
    validate_java_runtime,
)
from mcpack_evidence.item7_stage_output import StageOutputError, staging_tree


class FlushRecoveryRequest(BaseModel):
    """All immutable inputs and disposable outputs for one recovery run."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    runtime: WorldgenRequest
    world_key: str
    runtime_kind: RuntimeKind
    source_world: Path
    world_inventory: Path
    console_log: Path

    @model_validator(mode="after")
    def require_declared_identity(self) -> FlushRecoveryRequest:
        """Require the key, role, and runtime identity declared by the suite."""
        target = recovery_target(self.world_key)
        if (self.runtime.role, self.runtime_kind) != (target.role, target.runtime_kind):
            detail = f"recovery runtime identity differs: {self.world_key}"
            raise ValueError(detail)
        return self


def execute_recovery(request: FlushRecoveryRequest) -> FlushRecoveryReceipt:
    """Materialize, verify, reopen, flush, and stop one archived world."""
    preflight = None
    runtime = None
    source = None
    lifecycle = None
    try:
        preflight = prepare_worldgen(request.runtime)
        if request.runtime_kind == "retained":
            request.runtime.target.joinpath("mods", CHUNKY_FILENAME).unlink()
        runtime = _runtime_identity(request, preflight)
        source = _copy_verified_world(request)
        java, _ = validate_java_runtime(request.runtime.java_home)
        lifecycle = run_recovery_lifecycle(request, java)
    except (
        Item7RuntimeError,
        OSError,
        StageOutputError,
        UnsafeFilesystemError,
        ValueError,
    ) as error:
        return FlushRecoveryReceipt(
            runtime_kind=request.runtime_kind,
            role=request.runtime.role,
            preflight=preflight,
            runtime=runtime,
            source=source,
            lifecycle=lifecycle,
            rejection_reason=str(error),
        )
    rejection = lifecycle.rejection_reason
    return FlushRecoveryReceipt(
        runtime_kind=request.runtime_kind,
        role=request.runtime.role,
        preflight=preflight,
        runtime=runtime,
        source=source,
        lifecycle=lifecycle,
        rejection_reason=rejection,
    )


def _runtime_identity(
    request: FlushRecoveryRequest, preflight: PreflightReceipt
) -> RuntimeIdentity:
    rows = tuple(
        (path.name, sha256_file(path))
        for path in sorted(request.runtime.target.joinpath("mods").glob("*.jar"))
    )
    observed = hashlib.sha256(json.dumps(rows, separators=(",", ":")).encode()).hexdigest()
    count = 136 if request.runtime_kind == "retained" else 137
    expected = (
        preflight.retained_runtime_sha256
        if request.runtime_kind == "retained"
        else preflight.instrumented_runtime_sha256
    )
    if len(rows) != count or observed != expected:
        detail = f"recovery runtime differs: {request.world_key}"
        raise ValueError(detail)
    return RuntimeIdentity(candidate_count=count, runtime_sha256=observed)


def _copy_verified_world(request: FlushRecoveryRequest) -> WorldSourceIdentity:
    target = recovery_target(request.world_key)
    identity, expected = world_source_identity(request.world_inventory, target)
    destination = request.runtime.target / "world"
    if destination.exists() or destination.is_symlink():
        detail = f"recovery world target must be absent: {destination}"
        raise ValueError(detail)
    with open_tree(request.source_world) as opened:
        if _file_identities(opened) != expected:
            detail = f"recovery source world differs: {request.world_key}"
            raise ValueError(detail)
        with staging_tree(destination) as output:
            for row in opened:
                with duplicate_stream(row.descriptor) as stream:
                    output.write(PurePosixPath(row.relative_path), stream, row.size_bytes)
            output.publish()
    with open_tree(destination) as copied:
        if _file_identities(copied) != expected:
            detail = f"recovery world copy differs: {request.world_key}"
            raise ValueError(detail)
    return identity


def _file_identities(opened: tuple[OpenedFile, ...]) -> tuple[FileIdentity, ...]:
    return tuple(
        FileIdentity(
            relative_path=row.relative_path,
            size_bytes=row.size_bytes,
            sha256=sha256_descriptor(row.descriptor),
        )
        for row in opened
    )
