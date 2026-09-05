# Delegated stone ore generation

Captured using extractor revision 42a3de8. The capture and identities.json
reproduced byte for byte before this README was added:

```sh
uv run -m tools.inspect_item8_pool_elements --archive Zeta-1.1-40.jar --class-name org/violetmoon/zeta/world/generator/OreGenerator.class --output evidence/raw/item8/zeta-stone-ore-42a3de8
```

The NewStoneTypesModule callback preserved in quark-stone-clusters registers
OreGenerator with a stone block's default state and ALL_DIMS_STONE_MATCHER.
OreGenerator.generateChunk passes candidate positions from OrePocketConfig to
place. The latter derives an ore-vein volume from clusterSize and randomness,
then doPlace traverses that volume, deduplicates positions with a BitSet, tests
the supplied matcher and writes only placeState with flag two. It discards
setBlock's boolean result and counts attempted matching writes. Its return value
is therefore not proof of observed placement success.

The supplied combined matcher joins stone/deepslate, netherrack and end-stone
predicates. The writer has no entity, spawner, chest, loot-table or authored-room
operation. Together with the cluster writer already captured, this supports a
working terrain-contribution disposition for these stone-generation paths.
Material variants and ore pockets are not separate authored structure families.

This does not establish effective enablement, sampling frequency, occupied
extent or world occurrence. Exact candidate enumeration is unnecessary for this
family boundary and is not claimed audited. Do not expand into crafting,
material properties or unrelated configuration helpers to repeat this decision.
Scoped extractor Ruff and Basedpyright passed. No new measurement or server run.
