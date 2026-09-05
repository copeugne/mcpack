# Quark registered End generators

Extractor revision: `410f776dc4d60cdab00f1f80b78c1117246b3523`.
Exact archive, class and disassembly hashes are in identities.json.

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive Quark-4.1-480.jar \
  --class-name org/violetmoon/quark/content/world/gen/ChorusVegetationGenerator.class \
  --class-name org/violetmoon/quark/content/world/gen/SpiralSpireGenerator.class \
  --output evidence/raw/item8/quark-end-generators-410f776-reproduction
diff -r --exclude=README.md evidence/item-8/sources/quark-end-generators \
  evidence/raw/item8/quark-end-generators-410f776-reproduction
```

Fresh reproduction matched exactly before this README was added. Scoped
extractor Ruff and Basedpyright passed.

Both generators extend MultiChunkFeatureGenerator. Their getSourcesInChunk
methods reject source positions closer than 1050 to Vec3i.ZERO and require
positive configured rarity with nextInt(rarity) equal to zero. Chorus Vegetation
also requires the sampled source biome to be END_HIGHLANDS. Its chunk-part code
selects chorus_weeds or chorus_twist and requests placement above a searched
End Stone surface; getChance distinguishes highlands, midlands and other biomes
using module fields. These are vegetation requests, not template families.

Spiral Spire chunk-part generation checks the module's biome predicate, searches
downward for End Stone and calls makeSpike. The preserved full makeSpike method
contains block-level geometry and Myalite placement, with material checks that
include obsidian and crying obsidian. Its complete geometry and interaction
interpretation remain open; do not infer them from selected string references.

The source exclusion alone does not prove that generated parts cannot reach
the central island: source-to-chunk reach is controlled by the shared
MultiChunkFeatureGenerator, and effective radii/configuration must be reconciled.
DimensionConfig and the shared generator are concrete remaining applicability
dependencies. No observed generation, complete provider coverage or final family
classification is asserted by this capture.
