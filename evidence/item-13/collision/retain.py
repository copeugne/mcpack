"""Retain the first collision projection and console with explicit address redaction."""

# ruff: noqa: INP001
from __future__ import annotations

import gzip
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
RAW = ROOT / "evidence/raw/item13/collision-r1"
DESTINATION = Path(__file__).parent

if __name__ == "__main__":
    manifest: dict[str, object] = {}
    for name in (
        "collision.json",
        "capture.json",
        "console.log",
        "dimension-probe.log",
        "build.log",
    ):
        raw = (RAW / name).read_bytes()
        published = raw
        if name == "console.log":
            published, count = re.subn(
                rb"(Starting Minecraft server on )[^\r\n]*", rb"\1[REDACTED BIND ENDPOINT]", raw
            )
            if count != 1:
                message = "Expected exactly one server bind endpoint"
                raise ValueError(message)
        destination = DESTINATION / ("r1-" + name.replace(".log", ".txt") + ".gz")
        compressed = gzip.compress(published, mtime=0)
        with destination.open("xb") as stream:
            _ = stream.write(compressed)
        manifest[name] = {
            "original_sha256": hashlib.sha256(raw).hexdigest(),
            "original_size_bytes": len(raw),
            "retained_file": destination.name,
            "retained_sha256": hashlib.sha256(compressed).hexdigest(),
            "retained_size_bytes": len(compressed),
            "redaction": "bind endpoint only" if name == "console.log" else None,
        }
    with (DESTINATION / "r1-retention.json").open("x") as stream:
        _ = stream.write(json.dumps(manifest, indent=2) + "\n")
