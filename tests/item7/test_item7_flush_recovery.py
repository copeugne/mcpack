from __future__ import annotations

import hashlib
import secrets
from typing import TYPE_CHECKING

import pytest

from mcpack_evidence import item7_flush_recovery, item7_flush_recovery_lifecycle
from mcpack_evidence.item7_archive_models import FileIdentity
from mcpack_evidence.item7_flush_recovery import FlushRecoveryRequest
from mcpack_evidence.item7_flush_recovery_models import (
    RECOVERY_TARGETS,
    RecoveryLifecycle,
    WorldSourceIdentity,
    world_source_identity,
)
from mcpack_evidence.item7_world_archive_inventory import (
    WorldArchiveContents,
    WorldArchiveInventory,
)
from tests.item7.runtime_support import (
    ROOT,
    FakeProcess,
    fake_launch,
    fixed_token,
    record_pids,
    runtime_request,
)

if TYPE_CHECKING:
    from pathlib import Path


def _identity(path: Path, relative_path: str) -> FileIdentity:
    content = path.read_bytes()
    return FileIdentity(
        relative_path=relative_path,
        size_bytes=len(content),
        sha256=hashlib.sha256(content).hexdigest(),
    )


def _inventory(path: Path, source: Path) -> Path:
    prefix = "run-a-ordinary/world/"
    files = tuple(
        _identity(file, f"{prefix}{file.relative_to(source).as_posix()}")
        for file in sorted(source.rglob("*"))
        if file.is_file()
    )
    report = WorldArchiveInventory(
        schema_version="item7-world-archive-inventory-v1",
        archives=(
            WorldArchiveContents(
                archive_name="item-7-run-a-worlds-test.tar.gz",
                files=files,
            ),
        ),
    )
    _ = path.write_text(report.model_dump_json(), encoding="utf-8")
    return path


