"""Reuse accepted canonical membership without promoting attempts to locations."""

from typing import cast

import pytest
from tools.analyze_structure_density import (
    attribute_nonregistry_attempt,
    location_observation_acceptance,
    nonregistry_attempt_outcome,
    nonregistry_location_groups,
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


@pytest.mark.parametrize(
    ("returned", "block", "expected"),
    [
        (False, "minecraft:dandelion", "CONTENT_OBSERVED"),
        (True, "minecraft:air", "NO_CONTENT_OBSERVED"),
    ],
)
def test_fairy_origin_state_not_delegate_return_establishes_content(
    *, returned: bool, block: str, expected: str
) -> None:
    rows = attempt("org.violetmoon.quark.content.world.gen.FairyRingGenerator")
    rows[2:2] = [
        {"kind": "writer", "site": 1},
        write([1, 2, 3], "minecraft:air"),
        {"kind": "flower_begin", "position": [1, 2, 3]},
        {"kind": "flower_end", "returned": returned},
        {"kind": "flower_state", "state": "Block{" + block + "}"},
    ]
    result = nonregistry_attempt_outcome(rows, nonregistry_membership())
    assert result["outcome"] == expected
    assert result["last_successful_writes"] == [
        {"position": [1, 2, 3], "block_id": "minecraft:air"}
    ]
    assert result["flower_observations"] == [{"position": [1, 2, 3], "block_id": block}]


def test_fairy_cleanup_uses_collector_site_one_not_bytecode_offset() -> None:
    rows = attempt("org.violetmoon.quark.content.world.gen.FairyRingGenerator")
    rows[2:2] = [{"kind": "writer", "site": 1}, write([1, 2, 3], "minecraft:stone")]
    result = nonregistry_attempt_outcome(rows, nonregistry_membership())
    assert result["outcome"] == "NO_CONTENT_OBSERVED"


def outcome(number: int, family: str, anchor: list[int]) -> dict[str, object]:
    return {
        "attempt": number,
        "family": family,
        "anchor": anchor,
        "dimension": "minecraft:the_end",
        "route": "ordinary_generation",
        "outcome": "CONTENT_OBSERVED",
        "content_positions": [[1, 2, 3]],
        "content_blocks": [{"position": [1, 2, 3], "block_id": "supplementaries:urn"}],
    }


def test_components_share_source_and_arena_ignores_component_height() -> None:
    rows = [
        outcome(1, "quark:spiral_spire", [1, 0, 2]),
        outcome(2, "quark:spiral_spire", [1, 0, 2]),
        outcome(3, "betterendisland:dragon_arena", [0, 70, 0]),
        outcome(4, "betterendisland:dragon_arena", [0, 100, 0]),
    ]
    result = nonregistry_location_groups(
        rows, {"central": ("minecraft:the_end", (-32, 31, -32, 31))}
    )
    locations = cast("list[dict[str, object]]", result["locations"])
    assert len(locations) == 2
    assert locations[0]["attempts"] == [3, 4]
    assert locations[0]["anchor_y"] is None
    assert locations[1]["attempts"] == [1, 2]
    assert result == nonregistry_location_groups(
        list(reversed(rows)), {"central": ("minecraft:the_end", (-32, 31, -32, 31))}
    )


def test_halo_and_zero_content_sources_are_retained() -> None:
    row = outcome(1, "quark:spiral_spire", [-1, 0, 0])
    row.update(outcome="NO_CONTENT_OBSERVED", content_positions=[])
    result = nonregistry_location_groups([row], {"central": ("minecraft:the_end", (0, 0, 0, 0))})
    locations = cast("list[dict[str, object]]", result["locations"])
    assert locations[0]["frame"] is None
    assert locations[0]["chunk_x"] == -1
    assert locations[0]["outcomes"] == {"NO_CONTENT_OBSERVED": 1}


def test_overlapping_patch_origins_remain_explicit() -> None:
    rows = [
        outcome(1, "supplementaries:cave_urn_cache", [1, 2, 3]),
        outcome(2, "supplementaries:cave_urn_cache", [2, 2, 3]),
    ]
    result = nonregistry_location_groups(rows, {})
    assert result["overlaps"] == [{"candidates": [0, 1], "shared_content_positions": 1}]
    assert result["status"] == "CANDIDATES_AWAITING_ACCEPTANCE"


def test_overlapping_frames_reject_ambiguous_denominator() -> None:
    with pytest.raises(ValueError, match="overlapping sample frames"):
        _ = nonregistry_location_groups(
            [outcome(1, "quark:spiral_spire", [0, 0, 0])],
            {"a": ("minecraft:the_end", (0, 1, 0, 1)), "b": ("minecraft:the_end", (0, 1, 0, 1))},
        )


@pytest.mark.parametrize(
    ("case", "expected"),
    [
        ("normal", "OBSERVED_LOCATION"),
        ("missing", "SAVED_CONTENT_UNAVAILABLE"),
        ("changed", "CONTENT_NOT_PRESERVED"),
        ("failure", "PARTIAL_FAILURE"),
        ("empty", "NO_CONSTRUCTIVE_CONTENT"),
        ("outside", "OUTSIDE_FRAME"),
        ("lifecycle", "NON_WORLDGEN_CONTEXT"),
        ("overlap", "OVERLAP_REVIEW_REQUIRED"),
    ],
)
def test_location_observation_dispositions_preserve_uncertainty(case: str, expected: str) -> None:
    row = outcome(1, "supplementaries:cave_urn_cache", [1, 2, 3])
    if case == "failure":
        row["outcome"] = "EXCEPTION_WITH_CONTENT"
    if case == "lifecycle":
        row["route"] = "non_worldgen_accessor"
    if case == "empty":
        row.update(content_blocks=[], content_positions=[], outcome="NO_CONTENT_OBSERVED")
    rows = [row]
    if case == "overlap":
        rows.append(outcome(2, "supplementaries:cave_urn_cache", [2, 2, 3]))
    frames = {} if case == "outside" else {"end": ("minecraft:the_end", (0, 0, 0, 0))}
    grouped = nonregistry_location_groups(rows, frames)
    saved: dict[str, object] = {
        "observations": [
            {
                "dimension": "minecraft:the_end",
                "position": [1, 2, 3],
                "saved_state": None
                if case == "missing"
                else {"Name": "minecraft:air" if case == "changed" else "supplementaries:urn"},
            }
        ]
    }
    dispositions = location_observation_acceptance(grouped, rows, saved)
    assert all(item["disposition"] == expected for item in dispositions)
