#!/usr/bin/env python3
"""Run the bounded, console-driven Spark operational pilot."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import queue
import signal
import subprocess
import threading
import time
from pathlib import Path
from typing import IO, cast

from mcpack_evidence.item5 import sha256_file

REQUIRED_SPARK_COMMANDS = (
    "spark tps",
    "spark health --memory",
    "spark gc",
    "spark profiler start --interval 4",
    "spark profiler stop --save-to-file",
    "save-all flush",
    "stop",
)


class SparkPreflightError(ValueError):
    """The committed overlay or runtime profiler artifact is invalid."""


class ServerLaunchError(OSError):
    """The server process could not be created."""


class PilotRuntimeError(OSError):
    """The launched server encountered a local harness I/O failure."""


def validate_java_runtime(java_home: Path) -> str:
    """Require the pinned Java executable rather than falling through PATH."""
    executable = (java_home / "bin/java").resolve()
    if not executable.is_file() or not os.access(executable, os.X_OK):
        message = f"requested Java runtime is unavailable: {executable}"
        raise SparkPreflightError(message)
    completed = subprocess.run(  # noqa: S603 - executable is the validated pinned path.
        [executable, "-version"], capture_output=True, text=True, check=False
    )
    output = completed.stderr + completed.stdout
    if completed.returncode != 0 or 'version "21.0.12' not in output:
        message = f"requested Java runtime is not pinned Temurin 21.0.12: {executable}"
        raise SparkPreflightError(message)
    return output.splitlines()[0]


def confirms_profile_save(line: str, *, stop_requested: bool) -> bool:
    """Accept Spark's completion only after this harness requested a stop."""
    return stop_requested and "Profiler stopped & save complete!" in line


def confirms_requested_flush(line: str, *, flush_requested: bool) -> bool:
    """Ignore unrelated or automatic saves until this harness requests its flush."""
    return flush_requested and "Saved the game" in line


def send_console_command(stdin: IO[str], command: str) -> bool:
    """Return false instead of losing the receipt when the console pipe closes."""
    try:
        stdin.write(command + "\n")
        stdin.flush()
    except (BrokenPipeError, OSError):
        return False
    return True


def validate_runtime_mods(
    instance: Path, overlay_path: Path, retained_path: Path, acquisition_path: Path
) -> tuple[str, str, str]:
    """Verify every gameplay and instrumentation JAR and return their identities."""
    try:
        overlay = json.loads(overlay_path.read_bytes())
        artifact = overlay["overlay"]
        retained = [line for line in retained_path.read_text(encoding="utf-8").splitlines() if line]
        acquisition = json.loads(acquisition_path.read_bytes())
        acquired = {
            row["candidate_filename"]: row["identity"]["computed_sha256"]
            for row in acquisition["artifacts"]
        }
        expected = {name: acquired[name] for name in retained}
        expected[artifact["filename"]] = artifact["sha256"]
    except (KeyError, OSError, TypeError, ValueError) as error:
        message = f"cannot construct runtime mod identity: {error}"
        raise SparkPreflightError(message) from error
    observed_names = {path.name for path in (instance / "mods").glob("*.jar")}
    if observed_names != set(expected):
        message = "runtime mod filenames do not match retained manifest plus Spark overlay"
        raise SparkPreflightError(message)
    observed = {name: sha256_file(instance / "mods" / name) for name in sorted(expected)}
    if observed != expected:
        message = "runtime mod hashes do not match acquisition manifest plus Spark overlay"
        raise SparkPreflightError(message)
    identity = hashlib.sha256(
        json.dumps(observed, separators=(",", ":"), sort_keys=True).encode()
    ).hexdigest()
    return sha256_file(overlay_path), artifact["sha256"], identity


def validate_spark_overlay(instance: Path, overlay_path: Path) -> tuple[str, str]:
    """Compatibility helper that verifies the configured profiler artifact."""
    overlay = json.loads(overlay_path.read_bytes())
    artifact = overlay["overlay"]
    spark_path = instance / "mods" / artifact["filename"]
    actual_sha256 = sha256_file(spark_path)
    if actual_sha256 != artifact["sha256"]:
        message = f"Spark artifact hash mismatch: {spark_path}"
        raise SparkPreflightError(message)
    return sha256_file(overlay_path), actual_sha256


def preflight_failure_receipt(error: Exception) -> dict[str, object]:
    """Return machine-readable rejected evidence for an overlay preflight failure."""
    return {
        "schema_version": "item5-spark-lifecycle-v1",
        "ready": False,
        "profile_started": False,
        "profile_stopped": False,
        "save_all_flush": False,
        "clean_stop": False,
        "return_code": None,
        "duration_seconds": 0.0,
        "commands": [],
        "local_profiles": [],
        "configuration_sha256": None,
        "world_snapshot_sha256": None,
        "spark_overlay_sha256": None,
        "spark_artifact_sha256": None,
        "runtime_mods_sha256": None,
        "local_profile_sha256": None,
        "local_profile_size_bytes": None,
        "console_pipe_failed": False,
        "rejection_reason": f"Spark overlay preflight failed: {error}",
    }


