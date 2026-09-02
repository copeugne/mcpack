#!/usr/bin/env python3
"""Run the bounded, console-driven Spark operational pilot."""

from __future__ import annotations

import argparse
import json
import os
import queue
import signal
import subprocess
import threading
import time
from pathlib import Path
from typing import IO, cast


def run(  # noqa: C901, PLR0915 - lifecycle state machine is intentionally linear.
    instance: Path, java_home: Path, log_path: Path, timeout: int
) -> dict[str, object]:
    """Boot, exercise every approved Spark command, flush, and stop."""
    environment = os.environ.copy()
    environment["PATH"] = f"{java_home / 'bin'}:{environment['PATH']}"
    started = time.monotonic()
    sent: list[str] = []
    ready = profile_requested = profile_started = profile_stopped = flushed = False
    command_deadline = 0.0
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("w", encoding="utf-8") as log:
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
        stdin, stdout = cast("IO[str]", process.stdin), cast("IO[str]", process.stdout)
        lines: queue.Queue[str | None] = queue.Queue()

        def read_output() -> None:
            for line in iter(stdout.readline, ""):
                lines.put(line)
            lines.put(None)

        def send(command: str) -> None:
            sent.append(command)
            stdin.write(command + "\n")
            stdin.flush()

        reader = threading.Thread(target=read_output, daemon=True)
        reader.start()
        try:
            while True:
                elapsed = time.monotonic() - started
                if elapsed >= timeout:
                    os.killpg(process.pid, signal.SIGKILL)
                    break
                if profile_started and not profile_stopped and time.monotonic() >= command_deadline:
                    send("spark profiler stop --save-to-file")
                    profile_stopped = True
                try:
                    line = lines.get(timeout=0.5)
                except queue.Empty:
                    continue
                if line is None:
                    break
                log.write(line)
                log.flush()
                if not ready and "Done (" in line:
                    ready = True
                    for command in (
                        "spark tps",
                        "spark health --memory",
                        "spark gc",
                        "spark profiler start --interval 4",
                    ):
                        send(command)
                    profile_requested = True
                elif (
                    profile_requested and not profile_started and "Profiler is now running!" in line
                ):
                    profile_started = True
                    command_deadline = time.monotonic() + 30
                elif profile_stopped and "Profiler stopped & save complete!" in line:
                    send("save-all flush")
                elif profile_stopped and not flushed and "Saved the game" in line:
                    flushed = True
                    send("stop")
            return_code = process.wait(timeout=30)
        except (TimeoutError, subprocess.TimeoutExpired):
            os.killpg(process.pid, signal.SIGKILL)
            return_code = process.wait()
        finally:
            stdin.close()
            stdout.close()
            reader.join(timeout=1)
    profiles = sorted(str(path.relative_to(instance)) for path in instance.rglob("*.sparkprofile"))
    return {
        "schema_version": "item5-spark-lifecycle-v1",
        "ready": ready,
        "profile_started": profile_started,
        "profile_stopped": profile_stopped,
        "save_all_flush": flushed,
        "clean_stop": return_code == 0 and ready and profile_stopped and flushed,
        "return_code": return_code,
        "duration_seconds": round(time.monotonic() - started, 3),
        "commands": sent,
        "local_profiles": profiles,
    }


def main() -> int:
    """Parse arguments and write the lifecycle receipt."""
    parser = argparse.ArgumentParser()
    _ = parser.add_argument("--instance", type=Path, required=True)
    _ = parser.add_argument("--java-home", type=Path, required=True)
    _ = parser.add_argument("--log", type=Path, required=True)
    _ = parser.add_argument("--receipt", type=Path, required=True)
    _ = parser.add_argument("--timeout", type=int, default=900)
    arguments = parser.parse_args()
    receipt = run(arguments.instance, arguments.java_home, arguments.log, arguments.timeout)
    arguments.receipt.parent.mkdir(parents=True, exist_ok=True)
    _ = arguments.receipt.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2))
    return 0 if receipt["clean_stop"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
