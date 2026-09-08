"""Full-stream structure checks; family/location acceptance is tested separately."""

import hashlib
import json
from pathlib import Path
from typing import cast

import pytest
from tools import validate_item10_trace as validator
from tools.analyze_structure_density import (
    nonregistry_attempt_outcome,
    nonregistry_location_groups,
    nonregistry_membership,
)
from tools.validate_item10_trace import (
    FULL_COLLECTION_CLASSES,
    SCARECROW_CLASS,
    collection_attempts,
)

FEATURE = "com/yungnickyoung/minecraft/betterendisland/world/feature/BetterEndGatewayFeature"
CLASS_BYTES = {SCARECROW_CLASS: b"scarecrow fixture", FEATURE: b"gateway fixture"}
DIGESTS = {name: hashlib.sha256(payload).hexdigest() for name, payload in CLASS_BYTES.items()}


def events() -> list[dict[str, object]]:
    return [
        {"kind": "installed", "input_class_sha256": DIGESTS[SCARECROW_CLASS]},
        {"kind": "feature_installed", "class": FEATURE, "input_class_sha256": DIGESTS[FEATURE]},
        {"kind": "begin", "attempt": 1, "dimension": "minecraft:the_end", "origin": [1, 2, 3]},
        {"kind": "feature", "attempt": 1, "class": FEATURE.replace("/", ".")},
        {
            "kind": "island_context",
            "attempt": 1,
            "world_class": "test.World",
            "worldgen_region": True,
        },
        {
            "kind": "template_begin",
            "attempt": 1,
            "path": "betterendisland:gateway",
            "position": [1, 2, 3],
            "pivot": [1, 0, 1],
            "rotation": "NONE",
            "mirror": "NONE",
            "flags": 2,
        },
        {
            "kind": "write",
            "attempt": 1,
            "position": [1, 2, 3],
            "state": "stone",
            "flags": 2,
            "returned": False,
        },
        {"kind": "template_end", "attempt": 1, "returned": True},
        {"kind": "end", "attempt": 1, "returned": True},
        {"kind": "shutdown", "installed": True, "unfinished_attempts": 0},
    ]


def consume(
    tmp_path: Path,
    rows: list[dict[str, object]],
    *,
    wrong_hash: bool = False,
    class_defect: str | None = None,
    require_complete_observer: bool = False,
) -> list[list[dict[str, object]]]:
    path = tmp_path / "trace.jsonl"
    payload = "".join(json.dumps(row) + "\n" for row in rows).encode()
    _ = path.write_bytes(payload)
    for name, content in CLASS_BYTES.items():
        member = tmp_path / "trace.jsonl.classes" / (name + ".class")
        member.parent.mkdir(parents=True, exist_ok=True)
        _ = member.write_bytes(content)
    target = tmp_path / "trace.jsonl.classes" / (FEATURE + ".class")
    if class_defect == "missing":
        target.unlink()
    elif class_defect == "changed":
        _ = target.write_bytes(b"changed")
    elif class_defect == "linked":
        outside = tmp_path / "outside.class"
        _ = outside.write_bytes(CLASS_BYTES[FEATURE])
        target.unlink()
        target.symlink_to(outside)
    return list(
        collection_attempts(
            path,
            trace_sha256="0" * 64 if wrong_hash else hashlib.sha256(payload).hexdigest(),
            class_digests=DIGESTS,
            dimensions={"minecraft:the_end", "minecraft:overworld"},
            require_complete_observer=require_complete_observer,
        )
    )


def test_complete_attempt_preserves_refusals_and_all_metadata(tmp_path: Path) -> None:
    rows = events()
    assert consume(tmp_path, rows) == [rows[2:-1]]


def test_missing_feature_cannot_default_plain_writes_to_scarecrow(tmp_path: Path) -> None:
    rows = [
        row
        for row in events()
        if row["kind"] in {"installed", "feature_installed", "begin", "write", "end", "shutdown"}
    ]
    with pytest.raises(ValueError, match="collection provider"):
        _ = consume(tmp_path, rows)


