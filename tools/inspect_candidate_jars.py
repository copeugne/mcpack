"""Inspect all exact Item 3 candidate archives and embedded metadata."""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import UTC, datetime
from pathlib import Path
from typing import cast

from mcpack_evidence.item3_acquisition import ArtifactAcquisitionManifest
from mcpack_evidence.item3_jar import inspect_candidate_jar
from mcpack_evidence.item3_jar_models import CandidateJarInspection, JarInspectionReport


def main() -> int:
    """Inspect acquisition-manifest JARs and persist normalized results."""
    parser = argparse.ArgumentParser()
    _ = parser.add_argument("--acquisition-manifest", type=Path, required=True)
    _ = parser.add_argument("--output", type=Path, required=True)
    _ = parser.add_argument("--workers", type=int, choices=range(1, 17), default=6)
    arguments = parser.parse_args()
    acquisition = ArtifactAcquisitionManifest.model_validate_json(
        cast("Path", arguments.acquisition_manifest).read_bytes()
    )
    rows: dict[str, CandidateJarInspection] = {}
    with ThreadPoolExecutor(max_workers=cast("int", arguments.workers)) as executor:
        futures = {
            executor.submit(
                inspect_candidate_jar,
                artifact.candidate_filename,
                Path(artifact.local_path),
                artifact.identity.computed_sha256,
            ): artifact.candidate_filename
            for artifact in acquisition.artifacts
        }
        for completed, future in enumerate(as_completed(futures), start=1):
            row = future.result()
            rows[row.candidate_filename] = row
            message = (
                f"[{completed:03d}/{acquisition.candidate_count:03d}] "
                f"{row.inspection_status}: {row.candidate_filename}"
            )
            print(
                message,
                flush=True,
            )
    ordered = tuple(rows[row.candidate_filename] for row in acquisition.artifacts)
    report = JarInspectionReport(
        schema_version="item3-jar-inspection-v1",
        generated_at=datetime.now(UTC).isoformat(),
        candidate_count=len(ordered),
        all_inspections_passed=all(row.inspection_status == "pass" for row in ordered),
        candidates=ordered,
    )
    output = cast("Path", arguments.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    _ = output.write_text(report.model_dump_json(indent=2) + "\n", encoding="utf-8")
    return 0 if report.all_inspections_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
