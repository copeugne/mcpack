"""Validate one source-bound Item 7 flush recovery receipt."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path  # noqa: TC003
from typing import Final

from mcpack_evidence.item7_completion_io import strict_model
from mcpack_evidence.item7_flush_recovery_models import (
    FlushRecoveryReceipt,
    RecoveryTarget,
    world_source_identity,
)
from mcpack_evidence.item7_runtime import (
    CHUNKY_SHA256,
    CONFIG_AUDIT_SHA256,
    FROZEN_MANIFEST_SHA256,
    RETAINED_COUNT,
    RETAINED_MANIFEST_SHA256,
    SEED_SUITE_SHA256,
    Item7RuntimeError,
)

_COMMAND: Final = re.compile(r"say mcpack-item7-flush-(?P<token>[0-9a-f]{32})-before")
_STAGE: Final = "lifecycle"
_COMMAND_COUNT: Final = 4


@dataclass(frozen=True, slots=True)
class ReceiptEvidence:
    """Accepted receipt and its unique correlation token."""

    path: Path
    receipt: FlushRecoveryReceipt
    token: str


def validate_recovery_receipt(
    root: Path, target: RecoveryTarget, inventory_path: Path
) -> ReceiptEvidence:
    """Require one accepted receipt bound to the declared runtime and world."""
    path = root / target.evidence_root / "run-receipt.json"
    try:
        receipt = strict_model(path, FlushRecoveryReceipt)
        expected_source, _ = world_source_identity(inventory_path, target)
    except (OSError, ValueError) as error:
        raise _invalid(target) from error
    if (
        receipt.schema_version != "item7-flush-recovery-v1"
        or receipt.runtime_kind != target.runtime_kind
        or receipt.role != target.role
        or receipt.rejection_reason is not None
        or receipt.preflight is None
        or receipt.runtime is None
        or receipt.source != expected_source
        or receipt.lifecycle is None
    ):
        raise _invalid(target)
    preflight = receipt.preflight
    runtime_hash = (
        preflight.retained_runtime_sha256
        if target.runtime_kind == "retained"
        else preflight.instrumented_runtime_sha256
    )
    runtime_count = RETAINED_COUNT + (target.runtime_kind == "instrumented")
    if (
        preflight.seed_role != target.role
        or preflight.retained_candidate_count != RETAINED_COUNT
        or preflight.instrumented_candidate_count != RETAINED_COUNT + 1
        or preflight.retained_manifest_sha256 != RETAINED_MANIFEST_SHA256
        or preflight.frozen_manifest_sha256 != FROZEN_MANIFEST_SHA256
        or preflight.config_audit_sha256 != CONFIG_AUDIT_SHA256
        or preflight.seed_suite_sha256 != SEED_SUITE_SHA256
        or preflight.chunky_sha256 != CHUNKY_SHA256
        or receipt.runtime.candidate_count != runtime_count
        or receipt.runtime.runtime_sha256 != runtime_hash
    ):
        raise _invalid(target)
    lifecycle = receipt.lifecycle
    if (
        not lifecycle.ready
        or not lifecycle.save_all_flush
        or not lifecycle.clean_stop
        or lifecycle.return_code != 0
        or lifecycle.process_group_killed
        or lifecycle.rejection_reason is not None
        or lifecycle.console_log != f"{target.evidence_root}/console.log"
        or lifecycle.minecraft_log != f"{target.evidence_root}/minecraft-latest.log"
        or len(lifecycle.commands) != _COMMAND_COUNT
    ):
        raise _invalid(target)
    match = _COMMAND.fullmatch(lifecycle.commands[0])
    if match is None:
        raise _invalid(target)
    token = match.group("token")
    expected_commands = (
        f"say mcpack-item7-flush-{token}-before",
        "save-all flush",
        f"say mcpack-item7-flush-{token}-after",
        "stop",
    )
    if lifecycle.commands != expected_commands:
        raise _invalid(target)
    return ReceiptEvidence(path, receipt, token)


def _invalid(target: RecoveryTarget) -> Item7RuntimeError:
    detail = f"flush recovery receipt differs: {target.key}"
    return Item7RuntimeError(_STAGE, detail)
