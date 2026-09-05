# Vanilla ruined portal source inspection

The existing extractor preserves the structure, piece, setup, properties and
placement enum from the frozen mapped server. These five complete disassemblies
are one generated source-evidence increment, needed to interpret the shared
variant selection and placement paths without truncating their implementation.
Manifest SHA-256: `c5cde03aa864cfadf9b167a01e4cd90d2193ba6e67b5c5b0a4edaff56ef93f79`.
Archive SHA-256: `26ca9c40d7e1681190b428583c38816852218e78df3f8bdb60a59a78503aec71`.

```sh
uv run -m tools.inspect_item8_pool_elements --archive server-1.21.1-20240808.144430-srg.jar --class-name net/minecraft/world/level/levelgen/structure/structures/RuinedPortalStructure.class --class-name 'net/minecraft/world/level/levelgen/structure/structures/RuinedPortalStructure$Setup.class' --class-name net/minecraft/world/level/levelgen/structure/structures/RuinedPortalPiece.class --class-name 'net/minecraft/world/level/levelgen/structure/structures/RuinedPortalPiece$Properties.class' --class-name 'net/minecraft/world/level/levelgen/structure/structures/RuinedPortalPiece$VerticalPlacement.class' --output evidence/item-8/sources/vanilla-ruined-portal-code
uv run ruff check tools/inspect_item8_pool_elements.py
uv run basedpyright tools/inspect_item8_pool_elements.py
```

Extraction and scoped checks passed. Reproduce into a fresh output directory.
No new measurement system or server run is needed for this source inspection.

## Selection and placement

The structure selects a setup using its normalized weights (or the sole setup),
then samples airPocket and copies material/vegetation settings. A nextFloat <
0.05 selects one of giant_portal_1 through giant_portal_3; otherwise it selects
portal_1 through portal_10. All use the default namespace and ruined_portal path.
A random rotation and NONE or FRONT_BACK mirror act around the template's
horizontal center. The generation stub adds one RuinedPortalPiece. These are
alternatives of one generator, not additional families or jigsaw pool chains.

The generator uses OCEAN_FLOOR_WG for on_ocean_floor and WORLD_SURFACE_WG for
other placement modes. findSuitableY starts from a setup-dependent height:
Nether ranges depend on airPocket, mountain and underground ranges account for
template height, partly_buried offsets the surface-minus-height reference,
and remaining modes start at the surface reference. It scans the four base
columns at bounding-box corners downward until three satisfy the heightmap's
opaque predicate or the lower search boundary is reached. Do not reinterpret
the boundary return as a proven support test or a rejected candidate.
If canBeCold is true, coldEnoughToSnow at the selected position determines cold.

## Content and terrain changes

Settings select STRUCTURE_BLOCK versus STRUCTURE_AND_AIR according to airPocket.
Rules may remove gold, replace lava, or convert netherrack to magma. Lava becomes
magma in ocean-floor mode, netherrack when cold, or is subject to the 0.2 magma
replacement rule otherwise. Non-cold netherrack has a 0.07 magma replacement rule.
Gold removal uses 0.3. These are source rule inputs, not measured block counts.
Settings also apply BlockAgeProcessor, ProtectedBlockProcessor,
LavaSubmergedBlockProcessor and optional BlackstoneReplaceProcessor.

After base placement, the piece spreads netherrack, adds downward netherrack
columns, and may add vines or overgrowth. Therefore the template envelope alone
cannot bound the full altered terrain. The data-marker handler returns without
action. No direct mob or spawner creation path appears in these classes.
Template content and effective retained-mod transformations must still be
reconciled; no claim of observed absence of natural mobs is made.
