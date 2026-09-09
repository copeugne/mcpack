"""Exercise retained report and visual reproduction, including evidence rejection."""

# pyright: standard
import runpy
from pathlib import Path

import pytest
from tools.analyze_route_opportunities import ROOT

BASE = ROOT / "evidence/item-12"
NAME = "full-ordinary-r1-baseline"


def test_representative_report_and_diagram_reproduce() -> None:
    build = runpy.run_path(str(BASE / "summarize.py"))["build"]
    report = build(BASE / "results", representative=True)
    assert "| 837 / 4096 |" in report
    assert "0/8/0 of 8; 0/8/0 of 8" in report
    assert report.count("UNKNOWN extremum") == 6
    assert "132.0" in report
    render = runpy.run_path(str(BASE / "render.py"))["render"]
    assert (
        render(BASE / "results" / f"{NAME}.json.gz") == (BASE / "ordinary-sections.svg").read_text()
    )


def test_report_rejects_missing_matrix_and_changed_bytes(tmp_path: Path) -> None:
    build = runpy.run_path(str(BASE / "summarize.py"))["build"]
    with pytest.raises(ValueError, match="result matrix"):
        build(tmp_path)
    raw = (BASE / "results" / f"{NAME}.json.gz").read_bytes()
    (tmp_path / f"{NAME}.json.gz").write_bytes(raw + b"changed")
    with pytest.raises(ValueError, match="producer output"):
        build(tmp_path, representative=True)


def test_report_rejects_wrong_archive_binding(monkeypatch: pytest.MonkeyPatch) -> None:
    build = runpy.run_path(str(BASE / "summarize.py"))["build"]
    original = build.__globals__["read_bound"]

    def read(path: Path) -> bytes:
        raw = original(path)
        if path == ROOT / "evidence/item-10" / NAME / "archive-manifest.json":
            return raw + b"\n"
        return raw

    monkeypatch.setitem(build.__globals__, "read_bound", read)
    with pytest.raises(ValueError, match="provenance"):
        build(BASE / "results", representative=True)


def test_complete_report_reproduces_all_worlds_and_family_join() -> None:
    build = runpy.run_path(str(BASE / "summarize.py"))["build"]
    report = build(BASE / "results")
    assert report == (BASE / "report.md").read_text()
    assert report.count("## full-") == 16
    assert "94 observed canonical families" in report
    assert "354 have no case here" in report
    assert "### Biome-grouped ray denominators" in report
