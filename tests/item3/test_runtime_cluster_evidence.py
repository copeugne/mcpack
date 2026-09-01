from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import cast

EVIDENCE = Path("evidence/item-3/runtime/runtime-cluster-evidence.json")


def test_runtime_cluster_evidence_has_repeatable_retained_boots() -> None:
    evidence = _dict(cast("object", json.loads(EVIDENCE.read_text(encoding="utf-8"))))
    runs = [_dict(value) for value in _list(evidence["runs"])]
    passed = {run["id"] for run in runs if run["result"] == "pass"}

    assert evidence["schema_version"] == "item3-runtime-cluster-evidence-v1"
    assert "retained-server-136-first-boot" in passed
    assert "retained-server-136-restart" in passed
    assert "seven-seas-isolated" in passed
    assert "adorabuild-isolated" in passed


def test_runtime_log_artifacts_and_candidate_manifest_match_hashes() -> None:
    evidence = _dict(cast("object", json.loads(EVIDENCE.read_text(encoding="utf-8"))))
    manifest = _dict(evidence["retained_candidate_manifest"])
    manifest_path = Path(_str(manifest["path"]))

    assert len(manifest_path.read_text(encoding="utf-8").splitlines()) == 136
    assert _sha256(manifest_path) == manifest["sha256"]
    for artifact_value in _list(evidence["log_artifacts"]):
        artifact = _dict(artifact_value)
        path = Path(_str(artifact["path"]))
        assert path.stat().st_size == artifact["size_bytes"]
        assert _sha256(path) == artifact["sha256"]


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _dict(value: object) -> dict[str, object]:
    assert isinstance(value, dict)
    return cast("dict[str, object]", value)


def _list(value: object) -> list[object]:
    assert isinstance(value, list)
    return cast("list[object]", value)


def _str(value: object) -> str:
    assert isinstance(value, str)
    return value
