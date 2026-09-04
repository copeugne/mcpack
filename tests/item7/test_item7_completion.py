# pyright: standard
from __future__ import annotations

import hashlib
import json
from typing import TYPE_CHECKING

import pytest

from mcpack_evidence.item7_completion_io import CompletionError
from mcpack_evidence.item7_completion_provider_visual import (
    validate_provider_disposition,
    validate_visual_evidence,
)
from mcpack_evidence.item7_completion_publication import validate_publication

if TYPE_CHECKING:
    from pathlib import Path

    from pydantic import JsonValue


def _sha() -> str:
    return "a" * 64


def test_provider_adapter_requires_exact_catalog_accounting(tmp_path: Path) -> None:
    catalog = {
        "schema_version": "item7-provider-catalog-v2",
        "labels": {
            "Provider": {
                "role": "direct_structure",
                "components": [
                    {
                        "candidate_filename": "provider.jar",
                        "mod_id": "provider",
                        "role": "direct_structure",
                        "sha256": _sha(),
                        "data_namespaces": [],
                        "structure_ids": [],
                    }
                ],
            }
        },
    }
    catalog_path = tmp_path / "catalog.json"
    catalog_path.write_text(json.dumps(catalog), encoding="utf-8")
    disposition = {
        "schema_version": "item7-provider-disposition-v1",
        "catalog_path": "evidence/item-7/provider-catalog.json",
        "catalog_sha256": hashlib.sha256(catalog_path.read_bytes()).hexdigest(),
        "coverage_path": "run-a/provider-coverage.json",
        "coverage_sha256": _sha(),
        "inputs": [],
        "labels": [
            {
                "label": "Provider",
                "components": [
                    {
                        "candidate_filename": "provider.jar",
                        "mod_id": "provider",
                        "role": "direct_structure",
                        "sha256": _sha(),
                        "disposition": "direct_observed",
                        "direct_observations": [{"source": "synthetic"}],
                        "targeted_starts": [],
                        "limitation": "Synthetic direct observation.",
                        "downstream_action": "none",
                    }
                ],
            }
        ],
        "totals": {
            "direct_observed": 1,
            "targeted_observed": 0,
            "observed_generation_failure": 0,
            "indirect_observed": 0,
            "not_observed_with_limit": 0,
            "total_components": 1,
        },
    }
    disposition_path = tmp_path / "provider-disposition.json"
    disposition_path.write_text(json.dumps(disposition), encoding="utf-8")

    summary = validate_provider_disposition(catalog_path, disposition_path, expected_count=1)

    assert summary.total_components == 1
    component = disposition["labels"][0]["components"][0]
    component["disposition"] = "indirect_observed"
    disposition["totals"]["direct_observed"] = 0
    disposition["totals"]["indirect_observed"] = 1
    disposition_path.write_text(json.dumps(disposition), encoding="utf-8")
    with pytest.raises(CompletionError, match="provider disposition evidence shape"):
        validate_provider_disposition(catalog_path, disposition_path, expected_count=1)

    component["disposition"] = "direct_observed"
    disposition["totals"]["direct_observed"] = 1
    disposition["totals"]["indirect_observed"] = 0
    disposition["labels"][0]["components"].append(disposition["labels"][0]["components"][0])
    disposition_path.write_text(json.dumps(disposition), encoding="utf-8")
    with pytest.raises(CompletionError, match="provider component accounting"):
        validate_provider_disposition(catalog_path, disposition_path, expected_count=1)

    duplicate_key = json.dumps(disposition).replace(
        '"schema_version":', '"schema_version":"duplicate","schema_version":', 1
    )
    disposition_path.write_text(duplicate_key, encoding="utf-8")
    with pytest.raises(CompletionError, match="invalid strict JSON"):
        validate_provider_disposition(catalog_path, disposition_path, expected_count=1)


