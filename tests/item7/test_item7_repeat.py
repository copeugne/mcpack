from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path
from typing import TYPE_CHECKING, ClassVar, Literal

import pytest
from pydantic import BaseModel, ConfigDict
from tools.compare_item7_runs import compare_runs

from mcpack_evidence.item7_nbt import ChunkRecord
from mcpack_evidence.item7_protocol import load_protocol
from mcpack_evidence.item7_repeat import (
    ComparisonInputs,
    RepeatComparisonError,
    RepeatRegion,
    RepeatWorldManifest,
)

if TYPE_CHECKING:
    from collections.abc import Iterator

ROOT = Path(__file__).parents[2]
PROTOCOL = ROOT / "evidence/item-7/protocol/worldgen-audit-v1.json"


class _MismatchView(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(extra="forbid", strict=True)

    seed_role: str
    selection: str
    dimension: str
    chunk_x: int
    chunk_z: int
    field: str


class _SelectionView(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(extra="forbid", strict=True)

    label: str
    count: int
    run_a_normalized_sha256: str
    run_b_normalized_sha256: str
    equal: bool


class _SeedView(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(extra="forbid", strict=True)

    role: str
    seed: str
    selections: tuple[_SelectionView, ...]
    run_a_regions: tuple[RepeatRegion, ...]
    run_b_regions: tuple[RepeatRegion, ...]


class _ReceiptView(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(extra="forbid", strict=True)

    schema_version: Literal["item7-repeat-comparison-v1"]
    protocol_sha256: str
    raw_region_hash_treatment: Literal["preserve_and_explain_not_compare"]
    equal: bool
    seeds: tuple[_SeedView, ...]
    first_mismatch: _MismatchView | None


def _records() -> Iterator[dict[str, str | int | bool | list[dict[str, str]]]]:
    protocol = load_protocol(PROTOCOL)
    for selection in protocol.selections:
        center_x, center_z = selection.center_x // 16, selection.center_z // 16
        radius = selection.radius_chunks
        for chunk_x in range(center_x - radius, center_x + radius + 1):
            for chunk_z in range(center_z - radius, center_z + radius + 1):
                yield {
                    "schema_version": "item7-anvil-chunk-v1",
                    "dimension": selection.dimension,
                    "region": f"region/r.{chunk_x // 32}.{chunk_z // 32}.mca",
                    "slot": (chunk_x % 32) + (chunk_z % 32) * 32,
                    "timestamp": 100,
                    "chunk_x": chunk_x,
                    "chunk_z": chunk_z,
                    "data_version": 3955,
                    "status": "minecraft:full",
                    "full": True,
                    "compression": "zlib",
                    "external": False,
                    "heightmaps": [],
                    "biome_sections": [],
                    "structure_starts": [],
                }


def _seed_evidence(root: Path, role: str, *, transport_variant: bool = False) -> None:
    seed_dir = root / role
    seed_dir.mkdir(parents=True)
    decoded = seed_dir / "chunks.jsonl"
    with decoded.open("w", encoding="utf-8", newline="\n") as stream:
        for record in _records():
            if transport_variant:
                record["region"] = "different/r.0.0.mca"
                record["timestamp"] = 999
                record["compression"] = "gzip"
                record["external"] = True
            _ = stream.write(json.dumps(record, separators=(",", ":")) + "\n")
    protocol = load_protocol(PROTOCOL)
    sha256 = hashlib.sha256(decoded.read_bytes()).hexdigest()
    payload = {
        "schema_version": "item7-world-manifest-v1",
        "mode": "run",
        "regions": [
            {
                "path": "region/r.0.0.mca",
                "dimension": "minecraft:overworld",
                "region_x": 0,
                "region_z": 0,
                "size_bytes": 8192,
                "sha256": ("b" if transport_variant else "a") * 64,
                "zero_byte_placeholder": False,
                "decoded_chunk_count": sum(1 for _ in _records()),
            }
        ],
        "external_chunks": [],
        "selections": [
            {
                "label": row.label,
                "dimension": row.dimension,
                "center_block_x": row.center_x,
                "center_block_z": row.center_z,
                "radius_chunks": row.radius_chunks,
                "expected_chunk_count": row.expected_chunk_count,
                "observed_chunk_count": row.expected_chunk_count,
            }
            for row in protocol.selections
        ],
        "extra_chunks": [],
        "decoded": {
            "path": decoded.name,
            "size_bytes": decoded.stat().st_size,
            "sha256": sha256,
            "record_count": sum(1 for _ in _records()),
        },
    }
    _ = seed_dir.joinpath("world-manifest.json").write_text(
        json.dumps(payload, indent=2) + "\n", encoding="utf-8"
    )


def _run_pair(tmp_path: Path) -> ComparisonInputs:
    run_a, run_b = tmp_path / "run-a", tmp_path / "run-b"
    for seed in load_protocol(PROTOCOL).seeds:
        _seed_evidence(run_a, seed.role)
        _seed_evidence(run_b, seed.role, transport_variant=True)
    return ComparisonInputs(PROTOCOL, run_a, run_b, tmp_path / "comparison.json")


def test_compare_runs_normalizes_transport_fields_and_preserves_region_hashes(
    tmp_path: Path,
) -> None:
    inputs = _run_pair(tmp_path)

    _ = compare_runs(inputs)
    receipt = _ReceiptView.model_validate_json(inputs.output.read_bytes(), strict=True)

    assert receipt.equal is True
    assert receipt.first_mismatch is None
    assert len(receipt.seeds) == 4
    assert all(sum(row.count for row in seed.selections) == 6852 for seed in receipt.seeds)
    assert receipt.seeds[0].run_a_regions[0].sha256 == "a" * 64
    assert receipt.seeds[0].run_b_regions[0].sha256 == "b" * 64


def test_compare_runs_reports_first_semantic_mismatch(tmp_path: Path) -> None:
    inputs = _run_pair(tmp_path)
    decoded = inputs.run_b_root / "ordinary" / "chunks.jsonl"
    lines = decoded.read_text(encoding="utf-8").splitlines()
    changed = ChunkRecord.model_validate_json(lines[0], strict=True).model_copy(
        update={"data_version": 4000}
    )
    lines[0] = changed.model_dump_json()
    _ = decoded.write_text("\n".join(lines) + "\n", encoding="utf-8")
    manifest = inputs.run_b_root / "ordinary" / "world-manifest.json"
    payload = RepeatWorldManifest.model_validate_json(manifest.read_bytes(), strict=True)
    identity = payload.decoded.model_copy(
        update={
            "sha256": hashlib.sha256(decoded.read_bytes()).hexdigest(),
            "size_bytes": decoded.stat().st_size,
        }
    )
    _ = manifest.write_text(
        payload.model_copy(update={"decoded": identity}).model_dump_json(), encoding="utf-8"
    )

    _ = compare_runs(inputs)
    receipt = _ReceiptView.model_validate_json(inputs.output.read_bytes(), strict=True)

    assert receipt.equal is False
    assert receipt.first_mismatch is not None
    assert (
        receipt.first_mismatch.seed_role,
        receipt.first_mismatch.selection,
        receipt.first_mismatch.dimension,
        receipt.first_mismatch.chunk_x,
        receipt.first_mismatch.chunk_z,
        receipt.first_mismatch.field,
    ) == ("ordinary", "overworld", "minecraft:overworld", -31, -31, "data_version")


type _Failure = Literal["stale", "duplicate", "missing", "nonfull", "escape"]


@pytest.mark.parametrize("failure", ["stale", "duplicate", "missing", "nonfull", "escape"])
def test_compare_runs_rejects_untrusted_evidence(tmp_path: Path, failure: _Failure) -> None:
    inputs = _run_pair(tmp_path)
    _ = inputs.output.write_bytes(b"old receipt")
    seed_dir = inputs.run_b_root / "ordinary"
    decoded = seed_dir / "chunks.jsonl"
    manifest = seed_dir / "world-manifest.json"
    payload = RepeatWorldManifest.model_validate_json(manifest.read_bytes(), strict=True)
    lines = decoded.read_text(encoding="utf-8").splitlines()
    if failure == "stale":
        lines[0] += " "
    if failure == "duplicate":
        lines[1] = lines[0]
    if failure == "missing":
        _ = lines.pop()
    if failure == "nonfull":
        row = ChunkRecord.model_validate_json(lines[0], strict=True)
        lines[0] = row.model_copy(update={"full": False}).model_dump_json()
    if failure == "escape":
        identity = payload.decoded.model_copy(update={"path": "../chunks.jsonl"})
        payload = payload.model_copy(update={"decoded": identity})
    if failure == "escape":
        _ = manifest.write_text(payload.model_dump_json(), encoding="utf-8")
    else:
        _ = decoded.write_text("\n".join(lines) + "\n", encoding="utf-8")
        if failure != "stale":
            identity = payload.decoded.model_copy(
                update={
                    "sha256": hashlib.sha256(decoded.read_bytes()).hexdigest(),
                    "size_bytes": decoded.stat().st_size,
                    "record_count": len(lines),
                }
            )
            region = payload.regions[0].model_copy(update={"decoded_chunk_count": len(lines)})
            payload = payload.model_copy(update={"decoded": identity, "regions": (region,)})
        _ = manifest.write_text(payload.model_dump_json(), encoding="utf-8")

    with pytest.raises(RepeatComparisonError, match=failure):
        _ = compare_runs(inputs)
    assert inputs.output.read_bytes() == b"old receipt"


def test_compare_runs_rejects_duplicate_json_keys(tmp_path: Path) -> None:
    inputs = _run_pair(tmp_path)
    manifest = inputs.run_b_root / "ordinary" / "world-manifest.json"
    text = manifest.read_text(encoding="utf-8").replace(
        "{\n", '{\n  "schema_version": "duplicate",\n', 1
    )
    _ = manifest.write_text(text, encoding="utf-8")

    with pytest.raises(RepeatComparisonError, match="strict"):
        _ = compare_runs(inputs)


def test_cli_emits_equal_receipt_for_complete_run_pair(tmp_path: Path) -> None:
    inputs = _run_pair(tmp_path)

    completed = subprocess.run(  # noqa: S603 - the active uv Python runs a tracked script.
        [
            sys.executable,
            "tools/compare_item7_runs.py",
            "--protocol",
            str(inputs.protocol),
            "--run-a",
            str(inputs.run_a_root),
            "--run-b",
            str(inputs.run_b_root),
            "--output",
            str(inputs.output),
        ],
        check=False,
        capture_output=True,
        text=True,
    )
    receipt = _ReceiptView.model_validate_json(inputs.output.read_bytes(), strict=True)

    assert completed.returncode == 0
    assert receipt.equal is True
