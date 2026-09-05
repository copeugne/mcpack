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

## Family integration

All thirteen references resolve in the frozen catalog and are linked to each of
the seven roots. Each template has exactly one chest with the embedded loot
reference `minecraft:chests/ruined_portal`, and an empty entity list. No ordinary
or trial-spawner block types occur in the palettes. The only other block entities
are one jigsaw in each of portal_1 through portal_5. Their name, pool and target
are all `minecraft:empty`. Their final_state is netherrack except portal_3, which
specifies air. These metadata are not evidence of another active pool chain.
This inspection does not claim the final generated state of those jigsaw blocks.

Six attributes are now recorded: hostility interpretation, mob source, loot
source, spawners, enemy attribution and per-root placement modes. Observed
geometry remains intact; template dimensions do not cover terrain additions.
Retained-mod transformations and visual discoverability remain unresolved.

```sh
uv run pytest -q tests/item8/test_ruined_portal_sources.py tests/item8/test_family_decisions.py tests/item8/test_dimension_capture.py
uv run ruff check tests/item8/test_ruined_portal_sources.py tests/item8/test_family_decisions.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_ruined_portal_sources.py tests/item8/test_family_decisions.py tools/build_item8_inventory.py
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-ruined-portal-content.json
```

The focused test binds the source and template hashes, all thirteen references,
every chest, entity list, spawner palette check, five jigsaw metadata records
and all seven placement-mode derivations. Decision SHA-256:
`b8e7afa9e0bce110f88071c2eefdabd1f0c4500a93c0f2f1c1e6b4f4dde1f305`.
No measurement system or additional family is introduced. Item 8 remains open.

All 62 affected tests passed. Scoped Ruff and Basedpyright checks passed.
