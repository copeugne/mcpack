"""Audit packaged biome restrictions for every Item 7 provider structure."""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from io import BytesIO
from typing import TYPE_CHECKING, cast
from zipfile import BadZipFile, ZipFile

from pydantic import ValidationError

from .item7_restriction_models import (
    RestrictionAudit,
    RestrictionCandidate,
    RestrictionSource,
)

if TYPE_CHECKING:
    from pathlib import Path

    from .item7_restriction_inputs import ArchiveInput


class RestrictionAuditError(ValueError):
    """The restriction evidence boundary is incomplete or inconsistent."""


@dataclass(frozen=True, slots=True)
class _Structure:
    source: str
    identifier: str
    biomes: object


def audit_restrictions(
    sources: tuple[ArchiveInput, ...], provider_catalog_sha256: str
) -> RestrictionAudit:
    """Inspect all packaged structures and resolve their biome tag references."""
    tags: dict[str, list[object]] = {}
    structures: list[_Structure] = []
    placements: dict[str, set[str]] = {}
    identities: list[RestrictionSource] = []
    for source in sources:
        archive = _open_verified(source)
        with archive:
            _collect(source.name, archive, tags, structures, placements)
        identities.append(
            RestrictionSource(
                name=source.name,
                sha256=source.sha256,
                nested_archive=source.nested_archive,
            )
        )
    candidates = tuple(
        sorted(
            filter(None, (_candidate(row, tags, placements) for row in structures)),
            key=lambda row: row.structure_id,
        )
    )
    return RestrictionAudit(
        schema_version="item7-biome-restriction-audit-v1",
        provider_catalog_sha256=provider_catalog_sha256,
        sources=tuple(identities),
        structure_count=len(structures),
        resolved_structure_count=len(structures) - len(candidates),
        candidate_count=len(candidates),
        active_candidate_count=sum(bool(row.placement_sets) for row in candidates),
        candidates=candidates,
        exit_gate="PASS",
        limitations=(
            "This audit proves packaged restriction resolution, not observed spawn frequency.",
            (
                "Empty unplaced compatibility structures remain recorded rather than "
                "treated as defects."
            ),
        ),
    )


def _open_verified(source: ArchiveInput) -> ZipFile:
    try:
        data = source.path.read_bytes()
    except OSError as error:
        message = f"archive is unreadable: {source.name}"
        raise RestrictionAuditError(message) from error
    if hashlib.sha256(data).hexdigest() != source.sha256:
        message = f"archive hash mismatch: {source.name}"
        raise RestrictionAuditError(message)
    try:
        outer = ZipFile(BytesIO(data))
        if source.nested_archive is None:
            return outer
        nested = outer.read(source.nested_archive)
        outer.close()
        return ZipFile(BytesIO(nested))
    except (BadZipFile, KeyError) as error:
        message = f"archive structure is invalid: {source.name}"
        raise RestrictionAuditError(message) from error


def _collect(
    source: str,
    archive: ZipFile,
    tags: dict[str, list[object]],
    structures: list[_Structure],
    placements: dict[str, set[str]],
) -> None:
    for name in sorted(archive.namelist()):
        identifier = _resource_id(name, ("worldgen", "structure"), 4)
        if identifier is not None:
            structures.append(
                _Structure(source, identifier, _document(archive, name).get("biomes"))
            )
            continue
        identifier = _resource_id(name, ("tags", "worldgen", "biome"), 5)
        if identifier is not None:
            values = _document(archive, name).get("values")
            if not isinstance(values, list):
                message = f"biome tag has no values list: {name}"
                raise RestrictionAuditError(message)
            tags.setdefault(identifier, []).extend(cast("list[object]", values))
            continue
        identifier = _resource_id(name, ("worldgen", "structure_set"), 4)
        if identifier is not None:
            rows = _document(archive, name).get("structures")
            if not isinstance(rows, list):
                message = f"structure set has no structures list: {name}"
                raise RestrictionAuditError(message)
            for value in cast("list[object]", rows):
                if isinstance(value, dict):
                    row = cast("dict[str, object]", value)
                    structure = row.get("structure")
                    if isinstance(structure, str):
                        placements.setdefault(structure, set()).add(identifier)