def launch_failure_receipt(error: OSError) -> dict[str, object]:
    """Return machine-readable rejected evidence when the JVM cannot launch."""
    receipt = preflight_failure_receipt(error)
    receipt["rejection_reason"] = f"Server launch failed: {error}"
    return receipt


def runtime_failure_receipt(error: OSError) -> dict[str, object]:
    """Return machine-readable evidence for a cleaned-up post-launch failure."""
    receipt = preflight_failure_receipt(error)
    receipt["rejection_reason"] = f"Pilot runtime I/O failed after server cleanup: {error}"
    return receipt


def hash_tree(root: Path, relative_paths: tuple[Path, ...]) -> str:
    """Hash paths, sizes, and contents for a deterministic tree identity."""
    digest = hashlib.sha256()
    files: list[Path] = []
    for relative_path in relative_paths:
        target = root / relative_path
        if target.is_file():
            files.append(target)
        elif target.is_dir():
            files.extend(path for path in target.rglob("*") if path.is_file())
    for path in sorted(files, key=lambda candidate: candidate.relative_to(root).as_posix()):
        relative = path.relative_to(root).as_posix()
        if relative == "world/session.lock":
            continue
        size = path.stat().st_size
        digest.update(f"{relative}\0{size}\0".encode())
        with path.open("rb") as stream:
            for block in iter(lambda: stream.read(1024 * 1024), b""):
                digest.update(block)
    return digest.hexdigest()


def find_new_profiles(instance: Path, prior_profiles: dict[Path, tuple[int, int]]) -> list[Path]:
    """Return nonempty profiles created or replaced after lifecycle startup."""
    return sorted(
        path
        for path in instance.rglob("*.sparkprofile")
        if path.stat().st_size > 0
        and prior_profiles.get(path.resolve()) != (path.stat().st_size, path.stat().st_mtime_ns)
    )


def clean_stop_succeeded(  # noqa: PLR0913 - explicit lifecycle signals prevent ambiguity.
    *,
    return_code: int,
    ready: bool,
    profile_saved: bool,
    flushed: bool,
    profile_count: int,
    console_pipe_failed: bool,
    probes_confirmed: bool = True,
) -> bool:
    """Require one and only one preserved profile for lifecycle success."""
    return (
        return_code == 0
        and ready
        and profile_saved
        and flushed
        and profile_count == 1
        and not console_pipe_failed
        and probes_confirmed
    )


