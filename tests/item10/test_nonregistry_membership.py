"""Reuse accepted canonical membership without promoting attempts to locations."""

import pytest
from tools.analyze_structure_density import (
    attribute_nonregistry_attempt,
    nonregistry_attempt_outcome,
    nonregistry_membership,
)


def attempt(feature: str, *paths: str) -> list[dict[str, object]]:
    return [
        {"kind": "begin", "attempt": 1, "dimension": "minecraft:the_end", "origin": [0, 0, 0]},
        {"kind": "feature", "attempt": 1, "class": feature},
        *[{"kind": "template_begin", "path": path} for path in paths],
        {"kind": "end", "attempt": 1, "returned": False},
    ]


def test_building_design_uses_exact_packaged_path() -> None:
    result = attribute_nonregistry_attempt(
        attempt(
            "org.betterx.betterend.world.features.BuildingListFeature",
            "/data/betterend/structure/biome/lantern_woods/cabin.nbt",
        ),
        nonregistry_membership(),
    )
    assert result["family"] == "betterend:lantern_woods_cabin"
    assert result["reason"] == "ATTRIBUTED"  # Attribution does not override false placement.


def test_double_arch_is_not_an_extra_family() -> None:
    membership = nonregistry_membership()
    classes = membership["classes"]
    prefix = "com/yungnickyoung/minecraft/yungsextras/world/feature/swamp/"
    assert classes[prefix + "SwampArchFeature"] == "yungsextras:swamp_arch"
    assert classes[prefix + "SwampDoubleArchFeature"] == "yungsextras:swamp_arch"


def test_arena_templates_remain_one_family() -> None:
    membership = nonregistry_membership()
    paths = [
        path
        for path, family in membership["templates"].items()
        if family == "betterendisland:dragon_arena"
    ][:2]
    assert len(paths) == 2
    result = attribute_nonregistry_attempt(
        attempt(
            "com.yungnickyoung.minecraft.betterendisland.world.feature.BetterSpikeFeature", *paths
        ),
        membership,
    )
    assert result["family"] == "betterendisland:dragon_arena"
    assert result["templates"] == paths


def test_unknown_template_is_explicitly_unresolved() -> None:
    result = attribute_nonregistry_attempt(
        attempt("org.betterx.betterend.world.features.BuildingListFeature", "/unmapped/ruin.nbt"),
        nonregistry_membership(),
    )
    assert result["family"] is None
    assert result["reason"] == "UNMAPPED_TEMPLATE"


def test_early_building_failure_does_not_invent_a_design() -> None:
    result = attribute_nonregistry_attempt(
        attempt("org.betterx.betterend.world.features.BuildingListFeature"),
        nonregistry_membership(),
    )
    assert result["family"] is None
    assert result["reason"] == "NO_DESIGN_SELECTED"


def test_existing_ambient_dispositions_are_retained() -> None:
    membership = nonregistry_membership()
    ambient = [
        path for path, decision in membership["excluded"].items() if decision.startswith("AMBIENT")
    ]
    assert len(ambient) == 6
    for path in ambient:
        result = attribute_nonregistry_attempt(
            attempt("org.betterx.betterend.world.features.NBTFeature", path), membership
        )
        assert result["family"] is None
        assert result["reason"] == "AMBIENT_DECORATION_NOT_ADDITIONAL_FAMILY"


def test_disconnected_house_observation_reopens_inventory_boundary() -> None:
    with pytest.raises(ValueError, match="contradicts accepted"):
        _ = attribute_nonregistry_attempt(
            attempt(
                "org.betterx.betterend.world.features.BuildingListFeature",
                "/data/betterend/structure/biome/blossoming_spires/house.nbt",
            ),
            nonregistry_membership(),
        )


