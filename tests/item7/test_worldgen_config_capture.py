from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from mcpack_evidence import item7_config, item7_runtime
from mcpack_evidence.item6_capture import capture as real_capture
from tests.item7.runtime_support import FROZEN, runtime_request

if TYPE_CHECKING:
    from pathlib import Path


def _prepared_request(tmp_path: Path) -> item7_runtime.WorldgenRequest:
    request = runtime_request(tmp_path)
    _ = item7_runtime.prepare_worldgen(request)
    resourceful = request.target / "config/resourceful-config-web.json"
    frozen_resourceful = (FROZEN / "config/resourceful-config-web.json").read_text()
    _ = resourceful.write_text(
        frozen_resourceful.replace("<redacted-generated-secret>", "secret-value"), encoding="utf-8"
    )
    _ = (request.target / "world/serverconfig").mkdir(parents=True)
    _ = (request.target / "world/serverconfig/readme.txt").write_bytes(
        (FROZEN / "world-serverconfig/readme.txt").read_bytes()
    )
    return request


def _write_chunky_files(request: item7_runtime.WorldgenRequest, content: bytes) -> None:
    for relative in item7_config.CHUNKY_PATHS:
        path = request.target / relative
        _ = path.parent.mkdir(parents=True, exist_ok=True)
        _ = path.write_bytes(content)


def test_capture_sanitizes_generated_credential(tmp_path: Path) -> None:
    request = _prepared_request(tmp_path)
    chunky_files = {
        "config/chunky/config.json": b"{}",
        "config/chunky/tasks/minecraft/overworld.properties": b"done=true\n",
        "config/chunky/tasks/minecraft/the_end.properties": b"done=false\n",
        "config/chunky/tasks/minecraft/the_nether.properties": b"done=false\n",
    }
    for relative, content in chunky_files.items():
        path = request.target / relative
        _ = path.parent.mkdir(parents=True, exist_ok=True)
        _ = path.write_bytes(content)

    receipt = item7_config.capture_runtime_configuration(request)

    captured = (request.captured_config / "config/resourceful-config-web.json").read_text()
    assert "secret-value" not in captured
    assert "<redacted-generated-secret>" in captured
    assert (request.captured_config.parent / "config-sanitization.json").is_file()
    assert receipt.base_file_count == 228
    assert tuple(row.path for row in receipt.chunky_files) == tuple(chunky_files)
    assert receipt.normalized_runtime_drifts == ()


def test_capture_records_comment_only_runtime_normalization(tmp_path: Path) -> None:
    request = _prepared_request(tmp_path)
    _write_chunky_files(request, b"generated=true\n")
    normalized = request.target / "config/bettervillage_1.properties"
    _ = normalized.write_text(
        normalized.read_text(encoding="utf-8").replace(
            "#Thu Sep 03 19:56:32 UTC 2026", "#Fri Sep 04 07:06:06 CEST 2026"
        ),
        encoding="utf-8",
    )

    receipt = item7_config.capture_runtime_configuration(request)

    assert tuple(row.path for row in receipt.normalized_runtime_drifts) == (
        "config/bettervillage_1.properties",
    )


def test_capture_rejects_value_drift_in_comment_normalized_file(tmp_path: Path) -> None:
    request = _prepared_request(tmp_path)
    _write_chunky_files(request, b"generated=true\n")
    normalized = request.target / "config/bettervillage_1.properties"
    _ = normalized.write_text(
        normalized.read_text(encoding="utf-8").replace(
            "int.villages.separation=20", "int.villages.separation=21"
        ),
        encoding="utf-8",
    )

    with pytest.raises(item7_runtime.Item7RuntimeError, match="bettervillage"):
        _ = item7_config.capture_runtime_configuration(request)


def test_capture_rejects_unsanitized_generated_credential(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    request = _prepared_request(tmp_path)
    _write_chunky_files(request, b"generated=true\n")

    def leave_unsanitized(source: Path, destination: Path) -> None:
        _ = real_capture(source, destination)
        captured = destination / "config/resourceful-config-web.json"
        _ = captured.write_text(
            captured.read_text().replace("<redacted-generated-secret>", "secret-value")
        )

    monkeypatch.setattr("mcpack_evidence.item7_config.capture", leave_unsanitized)

    with pytest.raises(item7_runtime.Item7RuntimeError, match="captured Item 6 file differs"):
        _ = item7_config.capture_runtime_configuration(request)
