#!/usr/bin/env python3
# pyright: standard
"""Boot an Item 4 server, flush it after readiness, and require a clean stop."""

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


def run_lifecycle(
    instance: Path, java_home: Path, log_path: Path, timeout: int
) -> dict[str, object]:
    """Run the deterministic readiness, flush, and stop lifecycle."""
    environment = os.environ.copy()
    environment["PATH"] = f"{java_home / 'bin'}:{environment['PATH']}"
    started = time.monotonic()
    ready = flushed = False
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
        stdout = cast("IO[str]", process.stdout)
        stdin = cast("IO[str]", process.stdin)
        lines: queue.Queue[str | None] = queue.Queue()

        def read_output() -> None:
            for line in iter(stdout.readline, ""):
                lines.put(line)
            lines.put(None)

        reader = threading.Thread(target=read_output, daemon=True)
        reader.start()
        try:
            while True:
                remaining = timeout - (time.monotonic() - started)
                if remaining <= 0:
                    os.killpg(process.pid, signal.SIGKILL)
                    break
                try:
                    line = lines.get(timeout=min(1.0, remaining))
                except queue.Empty:
                    continue
                if line is None:
                    break
                log.write(line)
                log.flush()
                if not ready and "Done (" in line:
                    ready = True
                    stdin.write("save-all flush\n")
                    stdin.flush()
                elif ready and not flushed and "Saved the game" in line:
                    flushed = True
                    stdin.write("stop\n")
                    stdin.flush()
            return_code = process.wait(timeout=30)
        except (TimeoutError, subprocess.TimeoutExpired):
            os.killpg(process.pid, signal.SIGKILL)
            _ = process.wait()
            return_code = -9
        finally:
            stdin.close()
            stdout.close()
            reader.join(timeout=1)
    return {
        "schema_version": "item4-server-lifecycle-v1",
        "instance": str(instance),
        "ready": ready,
        "save_all_flush": flushed,
        "clean_stop": return_code == 0 and ready and flushed,
        "return_code": return_code,
        "duration_seconds": round(time.monotonic() - started, 3),
        "log": str(log_path),
    }


def main() -> int:
    """Parse CLI arguments and emit the lifecycle receipt."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--instance", type=Path, required=True)
    parser.add_argument("--java-home", type=Path, required=True)
    parser.add_argument("--log", type=Path, required=True)
    parser.add_argument("--receipt", type=Path, required=True)
    parser.add_argument("--timeout", type=int, default=600)
    args = parser.parse_args()
    receipt = run_lifecycle(args.instance, args.java_home, args.log, args.timeout)
    args.receipt.parent.mkdir(parents=True, exist_ok=True)
    _ = args.receipt.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2))
    return 0 if receipt["clean_stop"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
