from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import TYPE_CHECKING

import pytest

from mcpack_evidence.item7_archive_models import ArchiveManifest, FileIdentity
from mcpack_evidence.item7_completion_io import CompletionError
from mcpack_evidence.item7_completion_save import validate_save_sequence_audit
from mcpack_evidence.item7_flush_recovery_models import (
    RECOVERY_TARGETS,
    FlushRecoveryReceipt,
    RecoveryLifecycle,
    RuntimeIdentity,
    world_source_identity,
)
from mcpack_evidence.item7_runtime import (
    CHUNKY_SHA256,
    CONFIG_AUDIT_SHA256,
    FROZEN_MANIFEST_SHA256,
    RETAINED_MANIFEST_SHA256,
    SEED_SUITE_SHA256,
    Item7RuntimeError,
    PreflightReceipt,
)
from mcpack_evidence.item7_save_sequence import (
    build_save_sequence_audit,
    validate_save_sequences,
)
from mcpack_evidence.item7_world_archive_inventory import (
    WorldArchiveContents,
    WorldArchiveInventory,
)

if TYPE_CHECKING:
    from mcpack_evidence.item7_flush_recovery_models import RecoveryTarget


def _digest(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def _write_inventory(path: Path) -> None:
    archives: list[WorldArchiveContents] = []
    for group in ("run-a", "run-b", "auxiliary"):
        rows = tuple(
            FileIdentity(
                relative_path=f"{target.archive_prefix}level.dat",
                size_bytes=len(target.key),
                sha256=_digest(target.key.encode()),
            )
            for target in RECOVERY_TARGETS
            if target.archive_group == group
        )
        archives.append(
            WorldArchiveContents(
                archive_name=f"item-7-{group}-worlds-test.tar.gz",
                files=rows,
            )
        )
    inventory = WorldArchiveInventory(
        schema_version="item7-world-archive-inventory-v1",
        archives=tuple(archives),
    )
    _ = path.write_text(inventory.model_dump_json(), encoding="utf-8")


def _preflight(target: RecoveryTarget) -> PreflightReceipt:
    return PreflightReceipt(
        seed_role=target.role,
        seed="42",
        java_version="Temurin-21.0.12.1+1-LTS",
        retained_candidate_count=136,
        instrumented_candidate_count=137,
        retained_runtime_sha256="a" * 64,
        instrumented_runtime_sha256="b" * 64,
        retained_manifest_sha256=RETAINED_MANIFEST_SHA256,
        frozen_manifest_sha256=FROZEN_MANIFEST_SHA256,
        config_audit_sha256=CONFIG_AUDIT_SHA256,
        seed_suite_sha256=SEED_SUITE_SHA256,
        chunky_sha256=CHUNKY_SHA256,
    )


def _write_recovery(root: Path, inventory: Path, target: RecoveryTarget) -> None:
    evidence = root / target.evidence_root
    evidence.mkdir(parents=True)
    token = _digest(target.key.encode())[:32]
    console = (
        '[Server thread/INFO]: Done (1.0s)! For help, type "help"\n'
        f"[Server thread/INFO]: [Server] mcpack-item7-flush-{token}-before\n"
        "[Server thread/INFO]: Saving the game (this may take a moment!)\n"
        "[Server thread/INFO]: Saved the game\n"
        f"[Server thread/INFO]: [Server] mcpack-item7-flush-{token}-after\n"
    ).encode()
    minecraft = f"minecraft log {target.key}\n".encode()
    console_path = evidence / "console.log"
    minecraft_path = evidence / "minecraft-latest.log"
    _ = console_path.write_bytes(console)
    _ = minecraft_path.write_bytes(minecraft)
    source, _ = world_source_identity(inventory, target)
    preflight = _preflight(target)
    runtime_hash = (
        preflight.retained_runtime_sha256
        if target.runtime_kind == "retained"
        else preflight.instrumented_runtime_sha256
    )
    receipt = FlushRecoveryReceipt(
        runtime_kind=target.runtime_kind,
        role=target.role,
        preflight=preflight,
        runtime=RuntimeIdentity(
            candidate_count=136 + (target.runtime_kind == "instrumented"),
            runtime_sha256=runtime_hash,
        ),
        source=source,
        lifecycle=RecoveryLifecycle(
            ready=True,
            save_all_flush=True,
            clean_stop=True,
            return_code=0,
            commands=(
                f"say mcpack-item7-flush-{token}-before",
                "save-all flush",
                f"say mcpack-item7-flush-{token}-after",
                "stop",
            ),
            console_log=f"{target.evidence_root}/console.log",
            console_log_size_bytes=len(console),
            console_log_sha256=_digest(console),
            minecraft_log=f"{target.evidence_root}/minecraft-latest.log",
            minecraft_log_size_bytes=len(minecraft),
            minecraft_log_sha256=_digest(minecraft),
            duration_seconds=1.0,
            process_group_killed=False,
            rejection_reason=None,
        ),
        rejection_reason=None,
    )
    _ = (evidence / "run-receipt.json").write_text(receipt.model_dump_json(), encoding="utf-8")


def _write_manifest(root: Path, output: Path, forge: str | None = None) -> None:
    files: list[FileIdentity] = []
    for target in RECOVERY_TARGETS:
        for name in ("console.log", "minecraft-latest.log", "run-receipt.json"):
            path = root / target.evidence_root / name
            content = path.read_bytes()
            relative = f"{target.evidence_root}/{name}"
            files.append(
                FileIdentity(
                    relative_path=relative,
                    size_bytes=len(content),
                    sha256="f" * 64 if relative == forge else _digest(content),
                )
            )
    files.sort(key=lambda row: row.relative_path)
    manifest = ArchiveManifest(
        revision="test",
        archive_name="item-7-core-test.tar.gz",
        archive_size_bytes=0,
        archive_sha256="a" * 64,
        file_count=len(files),
        total_size_bytes=sum(row.size_bytes for row in files),
        files=tuple(files),
    )
    _ = output.write_text(manifest.model_dump_json(), encoding="utf-8")


def _accepted_surface(tmp_path: Path) -> tuple[Path, Path]:
    inventory = tmp_path / "world-inventory.json"
    _write_inventory(inventory)
    for target in RECOVERY_TARGETS:
        _write_recovery(tmp_path, inventory, target)
    manifest = tmp_path / "core-manifest.json"
    _write_manifest(tmp_path, manifest)
    return manifest, inventory


def test_accepts_twelve_source_bound_recovery_sequences(tmp_path: Path) -> None:
    manifest, inventory = _accepted_surface(tmp_path)

    records = validate_save_sequences(tmp_path, manifest, inventory)

    assert len(records) == 12
    assert len({row.source_world_key for row in records}) == 12
    assert all(
        row.ready_line
        < row.before_marker_line
        < row.saving_line
        < row.saved_line
        < row.after_marker_line
        for row in records
    )


def test_rejects_duplicate_complete_nonce_sequence(tmp_path: Path) -> None:
    manifest, inventory = _accepted_surface(tmp_path)
    target = RECOVERY_TARGETS[0]
    console = tmp_path / target.evidence_root / "console.log"
    _ = console.write_bytes(console.read_bytes() + console.read_bytes())
    _write_manifest(tmp_path, manifest)

    with pytest.raises(Item7RuntimeError, match="save sequence differs"):
        _ = validate_save_sequences(tmp_path, manifest, inventory)


def test_rejects_forged_source_world_identity(tmp_path: Path) -> None:
    manifest, inventory = _accepted_surface(tmp_path)
    target = RECOVERY_TARGETS[0]
    receipt_path = tmp_path / target.evidence_root / "run-receipt.json"
    receipt = FlushRecoveryReceipt.model_validate_json(receipt_path.read_bytes(), strict=True)
    assert receipt.source is not None
    forged = receipt.model_copy(
        update={"source": receipt.source.model_copy(update={"tree_sha256": "f" * 64})}
    )
    _ = receipt_path.write_text(forged.model_dump_json(), encoding="utf-8")
    _write_manifest(tmp_path, manifest)

    with pytest.raises(Item7RuntimeError, match="flush recovery receipt differs"):
        _ = validate_save_sequences(tmp_path, manifest, inventory)


def test_rejects_evidence_not_bound_by_core_manifest(tmp_path: Path) -> None:
    manifest, inventory = _accepted_surface(tmp_path)
    forged = f"{RECOVERY_TARGETS[0].evidence_root}/run-receipt.json"
    _write_manifest(tmp_path, manifest, forge=forged)

    with pytest.raises(Item7RuntimeError, match="differs from core manifest"):
        _ = validate_save_sequences(tmp_path, manifest, inventory)


def test_completion_rejects_forged_or_old_audit(tmp_path: Path) -> None:
    manifest, inventory = _accepted_surface(tmp_path)
    audit = tmp_path / "save-sequence.json"
    payload = build_save_sequence_audit(tmp_path, manifest, inventory)
    _ = audit.write_text(json.dumps(payload), encoding="utf-8")
    assert validate_save_sequence_audit(audit, tmp_path, manifest, inventory).path == audit.name

    payload["schema_version"] = "item7-save-sequence-audit-v2"
    _ = audit.write_text(json.dumps(payload), encoding="utf-8")
    with pytest.raises(CompletionError, match="save sequence audit source binding"):
        _ = validate_save_sequence_audit(audit, tmp_path, manifest, inventory)


def test_audit_document_identities_are_path_portable(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    manifest, inventory = _accepted_surface(tmp_path)
    monkeypatch.chdir(tmp_path)

    relative = build_save_sequence_audit(tmp_path, Path(manifest.name), Path(inventory.name))
    absolute = build_save_sequence_audit(tmp_path, manifest.resolve(), inventory.resolve())

    assert relative == absolute
    core_identity = relative["core_manifest"]
    world_identity = relative["world_inventory"]
    assert isinstance(core_identity, dict)
    assert isinstance(world_identity, dict)
    assert core_identity["path"] == manifest.name
    assert world_identity["path"] == inventory.name