def _resource_id(name: str, marker: tuple[str, ...], marker_end: int) -> str | None:
    parts = name.split("/")
    if (
        len(parts) <= marker_end
        or parts[0] != "data"
        or tuple(parts[2:marker_end]) != marker
        or not name.endswith(".json")
    ):
        return None
    return f"{parts[1]}:{'/'.join(parts[marker_end:]).removesuffix('.json')}"


def _document(archive: ZipFile, name: str) -> dict[str, object]:
    raw = archive.read(name).decode("utf-8-sig")
    try:
        value = cast("object", json.loads(raw))
    except json.JSONDecodeError:
        value = cast(
            "object",
            json.loads(
                "\n".join(line for line in raw.splitlines() if not line.lstrip().startswith("//"))
            ),
        )
    if not isinstance(value, dict):
        message = f"packaged document is not an object: {name}"
        raise RestrictionAuditError(message)
    return cast("dict[str, object]", value)


def _candidate(
    structure: _Structure,
    tags: dict[str, list[object]],
    placements: dict[str, set[str]],
) -> RestrictionCandidate | None:
    reference = structure.biomes
    if not isinstance(reference, str):
        status = "invalid_reference"
        missing: tuple[str, ...] = ()
    elif not reference.startswith("#"):
        return None
    else:
        tag = reference[1:]
        resolved, missing = resolve_biome_tag(tag, tags)
        if resolved and not missing:
            return None
        status = "missing_tag" if missing else "empty_tag"
    return RestrictionCandidate(
        source_archive=structure.source,
        structure_id=structure.identifier,
        biome_reference=reference if isinstance(reference, str) else repr(reference),
        status=status,
        placement_sets=tuple(sorted(placements.get(structure.identifier, set()))),
        missing_tags=missing,
    )


def resolve_biome_tag(  # noqa: C901 - explicit required/optional tag and biome semantics.
    tag: str,
    tags: dict[str, list[object]],
    stack: tuple[str, ...] = (),
    *,
    registered_biomes: frozenset[str] | None = None,
) -> tuple[set[str], tuple[str, ...]]:
    """Expand packaged tags, optionally distinguishing absent registered biome IDs.

    The caller supplies already merged tag values. This does not resolve pack
    precedence or prove that a runtime tag loader accepted a partially invalid tag.
    Without a registry, retain the original Item 7 packaged-reference semantics.
    """
    if tag in stack:
        return set(), (tag,)
    values = tags.get(tag)
    if values is None:
        return set(), (tag,)
    resolved: set[str] = set()
    missing: set[str] = set()
    for raw in values:
        required = True
        value = raw
        if isinstance(raw, dict):
            row = cast("dict[str, object]", raw)
            required = row.get("required", True) is not False
            value = row.get("id")
        if not isinstance(value, str):
            message = f"invalid biome tag member: {tag}"
            raise RestrictionAuditError(message)
        if not value.startswith("#"):
            if registered_biomes is None or value in registered_biomes:
                resolved.add(value)
            elif required:
                missing.add(value)
            continue
        nested = value[1:]
        nested_values, nested_missing = resolve_biome_tag(
            nested, tags, (*stack, tag), registered_biomes=registered_biomes
        )
        if registered_biomes is None or not nested_missing:
            resolved.update(nested_values)
        if required:
            missing.update(nested_missing)
    return resolved, tuple(sorted(missing))


def validate_restriction_audit(path: Path, provider_catalog_sha256: str) -> RestrictionAudit:
    """Validate the committed audit and its exact provider-catalog identity."""
    try:
        report = RestrictionAudit.model_validate_json(path.read_bytes(), strict=True)
    except (OSError, ValidationError) as error:
        message = "biome restriction audit is invalid"
        raise RestrictionAuditError(message) from error
    if report.provider_catalog_sha256 != provider_catalog_sha256:
        message = "biome restriction provider catalog hash mismatch"
        raise RestrictionAuditError(message)
    if (
        report.structure_count != report.resolved_structure_count + report.candidate_count
        or report.candidate_count != len(report.candidates)
        or report.active_candidate_count
        != sum(bool(candidate.placement_sets) for candidate in report.candidates)
        or len({candidate.structure_id for candidate in report.candidates})
        != report.candidate_count
    ):
        message = "biome restriction audit accounting mismatch"
        raise RestrictionAuditError(message)
    return report
