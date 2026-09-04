from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path

import pytest
from pydantic import JsonValue
from tools.summarize_item7_coverage import run

from mcpack_evidence.item7_coverage import summarize_coverage
from mcpack_evidence.item7_coverage_models import CoverageError, CoverageReport
from mcpack_evidence.item7_provider_models import ProviderCatalog

ROOT = Path(__file__).parents[2]


def _chunk() -> dict[str, JsonValue]:
    biome_section: dict[str, JsonValue] = {
        "section_y": 4,
        "palette": list[JsonValue](["terralith:alpine_grove"]),
        "indices": list[JsonValue]([0] * 64),
    }
    structure_start: dict[str, JsonValue] = {
        "structure_id": "dungeons_arise:abandoned_temple",
        "start_id": "dungeons_arise:abandoned_temple",
        "boxes": list[JsonValue](),
    }
    chunk: dict[str, JsonValue] = {
        "schema_version": "item7-anvil-chunk-v1",
        "dimension": "minecraft:overworld",
        "region": "world/region/r.0.0.mca",
        "slot": 0,
        "timestamp": 1,
        "chunk_x": 2,
        "chunk_z": 3,
        "data_version": 3955,
        "status": "minecraft:full",
        "full": True,
        "compression": "zlib",
        "external": False,
        "heightmaps": list[JsonValue](),
        "biome_sections": list[JsonValue]([biome_section]),
        "structure_starts": list[JsonValue]([structure_start]),
    }
    return chunk


def _inputs(tmp_path: Path) -> tuple[Path, Path]:
    catalog = tmp_path / "provider-catalog.json"
    _ = shutil.copyfile(ROOT / "evidence/item-7/provider-catalog.json", catalog)
    run = tmp_path / "run-a/ordinary"
    run.mkdir(parents=True)
    decoded = run / "chunks.jsonl"
    payload = json.dumps(_chunk(), separators=(",", ":")) + "\n"
    _ = decoded.write_text(payload, encoding="utf-8")
    digest = hashlib.sha256(payload.encode()).hexdigest()
    manifest = run / "world-manifest.json"
    _ = manifest.write_text(
        json.dumps(
            {
                "schema_version": "item7-world-manifest-v1",
                "decoded": {
                    "path": decoded.name,
                    "size_bytes": len(payload.encode()),
                    "sha256": digest,
                    "record_count": 1,
                },
            }
        ),
        encoding="utf-8",
    )
    return catalog.relative_to(tmp_path), manifest.relative_to(tmp_path)


def test_summary_maps_exact_structure_ids_and_biome_namespaces(tmp_path: Path) -> None:
    # Given: one hash-bound chunk with a Terralith biome and one WDA structure start.
    catalog, manifest = _inputs(tmp_path)

    # When: provider observation coverage is summarized.
    report = summarize_coverage(tmp_path, catalog, (manifest,))

    # Then: exact producers are observed while indirect providers retain uncertainty.
    by_label = {row.label: row for row in report.labels}
    terralith = by_label["Terralith"].components[0]
    assert terralith.status == "observed"
    assert terralith.observations[0].identifier == "terralith:alpine_grove"
    assert terralith.observations[0].count == 64
    assert terralith.observations[0].first_coordinate.chunk_x == 2
    wda = {row.mod_id: row for row in by_label["WDA"].components}["dungeons_arise"]
    assert wda.status == "observed"
    assert wda.observations[0].identifier == "dungeons_arise:abandoned_temple"
    assert wda.observations[0].count == 1
    assert by_label["Tectonic"].components[0].status == "requires_targeted_observation"
    assert by_label["TerraBlender"].components[0].status == "requires_targeted_observation"
    assert by_label["Lithostitched"].components[0].status == "requires_targeted_observation"
    assert len(report.labels) == 17


def test_summary_rejects_decoded_content_that_does_not_match_manifest_hash(
    tmp_path: Path,
) -> None:
    # Given: a decoded input changed after its binding manifest was written.
    catalog, manifest = _inputs(tmp_path)
    decoded = tmp_path / manifest.parent / "chunks.jsonl"
    _ = decoded.write_text(
        decoded.read_text(encoding="utf-8").replace('"timestamp":1', '"timestamp":2'),
        encoding="utf-8",
    )

    # When and Then: the summary fails closed on the identity mismatch.
    with pytest.raises(CoverageError, match="decoded identity mismatch"):
        _ = summarize_coverage(tmp_path, catalog, (manifest,))


