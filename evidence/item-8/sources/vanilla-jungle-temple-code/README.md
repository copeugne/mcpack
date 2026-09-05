# Vanilla jungle temple source inspection

Three classes preserve the direct piece, moss-stone selector and verbose
structure constructor binding from the frozen mapped server. Manifest SHA-256:
`cafcf426ad4a03e2c80939033ac90bb72aac90ffa359ec03e802dbda84a131d1`.
Archive SHA-256:
`26ca9c40d7e1681190b428583c38816852218e78df3f8bdb60a59a78503aec71`.
The generated piece disassembly is retained as one irreducible source artifact;
no binary is committed. The existing extractor and shared placement evidence
suffice, with no new measurement system or server run.

```sh
uv run -m tools.inspect_item8_pool_elements --archive server-1.21.1-20240808.144430-srg.jar --class-name net/minecraft/world/level/levelgen/structure/structures/JungleTempleStructure.class --class-name net/minecraft/world/level/levelgen/structure/structures/JungleTemplePiece.class --class-name 'net/minecraft/world/level/levelgen/structure/structures/JungleTemplePiece$MossStoneSelector.class' --output evidence/item-8/sources/vanilla-jungle-temple-code
uv run ruff check tools/inspect_item8_pool_elements.py
uv run basedpyright tools/inspect_item8_pool_elements.py
```

Extraction, Ruff and Basedpyright passed. Reproduce into a fresh directory.
Bootstrap entry 0 binds JungleTemplePiece(RandomSource,int,int) to the shared
SinglePieceStructure callback already preserved in vanilla-desert-pyramid-binding-code.
The piece supplies initial Y 64, width 12, height 10 and depth 15 to the shared
ScatteredFeaturePiece, with random horizontal orientation. It adjusts to average
ground height with offset 0 before placement, returning on failure. Its first
stone-selector box spans local (0,-4,0) through (width-1,0,depth-1), so nominal
constructor height excludes underground construction.

The inspected paths attempt dispensers at local (3,-2,1), facing NORTH, and
(9,-2,3), facing WEST, with JUNGLE_TEMPLE_DISPENSER loot. Main and hidden chest
attempts are at (8,-3,3) and (9,-3,10), with JUNGLE_TEMPLE loot. The corresponding
placedTrap1, placedTrap2, placedMainChest and placedHiddenChest flags each store
the helper's returned boolean and are saved. Attempts are not surviving counts.
The existing BuiltInLootTables source maps these to minecraft:chests/jungle_temple_dispenser
and minecraft:chests/jungle_temple. Do not omit the dispenser loot source.

Direct blocks include tripwire, hooks, redstone wire, levers, sticky pistons,
repeater, vines and stone decoration. MossStoneSelector chooses cobblestone when
nextFloat is below 0.4, otherwise mossy cobblestone. This is a selector branch,
not a measured material ratio. No direct EntityType or spawner block path appears
in these classes. Effective retained-mod behavior remains unresolved. Family
integration and its focused verification follow this source increment.

## Family integration

Nine source-backed attributes now record nominal dimensions, trap hostility,
mob/loot/spawner sources, enemy attribution, authored form and mixed surface/
underground placement. Nominal height 10 excludes the explicit Y -4 foundation
and basement construction. Actual exposure and effective mod changes remain open.
Registry root minecraft:jungle_pyramid uses generator type minecraft:jungle_temple;
these identifiers do not create two families. Dimensions, biome constraints and
world-observation links are preserved by the existing builder.

The focused test binds source hashes, bootstrap callback, constructor dimensions,
saved helper results and both loot mappings. Its first run incorrectly selected
a public constant instead of the constructor, producing an empty integer list.
The test now selects the exact constructor signature; the source and family data
were unchanged by that correction. The corrected focused test passes.

```sh
uv run pytest -q tests/item8/test_jungle_temple_sources.py tests/item8/test_family_decisions.py tests/item8/test_dimension_capture.py
uv run pytest -q tests/item8/test_jungle_temple_sources.py
uv run ruff check tests/item8/test_jungle_temple_sources.py tests/item8/test_family_decisions.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_jungle_temple_sources.py tests/item8/test_family_decisions.py tools/build_item8_inventory.py
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-jungle-temple-content.json
```

Decision SHA-256:
`3650c5d8f0406b623cf85007f2c5f1351f18eeaea634f8a25a13107ce22d10e7`.
Source increment is delivered in `8397ebc`. This closes the pending vanilla
content integration above, not Item 8 or effective retained-mod behavior.

Final affected-suite rerun: all 62 tests passed. Scoped Ruff and Basedpyright
passed, including the corrected constructor selector.

Family decisions and tests are delivered in `b4c5e6f`. Inventory rebuilt at that
commit with the command above, SHA-256:
`055f6b523673db40380f2b670e920c1b6320c45c03e611fb29168e89700b9285`.
The diff is confined to jungle temple content/grouping and the decision input
identity. Existing dimension membership, biome and world-observation links are
preserved. This source-derived record does not establish observed generation.
