from __future__ import annotations

import gzip
import hashlib

import pytest
from tools.extract_item8_world_context import world_context

from tests.item7.anvil_support import compound, integer, string


def level_data(seed: int = 42) -> bytes:
    return gzip.compress(
        compound(
            "",
            (
                compound(
                    "Data",
                    (
                        compound("WorldGenSettings", (integer("seed", seed),)),
                        compound("DataPacks", ()),
                        compound("Version", (string("Name", "1.21.1"),)),
                        compound("Player", (string("UUID", "must-not-publish"),)),
                        string("LevelName", "private name"),
                    ),
                ),
            ),
        ),
        mtime=0,
    )


def test_world_context_retains_source_identity_without_player_data() -> None:
    raw = level_data()
    result = world_context(raw)
    assert result["level_dat_sha256"] == hashlib.sha256(raw).hexdigest()
    assert result["WorldGenSettings"] == {"seed": 42}
    assert "Player" not in result
    assert "LevelName" not in result
    assert "must-not-publish" not in str(result)


def test_other_seed_cannot_be_bound_to_registry_capture() -> None:
    with pytest.raises(ValueError, match="does not match"):
        _ = world_context(level_data(43))
