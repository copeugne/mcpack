"""Validate retained placement traces against their immutable archive identities."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path
from typing import TYPE_CHECKING, Literal, Never, cast

from tools.run_item10_probe import COLLECTOR_JAR_SHA256

if TYPE_CHECKING:
    from collections.abc import Iterator

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


CaptureMode = Literal["bop", "monster", "spike", "spiral", "fairy", "urn", "bridge", "extras"]
URN_TRIES = 9
URN_SPREAD = (4, 1, 4)
URN = "net/minecraft/world/level/levelgen/feature/RandomPatchFeature"
PLACED = "net/minecraft/world/level/levelgen/placement/PlacedFeature"
SIMPLE = "net/minecraft/world/level/levelgen/feature/SimpleBlockFeature"
SPIRAL = "org/violetmoon/quark/content/world/gen/SpiralSpireGenerator"
FAIRY = "org/violetmoon/quark/content/world/gen/FairyRingGenerator"
NETHER_SPIKE = "org/violetmoon/quark/content/world/gen/ObsidianSpikeGenerator"
END_BUILDING = "org/betterx/betterend/world/features/BuildingListFeature"
END_NBT = "org/betterx/betterend/world/features/NBTFeature"
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

BRIDGE_ROOT = "com/yungnickyoung/minecraft/yungsbridges/world/"
BRIDGE_INSTALLED = {
    BRIDGE_ROOT + "feature/BridgeFeature",
    BRIDGE_ROOT + "feature/AbstractTemplateFeature",
    *{
        BRIDGE_ROOT + "processor/" + name
        for name in (
            "FenceBiomeProcessor",
            "ITemplateFeatureProcessor",
            "LanternRotProcessor",
            "LogBiomeProcessor",
            "OptionalBlockProcessor",
            "OptionalSlabProcessor",
            "OptionalStairProcessor",
            "OptionalWallProcessor",
            "PlanksBiomeProcessor",
            "SlabBiomeProcessor",
            "StairBiomeProcessor",
            "StoneVariationProcessor",
        )
    },
}

EXTRAS_ROOT = "com/yungnickyoung/minecraft/yungsextras/world/"
EXTRAS_INSTALLED = {
    EXTRAS_ROOT + "feature/AbstractNbtFeature",
    *{
        EXTRAS_ROOT + "feature/" + name
        for name in (
            "desert/ChillzoneDesertFeature",
            "desert/DesertGiantTorchFeature",
            "desert/DesertSmallRuinsFeature",
            "desert/DesertObeliskFeature",
            "desert/DesertWellFeature",
            "swamp/SwampArchFeature",
            "swamp/SwampChurchFeature",
            "swamp/SwampCubbyFeature",
            "swamp/SwampDoubleArchFeature",
            "swamp/SwampOgreFeature",
            "swamp/SwampPillarFeature",
        )
    },
    *{
        EXTRAS_ROOT + "processor/" + name
        for name in ("DesertWellProcessor", "INbtFeatureProcessor", "SwampFeatureProcessor")
    },
}

CAPTURE_CLASSES = {
    "bop": BOP_CLASSES,
    "monster": {MONSTER_BOX},
    "spike": {MONSTER_BOX, NETHER_SPIKE, END_BUILDING},
    "spiral": {MONSTER_BOX, NETHER_SPIKE, SPIRAL},
    "fairy": {MONSTER_BOX, NETHER_SPIKE, SPIRAL, END_BUILDING},
    "urn": {MONSTER_BOX, NETHER_SPIKE, SPIRAL, URN},
    "bridge": {MONSTER_BOX, NETHER_SPIKE, SPIRAL, URN, END_BUILDING},
    "extras": {MONSTER_BOX, NETHER_SPIKE, SPIRAL, URN},
}
DIAGNOSTICS = {
    "bop": "bop-fixture-r1",
    "monster": "monster-box-pilot-r1",
    "spike": "nether-spike-pilot-r1",
    "spiral": "spiral-pilot-r1",
    "fairy": "fairy-run-r1",
    "urn": "urn-pilot-r1",
    "bridge": "bridge-pilot-r1",
    "extras": "extras-pilot-r1",
}


def installed_classes(mode: CaptureMode) -> set[str]:
    """Bind the observed populations to their actual transformed classes."""
    return (
        BOP_INSTALLED
        | (CAPTURE_CLASSES[mode] - {END_BUILDING, URN})
        | ({FAIRY} if mode in {"fairy", "urn", "bridge", "extras"} else set[str]())
        | ({PLACED, SIMPLE} if mode in {"urn", "bridge", "extras"} else set[str]())
        | (BRIDGE_INSTALLED if mode in {"bridge", "extras"} else set[str]())
        | (EXTRAS_INSTALLED if mode == "extras" else set[str]())
    )


def check_feature_rows(  # noqa: C901, PLR0912, PLR0915
    rows: list[dict[str, object]], *, mode: CaptureMode = "bop"
) -> dict[str, object]:
    """Check either retained feature population, keeping failed and void outcomes distinct."""
    classes = CAPTURE_CLASSES[mode]
    required = installed_classes(mode)
    dimensions: dict[int, str] = {}
    urn_parents: dict[int, str | None] = {}
    grounds: set[int] = set()
    parts: set[int] = set()
    origins: dict[int, tuple[int, ...]] = {}
    spiral_sources: set[tuple[str, tuple[int, ...]]] = set()
    expected_dimensions = dict.fromkeys(classes, "minecraft:the_end")
    expected_dimensions.update(
        {
            MONSTER_BOX: "minecraft:overworld",
            NETHER_SPIKE: "minecraft:the_nether",
            URN: "minecraft:overworld",
        }
    )
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
        or rows[-1].get("installed") is not True
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
        if kind not in {
            "begin",
            "feature",
            "write",
            "end",
            "generator_end",
            "ground",
            "part",
            "urn_parent",
        }:
            fail("unexpected BOP event or unhandled failure")
        expected = (
            {"kind", "attempt", "class"}
            if kind == "feature"
            else {"kind", "attempt", "placed_feature"}
            if kind == "urn_parent"
            else {"kind", "attempt"}
            if kind == "generator_end"
            else {"kind", "attempt", "position"}
            if kind in {"ground", "part"}
            else FIELDS[cast("str", kind)]
        )
        if set(row) != expected or type(row.get("attempt")) is not int:
            fail("malformed BOP event")
        attempt = cast("int", row["attempt"])
        if kind in {"begin", "write", "ground", "part"}:
            position = row.get("origin" if kind == "begin" else "position")
            if (
                not isinstance(position, list)
                or len(cast("list[object]", position)) != COORDINATES
                or any(type(v) is not int for v in cast("list[object]", position))
            ):
                fail("invalid BOP coordinates")
        if kind == "begin":
            if (
                attempt <= 0
                or attempt in started
                or row["dimension"] not in set(expected_dimensions.values())
            ):
                fail("duplicate or wrong-dimension BOP attempt")
            origins[attempt] = tuple(cast("list[int]", row["origin"]))
            started.add(attempt)
            dimensions[attempt] = cast("str", row["dimension"])
            active[attempt] = None
            continue
        if attempt not in active:
            fail("unpaired BOP event")
        if kind == "feature":
            name = row["class"]
            if not isinstance(name, str) or name.replace(".", "/") not in classes:
                fail("unexpected BOP feature")
            source_class = name.replace(".", "/")
            installed = (
                END_NBT
                if source_class == END_BUILDING
                else PLACED
                if source_class == URN
                else source_class
            )
            if source_class == URN and SIMPLE not in installations:
                fail("urn feature before writer installation")
            if active[attempt] is not None or installed not in installations:
                fail("duplicate feature or feature before installation")
            if dimensions[attempt] != expected_dimensions[source_class]:
                fail("BOP/generator feature has wrong dimension")
            active[attempt] = name
            continue
        name = active[attempt]
        if name is None:
            fail("missing feature")
        building = name == END_BUILDING.replace("/", ".")
        spiral = name == SPIRAL.replace("/", ".")
        urn = name == URN.replace("/", ".")
        if kind == "urn_parent":
            parent = row["placed_feature"]
            if (
                not urn
                or attempt in urn_parents
                or (parent is not None and (not isinstance(parent, str) or ":" not in parent))
            ):
                fail("unexpected or malformed urn parent")
            urn_parents[attempt] = parent
            continue
        if urn and attempt not in urn_parents:
            fail("missing urn parent before result")
        if kind == "part":
            if not spiral or attempt in parts:
                fail("unexpected or repeated spiral part")
            parts.add(attempt)
            spiral_sources.add((dimensions[attempt], origins[attempt]))
            continue
        if kind == "ground":
            if not building or attempt in grounds:
                fail("unexpected or repeated BetterEnd ground")
            grounds.add(attempt)
            continue
        if kind != "generator_end" and type(row.get("returned")) is not bool:
            fail("invalid BOP result")
        if kind == "write":
            flags = row["flags"]
            if building or spiral:
                fail("unexpected writes in retained zero-write feature path")
            if type(flags) is not int or flags not in (
                (2,) if urn else (2, 3) if mode == "bop" else (0,)
            ):
                fail("invalid BOP flags")
            if name.endswith("MonolithFeature") and flags != HELPER_FLAGS:
                fail("unexpected monolith flags")
            if not isinstance(row["state"], str) or not row["state"]:
                fail("invalid BOP block state")
            attempt_writes[attempt] = attempt_writes.get(attempt, 0) + 1
            if name == MONSTER_BOX.replace("/", ".") and attempt_writes[attempt] > 1:
                fail("Monster Box exceeds frozen single-write bound")
            if urn and (
                attempt_writes[attempt] > URN_TRIES
                or not row["state"].startswith("Block{supplementaries:urn}[")
            ):
                fail("urn write exceeds patch bound or has wrong block")
            if urn and any(
                abs(value - origin) > limit
                for value, origin, limit in zip(
                    cast("list[int]", row["position"]), origins[attempt], URN_SPREAD, strict=True
                )
            ):
                fail("urn write outside patch spread")
            writes += 1
            refused += row["returned"] is False
            by_feature[name] = by_feature.get(name, 0) + 1
            if row["returned"]:
                path = (name, flags)
                successful_paths[path] = successful_paths.get(path, 0) + 1
        else:
            generator = name.replace(".", "/") in {MONSTER_BOX, NETHER_SPIKE, SPIRAL}
            if kind != ("generator_end" if generator else "end"):
                fail("wrong generator completion event")
            if urn and row["returned"] != (attempt_writes.get(attempt, 0) > 0):
                fail("urn return disagrees with direct writer attempts")
            if spiral and attempt not in parts:
                fail("missing spiral part")
            if building and (attempt not in grounds or row["returned"] is not False):
                fail("BetterEnd pilot failure needs ground and false return")
            del active[attempt]
    if active or started != set(range(1, len(started) + 1)):
        fail("unfinished or missing BOP attempts")
    if set(installations) != required | {"scarecrow"}:
        fail("incomplete BOP installations")
    if set(by_feature) != {n.replace("/", ".") for n in classes - {END_BUILDING, SPIRAL}}:
        fail("no exercised writes for one BOP feature")
    required_paths = {
        (name.replace("/", "."), flags)
        for name in BOP_CLASSES
        for flags in ((2, 3) if name.endswith("AnomalyFeature") else (3,))
    }
    if mode != "bop":
        required_paths = {
            (name.replace("/", "."), 2 if name == URN else 0)
            for name in classes - {END_BUILDING, SPIRAL}
        }
    if set(successful_paths) != required_paths:
        fail(
            "Monster Box requires a successful write"
            if mode != "bop"
            else "BOP requires successful writes on all three provider/flag paths"
        )
    if mode in {"spiral", "fairy", "urn", "bridge", "extras"} and not parts:
        fail("missing spiral attempts in retained diagnostic")
    return {
        **(
            {"spiral_parts": len(parts), "spiral_source_keys": len(spiral_sources)}
            if mode in {"spiral", "fairy", "urn", "bridge", "extras"}
            else {}
        ),
        **(
            {
                "urn_patch_attempts": len(urn_parents),
                "cave_parent_attempts": sum(
                    parent == "supplementaries:cave_urns" for parent in urn_parents.values()
                ),
            }
            if mode in {"urn", "bridge", "extras"}
            else {}
        ),
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


def validate_feature_trace(raw_root: Path, *, mode: CaptureMode = "bop") -> dict[str, object]:
    """Bind a declared feature trace and incoming classes to its immutable archive."""
    diagnostic = DIAGNOSTICS[mode]
    required = installed_classes(mode)
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
    result = check_feature_rows(rows, mode=mode)
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
        "scope": (
            {
                "bop": "BOP r1",
                "monster": "Monster Box r1",
                "spike": "Nether spike r1",
                "spiral": "Spiral r1",
                "fairy": "Fairy r1",
                "urn": "Urn r1",
                "bridge": "Bridge r1 (zero bridge attempts)",
                "extras": "Extras r1 (zero Extras and bridge attempts)",
            }[mode]
        )
        + " capture integrity only; not saved-block acceptance",
        "sha256": digests["trace.jsonl"],
        **result,
    }


COLLECTION_FIELDS = FIELDS | {
    "feature_installed": {"kind", "class", "input_class_sha256"},
    "feature": {"kind", "attempt", "class"},
    "generator_end": {"kind", "attempt"},
    "template_begin": {
        "kind",
        "attempt",
        "path",
        "position",
        "pivot",
        "rotation",
        "mirror",
        "flags",
    },
    "template_end": {"kind", "attempt", "returned"},
    "flower_end": {"kind", "attempt", "returned"},
    **{
        kind: {"kind", "attempt", "exception"}
        for kind in ("attempt_exception", "template_exception", "flower_exception")
    },
    "write_exception": {"kind", "attempt", "position", "exception"},
    **{
        kind: {"kind", "attempt", "position"}
        for kind in ("ground", "part", "pillar_fill", "flower_begin")
    },
    "urn_parent": {"kind", "attempt", "placed_feature"},
    **{
        kind: {"kind", "attempt", "configured_feature"}
        for kind in ("bridge_configured", "extras_configured")
    },
    **{kind: {"kind", "attempt"} for kind in ("bridge_processor", "extras_processor")},
    "writer": {"kind", "attempt", "site"},
    "flower_state": {"kind", "attempt", "state"},
    "island_context": {"kind", "attempt", "world_class", "worldgen_region"},
}
SCARECROW_CLASS = "com/tristankechlo/explorations/worldgen/features/ScarecrowFeature"
ISLAND_CLASSES = {
    "com/yungnickyoung/minecraft/betterendisland/world/feature/" + name
    for name in (
        "BetterEndGatewayFeature",
        "BetterEndSpawnPlatformFeature",
        "BetterEndPodiumFeature",
        "BetterSpikeFeature",
    )
}
PILLAR_CLASSES = {
    "org/betterx/betterend/world/features/terrain/" + name
    for name in ("FallenPillarFeature", "ObsidianPillarBasementFeature")
}
FULL_COLLECTION_CLASSES = (
    installed_classes("extras")
    | ISLAND_CLASSES
    | PILLAR_CLASSES
    | {SCARECROW_CLASS, "org/betterx/bclib/util/BlocksHelper"}
)
CONDITIONAL_GATEWAY_CLASS = (
    "com/yungnickyoung/minecraft/betterendisland/world/feature/BetterEndGatewayFeature"
)


def _legacy_scarecrow(rows: list[dict[str, object]]) -> None:
    """Identify the frozen collector's sole unlabelled writer, or reject ambiguity.

    The pinned Scarecrow bytecode and its nine packaged configurations require
    these five ordered writes. Zero-write returns and exceptions cannot identify
    their provider in a mixed stream and are deliberately rejected.
    """
    if (
        [row["kind"] for row in rows] != ["begin", *(["write"] * WRITES_PER_ATTEMPT), "end"]
        or rows[0]["dimension"] != "minecraft:overworld"
        or rows[-1]["returned"] is not True
    ):
        fail("collection provider missing identity or strict Scarecrow signature")
    writes = rows[1:-1]
    fence = re.fullmatch(
        r"Block\{minecraft:(acacia|bamboo|birch|cherry|dark_oak|jungle|mangrove|oak|spruce)_fence\}"
        r"\[east=false,north=false,south=false,waterlogged=false,west=false\]",
        cast("str", writes[0]["state"]),
    )
    head = re.fullmatch(
        r"Block\{minecraft:(carved_pumpkin|jack_o_lantern)\}\[facing=(north|east|south|west)\]",
        cast("str", writes[-1]["state"]),
    )
    if fence is None or head is None:
        fail("collection provider missing Scarecrow materials")
    x, y, z = cast("list[int]", rows[0]["origin"])
    # Clockwise arm first, then counterclockwise, with connections facing inward.
    dx, dz, inward, opposite = {
        "north": (1, 0, "west", "east"),
        "east": (0, 1, "north", "south"),
        "south": (-1, 0, "east", "west"),
        "west": (0, -1, "south", "north"),
    }[head[2]]
    positions = [
        [x, y, z],
        [x, y + 1, z],
        [x + dx, y + 1, z + dz],
        [x - dx, y + 1, z - dz],
        [x, y + 2, z],
    ]
    leg = cast("str", writes[0]["state"])
    states = [
        leg,
        "Block{minecraft:hay_block}[axis=y]",
        leg.replace(inward + "=false", inward + "=true"),
        leg.replace(opposite + "=false", opposite + "=true"),
        writes[-1]["state"],
    ]
    if any(
        row["position"] != position or row["state"] != state or row["flags"] != HELPER_FLAGS
        for row, position, state in zip(writes, positions, states, strict=True)
    ):
        fail("collection provider missing exact Scarecrow geometry, states or flags")


def _collection_provider(rows: list[dict[str, object]]) -> None:
    """Reject cross-provider metadata and wrong method completion semantics."""
    feature = next((row for row in rows if row["kind"] == "feature"), None)
    if feature is None:
        _legacy_scarecrow(rows)
    name = SCARECROW_CLASS if feature is None else cast("str", feature["class"]).replace(".", "/")
    kinds = {cast("str", row["kind"]) for row in rows}
    owners = {
        "island_context": ISLAND_CLASSES,
        "pillar_fill": PILLAR_CLASSES,
        "ground": {END_NBT, END_BUILDING},
        "part": {SPIRAL},
        "urn_parent": {URN},
        "bridge_configured": {BRIDGE_ROOT + "feature/BridgeFeature"},
        "bridge_processor": {BRIDGE_ROOT + "feature/BridgeFeature"},
        "extras_configured": {n for n in EXTRAS_INSTALLED if "/feature/" in n},
        "extras_processor": {n for n in EXTRAS_INSTALLED if "/feature/" in n},
        **{
            kind: {FAIRY}
            for kind in (
                "writer",
                "flower_begin",
                "flower_end",
                "flower_exception",
                "flower_state",
            )
        },
    }
    for kind in kinds & owners.keys():
        if name not in owners[kind]:
            fail("collection provider does not own metadata: " + kind)
    required = (
        {"island_context"}
        if name in ISLAND_CLASSES
        else {"urn_parent"}
        if name == URN
        else {"bridge_configured"}
        if name == BRIDGE_ROOT + "feature/BridgeFeature"
        else {"extras_configured"}
        if name.startswith(EXTRAS_ROOT + "feature/")
        else set[str]()
    )
    if not required <= kinds:
        fail("collection provider metadata is incomplete")
    void = name in {MONSTER_BOX, NETHER_SPIKE, SPIRAL, FAIRY} or name.endswith(
        "/BetterSpikeFeature"
    )
    if rows[-1]["kind"] not in {"attempt_exception", "generator_end" if void else "end"}:
        fail("collection provider completion differs from its method return type")
    if name == SCARECROW_CLASS and kinds - {
        "begin",
        "feature",
        "write",
        "write_exception",
        "end",
        "attempt_exception",
    }:
        fail("collection provider metadata cannot be attributed to Scarecrow")


def _collection_event(row: dict[str, object]) -> str:  # noqa: C901 - explicit wire-field checks
    """Check the existing collector wire fields without coercing raw values."""
    kind = row.get("kind")
    if (
        not isinstance(kind, str)
        or kind not in COLLECTION_FIELDS
        or set(row) != COLLECTION_FIELDS[kind]
    ):
        fail("unknown or malformed collection event")
    for field in ("attempt", "flags", "site", "unfinished_attempts"):
        if field in row and (
            type(row[field]) is not int
            or cast("int", row[field]) < (1 if field in {"attempt", "site"} else 0)
        ):
            fail("invalid collection integer: " + field)
    for field in ("origin", "position", "pivot"):
        if field in row:
            value = row[field]
            if (
                not isinstance(value, list)
                or len(cast("list[object]", value)) != COORDINATES
                or any(type(v) is not int for v in cast("list[object]", value))
            ):
                fail("invalid collection coordinates: " + field)
    for field in ("returned", "installed", "worldgen_region"):
        if field in row and type(row[field]) is not bool:
            fail("invalid collection boolean: " + field)
    for field in (
        "class",
        "dimension",
        "state",
        "path",
        "rotation",
        "mirror",
        "exception",
        "world_class",
        "input_class_sha256",
    ):
        if field in row and (not isinstance(row[field], str) or not row[field]):
            fail("invalid collection text: " + field)
    for field in ("configured_feature", "placed_feature"):
        if (
            field in row
            and row[field] is not None
            and (not isinstance(row[field], str) or ":" not in cast("str", row[field]))
        ):
            fail("invalid collection registry key")
    return kind


def collection_attempts(  # noqa: C901, PLR0912, PLR0915
    path: Path,
    *,
    trace_sha256: str,
    class_digests: dict[str, str],
    dimensions: set[str],
    require_complete_observer: bool = False,
) -> Iterator[list[dict[str, object]]]:
    """Stream structurally complete attempts from a hash-bound full collection.

    Callers must supply independently verified archive/class identities and consume
    the iterator completely before publishing results. This preserves every event
    in an attempt; provider-specific location acceptance is a separate requirement.
    Memory retains active attempts only, rather than the complete world trace.
    """
    if not class_digests or not dimensions:
        fail("collection requires class identities and dimension exposure")
    if require_complete_observer:
        missing = FULL_COLLECTION_CLASSES - set(class_digests)
        if set(class_digests) - FULL_COLLECTION_CLASSES or missing not in (
            set(),
            {CONDITIONAL_GATEWAY_CLASS},
        ):
            fail("collection does not bind the complete declared observer class set")
        agent = path.with_name("probe.jar")
        if agent.is_symlink() or not agent.is_file():
            fail("full collection requires the frozen observer JAR")
        with agent.open("rb") as stream:
            if hashlib.file_digest(stream, "sha256").hexdigest() != COLLECTOR_JAR_SHA256:
                fail("full collection observer JAR differs from frozen identity")
        # A loaded-but-undeclared class is not an unexercised generator.
        for name in missing:
            capture = path.with_name(path.name + ".classes") / (name + ".class")
            if capture.exists() or capture.is_symlink():
                fail("undeclared conditional collection incoming class")
    for value in (trace_sha256, *class_digests.values()):
        if len(value) != SHA256_HEX_LENGTH or any(c not in "0123456789abcdef" for c in value):
            fail("invalid declared collection digest")
    class_root = path.with_name(path.name + ".classes")
    if class_root.is_symlink() or not class_root.is_dir():
        fail("missing or linked collection incoming-class directory")
    for name, expected in class_digests.items():
        parts = name.split("/")
        if not name or any(part in {"", ".", ".."} or "\\" in part for part in parts):
            fail("invalid collection incoming-class path")
        member = class_root / (name + ".class")
        if not member.resolve().is_relative_to(class_root.resolve()) or member.is_symlink():
            fail("collection incoming class escapes its directory or is linked")
        if not member.is_file():
            fail("missing collection incoming class: " + name)
        with member.open("rb") as class_stream:
            if hashlib.file_digest(class_stream, "sha256").hexdigest() != expected:
                fail("collection incoming class differs from declared identity: " + name)
    with path.open("rb") as stream:
        if hashlib.file_digest(stream, "sha256").hexdigest() != trace_sha256:
            fail("collection trace differs from declared archive identity")
        _ = stream.seek(0)
        digest = hashlib.sha256()
        active: dict[int, list[dict[str, object]]] = {}
        marks: dict[int, set[str]] = {}
        nested: dict[int, set[str]] = {}
        seen: set[int] = set()
        installed: set[str] = set()
        shutdown = False
        for line in stream:
            digest.update(line)
            raw = parse_strict_json(line)
            if not isinstance(raw, dict):
                fail("collection row is not an object")
            row = cast("dict[str, object]", raw)
            kind = _collection_event(row)
            if shutdown:
                fail("collection event after shutdown")
            if kind in {"installed", "feature_installed"}:
                name = SCARECROW_CLASS if kind == "installed" else cast("str", row["class"])
                if name in installed or class_digests.get(name) != row["input_class_sha256"]:
                    fail("unexpected or mismatched collection installation")
                installed.add(name)
                continue
            if kind == "shutdown":
                if active or row["installed"] is not True or row["unfinished_attempts"] != 0:
                    fail("unfinished or unhealthy collection shutdown")
                shutdown = True
                continue
            attempt = cast("int", row["attempt"])
            if kind == "begin":
                if attempt in seen or row["dimension"] not in dimensions:
                    fail("duplicate collection attempt or undeclared dimension")
                seen.add(attempt)
                active[attempt] = [row]
                marks[attempt] = set()
                nested[attempt] = set()
                continue
            if attempt not in active:
                fail("unpaired collection event")
            if kind in {
                "feature",
                "ground",
                "part",
                "urn_parent",
                "bridge_configured",
                "extras_configured",
                "island_context",
                "pillar_fill",
            }:
                if kind in marks[attempt]:
                    fail("duplicate collection attempt metadata")
                marks[attempt].add(kind)
            if kind == "feature":
                name = cast("str", row["class"]).replace(".", "/")
                source = END_NBT if name == END_BUILDING else PLACED if name == URN else name
                if source not in installed:
                    fail("collection feature before verified installation")
            for phase in ("template", "flower"):
                if kind == phase + "_begin":
                    if phase in nested[attempt]:
                        fail("nested collection delegate")
                    nested[attempt].add(phase)
                elif kind in {phase + "_end", phase + "_exception"}:
                    if phase not in nested[attempt]:
                        fail("unpaired collection delegate completion")
                    nested[attempt].remove(phase)
            active[attempt].append(row)
            if kind in {"end", "generator_end", "attempt_exception"}:
                if nested[attempt]:
                    fail("collection attempt ended inside delegate")
                if "feature" not in marks[attempt] and (
                    SCARECROW_CLASS not in installed or class_digests[SCARECROW_CLASS] != CLASS_SHA
                ):
                    fail("collection provider has no pinned legacy Scarecrow installation")
                _collection_provider(active[attempt])
                del marks[attempt], nested[attempt]
                yield active.pop(attempt)
        if not shutdown or installed != set(class_digests) or seen != set(range(1, len(seen) + 1)):
            fail("incomplete collection stream or installations")
        if digest.hexdigest() != trace_sha256:
            fail("collection trace changed during processing")


if __name__ == "__main__":
    if len(sys.argv[1:]) == MIN_EVENTS and sys.argv[1] in {
        "--bop-r1",
        "--monster-r1",
        "--spike-r1",
        "--spiral-r1",
        "--fairy-r1",
        "--urn-r1",
        "--bridge-r1",
        "--extras-r1",
    }:
        print(
            json.dumps(
                validate_feature_trace(
                    Path(sys.argv[2]), mode=cast("CaptureMode", sys.argv[1][2:-3])
                ),
                indent=2,
            )
        )
        raise SystemExit(0)
    if len(sys.argv[1:]) != 1:
        message = "usage: python -m tools.validate_item10_trace TRACE.jsonl"
        raise SystemExit(message)
    print(json.dumps(validate_trace(Path(sys.argv[1])), indent=2))
