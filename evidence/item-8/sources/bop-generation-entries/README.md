# Biomes O' Plenty generation entry consumers

Selector 70dade0 captures nine classes. All ten generated files reproduce exactly
against the independent r1 capture. Manifest SHA-256:
e39ce1ed03f04e960d04b689e6843a27be532200b5b7c523162564b489ddcaed.

```sh
uv run -m tools.inspect_item8_pool_elements --archive BiomesOPlenty-neoforge-1.21.1-21.1.0.13.jar --class-name biomesoplenty/core/BiomesOPlenty.class --class-name biomesoplenty/neoforge/core/BiomesOPlentyNeoForge.class --class-name biomesoplenty/neoforge/datagen/DataGenerationHandler.class --class-name biomesoplenty/init/ModBiomes.class --class-name biomesoplenty/worldgen/feature/BOPBaseFeatures.class --class-name biomesoplenty/worldgen/carver/BOPWorldCarvers.class --class-name biomesoplenty/worldgen/carver/OriginCaveWorldCarver.class --class-name biomesoplenty/neoforge/mixin/MixinBloodFluid.class --class-name biomesoplenty/neoforge/mixin/MixinLiquidNullFluid.class --output evidence/raw/item8/bop-generation-entries-r1
```

The NeoForge entry calls the common initializer and prepares GlitchCore event
handlers. The common initializer registers content through RegistryHelper.
Preserved method handles bind the feature registrar to BOPBaseFeatures and the
carver registrar to BOPWorldCarvers. Its other server handler adds configured
wandering-trader trades; client handlers are guarded by Environment.isClient.
The common setup callback configures TerraBlender and fluid interactions.

ModBiomes registers Overworld and Nether regions using configuration weights,
and End Wilds, End Reef and End Corruption through its highlands-biome helper.
The region registration path is biome/terrain selection, not a separately
registered structure family. Biome datagen bootstrap code is preserved separately
from normal setup. DataGenerationHandler subscribes to the datagen event and
supplies resource providers; its presence is not evidence of a server-world run.

BOPWorldCarvers registers origin_cave. OriginCaveWorldCarver inherits vanilla
cave carving and overrides the replaceable block test for its explicit terrain
material set. It supplies no authored structure placement. The two declared
NeoForge mixins only return the registered Blood and Liquid Null FluidTypes.
They introduce no separate generation route.

BOPBaseFeatures binds the candidate anomaly, monolith and bone_spine names to
the three already preserved direct writers. Reuse d08e469 for their packaged
placement and live biome-source membership. Remaining feature implementations
still require their terrain/vegetation or candidate dispositions; this capture
does not close whole-provider coverage or validate unrelated gameplay internals.
