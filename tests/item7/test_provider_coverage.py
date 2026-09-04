from __future__ import annotations

import json
from pathlib import Path

import pytest
from pydantic import TypeAdapter

from mcpack_evidence.item7_provider import (
    CatalogInputs,
    ProviderCatalogError,
    ProviderRole,
    build_provider_catalog,
)

ROOT = Path(__file__).parents[2]


def test_catalog_covers_every_item7_label_with_verified_retained_components() -> None:
    catalog = build_provider_catalog(CatalogInputs.from_repository(ROOT))

    assert set(catalog.labels) == {
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
    }
    assert all(
        component.sha256 for label in catalog.labels.values() for component in label.components
    )
    assert all(
        component.data_namespaces is not None
        for label in catalog.labels.values()
        for component in label.components
    )


def test_catalog_distinguishes_terrain_direct_and_library_providers() -> None:
    catalog = build_provider_catalog(CatalogInputs.from_repository(ROOT))

    assert catalog.labels["Tectonic"].role is ProviderRole.TERRAIN_BIOME
    assert catalog.labels["WDA"].role is ProviderRole.DIRECT_STRUCTURE
    assert catalog.labels["TerraBlender"].role is ProviderRole.LIBRARY
    assert catalog.labels["Lithostitched"].role is ProviderRole.LIBRARY
    betterend = catalog.labels["BetterEnd"].components[0]
    assert {"bclib", "betterend", "wover"} <= set(betterend.data_namespaces)
    assert catalog.labels["Tectonic"].components[0].data_namespaces == ()
    integrated = {
        component.mod_id: component
        for component in catalog.labels["Integrated structures"].components
    }
    assert integrated["integrated_api"].role is ProviderRole.LIBRARY
    assert "integrated_villages" in integrated["integrated_villages"].data_namespaces
    yung_mod_ids = {component.mod_id for component in catalog.labels["YUNG"].components}
    moog_mod_ids = {component.mod_id for component in catalog.labels["Moog"].components}
    assert yung_mod_ids == {
        "yungsapi",
        "bettercaves",
        "betterdeserttemples",
        "betterdungeons",
        "betterendisland",
        "betterjungletemples",
        "bettermineshafts",
        "betterfortresses",
        "betteroceanmonuments",
        "betterstrongholds",
        "betterwitchhuts",
        "yungsbridges",
        "yungscavebiomes",
        "yungsextras",
    }
    assert moog_mod_ids == {"mes", "mns", "mss", "mvs", "moogs_structures"}
    yung = {component.mod_id: component for component in catalog.labels["YUNG"].components}
    assert yung["yungsapi"].role is ProviderRole.LIBRARY
    assert yung["bettercaves"].role is ProviderRole.TERRAIN_BIOME


def test_catalog_reports_sorted_packaged_structure_registry_ids() -> None:
    catalog = build_provider_catalog(CatalogInputs.from_repository(ROOT))

    components = {
        component.mod_id: component
        for label in catalog.labels.values()
        for component in label.components
    }
    assert components["dungeons_arise"].structure_ids[:3] == (
        "dungeons_arise:abandoned_temple",
        "dungeons_arise:aviary",
        "dungeons_arise:bandit_towers",
    )
    assert components["integrated_villages"].structure_ids == (
        "integrated_villages:airship_village",
        "integrated_villages:cabin_village",
        "integrated_villages:clockwork_village",
        "integrated_villages:kutcha_village",
        "integrated_villages:marketstead_village",
        "integrated_villages:mediterranean_village",
        "integrated_villages:mossy_mounds",
        "integrated_villages:oasis_village",
        "integrated_villages:pirate_village",
        "integrated_villages:quark/minka_village",
        "integrated_villages:sunken_village",
        "integrated_villages:tavern_village",
    )
    assert "idas:animal_den/foxhound_den" in components["idas"].structure_ids
    assert components["moogs_structures"].role is ProviderRole.LIBRARY
    assert all(
        component.structure_ids == tuple(sorted(set(component.structure_ids)))
        for component in components.values()
    )
    assert all(
        component.structure_ids
        or component.role is not ProviderRole.DIRECT_STRUCTURE
        or component.mod_id in {"betterendisland", "yungsbridges", "yungsextras"}
        for component in components.values()
    )


def test_catalog_rejects_filename_only_provider_claim(tmp_path: Path) -> None:
    inputs = CatalogInputs.from_repository(ROOT)
    altered_matrix = tmp_path / "matrix.json"
    _ = altered_matrix.write_text(
        inputs.matrix.read_text(encoding="utf-8").replace(
            '"mod_id": "tectonic"', '"mod_id": "unproven_tectonic"', 1
        ),
        encoding="utf-8",
    )

    with pytest.raises(ProviderCatalogError, match="tectonic"):
        _ = build_provider_catalog(inputs.with_matrix(altered_matrix))


def test_catalog_rejects_unknown_item3_evidence_fields(tmp_path: Path) -> None:
    inputs = CatalogInputs.from_repository(ROOT)
    document = TypeAdapter(dict[str, object]).validate_python(
        json.loads(inputs.acquisition.read_text(encoding="utf-8"))
    )
    document["unexpected_acceptance_claim"] = True
    altered = tmp_path / "acquisition.json"
    _ = altered.write_text(json.dumps(document), encoding="utf-8")

    with pytest.raises(ValueError, match="unexpected_acceptance_claim"):
        _ = build_provider_catalog(
            CatalogInputs(
                retained=inputs.retained,
                acquisition=altered,
                matrix=inputs.matrix,
                inspection=inputs.inspection,
                candidate_directory=inputs.candidate_directory,
            )
        )
