"""Validate the complete Item 5 protocol and pilot receipts."""

from __future__ import annotations

import argparse
import csv
import gzip
import json
import math
import re
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


def confined_artifact_path(root: Path, artifact_path: str) -> Path:
    """Resolve a receipt path while refusing absolute and repository escapes."""
    repository = root.resolve()
    candidate = Path(artifact_path)
    if candidate.is_absolute():
        message = f"artifact path escapes repository: {artifact_path}"
        raise ValueError(message)
    resolved = (repository / candidate).resolve()
    try:
        resolved.relative_to(repository)
    except ValueError as error:
        message = f"artifact path escapes repository: {artifact_path}"
        raise ValueError(message) from error
    return resolved


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
    with confined_artifact_path(root, csv_artifacts[0].path).open(
        encoding="utf-8", newline=""
    ) as stream:
        expected = analyze_samples(csv.DictReader(stream))
    observed = json.loads(confined_artifact_path(root, json_artifacts[0].path).read_bytes())
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
    lifecycle = json.loads(confined_artifact_path(root, lifecycle_artifacts[0].path).read_bytes())
    expected_identities = {
        "configuration_sha256": pilot.environment.configuration_sha256,
        "world_snapshot_sha256": pilot.environment.world_snapshot_sha256,
        "spark_overlay_sha256": pilot.environment.spark_overlay_sha256,
        "spark_artifact_sha256": pilot.environment.spark_artifact_sha256,
        "runtime_mods_sha256": pilot.environment.runtime_mods_sha256,
        "input_world_sha256": pilot.environment.input_world_sha256,
    }
    for key, expected in expected_identities.items():
        if lifecycle.get(key) != expected:
            message = f"pilot {key} does not match lifecycle receipt"
            raise ValueError(message)
    lifecycle_java = lifecycle.get("java_version")
    if not isinstance(lifecycle_java, str) or 'version "21.0.12.1"' not in lifecycle_java:
        message = "accepted pilot lifecycle does not identify pinned Temurin 21"
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


def validate_runtime_provenance(  # noqa: C901 - provenance checks are intentionally linear.
    pilot: PilotRun, root: Path
) -> None:
    """Bind receipt versions, seed, and player case to preserved raw evidence."""
    if pilot.status != "accepted":
        return
    logs = [artifact for artifact in pilot.raw_artifacts if artifact.path.endswith(".log.gz")]
    csvs = [artifact for artifact in pilot.raw_artifacts if artifact.path.endswith(".csv")]
    if len(logs) != 1 or len(csvs) != 1:
        message = "accepted pilot must contain one runtime log and one sample CSV"
        raise ValueError(message)
    with gzip.open(confined_artifact_path(root, logs[0].path), "rt", encoding="utf-8") as stream:
        log = stream.read()
    if "java version 21.0.12.1 by Eclipse Adoptium" not in log:
        message = "accepted pilot did not run on pinned Eclipse Adoptium Java 21"
        raise ValueError(message)
    if pilot.environment.java_version not in {
        "Temurin-21.0.12.1+1",
        "Temurin-21.0.12.1+1-LTS",
    }:
        message = "pilot java_version does not match pinned Temurin build"
        raise ValueError(message)
    probe_markers = {
        "spark tps": "TPS from last 5s",
        "spark health --memory": "> Memory usage:",
        "spark gc": "> Garbage Collector statistics",
    }
    for command, marker in probe_markers.items():
        if marker not in log:
            message = f"pilot has no successful response for required probe: {command}"
            raise ValueError(message)
    minecraft = re.escape(pilot.environment.minecraft_version)
    neoforge = re.escape(pilot.environment.neoforge_version)
    version_patterns = {
        "minecraft_version": rf"--fml\.mcVersion, {minecraft}(?:,|\])",
        "neoforge_version": rf"--fml\.neoForgeVersion, {neoforge}(?:,|\])",
    }
    for field, pattern in version_patterns.items():
        if re.search(pattern, log) is None:
            message = f"pilot {field} does not match preserved runtime output"
            raise ValueError(message)
    seed_suite = json.loads((root / "test-environment/seed-suite.json").read_bytes())
    seed_roles = {int(row["seed"]): row["role"] for row in seed_suite["seeds"]}
    if pilot.seed not in seed_roles:
        message = "pilot seed is not declared in the committed seed suite"
        raise ValueError(message)
    with confined_artifact_path(root, csvs[0].path).open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    if not rows or any(
        row.get("seed_case") != seed_roles[pilot.seed]
        or row.get("player_case") != pilot.player_case
        for row in rows
    ):
        message = "pilot seed or player case does not match raw samples"
        raise ValueError(message)
    tps = re.search(r"> TPS from last 5s[^\n]*:\n\s*([0-9]+(?:\.[0-9]+)?)", log)
    mspt = re.search(r"> Tick durations [^\n]*:\n\s*([0-9]+(?:\.[0-9]+)?)/", log)
    memory = re.search(r"> Memory usage:\n\s*([0-9]+(?:\.[0-9]+)?) GB", log)
    runtime_values = {
        ("tps", None): float(tps.group(1)) if tps else None,
        ("idle_mspt", None): float(mspt.group(1)) if mspt else None,
        ("memory", "heap_used_bytes"): float(memory.group(1)) * 1_000_000_000 if memory else None,
    }
    for row in rows:
        key = (row["metric_id"], row.get("component") or None)
        observed = runtime_values.get(key)
        if observed is None or not math.isclose(float(row["value"]), observed):
            message = f"sample {key[0]} value does not match preserved runtime output"
            raise ValueError(message)


