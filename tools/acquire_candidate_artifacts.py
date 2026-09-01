"""Acquire and verify every exact Item 3 candidate artifact."""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import cast

from mcpack_evidence.item3_acquisition import (
    AcquiredArtifact,
    acquire_candidate,
    build_acquisition_manifest,
)
from mcpack_evidence.item3_source_models import SourceMatrix


def main() -> int:
    """Download exact source-matrix artifacts and persist verified identities."""
    parser = argparse.ArgumentParser()
    _ = parser.add_argument("--source-matrix", type=Path, required=True)
    _ = parser.add_argument("--download-root", type=Path, required=True)
    _ = parser.add_argument("--output", type=Path, required=True)
    _ = parser.add_argument("--workers", type=int, choices=range(1, 17), default=6)
    arguments = parser.parse_args()
    matrix = SourceMatrix.model_validate_json(cast("Path", arguments.source_matrix).read_bytes())
    root = cast("Path", arguments.download_root)
    workers = cast("int", arguments.workers)
    rows: dict[str, AcquiredArtifact] = {}
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {
            executor.submit(acquire_candidate, candidate, root): candidate.candidate_filename
            for candidate in matrix.candidates
        }
        for completed, future in enumerate(as_completed(futures), start=1):
            row = future.result()
            rows[row.candidate_filename] = row
            message = (
                f"[{completed:03d}/{matrix.inventory_count:03d}] "
                f"{row.acquisition}: {row.candidate_filename}"
            )
            print(
                message,
                flush=True,
            )
    ordered = tuple(rows[candidate.candidate_filename] for candidate in matrix.candidates)
    manifest = build_acquisition_manifest(ordered)
    output = cast("Path", arguments.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    _ = output.write_text(manifest.model_dump_json(indent=2) + "\n", encoding="utf-8")
    print(f"verified {manifest.candidate_count} files ({manifest.total_size_bytes} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
