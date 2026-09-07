# pyright: standard
from __future__ import annotations

import json
import secrets
from pathlib import Path

import pytest
from tools import run_item7_gap_targets

from mcpack_evidence import item7_gap
from tests.item7.runtime_support import (
    FakeProcess,
    SynchronousThread,
    fake_launch,
    fixed_token,
    record_pids,
    runtime_request,
)


def _request(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> item7_gap.GapRequest:
    return item7_gap.GapRequest(runtime=runtime_request(tmp_path, monkeypatch, role="ordinary"))


def _located(structure: str, x: int, z: int) -> str:
    return f"[Server thread/INFO]: The nearest {structure} is at [{x}, ~, {z}] (1 blocks away)\n"


def _parse_rejected(line: str, target: item7_gap.GapTarget) -> str:
    if line.startswith("[Chunky]"):
        return item7_gap.parse_completion_marker(line, target)
    return item7_gap.parse_locate_line(line, target).structure


@pytest.mark.parametrize("custom_targets", [False, True])
def test_gap_targets_are_sorted_and_locations_drive_exact_chunky_commands(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, custom_targets: bool
) -> None:
    monkeypatch.setattr(secrets, "token_hex", fixed_token("gap"))
    request = _request(tmp_path, monkeypatch)
    identifiers = (
        (
            "explorify:campsite",
            "explorify:dark_forest_settlement",
            "explorify:ruins",
            "explorify:tavern",
        )
        if custom_targets
        else tuple(target.structure for target in item7_gap.GAP_TARGETS)
    )
    request = item7_gap.GapRequest(
        runtime=request.runtime,
        targets=tuple(item7_gap.GapTarget(structure=identifier) for identifier in identifiers),
    )
    request.runtime.target.mkdir()
    logs = request.runtime.target / "logs"
    logs.mkdir()
    (logs / "latest.log").write_text("authoritative log\n", encoding="utf-8")
    lines = (
        '[Server thread/INFO]: Done (1.0s)! For help, type "help"\n',
        _located(identifiers[0], 32, -48),
        _located(identifiers[1], -64, 96),
        _located(identifiers[2], 128, 160),
        _located(identifiers[3], -192, -224),
        "[Chunky] Task finished for minecraft:overworld. Processed: 81 chunks (100.00%)\n",
        "[Chunky] Task finished for minecraft:overworld. Processed: 81 chunks (100.00%)\n",
        "[Chunky] Task finished for minecraft:overworld. Processed: 81 chunks (100.00%)\n",
        "[Chunky] Task finished for minecraft:overworld. Processed: 81 chunks (100.00%)\n",
    )
    process = FakeProcess(
        lines,
        responses={
            "say mcpack-item7-flush-gap-before": (
                "[Server thread/INFO]: [Server] mcpack-item7-flush-gap-before\n",
            ),
            "save-all flush": (
                "[Server thread/INFO]: Saving the game (this may take a moment!)\n",
                "[Server thread/INFO]: Saved the game\n",
            ),
            "say mcpack-item7-flush-gap-after": (
                "[Server thread/INFO]: [Server] mcpack-item7-flush-gap-after\n",
            ),
            "stop": ("[Server thread/INFO]: Stopped server\n",),
        },
    )
    monkeypatch.setattr("mcpack_evidence.item7_gap.subprocess.Popen", fake_launch(process))

    receipt = item7_gap.run_gap_lifecycle(request, request.runtime.java_home / "bin/java")

    assert tuple(target.structure for target in item7_gap.GAP_TARGETS) == tuple(
        sorted(target.structure for target in item7_gap.GAP_TARGETS)
    )
    assert receipt.clean_stop is True
    assert receipt.completed_targets == identifiers
    assert process.stdin.getvalue().splitlines() == [
        f"locate structure {identifiers[0]}",
        f"locate structure {identifiers[1]}",
        f"locate structure {identifiers[2]}",
        f"locate structure {identifiers[3]}",
        "chunky world minecraft:overworld",
        "chunky center 32 -48",
        "chunky radius 4c",
        "chunky start",
        "chunky world minecraft:overworld",
        "chunky center -64 96",
        "chunky radius 4c",
        "chunky start",
        "chunky world minecraft:overworld",
        "chunky center 128 160",
        "chunky radius 4c",
        "chunky start",
        "chunky world minecraft:overworld",
        "chunky center -192 -224",
        "chunky radius 4c",
        "chunky start",
        "say mcpack-item7-flush-gap-before",
        "save-all flush",
        "say mcpack-item7-flush-gap-after",
        "stop",
    ]
    assert Path(receipt.minecraft_log or "").read_text(encoding="utf-8") == "authoritative log\n"


def test_gap_waits_for_unique_marker_before_accepting_delayed_save_lines(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(secrets, "token_hex", fixed_token("gap-delayed"))
    request = _request(tmp_path, monkeypatch)
    _ = request.runtime.target.mkdir()
    _ = (request.runtime.target / "logs").mkdir()
    _ = (request.runtime.target / "logs/latest.log").write_text("warnings\n", encoding="utf-8")
    lines = (
        '[Server thread/INFO]: Done (1.0s)! For help, type "help"\n',
        _located("betterdeserttemples:desert_temple", 32, -48),
        _located("betterstrongholds:stronghold", -64, 96),
        _located("betterwitchhuts:witch_hut", 128, 160),
        _located("integrated_stronghold:stronghold", -192, -224),
        *(
            "[Chunky] Task finished for minecraft:overworld. Processed: 81 chunks (100.00%)\n"
            for _ in item7_gap.GAP_TARGETS
        ),
    )
    process = FakeProcess(
        lines,
        responses={
            "say mcpack-item7-flush-gap-delayed-before": (
                "[Server thread/INFO]: [Server] mcpack-item7-flush-gap-delayed-before\n",
            ),
            "save-all flush": (
                "[Server thread/INFO]: Saving the game (this may take a moment!)\n",
                "[Server thread/INFO]: Saved the game\n",
            ),
            "say mcpack-item7-flush-gap-delayed-after": (
                "[Server thread/INFO]: [Server] mcpack-item7-flush-gap-delayed-after\n",
            ),
            "stop": ("[Server thread/INFO]: Stopped server\n",),
        },
        delayed_lines=(
            "[Server thread/INFO]: Saving the game (this may take a moment!)\n",
            "[Server thread/INFO]: Saved the game\n",
        ),
    )
    monkeypatch.setattr("mcpack_evidence.item7_gap.subprocess.Popen", fake_launch(process))

    receipt = item7_gap.run_gap_lifecycle(request, request.runtime.java_home / "bin/java")

    assert receipt.clean_stop is True
    assert process.stdin.getvalue().splitlines()[-4:] == [
        "say mcpack-item7-flush-gap-delayed-before",
        "save-all flush",
        "say mcpack-item7-flush-gap-delayed-after",
        "stop",
    ]


@pytest.mark.parametrize(
    ("line", "expected"),
    [
        (
            "[Server thread/INFO]: The nearest wrong:structure is at [32, ~, -48] (1 blocks away)",
            "located structure differs",
        ),
        (
            "[Chunky] Task finished for minecraft:the_nether. Processed: 81 chunks (100.00%)",
            "completion marker differs",
        ),
    ],
)
def test_gap_parser_rejects_wrong_structure_or_completion_marker(line: str, expected: str) -> None:
    target = item7_gap.GAP_TARGETS[0]

    with pytest.raises(item7_gap.GapError, match=expected):
        _ = _parse_rejected(line, target)


def test_gap_lifecycle_kills_group_on_timeout(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    runtime = runtime_request(tmp_path, monkeypatch, role="ordinary").model_copy(
        update={"timeout_seconds": 0}
    )
    request = item7_gap.GapRequest(runtime=runtime)
    runtime.target.mkdir()
    process = FakeProcess(())
    killed: list[int] = []
    monkeypatch.setattr("mcpack_evidence.item7_gap.subprocess.Popen", fake_launch(process))
    monkeypatch.setattr("mcpack_evidence.item7_gap.os.killpg", record_pids(killed))

    receipt = item7_gap.run_gap_lifecycle(request, runtime.java_home / "bin/java")

    assert receipt.clean_stop is False
    assert receipt.rejection_reason == "gap target lifecycle timed out"
    assert killed == [43210]


def test_gap_lifecycle_rejects_save_confirmation_queued_before_flush_command(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    # Given: all locate and Chunky markers plus an automatic save queued before the flush.
    request = _request(tmp_path, monkeypatch)
    _ = request.runtime.target.mkdir()
    process = FakeProcess(
        (
            '[Server thread/INFO]: Done (1.0s)! For help, type "help"\n',
            _located("betterdeserttemples:desert_temple", 32, -48),
            _located("betterstrongholds:stronghold", -64, 96),
            _located("betterwitchhuts:witch_hut", 128, 160),
            _located("integrated_stronghold:stronghold", -192, -224),
            *(
                "[Chunky] Task finished for minecraft:overworld. Processed: 81 chunks (100.00%)\n"
                for _ in item7_gap.GAP_TARGETS
            ),
            "[Server thread/INFO]: Saved the game\n",
        )
    )
    monkeypatch.setattr("mcpack_evidence.item7_gap.subprocess.Popen", fake_launch(process))
    monkeypatch.setattr("mcpack_evidence.item7_gap.threading.Thread", SynchronousThread)
    monkeypatch.setattr("mcpack_evidence.item7_gap.os.killpg", lambda pid, signal: None)

    # When: the gap lifecycle consumes the queued server output.
    receipt = item7_gap.run_gap_lifecycle(request, request.runtime.java_home / "bin/java")

    # Then: the stale confirmation cannot complete the requested flush.
    assert receipt.save_all_flush is False
    assert receipt.clean_stop is False
    assert receipt.commands[-1].endswith("-before")


def test_gap_cli_preserves_atomic_rejected_receipt_without_java(tmp_path: Path) -> None:
    target = tmp_path / "existing"
    target.mkdir()
    receipt = tmp_path / "receipt.json"
    arguments = [
        "--pristine",
        "/missing",
        "--artifact-manifest",
        "/missing",
        "--retained-manifest",
        "/missing",
        "--seed-suite",
        "/missing",
        "--frozen-config",
        "/missing",
        "--frozen-manifest",
        "/missing",
        "--config-audit",
        "/missing",
        "--java-home",
        "/missing",
        "--target",
        str(target),
        "--log-path",
        str(tmp_path / "runtime.log"),
        "--captured-config",
        str(tmp_path / "captured"),
        "--receipt",
        str(receipt),
    ]

    assert run_item7_gap_targets.main(arguments) == 1

    document = json.loads(receipt.read_text(encoding="utf-8"))
    assert "target must be absent" in document["rejection_reason"]