def _request(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> tuple[FlushRecoveryRequest, Path]:
    runtime = runtime_request(tmp_path, monkeypatch, role="ordinary")
    source = tmp_path / "source-world"
    _ = (source / "region").mkdir(parents=True)
    _ = (source / "level.dat").write_bytes(b"level")
    _ = (source / "region/r.0.0.mca").write_bytes(b"region")
    inventory = _inventory(tmp_path / "inventory.json", source)
    return (
        FlushRecoveryRequest(
            runtime=runtime,
            world_key="run-a/ordinary",
            runtime_kind="instrumented",
            source_world=source,
            world_inventory=inventory,
            console_log=tmp_path / "raw/flush-recovery/run-a/ordinary/console.log",
        ),
        source,
    )


def _accepted_lifecycle(request: FlushRecoveryRequest, java: Path) -> RecoveryLifecycle:
    del java
    log = request.console_log
    log.parent.mkdir(parents=True, exist_ok=True)
    _ = log.write_text("accepted\n", encoding="utf-8")
    minecraft = log.with_name("minecraft-latest.log")
    _ = minecraft.write_text("accepted\n", encoding="utf-8")
    digest = hashlib.sha256(b"accepted\n").hexdigest()
    root = "flush-recovery/run-a/ordinary"
    return RecoveryLifecycle(
        ready=True,
        save_all_flush=True,
        clean_stop=True,
        return_code=0,
        commands=("say before", "save-all flush", "say after", "stop"),
        console_log=f"{root}/console.log",
        console_log_size_bytes=9,
        console_log_sha256=digest,
        minecraft_log=f"{root}/minecraft-latest.log",
        minecraft_log_size_bytes=9,
        minecraft_log_sha256=digest,
        duration_seconds=1.0,
        process_group_killed=False,
        rejection_reason=None,
    )


def test_committed_inventory_has_twelve_unique_source_bound_worlds() -> None:
    inventory = ROOT / "evidence/item-7/world-archive-inventory.json"

    identities = tuple(world_source_identity(inventory, target)[0] for target in RECOVERY_TARGETS)

    assert len(identities) == 12
    assert len({row.world_key for row in identities}) == 12
    assert len({row.tree_sha256 for row in identities}) == 12
    assert all(row.file_count > 0 and row.total_size_bytes > 0 for row in identities)


def test_recovery_binds_preflight_runtime_and_exact_source(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    request, _ = _request(tmp_path, monkeypatch)
    monkeypatch.setattr(item7_flush_recovery, "run_recovery_lifecycle", _accepted_lifecycle)

    receipt = item7_flush_recovery.execute_recovery(request)

    assert receipt.rejection_reason is None
    assert receipt.preflight is not None
    assert receipt.runtime is not None
    assert receipt.runtime.candidate_count == 137
    assert receipt.runtime.runtime_sha256 == receipt.preflight.instrumented_runtime_sha256
    assert isinstance(receipt.source, WorldSourceIdentity)
    assert receipt.source.world_key == "run-a/ordinary"
    assert receipt.source.file_count == 2
    assert (request.runtime.target / "world/level.dat").read_bytes() == b"level"


def test_recovery_rejects_source_world_changed_after_inventory(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    request, source = _request(tmp_path, monkeypatch)
    _ = (source / "level.dat").write_bytes(b"changed")

    receipt = item7_flush_recovery.execute_recovery(request)

    assert receipt.rejection_reason == "recovery source world differs: run-a/ordinary"
    assert receipt.source is None
    assert receipt.lifecycle is None


def test_recovery_lifecycle_allows_bounded_clean_exit(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    request, _ = _request(tmp_path, monkeypatch)
    _ = request.runtime.target.mkdir()
    _ = (request.runtime.target / "logs").mkdir()
    _ = (request.runtime.target / "logs/latest.log").write_text("accepted\n", encoding="utf-8")
    monkeypatch.setattr(secrets, "token_hex", fixed_token("a" * 32))

    process = FakeProcess(
        ('[Server thread/INFO]: Done (1.0s)! For help, type "help"\n',),
        responses={
            f"say mcpack-item7-flush-{'a' * 32}-before": (
                f"[Server] mcpack-item7-flush-{'a' * 32}-before\n",
            ),
            "save-all flush": (
                "Saving the game (this may take a moment!)\n",
                "Saved the game\n",
            ),
            f"say mcpack-item7-flush-{'a' * 32}-after": (
                f"[Server] mcpack-item7-flush-{'a' * 32}-after\n",
            ),
            "stop": ("Stopped server\n",),
        },
    )
    monkeypatch.setattr(
        "mcpack_evidence.item7_flush_recovery_lifecycle.subprocess.Popen",
        fake_launch(process),
    )

    lifecycle = item7_flush_recovery_lifecycle.run_recovery_lifecycle(
        request, request.runtime.java_home / "bin/java"
    )

    assert lifecycle.clean_stop is True
    assert process.wait_timeouts == [120]


def test_recovery_lifecycle_kills_process_group_when_interrupted(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    request, _ = _request(tmp_path, monkeypatch)
    _ = request.runtime.target.mkdir()
    process = FakeProcess(())
    killed: list[int] = []

    def interrupt(*args: object) -> None:
        del args
        raise KeyboardInterrupt

    monkeypatch.setattr(
        "mcpack_evidence.item7_flush_recovery_lifecycle.subprocess.Popen",
        fake_launch(process),
    )
    monkeypatch.setattr("mcpack_evidence.item7_flush_recovery_lifecycle._drive", interrupt)
    monkeypatch.setattr(
        "mcpack_evidence.item7_flush_recovery_lifecycle.os.killpg", record_pids(killed)
    )

    with pytest.raises(KeyboardInterrupt):
        _ = item7_flush_recovery_lifecycle.run_recovery_lifecycle(
            request, request.runtime.java_home / "bin/java"
        )

    assert killed == [43210]
