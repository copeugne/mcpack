# Explorations scarecrow scope

Captured with f92c2d3 and reproduced byte for byte. Manifest SHA-256:
10fef0e01f61350f80a293996510e87642d07ada473ecbc81882236a2b7d3b43.

```sh
uv run -m tools.inspect_item8_pool_elements --archive explorations-neoforge-1.21.1-1.6.2.jar --class-name com/tristankechlo/explorations/worldgen/features/ScarecrowFeature.class --output evidence/raw/item8/explorations-scarecrow-scope-r1
```

ScarecrowFeature writes a five-position figure: legs at the origin, body above,
head two blocks above and two arms beside the body. Head/body/legs/arm states
come from configuration. Horizontal facing and material choices do not create
different structure families. The write results are ignored; the code returning
true does not prove every block was placed.

The packaged catalog contains nine named material configurations of type
explorations:scarecrow (acacia, bamboo, birch, cherry, dark_oak, jungle, mangrove,
oak and spruce). The unsuffixed scarecrow configured feature instead uses
minecraft:simple_random_selector. All ten names occur in the preserved live
configured-feature registry. This is one scarecrow design candidate, not ten
families. Complete registration, selector and placement/biome relationships
before final acceptance; no further arm/head helper tracing is needed for the
family boundary. No new world measurement.

## Complete descriptive attribution

Six additional required attributes and resolved membership for all nine biome
tags are integrated in the family decision and inventory. Existing geometry,
placement and qualitative form are preserved. Use biome_constraint with the
variant_tags, structure-inputs.json biome_tags and the captured worldgen_biome
registry. All nine resolve without missing/unresolved inputs. Join those lists
to dimension-r3/dimension-biomes.json: each overlaps only the Overworld.

The full writer and its arm/head helpers only write or adjust block states.
The nine packaged configurations select material fences and pumpkin heads;
ScarecrowFeatureConfig in explorations-provider supplies the omitted hay body.
No direct mob, spawner or container-loot operation is present. Natural mobs,
block harvesting and successful placement remain separate from these source
answers. This does not promise that the figure repels enemies or spawns a guard.

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-scarecrow-descriptions.json
uv run pytest -q tests/item8/test_explorations_provider_scope.py tests/item8/test_structure_biomes.py tests/item8/test_biome_tag_inputs.py tests/item8/test_biome_resolution.py
uv run ruff check tools/build_item8_inventory.py
uv run basedpyright tools/build_item8_inventory.py
```

Seventeen affected tests pass; scoped quality checks pass. An initial command
named nonexistent test_biomes.py and ran no tests; the commands above correct
that filename error. No new capture, measurement or validation framework.
