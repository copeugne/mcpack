"""Validate the complete Item 5 protocol and pilot receipts."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import cast

from mcpack_evidence.item5 import MeasurementProtocol, PilotRun, sha256_file


def main() -> int:
    """Validate strict models and every referenced artifact hash."""
    parser = argparse.ArgumentParser()
    _ = parser.add_argument("--protocol", required=True, type=Path)
    _ = parser.add_argument("--pilot", action="append", default=[], type=Path)
    arguments = parser.parse_args()
    protocol_path = cast("Path", arguments.protocol)
    protocol = MeasurementProtocol.model_validate_json(protocol_path.read_bytes())
    pilots = cast("list[Path]", arguments.pilot)
    root = Path.cwd()
    statuses: set[str] = set()
    for path in pilots:
        pilot = PilotRun.model_validate_json(path.read_bytes())
        statuses.add(pilot.status)
        for artifact in (*pilot.raw_artifacts, *pilot.processed_artifacts):
            target = root / artifact.path
            if not target.is_file() or target.stat().st_size != artifact.size_bytes:
                message = f"artifact missing or size mismatch: {artifact.path}"
                raise SystemExit(message)
            if sha256_file(target) != artifact.sha256:
                message = f"artifact hash mismatch: {artifact.path}"
                raise SystemExit(message)
    if pilots and statuses != {"accepted", "rejected"}:
        message = "pilot set must prove accepted and rejected handling"
        raise SystemExit(message)
    print(
        f"validated {len(protocol.metrics)} metrics, "
        f"{len(protocol.player_cases)} cases, {len(pilots)} pilots"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
