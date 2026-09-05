# Vanilla buried treasure source inspection

Three classes from the frozen mapped server establish the direct piece generator.
Manifest SHA-256: `a3ee21e981a4c041695e894ba4c5ef8221ac720283870f2e71f9cb41b0a5bd4f`.
Archive SHA-256: `26ca9c40d7e1681190b428583c38816852218e78df3f8bdb60a59a78503aec71`.

```sh
uv run -m tools.inspect_item8_pool_elements --archive server-1.21.1-20240808.144430-srg.jar --class-name net/minecraft/world/level/levelgen/structure/structures/BuriedTreasureStructure.class --class-name net/minecraft/world/level/levelgen/structure/structures/BuriedTreasurePieces.class --class-name 'net/minecraft/world/level/levelgen/structure/structures/BuriedTreasurePieces$BuriedTreasurePiece.class' --output evidence/item-8/sources/vanilla-buried-treasure-code
uv run ruff check tools/inspect_item8_pool_elements.py
uv run basedpyright tools/inspect_item8_pool_elements.py
```

Extraction and scoped checks passed. Reproduce into a fresh output directory.
This uses the existing extractor and adds no measurement system or server run.
The complete disassemblies are one generated source-evidence increment.

The structure creates one BuriedTreasurePiece at chunk-local X 9, Z 9 and
initial Y 90. Its bounding box is a single position. postProcess replaces the
initial height with OCEAN_FLOOR_WG at that X/Z, then scans downward while Y is
above minimum build height. The block below must equal a default sandstone,
stone, andesite, granite or diorite state. This uses exact state identity, not
a general solid-block test. If no match is found, it returns without a chest.

On a match, it chooses the current block as fill unless that block is air or
isLiquid, in which case fill is sand. isLiquid recognizes exact default water
and lava states. It examines each directly adjacent position; eligible air or
liquid gaps receive the support state or selected fill, according to the block
below the neighbor and whether the direction is UP. It then sets the piece box
to the single selected position and calls createChest with BURIED_TREASURE.
The boolean result is discarded and the method returns, so this code does not
prove successful chest creation. No template, pool, mob or spawner generator
is invoked. The container and surrounding infill are not a surface landmark.

The one-position piece box describes the chest target, not the neighboring
terrain edits or a guaranteed surviving chest. Natural mobs, actual cover,
visual range and retained-mod transformations are not established here.

## Family integration

The decision records an empty template list as resolved absence and identifies
the direct piece class. Seven source-backed attributes cover hostility, mobs,
loot, spawners, enemy attribution, authored visual cues and placement. Existing
observed geometry is preserved. The absence of a landmark is distinct from
actual visibility, which still depends on terrain and final placement.

Existing BuiltInLootTables evidence in `../vanilla-end-city-code` maps
BURIED_TREASURE to `minecraft:chests/buried_treasure`. Its manifest SHA-256 is
`ca7cb2c777ad0fc638e28cded50a78ab048ca26ad243eeb564fa72be7cac943c`.
The focused test binds both source manifests and their disassemblies to the
decision, including the direct piece and loot-reference identities.

```sh
uv run pytest -q tests/item8/test_buried_treasure_sources.py tests/item8/test_family_decisions.py tests/item8/test_dimension_capture.py
uv run ruff check tests/item8/test_buried_treasure_sources.py tests/item8/test_family_decisions.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_buried_treasure_sources.py tests/item8/test_family_decisions.py tools/build_item8_inventory.py
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-buried-treasure-content.json
```

Decision SHA-256:
`873cac500cf01735864b85e9f5db35ef99085ae3d33990b45774f1eb6d836b3c`.
Retained-mod effects and actual generated rewards remain unresolved. This is a
family increment, not Item 8 completion, and adds no measurement system.

All 62 affected tests passed. Basedpyright passed. Ruff passed after combining
the two empty-list assertions in the existing test and wrapping the expression,
keeping the change within its existing statement-count limit without a new helper.
