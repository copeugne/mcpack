import copy
import json
from pathlib import Path
from typing import cast

import pytest
from tools.validate_item10_trace import (
    BOP_CLASSES,
    BOP_INSTALLED,
    CLASS_SHA,
    END_BUILDING,
    FAIRY,
    MONSTER_BOX,
    NETHER_SPIKE,
    SPIRAL,
    check_feature_rows,
    check_rows,
    validate_feature_trace,
    validate_trace,
)

TRACE = Path(__file__).resolve().parents[2] / "evidence/item-10/scarecrow-probe-r3/trace.jsonl"


def test_retained_trace_passes_published_identity_and_complete_capture() -> None:
    result = validate_trace(TRACE)
    assert result["attempts"] == 6
    assert result["writes"] == 30
    assert result["five_write_attempts"] == 6
    assert result["refused_writes"] == 0


@pytest.mark.parametrize(
    "defect",
    [
        "identity",
        "missing-write",
        "unpaired",
        "duplicate-end",
        "missing-end",
        "shutdown",
        "malformed",
        "boolean-id",
    ],
)
def test_capture_rejects_broken_event_contract(defect: str) -> None:
    rows = [cast("dict[str, object]", json.loads(line)) for line in TRACE.read_text().splitlines()]
    if defect == "identity":
        rows[0]["input_class_sha256"] = "wrong"
    elif defect == "missing-write":
        del rows[2]
    elif defect == "unpaired":
        rows[2]["attempt"] = 999
    elif defect == "duplicate-end":
        rows.insert(8, copy.deepcopy(rows[7]))
    elif defect == "missing-end":
        del rows[7]
    elif defect == "shutdown":
        rows[-1]["unfinished_attempts"] = 1
    elif defect == "malformed":
        rows[2]["position"] = [1, 2]
    else:
        rows[1]["attempt"] = True
    with pytest.raises(
        ValueError, match=r"installation|writer|unpaired|unfinished|shutdown|coordinates|identity"
    ):
        _ = check_rows(rows)


def test_omitted_whole_attempt_cannot_pass_archive_binding(tmp_path: Path) -> None:
    lines = TRACE.read_bytes().splitlines(keepends=True)
    changed = tmp_path / "trace.jsonl"
    _ = changed.write_bytes(b"".join(lines[:1] + lines[8:]))
    with pytest.raises(ValueError, match="published r3 archive"):
        _ = validate_trace(changed)


def bop_rows() -> list[dict[str, object]]:
    """Small complete capture exercising both supported BOP writers."""

    rows: list[dict[str, object]] = [{"kind": "installed", "input_class_sha256": CLASS_SHA}]
    rows.extend(
        {"kind": "feature_installed", "class": name, "input_class_sha256": "a" * 64}
        for name in sorted(BOP_INSTALLED)
    )
    for attempt, name in enumerate(sorted(BOP_CLASSES), 1):
        rows.extend(
            [
                {
                    "kind": "begin",
                    "attempt": attempt,
                    "dimension": "minecraft:the_end",
                    "origin": [0, 80, 0],
                },
                {"kind": "feature", "attempt": attempt, "class": name.replace("/", ".")},
                {
                    "kind": "write",
                    "attempt": attempt,
                    "position": [0, 80, 0],
                    "state": "Block{minecraft:end_stone}",
                    "flags": 3,
                    "returned": True,
                },
                {"kind": "end", "attempt": attempt, "returned": True},
            ]
        )
        extra = copy.deepcopy(rows[-2])
        extra["flags"] = 2 if name.endswith("AnomalyFeature") else 3
        extra["returned"] = name.endswith("AnomalyFeature")
        rows.insert(len(rows) - 1, extra)
    rows.append({"kind": "shutdown", "installed": True, "unfinished_attempts": 0})
    return rows


def test_bop_capture_preserves_refused_write_denominator() -> None:

    result = check_feature_rows(bop_rows())
    assert result["attempts"] == 2
    assert result["writes"] == 4
    assert result["refused_writes"] == 1


