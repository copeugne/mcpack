# Vanilla desert pyramid source inspection

Two classes from the frozen mapped server preserve the direct pyramid piece
and structure-level archaeology post-processing. Manifest SHA-256:
`89770d3b09f15c47e801b2889bf431d3f5e823c047cc8025c1fd433932e405d9`.
Archive SHA-256: `26ca9c40d7e1681190b428583c38816852218e78df3f8bdb60a59a78503aec71`.
The large piece disassembly is an irreducible generated source increment: its
block placement, traps, cellar and archaeology paths must remain inspectable.
No game binary is committed.

```sh
uv run -m tools.inspect_item8_pool_elements --archive server-1.21.1-20240808.144430-srg.jar --class-name net/minecraft/world/level/levelgen/structure/structures/DesertPyramidStructure.class --class-name net/minecraft/world/level/levelgen/structure/structures/DesertPyramidPiece.class --output evidence/item-8/sources/vanilla-desert-pyramid-code
uv run ruff check tools/inspect_item8_pool_elements.py
uv run basedpyright tools/inspect_item8_pool_elements.py
```

Extraction and scoped checks passed. Reproduce into a fresh output directory.
The existing extractor suffices; no measurement system or server run was added.

## Inspected paths

The piece constructor supplies width 21, height 15 and depth 21 to the preserved
ScatteredFeaturePiece base class. Its postProcess calls the lowest-ground-height
adjustment with offset -nextInt(3), returning early if adjustment fails. Initial
Y 64 is not final placement. Underground trap and cellar construction extends
below the nominal piece height, so constructor dimensions alone are not a full
assembled geometry proof.

The trap places a stone pressure plate at local (10,-11,10) and calls generateBox
with TNT across local X/Z 9 through 11 at Y -13. Chest attempts use the
DESERT_PYRAMID loot constant, and each createChest result is stored into the
corresponding hasPlacedChest entry. These flags differ from the swamp hut's
pre-creation flags. They are persisted as hasPlacedChest0 through hasPlacedChest3.
The cellar is constructed relative to (16,-4,13), with stairs, a room, sand
candidate positions and collapsed-roof placement.

The structure afterPlace collects candidate suspicious-sand positions from
DesertPyramidPiece instances into a sorted set, separately attempts a collapsed
roof position, shuffles candidates with a world-seed positional random source
at the pieces' bounding-box center, and selects min(candidate count,
nextInt(5,8)) candidates. The selection counter decreases before the helper's
clipping check. Non-selected candidates inside the clipping box become sand.
Consequently selection parameters are not a measured generated block count.

placeSuspiciousSand checks the clipping box, places suspicious sand and, when
a BrushableBlockEntity is present, assigns DESERT_PYRAMID_ARCHAEOLOGY with the
position's packed long as seed. Chest and archaeology assignment paths must
both be retained in the family inventory. No realized loot count is inferred.

## Remaining integration

The inventory and family decisions are unchanged at this source milestone.
Before integrating, resolve the SinglePieceStructure constructor callback and
placement contract, inspect the remaining cellar geometry and candidate logic,
and bind the two loot constants to the existing BuiltInLootTables evidence.
Ordinary javap output shows an invokedynamic PieceConstructor but does not show
its bootstrap target; use the extractor's existing verbose mode to preserve that
binding rather than infer it. Reuse the existing scattered-feature source.
Do not repeat the extraction above or introduce a new measurement framework.
Item 8 remains incomplete.

The constructor callback and shared wrapper are now resolved in
`../vanilla-desert-pyramid-binding-code`. Its focused test verifies the same
frozen class/archive identity and the bootstrap link to DesertPyramidPiece.
This supersedes the pending callback instruction above. Cellar geometry,
content integration and loot-source reconciliation remain open.

## Family integration

The pending content integration above is superseded. Seven family attributes
now record trap hostility, mob sources, both loot assignments, absence of
vanilla spawners, enemy attribution, authored visual form and surface/underground
placement. Existing observed geometry, dimensions and biome links are preserved.
The direct piece uses no template or pool components. BuiltInLootTables from
the existing vanilla-end-city-code evidence binds the chest and archaeology
constants to minecraft:chests/desert_pyramid and minecraft:archaeology/desert_pyramid.

Cellar sand candidates are collected as transformed world positions, not placed
immediately. The room's sand box and side candidates are distinct from the
collapsed roof. The roof first places sand/sandstone and records a positional
randomly selected roof coordinate for the separate suspicious-sand attempt.
The stairs remain part of this same cellar. No extra family, successful block
count or full occupied geometry is inferred from those components.

The existing binding test now also verifies preserved source hashes, the two
loot mappings, trap block identities, empty authored entity/spawner sources and
the saved chest-result assignment. No measurement system or server run is added.

```sh
uv run pytest -q tests/item8/test_desert_pyramid_binding.py tests/item8/test_family_decisions.py tests/item8/test_dimension_capture.py
uv run ruff check tests/item8/test_desert_pyramid_binding.py tests/item8/test_family_decisions.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_desert_pyramid_binding.py tests/item8/test_family_decisions.py tools/build_item8_inventory.py
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-desert-pyramid-content.json
```

Decision SHA-256:
`78b6dcd53d7e3c855b6e64477c0773601c3b83138705ea122eb6cc48be955378`.
Actual visibility, successful generation and effective retained-mod behavior
remain distinct from these source-derived attributes. Item 8 remains incomplete.

All 63 affected tests passed. Scoped Ruff and Basedpyright checks passed.

Content decisions and tests are delivered in `f9fe8a1`. The inventory was rebuilt
at that commit using the command above. Inventory SHA-256:
`960a8759842f2a0a267fba6eae526c8e59062d08e6148c33fad7d5d498b1e133`.
Changes are confined to this family's content/grouping and decision input hash.
The unchanged footprint and vertical-size fields remain UNKNOWN: this family
has no retained full-start envelope observation. Nominal constructor dimensions
do not resolve its full generated vertical extent.
