"""Hash-bound provider observation coverage for Item 7."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Final

from pydantic import BaseModel, ValidationError

from mcpack_evidence.item6_json import StrictJsonError, parse_strict_json
from mcpack_evidence.item7_coverage_models import (
    ComponentCoverage,
    CoverageError,
    CoverageReport,
    CoverageStatus,
    DecodedInput,
    FirstCoordinate,
    InputIdentity,
    LabelCoverage,
    Observation,
    Observed,
    ProviderRoleValue,
    WorldManifest,
)
from mcpack_evidence.item7_nbt import ChunkRecord
from mcpack_evidence.item7_provider_models import ProviderCatalog, ProviderComponent, ProviderRole

_LABELS = (
    "Tectonic",
    "Terralith",
    "Biomes O' Plenty",
    "Regions Unexplored",
    "TerraBlender",
    "Lithostitched",
    "BetterEnd",
    "YUNG",
    "WDA",
    "IDAS",
    "Integrated structures",
    "Moog",
    "Explorify",
    "Explorations",
    "Repurposed Structures",
    "CTOV",
    "Towns & Towers",
)
_ROLE_VALUES: Final[dict[ProviderRole, ProviderRoleValue]] = {
    ProviderRole.DIRECT_STRUCTURE: "direct_structure",
    ProviderRole.TERRAIN_BIOME: "terrain_biome",
    ProviderRole.LIBRARY: "library",
}


def _resolve(root: Path, relative: Path) -> Path:
    if relative.is_absolute() or not relative.parts or ".." in relative.parts:
        detail = f"evidence path is not relative: {relative}"
        raise CoverageError(detail)
    path = root / relative
    try:
        _ = path.resolve().relative_to(root.resolve())
    except ValueError as error:
        detail = f"evidence path escapes root: {relative}"
        raise CoverageError(detail) from error
    if path.is_symlink() or not path.is_file():
        detail = f"evidence input is not a real file: {relative}"
        raise CoverageError(detail)
    return path


def _parse_model[Model: BaseModel](model: type[Model], path: Path) -> tuple[Model, str]:
    try:
        raw = path.read_bytes()
        document = parse_strict_json(raw)
        parsed = model.model_validate_json(json.dumps(document, separators=(",", ":")))
    except (OSError, StrictJsonError, ValidationError) as error:
        detail = f"invalid evidence JSON: {path}"
        raise CoverageError(detail) from error
    return parsed, hashlib.sha256(raw).hexdigest()


def _manifest_input(root: Path, relative: Path) -> DecodedInput:
    manifest_path = _resolve(root, relative)
    manifest, manifest_sha256 = _parse_model(WorldManifest, manifest_path)
    decoded_relative = relative.parent / Path(manifest.decoded.path)
    decoded_path = _resolve(root, decoded_relative)
    identity = InputIdentity(
        manifest_path=relative.as_posix(),
        manifest_sha256=manifest_sha256,
        decoded_path=decoded_relative.as_posix(),
        decoded_sha256=manifest.decoded.sha256,
        record_count=manifest.decoded.record_count,
    )
    return DecodedInput(decoded_path, decoded_relative.as_posix(), manifest.decoded, identity)


def _coordinate(record: ChunkRecord, display: str) -> FirstCoordinate:
    return FirstCoordinate(
        input_path=display,
        dimension=record.dimension,
        chunk_x=record.chunk_x,
        chunk_z=record.chunk_z,
    )


def _read_decoded(source: DecodedInput, observed: Observed) -> None:
    digest = hashlib.sha256()
    size = 0
    records = 0
    try:
        with source.path.open("rb") as stream:
            for number, line in enumerate(stream, start=1):
                digest.update(line)
                size += len(line)
                if not line.strip():
                    detail = f"blank decoded line {number}: {source.display}"
                    raise CoverageError(detail)
                document = parse_strict_json(line)
                normalized = json.dumps(document, separators=(",", ":"))
                record = ChunkRecord.model_validate_json(normalized)
                records += 1
                coordinate = _coordinate(record, source.display)
                for start in record.structure_starts:
                    observed.structure_counts[start.structure_id] = (
                        observed.structure_counts.get(start.structure_id, 0) + 1
                    )
                    _ = observed.structure_first.setdefault(start.structure_id, coordinate)
                for section in record.biome_sections:
                    for index in section.indices:
                        biome = section.palette[index]
                        observed.biome_counts[biome] = observed.biome_counts.get(biome, 0) + 1
                        _ = observed.biome_first.setdefault(biome, coordinate)
    except (OSError, StrictJsonError, ValidationError, IndexError) as error:
        detail = f"invalid decoded evidence: {source.display}"
        raise CoverageError(detail) from error
    if (digest.hexdigest(), size, records) != (
        source.seal.sha256,
        source.seal.size_bytes,
        source.seal.record_count,
    ):
        detail = f"decoded identity mismatch: {source.display}"
        raise CoverageError(detail)


def _observations(component: ProviderComponent, observed: Observed) -> tuple[Observation, ...]:
    rows = [
        Observation(
            identifier=identifier,
            kind="structure_start",
            count=observed.structure_counts[identifier],
            first_coordinate=observed.structure_first[identifier],
        )
        for identifier in component.structure_ids
        if identifier in observed.structure_counts
    ]
    observes_biomes = (
        component.role is ProviderRole.TERRAIN_BIOME
        and component.mod_id in component.data_namespaces
    )
    if observes_biomes:
        rows.extend(
            Observation(
                identifier=identifier,
                kind="biome_quart",
                count=count,
                first_coordinate=observed.biome_first[identifier],
            )
            for identifier, count in observed.biome_counts.items()
            if identifier.partition(":")[0] == component.mod_id
        )
    return tuple(sorted(rows, key=lambda row: (row.kind, row.identifier)))


def _coverage(component: ProviderComponent, observed: Observed) -> ComponentCoverage:
    observations = _observations(component, observed)
    requirement: str | None = None
    status = CoverageStatus.OBSERVED
    if not observations:
        status = CoverageStatus.UNOBSERVED
        registry_target = component.role is ProviderRole.LIBRARY or (
            component.role is ProviderRole.TERRAIN_BIOME
            and component.mod_id not in component.data_namespaces
        )
        if registry_target:
            status = CoverageStatus.REQUIRES_TARGET
            requirement = "catalog_registry_and_generated_consumer_output"
        direct_target = (
            component.role is ProviderRole.DIRECT_STRUCTURE and not component.structure_ids
        )
        if direct_target:
            status = CoverageStatus.REQUIRES_TARGET
            requirement = "catalog_and_targeted_generated_output"
    return ComponentCoverage(
        candidate_filename=component.candidate_filename,
        mod_id=component.mod_id,
        role=_ROLE_VALUES[component.role],
        sha256=component.sha256,
        packaged_structure_ids=component.structure_ids,
        observations=observations,
        status=status,
        target_requirement=requirement,
    )


def summarize_coverage(
    root: Path, catalog_path: Path, manifest_paths: tuple[Path, ...]
) -> CoverageReport:
    """Summarize provider observations from hash-bound decoded worlds."""
    if root.is_symlink() or not root.is_dir() or not manifest_paths:
        detail = "coverage root and at least one manifest are required"
        raise CoverageError(detail)
    catalog_file = _resolve(root, catalog_path)
    catalog, catalog_sha256 = _parse_model(ProviderCatalog, catalog_file)
    if tuple(catalog.labels) != _LABELS:
        detail = "provider catalog labels differ from Item 7 protocol"
        raise CoverageError(detail)
    component_files = tuple(
        component.candidate_filename
        for label in catalog.labels.values()
        for component in label.components
    )
    if len(component_files) != len(set(component_files)):
        detail = "duplicate provider component in catalog"
        raise CoverageError(detail)
    paths = tuple(sorted(set(manifest_paths), key=Path.as_posix))
    if len(paths) != len(manifest_paths):
        detail = "duplicate world manifest input"
        raise CoverageError(detail)
    sources = tuple(_manifest_input(root, path) for path in paths)
    observed = Observed({}, {}, {}, {})
    for source in sources:
        _read_decoded(source, observed)
    labels = tuple(
        LabelCoverage(
            label=label,
            role=_ROLE_VALUES[catalog.labels[label].role],
            components=tuple(
                _coverage(component, observed) for component in catalog.labels[label].components
            ),
        )
        for label in _LABELS
    )
    missing = tuple(
        f"{label.label}/{component.mod_id}"
        for label in labels
        for component in label.components
        if component.status is not CoverageStatus.OBSERVED
    )
    return CoverageReport(
        schema_version="item7-provider-observation-coverage-v1",
        provider_catalog_path=catalog_path.as_posix(),
        provider_catalog_sha256=catalog_sha256,
        inputs=tuple(source.identity for source in sources),
        labels=labels,
        missing=missing,
    )
