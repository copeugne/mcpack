# pyright: standard
"""Check the report's actual accepted-input and complete-matrix boundaries."""

import gzip
import hashlib
import json
import runpy
from pathlib import Path

import pytest
from tools.analyze_route_opportunities import ROOT, accepted_inputs, read_bound

SCRIPT = ROOT / "evidence/item-11/summarize.py"
PILOT = ROOT / "evidence/item-11/results/full-ordinary-r1-baseline.json.gz"


@pytest.mark.parametrize("defect", ["world", "source", "category", "mode", "human", "digest"])
def test_report_rejects_misbound_or_incomplete_result(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, defect: str
) -> None:
    namespace = runpy.run_path(str(SCRIPT))
    build = namespace["build"]
    result = json.loads(gzip.decompress(PILOT.read_bytes()))
    if defect == "world":
        result["world"] = "wrong-world"
    elif defect == "source":
        result["inputs"]["census_sha256"] = "0" * 64
    elif defect == "category":
        result["routes"]["east-south"]["summaries"].pop()
    elif defect == "mode":
        del result["routes"]["east-south"]["transport"]["boat"]
    elif defect == "human":
        result["human_metrics"] = "OBSERVED"
    encoded = gzip.compress(json.dumps(result).encode(), mtime=0)
    accepted = accepted_inputs()
    first = "full-ordinary-r1-baseline"
    ordered = {first: accepted[first], **accepted}
    monkeypatch.setitem(build.__globals__, "accepted_inputs", lambda: ordered)

    def read(path: Path, expected: str | None = None) -> bytes:
        if path.parent == tmp_path:
            return encoded
        if path.parent == ROOT / "evidence/item-11/validation/full" and defect != "digest":
            return json.dumps(
                {
                    "world": first,
                    "output_bytes": len(encoded),
                    "sha256": hashlib.sha256(encoded).hexdigest(),
                }
            ).encode()
        return read_bound(path, expected)

    monkeypatch.setitem(build.__globals__, "read_bound", read)
    with pytest.raises(ValueError, match=r"mismatch|accepted census|incomplete|result digest"):
        build(tmp_path)


def test_complete_report_rebuilds_byte_identically() -> None:
    build = runpy.run_path(str(SCRIPT))["build"]
    assert (
        build(ROOT / "evidence/item-11/results")
        == (ROOT / "evidence/item-11/report.md").read_text()
    )
