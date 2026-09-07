"""Final listing coverage and preservation across existing assessment shapes."""

from __future__ import annotations

import json
from pathlib import Path
from typing import TYPE_CHECKING, cast

import pytest
from tools.build_item8_inventory import consolidate, main

if TYPE_CHECKING:
    from _pytest.monkeypatch import MonkeyPatch
    from pydantic import JsonValue


def test_final_listing_preserves_family_assessments_and_registry_coverage(
    tmp_path: Path, monkeypatch: MonkeyPatch,
) -> None:
    output = tmp_path / "inventory.json"
    monkeypatch.setattr("sys.argv", ["build_item8_inventory", "--output", str(output)])
    main()
    result = cast("dict[str, JsonValue]", json.loads(output.read_text()))
    families = cast("dict[str, dict[str, JsonValue]]", result["families"])
    other = cast("dict[str, dict[str, JsonValue]]", result["other_registry_groups"])
    assert len(families) == 448
    assert len(other) == 18
    assert not families.keys() & other.keys()
    assert "aether:large_aercloud" in other
    assert "minecraft:stronghold" in other
    roots = [root for row in [*families.values(), *other.values()]
             for root in cast("list[str]", row["structure_ids"])]
    assert len(roots) == len(set(roots)) == 887
    assert result["unassigned_registry_ids"] == []
    non_registry = cast("dict[str, JsonValue]", result["non_registry_content"])
    contributions = cast("dict[str, dict[str, JsonValue]]", non_registry["contributions"])
    # Exercise all three existing source layouts without recomputing their assessments.
    examples = {
        "yungsbridges:bridge": cast(
            "list[dict[str, JsonValue]]", contributions["yungsbridges:bridges"]["families"]
        )[0],
        "betterend:crashed_ship": contributions["betterend:crashed_ship"],
        "betterend:mushroom_library": cast(
            "dict[str, dict[str, JsonValue]]", contributions["betterend:biome_buildings"]["designs"]
        )["betterend:mushroom_library"],
        "explorations:scarecrow": contributions["explorations:scarecrow"],
    }
    for family, source in examples.items():
        assert families[family]["structure_ids"] == []
        for attribute, value in cast("dict[str, JsonValue]", source["attributes"]).items():
            assert families[family][attribute] == value
    assert result["status"] == "INCOMPLETE"


def test_consolidation_rejects_duplicate_family_across_contributors() -> None:
    decisions = cast("dict[str, JsonValue]", json.loads(
        Path("evidence/item-8/family-decisions.json").read_text()
    ))
    non_registry = cast("dict[str, JsonValue]", decisions["non_registry_content"])
    contributions = cast("dict[str, dict[str, JsonValue]]", non_registry["contributions"])
    contribution = contributions["betterend:crashed_ship"]
    with pytest.raises(ValueError, match="duplicate canonical family"):
        consolidate({"families": {}}, {"first": contribution, "second": contribution})


def test_consolidation_rejects_missing_required_assessment() -> None:
    with pytest.raises(ValueError, match="attributes differ from requirements"):
        consolidate(
            {"families": {}},
            {"example": {"families": ["example:family"], "attributes": {}}},
        )
