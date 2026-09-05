# Vanilla End city generation sources

Extractor change `888f3b8`, source delivery `a73fd28`, and frozen template check
`f5348b7` connect the custom End city generator to packaged components and markers.
Manifest SHA-256:
`ca7cb2c777ad0fc638e28cded50a78ab048ca26ad243eeb564fa72be7cac943c`.
It binds all nine class disassemblies to mapped-server archive SHA-256
`26ca9c40d7e1681190b428583c38816852218e78df3f8bdb60a59a78503aec71`.

Executed extraction, followed by the focused check:

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive server-1.21.1-20240808.144430-srg.jar \
  --class-name net/minecraft/world/level/levelgen/structure/structures/EndCityStructure.class \
  --class-name net/minecraft/world/level/levelgen/structure/structures/EndCityPieces.class \
  --class-name 'net/minecraft/world/level/levelgen/structure/structures/EndCityPieces$EndCityPiece.class' \
  --class-name 'net/minecraft/world/level/levelgen/structure/structures/EndCityPieces$SectionGenerator.class' \
  --class-name 'net/minecraft/world/level/levelgen/structure/structures/EndCityPieces$1.class' \
  --class-name 'net/minecraft/world/level/levelgen/structure/structures/EndCityPieces$2.class' \
  --class-name 'net/minecraft/world/level/levelgen/structure/structures/EndCityPieces$3.class' \
  --class-name 'net/minecraft/world/level/levelgen/structure/structures/EndCityPieces$4.class' \
  --class-name net/minecraft/world/level/storage/loot/BuiltInLootTables.class \
  --output evidence/item-8/sources/vanilla-end-city-code
uv run pytest -q tests/item8/test_end_city_sources.py
uv run ruff check tools/inspect_item8_pool_elements.py
uv run basedpyright tools/inspect_item8_pool_elements.py
uv run ruff check tests/item8/test_end_city_sources.py
uv run basedpyright tests/item8/test_end_city_sources.py
```

Extraction, the focused test and scoped checks passed. Use a fresh output
directory for reproduction. The initial non-verbose pilot remains under
`evidence/raw/item8/vanilla-end-city-code-pilot`; it lacked the concatenation
recipe and loot-key mapping needed for the final source interpretation.

## Source disposition

`EndCityStructure.findGenerationPoint` chooses a rotation and rejects its
calculated base position below Y 60. `generatePieces` calls
`EndCityPieces.startHouseTower`. The main generator and four section generators
reference 19 template names. `EndCityPiece.makeResourceLocation` uses the
`end_city/` concatenation recipe and default Minecraft namespace, retained in
verbose output. All 19 templates exist in the frozen catalog. The twentieth
packaged template, `tower_floor`, has no reference in this vanilla generator.
These are assembly components, including a possible ship, not 20 families.

The recursive child assembler rejects depth greater than eight and tests
piece collisions before accepting a generated group. The archived code preserves
branch and ship-selection conditions. Neither the number of referenced templates
nor recursion depth establishes assembled footprint, height or encounter cadence.

`EndCityPiece.makeSettings` sets ignoreEntities to true and selects either the
structure-block ignore processor or the structure-and-air ignore processor.
`handleDataMarker` has three relevant prefix branches:

- `Chest`: assign `BuiltInLootTables.END_CITY_TREASURE` to the block below the
  marker when that position is inside the supplied bounding box. The retained
  loot registry initializer maps this constant to `chests/end_city_treasure`.
- `Sentry`: create a shulker at the marker when inside the box and spawnable
  world bounds. Creation can return null; adding an entity is not proof that a
  specific generated world contains it.
- `Elytra`: create an item frame facing rotated south, containing an elytra,
  subject to the same position bounds. This is authored placed content, not a
  chest-table roll or a mob spawner.

The hash-bound catalog test preserves the exact marker counts by template:
base floor, fat-tower middle/top, second-floor variant 2, ship, third-floor
variant 2 and tower top carry the relevant markers. Referenced templates have
empty authored entity lists and no explicit ordinary/trial-spawner NBT IDs.
Marker counts are per template, not per assembled city or measured population.

## Remaining work

Incorporate these source-backed mob, loot and component dispositions into the
existing End city family attributes. Preserve the custom-generation trace entry
as a no-direct-pool distinction rather than pretending this is jigsaw tracing.
Retained-mod transformations, effective loot modifications, final geometry and
other unresolved family attributes still need reconciliation. The current trace,
family decisions and inventory have not changed in this source milestone.
