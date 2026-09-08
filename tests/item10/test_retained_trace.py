import copy
import json
from pathlib import Path
from typing import cast

import pytest
from tools.validate_item10_trace import check_rows, validate_trace

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
