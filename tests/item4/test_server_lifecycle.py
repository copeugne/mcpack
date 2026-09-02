from __future__ import annotations

import time
from typing import TYPE_CHECKING

from tools.run_item4_server_lifecycle import run_lifecycle

if TYPE_CHECKING:
    from pathlib import Path


def test_silent_server_is_killed_at_deadline(tmp_path: Path) -> None:
    run_script = tmp_path / "run.sh"
    _ = run_script.write_text("#!/usr/bin/env bash\nsleep 30\n")
    _ = run_script.chmod(0o755)
    started = time.monotonic()

    receipt = run_lifecycle(tmp_path, tmp_path / "java", tmp_path / "server.log", timeout=1)

    assert time.monotonic() - started < 5
    assert receipt["return_code"] == -9
    assert receipt["clean_stop"] is False