def run(  # noqa: C901, PLR0912, PLR0913, PLR0915, PLR0917 - explicit lifecycle inputs.
    instance: Path,
    java_home: Path,
    spark_overlay: Path,
    retained_manifest: Path,
    acquisition_manifest: Path,
    log_path: Path,
    timeout: int,
) -> dict[str, object]:
    """Boot, exercise every approved Spark command, flush, and stop."""
    environment = os.environ.copy()
    java_version = validate_java_runtime(java_home)
    environment["PATH"] = f"{java_home / 'bin'}:{environment['PATH']}"
    started = time.monotonic()
    sent: list[str] = []
    console_pipe_failed = False
    spark_overlay_sha256, spark_artifact_sha256, runtime_mods_sha256 = validate_runtime_mods(
        instance, spark_overlay, retained_manifest, acquisition_manifest
    )
    prior_profiles = {
        path.resolve(): (path.stat().st_size, path.stat().st_mtime_ns)
        for path in instance.rglob("*.sparkprofile")
    }
    configuration_sha256 = hash_tree(
        instance,
        (
            Path("config"),
            Path("defaultconfigs"),
            Path("server.properties"),
            Path("user_jvm_args.txt"),
        ),
    )
    input_world_sha256 = hash_tree(instance, (Path("world"),))
    ready = profile_requested = profile_started = profile_stop_requested = False
    profile_saved = flush_requested = flushed = False
    tps_confirmed = memory_confirmed = gc_confirmed = False
    command_deadline = 0.0
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("w", encoding="utf-8") as log:
        try:
            process = subprocess.Popen(
                ["./run.sh", "nogui"],
                cwd=instance,
                env=environment,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
                start_new_session=True,
            )
        except OSError as error:
            raise ServerLaunchError(str(error)) from error
        stdin, stdout = cast("IO[str]", process.stdin), cast("IO[str]", process.stdout)
        lines: queue.Queue[str | None] = queue.Queue()

        def read_output() -> None:
            for line in iter(stdout.readline, ""):
                lines.put(line)
            lines.put(None)

        def send(command: str) -> None:
            nonlocal console_pipe_failed
            if console_pipe_failed:
                return
            if not send_console_command(stdin, command):
                console_pipe_failed = True
                return
            sent.append(command)

        reader = threading.Thread(target=read_output, daemon=True)
        reader.start()
        try:
            while True:
                elapsed = time.monotonic() - started
                if elapsed >= timeout:
                    os.killpg(process.pid, signal.SIGKILL)
                    break
                if (
                    profile_started
                    and not profile_stop_requested
                    and time.monotonic() >= command_deadline
                ):
                    send(REQUIRED_SPARK_COMMANDS[4])
                    profile_stop_requested = True
                try:
                    line = lines.get(timeout=0.5)
                except queue.Empty:
                    continue
                if line is None:
                    break
                log.write(line)
                log.flush()
                tps_confirmed = tps_confirmed or "TPS from last 5s" in line
                memory_confirmed = memory_confirmed or "> Memory usage:" in line
                gc_confirmed = gc_confirmed or "> Garbage Collector statistics" in line
                if not ready and "Done (" in line:
                    ready = True
                    for command in REQUIRED_SPARK_COMMANDS[:4]:
                        send(command)
                    profile_requested = True
                elif (
                    profile_requested and not profile_started and "Profiler is now running!" in line
                ):
                    profile_started = True
                    command_deadline = time.monotonic() + 30
                elif confirms_profile_save(line, stop_requested=profile_stop_requested):
                    profile_saved = True
                    send(REQUIRED_SPARK_COMMANDS[5])
                    flush_requested = True
                elif not flushed and confirms_requested_flush(
                    line, flush_requested=flush_requested
                ):
                    flushed = True
                    send(REQUIRED_SPARK_COMMANDS[6])
            return_code = process.wait(timeout=30)
        except (TimeoutError, subprocess.TimeoutExpired):
            os.killpg(process.pid, signal.SIGKILL)
            return_code = process.wait()
        except OSError as error:
            if process.poll() is None:
                os.killpg(process.pid, signal.SIGKILL)
                _ = process.wait()
            raise PilotRuntimeError(str(error)) from error
        except BaseException:
            if process.poll() is None:
                os.killpg(process.pid, signal.SIGKILL)
                _ = process.wait()
            raise
        finally:
            try:
                stdin.close()
            except (BrokenPipeError, OSError):
                console_pipe_failed = True
            stdout.close()
            reader.join(timeout=1)
    new_profiles = find_new_profiles(instance, prior_profiles)
    profiles = [str(path.relative_to(instance)) for path in new_profiles]
    local_profile_sha256 = sha256_file(new_profiles[0]) if len(new_profiles) == 1 else None
    local_profile_size_bytes = new_profiles[0].stat().st_size if len(new_profiles) == 1 else None
    world_snapshot_sha256 = hash_tree(instance, (Path("world"),)) if ready else None
    return {
        "schema_version": "item5-spark-lifecycle-v1",
        "ready": ready,
        "profile_started": profile_started,
        "profile_stopped": profile_saved,
        "save_all_flush": flushed,
        "clean_stop": clean_stop_succeeded(
            return_code=return_code,
            ready=ready,
            profile_saved=profile_saved,
            flushed=flushed,
            profile_count=len(profiles),
            console_pipe_failed=console_pipe_failed,
            probes_confirmed=tps_confirmed and memory_confirmed and gc_confirmed,
        ),
        "return_code": return_code,
        "duration_seconds": round(time.monotonic() - started, 3),
        "commands": sent,
        "local_profiles": profiles,
        "configuration_sha256": configuration_sha256,
        "input_world_sha256": input_world_sha256,
        "world_snapshot_sha256": world_snapshot_sha256,
        "spark_overlay_sha256": spark_overlay_sha256,
        "spark_artifact_sha256": spark_artifact_sha256,
        "runtime_mods_sha256": runtime_mods_sha256,
        "local_profile_sha256": local_profile_sha256,
        "local_profile_size_bytes": local_profile_size_bytes,
        "console_pipe_failed": console_pipe_failed,
        "probe_confirmations": {
            "spark_tps": tps_confirmed,
            "spark_health_memory": memory_confirmed,
            "spark_gc": gc_confirmed,
        },
        "java_version": java_version,
    }


def main() -> int:
    """Parse arguments and write the lifecycle receipt."""
    parser = argparse.ArgumentParser()
    _ = parser.add_argument("--instance", type=Path, required=True)
    _ = parser.add_argument("--java-home", type=Path, required=True)
    _ = parser.add_argument("--spark-overlay", type=Path, required=True)
    _ = parser.add_argument(
        "--retained-manifest",
        type=Path,
        default=Path("evidence/item-3/runtime/retained-server-candidates.txt"),
    )
    _ = parser.add_argument(
        "--acquisition-manifest",
        type=Path,
        default=Path("evidence/item-3/artifact-acquisition-manifest.json"),
    )
    _ = parser.add_argument("--log", type=Path, required=True)
    _ = parser.add_argument("--receipt", type=Path, required=True)
    _ = parser.add_argument("--timeout", type=int, default=900)
    arguments = parser.parse_args()
    try:
        receipt = run(
            arguments.instance,
            arguments.java_home,
            arguments.spark_overlay,
            arguments.retained_manifest,
            arguments.acquisition_manifest,
            arguments.log,
            arguments.timeout,
        )
    except SparkPreflightError as error:
        receipt = preflight_failure_receipt(error)
    except ServerLaunchError as error:
        receipt = launch_failure_receipt(error)
    except PilotRuntimeError as error:
        receipt = runtime_failure_receipt(error)
    arguments.receipt.parent.mkdir(parents=True, exist_ok=True)
    _ = arguments.receipt.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2))
    return 0 if receipt["clean_stop"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
