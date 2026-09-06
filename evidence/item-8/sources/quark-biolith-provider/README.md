# quark biolith provider

Extractor 1ee9b51 captures 26 selected classes. Independent r1
extraction matches every generated file byte for byte.
Manifest SHA-256: c8990b7cdc842caf2f85e84e28ecdb16d1b72dfc6ab51f43150d14c761c49d0f.

```sh
uv run -m tools.inspect_item8_pool_elements --archive Quark-4.1-480.jar --nested-archive META-INF/jarjar/biolith-neoforge-3.0.10.jar --class-name com/terraformersmc/biolith/api/biome/BiomePlacement.class --class-name com/terraformersmc/biolith/api/surface/SurfaceGeneration.class --class-name com/terraformersmc/biolith/impl/Biolith.class --class-name com/terraformersmc/biolith/impl/BiolithInit.class --class-name com/terraformersmc/biolith/impl/commands/BiolithCommands.class --class-name com/terraformersmc/biolith/impl/compat/BiolithCompat.class --class-name com/terraformersmc/biolith/impl/data/BiomePlacementLoader.class --class-name com/terraformersmc/biolith/impl/data/SurfaceGenerationLoader.class --class-name com/terraformersmc/biolith/impl/mixin/BiolithNeoForgeMixinConfigPlugin.class --class-name com/terraformersmc/biolith/impl/mixin/MixinBiomeSource.class --class-name com/terraformersmc/biolith/impl/mixin/MixinChunkGenerator.class --class-name com/terraformersmc/biolith/impl/mixin/MixinChunkGeneratorSettings.class --class-name com/terraformersmc/biolith/impl/mixin/MixinDataPackContents.class --class-name com/terraformersmc/biolith/impl/mixin/MixinDimensionOptions.class --class-name com/terraformersmc/biolith/impl/mixin/MixinMBBiomeSource.class --class-name com/terraformersmc/biolith/impl/mixin/MixinMinecraftServer.class --class-name com/terraformersmc/biolith/impl/mixin/MixinMultiNoiseBiomeSource.class --class-name com/terraformersmc/biolith/impl/mixin/MixinPlacedFeatureIndexer.class --class-name com/terraformersmc/biolith/impl/mixin/MixinSaveLoader.class --class-name com/terraformersmc/biolith/impl/mixin/MixinSearchTree.class --class-name com/terraformersmc/biolith/impl/mixin/MixinServerWorld.class --class-name com/terraformersmc/biolith/impl/mixin/MixinSurfaceBuilder.class --class-name com/terraformersmc/biolith/impl/mixin/MixinTBTheEndBiomeSource.class --class-name com/terraformersmc/biolith/impl/mixin/MixinTheEndBiomeSource.class --class-name com/terraformersmc/biolith/impl/platform/NeoForgePlatformHelper.class --class-name com/terraformersmc/biolith/impl/platform/services/PlatformHelper.class --output evidence/raw/item8/quark-biolith-provider-r1
```

Bundled Biolith initializes biome/surface services, criteria and commands. Its
loaders read biolith/biome_placement.json and biolith/surface_generation.json
resources and apply supplied biome and surface rules before server startup.
The captured public APIs accept consumer-provided biome/surface inputs. Mixins
connect biome selection, feature indexing, world/server lifecycle and surface
building, including optional biome-source integrations selected by the plugin.
This capture supports the remaining Quark provider reconciliation; it does not
prove successful biome placement or close all provider entry roles.
