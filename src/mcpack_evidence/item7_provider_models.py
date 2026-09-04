"""Public model boundaries for the Item 7 provider catalog."""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum, unique
from typing import TYPE_CHECKING, ClassVar, Literal, override

from pydantic import BaseModel, ConfigDict

if TYPE_CHECKING:
    from pathlib import Path


@unique
class ProviderRole(StrEnum):
    """The worldgen responsibility exercised by a retained component."""

    DIRECT_STRUCTURE = "direct_structure"
    TERRAIN_BIOME = "terrain_biome"
    LIBRARY = "library"


@dataclass(frozen=True, slots=True)
class ProviderCatalogError(Exception):
    """A provider cannot be bound to the required retained evidence."""

    detail: str

    @override
    def __str__(self) -> str:
        """Render the evidence-bound failure detail."""
        return self.detail


@dataclass(frozen=True, slots=True)
class CatalogInputs:
    """Paths that bind catalog generation to the exact Item 3 sources."""

    retained: Path
    acquisition: Path
    matrix: Path
    inspection: Path
    candidate_directory: Path

    @classmethod
    def from_repository(cls, root: Path) -> CatalogInputs:
        """Resolve the canonical Item 3 sources under one repository root."""
        return cls(
            retained=root / "evidence/item-3/runtime/retained-server-candidates.txt",
            acquisition=root / "evidence/item-3/artifact-acquisition-manifest.json",
            matrix=root / "evidence/item-3/final-compatibility-matrix.json",
            inspection=root / "evidence/item-3/jar-inspection.json",
            candidate_directory=root / "downloads/item3/candidates",
        )

    def with_matrix(self, matrix: Path) -> CatalogInputs:
        """Return equivalent inputs with a supplied matrix boundary."""
        return CatalogInputs(
            retained=self.retained,
            acquisition=self.acquisition,
            matrix=matrix,
            inspection=self.inspection,
            candidate_directory=self.candidate_directory,
        )


class ProviderComponent(BaseModel):
    """One retained artifact proven to provide an Item 7 component."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid", strict=True)

    candidate_filename: str
    mod_id: str
    role: ProviderRole
    sha256: str
    data_namespaces: tuple[str, ...]


class ProviderLabel(BaseModel):
    """All retained components that satisfy one Item 7 label."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid", strict=True)

    role: ProviderRole
    components: tuple[ProviderComponent, ...]


class ProviderCatalog(BaseModel):
    """Deterministic ownership catalog for all Item 7 provider labels."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid", strict=True)

    schema_version: Literal["item7-provider-catalog-v1"]
    labels: dict[str, ProviderLabel]
