"""Shared Item 7 repeat-comparison reconstruction."""

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path
from typing import Final

from pydantic import JsonValue

from mcpack_evidence.item7_repeat import (
    ComparisonInputs,
    field_mismatch_counts,
    first_mismatch,
    normalized_sha256,
    write_receipt,
)
from mcpack_evidence.item7_repeat_aggregate import (
    ComparisonGeometry,
    SelectedRecords,
    load_aggregate_seed,
    load_comparison_protocol,
)
from mcpack_evidence.item7_repeat_selection import load_selection_seed

_RAW_REGION_HASH_TREATMENT: Final = "preserve_and_explain_not_compare"
type SeedLoader = Callable[
    [Path, str, ComparisonGeometry, str], tuple[dict[str, JsonValue], SelectedRecords]
]


def compare_runs(inputs: ComparisonInputs) -> bool:
    """Compare aggregate decoded Run A and Run B evidence and write its receipt."""
    payload = _rebuild(inputs.protocol, inputs.run_a_root, inputs.run_b_root, load_aggregate_seed)
    write_receipt(inputs.output, payload)
    return payload["equal"] is True


def rebuild_selection_comparison(protocol_path: Path, raw_root: Path) -> dict[str, JsonValue]:
    """Rebuild the repeat receipt from accepted selection JSONL sources."""
    return _rebuild(protocol_path, raw_root / "run-a", raw_root / "run-b", load_selection_seed)


def _rebuild(
    protocol_path: Path,
    run_a_root: Path,
    run_b_root: Path,
    loader: SeedLoader,
) -> dict[str, JsonValue]:
    protocol, protocol_sha = load_comparison_protocol(protocol_path)
    geometry = ComparisonGeometry.from_protocol(protocol)
    seeds: list[JsonValue] = []
    first: dict[str, JsonValue] | None = None
    for seed in protocol.seeds:
        manifest_a, selected_a = loader(run_a_root, seed.role, geometry, protocol_sha)
        manifest_b, selected_b = loader(run_b_root, seed.role, geometry, protocol_sha)
        selections: list[JsonValue] = []
        for index, selection in enumerate(protocol.selections):
            left, right = selected_a[index], selected_b[index]
            counts = field_mismatch_counts(
                (left, right), protocol.normalization.chunk_compare_fields
            )
            equal = not any(counts.values())
            selections.append(
                {
                    "label": selection.label,
                    "count": len(left),
                    "run_a_normalized_sha256": normalized_sha256(left),
                    "run_b_normalized_sha256": normalized_sha256(right),
                    "equal": equal,
                    "field_mismatch_counts": counts,
                }
            )
            if not equal and first is None:
                first = first_mismatch(
                    (seed.role, selection.label),
                    (left, right),
                    protocol.normalization.chunk_compare_fields,
                )
        seeds.append(
            {
                "role": seed.role,
                "seed": seed.seed,
                "selections": selections,
                "run_a_regions": manifest_a["regions"],
                "run_b_regions": manifest_b["regions"],
            }
        )
    return {
        "schema_version": "item7-repeat-comparison-v1",
        "protocol_sha256": protocol_sha,
        "raw_region_hash_treatment": _RAW_REGION_HASH_TREATMENT,
        "equal": first is None,
        "seeds": seeds,
        "first_mismatch": first,
    }