def validate_rejected_lifecycle_document(lifecycle: object) -> dict[str, object]:
    """Return a rejected lifecycle only after validating its core v1 shape."""
    if not isinstance(lifecycle, dict):
        message = "rejected pilot lifecycle is incomplete or malformed"
        raise ValueError(message)  # noqa: TRY004 - evidence validation has one error contract.
    required_types: dict[str, type[object]] = {
        "schema_version": str,
        "ready": bool,
        "profile_started": bool,
        "profile_stopped": bool,
        "save_all_flush": bool,
        "clean_stop": bool,
        "duration_seconds": (int, float),
        "commands": list,
        "local_profiles": list,
    }
    if any(
        key not in lifecycle or not isinstance(lifecycle[key], kind)
        for key, kind in required_types.items()
    ):
        message = "rejected pilot lifecycle is incomplete or malformed"
        raise ValueError(message)
    if lifecycle["schema_version"] != "item5-spark-lifecycle-v1":
        message = "rejected pilot lifecycle has an unsupported schema"
        raise ValueError(message)
    return lifecycle


def validate_rejected_lifecycle(pilot: PilotRun, root: Path) -> None:
    """Require rejected receipts to bind a machine-observable failure."""
    if pilot.status != "rejected":
        return
    lifecycle_artifacts = [
        artifact for artifact in pilot.raw_artifacts if artifact.path.endswith("/lifecycle.json")
    ]
    if len(lifecycle_artifacts) != 1:
        message = "rejected pilot must reference exactly one lifecycle receipt"
        raise ValueError(message)
    lifecycle = validate_rejected_lifecycle_document(
        json.loads(confined_artifact_path(root, lifecycle_artifacts[0].path).read_bytes())
    )
    success_fields = ("ready", "profile_started", "profile_stopped", "save_all_flush", "clean_stop")
    console_pipe_failed = lifecycle.get("console_pipe_failed")
    if console_pipe_failed is not None and not isinstance(console_pipe_failed, bool):
        message = "rejected pilot lifecycle has an invalid console-pipe status"
        raise ValueError(message)
    return_code = lifecycle.get("return_code")
    if return_code is not None and (
        isinstance(return_code, bool) or not isinstance(return_code, int)
    ):
        message = "rejected pilot lifecycle has an invalid return code"
        raise ValueError(message)
    lifecycle_failed = (
        any(lifecycle[field] is False for field in success_fields)
        or (isinstance(return_code, int) and return_code != 0)
        or console_pipe_failed is True
    )
    failure_markers = (b"Server already shutting down", b"Spark overlay preflight failed")
    log_failed = False
    for artifact in pilot.raw_artifacts:
        if artifact.path.endswith(".log.gz"):
            with gzip.open(confined_artifact_path(root, artifact.path), "rb") as stream:
                content = stream.read()
            log_failed = any(marker in content for marker in failure_markers)
            if log_failed:
                break
    if not lifecycle_failed and not log_failed:
        message = "rejected pilot has no machine-observable lifecycle failure"
        raise ValueError(message)


def validate_pilots(  # noqa: C901 - cross-artifact gate is intentionally linear.
    protocol_path: Path, pilots: list[Path], root: Path
) -> MeasurementProtocol:
    """Validate protocol coverage, receipt binding, statuses, and artifact identities."""
    protocol = MeasurementProtocol.model_validate_json(protocol_path.read_bytes())
    protocol_sha256 = sha256_file(protocol_path)
    fixtures = {
        "combat": ("measurement/item5/combat-fixture-v1.json", protocol.combat_fixture_sha256),
        "worldgen": (
            "measurement/item5/worldgen-fixture-v1.json",
            protocol.worldgen_fixture_sha256,
        ),
        "pathfinding": (
            "measurement/item5/pathfinding-fixture-v1.json",
            protocol.pathfinding_fixture_sha256,
        ),
    }
    for name, (relative_path, expected_hash) in fixtures.items():
        if sha256_file(root / relative_path) != expected_hash:
            message = f"protocol {name} fixture hash mismatch"
            raise ValueError(message)
    retained_manifest_sha256 = sha256_file(
        root / "evidence/item-3/runtime/retained-server-candidates.txt"
    )
    host_evidence_sha256 = sha256_file(root / "evidence/item-2/host-discovery.json")
    platform = json.loads((root / "infrastructure/manifests/platform-1.21.1.json").read_bytes())
    java_archive_sha256 = next(
        artifact["sha256"] for artifact in platform["artifacts"] if artifact["id"] == "temurin-jdk"
    )
    statuses: set[str] = set()
    for path in pilots:
        pilot = PilotRun.model_validate_json(path.read_bytes())
        if pilot.environment.protocol_sha256 != protocol_sha256:
            message = f"pilot protocol hash mismatch: {path}"
            raise ValueError(message)
        if pilot.environment.retained_manifest_sha256 != retained_manifest_sha256:
            message = f"pilot retained manifest hash mismatch: {path}"
            raise ValueError(message)
        if pilot.environment.host_evidence_sha256 != host_evidence_sha256:
            message = f"pilot host evidence hash mismatch: {path}"
            raise ValueError(message)
        if pilot.environment.java_archive_sha256 != java_archive_sha256:
            message = f"pilot Java archive hash mismatch: {path}"
            raise ValueError(message)
        statuses.add(pilot.status)
        for artifact in (*pilot.raw_artifacts, *pilot.processed_artifacts):
            target = confined_artifact_path(root, artifact.path)
            if not target.is_file() or target.stat().st_size != artifact.size_bytes:
                message = f"artifact missing or size mismatch: {artifact.path}"
                raise ValueError(message)
            if sha256_file(target) != artifact.sha256:
                message = f"artifact hash mismatch: {artifact.path}"
                raise ValueError(message)
        validate_lifecycle_identities(pilot, root)
        validate_runtime_provenance(pilot, root)
        validate_rejected_lifecycle(pilot, root)
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
