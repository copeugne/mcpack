"""Validate the complete Item 5 protocol and pilot receipts."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import cast

from mcpack_evidence.item5 import MeasurementProtocol, PilotRun, analyze_samples, sha256_file

REQUIRED_SPARK_COMMANDS = [
    "spark tps",
    "spark health --memory",
    "spark gc",
    "spark profiler start --interval 4",
    "spark profiler stop --save-to-file",
    "save-all flush",
    "stop",
]


def validate_lifecycle_success(lifecycle: dict[str, object], pilot: PilotRun) -> None:
    """Require every operational success signal and the preserved profile."""
    success_fields = ("ready", "profile_started", "profile_stopped", "save_all_flush", "clean_stop")
    if not all(lifecycle.get(field) is True for field in success_fields):
        message = "accepted pilot lifecycle does not report complete success"
        raise ValueError(message)
    if lifecycle.get("return_code") != 0 or lifecycle.get("console_pipe_failed") is not False:
        message = "accepted pilot lifecycle has a process or console failure"
        raise ValueError(message)
    if lifecycle.get("commands") != REQUIRED_SPARK_COMMANDS:
        message = "accepted pilot lifecycle does not contain the required command sequence"
        raise ValueError(message)
    profiles = lifecycle.get("local_profiles")
    if not isinstance(profiles, list) or len(profiles) != 1:
        message = "accepted pilot lifecycle must contain exactly one new local profile"
        raise ValueError(message)
    profile_artifacts = [
        artifact for artifact in pilot.raw_artifacts if artifact.path.endswith(".sparkprofile")
    ]
    if len(profile_artifacts) != 1 or profile_artifacts[0].size_bytes <= 0:
        message = "accepted pilot must preserve exactly one nonempty Spark profile"
        raise ValueError(message)
    profile = profile_artifacts[0]
    if (
        lifecycle.get("local_profile_sha256") != profile.sha256
        or lifecycle.get("local_profile_size_bytes") != profile.size_bytes
    ):
        message = "preserved Spark profile does not match lifecycle output"
        raise ValueError(message)


def validate_processed_samples(pilot: PilotRun, root: Path) -> None:
    """Recompute accepted sample summaries and require exact semantic equality."""
    if pilot.status != "accepted":
        return
    csv_artifacts = [artifact for artifact in pilot.raw_artifacts if artifact.path.endswith(".csv")]
    json_artifacts = [
        artifact for artifact in pilot.processed_artifacts if artifact.path.endswith(".json")
    ]
    if len(csv_artifacts) != 1 or len(json_artifacts) != 1:
        message = "accepted pilot must bind one raw CSV to one processed JSON summary"
        raise ValueError(message)
    with (root / csv_artifacts[0].path).open(encoding="utf-8", newline="") as stream:
        expected = analyze_samples(csv.DictReader(stream))
    observed = json.loads((root / json_artifacts[0].path).read_bytes())
    if observed != expected:
        message = "processed summary does not match the accepted raw samples"
        raise ValueError(message)


def validate_lifecycle_identities(pilot: PilotRun, root: Path) -> None:
    """Bind accepted environment identities to the raw lifecycle receipt."""
    if pilot.status != "accepted":
        return
    lifecycle_artifacts = [
        artifact for artifact in pilot.raw_artifacts if artifact.path.endswith("/lifecycle.json")
    ]
    if len(lifecycle_artifacts) != 1:
        message = "accepted pilot must reference exactly one lifecycle receipt"
        raise ValueError(message)
    lifecycle = json.loads((root / lifecycle_artifacts[0].path).read_bytes())
    expected_identities = {
        "configuration_sha256": pilot.environment.configuration_sha256,
        "world_snapshot_sha256": pilot.environment.world_snapshot_sha256,
        "spark_overlay_sha256": pilot.environment.spark_overlay_sha256,
        "spark_artifact_sha256": pilot.environment.spark_artifact_sha256,
    }
    for key, expected in expected_identities.items():
        if lifecycle.get(key) != expected:
            message = f"pilot {key} does not match lifecycle receipt"
            raise ValueError(message)
    overlay_path = root / "measurement/item5/spark-overlay.json"
    overlay = json.loads(overlay_path.read_bytes())
    if sha256_file(overlay_path) != pilot.environment.spark_overlay_sha256:
        message = "pilot Spark overlay hash does not match the committed overlay"
        raise ValueError(message)
    if overlay["overlay"]["sha256"] != pilot.environment.spark_artifact_sha256:
        message = "pilot Spark artifact hash does not match the committed overlay"
        raise ValueError(message)
    validate_lifecycle_success(lifecycle, pilot)


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
        validate_lifecycle_identities(pilot, root)
        validate_processed_samples(pilot, root)
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
