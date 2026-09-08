from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pytest
from pydantic import ValidationError

from mcpack_evidence import item7_runtime as runtime
from mcpack_evidence.item7_selections import ITEM10_SELECTIONS
from tests.item7.runtime_support import runtime_request


def test_declared_control_manifest_is_exact_baseline_minus_sparse() -> None:
    root = Path(__file__).parents[2]
    baseline = (
        (root / "evidence/item-3/runtime/retained-server-candidates.txt").read_text().splitlines()
    )
    control = root / "evidence/item-10/control-server-candidates.txt"
    assert control.read_text().splitlines() == [
        name for name in baseline if name != runtime.SPARSE_FILENAME
    ]
    assert len(control.read_text().splitlines()) == 135
    assert (
        runtime.sha256_file(control)
        == "a598513faef1248fd4a41da9137c1c721f9d34d307d12166141010bf815a20b4"
    )


def test_control_omits_only_sparse_and_preserves_source_and_configuration(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    diagnostic = runtime_request(tmp_path, monkeypatch)
    baseline = runtime.WorldgenRequest.model_validate(
        {
            **{name: getattr(diagnostic, name) for name in runtime.WorldgenRequest.model_fields},
            "mode": "item10",
            "selections": ITEM10_SELECTIONS,
        }
    )
    artifacts = tmp_path / "artifacts"
    names = sorted(baseline.retained_manifest.read_text().splitlines())
    rows = [(name, runtime.sha256_file(artifacts / name)) for name in names]
    expected = hashlib.sha256(json.dumps(rows, separators=(",", ":")).encode()).hexdigest()
    sparse_hash = runtime.sha256_file(artifacts / runtime.SPARSE_FILENAME)
    monkeypatch.setattr(runtime, "RETAINED_RUNTIME_SHA256", expected)
    monkeypatch.setattr(runtime, "SPARSE_SHA256", sparse_hash)
    baseline_receipt = runtime.prepare_worldgen(baseline)
    control = baseline.model_copy(
        update={
            "target": tmp_path / "control",
            "omit_sparse_structures": True,
        }
    )
    control_receipt = runtime.prepare_worldgen(control)
    baseline_mods = {
        path.name: runtime.sha256_file(path) for path in (baseline.target / "mods").iterdir()
    }
    control_mods = {
        path.name: runtime.sha256_file(path) for path in (control.target / "mods").iterdir()
    }
    assert control_mods == {
        name: digest for name, digest in baseline_mods.items() if name != runtime.SPARSE_FILENAME
    }
    assert runtime.sha256_file(artifacts / runtime.SPARSE_FILENAME) == sparse_hash
    assert runtime.sha256_file(baseline.target / "mods" / runtime.SPARSE_FILENAME) == sparse_hash
    for name in ("config", "defaultconfigs"):
        before = {
            p.relative_to(baseline.target / name): p.read_bytes()
            for p in (baseline.target / name).rglob("*")
            if p.is_file()
        }
        after = {
            p.relative_to(control.target / name): p.read_bytes()
            for p in (control.target / name).rglob("*")
            if p.is_file()
        }
        assert before == after
    assert (baseline.target / "server.properties").read_bytes() == (
        control.target / "server.properties"
    ).read_bytes()
    assert (
        baseline_receipt.retained_runtime_sha256
        == control_receipt.retained_runtime_sha256
        == expected
    )
    assert not baseline_receipt.sparse_structures_omitted
    assert control_receipt.sparse_structures_omitted
    assert control_receipt.instrumented_candidate_count == 136
    assert baseline_receipt.instrumented_candidate_count == 137
    assert (
        baseline_receipt.instrumented_runtime_sha256 != control_receipt.instrumented_runtime_sha256
    )
    with pytest.raises(ValidationError, match="instrumented count disagrees"):
        _ = runtime.PreflightReceipt.model_validate(
            {
                **control_receipt.model_dump(),
                "sparse_structures_omitted": False,
            }
        )


def test_control_cannot_be_requested_for_item7(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    request = runtime_request(tmp_path, monkeypatch)
    with pytest.raises(ValidationError, match="restricted to the Item 10 control"):
        _ = runtime.WorldgenRequest.model_validate(
            {
                **{name: getattr(request, name) for name in runtime.WorldgenRequest.model_fields},
                "omit_sparse_structures": True,
            }
        )


def test_full_materialization_rejects_nonfrozen_runtime_before_omission(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    request = runtime_request(tmp_path, monkeypatch).model_copy(
        update={
            "mode": "item10",
            "selections": ITEM10_SELECTIONS,
            "omit_sparse_structures": True,
        }
    )
    with pytest.raises(runtime.Item7RuntimeError, match="frozen retained runtime identity differs"):
        _ = runtime.prepare_worldgen(request)
    assert (request.target / "mods" / runtime.SPARSE_FILENAME).is_file()
