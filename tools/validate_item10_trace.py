"""Validate retained placement traces against their immutable archive identities."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from typing import Never, cast

from mcpack_evidence.item6_json import parse_strict_json

CLASS_SHA = "6d959a626cd2b3011adb2e2571bb74d3a7b49aaa2f0f259a287439787a2a763a"
SHA256_HEX_LENGTH = 64
HELPER_FLAGS = 3
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


MONSTER_BOX = "org/violetmoon/quark/content/world/gen/MonsterBoxGenerator"
BOP_CLASSES = {
    "biomesoplenty/worldgen/feature/misc/AnomalyFeature",
    "biomesoplenty/worldgen/feature/misc/MonolithFeature",
}
BOP_INSTALLED = BOP_CLASSES | {
    "net/minecraft/world/level/levelgen/feature/Feature",
    "org/betterx/betterend/world/features/NBTFeature",
    "org/betterx/betterend/world/features/BuildingListFeature$StructureInfo",
    "org/betterx/betterend/world/features/CrashedShipFeature",
    "net/minecraft/world/level/levelgen/structure/templatesystem/StructureTemplate",
}


def check_feature_rows(  # noqa: C901, PLR0912, PLR0915
    rows: list[dict[str, object]], *, monster_box: bool = False
) -> dict[str, object]:
    """Check either retained feature population, keeping failed and void outcomes distinct."""
    classes = {MONSTER_BOX} if monster_box else BOP_CLASSES
    required = BOP_INSTALLED | ({MONSTER_BOX} if monster_box else set[str]())
    dimension = "minecraft:overworld" if monster_box else "minecraft:the_end"
    ending = "generator_end" if monster_box else "end"
    attempt_writes: dict[int, int] = {}
    installations: dict[str, str] = {}
    active: dict[int, str | None] = {}
    started: set[int] = set()
    writes = refused = 0
    by_feature: dict[str, int] = {}
    successful_paths: dict[tuple[str, int], int] = {}
    if (
        not rows
        or rows[-1] != {"kind": "shutdown", "installed": True, "unfinished_attempts": 0}
        or type(rows[-1].get("unfinished_attempts")) is not int
    ):
        fail("missing or unhealthy BOP shutdown")
    for row in rows[:-1]:
        kind = row.get("kind")
        if kind in {"installed", "feature_installed"}:
            expected = {"kind", "input_class_sha256"}
            name = "scarecrow"
            if kind == "feature_installed":
                expected.add("class")
                name = cast("str", row.get("class"))
                if name not in required:
                    fail("unexpected BOP installation class")
            digest = row.get("input_class_sha256")
            if set(row) != expected or name in installations or not isinstance(digest, str):
                fail("duplicate or malformed BOP installation")
            if len(digest) != SHA256_HEX_LENGTH or any(c not in "0123456789abcdef" for c in digest):
                fail("invalid BOP class digest")
            if name == "scarecrow" and digest != CLASS_SHA:
                fail("incorrect scarecrow installation")
            installations[name] = digest
            continue
        if kind not in {"begin", "feature", "write", ending}:
            fail("unexpected BOP event or unhandled failure")
        expected = (
            {"kind", "attempt", "class"}
            if kind == "feature"
            else {"kind", "attempt"}
            if kind == "generator_end"
            else FIELDS[cast("str", kind)]
        )
        if set(row) != expected or type(row.get("attempt")) is not int:
            fail("malformed BOP event")
        attempt = cast("int", row["attempt"])
        if kind in {"begin", "write"}:
            position = row.get("origin" if kind == "begin" else "position")
            if (
                not isinstance(position, list)
                or len(cast("list[object]", position)) != COORDINATES
                or any(type(v) is not int for v in cast("list[object]", position))
            ):
                fail("invalid BOP coordinates")
        if kind == "begin":
            if attempt <= 0 or attempt in started or row["dimension"] != dimension:
                fail("duplicate or wrong-dimension BOP attempt")
            started.add(attempt)
            active[attempt] = None
            continue
        if attempt not in active:
            fail("unpaired BOP event")
        if kind == "feature":
            name = row["class"]
            if not isinstance(name, str) or name.replace(".", "/") not in classes:
                fail("unexpected BOP feature")
            if active[attempt] is not None or name.replace(".", "/") not in installations:
                fail("duplicate feature or feature before installation")
            active[attempt] = name
            continue
        name = active[attempt]
        if name is None or (kind != "generator_end" and type(row.get("returned")) is not bool):
            fail("missing feature or invalid BOP result")
        if kind == "write":
            flags = row["flags"]
            if type(flags) is not int or flags not in ((0,) if monster_box else (2, 3)):
                fail("invalid BOP flags")
            if name.endswith("MonolithFeature") and flags != HELPER_FLAGS:
                fail("unexpected monolith flags")
            if not isinstance(row["state"], str) or not row["state"]:
                fail("invalid BOP block state")
            attempt_writes[attempt] = attempt_writes.get(attempt, 0) + 1
            if monster_box and attempt_writes[attempt] > 1:
                fail("Monster Box exceeds frozen single-write bound")
            writes += 1
            refused += row["returned"] is False
            by_feature[name] = by_feature.get(name, 0) + 1
            if row["returned"]:
                path = (name, flags)
                successful_paths[path] = successful_paths.get(path, 0) + 1
        else:
            del active[attempt]
    if active or started != set(range(1, len(started) + 1)):
        fail("unfinished or missing BOP attempts")
    if set(installations) != required | {"scarecrow"}:
        fail("incomplete BOP installations")
    if set(by_feature) != {n.replace("/", ".") for n in classes}:
        fail("no exercised writes for one BOP feature")
    required_paths = {
        (name.replace("/", "."), flags)
        for name in BOP_CLASSES
        for flags in ((2, 3) if name.endswith("AnomalyFeature") else (3,))
    }
    if monster_box:
        required_paths = {(MONSTER_BOX.replace("/", "."), 0)}
    if set(successful_paths) != required_paths:
        fail(
            "Monster Box requires a successful write"
            if monster_box
            else "BOP requires successful writes on all three provider/flag paths"
        )
    return {
        "successful_write_paths": [
            {"feature": name, "flags": flags, "writes": count}
            for (name, flags), count in sorted(successful_paths.items())
        ],
        "attempts": len(started),
        "writes": writes,
        "refused_writes": refused,
        "writes_by_feature": by_feature,
        "installations": installations,
    }


def validate_feature_trace(raw_root: Path, *, monster_box: bool = False) -> dict[str, object]:
    """Bind a declared feature trace and incoming classes to its immutable archive."""
    diagnostic = "monster-box-pilot-r1" if monster_box else "bop-fixture-r1"
    required = BOP_INSTALLED | ({MONSTER_BOX} if monster_box else set[str]())
    manifest_path = (
        Path(__file__).resolve().parents[1]
        / "evidence/item-10"
        / diagnostic
        / "archive-manifest.json"
    )
    manifest = cast("dict[str, object]", parse_strict_json(manifest_path.read_bytes()))
    members = cast("list[dict[str, object]]", manifest["files"])
    names = [
        "trace.jsonl",
        *["trace.jsonl.classes/" + name + ".class" for name in sorted(required)],
        "trace.jsonl.classes/com/tristankechlo/explorations/worldgen/features/ScarecrowFeature.class",
    ]
    digests: dict[str, str] = {}
    trace_bytes = b""
    for name in names:
        path = raw_root / name
        if not path.resolve().is_relative_to(raw_root.resolve()):
            fail("BOP input escapes raw root")
        payload = path.read_bytes()
        digest = hashlib.sha256(payload).hexdigest()
        records = [r for r in members if r["relative_path"] == name]
        if (
            len(records) != 1
            or records[0]["sha256"] != digest
            or records[0]["size_bytes"] != len(payload)
        ):
            fail("BOP input differs from archived member: " + name)
        digests[name] = digest
        if name == "trace.jsonl":
            trace_bytes = payload
    rows: list[dict[str, object]] = []
    for line in trace_bytes.splitlines():
        row = parse_strict_json(line)
        if not isinstance(row, dict):
            fail("BOP trace row is not an object")
        rows.append(cast("dict[str, object]", row))
    result = check_feature_rows(rows, monster_box=monster_box)
    for name, digest in cast("dict[str, str]", result["installations"]).items():
        target = (
            "com/tristankechlo/explorations/worldgen/features/ScarecrowFeature"
            if name == "scarecrow"
            else name
        )
        if digests["trace.jsonl.classes/" + target + ".class"] != digest:
            fail("BOP installation differs from incoming class")
    return {
        "status": "PASS",
        "scope": ("Monster Box r1" if monster_box else "BOP r1")
        + " capture integrity only; not saved-block acceptance",
        "sha256": digests["trace.jsonl"],
        **result,
    }


if __name__ == "__main__":
    if len(sys.argv[1:]) == MIN_EVENTS and sys.argv[1] in {"--bop-r1", "--monster-r1"}:
        print(
            json.dumps(
                validate_feature_trace(
                    Path(sys.argv[2]), monster_box=sys.argv[1] == "--monster-r1"
                ),
                indent=2,
            )
        )
        raise SystemExit(0)
    if len(sys.argv[1:]) != 1:
        message = "usage: python -m tools.validate_item10_trace TRACE.jsonl"
        raise SystemExit(message)
    print(json.dumps(validate_trace(Path(sys.argv[1])), indent=2))
