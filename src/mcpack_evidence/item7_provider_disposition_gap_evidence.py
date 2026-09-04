"""Accepted targeted-run evidence for Item 7 provider closure."""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import ClassVar, Literal

from pydantic import BaseModel, ConfigDict, ValidationError

from mcpack_evidence.item6_json import StrictJsonError, parse_strict_json
from mcpack_evidence.item7_config import ConfigCaptureReceipt  # noqa: TC001
from mcpack_evidence.item7_gap import GAP_TARGETS, GapLifecycleReceipt
from mcpack_evidence.item7_nbt import ChunkRecord
from mcpack_evidence.item7_provider_disposition_models import FileBinding, SavedStart
from mcpack_evidence.item7_runtime import PreflightReceipt  # noqa: TC001

_TARGETS = tuple(target.structure for target in GAP_TARGETS)
_LOCATIONS = ((-736, -4624), (656, -5120), (1040, -13920), (-1792, -10592))


class ProviderDispositionError(ValueError):
    """One strict provider-disposition boundary failed."""


class _GapReceipt(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid", strict=True)
    schema_version: Literal["item7-gap-run-v1"]
    preflight: PreflightReceipt
    lifecycle: GapLifecycleReceipt
    configuration: ConfigCaptureReceipt
    rejection_reason: None


@dataclass(frozen=True, slots=True)
class GapEvidence:
    """Validated targeted-run starts, identities, and runtime log."""

    starts: dict[str, SavedStart]
    inputs: tuple[FileBinding, ...]
    preflight: PreflightReceipt
    log: str


def resolve(root: Path, relative: Path) -> Path:
    """Resolve one real evidence file without permitting a root escape."""
    if relative.is_absolute() or not relative.parts or ".." in relative.parts:
        detail = f"evidence path is not relative: {relative}"
        raise ProviderDispositionError(detail)
    path = root / relative
    try:
        _ = path.resolve().relative_to(root.resolve())
    except ValueError as error:
        detail = f"evidence path escapes root: {relative}"
        raise ProviderDispositionError(detail) from error
    if path.is_symlink() or not path.is_file():
        detail = f"evidence input is not a real file: {relative}"
        raise ProviderDispositionError(detail)
    return path


def binding(path: Path, display: str, record_count: int) -> FileBinding:
    """Bind one input's content identity and meaningful record count."""
    content = path.read_bytes()
    return FileBinding(
        path=display,
        sha256=hashlib.sha256(content).hexdigest(),
        size_bytes=len(content),
        record_count=record_count,
    )


def parse[Model: BaseModel](model: type[Model], path: Path) -> Model:
    """Strictly parse one Pydantic evidence boundary."""
    try:
        return model.model_validate_json(
            json.dumps(parse_strict_json(path.read_bytes()), separators=(",", ":"))
        )
    except (OSError, StrictJsonError, ValidationError) as error:
        detail = f"invalid evidence JSON: {path}"
        raise ProviderDispositionError(detail) from error


def load_gap(root: Path, relative: Path, name: Literal["gap-a", "gap-b"]) -> GapEvidence:
    """Verify lifecycle, frozen identity, decoded seal, and one saved target each."""
    receipt_path = resolve(root, relative / "run-receipt.json")
    decoded_path = resolve(root, relative / "chunks.jsonl")
    log_path = resolve(root, relative / "gap-minecraft-latest.log")
    receipt = parse(_GapReceipt, receipt_path)
    lifecycle = receipt.lifecycle
    if (
        not lifecycle.ready
        or not lifecycle.save_all_flush
        or not lifecycle.clean_stop
        or lifecycle.return_code != 0
        or lifecycle.process_group_killed
        or tuple(item.structure for item in lifecycle.located_targets) != _TARGETS
        or tuple((item.x, item.z) for item in lifecycle.located_targets) != _LOCATIONS
        or lifecycle.completed_targets != _TARGETS
        or lifecycle.minecraft_log is None
        or Path(lifecycle.minecraft_log).name != log_path.name
    ):
        detail = f"gap lifecycle is not accepted: {relative}"
        raise ProviderDispositionError(detail)
    content = decoded_path.read_bytes()
    lines = tuple(line for line in content.splitlines(keepends=True) if line.strip())
    starts: dict[str, SavedStart] = {}
    for line in lines:
        try:
            record = ChunkRecord.model_validate_json(
                json.dumps(parse_strict_json(line), separators=(",", ":"))
            )
        except (StrictJsonError, ValidationError) as error:
            detail = f"invalid gap decoded record: {relative}"
            raise ProviderDispositionError(detail) from error
        for start in record.structure_starts:
            if start.structure_id in _TARGETS:
                if start.structure_id in starts:
                    detail = f"duplicate targeted saved start: {start.structure_id}"
                    raise ProviderDispositionError(detail)
                starts[start.structure_id] = SavedStart(
                    run=name,
                    structure_id=start.structure_id,
                    chunk_x=record.chunk_x,
                    chunk_z=record.chunk_z,
                )
    if tuple(sorted(starts)) != _TARGETS:
        detail = f"gap saved starts differ from targets: {relative}"
        raise ProviderDispositionError(detail)
    return GapEvidence(
        starts,
        (
            binding(receipt_path, f"raw/{relative}/run-receipt.json", 1),
            binding(decoded_path, f"raw/{relative}/chunks.jsonl", len(lines)),
            binding(
                log_path,
                f"raw/{relative}/gap-minecraft-latest.log",
                len(log_path.read_text().splitlines()),
            ),
        ),
        receipt.preflight,
        log_path.read_text(encoding="utf-8"),
    )
