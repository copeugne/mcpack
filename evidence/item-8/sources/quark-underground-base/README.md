# Shared underground generator and basic style

Captured at extractor revision ec82adc. identities.json binds the retained
archive, classes and disassemblies. Both captures and identities reproduced
byte for byte before this README was added:

```sh
uv run -m tools.inspect_item8_pool_elements --archive Quark-4.1-480.jar --class-name org/violetmoon/quark/content/world/undergroundstyle/base/UndergroundStyleGenerator.class --class-name org/violetmoon/quark/content/world/undergroundstyle/base/BasicUndergroundStyle.class --output evidence/raw/item8/quark-underground-base-ec82adc
```

UndergroundStyleGenerator extends ClusterBasedGenerator. Its constructor passes
the configured dimensions, cluster settings and style-name hash to that base.
Its reported feature radius is horizontalSize plus horizontalVariation. Source
selection returns no position unless rarity is positive and nextInt(rarity)
is zero. It then chooses local X/Z in 0 through 15 and Y in the configured
half-open minYLevel/maxYLevel interval. The configured biome predicate must
accept the sampled biome and WORLD_SURFACE_WG height must be at least that Y.
Only then does it return the single candidate source.

createContext constructs UndergroundStyleGenerator.Context with world, source,
chunk generator, random and style settings. The outer class does not implement
per-position generation, so its source selection alone cannot establish a
terrain-only disposition or a structure-family boundary.

BasicUndergroundStyle stores floor, ceiling and wall states. Each corresponding
fill method writes its non-null configured state at the supplied position,
using flag two and discarding the Boolean write result. fillInside calls
fillWall only when mimicInside is true. The three-state constructor sets
mimicInside false. There is no entity, physical-spawner or container-loot
operation in these methods. This is limited to this base implementation;
subclass overrides and the generation context remain separate.

The necessary remaining direct source is UndergroundStyleGenerator.Context,
which decides what positions receive those operations. Inspect its generation
logic before counting or excluding the two consumers. Do not repeat the
captured source-selection predicates or basic state-writing methods. Scoped
extractor checks passed; no new measurement system or server run was added.
