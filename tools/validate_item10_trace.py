"""Validate the retained scarecrow trace against its immutable archive identity."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from typing import Never, cast

from mcpack_evidence.item6_json import parse_strict_json

CLASS_SHA = "6d959a626cd2b3011adb2e2571bb74d3a7b49aaa2f0f259a287439787a2a763a"
MIN_EVENTS = 2
COORDINATES = 3
WRITES_PER_ATTEMPT = 5
FIELDS = {
    "installed": {"kind", "input_class_sha256"},
    "begin": {"kind", "attempt", "dimension", "origin"},
    "write": {"kind", "attempt", "position", "state", "flags", "returned"},
    "end": {"kind", "attempt", "returned"},
    "shutdown": {"kind", "installed", "unfinished_attempts"},
}


def fail(reason: str) -> Never:
    """Reject this trace with a concrete diagnostic."""
    raise ValueError(reason)


def check_rows(rows: list[dict[str, object]]) -> dict[str, int]:  # noqa: C901, PLR0912
    """Check the fixed writer's identity, event ordering, pairing and completeness."""
    if len(rows) < MIN_EVENTS or rows[0] != {"kind": "installed", "input_class_sha256": CLASS_SHA}:
        fail("missing or incorrect installation identity")
    if rows[-1] != {"kind": "shutdown", "installed": True, "unfinished_attempts": 0}:
        fail("missing or unhealthy shutdown")
    if type(rows[-1]["unfinished_attempts"]) is not int or rows[-1]["installed"] is not True:
        fail("invalid shutdown field types")
    active: dict[int, int] = {}
    started = writes = complete = refused = 0
    for row in rows[1:-1]:
        kind = row.get("kind")
        if kind not in ("begin", "write", "end") or set(row) != FIELDS[cast("str", kind)]:
            fail("unexpected or malformed event")
        attempt = row.get("attempt")
        if type(attempt) is not int:
            fail("attempt identity must be an integer")
        if kind in ("begin", "write"):
            position = row.get("origin" if kind == "begin" else "position")
            if not isinstance(position, list):
                fail("invalid recorded coordinates")
            coordinates = cast("list[object]", position)
            if len(coordinates) != COORDINATES or any(
                type(value) is not int for value in coordinates
            ):
                fail("invalid recorded coordinates")
        if kind == "begin":
            if attempt != started + 1 or row["dimension"] != "minecraft:overworld":
                fail("missing, repeated or wrong-dimension attempt")
            active[attempt] = 0
            started += 1
            continue
        if attempt not in active or type(row.get("returned")) is not bool:
            fail("unpaired event or invalid return value")
        if kind == "write":
            if (
                type(row["flags"]) is not int
                or not isinstance(row["state"], str)
                or not row["state"]
            ):
                fail("invalid write arguments")
            active[attempt] += 1
            writes += 1
            refused += row["returned"] is False
        else:
            count = active.pop(attempt)
            if count not in (0, WRITES_PER_ATTEMPT) or (
                count == 0 and row["returned"] is not False
            ):
                fail("missing or excess writer calls")
            complete += count == WRITES_PER_ATTEMPT
    if active or complete == 0:
        fail("unfinished attempts or no exercised five-write placement")
    return {
        "attempts": started,
        "writes": writes,
        "five_write_attempts": complete,
        "refused_writes": refused,
    }


def validate_trace(path: Path) -> dict[str, object]:
    """Bind r3 bytes to the published manifest before checking every JSONL record."""
    root = Path(__file__).resolve().parents[1]
    manifest = cast(
        "dict[str, object]",
        parse_strict_json(
            (root / "evidence/item-10/scarecrow-probe-r3/archive-manifest.json").read_bytes()
        ),
    )
    files = cast("list[dict[str, object]]", manifest["files"])
    expected = [
        row["sha256"] for row in files if row["relative_path"] == "scarecrow-probe-r3/trace.jsonl"
    ]
    source = path.read_bytes()
    digest = hashlib.sha256(source).hexdigest()
    if expected != [digest]:
        fail("trace differs from the published r3 archive member")
    rows: list[dict[str, object]] = []
    for line in source.splitlines():
        row = parse_strict_json(line)
        if not isinstance(row, dict):
            fail("trace record is not an object")
        rows.append(cast("dict[str, object]", row))
    return {
        "status": "PASS",
        "scope": "r3 capture health only",
        "sha256": digest,
        **check_rows(rows),
    }


if __name__ == "__main__":
    if len(sys.argv[1:]) != 1:
        message = "usage: python -m tools.validate_item10_trace TRACE.jsonl"
        raise SystemExit(message)
    print(json.dumps(validate_trace(Path(sys.argv[1])), indent=2))
