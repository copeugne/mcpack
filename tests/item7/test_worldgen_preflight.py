from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pytest
from pydantic import TypeAdapter

from mcpack_evidence import item7_runtime
from mcpack_evidence.item7_selections import PILOT_SELECTIONS, RUN_SELECTIONS
from tests.item7.runtime_support import (
    CHUNKY_FIXTURE,
    FROZEN,
    AcquisitionDocument,
    runtime_request,
)


def test_preflight_materializes_exact_frozen_runtime(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    request = runtime_request(tmp_path, monkeypatch)

    receipt = item7_runtime.prepare_worldgen(request)

    assert receipt.seed == "6671238423019257953"
    assert receipt.retained_candidate_count == 136
    assert receipt.instrumented_candidate_count == 137
    assert (
        receipt.config_audit_sha256
        == "181e0c299f44ded319d93c84f7b983738364b4090286251b00421fa041b989dd"
    )
    assert (
        receipt.seed_suite_sha256
        == "de5e5e89bd04b6f75dac4eab2e84524956f46faa91660b5315c8eade269d39ae"
    )
    assert receipt.chunky_sha256 == hashlib.sha256(CHUNKY_FIXTURE).hexdigest()
    assert not (request.target / "world").exists()
    assert not (request.target / "config/resourceful-config-web.json").exists()
    assert (request.target / "config/aether-common.toml").read_bytes() == (
        FROZEN / "config/aether-common.toml"
    ).read_bytes()
    assert "level-seed=6671238423019257953" in (request.target / "server.properties").read_text(
        encoding="utf-8"
    )


def test_preflight_rejects_existing_target_and_wrong_retained_count(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    existing = runtime_request(tmp_path / "existing", monkeypatch)
    _ = existing.target.mkdir()
    with pytest.raises(item7_runtime.Item7RuntimeError, match="target must be absent"):
        _ = item7_runtime.prepare_worldgen(existing)

    wrong_count = runtime_request(tmp_path / "wrong-count", monkeypatch)
    names = wrong_count.retained_manifest.read_text(encoding="utf-8").splitlines()
    _ = wrong_count.retained_manifest.write_text("\n".join(names[:-1]) + "\n", encoding="utf-8")
    with pytest.raises(item7_runtime.Item7RuntimeError, match="retained manifest identity differs"):
        _ = item7_runtime.prepare_worldgen(wrong_count)

    wrong_overlay = runtime_request(tmp_path / "wrong-overlay", monkeypatch)
    manifest = TypeAdapter(AcquisitionDocument).validate_json(
        wrong_overlay.artifact_manifest.read_bytes()
    )
    overlay = Path(manifest["artifacts"][-1]["local_path"])
    _ = overlay.write_bytes(b"tampered")
    manifest["artifacts"][-1]["identity"] = {
        "size_bytes": overlay.stat().st_size,
        "computed_sha256": item7_runtime.sha256_file(overlay),
    }
    _ = wrong_overlay.artifact_manifest.write_text(json.dumps(manifest), encoding="utf-8")
    with pytest.raises(item7_runtime.Item7RuntimeError, match="artifact identity mismatch"):
        _ = item7_runtime.prepare_worldgen(wrong_overlay)


def test_java_preflight_requires_exact_temurin_build(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    request = runtime_request(tmp_path, monkeypatch)
    java = request.java_home / "bin/java"
    _ = java.write_text("#!/bin/sh\necho 'Temurin-21.0.12.1+10-LTS' >&2\n", encoding="utf-8")

    with pytest.raises(item7_runtime.Item7RuntimeError, match="not pinned Temurin"):
        _ = item7_runtime.validate_java_runtime(request.java_home)

    _ = java.write_text("#!/bin/sh\necho 'Temurin-21.0.12.1+1' >&2\n", encoding="utf-8")

    with pytest.raises(item7_runtime.Item7RuntimeError, match="not pinned Temurin"):
        _ = item7_runtime.validate_java_runtime(request.java_home)


@pytest.mark.parametrize(
    ("field", "message"),
    [
        ("retained_manifest", "retained manifest identity differs"),
        ("frozen_manifest", "frozen manifest identity differs"),
        ("config_audit", "config audit identity differs"),
        ("seed_suite", "seed suite identity differs"),
    ],
)
def test_preflight_rejects_changed_frozen_document_identity(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, field: str, message: str
) -> None:
    request = runtime_request(tmp_path, monkeypatch)
    sources: dict[str, Path] = {
        "retained_manifest": request.retained_manifest,
        "frozen_manifest": request.frozen_manifest,
        "config_audit": request.config_audit,
        "seed_suite": request.seed_suite,
    }
    source = sources[field]
    path = tmp_path / f"changed-{source.name}"
    _ = path.write_bytes(source.read_bytes() + b"\n")
    request = request.model_copy(update={field: path})

    with pytest.raises(item7_runtime.Item7RuntimeError, match=message):
        _ = item7_runtime.prepare_worldgen(request)


def test_presets_bind_all_four_selection_counts_and_centers() -> None:
    assert tuple(row.expected_chunk_count for row in PILOT_SELECTIONS) == (81,) * 4
    assert tuple(row.expected_chunk_count for row in RUN_SELECTIONS) == (3969, 961, 961, 961)
    assert RUN_SELECTIONS[-1].center_x == 1536


def test_production_chunky_identity_remains_frozen() -> None:
    assert item7_runtime.CHUNKY_SIZE_BYTES == 340572
    assert (
        item7_runtime.CHUNKY_SHA256
        == "d72f235cf1f56f2c374f52c00bdda5034524b28142305a84cfc123a3f92ad274"
    )