@pytest.mark.parametrize(
    "defect", [None, "identity", "empty", "exception", "material", "arm", "flags", "return"]
)
def test_legacy_scarecrow_requires_complete_distinct_writer_signature(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, defect: str | None
) -> None:
    if defect != "identity":
        monkeypatch.setattr(validator, "CLASS_SHA", DIGESTS[SCARECROW_CLASS])
    leg = (
        "Block{minecraft:oak_fence}"
        "[east=false,north=false,south=false,waterlogged=false,west=false]"
    )
    states = [
        leg,
        "Block{minecraft:hay_block}[axis=y]",
        leg.replace("east=false", "east=true"),
        leg.replace("west=false", "west=true"),
        "Block{minecraft:carved_pumpkin}[facing=south]",
    ]
    positions = [[1, 2, 3], [1, 3, 3], [0, 3, 3], [2, 3, 3], [1, 4, 3]]
    rows: list[dict[str, object]] = [
        {"kind": "begin", "attempt": 1, "dimension": "minecraft:overworld", "origin": [1, 2, 3]},
        *[
            {
                "kind": "write",
                "attempt": 1,
                "position": pos,
                "state": state,
                "flags": 3,
                "returned": False,
            }
            for pos, state in zip(positions, states, strict=True)
        ],
        {"kind": "end", "attempt": 1, "returned": True},
    ]
    if defect == "empty":
        rows = [rows[0], rows[-1]]
    elif defect == "exception":
        rows[-1] = {"kind": "attempt_exception", "attempt": 1, "exception": "test.Failure"}
    elif defect == "material":
        rows[2]["state"] = "Block{minecraft:stone}"
    elif defect == "arm":
        rows[3]["position"] = [2, 3, 3]
    elif defect == "flags":
        rows[1]["flags"] = 2
    elif defect == "return":
        rows[-1]["returned"] = False
    stream = [*events()[:2], *rows, events()[-1]]
    if defect is None:
        assert consume(tmp_path, stream) == [rows]
        assert all(row["returned"] is False for row in rows[1:-1])
    else:
        with pytest.raises(ValueError, match="collection provider"):
            _ = consume(tmp_path, stream)


def test_partial_observer_cannot_be_promoted_to_full_collection(tmp_path: Path) -> None:
    assert len(FULL_COLLECTION_CLASSES) == 50
    with pytest.raises(ValueError, match="complete declared observer class set"):
        _ = consume(tmp_path, events(), require_complete_observer=True)


@pytest.mark.parametrize(
    "defect",
    [None, "all_loaded", "other_missing", "jar_missing", "jar_changed", "capture", "event"],
)
def test_conditional_gateway_requires_frozen_observer_and_consistent_absence(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, defect: str | None
) -> None:
    # Identity checking uses small fixture bytes; the Java fixture separately pins
    # the actual collector and verifies JVM loading versus capture behavior.
    agent = b"frozen observer fixture"
    monkeypatch.setattr(validator, "COLLECTOR_JAR_SHA256", hashlib.sha256(agent).hexdigest())
    if defect != "jar_missing":
        _ = (tmp_path / "probe.jar").write_bytes(b"changed" if defect == "jar_changed" else agent)
    names = FULL_COLLECTION_CLASSES - {FEATURE}
    if defect == "all_loaded":
        names = FULL_COLLECTION_CLASSES
    if defect == "other_missing":
        names = names - {SCARECROW_CLASS}
    digests: dict[str, str] = {}
    rows: list[dict[str, object]] = []
    for name in sorted(names):
        payload = name.encode()
        digests[name] = hashlib.sha256(payload).hexdigest()
        member = tmp_path / "trace.jsonl.classes" / (name + ".class")
        member.parent.mkdir(parents=True, exist_ok=True)
        _ = member.write_bytes(payload)
        rows.append(
            {"kind": "installed", "input_class_sha256": digests[name]}
            if name == SCARECROW_CLASS
            else {"kind": "feature_installed", "class": name, "input_class_sha256": digests[name]}
        )
    if defect == "capture":
        _ = (tmp_path / "trace.jsonl.classes" / (FEATURE + ".class")).write_bytes(b"undeclared")
    if defect == "event":
        rows.append({"kind": "feature_installed", "class": FEATURE, "input_class_sha256": "a" * 64})
    rows.append({"kind": "shutdown", "installed": True, "unfinished_attempts": 0})
    path = tmp_path / "trace.jsonl"
    payload = "".join(json.dumps(row) + "\n" for row in rows).encode()
    _ = path.write_bytes(payload)
    attempts = collection_attempts(
        path,
        trace_sha256=hashlib.sha256(payload).hexdigest(),
        class_digests=digests,
        dimensions={"minecraft:the_end"},
        require_complete_observer=True,
    )
    if defect in {None, "all_loaded"}:
        assert list(attempts) == []
    else:
        with pytest.raises(ValueError, match="collection"):
            _ = list(attempts)


@pytest.mark.parametrize("defect", ["missing_feature", "wrong_provider", "wrong_end"])
def test_provider_metadata_cannot_be_reassigned_or_dropped(tmp_path: Path, defect: str) -> None:
    rows = events()
    if defect == "missing_feature":
        del rows[3]
    elif defect == "wrong_provider":
        rows[3]["class"] = SCARECROW_CLASS
    else:
        rows[8] = {"kind": "generator_end", "attempt": 1}
    with pytest.raises(ValueError, match="collection provider"):
        _ = consume(tmp_path, rows)


