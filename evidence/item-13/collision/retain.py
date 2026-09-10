"""Retain the first collision projection and console with explicit address redaction."""

# ruff: noqa: INP001
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import re
from pathlib import Path
from typing import cast

ROOT = Path(__file__).resolve().parents[3]
RAW = ROOT / "evidence/raw/item13/collision-r1"
DESTINATION = Path(__file__).parent

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    _ = mode.add_argument("--spawner-lookup", action="store_true")
    _ = mode.add_argument("--second-house", action="store_true")
    _ = mode.add_argument("--temple-attempt", type=int, choices=(1, 2, 3, 4))
    args = parser.parse_args()
    spawner_lookup = cast("bool", args.spawner_lookup)
    raw_directory = ROOT / "evidence/raw/item13/spawner-lookup-r1" if spawner_lookup else RAW
    prefix = "spawner-r1-" if spawner_lookup else "r1-"
    if cast("bool", args.second_house):
        raw_directory = ROOT / "evidence/raw/item13/house2-collision-r1"
        prefix = "house2-r1-"
    projection = "spawners.json" if spawner_lookup else "collision.json"
    temple_attempt = cast("int | None", args.temple_attempt)
    destination_directory = DESTINATION
    if temple_attempt is not None:
        raw_directory = ROOT / f"evidence/raw/item13/temple-variants-r{temple_attempt}"
        prefix = f"r{temple_attempt}-"
        projection = "temple-variants.json"
        destination_directory = DESTINATION.parent / "temple-variants"
    manifest: dict[str, object] = {}
    for name in (
        projection,
        "capture.json",
        "console.log",
        "dimension-probe.log",
        "build.log",
    ):
        raw = (raw_directory / name).read_bytes()
        published = raw
        if name == "console.log":
            published, count = re.subn(
                rb"(Starting Minecraft server on )[^\r\n]*", rb"\1[REDACTED BIND ENDPOINT]", raw
            )
            if count != 1:
                message = "Expected exactly one server bind endpoint"
                raise ValueError(message)
        destination = destination_directory / (prefix + name.replace(".log", ".txt") + ".gz")
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
    with (destination_directory / (prefix + "retention.json")).open("x") as stream:
        _ = stream.write(json.dumps(manifest, indent=2) + "\n")
