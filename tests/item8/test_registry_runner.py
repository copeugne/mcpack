from __future__ import annotations

import json
import subprocess
from typing import TYPE_CHECKING

import pytest
from tools import run_item8_registry as runner

from mcpack_evidence.item7_runtime import Item7RuntimeError

if TYPE_CHECKING:
    from pathlib import Path

    from mcpack_evidence.item7_control import ControlRequest


def arguments(tmp_path: Path) -> runner.Arguments:
    return runner.Arguments(
        pristine=tmp_path / "pristine",
        java_home=tmp_path / "java",
        target=tmp_path / "instance",
        output=tmp_path / "output",
        timeout_seconds=5,
    )


def clean_git(*args: object, **kwargs: object) -> str:
    del args, kwargs
    return ""


def reject_preflight(request: ControlRequest) -> None:
    del request
    stage = "preflight"
    detail = "bad input fixture"
    raise Item7RuntimeError(stage, detail)


def test_preflight_failure_is_preserved_without_copying_unowned_logs(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    request = arguments(tmp_path)
    (request.target / "logs").mkdir(parents=True)
    _ = (request.target / "logs/latest.log").write_text(
        "private existing instance", encoding="utf-8"
    )
    monkeypatch.setattr(subprocess, "check_output", clean_git)
    monkeypatch.setattr(runner, "prepare_control", reject_preflight)
    result = runner.capture(request)
    assert result["rejection_reason"] == "preflight: bad input fixture"
    assert json.loads((request.output / "capture.json").read_text()) == result
    assert not (request.output / "latest.log").exists()
    assert (request.target / "logs/latest.log").read_text() == "private existing instance"


def test_output_reuse_is_refused(tmp_path: Path) -> None:
    request = arguments(tmp_path)
    request.output.mkdir()
    with pytest.raises(FileExistsError):
        _ = runner.capture(request)


def test_linked_output_is_refused(tmp_path: Path) -> None:
    request = arguments(tmp_path)
    request.output.symlink_to(tmp_path / "elsewhere", target_is_directory=True)
    with pytest.raises(ValueError, match="symlink"):
        _ = runner.capture(request)
    assert not (tmp_path / "elsewhere").exists()


def test_existing_administrative_interfaces_are_not_silently_changed(tmp_path: Path) -> None:
    properties = tmp_path / "server.properties"
    _ = properties.write_text("enable-rcon=true\nenable-query=false\n", encoding="utf-8")
    with pytest.raises(ValueError, match="disabled RCON"):
        runner.check_ports(properties)
