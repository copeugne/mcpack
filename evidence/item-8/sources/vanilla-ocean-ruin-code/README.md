# Vanilla ocean ruin source inspection

Five classes are preserved from the frozen mapped-server archive. The generated
text is one source-evidence increment: it retains the complete generator, piece,
temperature enum and switch dispatch needed to interpret its branches.
Manifest SHA-256: `966f0fe1112562cc35c718bad64a241c2ef4dd8ad7331f9afd4a77b7da155382`.
Archive SHA-256: `26ca9c40d7e1681190b428583c38816852218e78df3f8bdb60a59a78503aec71`.

```sh
uv run -m tools.inspect_item8_pool_elements --archive server-1.21.1-20240808.144430-srg.jar --class-name net/minecraft/world/level/levelgen/structure/structures/OceanRuinStructure.class --class-name 'net/minecraft/world/level/levelgen/structure/structures/OceanRuinStructure$Type.class' --class-name net/minecraft/world/level/levelgen/structure/structures/OceanRuinPieces.class --class-name 'net/minecraft/world/level/levelgen/structure/structures/OceanRuinPieces$OceanRuinPiece.class' --class-name 'net/minecraft/world/level/levelgen/structure/structures/OceanRuinPieces$1.class' --output evidence/item-8/sources/vanilla-ocean-ruin-code
uv run ruff check tools/inspect_item8_pool_elements.py
uv run basedpyright tools/inspect_item8_pool_elements.py
```

Extraction and scoped checks passed. Reproduce into a fresh output directory.
This reuses the existing extractor, with no new measurement system or server run.

## Generation and content

`addPieces` selects large when nextFloat <= largeProbability, with integrity
0.9 for large or 0.8 for small. A large primary ruin may trigger cluster placement
when a second nextFloat <= clusterProbability. These are code conditions, not
observed generation frequencies. Both packaged roots set those probabilities
to 0.3 and 0.9 respectively.

Warm ruins select one template from the applicable warm array. Cold ruins choose
one array index, then place brick, cracked and mossy entries at the same position
and rotation. Cracked integrity is 0.7 and mossy is 0.5. Layers, size alternatives
and cluster components belong to the existing ocean ruin family.

Piece settings apply BlockRotProcessor, STRUCTURE_AND_AIR and the selected
archaeology processor. Warm converts sand to suspicious sand and appends
OCEAN_RUIN_WARM_ARCHAEOLOGY; cold converts gravel to suspicious gravel and appends
OCEAN_RUIN_COLD_ARCHAEOLOGY. Each processor is constructed with ConstantInt(5)
as its cap. That is not a guaranteed count of generated suspicious blocks.

The `chest` marker places a chest at the marker position, waterlogged according
to the fluid there, then assigns UNDERWATER_RUIN_BIG or UNDERWATER_RUIN_SMALL
according to isLarge, with a random seed. The `drowned` marker creates a drowned,
requires persistence, moves it to the marker, finalizes it with STRUCTURE spawn
reason and local difficulty, then adds it with passengers. If creation succeeds,
the marker becomes air above sea level or water at or below sea level. This is
an authored mob path despite the templates' empty entity lists.

Existing BuiltInLootTables evidence under `../vanilla-end-city-code` resolves
these constants to `minecraft:chests/underwater_ruin_big`,
`minecraft:chests/underwater_ruin_small`,
`minecraft:archaeology/ocean_ruin_warm` and
`minecraft:archaeology/ocean_ruin_cold`. Its manifest SHA-256 is
`ca7cb2c777ad0fc638e28cded50a78ab048ca26ad243eeb564fa72be7cac943c`.

Post-processing starts at OCEAN_FLOOR_WG at the piece origin, then applies the
piece's getHeight adjustment before base template placement. getHeight scans
downward through air, water and ice under the transformed footprint and may
lower placement where support drops. The constructor's initial Y 90 is not the
final placement height. This supports a seafloor placement classification, not
a universal submerged/exposed claim.

Template reconciliation and effective retained-mod effects remain open at this
source milestone. Preserve observed geometry; individual template dimensions
cannot establish the footprint or vertical extent of a terrain-adjusted cluster.
