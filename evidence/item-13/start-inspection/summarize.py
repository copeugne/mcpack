"""Join the full baseline inspection to its candidates without losing cases."""

# pyright: standard
# ruff: noqa: D103, EM101, TRY003, INP001, T201, ANN201, ANN001
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path

from tools.analyze_route_opportunities import ROOT, read_bound

from mcpack_evidence.item8_pool_links import _versioned_edges


def named_components(value):  # noqa: C901 - saved ordinary, custom and versioned components.
    names = set()
    if isinstance(value, dict):
        if value.get("element_type") == "moogs_structures:versioned_single_pool_element":
            for edge in _versioned_edges(value.get("locations"), "/saved_pool_element"):
                if not isinstance(edge, dict):
                    raise TypeError("version resolver returned a non-object edge")
                if edge.get("selected"):
                    name = edge["id"]
                    if not isinstance(name, str):
                        raise TypeError("version resolver returned a non-text template")
                    names.add(name)
            return names
        for key, child in value.items():
            if key in {"Template", "location"} and isinstance(child, str):
                names.add(child)
            else:
                names.update(named_components(child))
    elif isinstance(value, list):
        for child in value:
            names.update(named_components(child))
    return names


def main(directory=None) -> None:
    directory = directory or Path(__file__).parent
    candidate_raw = read_bound(ROOT / "evidence/item-13/candidates.json")
    index = json.loads(candidate_raw)
    candidates = {r["id"]: r for r in index["candidates"]}
    execution = [json.loads(line) for line in read_bound(directory / "execution.txt").splitlines()]
    worlds = sorted(index["worlds"])
    if len(execution) != len(worlds):
        raise ValueError("full baseline execution is incomplete")
    groups = {}
    totals = {"starts": 0, "incomplete_starts": 0, "incomplete_envelopes": 0}
    for name, run in zip(worlds, execution, strict=True):
        raw = read_bound(directory / f"{name}.json.gz", run["sha256"])
        result = json.loads(gzip.decompress(raw))
        if (
            result["world"] != name
            or result["candidate_sha256"] != hashlib.sha256(candidate_raw).hexdigest()
            or result["world_backup_sha256"] != index["worlds"][name]["world_backup_sha256"]
        ):
            raise ValueError("inspection input identity mismatch")
        starts = result["starts"]
        expected = {k for k, c in candidates.items() if c["world"] == name}
        if (
            len(starts) != run["starts"]
            or len(starts) != len(expected)
            or {r["id"] for r in starts} != expected
        ):
            raise ValueError("inspection omits or duplicates a candidate")
        for row in starts:
            case = candidates[row["id"]]
            start = row.get("start_nbt")
            if start is not None:
                bounds = [child["BB"] for child in start["Children"]]
                digest = hashlib.sha256(
                    json.dumps(bounds, separators=(",", ":")).encode()
                ).hexdigest()
                if digest != case["piece_bounds_sha256"]:
                    raise ValueError("saved bounds disagree with accepted census")
            key = case["family_id"] + "|" + case["root"] + "|" + case["dimension"]
            group = groups.setdefault(key, [])
            group.append(
                {
                    "id": row["id"],
                    "seed_role": case["seed_role"],
                    "start_status": row["status"],
                    "incomplete_chunks": row["incomplete_chunks"],
                    "required_chunks": row["required_chunks"],
                    "named_components": sorted(named_components(start)),
                    "component_record_types": sorted({c["id"] for c in start["Children"]})
                    if start
                    else [],
                }
            )
            totals["starts"] += 1
            totals["incomplete_starts"] += row["status"] != "SAVED"
            totals["incomplete_envelopes"] += bool(row["incomplete_chunks"])
    print(
        json.dumps(
            {
                "totals": totals,
                "family_root_dimension_candidates": groups,
                "scope": "Assembly membership and saved chunks, not playable topology",
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--directory", type=Path)
    main(parser.parse_args().directory)
