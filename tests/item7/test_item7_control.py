# pyright: standard
from __future__ import annotations

import json
import secrets
from pathlib import Path

import pytest
from tools import run_item7_control

from mcpack_evidence import item7_control
from tests.item7.runtime_support import (
    FROZEN,
    BrokenPipe,
    FakeProcess,
    SynchronousThread,
    fake_launch,
    fixed_token,
    record_pids,
    runtime_request,
)


def _request(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    *,
    settle_seconds: float = 5,
) -> item7_control.ControlRequest:
    return item7_control.ControlRequest(
        runtime=runtime_request(tmp_path, monkeypatch, role="ordinary"),
        settle_seconds=settle_seconds,
    )


def test_control_preflight_materializes_exact_136_without_chunky(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    request = _request(tmp_path, monkeypatch)

    receipt = run_item7_control.prepare_control(request)

    mods = tuple(sorted(path.name for path in request.runtime.target.joinpath("mods").iterdir()))
    assert receipt.seed == "42"
    assert receipt.candidate_count == 136
    assert len(mods) == 136
    assert "Chunky-NeoForge-1.4.23.jar" not in mods
    assert not request.runtime.target.joinpath("config/resourceful-config-web.json").exists()
    assert "level-seed=42" in request.runtime.target.joinpath("server.properties").read_text()


def test_control_preflight_rejects_nonordinary_role(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    runtime = runtime_request(tmp_path, monkeypatch, role="mountainous")

    with pytest.raises(ValueError, match="ordinary seed only"):
        item7_control.ControlRequest(runtime=runtime, settle_seconds=5)


def test_control_lifecycle_waits_for_success_then_settles_flushes_and_stops(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(secrets, "token_hex", fixed_token("control"))
    request = _request(tmp_path, monkeypatch)
    request.runtime.target.mkdir()
    (request.runtime.target / "logs").mkdir()
    (request.runtime.target / "logs/latest.log").write_text("raw warning\n", encoding="utf-8")
    process = FakeProcess(
        (
            '[Server thread/INFO]: Done (1.0s)! For help, type "help"\n',
            (
                "[Server thread/INFO]: Marked 81 chunks in Overworld "
                "from [-4, -4] to [4, 4] to be force loaded\n"
            ),
        ),
        responses={
            "say mcpack-item7-flush-control-before": (
                "[Server thread/INFO]: [Server] mcpack-item7-flush-control-before\n",
            ),
            "save-all flush": (
                "[Server thread/INFO]: Saving the game (this may take a moment!)\n",
                "[Server thread/INFO]: Saved the game\n",
            ),
            "say mcpack-item7-flush-control-after": (
                "[Server thread/INFO]: [Server] mcpack-item7-flush-control-after\n",
            ),
            "stop": ("[Server thread/INFO]: Stopped server\n",),
        },
    )
    sessions: list[bool] = []
    settled: list[float] = []

    def launch(*args: str, **kwargs: str | bool | int | Path) -> FakeProcess:
        del args
        sessions.append(kwargs["start_new_session"] is True)
        return process

    monkeypatch.setattr("mcpack_evidence.item7_control.subprocess.Popen", launch)
    monkeypatch.setattr("mcpack_evidence.item7_control.time.sleep", settled.append)

    receipt = item7_control.run_control_lifecycle(request, request.runtime.java_home / "bin/java")

    assert process.stdin.getvalue().splitlines() == [
        "forceload add -64 -64 64 64",
        "say mcpack-item7-flush-control-before",
        "save-all flush",
        "say mcpack-item7-flush-control-after",
        "stop",
    ]
    assert sessions == [True]
    assert settled == [5]
    assert receipt.clean_stop is True
    assert receipt.forceload_success is receipt.save_all_flush is True
    assert receipt.minecraft_log is not None
    assert Path(receipt.minecraft_log).read_text() == "raw warning\n"
    assert request.runtime.log_path.read_text().endswith("Stopped server\n")


def test_control_waits_for_unique_marker_before_accepting_delayed_save_lines(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(secrets, "token_hex", fixed_token("control-delayed"))
    request = _request(tmp_path, monkeypatch, settle_seconds=0)
    _ = request.runtime.target.mkdir()
    _ = (request.runtime.target / "logs").mkdir()
    _ = (request.runtime.target / "logs/latest.log").write_text("warnings\n", encoding="utf-8")
    process = FakeProcess(
        (
            '[Server thread/INFO]: Done (1.0s)! For help, type "help"\n',
            (
                "[Server thread/INFO]: Marked 81 chunks in Overworld "
                "from [-4, -4] to [4, 4] to be force loaded\n"
            ),
        ),
        responses={
            "say mcpack-item7-flush-control-delayed-before": (
                "[Server thread/INFO]: [Server] mcpack-item7-flush-control-delayed-before\n",
            ),
            "save-all flush": (
                "[Server thread/INFO]: Saving the game (this may take a moment!)\n",
                "[Server thread/INFO]: Saved the game\n",
            ),
            "say mcpack-item7-flush-control-delayed-after": (
                "[Server thread/INFO]: [Server] mcpack-item7-flush-control-delayed-after\n",
            ),
            "stop": ("[Server thread/INFO]: Stopped server\n",),
        },
        delayed_lines=(
            "[Server thread/INFO]: Saving the game (this may take a moment!)\n",
            "[Server thread/INFO]: Saved the game\n",
        ),
    )
    monkeypatch.setattr("mcpack_evidence.item7_control.subprocess.Popen", fake_launch(process))

    receipt = item7_control.run_control_lifecycle(request, request.runtime.java_home / "bin/java")

    assert receipt.clean_stop is True
    assert process.stdin.getvalue().splitlines()[-4:] == [
        "say mcpack-item7-flush-control-delayed-before",
        "save-all flush",
        "say mcpack-item7-flush-control-delayed-after",
        "stop",
    ]


@pytest.mark.parametrize(
    "lines",
    [
        (),
        (
            '[Server thread/INFO]: Done (1.0s)! For help, type "help"\n',
            (
                "[Server thread/INFO]: Marked 81 chunks in minecraft:overworld "
                "from [-4, -4] to [4, 4] to be force loaded\n"
            ),
        ),
    ],
)
def test_control_lifecycle_rejects_missing_exact_success_marker(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, lines: tuple[str, ...]
) -> None:
    request = _request(tmp_path, monkeypatch, settle_seconds=0)
    request.runtime.target.mkdir()
    process = FakeProcess(lines)
    killed: list[int] = []
    monkeypatch.setattr("mcpack_evidence.item7_control.subprocess.Popen", fake_launch(process))
    monkeypatch.setattr("mcpack_evidence.item7_control.os.killpg", record_pids(killed))

    receipt = item7_control.run_control_lifecycle(request, request.runtime.java_home / "bin/java")

    assert receipt.clean_stop is False
    assert receipt.forceload_success is False
    assert "save-all flush" not in receipt.commands
    assert killed == [43210]


def test_control_lifecycle_kills_group_on_timeout_or_pipe_failure(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    timeout_runtime = runtime_request(
        tmp_path / "timeout", monkeypatch, role="ordinary"
    ).model_copy(update={"timeout_seconds": 0})
    timeout = item7_control.ControlRequest(
        runtime=timeout_runtime,
        settle_seconds=0,
    )
    timeout.runtime.target.mkdir()
    timeout_process = FakeProcess(())
    timeout_kills: list[int] = []
    monkeypatch.setattr(
        "mcpack_evidence.item7_control.subprocess.Popen", fake_launch(timeout_process)
    )
    monkeypatch.setattr("mcpack_evidence.item7_control.os.killpg", record_pids(timeout_kills))
    timeout_receipt = item7_control.run_control_lifecycle(
        timeout, timeout.runtime.java_home / "bin/java"
    )
    assert timeout_kills == [43210]
    assert timeout_receipt.rejection_reason == "control generation timed out"

    broken = _request(tmp_path / "broken", monkeypatch, settle_seconds=0)
    broken.runtime.target.mkdir()
    broken_process = FakeProcess(
        ('[Server thread/INFO]: Done (1.0s)! For help, type "help"\n',), BrokenPipe()
    )
    broken_kills: list[int] = []
    monkeypatch.setattr(
        "mcpack_evidence.item7_control.subprocess.Popen", fake_launch(broken_process)
    )
    monkeypatch.setattr("mcpack_evidence.item7_control.os.killpg", record_pids(broken_kills))
    broken_receipt = item7_control.run_control_lifecycle(
        broken, broken.runtime.java_home / "bin/java"
    )
    assert broken_kills == [43210]
    assert broken_receipt.rejection_reason == "server console pipe failed"


def test_control_lifecycle_rejects_save_confirmation_queued_before_flush_command(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    # Given: a force-load success and automatic save confirmation queued before the flush.
    request = _request(tmp_path, monkeypatch, settle_seconds=0)
    _ = request.runtime.target.mkdir()
    process = FakeProcess(
        (
            '[Server thread/INFO]: Done (1.0s)! For help, type "help"\n',
            (
                "[Server thread/INFO]: Marked 81 chunks in Overworld "
                "from [-4, -4] to [4, 4] to be force loaded\n"
            ),
            "[Server thread/INFO]: Saved the game\n",
        )
    )
    monkeypatch.setattr("mcpack_evidence.item7_control.subprocess.Popen", fake_launch(process))
    monkeypatch.setattr("mcpack_evidence.item7_control.threading.Thread", SynchronousThread)
    monkeypatch.setattr("mcpack_evidence.item7_control.os.killpg", lambda pid, signal: None)

    # When: the control lifecycle consumes the queued server output.
    receipt = item7_control.run_control_lifecycle(request, request.runtime.java_home / "bin/java")

    # Then: the stale confirmation cannot complete the requested flush.
    assert receipt.save_all_flush is False
    assert receipt.clean_stop is False
    assert "save-all flush" in receipt.commands


def test_control_capture_sanitizes_and_rejects_chunky_files(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    request = _request(tmp_path, monkeypatch)
    _ = run_item7_control.prepare_control(request)
    frozen_resourceful = FROZEN.joinpath("config/resourceful-config-web.json").read_text()
    request.runtime.target.joinpath("config/resourceful-config-web.json").write_text(
        frozen_resourceful.replace("<redacted-generated-secret>", "secret-value"), encoding="utf-8"
    )
    request.runtime.target.joinpath("world/serverconfig").mkdir(parents=True)
    request.runtime.target.joinpath("world/serverconfig/readme.txt").write_bytes(
        FROZEN.joinpath("world-serverconfig/readme.txt").read_bytes()
    )

    receipt = item7_control.capture_control_configuration(request)

    captured = request.runtime.captured_config.joinpath("config/resourceful-config-web.json")
    assert "secret-value" not in captured.read_text()
    assert receipt.base_file_count == 228
    assert receipt.chunky_files == ()

    rejected = _request(tmp_path / "rejected", monkeypatch)
    _ = run_item7_control.prepare_control(rejected)
    chunky = rejected.runtime.target / "config/chunky/config.json"
    chunky.parent.mkdir(parents=True)
    chunky.write_text("{}", encoding="utf-8")
    with pytest.raises(item7_control.ControlError, match="Chunky configuration is forbidden"):
        item7_control.capture_control_configuration(rejected)


def test_control_cli_help_and_rejected_receipt_need_no_java(tmp_path: Path) -> None:
    with pytest.raises(SystemExit) as help_exit:
        run_item7_control.build_parser().parse_args(["--help"])
    assert help_exit.value.code == 0

    target = tmp_path / "existing"
    target.mkdir()
    receipt = tmp_path / "rejected.json"
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
        str(tmp_path / "console.log"),
        "--captured-config",
        str(tmp_path / "captured"),
        "--receipt",
        str(receipt),
    ]
    assert run_item7_control.main(arguments) == 1
    document = json.loads(receipt.read_text())
    assert "target must be absent" in document["rejection_reason"]
