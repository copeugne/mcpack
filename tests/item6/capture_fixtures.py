# pyright: standard
"""Fixture builders shared by Item 6 capture contract tests."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path

_TEST_SOURCE_VALUE = "test-only-source-value"


def _make_instance(tmp_path: Path) -> Path:
    """Create a complete minimal source instance for capture tests."""
    instance = tmp_path / "instance"
    for directory, payload in (
        (instance / "config", "config=value\n"),
        (instance / "defaultconfigs", "defaults=value\n"),
        (instance / "world" / "serverconfig", "world=value\n"),
    ):
        directory.mkdir(parents=True)
        (directory / "settings.txt").write_text(payload, encoding="utf-8")
    (instance / "config" / "resourceful-config-web.json").write_text(
        json.dumps(
            {
                "enabled": False,
                "port": 8080,
                "validator": {
                    "if": {
                        "password": _TEST_SOURCE_VALUE,
                        "type": "uuid",
                        "uuids": [],
                    },
                    "type": "if",
                },
            }
        ),
        encoding="utf-8",
    )
    (instance / "server.properties").write_text("level-name=world\n", encoding="utf-8")
    return instance


def _write_resourceful_config(instance: Path, payload: bytes) -> None:
    """Replace the capture source config with exact bytes for boundary tests."""
    _ = (instance / "config" / "resourceful-config-web.json").write_bytes(payload)
