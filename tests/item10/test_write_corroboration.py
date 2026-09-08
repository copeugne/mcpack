"""Regression checks for retained coordinate inspections."""

import runpy
import sys
from pathlib import Path
from typing import cast

import pytest
from pydantic import JsonValue

from mcpack_evidence import item7_nbt

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "evidence/item-10/scarecrow-probe-r3/inspect-writes.py"
WORLD = ROOT / "evidence/raw/item10/probe-pair-r3-custody/world-scarecrow-probe-r3/world"


@pytest.mark.parametrize("mode", ["scarecrow", "bop", "monster"])
@pytest.mark.parametrize("defect", ["trace", "manifest", "region", "block"])
def test_corroboration_rejects_invalid_evidence(
    defect: str, mode: str, monkeypatch: pytest.MonkeyPatch
) -> None:
    diagnostic = "monster-box-pilot-r1" if mode == "monster" else "bop-fixture-r1"
    world = (
        WORLD
        if mode == "scarecrow"
        else ROOT / "evidence/raw/item10" / (diagnostic + "-custody") / "restored-world/world"
    )
    if not world.is_dir():
        pytest.skip(
            "Restore the published diagnostic world before running retained-world regressions"
        )
    monkeypatch.chdir(ROOT)
    monkeypatch.setattr(
        sys, "argv", [str(SCRIPT), *([] if mode == "scarecrow" else ["--" + mode + "-r1"])]
    )
    read_bytes = Path.read_bytes

    def changed_bytes(path: Path) -> bytes:
        data = read_bytes(path)
        if (
            (defect == "trace" and path.name == "trace.jsonl")
            or (defect == "manifest" and path.name == "world-backup.json")
            or (defect == "region" and path.suffix == ".mca")
        ):
            return data + b" "
        return data

    monkeypatch.setattr(Path, "read_bytes", changed_bytes)
    decode = item7_nbt.decode_compound_nbt

    def changed_blocks(payload: bytes) -> dict[str, JsonValue]:
        data = decode(payload)
        for section in cast("list[dict[str, JsonValue]]", data["sections"]):
            states = cast("dict[str, JsonValue]", section.get("block_states", {}))
            for state in cast("list[dict[str, JsonValue]]", states.get("palette", [])):
                state["Name"] = "test:incorrect_block"
        return data

    if defect == "block":
        monkeypatch.setattr(item7_nbt, "decode_compound_nbt", changed_blocks)
    with pytest.raises(ValueError, match=r"differs|30 recorded block IDs|BOP last recorded"):
        _ = runpy.run_path(str(SCRIPT))
