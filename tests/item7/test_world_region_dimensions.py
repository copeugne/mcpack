from pathlib import Path

import pytest

from mcpack_evidence.item7_anvil import RegionDecodeError, world_regions


@pytest.mark.parametrize(
    ("relative", "dimension", "geometry"),
    [
        ("region", "minecraft:overworld", (-64, 384)),
        ("DIM-1/region", "minecraft:the_nether", (0, 256)),
        ("DIM1/region", "minecraft:the_end", (0, 256)),
    ],
)
def test_vanilla_dimension_context_is_preserved(
    tmp_path: Path, relative: str, dimension: str, geometry: tuple[int, int]
) -> None:
    directory = tmp_path / relative
    directory.mkdir(parents=True)
    (directory / "r.0.0.mca").touch()
    ((_, context),) = world_regions(tmp_path)
    assert context.dimension == dimension
    assert (context.min_y, context.build_height) == geometry


def test_custom_dimension_requires_geometry_instead_of_becoming_overworld(tmp_path: Path) -> None:
    directory = tmp_path / "dimensions/example/nested/moon/region"
    directory.mkdir(parents=True)
    (directory / "r.0.0.mca").touch()
    with pytest.raises(
        RegionDecodeError, match="dimension geometry required for example:nested/moon"
    ):
        _ = world_regions(tmp_path)
    ((_, context),) = world_regions(tmp_path, dimension_geometry={"example:nested/moon": (16, 128)})
    assert context.dimension == "example:nested/moon"
    assert (context.min_y, context.build_height) == (16, 128)


@pytest.mark.parametrize("geometry", [(1, 256), (0, 0), (0, -16), (0, 17)])
def test_invalid_explicit_geometry_is_rejected(tmp_path: Path, geometry: tuple[int, int]) -> None:
    directory = tmp_path / "region"
    directory.mkdir()
    (directory / "r.0.0.mca").touch()
    with pytest.raises(RegionDecodeError, match="invalid build geometry"):
        _ = world_regions(tmp_path, dimension_geometry={"minecraft:overworld": geometry})


def test_nested_unidentified_region_directory_is_not_counted_as_overworld(tmp_path: Path) -> None:
    directory = tmp_path / "backup/region"
    directory.mkdir(parents=True)
    (directory / "r.0.0.mca").touch()
    with pytest.raises(RegionDecodeError, match="supported dimension layout"):
        _ = world_regions(tmp_path)