def test_summary_rejects_absolute_evidence_paths(tmp_path: Path) -> None:
    # Given: otherwise valid evidence addressed by an absolute catalog path.
    catalog, manifest = _inputs(tmp_path)

    # When and Then: the relative-path boundary rejects it.
    with pytest.raises(CoverageError, match="not relative"):
        _ = summarize_coverage(tmp_path, tmp_path / catalog, (manifest,))


def test_summary_never_credits_an_unpublished_structure_id(tmp_path: Path) -> None:
    # Given: a generated start in the WDA namespace but absent from WDA's packaged IDs.
    catalog, manifest = _inputs(tmp_path)
    decoded = tmp_path / manifest.parent / "chunks.jsonl"
    original = decoded.read_text(encoding="utf-8")
    payload = original.replace("dungeons_arise:abandoned_temple", "dungeons_arise:not_packaged")
    _ = decoded.write_text(payload, encoding="utf-8")
    digest = hashlib.sha256(payload.encode()).hexdigest()
    manifest_path = tmp_path / manifest
    manifest_text = manifest_path.read_text(encoding="utf-8")
    manifest_text = manifest_text.replace(hashlib.sha256(original.encode()).hexdigest(), digest)
    manifest_text = manifest_text.replace(str(len(original.encode())), str(len(payload.encode())))
    _ = manifest_path.write_text(manifest_text, encoding="utf-8")

    # When: the exact-ID coverage summary is built.
    report = summarize_coverage(tmp_path, catalog, (manifest,))

    # Then: namespace similarity does not count as provider observation.
    wda = next(row for row in report.labels if row.label == "WDA")
    direct = next(row for row in wda.components if row.mod_id == "dungeons_arise")
    assert direct.status == "unobserved"
    assert direct.observations == ()


def test_summary_emits_every_catalog_component_once_with_stable_missing_order(
    tmp_path: Path,
) -> None:
    # Given: the complete frozen provider catalog and one bound observation input.
    catalog, manifest = _inputs(tmp_path)

    # When: coverage is summarized.
    report = summarize_coverage(tmp_path, catalog, (manifest,))

    # Then: component identity is unique and target-only evidence remains explicit.
    components = [component for label in report.labels for component in label.components]
    filenames = [component.candidate_filename for component in components]
    assert len(filenames) == len(set(filenames))
    better_end_island = next(row for row in components if row.mod_id == "betterendisland")
    assert better_end_island.status == "requires_targeted_observation"
    assert better_end_island.target_requirement == "catalog_and_targeted_generated_output"
    assert report.missing[0] == "Tectonic/tectonic"


def test_summary_rejects_a_component_repeated_across_catalog_labels(tmp_path: Path) -> None:
    # Given: a complete catalog that repeats one exact retained component under another label.
    catalog, manifest = _inputs(tmp_path)
    catalog_path = tmp_path / catalog
    document = ProviderCatalog.model_validate_json(catalog_path.read_bytes())
    labels = dict(document.labels)
    duplicate = labels["Terralith"].components[0]
    labels["Tectonic"] = labels["Tectonic"].model_copy(
        update={"components": (*labels["Tectonic"].components, duplicate)}
    )
    _ = catalog_path.write_text(
        document.model_copy(update={"labels": labels}).model_dump_json(), encoding="utf-8"
    )

    # When and Then: exact-once component accounting fails closed.
    with pytest.raises(CoverageError, match="duplicate provider component"):
        _ = summarize_coverage(tmp_path, catalog, (manifest,))


def test_cli_writes_strict_json_atomically_and_preserves_prior_output_on_failure(
    tmp_path: Path,
) -> None:
    # Given: valid relative inputs and a pre-existing output file.
    catalog, manifest = _inputs(tmp_path)
    output = Path("coverage.json")
    output_path = tmp_path / output
    _ = output_path.write_text("sentinel\n", encoding="utf-8")
    arguments = (
        "--root",
        tmp_path.as_posix(),
        "--catalog",
        catalog.as_posix(),
        manifest.as_posix(),
        "--output",
        output.as_posix(),
    )

    # When: the real CLI boundary writes the report.
    assert run(arguments) == 0

    # Then: strict output parses and a later failure cannot truncate it.
    report = CoverageReport.model_validate_json(output_path.read_bytes())
    decoded = tmp_path / manifest.parent / "chunks.jsonl"
    _ = decoded.write_text(decoded.read_text(encoding="utf-8") + "\n", encoding="utf-8")
    with pytest.raises(CoverageError):
        _ = run(arguments)
    assert CoverageReport.model_validate_json(output_path.read_bytes()) == report
