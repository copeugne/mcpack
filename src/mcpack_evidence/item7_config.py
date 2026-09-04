"""Capture and verify the bounded Item 7 runtime configuration."""

from __future__ import annotations

import hashlib
from typing import TYPE_CHECKING, ClassVar, Final, Literal

from pydantic import BaseModel, ConfigDict

from mcpack_evidence.item6_capture import capture
from mcpack_evidence.item7_runtime import (
    ArtifactHash,
    Item7RuntimeError,
    WorldgenRequest,
    materialized_seed,
    replace_property,
    sha256_file,
)

if TYPE_CHECKING:
    from pathlib import Path

FROZEN_FILE_COUNT: Final = 228
OVERWORLD_CHUNKY_PATHS: Final = (
    "config/chunky/config.json",
    "config/chunky/tasks/minecraft/overworld.properties",
)
CHUNKY_PATHS: Final = (
    *OVERWORLD_CHUNKY_PATHS,
    "config/chunky/tasks/minecraft/the_end.properties",
    "config/chunky/tasks/minecraft/the_nether.properties",
)
_COMMENT_NORMALIZED_PATHS: Final = frozenset(
    {
        "config/bettervillage_1.properties",
        "config/c2me.toml",
        "config/libraryferret_1.properties",
        "server.properties",
    }
)
_CAPTURE_STAGE: Final = "capture"


class RuntimeConfigDrift(BaseModel):
    """One byte change proven to affect comments only."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True)

    path: str
    frozen_sha256: str
    captured_sha256: str
    normalization: Literal["comment-lines-removed"] = "comment-lines-removed"


class ConfigCaptureReceipt(BaseModel):
    """Item 6 parity and separately hashed Chunky-generated configuration."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True)

    schema_version: Literal["item7-config-capture-v1"] = "item7-config-capture-v1"
    base_file_count: Literal[228]
    chunky_files: tuple[ArtifactHash, ...]
    normalized_runtime_drifts: tuple[RuntimeConfigDrift, ...]


def capture_runtime_configuration(
    request: WorldgenRequest, *, chunky_paths: tuple[str, ...] = CHUNKY_PATHS
) -> ConfigCaptureReceipt:
    """Capture safely, require Item 6 parity, and isolate the expected Chunky files."""
    try:
        capture(request.target, request.captured_config)
    except (OSError, ValueError) as error:
        raise Item7RuntimeError(_CAPTURE_STAGE, str(error)) from error
    frozen_files = _relative_files(request.frozen_config)
    captured_files = _relative_files(request.captured_config)
    if set(captured_files) != set(frozen_files) | set(chunky_paths):
        detail = "captured file inventory differs from Item 6 plus Chunky"
        raise Item7RuntimeError(_CAPTURE_STAGE, detail)
    normalized_drifts: list[RuntimeConfigDrift] = []
    for relative, source in frozen_files.items():
        expected = source.read_bytes()
        if relative == "server.properties":
            expected = replace_property(expected, "level-seed", materialized_seed(request))
        captured = captured_files[relative].read_bytes()
        if captured == expected:
            continue
        if relative not in _COMMENT_NORMALIZED_PATHS or _semantic_lines(
            captured
        ) != _semantic_lines(expected):
            raise Item7RuntimeError(_CAPTURE_STAGE, f"captured Item 6 file differs: {relative}")
        normalized_drifts.append(
            RuntimeConfigDrift(
                path=relative,
                frozen_sha256=_sha256_bytes(expected),
                captured_sha256=_sha256_bytes(captured),
            )
        )
    rows = tuple(
        ArtifactHash(path=relative, sha256=sha256_file(captured_files[relative]))
        for relative in chunky_paths
    )
    if len(frozen_files) != FROZEN_FILE_COUNT:
        detail = "frozen Item 6 inventory is not exactly 228 files"
        raise Item7RuntimeError(_CAPTURE_STAGE, detail)
    return ConfigCaptureReceipt(
        base_file_count=FROZEN_FILE_COUNT,
        chunky_files=rows,
        normalized_runtime_drifts=tuple(normalized_drifts),
    )


def _relative_files(root: Path) -> dict[str, Path]:
    return {
        path.relative_to(root).as_posix(): path
        for path in sorted(root.rglob("*"))
        if path.is_file()
    }


def _semantic_lines(content: bytes) -> tuple[str, ...]:
    return tuple(
        line
        for line in content.decode().splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    )


def _sha256_bytes(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()
