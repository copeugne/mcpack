"""Identity models for correlated Item 7 world flush recovery."""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path  # noqa: TC003
from typing import ClassVar, Final, Literal

from pydantic import BaseModel, ConfigDict

from mcpack_evidence.item7_archive_models import FileIdentity
from mcpack_evidence.item7_completion_io import sha256_file, strict_model
from mcpack_evidence.item7_runtime import PreflightReceipt  # noqa: TC001
from mcpack_evidence.item7_world_archive_inventory import WorldArchiveInventory

type RuntimeKind = Literal["retained", "instrumented"]


@dataclass(frozen=True, slots=True)
class RecoveryTarget:
    """One archived world and the runtime identity that produced it."""

    key: str
    archive_group: Literal["run-a", "run-b", "auxiliary"]
    archive_prefix: str
    role: str
    runtime_kind: RuntimeKind

    @property
    def evidence_root(self) -> str:
        """Return the portable raw-evidence directory for this recovery."""
        return f"flush-recovery/{self.key}"


RECOVERY_TARGETS: Final = (
    *(
        RecoveryTarget(
            f"{run}/{role}",
            run,
            f"{run}-{role}/world/",
            role,
            "instrumented",
        )
        for run in ("run-a", "run-b")
        for role in ("ordinary", "mountainous", "ocean-heavy", "biome-diverse")
    ),
    RecoveryTarget(
        "control/ordinary", "auxiliary", "control-ordinary/world/", "ordinary", "retained"
    ),
    RecoveryTarget(
        "gap-a/ordinary", "auxiliary", "gap-a-ordinary/world/", "ordinary", "instrumented"
    ),
    RecoveryTarget(
        "gap-b/ordinary", "auxiliary", "gap-b-ordinary/world/", "ordinary", "instrumented"
    ),
    RecoveryTarget(
        "pilot/ordinary-success",
        "auxiliary",
        "pilot-tracked-ordinary-success/world/",
        "ordinary",
        "instrumented",
    ),
)


class _StrictModel(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid", strict=True)


class WorldSourceIdentity(_StrictModel):
    """Portable identity for one world subset in the complete world inventory."""

    world_key: str
    inventory_path: str
    inventory_size_bytes: int
    inventory_sha256: str
    file_count: int
    total_size_bytes: int
    tree_sha256: str


class RuntimeIdentity(_StrictModel):
    """Observed runtime JAR set immediately before server launch."""

    candidate_count: int
    runtime_sha256: str


class RecoveryLifecycle(_StrictModel):
    """Observed response-gated flush and clean process exit."""

    ready: bool
    save_all_flush: bool
    clean_stop: bool
    return_code: int
    commands: tuple[str, ...]
    console_log: str
    console_log_size_bytes: int
    console_log_sha256: str
    minecraft_log: str
    minecraft_log_size_bytes: int
    minecraft_log_sha256: str
    duration_seconds: float
    process_group_killed: bool
    rejection_reason: str | None


class FlushRecoveryReceipt(_StrictModel):
    """Complete runtime, source-world, and lifecycle recovery evidence."""

    schema_version: Literal["item7-flush-recovery-v1"] = "item7-flush-recovery-v1"
    runtime_kind: RuntimeKind
    role: str
    preflight: PreflightReceipt | None
    runtime: RuntimeIdentity | None
    source: WorldSourceIdentity | None
    lifecycle: RecoveryLifecycle | None
    rejection_reason: str | None


def recovery_target(key: str) -> RecoveryTarget:
    """Resolve one declared recovery target or fail closed."""
    matches = tuple(target for target in RECOVERY_TARGETS if target.key == key)
    if len(matches) != 1:
        detail = f"unknown Item 7 recovery world key: {key}"
        raise ValueError(detail)
    return matches[0]


def expected_world_files(
    inventory: WorldArchiveInventory, target: RecoveryTarget
) -> tuple[FileIdentity, ...]:
    """Return one world's normalized rows from the complete inventory."""
    marker = f"-{target.archive_group}-worlds-"
    archives = tuple(row for row in inventory.archives if marker in row.archive_name)
    if target.archive_group == "auxiliary":
        archives = tuple(
            row for row in inventory.archives if "-auxiliary-worlds-" in row.archive_name
        )
    if len(archives) != 1:
        detail = f"world archive group differs: {target.archive_group}"
        raise ValueError(detail)
    rows = tuple(
        FileIdentity(
            relative_path=row.relative_path.removeprefix(target.archive_prefix),
            size_bytes=row.size_bytes,
            sha256=row.sha256,
        )
        for row in archives[0].files
        if row.relative_path.startswith(target.archive_prefix)
    )
    if not rows:
        detail = f"world inventory subset is incomplete: {target.key}"
        raise ValueError(detail)
    return rows


def world_source_identity(
    inventory_path: Path, target: RecoveryTarget
) -> tuple[WorldSourceIdentity, tuple[FileIdentity, ...]]:
    """Build the expected portable identity for one declared source world."""
    inventory = strict_model(inventory_path, WorldArchiveInventory)
    files = expected_world_files(inventory, target)
    encoded = json.dumps(
        [row.model_dump(mode="json") for row in files],
        sort_keys=True,
        separators=(",", ":"),
    ).encode()
    return (
        WorldSourceIdentity(
            world_key=target.key,
            inventory_path=inventory_path.name,
            inventory_size_bytes=inventory_path.stat().st_size,
            inventory_sha256=sha256_file(inventory_path),
            file_count=len(files),
            total_size_bytes=sum(row.size_bytes for row in files),
            tree_sha256=hashlib.sha256(encoded).hexdigest(),
        ),
        files,
    )
