"""Build a provenance-bound Item 7 provider coverage catalog."""

from __future__ import annotations

from .item7_provider_evidence import build_component, load_evidence
from .item7_provider_models import (
    CatalogInputs,
    ProviderCatalog,
    ProviderCatalogError,
    ProviderLabel,
    ProviderRole,
)
from .item7_provider_requirements import REQUIREMENTS


def build_provider_catalog(inputs: CatalogInputs) -> ProviderCatalog:
    """Build every Item 7 label from exact retained evidence and JAR contents."""
    evidence = load_evidence(inputs)
    labels = {
        requirement.label: ProviderLabel(
            role=requirement.role,
            components=tuple(
                build_component(component, evidence) for component in requirement.components
            ),
        )
        for requirement in REQUIREMENTS
    }
    return ProviderCatalog(schema_version="item7-provider-catalog-v1", labels=labels)


__all__ = (
    "CatalogInputs",
    "ProviderCatalogError",
    "ProviderRole",
    "build_provider_catalog",
)
