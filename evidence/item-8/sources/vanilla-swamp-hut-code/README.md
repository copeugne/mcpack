# Vanilla swamp hut source inspection

Two frozen mapped-server classes preserve the direct hut generator.
Manifest SHA-256: `504b9d418376e547f229aca14b3d91e8b60fa0e2e4fe84f733dfa1cfc376bb5e`.
Archive SHA-256: `26ca9c40d7e1681190b428583c38816852218e78df3f8bdb60a59a78503aec71`.

```sh
uv run -m tools.inspect_item8_pool_elements --archive server-1.21.1-20240808.144430-srg.jar --class-name net/minecraft/world/level/levelgen/structure/structures/SwampHutStructure.class --class-name net/minecraft/world/level/levelgen/structure/structures/SwampHutPiece.class --output evidence/item-8/sources/vanilla-swamp-hut-code
uv run -m tools.inspect_item8_pool_elements --archive server-1.21.1-20240808.144430-srg.jar --class-name net/minecraft/world/level/levelgen/structure/ScatteredFeaturePiece.class --output evidence/item-8/sources/vanilla-scattered-feature-code
uv run ruff check tools/inspect_item8_pool_elements.py
uv run basedpyright tools/inspect_item8_pool_elements.py
```

Extraction and checks passed. Reproduce into fresh directories. The shared
ScatteredFeaturePiece source is needed to interpret constructor dimensions and
height adjustment, rather than assuming their meaning from integer arguments.
It also serves the remaining desert pyramid and jungle temple generators.
No measurement system or server run is added.

The structure uses WORLD_SURFACE_WG for its generation stub and adds one piece
at the chunk origin. The piece constructor supplies width 7, height 7, depth 9
and random horizontal orientation to ScatteredFeaturePiece. Its initial Y 64
is not final terrain placement. updateAverageGroundHeight with offset 0 averages
MOTION_BLOCKING_NO_LEAVES samples inside the supplied clipping box and shifts
the piece box to that average. With no eligible samples it returns false and
the hut post-process returns. Nominal dimensions are not exposed height.

The hut directly places spruce planks/stairs, oak logs/fences, air, a potted red
mushroom, crafting table and cauldron. No template, pool, chest loot or spawner
path appears in these classes. Four support calls at local (1,-1,2), (5,-1,2),
(1,-1,7) and (5,-1,7) fill oak logs downward. Their terrain-dependent depth lies
outside the nominal seven-block piece height.

At transformed local (2,2,5), the piece attempts a persistent witch and cat,
each finalized with STRUCTURE spawn reason and local difficulty, then added
with passengers. Each path requires its saved flag to be false and the target
to be inside the clipping box. The flag is set BEFORE EntityType.create and its
null check, so a set flag does not prove a successful spawn or trigger a retry.
The flags are preserved as Witch and Cat in saved piece data. No specific cat
variant or observed population is inferred from this source.

The packaged root additionally specifies piece-bounded natural-spawn candidates:
monster witch and creature cat, each weight 1 with minCount=maxCount=1. These
candidate entries are distinct from the generation attempts and do not measure
actual spawning or prove farm throughput. Retained-mod transformations remain
unresolved; the source does not close Item 8 by itself.

## Family integration

Nine attributes are recorded from these sources: nominal footprint/height,
hostility interpretation, mob source, loot, spawners, enemy attribution,
authored visual form and surface placement. Dimension and biome evidence are
preserved. The empty template list is resolved absence for the direct piece.
The focused test binds both code manifests, derives constructor dimensions,
checks explicit block/entity identities and reconciles the two packaged spawn
categories with the family record. No additional measurement system is required.

```sh
uv run pytest -q tests/item8/test_swamp_hut_sources.py tests/item8/test_family_decisions.py tests/item8/test_dimension_capture.py
uv run ruff check tests/item8/test_swamp_hut_sources.py tests/item8/test_family_decisions.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_swamp_hut_sources.py tests/item8/test_family_decisions.py tools/build_item8_inventory.py
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-swamp-hut-content.json
```

Decision SHA-256:
`ce6e76b57b9b5a015cd05472a95ea23510a67c99d2c544949ef9931097d69ef1`.
This records vanilla behavior with its limitations, not successful placement,
actual visibility, effective retained-mod behavior or completion of Item 8.

All 62 affected tests passed. Scoped Ruff and Basedpyright checks passed.

Source evidence is delivered in `ab64119`, decisions and tests in `5498f16`.
The inventory was rebuilt at `5498f16` with the command above. Inventory SHA:
`d93524bb47e54899420a239639a7799f24f698ff0e8e104264d2b6eb7fe0ae14`.
Changes are confined to swamp hut content/grouping and decision input identity.
Dimension membership, biome constraints and existing world-observation links are preserved.
