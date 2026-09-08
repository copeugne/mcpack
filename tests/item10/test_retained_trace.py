import copy
import json
from pathlib import Path
from typing import cast

import pytest
from tools.validate_item10_trace import (
    BOP_CLASSES,
    BOP_INSTALLED,
    CLASS_SHA,
    check_bop_rows,
    check_rows,
    validate_bop_trace,
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

    result = check_bop_rows(bop_rows())
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
        _ = check_bop_rows(rows)


def test_bop_changed_trace_rejected_before_class_reads(tmp_path: Path) -> None:

    _ = (tmp_path / "trace.jsonl").write_text("{}\n")
    with pytest.raises(ValueError, match=r"differs from archived member: trace\.jsonl"):
        _ = validate_bop_trace(tmp_path)


def test_bop_escaped_trace_rejected(tmp_path: Path) -> None:

    raw = tmp_path / "raw"
    raw.mkdir()
    outside = tmp_path / "outside.jsonl"
    _ = outside.write_text("{}\n")
    (raw / "trace.jsonl").symlink_to(outside)
    with pytest.raises(ValueError, match="escapes raw root"):
        _ = validate_bop_trace(raw)


@pytest.mark.parametrize("path", ["anomaly-helper", "anomaly-direct", "monolith"])
def test_bop_requires_successful_write_on_each_path(path: str) -> None:
    rows = bop_rows()
    attempt = 2 if path == "monolith" else 1
    flags = 2 if path == "anomaly-direct" else 3
    for row in rows:
        if row["kind"] == "write" and row["attempt"] == attempt and row["flags"] == flags:
            row["returned"] = False
    with pytest.raises(ValueError, match="successful writes on all three"):
        _ = check_bop_rows(rows)


def test_bop_rejects_omitted_anomaly_final_write() -> None:
    rows = [row for row in bop_rows() if row.get("flags") != 2]
    with pytest.raises(ValueError, match="successful writes on all three"):
        _ = check_bop_rows(rows)
