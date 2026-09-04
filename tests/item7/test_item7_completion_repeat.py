from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import TYPE_CHECKING

import pytest

from mcpack_evidence.item7_completion_io import CompletionError
from mcpack_evidence.item7_completion_repeat import validate_repeat
from mcpack_evidence.item7_protocol import load_protocol

if TYPE_CHECKING:
    from pydantic import JsonValue

    from mcpack_evidence.item7_protocol import Item7Protocol


ROOT = Path(__file__).parents[2]
PROTOCOL_PATH = ROOT / "evidence/item-7/protocol/worldgen-audit-v1.json"


def _identity(path: Path, record_count: int) -> dict[str, str | int]:
    return {
        "path": path.name,
        "size_bytes": path.stat().st_size,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "record_count": record_count,
    }


def _selection_records(protocol: Item7Protocol, label: str) -> list[JsonValue]:
    selection = next(row for row in protocol.selections if row.label == label)
    center_x, center_z = selection.center_x // 16, selection.center_z // 16
    return [
        {
            "schema_version": "item7-anvil-chunk-v1",
            "dimension": selection.dimension,
            "region": "region/r.0.0.mca",
            "slot": (chunk_x % 32) + (chunk_z % 32) * 32,
            "timestamp": 0,
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
        for chunk_x in range(
            center_x - selection.radius_chunks, center_x + selection.radius_chunks + 1
        )
        for chunk_z in range(
            center_z - selection.radius_chunks, center_z + selection.radius_chunks + 1
        )
    ]


def _write_sources(raw_root: Path, protocol: Item7Protocol) -> None:
    protocol_sha = hashlib.sha256(PROTOCOL_PATH.read_bytes()).hexdigest()
    selections = [
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
    ]
    manifest = {
        "schema_version": "item7-world-manifest-v1",
        "mode": "run",
        "regions": [],
        "external_chunks": [],
        "selections": selections,
        "extra_chunks": [],
        "decoded": {
            "path": "chunks.jsonl",
            "size_bytes": 0,
            "sha256": "a" * 64,
            "record_count": 0,
        },
    }
    for run_id in ("run-a", "run-b"):
        for seed in protocol.seeds:
            root = raw_root / run_id / seed.role
            selected_root = root / "selections"
            selected_root.mkdir(parents=True)
            _ = (root / "world-manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
            for selection in protocol.selections:
                selected = selected_root / f"{selection.label}.jsonl"
                records = _selection_records(protocol, selection.label)
                _ = selected.write_text(
                    "".join(json.dumps(row, separators=(",", ":")) + "\n" for row in records),
                    encoding="utf-8",
                )
                receipt = {
                    "schema_version": "item7-selection-extract-receipt-v1",
                    "protocol": {
                        "path": "worldgen-audit-v1.json",
                        "size_bytes": PROTOCOL_PATH.stat().st_size,
                        "sha256": protocol_sha,
                        "record_count": 1,
                    },
                    "world_manifest": {
                        "path": "world-manifest.json",
                        "size_bytes": (root / "world-manifest.json").stat().st_size,
                        "sha256": hashlib.sha256(
                            (root / "world-manifest.json").read_bytes()
                        ).hexdigest(),
                        "record_count": 1,
                    },
                    "aggregate": {
                        "path": "chunks.jsonl",
                        "size_bytes": 0,
                        "sha256": "a" * 64,
                        "record_count": 0,
                    },
                    "selection": selections[protocol.selections.index(selection)],
                    "selected": _identity(selected, len(records)),
                }
                _ = selected.with_suffix(".jsonl.receipt.json").write_text(
                    json.dumps(receipt), encoding="utf-8"
                )


def _forged_report(protocol: Item7Protocol, protocol_sha: str) -> dict[str, JsonValue]:
    fields: dict[str, JsonValue] = {
        "schema_version": 0,
        "dimension": 0,
        "slot": 0,
        "chunk_x": 0,
        "chunk_z": 0,
        "data_version": 0,
        "status": 0,
        "full": 0,
        "heightmaps": 0,
        "biome_sections": 0,
        "structure_starts": 0,
    }
    fields["heightmaps"] = 1
    seeds: list[JsonValue] = []
    for seed in protocol.seeds:
        selections: list[JsonValue] = [
            {
                "label": selection.label,
                "count": selection.expected_chunk_count,
                "run_a_normalized_sha256": "a" * 64,
                "run_b_normalized_sha256": "b" * 64,
                "equal": False,
                "field_mismatch_counts": fields,
            }
            for selection in protocol.selections
        ]
        seeds.append(
            {
                "role": seed.role,
                "seed": seed.seed,
                "selections": selections,
                "run_a_regions": [],
                "run_b_regions": [],
            }
        )
    return {
        "schema_version": "item7-repeat-comparison-v1",
        "protocol_sha256": protocol_sha,
        "raw_region_hash_treatment": "preserve_and_explain_not_compare",
        "equal": False,
        "first_mismatch": {"field": "heightmaps"},
        "seeds": seeds,
    }


def test_validate_repeat_rebuilds_all_selection_sources_before_accepting_nondeterminism(
    tmp_path: Path,
) -> None:
    # Given: every accepted Run A and Run B selection stream has identical semantics.
    protocol = load_protocol(PROTOCOL_PATH)
    _write_sources(tmp_path, protocol)
    comparison = tmp_path / "repeat-comparison.json"
    protocol_sha = hashlib.sha256(PROTOCOL_PATH.read_bytes()).hexdigest()
    _ = comparison.write_text(json.dumps(_forged_report(protocol, protocol_sha)), encoding="utf-8")

    # When: completion validates a stale report that claims semantic nondeterminism.
    # Then: the report is rejected because the rebuilt comparison is equal.
    with pytest.raises(CompletionError, match="repeat comparison source binding"):
        _ = validate_repeat(comparison, PROTOCOL_PATH)
