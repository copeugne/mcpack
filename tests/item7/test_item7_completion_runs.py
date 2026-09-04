from __future__ import annotations

import hashlib
import json
from typing import TYPE_CHECKING

import pytest

import mcpack_evidence.item7_completion_runs as completion_runs
from mcpack_evidence.item7_analysis import analyze_jsonl
from mcpack_evidence.item7_analysis_models import AnalysisIdentity, WorldAnalysis
from mcpack_evidence.item7_completion_io import CompletionError, strict_model
from mcpack_evidence.item7_selection_extract import SelectionReceipt

if TYPE_CHECKING:
    from pathlib import Path

    from pydantic import BaseModel


def test_completion_rejects_analysis_rebuilt_differently_from_selected_jsonl(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    # Given
    raw = tmp_path / "raw"
    selected = raw / "run-a/ordinary/selections/overworld.jsonl"
    selected.parent.mkdir(parents=True)
    record = {
        "schema_version": "item7-anvil-chunk-v1",
        "dimension": "minecraft:overworld",
        "region": "region/r.0.0.mca",
        "slot": 0,
        "timestamp": 1,
        "chunk_x": 0,
        "chunk_z": 0,
        "data_version": 4189,
        "status": "minecraft:full",
        "full": True,
        "compression": "zlib",
        "external": False,
        "heightmaps": [
            {"name": "WORLD_SURFACE", "values": [64] * 256},
            {"name": "OCEAN_FLOOR", "values": [64] * 256},
        ],
        "biome_sections": [{"section_y": 4, "palette": ["minecraft:plains"], "indices": [0] * 64}],
        "structure_starts": [],
    }
    _ = selected.write_text(json.dumps(record, separators=(",", ":")) + "\n", encoding="utf-8")
    selected_sha256 = hashlib.sha256(selected.read_bytes()).hexdigest()
    expected = analyze_jsonl(
        selected,
        AnalysisIdentity("run-a", "ordinary", "overworld", "minecraft:overworld"),
        selected_sha256,
    )
    stale = expected.model_copy(
        update={"denominators": expected.denominators.model_copy(update={"chunk_count": 2})}
    )
    analysis_path = raw / "run-a/ordinary/analysis/overworld.json"
    analysis_path.parent.mkdir()
    _ = analysis_path.write_text(stale.model_dump_json() + "\n", encoding="utf-8")
    receipt = SelectionReceipt.model_validate(
        {
            "schema_version": "item7-selection-extract-receipt-v1",
            "protocol": {
                "path": "protocol.json",
                "size_bytes": 1,
                "sha256": "a" * 64,
                "record_count": 1,
            },
            "world_manifest": {
                "path": "world-manifest.json",
                "size_bytes": 1,
                "sha256": "b" * 64,
                "record_count": 1,
            },
            "aggregate": {
                "path": "chunks.jsonl",
                "size_bytes": 1,
                "sha256": "c" * 64,
                "record_count": 1,
            },
            "selection": {
                "label": "overworld",
                "dimension": "minecraft:overworld",
                "center_block_x": 0,
                "center_block_z": 0,
                "radius_chunks": 31,
                "expected_chunk_count": 3969,
                "observed_chunk_count": 3969,
            },
            "selected": {
                "path": "overworld.jsonl",
                "size_bytes": selected.stat().st_size,
                "sha256": selected_sha256,
                "record_count": 3969,
            },
        },
        strict=True,
    )
    for run_id in ("run-a", "run-b"):
        root = raw / f"{run_id}/ordinary"
        for relative in (
            "run-receipt.json",
            "world-manifest.json",
            "selections/overworld.jsonl.receipt.json",
        ):
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            _ = path.write_text("{}\n", encoding="utf-8")
        if run_id == "run-b":
            output = root / "selections/overworld.jsonl"
            _ = output.write_text(selected.read_text(encoding="utf-8"), encoding="utf-8")

    def fake_strict_model(path: Path, model: type[BaseModel]) -> BaseModel:
        if model is WorldAnalysis:
            return strict_model(path, WorldAnalysis)
        return receipt

    def skip_validation(
        *values: BaseModel | Path | SelectionReceipt | str | tuple[str, str, int, int, int, int],
    ) -> None:
        _ = values

    monkeypatch.setattr(completion_runs, "_ROLES", (("ordinary", "42"),))
    monkeypatch.setattr(
        completion_runs,
        "_SELECTIONS",
        (("overworld", "minecraft:overworld", 0, 0, 31, 3969),),
    )
    monkeypatch.setattr(completion_runs, "_RUN_ARTIFACT_COUNT", 9)
    monkeypatch.setattr(completion_runs, "_ANALYSIS_COUNT", 1)
    monkeypatch.setattr(completion_runs, "strict_model", fake_strict_model)
    monkeypatch.setattr(completion_runs, "_validate_run", skip_validation)
    monkeypatch.setattr(completion_runs, "_validate_manifest", skip_validation)
    monkeypatch.setattr(completion_runs, "_validate_selection", skip_validation)

    # When / Then
    with pytest.raises(CompletionError, match="analysis identity or anomaly accounting"):
        _ = completion_runs.validate_runs(raw, "a" * 64)
