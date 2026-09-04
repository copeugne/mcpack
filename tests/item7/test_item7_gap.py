# pyright: standard
from __future__ import annotations

import json
from pathlib import Path

import pytest
from tools import run_item7_gap_targets

from mcpack_evidence import item7_gap
from tests.item7.runtime_support import FakeProcess, fake_launch, record_pids, runtime_request


def _request(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> item7_gap.GapRequest:
    return item7_gap.GapRequest(runtime=runtime_request(tmp_path, monkeypatch, role="ordinary"))


def _located(structure: str, x: int, z: int) -> str:
    return f"[Server thread/INFO]: The nearest {structure} is at [{x}, ~, {z}] (1 blocks away)\n"


def _parse_rejected(line: str, target: item7_gap.GapTarget) -> str:
    if line.startswith("[Chunky]"):
        return item7_gap.parse_completion_marker(line, target)
    return item7_gap.parse_locate_line(line, target).structure


def test_gap_targets_are_sorted_and_locations_drive_exact_chunky_commands(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    request = _request(tmp_path, monkeypatch)
    request.runtime.target.mkdir()
    logs = request.runtime.target / "logs"
    logs.mkdir()
    (logs / "latest.log").write_text("authoritative log\n", encoding="utf-8")
    lines = (
        '[Server thread/INFO]: Done (1.0s)! For help, type "help"\n',
        _located("betterdeserttemples:desert_temple", 32, -48),
        _located("betterstrongholds:stronghold", -64, 96),
        _located("betterwitchhuts:witch_hut", 128, 160),
        _located("integrated_stronghold:stronghold", -192, -224),
        "[Chunky] Task finished for minecraft:overworld. Processed: 81 chunks (100.00%)\n",
        "[Chunky] Task finished for minecraft:overworld. Processed: 81 chunks (100.00%)\n",
        "[Chunky] Task finished for minecraft:overworld. Processed: 81 chunks (100.00%)\n",
        "[Chunky] Task finished for minecraft:overworld. Processed: 81 chunks (100.00%)\n",
        "[Server thread/INFO]: Saved the game\n",
    )
    process = FakeProcess(lines)
    monkeypatch.setattr("mcpack_evidence.item7_gap.subprocess.Popen", fake_launch(process))

    receipt = item7_gap.run_gap_lifecycle(request, request.runtime.java_home / "bin/java")

    assert tuple(target.structure for target in item7_gap.GAP_TARGETS) == tuple(
        sorted(target.structure for target in item7_gap.GAP_TARGETS)
    )
    assert receipt.clean_stop is True
    assert receipt.completed_targets == tuple(target.structure for target in item7_gap.GAP_TARGETS)
    assert process.stdin.getvalue().splitlines() == [
        "locate structure betterdeserttemples:desert_temple",
        "locate structure betterstrongholds:stronghold",
        "locate structure betterwitchhuts:witch_hut",
        "locate structure integrated_stronghold:stronghold",
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
        "save-all flush",
        "stop",
    ]
    assert Path(receipt.minecraft_log or "").read_text(encoding="utf-8") == "authoritative log\n"


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
