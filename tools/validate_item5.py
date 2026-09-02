"""Validate the complete Item 5 protocol and pilot receipts."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import cast

from mcpack_evidence.item5 import MeasurementProtocol, PilotRun, sha256_file


def validate_pilots(protocol_path: Path, pilots: list[Path], root: Path) -> MeasurementProtocol:
    """Validate protocol coverage, receipt binding, statuses, and artifact identities."""
    protocol = MeasurementProtocol.model_validate_json(protocol_path.read_bytes())
    protocol_sha256 = sha256_file(protocol_path)
    statuses: set[str] = set()
    for path in pilots:
        pilot = PilotRun.model_validate_json(path.read_bytes())
        if pilot.environment.protocol_sha256 != protocol_sha256:
            message = f"pilot protocol hash mismatch: {path}"
            raise ValueError(message)
        statuses.add(pilot.status)
        for artifact in (*pilot.raw_artifacts, *pilot.processed_artifacts):
            target = root / artifact.path
            if not target.is_file() or target.stat().st_size != artifact.size_bytes:
                message = f"artifact missing or size mismatch: {artifact.path}"
                raise ValueError(message)
            if sha256_file(target) != artifact.sha256:
                message = f"artifact hash mismatch: {artifact.path}"
                raise ValueError(message)
    if pilots and statuses != {"accepted", "rejected"}:
        message = "pilot set must prove accepted and rejected handling"
        raise ValueError(message)
    return protocol


def main() -> int:
    """Validate strict models and every referenced artifact hash."""
    parser = argparse.ArgumentParser()
    _ = parser.add_argument("--protocol", required=True, type=Path)
    _ = parser.add_argument("--pilot", action="append", default=[], type=Path)
    arguments = parser.parse_args()
    protocol_path = cast("Path", arguments.protocol)
    pilots = cast("list[Path]", arguments.pilot)
    try:
        protocol = validate_pilots(protocol_path, pilots, Path.cwd())
    except ValueError as error:
        raise SystemExit(str(error)) from error
    print(
        f"validated {len(protocol.metrics)} metrics, "
        f"{len(protocol.player_cases)} cases, {len(pilots)} pilots"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