@pytest.mark.parametrize(
    "defect",
    ["begin", "end", "installation", "feature", "flags", "coordinates", "dimension", "shutdown"],
)
def test_bop_capture_rejects_broken_contract(defect: str) -> None:

    rows = bop_rows()
    kind = {
        "installation": "feature_installed",
        "coordinates": "write",
        "flags": "write",
        "dimension": "begin",
    }.get(defect, defect)
    index = next(i for i, row in enumerate(rows) if row["kind"] == kind)
    if defect in {"begin", "end", "installation"}:
        del rows[index]
    elif defect == "feature":
        rows.insert(index, copy.deepcopy(rows[index]))
    elif defect == "flags":
        rows[index]["flags"] = True
    elif defect == "coordinates":
        rows[index]["position"] = [True, 80, 0]
    elif defect == "dimension":
        rows[index]["dimension"] = "minecraft:overworld"
    else:
        rows[index]["unfinished_attempts"] = 1
    with pytest.raises(ValueError, match=r"BOP|duplicate feature|feature before installation"):
        _ = check_feature_rows(rows)


def test_bop_changed_trace_rejected_before_class_reads(tmp_path: Path) -> None:

    _ = (tmp_path / "trace.jsonl").write_text("{}\n")
    with pytest.raises(ValueError, match=r"differs from archived member: trace\.jsonl"):
        _ = validate_feature_trace(tmp_path)


def test_bop_escaped_trace_rejected(tmp_path: Path) -> None:

    raw = tmp_path / "raw"
    raw.mkdir()
    outside = tmp_path / "outside.jsonl"
    _ = outside.write_text("{}\n")
    (raw / "trace.jsonl").symlink_to(outside)
    with pytest.raises(ValueError, match="escapes raw root"):
        _ = validate_feature_trace(raw)


def monster_rows() -> list[dict[str, object]]:
    """Retain both successful and refused single-write generator calls."""
    rows = bop_rows()
    seen: set[int] = set()
    single: list[dict[str, object]] = []
    for row in rows:
        if row["kind"] == "write":
            attempt = cast("int", row["attempt"])
            if attempt in seen:
                continue
            seen.add(attempt)
            row["returned"] = attempt == 1
        single.append(row)
    rows = single
    rows.insert(
        1, {"kind": "feature_installed", "class": MONSTER_BOX, "input_class_sha256": "b" * 64}
    )
    for row in rows:
        if row["kind"] == "begin":
            row["dimension"] = "minecraft:overworld"
        elif row["kind"] == "feature":
            row["class"] = MONSTER_BOX.replace("/", ".")
        elif row["kind"] == "write":
            row["flags"] = 0
        elif row["kind"] == "end":
            row["kind"] = "generator_end"
            del row["returned"]
    return rows


def test_monster_void_completion_keeps_write_denominator() -> None:
    result = check_feature_rows(monster_rows(), mode="monster")
    assert result["attempts"] == 2
    assert result["writes"] == 2
    assert result["refused_writes"] == 1


@pytest.mark.parametrize(
    "defect", ["boolean-end", "excess-write", "dimension", "missing-end", "refused-only"]
)
def test_monster_capture_rejects_invalid_generator_contract(defect: str) -> None:
    rows = monster_rows()
    if defect == "boolean-end":
        next(r for r in rows if r["kind"] == "generator_end")["returned"] = True
    elif defect == "excess-write":
        index = next(i for i, r in enumerate(rows) if r["kind"] == "write")
        rows.insert(index, copy.deepcopy(rows[index]))
    elif defect == "dimension":
        next(r for r in rows if r["kind"] == "begin")["dimension"] = "minecraft:the_end"
    elif defect == "refused-only":
        for row in rows:
            if row["kind"] == "write":
                row["returned"] = False
    else:
        del rows[next(i for i, r in enumerate(rows) if r["kind"] == "generator_end")]
    with pytest.raises(ValueError, match=r"BOP|Monster Box"):
        _ = check_feature_rows(rows, mode="monster")


