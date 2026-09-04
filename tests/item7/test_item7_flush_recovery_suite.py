from __future__ import annotations

import subprocess
import sys
from typing import TYPE_CHECKING

from tools import run_item7_flush_recovery_suite

if TYPE_CHECKING:
    from pathlib import Path

    import pytest


def test_suite_is_sequential_and_stops_after_first_failure(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    calls: list[list[str]] = []

    def reject_first(
        command: list[str],
        *,
        cwd: Path,
        capture_output: bool,
        text: bool,
        check: bool,
    ) -> subprocess.CompletedProcess[str]:
        del cwd, capture_output, text, check
        calls.append(command)
        return subprocess.CompletedProcess(command, 1, "rejected", "")

    monkeypatch.setattr(subprocess, "run", reject_first)
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "run_item7_flush_recovery_suite.py",
            "--project",
            str(tmp_path),
            "--restored",
            str(tmp_path / "restored"),
            "--pristine",
            str(tmp_path / "pristine"),
            "--java-home",
            str(tmp_path / "java"),
            "--output",
            str(tmp_path / "output"),
        ],
    )

    assert run_item7_flush_recovery_suite.main() == 1
    assert len(calls) == 1
