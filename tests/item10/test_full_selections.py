from __future__ import annotations

import json
from pathlib import Path
from typing import cast

import pytest
from pydantic import ValidationError

from mcpack_evidence.item7_runtime import WorldgenRequest
from mcpack_evidence.item7_selections import ITEM10_SELECTIONS, PILOT_SELECTIONS, RUN_SELECTIONS
from tests.item7.runtime_support import runtime_request


def test_full_generation_covers_exact_census_and_retains_only_edge_halo() -> None:
    root = Path(__file__).parents[2]
    dimensions = cast(
        "dict[str, list[str]]",
        json.loads(
            (root / "evidence/item-8/runtime/dimension-r3/dimension-biomes.json").read_text()
        ),
    )
    assert sorted({row.dimension for row in ITEM10_SELECTIONS}) == sorted(dimensions)
    assert [row.dimension for row in ITEM10_SELECTIONS] == sorted(
        row.dimension for row in ITEM10_SELECTIONS
    )
    assert len({row.label for row in ITEM10_SELECTIONS}) == 11
    for row in ITEM10_SELECTIONS:
        offset = 512 if row.label == "end-outer" else 0
        assert row.center_x == row.center_z == offset * 16
        generated = {
            (x, z) for x in range(offset - 32, offset + 33) for z in range(offset - 32, offset + 33)
        }
        census = {
            (x, z) for x in range(offset - 32, offset + 32) for z in range(offset - 32, offset + 32)
        }
        assert row.radius_chunks == 32
        assert len(generated) == row.expected_chunk_count == 4225
        assert len(census) == 4096
        assert census <= generated
        assert len(generated - census) == 129
    assert sum(row.expected_chunk_count for row in ITEM10_SELECTIONS) == 46475
    assert 4096 * len(ITEM10_SELECTIONS) * 16 == 720896


def test_full_geometry_is_explicit_and_does_not_relax_item7_presets(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    request = runtime_request(tmp_path, monkeypatch)
    data = {name: getattr(request, name) for name in WorldgenRequest.model_fields}
    for mode, selections in (
        ("pilot", PILOT_SELECTIONS),
        ("run", RUN_SELECTIONS),
        ("item10", ITEM10_SELECTIONS),
    ):
        assert (
            WorldgenRequest.model_validate(
                {**data, "mode": mode, "selections": selections}
            ).selections
            == selections
        )
        with pytest.raises(ValidationError, match="fixed generation geometry"):
            _ = WorldgenRequest.model_validate(
                {**data, "mode": mode, "selections": selections[:-1]}
            )
    with pytest.raises(ValidationError, match="fixed generation geometry"):
        _ = WorldgenRequest.model_validate({**data, "selections": ITEM10_SELECTIONS})