@pytest.mark.parametrize("path", ["anomaly-helper", "anomaly-direct", "monolith"])
def test_bop_requires_successful_write_on_each_path(path: str) -> None:
    rows = bop_rows()
    attempt = 2 if path == "monolith" else 1
    flags = 2 if path == "anomaly-direct" else 3
    for row in rows:
        if row["kind"] == "write" and row["attempt"] == attempt and row["flags"] == flags:
            row["returned"] = False
    with pytest.raises(ValueError, match="successful writes on all three"):
        _ = check_feature_rows(rows)


def test_bop_rejects_omitted_anomaly_final_write() -> None:
    rows = [row for row in bop_rows() if row.get("flags") != 2]
    with pytest.raises(ValueError, match="successful writes on all three"):
        _ = check_feature_rows(rows)


def spike_rows() -> list[dict[str, object]]:
    rows = monster_rows()
    rows.insert(
        1, {"kind": "feature_installed", "class": NETHER_SPIKE, "input_class_sha256": "c" * 64}
    )
    rows[-1:-1] = [
        {"kind": "begin", "attempt": 3, "dimension": "minecraft:the_nether", "origin": [0, 80, 0]},
        {"kind": "feature", "attempt": 3, "class": NETHER_SPIKE.replace("/", ".")},
        {
            "kind": "write",
            "attempt": 3,
            "position": [0, 80, 0],
            "state": "Block{minecraft:obsidian}",
            "flags": 0,
            "returned": True,
        },
        {"kind": "generator_end", "attempt": 3},
        {"kind": "begin", "attempt": 4, "dimension": "minecraft:the_end", "origin": [0, 80, 0]},
        {"kind": "feature", "attempt": 4, "class": END_BUILDING.replace("/", ".")},
        {"kind": "ground", "attempt": 4, "position": [0, 81, 0]},
        {"kind": "end", "attempt": 4, "returned": False},
    ]
    return rows


def test_mixed_capture_keeps_void_and_false_returns_separate() -> None:
    result = check_feature_rows(spike_rows(), mode="spike")
    assert result["attempts"] == 4
    assert result["writes"] == 3
    assert result["refused_writes"] == 1


@pytest.mark.parametrize(
    "defect",
    [
        "dimension",
        "wrong-ending",
        "missing-ground",
        "repeated-ground",
        "true-building-end",
        "refused-spike",
        "shutdown-type",
    ],
)
def test_mixed_capture_rejects_invalid_lifecycle(defect: str) -> None:
    rows = spike_rows()
    if defect == "dimension":
        next(r for r in rows if r["kind"] == "begin" and r["attempt"] == 3)["dimension"] = (
            "minecraft:overworld"
        )
    elif defect == "wrong-ending":
        end = next(r for r in rows if r["kind"] == "generator_end" and r["attempt"] == 3)
        end.update(kind="end", returned=False)
    elif defect == "missing-ground":
        rows = [r for r in rows if r["kind"] != "ground"]
    elif defect == "repeated-ground":
        index = next(i for i, r in enumerate(rows) if r["kind"] == "ground")
        rows.insert(index, copy.deepcopy(rows[index]))
    elif defect == "true-building-end":
        next(r for r in rows if r["kind"] == "end")["returned"] = True
    elif defect == "refused-spike":
        next(r for r in rows if r["kind"] == "write" and r["attempt"] == 3)["returned"] = False
    else:
        rows[-1]["installed"] = 1
    with pytest.raises(
        ValueError, match=r"dimension|completion|ground|false return|successful write|shutdown"
    ):
        _ = check_feature_rows(rows, mode="spike")


