from __future__ import annotations

import secrets
from pathlib import Path
from signal import SIGKILL

import pytest
from tools.run_item7_worldgen import execute

from mcpack_evidence import item7_lifecycle, item7_runtime
from tests.item7.runtime_support import (
    READY_LINES,
    BrokenPipe,
    FakeProcess,
    PipeLessProcess,
    SynchronousThread,
    fake_launch,
    fixed_token,
    pipe_less_launch,
    record_pid_signals,
    record_pids,
    runtime_request,
)


def _discard_kill(pid: int, signal_number: int) -> None:
    del pid, signal_number


def test_lifecycle_sends_commands_only_after_matching_markers(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(secrets, "token_hex", fixed_token("fixed"))
    request = runtime_request(tmp_path, monkeypatch)
    _ = request.target.mkdir()
    _ = (request.target / "logs").mkdir()
    _ = (request.target / "logs/latest.log").write_text("authoritative warning\n", encoding="utf-8")
    process = FakeProcess(
        READY_LINES[:-1],
        responses={
            "say mcpack-item7-flush-fixed-before": (
                "[Server thread/INFO]: [Server] mcpack-item7-flush-fixed-before\n",
            ),
            "save-all flush": (
                "[Server thread/INFO]: Saving the game (this may take a moment!)\n",
                "[Server thread/INFO]: Saved the game\n",
            ),
            "say mcpack-item7-flush-fixed-after": (
                "[Server thread/INFO]: [Server] mcpack-item7-flush-fixed-after\n",
            ),
            "stop": ("[Server thread/INFO]: Stopped server\n",),
        },
    )
    launch_arguments: list[bool] = []

    def launch(*args: str, **kwargs: str | bool | int | Path) -> FakeProcess:
        del args
        launch_arguments.append(kwargs["start_new_session"] is True)
        return process

    monkeypatch.setattr("mcpack_evidence.item7_lifecycle.subprocess.Popen", launch)

    receipt = item7_lifecycle.run_lifecycle(request, request.java_home / "bin/java")

    assert process.stdin.getvalue().splitlines() == [
        "chunky world minecraft:overworld",
        "chunky center 0 0",
        "chunky radius 4c",
        "chunky start",
        "chunky world minecraft:the_nether",
        "chunky center 0 0",
        "chunky radius 4c",
        "chunky start",
        "chunky world minecraft:the_end",
        "chunky center 0 0",
        "chunky radius 4c",
        "chunky start",
        "chunky world minecraft:the_end",
        "chunky center 1536 0",
        "chunky radius 4c",
        "chunky start",
        "say mcpack-item7-flush-fixed-before",
        "save-all flush",
        "say mcpack-item7-flush-fixed-after",
        "stop",
    ]
    assert launch_arguments == [True]
    assert receipt.clean_stop is True
    assert receipt.ready is receipt.generation_finished is receipt.save_all_flush is True
    assert tuple(row.expected_chunk_count for row in receipt.selections) == (81,) * 4
    assert receipt.minecraft_log is not None
    assert Path(receipt.minecraft_log).read_text() == "authoritative warning\n"
    assert receipt.completed_selection_labels == (
        "overworld",
        "nether",
        "end-central",
        "end-outer",
    )


def test_lifecycle_waits_for_unique_marker_before_accepting_delayed_save_lines(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(secrets, "token_hex", fixed_token("delayed"))
    request = runtime_request(tmp_path, monkeypatch)
    _ = request.target.mkdir()
    _ = (request.target / "logs").mkdir()
    _ = (request.target / "logs/latest.log").write_text("warnings\n", encoding="utf-8")
    process = FakeProcess(
        READY_LINES[:-1],
        responses={
            "say mcpack-item7-flush-delayed-before": (
                "[Server thread/INFO]: [Server] mcpack-item7-flush-delayed-before\n",
            ),
            "save-all flush": (
                "[Server thread/INFO]: Saving the game (this may take a moment!)\n",
                "[Server thread/INFO]: Saved the game\n",
            ),
            "say mcpack-item7-flush-delayed-after": (
                "[Server thread/INFO]: [Server] mcpack-item7-flush-delayed-after\n",
            ),
            "stop": ("[Server thread/INFO]: Stopped server\n",),
        },
        delayed_lines=(
            "[Server thread/INFO]: Saving the game (this may take a moment!)\n",
            "[Server thread/INFO]: Saved the game\n",
        ),
    )
    monkeypatch.setattr("mcpack_evidence.item7_lifecycle.subprocess.Popen", fake_launch(process))

    receipt = item7_lifecycle.run_lifecycle(request, request.java_home / "bin/java")

    assert receipt.clean_stop is True
    assert process.stdin.getvalue().splitlines()[-4:] == [
        "say mcpack-item7-flush-delayed-before",
        "save-all flush",
        "say mcpack-item7-flush-delayed-after",
        "stop",
    ]
    lines = request.log_path.read_text(encoding="utf-8").splitlines()
    marker = next(index for index, line in enumerate(lines) if "flush-delayed-before" in line)
    assert sum("Saving the game" in line for line in lines[:marker]) == 1
    assert sum("Saving the game" in line for line in lines[marker + 1 :]) == 1


def test_lifecycle_kills_process_group_on_timeout(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    request = runtime_request(tmp_path, monkeypatch).model_copy(update={"timeout_seconds": 0})
    _ = request.target.mkdir()
    process = FakeProcess(())
    killed: list[tuple[int, int]] = []
    monkeypatch.setattr("mcpack_evidence.item7_lifecycle.subprocess.Popen", fake_launch(process))
    monkeypatch.setattr("mcpack_evidence.item7_lifecycle.os.killpg", record_pid_signals(killed))

    receipt = item7_lifecycle.run_lifecycle(request, request.java_home / "bin/java")

    assert killed == [(43210, SIGKILL)]
    assert receipt.clean_stop is False
    assert receipt.rejection_reason == "world generation timed out"


def test_lifecycle_rejects_broad_or_wrong_chunky_completion(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    request = runtime_request(tmp_path, monkeypatch)
    _ = request.target.mkdir()
    process = FakeProcess(
        (
            '[Server thread/INFO]: Done (1.0s)! For help, type "help"\n',
            "[Chunky] Task finished for minecraft:overworld. Processed: 80 chunks (100.00%)\n",
        )
    )
    monkeypatch.setattr("mcpack_evidence.item7_lifecycle.subprocess.Popen", fake_launch(process))
    monkeypatch.setattr("mcpack_evidence.item7_lifecycle.os.killpg", _discard_kill)

    receipt = item7_lifecycle.run_lifecycle(request, request.java_home / "bin/java")

    assert receipt.clean_stop is False
    assert receipt.completed_selection_labels == ()
    assert "save-all flush" not in receipt.commands


def test_lifecycle_rejects_save_confirmation_queued_before_flush_command(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    # Given: all generation markers and an automatic save confirmation queued before the flush.
    request = runtime_request(tmp_path, monkeypatch)
    _ = request.target.mkdir()
    _ = (request.target / "logs").mkdir()
    process = FakeProcess((*READY_LINES[:-1], "[Server thread/INFO]: Saved the game\n"))
    monkeypatch.setattr("mcpack_evidence.item7_lifecycle.subprocess.Popen", fake_launch(process))
    monkeypatch.setattr("mcpack_evidence.item7_lifecycle.threading.Thread", SynchronousThread)
    monkeypatch.setattr("mcpack_evidence.item7_lifecycle.os.killpg", _discard_kill)

    # When: the lifecycle consumes the queued server output.
    receipt = item7_lifecycle.run_lifecycle(request, request.java_home / "bin/java")

    # Then: the stale confirmation cannot complete the requested flush.
    assert receipt.save_all_flush is False
    assert receipt.clean_stop is False
    assert receipt.commands[-1].endswith("-before")


def test_lifecycle_kills_process_group_on_console_pipe_failure(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    request = runtime_request(tmp_path, monkeypatch)
    _ = request.target.mkdir()
    process = FakeProcess(READY_LINES, BrokenPipe())
    killed: list[int] = []
    monkeypatch.setattr("mcpack_evidence.item7_lifecycle.subprocess.Popen", fake_launch(process))
    monkeypatch.setattr("mcpack_evidence.item7_lifecycle.os.killpg", record_pids(killed))

    receipt = item7_lifecycle.run_lifecycle(request, request.java_home / "bin/java")

    assert killed == [43210]
    assert receipt.clean_stop is False
    assert receipt.rejection_reason == "server console pipe failed"


def test_lifecycle_kills_process_group_on_post_launch_io_failure(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    request = runtime_request(tmp_path, monkeypatch)
    _ = request.target.mkdir()
    process = FakeProcess(())
    killed: list[int] = []

    def fail_io(*args: str) -> None:
        del args
        detail = "evidence disk failed"
        raise OSError(detail)

    monkeypatch.setattr("mcpack_evidence.item7_lifecycle.subprocess.Popen", fake_launch(process))
    monkeypatch.setattr("mcpack_evidence.item7_lifecycle._drive_lifecycle", fail_io)
    monkeypatch.setattr("mcpack_evidence.item7_lifecycle.os.killpg", record_pids(killed))

    receipt = item7_lifecycle.run_lifecycle(request, request.java_home / "bin/java")

    assert killed == [43210]
    assert receipt.rejection_reason == "server lifecycle I/O failed"


def test_lifecycle_rejects_log_open_failure_before_launch(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    request = runtime_request(tmp_path, monkeypatch)
    _ = request.target.mkdir()
    request = request.model_copy(update={"log_path": request.target})
    launched: list[bool] = []

    def launch(*args: str, **kwargs: str | bool | int | Path) -> FakeProcess:
        del args, kwargs
        launched.append(True)
        return FakeProcess(())

    monkeypatch.setattr("mcpack_evidence.item7_lifecycle.subprocess.Popen", launch)

    with pytest.raises(item7_runtime.Item7RuntimeError, match="runtime log could not be opened"):
        _ = item7_lifecycle.run_lifecycle(request, request.java_home / "bin/java")
    assert launched == []


def test_lifecycle_kills_process_group_when_launch_has_no_console_pipe(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    request = runtime_request(tmp_path, monkeypatch)
    _ = request.target.mkdir()
    process = PipeLessProcess()
    killed: list[int] = []
    monkeypatch.setattr(
        "mcpack_evidence.item7_lifecycle.subprocess.Popen", pipe_less_launch(process)
    )
    monkeypatch.setattr("mcpack_evidence.item7_lifecycle.os.killpg", record_pids(killed))

    with pytest.raises(item7_runtime.Item7RuntimeError, match="pipe was not created"):
        _ = item7_lifecycle.run_lifecycle(request, request.java_home / "bin/java")

    assert killed == [43210]


def test_execute_preserves_completed_stages_when_config_capture_fails(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    request = runtime_request(tmp_path, monkeypatch)
    lifecycle = item7_lifecycle.LifecycleReceipt(
        ready=True,
        generation_finished=True,
        save_all_flush=True,
        clean_stop=True,
        return_code=0,
        commands=("save-all flush", "stop"),
        selections=request.selections,
        completed_selection_labels=tuple(row.label for row in request.selections),
        log=str(request.log_path),
        minecraft_log=str(tmp_path / "minecraft-latest.log"),
        duration_seconds=1.0,
        process_group_killed=False,
        rejection_reason=None,
    )

    def completed_lifecycle(
        current_request: item7_runtime.WorldgenRequest, java: Path
    ) -> item7_lifecycle.LifecycleReceipt:
        del current_request, java
        return lifecycle

    monkeypatch.setattr("tools.run_item7_worldgen.run_lifecycle", completed_lifecycle)

    def fail_capture(request: item7_runtime.WorldgenRequest) -> None:
        del request
        stage, detail = "capture", "capture failed"
        raise item7_runtime.Item7RuntimeError(stage, detail)

    monkeypatch.setattr("tools.run_item7_worldgen.capture_runtime_configuration", fail_capture)

    receipt = execute(request)

    assert receipt.preflight is not None
    assert receipt.lifecycle == lifecycle
    assert receipt.configuration is None
    assert receipt.rejection_reason == "capture: capture failed"
