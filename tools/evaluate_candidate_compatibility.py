#!/usr/bin/env python3
"""Evaluate Item 3 candidate metadata using captured Maven oracle results."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from mcpack_evidence.item3_compatibility import evaluate_compatibility
from mcpack_evidence.item3_jar_models import JarInspectionReport


def main() -> None:
    """Load inspection evidence and emit a deterministic static compatibility report."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--inspection", type=Path, required=True)
    parser.add_argument("--oracle-requests", type=Path)
    parser.add_argument("--oracle-results", type=Path)
    parser.add_argument(
        "--provider-candidates",
        type=Path,
        help="newline-delimited installed candidate filenames; defaults to the full inventory",
    )
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    inspection = JarInspectionReport.model_validate_json(
        args.inspection.read_text(encoding="utf-8")
    )
    if bool(args.oracle_requests) != bool(args.oracle_results):
        parser.error("--oracle-requests and --oracle-results must be supplied together")
    results = (
        _read_results(args.oracle_requests, args.oracle_results) if args.oracle_results else {}
    )
    report = evaluate_compatibility(
        inspection,
        lambda version, version_range: results.get(
            (version, version_range), "missing_oracle_result"
        ),
        _read_provider_candidates(args.provider_candidates),
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    _ = args.output.write_text(
        json.dumps(report.model_dump(mode="json"), indent=2, sort_keys=False) + "\n",
        encoding="utf-8",
    )


def _read_provider_candidates(path: Path | None) -> frozenset[str] | None:
    if path is None:
        return None
    return frozenset(path.read_text(encoding="utf-8").splitlines())


def _read_results(request_path: Path, result_path: Path) -> dict[tuple[str, str], str]:
    requests: dict[str, tuple[str, str]] = {}
    expected_field_count = 3
    for line_number, line in enumerate(
        request_path.read_text(encoding="utf-8").splitlines(), start=1
    ):
        fields = line.split("\t")
        if len(fields) != expected_field_count:
            message = f"{request_path}:{line_number}: expected probe_id, version, range"
            raise ValueError(message)
        probe_id, version, version_range = fields
        requests[probe_id] = (version, version_range)
    results: dict[tuple[str, str], str] = {}
    for line_number, line in enumerate(
        result_path.read_text(encoding="utf-8").splitlines(), start=1
    ):
        fields = line.split("\t", 2)
        if len(fields) != expected_field_count:
            message = f"{result_path}:{line_number}: expected probe_id, status, detail"
            raise ValueError(message)
        probe_id, status, _detail = fields
        if probe_id not in requests:
            message = f"{result_path}:{line_number}: unknown probe id {probe_id!r}"
            raise ValueError(message)
        key = requests[probe_id]
        previous = results.setdefault(key, status)
        if previous != status:
            message = f"conflicting oracle results for {key[0]!r} and {key[1]!r}"
            raise ValueError(message)
    missing = requests.keys() - {
        line.split("\t", 1)[0] for line in result_path.read_text(encoding="utf-8").splitlines()
    }
    if missing:
        message = f"missing oracle results: {sorted(missing)!r}"
        raise ValueError(message)
    return results


if __name__ == "__main__":
    main()
