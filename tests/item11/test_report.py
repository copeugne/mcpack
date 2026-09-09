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


@pytest.mark.parametrize(
    "defect", ["world", "source", "archive", "backup", "category", "mode", "human", "digest"]
)
def test_report_rejects_misbound_or_incomplete_result(  # noqa: C901 - existing fixed mutation cases
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, defect: str
) -> None:
    namespace = runpy.run_path(str(SCRIPT))
    build = namespace["build"]
    result = json.loads(gzip.decompress(PILOT.read_bytes()))
    if defect == "world":
        result["world"] = "wrong-world"
    elif defect == "source":
        result["inputs"]["census_sha256"] = "0" * 64
    elif defect in ("archive", "backup"):
        key = "archive_manifest_sha256" if defect == "archive" else "world_backup_sha256"
        result["inputs"][key] = "0" * 64
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
            if defect in ("archive", "backup") and path.name != PILOT.name:
                pytest.fail("accepted first result with mismatched world provenance")
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


def test_report_includes_retained_feasible_and_failed_costs() -> None:
    report = runpy.run_path(str(SCRIPT))["build"](ROOT / "evidence/item-11/results")
    assert "| ordinary-r1-baseline / east-north / boat | 96.00 [76.80, 128.00] |" in report
    assert (
        "| ocean-heavy-r1-without-sparse / east-south / boat | null | "
        "94.50 [75.60, 126.00] | 96.00 [76.80, 128.00] |" in report
    )
    assert (
        "| ordinary-r1-baseline / east-north / boat | 59; median 0.75; "
        "central [0.00, 18.00]; speed [0.00, 24.00] |" in report
    )
    assert "## Modeled repeated-family interval times" in report
    assert "No repeat: right-censored at 768 blocks" in report
    assert (
        "| ordinary-r1-without-sparse / east-north | 51 / 1 / 72 / 0 | "
        "50 / 1 / 72 / 0 | 49 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | "
        "0 / 0 / 0 / 0 | 1 / 1 / 72 / 0 |" in report
    )
    assert (
        "| ordinary-r1-without-sparse / east-south | 105 / 1 / 104 / 0 | "
        "103 / 0 / 0 / 0 | 103 / 0 / 0 / 0 | 4 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | "
        "0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 |" in report
    )

    assert "Unknown-only / denominator" in report
