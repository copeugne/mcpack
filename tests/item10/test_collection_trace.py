"""Full-stream structure checks; family/location acceptance is tested separately."""

import hashlib
import json
from pathlib import Path
from typing import cast

import pytest
from tools.analyze_structure_density import nonregistry_attempt_outcome, nonregistry_membership
from tools.validate_item10_trace import SCARECROW_CLASS, collection_attempts

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
            dimensions={"minecraft:the_end"},
        )
    )


def test_complete_attempt_preserves_refusals_and_all_metadata(tmp_path: Path) -> None:
    rows = events()
    assert consume(tmp_path, rows) == [rows[2:-1]]


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
