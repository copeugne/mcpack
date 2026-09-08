"""The bounded r3 derivation rejects inputs from a different world."""

import gzip
import hashlib
import json
import runpy
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "evidence/item-10/scarecrow-probe-r3/compare-typed.py"


@pytest.mark.parametrize("defect", [None, "hash", "missing", "duplicate", "manifest"])
def test_comparison_binds_retained_regions(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, defect: str | None
) -> None:
    bundle = json.loads(gzip.decompress(SCRIPT.with_name("typed-comparison.json.gz").read_bytes()))
    source = tmp_path / "evidence/raw/item10/probe-pair-r3-typed"
    destination = tmp_path / "evidence/item-10/scarecrow-probe-r3"
    source.mkdir(parents=True)
    destination.mkdir(parents=True)
    files = []
    for member in ("probe", "control"):
        regions = {}
        for name, data in bundle["inputs"].items():
            if name.startswith(member + "-"):
                regions.update({row["path"]: row["sha256"] for row in data["anvil_inputs"]})
        payload = json.dumps(
            {"world_files": [{"path": path, "sha256": digest} for path, digest in regions.items()]}
        ).encode()
        relative = f"scarecrow-{member}-r3/world-backup.json"
        path = tmp_path / "evidence/raw/item10" / relative
        path.parent.mkdir(parents=True)
        path.write_bytes(payload)
        files.append(
            {
                "relative_path": relative,
                "size_bytes": len(payload),
                "sha256": hashlib.sha256(payload).hexdigest(),
            }
        )
        if defect == "manifest" and member == "probe":
            path.write_bytes(payload + b" ")
    (destination / "archive-manifest.json").write_text(json.dumps({"files": files}))
    rows = bundle["inputs"]["probe-overworld.json"]["anvil_inputs"]
    if defect == "hash":
        rows[0]["sha256"] = "0" * 64
    elif defect == "missing":
        rows.pop()
    elif defect == "duplicate":
        rows.append(rows[0])
    for name, data in bundle["inputs"].items():
        (source / name).write_text(json.dumps(data))
    monkeypatch.chdir(tmp_path)
    if defect:
        with pytest.raises(ValueError, match=r"manifest|retained archive"):
            runpy.run_path(str(SCRIPT))
        assert not (destination / "typed-comparison.json.gz").exists()
    else:
        runpy.run_path(str(SCRIPT))
        result = json.loads((destination / "typed-comparison.json").read_text())
        assert [row["mismatch_count"] for row in result["comparisons"]] == [3969, 960, 0, 671]