def test_conflicting_template_and_generator_rejected() -> None:
    with pytest.raises(ValueError, match="identities disagree"):
        _ = attribute_nonregistry_attempt(
            attempt(
                "org.betterx.betterend.world.features.CrashedShipFeature",
                "/data/betterend/structure/biome/lantern_woods/cabin.nbt",
            ),
            nonregistry_membership(),
        )


def test_urn_requires_cave_parent() -> None:
    rows = attempt("net.minecraft.world.level.levelgen.feature.RandomPatchFeature")
    result = attribute_nonregistry_attempt(rows, nonregistry_membership())
    assert result["reason"] == "UNRESOLVED_URN_PARENT"
    rows.insert(
        2, {"kind": "urn_parent", "attempt": 1, "placed_feature": "supplementaries:cave_urns"}
    )
    assert (
        attribute_nonregistry_attempt(rows, nonregistry_membership())["family"]
        == "supplementaries:cave_urn_cache"
    )


def write(position: list[int], state: str, returned: bool = True) -> dict[str, object]:
    return {
        "kind": "write",
        "attempt": 1,
        "position": position,
        "state": "Block{" + state + "}",
        "flags": 2,
        "returned": returned,
    }


def test_urn_outcome_preserves_multiple_blocks_as_one_attempt() -> None:
    rows = attempt("net.minecraft.world.level.levelgen.feature.RandomPatchFeature")
    rows[2:2] = [
        {"kind": "urn_parent", "placed_feature": "supplementaries:cave_urns"},
        write([1, 2, 3], "supplementaries:urn"),
        write([2, 2, 3], "supplementaries:urn"),
        write([3, 2, 3], "supplementaries:urn", returned=False),
    ]
    result = nonregistry_attempt_outcome(rows, nonregistry_membership())
    assert result["attempt"] == 1
    assert result["content_positions"] == [[1, 2, 3], [2, 2, 3]]
    assert result["refused_writes"] == 1
    assert result["outcome"] == "CONTENT_OBSERVED"


def test_template_eroded_to_air_does_not_retain_initial_content() -> None:
    rows = attempt("org.betterx.betterend.world.features.CrashedShipFeature")
    rows[2:2] = [
        {"kind": "template_begin", "path": "minecraft:end_city/ship", "position": [5, 8, 9]},
        write([5, 8, 9], "minecraft:purpur_block"),
        {"kind": "template_end", "returned": True},
        write([5, 8, 9], "minecraft:air"),
        write([5, 7, 9], "minecraft:end_stone"),
    ]
    result = nonregistry_attempt_outcome(rows, nonregistry_membership())
    assert result["anchor"] == [5, 8, 9]
    assert result["outcome"] == "NO_CONTENT_OBSERVED"
    assert result["content_positions"] == []
    assert result["last_successful_writes"] == [
        {"position": [5, 7, 9], "block_id": "minecraft:end_stone"},
        {"position": [5, 8, 9], "block_id": "minecraft:air"},
    ]


def test_exception_with_writes_remains_explicit_partial_evidence() -> None:
    rows = attempt("biomesoplenty.worldgen.feature.misc.MonolithFeature")
    rows.insert(2, write([1, 2, 3], "minecraft:obsidian"))
    rows[-1] = {"kind": "attempt_exception", "exception": "test.Failure"}
    result = nonregistry_attempt_outcome(rows, nonregistry_membership())
    assert result["outcome"] == "EXCEPTION_WITH_CONTENT"


def test_arena_component_keeps_central_location_and_non_worldgen_context() -> None:
    rows = attempt("com.yungnickyoung.minecraft.betterendisland.world.feature.BetterSpikeFeature")
    rows[0]["origin"] = [42, 80, 0]
    rows.insert(2, {"kind": "island_context", "worldgen_region": False})
    result = nonregistry_attempt_outcome(rows, nonregistry_membership())
    assert result["anchor"] == [0, 80, 0]
    assert result["origin"] == [42, 80, 0]
    assert result["route"] == "non_worldgen_accessor"