def test_visual_adapter_binds_hashes_commits_and_all_capture_rows(tmp_path: Path) -> None:
    captures = tmp_path / "captures"
    captures.mkdir()
    capture = captures / "one.png"
    capture.write_bytes(
        b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR"
        + (1440).to_bytes(4, "big")
        + (1200).to_bytes(4, "big")
    )
    capture_sha = hashlib.sha256(capture.read_bytes()).hexdigest()
    manifest = captures / "capture-manifest.tsv"
    manifest.write_text(f"one.png\thttp://127.0.0.1/one.svg\t{capture_sha}\t24\n", encoding="utf-8")
    manifest_sha = hashlib.sha256(manifest.read_bytes()).hexdigest()
    reviews: list[Path] = []
    for lane in ("capture-and-source-integrity", "visual-fidelity"):
        path = tmp_path / f"{lane}.json"
        path.write_text(
            json.dumps(
                {
                    "schema_version": "item7-visual-review-v1",
                    "lane": lane,
                    "verdict": "PASS",
                    "confidence": "HIGH",
                    "renderer_commit": "b" * 40,
                    "capture_tool_commit": "c" * 40,
                    "capture_manifest": {
                        "archive_path": "visual-qa/captures/capture-manifest.tsv",
                        "sha256": manifest_sha,
                        "size_bytes": manifest.stat().st_size,
                        "capture_count": 1,
                    },
                    "checked": {},
                    "findings": [],
                    "observations": [],
                }
            ),
            encoding="utf-8",
        )
        reviews.append(path)

    summary = validate_visual_evidence(manifest, tuple(reviews), expected_count=1)

    assert summary.capture_count == 1
    assert summary.review_count == 2
    capture.write_bytes(b"changed")
    with pytest.raises(CompletionError, match="capture identity"):
        validate_visual_evidence(manifest, tuple(reviews), expected_count=1)


def test_publication_binds_every_remote_asset_to_its_archive_manifest(tmp_path: Path) -> None:
    revision = "a" * 40
    release_url = "https://github.com/copeugne/mcpack/releases/tag/item-7-test"
    manifests: list[Path] = []
    assets: list[dict[str, JsonValue]] = []
    for index in range(4):
        name = f"asset-{index}.tar.gz"
        digest = str(index) * 64
        manifest = tmp_path / f"asset-{index}-manifest.json"
        manifest.write_text(
            json.dumps(
                {
                    "schema_version": "item7-raw-evidence-archive-v1",
                    "revision": revision,
                    "archive_name": name,
                    "archive_size_bytes": index + 1,
                    "archive_sha256": digest,
                    "file_count": 0,
                    "total_size_bytes": 0,
                    "files": [],
                }
            ),
            encoding="utf-8",
        )
        manifests.append(manifest)
        assets.append(
            {
                "name": name,
                "size_bytes": index + 1,
                "sha256": digest,
                "manifest": f"evidence/item-7/archive/asset-{index}-manifest.json",
                "restore_receipt": f"evidence/item-7/archive/asset-{index}-restore.json",
                "url": f"{release_url.replace('/tag/', '/download/')}/{name}",
            }
        )
    publication = tmp_path / "publication.json"
    payload = {
        "schema_version": "item7-raw-evidence-publication-v1",
        "repository": "copeugne/mcpack",
        "release_url": release_url,
        "tag": "item-7-test",
        "tag_object_sha": "b" * 40,
        "source_revision": revision,
        "published_at": "2026-09-04T00:00:00Z",
        "verified_at": "2026-09-04T00:01:00Z",
        "verification_tool": "tools/verify_item7_release.sh",
        "verification_command": "tools/verify_item7_release.sh test",
        "downloaded_bytes_verified": True,
        "assets": assets,
    }
    publication.write_text(json.dumps(payload), encoding="utf-8")

    _, observed_url = validate_publication(publication, tuple(manifests))

    assert observed_url == release_url
    assets[0]["sha256"] = "f" * 64
    publication.write_text(json.dumps(payload), encoding="utf-8")
    with pytest.raises(CompletionError, match="publication asset identities"):
        validate_publication(publication, tuple(manifests))
