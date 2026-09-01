#!/usr/bin/env python3
"""Generate the Item 3 embedded-library overlap report."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from mcpack_evidence.item3_jar_models import JarInspectionReport
from mcpack_evidence.item3_overlap import build_overlap_report


def main() -> None:
    """Build and persist a deterministic report from committed JAR inspection evidence."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--inspection", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    inspection = JarInspectionReport.model_validate_json(
        args.inspection.read_text(encoding="utf-8")
    )
    report = build_overlap_report(inspection)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    _ = args.output.write_text(
        json.dumps(report.model_dump(mode="json"), indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
