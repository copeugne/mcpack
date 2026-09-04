from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

import pytest

from mcpack_evidence.item7_nbt import ChunkRecord
from mcpack_evidence.item7_protocol import load_protocol
from mcpack_evidence.item7_selection_extract import (
    SelectionExtractError,
    SelectionReceipt,
    extract_selection,
)

ROOT = Path(__file__).parents[2]
PROTOCOL = ROOT / "evidence/item-7/protocol/worldgen-audit-v1.json"


def _record(dimension: str, chunk_x: int, chunk_z: int, *, full: bool = True) -> dict[str, object]:
    return {
        "schema_version": "item7-anvil-chunk-v1",
        "dimension": dimension,
        "region": f"region/r.{chunk_x // 32}.{chunk_z // 32}.mca",
        "slot": (chunk_x % 32) + (chunk_z % 32) * 32,
        "timestamp": 100,
        "chunk_x": chunk_x,
        "chunk_z": chunk_z,
        "data_version": 3955,
        "status": "minecraft:full" if full else "minecraft:carvers",
        "full": full,
        "compression": "zlib",
        "external": False,
        "heightmaps": [],
        "biome_sections": [],
        "structure_starts": [],
    }


def _coordinates(label: str) -> list[dict[str, object]]:
    protocol = load_protocol(PROTOCOL)
    selection = next(row for row in protocol.selections if row.label == label)
    center_x, center_z = selection.center_x // 16, selection.center_z // 16
    return [
        _record(selection.dimension, chunk_x, chunk_z)
        for chunk_x in range(
            center_x - selection.radius_chunks, center_x + selection.radius_chunks + 1
        )
        for chunk_z in range(
            center_z - selection.radius_chunks, center_z + selection.radius_chunks + 1
        )
    ]


def _evidence(root: Path, records: list[dict[str, object]]) -> tuple[Path, Path, Path]:
    aggregate = root / "chunks.jsonl"
    _ = aggregate.write_bytes(
        b"".join(json.dumps(row, sort_keys=True).encode() + b"\n" for row in records)
    )
    protocol = load_protocol(PROTOCOL)
    manifest = root / "world-manifest.json"
    payload = {
        "schema_version": "item7-world-manifest-v1",
        "mode": "run",
        "regions": [],
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
            "path": aggregate.name,
            "size_bytes": aggregate.stat().st_size,
            "sha256": hashlib.sha256(aggregate.read_bytes()).hexdigest(),
            "record_count": len(records),
        },
    }
    _ = manifest.write_text(json.dumps(payload), encoding="utf-8")
    return PROTOCOL, manifest, aggregate


@pytest.mark.parametrize("label", ["overworld", "nether", "end-central", "end-outer"])
def test_extracts_every_frozen_selection_once(tmp_path: Path, label: str) -> None:
    protocol, manifest, aggregate = _evidence(
        tmp_path, [*_coordinates(label), _record("minecraft:overworld", 999, 999)]
    )
    output = tmp_path / f"{label}.jsonl"

    receipt = extract_selection(protocol, manifest, aggregate, label, output)

    assert receipt.selection.label == label
    assert receipt.selected.record_count == len(_coordinates(label))
    assert len(output.read_bytes().splitlines()) == len(_coordinates(label))


def test_end_outer_block_center_maps_to_chunk_96(tmp_path: Path) -> None:
    protocol, manifest, aggregate = _evidence(tmp_path, _coordinates("end-outer"))
    output = tmp_path / "end.jsonl"

    _ = extract_selection(protocol, manifest, aggregate, "end-outer", output)

    records = [
        ChunkRecord.model_validate_json(line, strict=True)
        for line in output.read_text().splitlines()
    ]
    coordinates = {(record.chunk_x, record.chunk_z) for record in records}
    assert (96, 0) in coordinates
    assert min(x for x, _ in coordinates) == 81
    assert max(x for x, _ in coordinates) == 111


@pytest.mark.parametrize(
    "variant", ["missing", "duplicate", "nonfull", "malformed", "hash", "escape"]
)
def test_rejects_unbound_or_incomplete_evidence(tmp_path: Path, variant: str) -> None:
    records = _coordinates("nether")
    protocol, manifest, aggregate = _evidence(tmp_path, records)
    output = tmp_path / "selected.jsonl"
    receipt = output.with_suffix(".jsonl.receipt.json")
    _ = output.write_bytes(b"old selected")
    _ = receipt.write_bytes(b"old receipt")
    match variant:
        case "missing":
            _ = records.pop()
            protocol, manifest, aggregate = _evidence(tmp_path, records)
        case "duplicate":
            records.append(records[0])
            protocol, manifest, aggregate = _evidence(tmp_path, records)
        case "nonfull":
            records[0] = _record("minecraft:the_nether", -15, -15, full=False)
            protocol, manifest, aggregate = _evidence(tmp_path, records)
        case "malformed":
            _ = aggregate.write_bytes(aggregate.read_bytes() + b"{not-json}\n")
        case "hash":
            original = hashlib.sha256(aggregate.read_bytes()).hexdigest()
            _ = manifest.write_text(
                manifest.read_text().replace(original, "0" * 64), encoding="utf-8"
            )
        case "escape":
            _ = manifest.write_text(
                manifest.read_text().replace('"path": "chunks.jsonl"', '"path": "../chunks.jsonl"'),
                encoding="utf-8",
            )
        case unreachable:
            pytest.fail(f"unexpected test variant: {unreachable}")

    with pytest.raises(SelectionExtractError):
        _ = extract_selection(protocol, manifest, aggregate, "nether", output)
    assert (output.read_bytes(), receipt.read_bytes()) == (b"old selected", b"old receipt")


def test_cli_writes_receipt_bound_to_exact_aggregate(tmp_path: Path) -> None:
    protocol, manifest, aggregate = _evidence(tmp_path, _coordinates("nether"))
    output = tmp_path / "nether.jsonl"

    completed = subprocess.run(  # noqa: S603 - test invokes the repository-owned CLI.
        [
            sys.executable,
            "tools/extract_item7_selection.py",
            str(protocol),
            str(manifest),
            str(aggregate),
            "nether",
            str(output),
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert completed.returncode == 0, completed.stderr
    receipt = SelectionReceipt.model_validate_json(
        output.with_suffix(".jsonl.receipt.json").read_bytes(), strict=True
    )
    assert receipt.aggregate.sha256 == hashlib.sha256(aggregate.read_bytes()).hexdigest()