@pytest.mark.parametrize("defect", ["missing", "changed", "linked"])
def test_incoming_class_bytes_are_required(tmp_path: Path, defect: str) -> None:
    with pytest.raises(ValueError, match="collection incoming class"):
        _ = consume(tmp_path, events(), class_defect=defect)


def test_exception_attempt_is_retained_as_failure_not_a_location(tmp_path: Path) -> None:
    rows = events()
    rows[7] = {"kind": "template_exception", "attempt": 1, "exception": "test.Failure"}
    rows[8] = {"kind": "attempt_exception", "attempt": 1, "exception": "test.Failure"}
    assert consume(tmp_path, rows) == [rows[2:-1]]


@pytest.mark.parametrize(
    "defect",
    [
        "hash",
        "installation",
        "missing_installation",
        "missing_end",
        "missing_template_end",
        "duplicate_begin",
        "duplicate_context",
        "after_shutdown",
        "dimension",
        "boolean_coordinate",
        "coerced_return",
        "unknown_event",
        "missing_shutdown",
        "attempt_gap",
        "nested_template",
    ],
)
def test_rejects_incomplete_or_mismatched_collection(  # noqa: C901, PLR0912 - explicit mutation cases
    tmp_path: Path, defect: str
) -> None:
    rows = events()
    if defect == "installation":
        rows[1]["input_class_sha256"] = "b" * 64
    elif defect == "missing_installation":
        del rows[1]
    elif defect == "missing_end":
        del rows[8]
    elif defect == "missing_template_end":
        del rows[7]
    elif defect == "duplicate_begin":
        rows.insert(3, rows[2].copy())
    elif defect == "duplicate_context":
        rows.insert(5, rows[4].copy())
    elif defect == "after_shutdown":
        rows.append(rows[2].copy())
    elif defect == "dimension":
        rows[2]["dimension"] = "test:outside"
    elif defect == "boolean_coordinate":
        rows[6]["position"] = [True, 2, 3]
    elif defect == "coerced_return":
        rows[6]["returned"] = 1
    elif defect == "unknown_event":
        rows[6]["kind"] = "unhandled"
    elif defect == "missing_shutdown":
        _ = rows.pop()
    elif defect == "attempt_gap":
        for row in rows:
            if "attempt" in row:
                row["attempt"] = 2
    elif defect == "nested_template":
        rows.insert(6, rows[5].copy())
    with pytest.raises(ValueError, match=r"collection|delegate"):
        _ = consume(tmp_path, rows, wrong_hash=defect == "hash")


@pytest.mark.parametrize("diagnostic", ["bridge-pilot-r1", "extras-pilot-r1"])
def test_collection_reader_preserves_retained_mixed_trace(diagnostic: str) -> None:
    root = Path(__file__).resolve().parents[2]
    raw = root / "evidence/raw/item10" / diagnostic
    trace = raw / "trace.jsonl"
    if not trace.is_file():
        pytest.skip("Restored retained trace is required for collection-reader integration")
    manifest = cast(
        "dict[str, list[dict[str, str]]]",
        json.loads((root / "evidence/item-10" / diagnostic / "archive-manifest.json").read_text()),
    )
    prefix = "trace.jsonl.classes/"
    classes = {
        row["relative_path"][len(prefix) : -6]: row["sha256"]
        for row in manifest["files"]
        if row["relative_path"].startswith(prefix)
    }
    trace_hash = next(
        row["sha256"] for row in manifest["files"] if row["relative_path"] == "trace.jsonl"
    )
    attempts = list(
        collection_attempts(
            trace,
            trace_sha256=trace_hash,
            class_digests=classes,
            dimensions={"minecraft:overworld", "minecraft:the_nether", "minecraft:the_end"},
        )
    )
    accepted = cast(
        "dict[str, object]",
        json.loads((root / "evidence/item-10" / diagnostic / "trace-validation.json").read_text()),
    )
    assert len(attempts) == accepted["attempts"]
    membership = nonregistry_membership()
    attributed = [nonregistry_attempt_outcome(attempt, membership) for attempt in attempts]
    grouped = nonregistry_location_groups(attributed, {})
    assert (
        sum(
            row["family"] == "quark:spiral_spire"
            for row in cast("list[dict[str, object]]", grouped["locations"])
        )
        == accepted["spiral_source_keys"]
    )
    assert (
        sum(row["family"] == "supplementaries:cave_urn_cache" for row in attributed)
        == accepted["cave_parent_attempts"]
    )
    urn_positions = sum(
        len(cast("list[object]", row["content_positions"]))
        for row in attributed
        if row["family"] == "supplementaries:cave_urn_cache"
    )
    assert (
        urn_positions
        == cast("dict[str, int]", accepted["writes_by_feature"])[
            "net.minecraft.world.level.levelgen.feature.RandomPatchFeature"
        ]
    )
    assert (
        sum(row["kind"] == "write" for attempt in attempts for row in attempt) == accepted["writes"]
    )