def spiral_rows() -> list[dict[str, object]]:
    rows = [r for r in spike_rows() if r.get("attempt") != 4]
    rows.insert(1, {"kind": "feature_installed", "class": SPIRAL, "input_class_sha256": "d" * 64})
    for attempt, destination in [(4, [0, 0, 0]), (5, [16, 0, 0])]:
        rows[-1:-1] = [
            {
                "kind": "begin",
                "attempt": attempt,
                "dimension": "minecraft:the_end",
                "origin": [16, 0, 16],
            },
            {"kind": "feature", "attempt": attempt, "class": SPIRAL.replace("/", ".")},
            {"kind": "part", "attempt": attempt, "position": destination},
            {"kind": "generator_end", "attempt": attempt},
        ]
    return rows


def test_zero_write_spiral_parts_keep_shared_source() -> None:
    result = check_feature_rows(spiral_rows(), mode="spiral")
    assert result["attempts"] == 5
    assert result["spiral_parts"] == 2
    assert result["spiral_source_keys"] == 1
    assert result["writes"] == 3


def test_absent_fairy_helper_still_requires_installed_class() -> None:
    rows = spiral_rows()
    with pytest.raises(ValueError, match="installations"):
        _ = check_feature_rows(rows, mode="fairy")
    rows.insert(1, {"kind": "feature_installed", "class": FAIRY, "input_class_sha256": "e" * 64})
    assert check_feature_rows(rows, mode="fairy")["attempts"] == 5


@pytest.mark.parametrize(
    "defect", ["missing", "duplicate", "wrong-feature", "coordinates", "write", "no-attempts"]
)
def test_zero_write_part_capture_rejects_invalid_trace(defect: str) -> None:
    rows = spiral_rows()
    index = next(i for i, r in enumerate(rows) if r["kind"] == "part")
    if defect == "missing":
        del rows[index]
    elif defect == "duplicate":
        rows.insert(index, copy.deepcopy(rows[index]))
    elif defect == "wrong-feature":
        rows[index]["attempt"] = 3
    elif defect == "coordinates":
        rows[index]["position"] = [True, 0, 0]
    elif defect == "write":
        rows.insert(
            index + 1,
            {
                "kind": "write",
                "attempt": 4,
                "position": [0, 0, 0],
                "state": "obsidian",
                "flags": 0,
                "returned": True,
            },
        )
    else:
        rows = [r for r in rows if r.get("attempt") not in {4, 5}]
    with pytest.raises(ValueError, match=r"spiral|unpaired|coordinates|zero-write"):
        _ = check_feature_rows(rows, mode="spiral")


@pytest.mark.parametrize(
    "defect", ["missing", "duplicate", "type", "flags", "block", "return", "coordinates"]
)
def test_urn_parent_and_write_boundaries(defect: str) -> None:
    raw = TRACE.parents[3] / "evidence/raw/item10/urn-pilot-r1-custody/restored/trace.jsonl"
    rows = cast(
        "list[dict[str, object]]", [json.loads(line) for line in raw.read_text().splitlines()]
    )
    parent = next(i for i, row in enumerate(rows) if row["kind"] == "urn_parent")
    urn_ids = {row["attempt"] for row in rows if row["kind"] == "urn_parent"}
    write = next(
        i for i, row in enumerate(rows) if row["kind"] == "write" and row["attempt"] in urn_ids
    )
    if defect == "missing":
        del rows[parent]
    elif defect == "duplicate":
        rows.insert(parent, copy.deepcopy(rows[parent]))
    elif defect == "type":
        rows[parent]["placed_feature"] = 7
    elif defect == "flags":
        rows[write]["flags"] = 0
    elif defect == "coordinates":
        rows[write]["position"] = [999999, 0, 0]
    elif defect == "block":
        rows[write]["state"] = "Block{minecraft:stone}"
    else:
        end = next(
            row for row in rows if row["kind"] == "end" and row["attempt"] == rows[write]["attempt"]
        )
        end["returned"] = False
    with pytest.raises(ValueError, match=r"urn|flags"):
        _ = check_feature_rows(rows, mode="urn")
