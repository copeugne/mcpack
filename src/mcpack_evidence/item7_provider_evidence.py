"""Item 3 evidence parsing and exact JAR verification for Item 7."""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, ClassVar, Final
from zipfile import BadZipFile, ZipFile

from pydantic import BaseModel, ConfigDict

from .item7_provider_models import (
    CatalogInputs,
    ProviderCatalogError,
    ProviderComponent,
)

if TYPE_CHECKING:
    from .item7_provider_requirements import RequiredComponent


_MIN_DATA_PATH_SEPARATORS: Final = 2


class _AcquisitionIdentity(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="ignore", strict=True)

    computed_sha256: str


class _AcquisitionArtifact(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="ignore", strict=True)

    candidate_filename: str
    identity: _AcquisitionIdentity


class _AcquisitionManifest(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="ignore", strict=True)

    schema_version: str
    artifacts: tuple[_AcquisitionArtifact, ...]


class _MatrixArtifact(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="ignore", strict=True)

    exact_filename: str


class _ProvidedMod(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="ignore", strict=True)

    mod_id: str


class _MatrixRow(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="ignore", strict=True)

    candidate_filename: str
    artifact: _MatrixArtifact
    final_disposition: str
    provided_mods: tuple[_ProvidedMod, ...]


class _FinalMatrix(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="ignore", strict=True)

    schema_version: str
    rows: tuple[_MatrixRow, ...]


class _InspectionMod(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="ignore", strict=True)

    mod_id: str


class _InspectionRow(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="ignore", strict=True)

    candidate_filename: str
    expected_sha256: str
    computed_sha256: str
    inspection_status: str
    mods: tuple[_InspectionMod, ...]


class _JarInspection(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="ignore", strict=True)

    schema_version: str
    candidates: tuple[_InspectionRow, ...]


@dataclass(frozen=True, slots=True)
class EvidenceIndexes:
    """Indexes parsed from the exact retained Item 3 evidence boundary."""

    retained: frozenset[str]
    acquisition: dict[str, _AcquisitionArtifact]
    matrix: dict[str, _MatrixRow]
    inspection: dict[str, _InspectionRow]
    candidate_directory: Path


def load_evidence(inputs: CatalogInputs) -> EvidenceIndexes:
    """Parse the Item 3 boundary into component lookup indexes."""
    acquisition = _AcquisitionManifest.model_validate_json(inputs.acquisition.read_bytes())
    matrix = _FinalMatrix.model_validate_json(inputs.matrix.read_bytes())
    inspection = _JarInspection.model_validate_json(inputs.inspection.read_bytes())
    _check_schema_versions(acquisition, matrix, inspection)
    return EvidenceIndexes(
        retained=frozenset(
            line for line in inputs.retained.read_text(encoding="utf-8").splitlines() if line
        ),
        acquisition={row.candidate_filename: row for row in acquisition.artifacts},
        matrix={row.candidate_filename: row for row in matrix.rows},
        inspection={row.candidate_filename: row for row in inspection.candidates},
        candidate_directory=inputs.candidate_directory,
    )


def build_component(component: RequiredComponent, evidence: EvidenceIndexes) -> ProviderComponent:
    """Verify one component against manifests, metadata, and exact JAR bytes."""
    filename = component.candidate_filename
    if Path(filename).name != filename or filename not in evidence.retained:
        detail = f"required retained provider missing: {filename}"
        raise ProviderCatalogError(detail)
    acquisition = evidence.acquisition.get(filename)
    matrix = evidence.matrix.get(filename)
    inspection = evidence.inspection.get(filename)
    if acquisition is None or matrix is None or inspection is None:
        detail = f"missing Item 3 provenance for {filename}"
        raise ProviderCatalogError(detail)
    if matrix.artifact.exact_filename != filename or matrix.final_disposition != "retained_server":
        detail = f"final matrix does not retain exact provider {filename}"
        raise ProviderCatalogError(detail)
    if component.mod_id not in {entry.mod_id for entry in matrix.provided_mods}:
        detail = f"matrix metadata does not prove {component.mod_id} in {filename}"
        raise ProviderCatalogError(detail)
    if component.mod_id not in {entry.mod_id for entry in inspection.mods}:
        detail = f"jar metadata does not prove {component.mod_id} in {filename}"
        raise ProviderCatalogError(detail)
    sha256 = acquisition.identity.computed_sha256
    if inspection.inspection_status != "pass" or (
        sha256 != inspection.expected_sha256 or sha256 != inspection.computed_sha256
    ):
        detail = f"jar inspection identity failed for {filename}"
        raise ProviderCatalogError(detail)
    jar = evidence.candidate_directory / filename
    if hashlib.sha256(jar.read_bytes()).hexdigest() != sha256:
        detail = f"candidate jar hash mismatch for {filename}"
        raise ProviderCatalogError(detail)
    return ProviderComponent(
        candidate_filename=filename,
        mod_id=component.mod_id,
        role=component.role,
        sha256=sha256,
        data_namespaces=_data_namespaces(jar),
    )


def _check_schema_versions(
    acquisition: _AcquisitionManifest, matrix: _FinalMatrix, inspection: _JarInspection
) -> None:
    if acquisition.schema_version != "item3-artifact-acquisition-v1":
        detail = "unsupported acquisition schema"
        raise ProviderCatalogError(detail)
    if matrix.schema_version != "item3-final-compatibility-matrix-v1":
        detail = "unsupported final matrix schema"
        raise ProviderCatalogError(detail)
    if inspection.schema_version != "item3-jar-inspection-v1":
        detail = "unsupported jar inspection schema"
        raise ProviderCatalogError(detail)


def _data_namespaces(jar: Path) -> tuple[str, ...]:
    try:
        with ZipFile(jar) as archive:
            return tuple(
                sorted(
                    {
                        entry.split("/")[1]
                        for entry in archive.namelist()
                        if entry.startswith("data/")
                        and entry.count("/") >= _MIN_DATA_PATH_SEPARATORS
                    }
                )
            )
    except (BadZipFile, FileNotFoundError) as error:
        detail = f"candidate jar is unreadable: {jar.name}"
        raise ProviderCatalogError(detail) from error
