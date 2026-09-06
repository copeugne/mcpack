# Better Caves generation entries

Extractor 6d88d16 captures 23 entry, carver, layer, context and mixin classes.
Independent r1 extraction matches every generated file.
Manifest SHA-256: 8edcd258cbb0e0133a0595cc6da3eade478e5ab662c246ab441469442f9af988.

```sh
uv run -m tools.inspect_item8_pool_elements --archive YungsBetterCaves-1.21.1-NeoForge-3.1.4.jar --class-name com/yungnickyoung/minecraft/bettercaves/BetterCavesCommon.class --class-name com/yungnickyoung/minecraft/bettercaves/BetterCavesNeoForge.class --class-name com/yungnickyoung/minecraft/bettercaves/mixin/ChunkStatusTasksMixin.class --class-name com/yungnickyoung/minecraft/bettercaves/mixin/ServerLevelMixin.class --class-name com/yungnickyoung/minecraft/bettercaves/mixin/accessor/StructureManagerAccessor.class --class-name com/yungnickyoung/minecraft/bettercaves/mixin/aquiferfix/AquiferMixin.class --class-name com/yungnickyoung/minecraft/bettercaves/mixin/aquiferfix/ChunkStatusTasksMixin.class --class-name com/yungnickyoung/minecraft/bettercaves/mixin/aquiferfix/ChunkStepMixin.class --class-name com/yungnickyoung/minecraft/bettercaves/mixin/aquiferfix/NoiseBasedChunkGeneratorMixin.class --class-name com/yungnickyoung/minecraft/bettercaves/module/CarverModuleNeoForge.class --class-name com/yungnickyoung/minecraft/bettercaves/module/ConfigModuleNeoForge.class --class-name com/yungnickyoung/minecraft/bettercaves/services/IPlatformHelper.class --class-name com/yungnickyoung/minecraft/bettercaves/services/NeoForgePlatformHelper.class --class-name com/yungnickyoung/minecraft/bettercaves/services/Services.class --class-name com/yungnickyoung/minecraft/bettercaves/worldgen/BetterCavesWorldCarver.class --class-name com/yungnickyoung/minecraft/bettercaves/worldgen/carver/AbstractCarver.class --class-name com/yungnickyoung/minecraft/bettercaves/worldgen/carver/CaveCarver.class --class-name com/yungnickyoung/minecraft/bettercaves/worldgen/carver/CavernCarver.class --class-name com/yungnickyoung/minecraft/bettercaves/worldgen/context/AquiferContext.class --class-name com/yungnickyoung/minecraft/bettercaves/worldgen/context/CavegenContext.class --class-name com/yungnickyoung/minecraft/bettercaves/worldgen/controller/MasterController.class --class-name com/yungnickyoung/minecraft/bettercaves/worldgen/layer/CaveLayer.class --class-name com/yungnickyoung/minecraft/bettercaves/worldgen/layer/CavernLayer.class --output evidence/raw/item8/better-caves-provider-r1
```

The NeoForge entry registers a single custom WorldCarver, better_cave, and loads
configuration. The common entry scans the module package through YUNG API.
The world carver obtains its server context and invokes a cached MasterController;
the controller dispatches cave/cavern layers, which sample noise and call the
column carvers. AbstractCarver writes carving states and schedules fluid
postprocessing. Debug block materials visualize carving, not authored buildings.

Seven mixins attach server/carving context, expose the level, manage aquifer
context and substitute configured liquid-region results in aquifer processing.
These affect terrain generation. They do not register structure roots or assemble
independent authored content. Configuration loading reads liquidregions.json for
dimension-level liquid-region settings. Preserve its error/default behavior and
all source predicates without claiming runtime equivalence or performance.

This capture supports bounded provider reconciliation, not a rerun of Item 7,
an acceptance of every worldgen interaction or complete Item 8 attributes.
