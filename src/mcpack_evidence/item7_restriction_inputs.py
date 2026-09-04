"""Frozen archive inputs for the Item 7 packaged restriction audit."""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from typing import TYPE_CHECKING

from .item7_provider_models import ProviderCatalog

if TYPE_CHECKING:
    from pathlib import Path

MINECRAFT_SHA256 = "e3bc55693e93cda0188f2e60aea28113fc647c5e85a15fa3d1b347349231b4bb"
NEOFORGE_SHA256 = "63ba902edcae4476d49ffc28b18d566b0fcc5bf12edebcce1a2033f254f28155"
MINECRAFT_NESTED = "META-INF/versions/1.21.1/server-1.21.1.jar"


class RestrictionInputError(ValueError):
    """The frozen restriction input identities are inconsistent."""


@dataclass(frozen=True, slots=True)
class ArchiveInput:
    """One exact archive supplied to the deterministic audit."""

    name: str
    path: Path
    sha256: str
    nested_archive: str | None = None


def repository_inputs(root: Path, catalog_path: Path) -> tuple[ArchiveInput, ...]:
    """Resolve the frozen vanilla, NeoForge, and provider archive identities."""
    catalog = ProviderCatalog.model_validate_json(catalog_path.read_bytes(), strict=True)
    identities: dict[str, str] = {}
    for label in catalog.labels.values():
        for component in label.components:
            prior = identities.setdefault(component.candidate_filename, component.sha256)
            if prior != component.sha256:
                message = "provider archive has conflicting hashes"
                raise RestrictionInputError(message)
    providers = tuple(
        ArchiveInput(name, root / "downloads/item3/candidates" / name, digest)
        for name, digest in sorted(identities.items())
    )
    return (
        ArchiveInput(
            "minecraft-server-1.21.1.jar",
            root / "downloads/item2/minecraft/server.jar",
            MINECRAFT_SHA256,
            MINECRAFT_NESTED,
        ),
        ArchiveInput(
            "neoforge-21.1.249-universal.jar",
            root
            / "instances/pristine-baseline-v0/libraries/net/neoforged/neoforge/21.1.249"
            / "neoforge-21.1.249-universal.jar",
            NEOFORGE_SHA256,
        ),
        *providers,
    )


def sha256_path(path: Path) -> str:
    """Return the SHA-256 of one evidence input."""
    return hashlib.sha256(path.read_bytes()).hexdigest()
