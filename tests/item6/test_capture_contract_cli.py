# pyright: standard
"""Public CLI tests for the Item 6 capture boundary."""

from __future__ import annotations

import json
import subprocess
import sys
from typing import TYPE_CHECKING

from tests.item6.capture_fixtures import _TEST_SOURCE_VALUE, _make_instance
from tests.item6.helpers import ROOT

if TYPE_CHECKING:
    from pathlib import Path

_REDACTION_SENTINEL = "<redacted-generated-secret>"


def test_capture_cli_writes_exact_public_layout(tmp_path: Path) -> None:
    """The public CLI captures all and only the documented layout."""
    # Given: a valid source instance and absent target.
    instance = _make_instance(tmp_path)
    output = tmp_path / "captured"

    # When: the public command-line interface captures the source.
    completed = subprocess.run(  # noqa: S603
        (
            sys.executable,
            "tools/freeze_item6_config.py",
            "capture",
            "--instance",
            str(instance),
            "--output",
            str(output),
        ),
        check=False,
        cwd=ROOT,
        capture_output=True,
        text=True,
    )

    # Then: the command succeeds with exactly the public configuration inventory.
    assert completed.returncode == 0, completed.stderr
    assert _TEST_SOURCE_VALUE not in completed.stdout
    assert _TEST_SOURCE_VALUE not in completed.stderr
    captured = json.loads(
        (output / "config" / "resourceful-config-web.json").read_text(encoding="utf-8")
    )
    assert captured["validator"]["if"]["password"] == _REDACTION_SENTINEL
    receipt_text = (tmp_path / "config-sanitization.json").read_text(encoding="utf-8")
    assert _TEST_SOURCE_VALUE not in receipt_text
    assert "hash" not in receipt_text
    assert sorted(
        path.relative_to(output).as_posix() for path in output.rglob("*") if path.is_file()
    ) == [
        "config/resourceful-config-web.json",
        "config/settings.txt",
        "defaultconfigs/settings.txt",
        "server.properties",
        "world-serverconfig/settings.txt",
    ]
    assert (tmp_path / "config-sanitization.json").is_file()
