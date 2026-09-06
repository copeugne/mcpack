# Better Jungle Temples provider consumers

Extractor d1db0e4 captures 29 classes in addition to the three already in
jungle-temple-suppression. The captures cover all 32 packaged classes. An
independent r1 extraction reproduced every generated file before this README.
Archive SHA-256:
a0d57b78c7a1891796f342b1f09c214bc27bedf0a3a894f029dfdb2db9f813d0.
Manifest SHA-256:
c58f507bc5d0896b3f5fd6238d7ab9b3a79ce4ff4408417e896c041d6ce0c027.

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive YungsBetterJungleTemples-1.21.1-NeoForge-3.1.2.jar \
  --class-name com/yungnickyoung/minecraft/betterjungletemples/BetterJungleTemplesCommon.class \
  --class-name com/yungnickyoung/minecraft/betterjungletemples/BetterJungleTemplesNeoForge.class \
  --class-name com/yungnickyoung/minecraft/betterjungletemples/config/BJTConfigNeoForge.class \
  --class-name com/yungnickyoung/minecraft/betterjungletemples/mixin/LocateVanillaJungleTempleCommandMixin.class \
  --class-name com/yungnickyoung/minecraft/betterjungletemples/mixin/accessor/ChunkGeneratorStructureStateAccessor.class \
  --class-name com/yungnickyoung/minecraft/betterjungletemples/module/CompatModule.class \
  --class-name 'com/yungnickyoung/minecraft/betterjungletemples/module/ConfigModule$Compat.class' \
  --class-name 'com/yungnickyoung/minecraft/betterjungletemples/module/ConfigModule$General.class' \
  --class-name com/yungnickyoung/minecraft/betterjungletemples/module/ConfigModule.class \
  --class-name com/yungnickyoung/minecraft/betterjungletemples/module/StructurePlacementTypeModule.class \
  --class-name com/yungnickyoung/minecraft/betterjungletemples/module/StructureProcessorTypeModule.class \
  --class-name com/yungnickyoung/minecraft/betterjungletemples/module/TagModule.class \
  --class-name com/yungnickyoung/minecraft/betterjungletemples/services/IModulesLoader.class \
  --class-name com/yungnickyoung/minecraft/betterjungletemples/services/IPlatformHelper.class \
  --class-name com/yungnickyoung/minecraft/betterjungletemples/services/IProcessorProvider.class \
  --class-name com/yungnickyoung/minecraft/betterjungletemples/services/NeoForgeModulesLoader.class \
  --class-name com/yungnickyoung/minecraft/betterjungletemples/services/NeoForgePlatformHelper.class \
  --class-name com/yungnickyoung/minecraft/betterjungletemples/services/NeoForgeProcessorProvider.class \
  --class-name com/yungnickyoung/minecraft/betterjungletemples/services/Services.class \
  --class-name com/yungnickyoung/minecraft/betterjungletemples/world/placement/BetterJungleTemplePlacement.class \
  --class-name com/yungnickyoung/minecraft/betterjungletemples/world/processor/BlastFurnaceProcessor.class \
  --class-name com/yungnickyoung/minecraft/betterjungletemples/world/processor/BlockReplaceProcessor.class \
  --class-name com/yungnickyoung/minecraft/betterjungletemples/world/processor/CaveVineDecorationProcessor.class \
  --class-name com/yungnickyoung/minecraft/betterjungletemples/world/processor/EmptyDispenserProcessor.class \
  --class-name com/yungnickyoung/minecraft/betterjungletemples/world/processor/FireballDispenserProcessor.class \
  --class-name com/yungnickyoung/minecraft/betterjungletemples/world/processor/ItemFrameProcessor.class \
  --class-name com/yungnickyoung/minecraft/betterjungletemples/world/processor/PillarProcessor.class \
  --class-name com/yungnickyoung/minecraft/betterjungletemples/world/processor/TorchProcessor.class \
  --class-name com/yungnickyoung/minecraft/betterjungletemples/world/util/ArrowData.class \
  --output evidence/raw/item8/jungle-temple-provider-r1
```

The capture includes common/NeoForge initialization, configuration, module and
service registration, custom placement, eight component processors and ArrowData.
CompatModule.init and the IModulesLoader default have empty bodies. Reuse the
prior configuration/suppression evidence; shared YUNG API remains a separate
provider dependency.

BetterJungleTemplePlacement extends random-spread placement, accesses the biome
source for horizontal biome search, and supports an enhanced exclusion zone.
It places the existing temple root rather than introducing another design.
The exact lookup, exclusion and integer operations remain in source; this is not
an observed density or exploration-pacing measurement.

Component roles include configured block replacement and fluid ticks, pillar
support writes, vine/slab ornament variation, torch variation, blast-furnace
marker variation and dispenser trap contents. ArrowData supplies the arrow item
and component information for EmptyDispenserProcessor. FireballDispenserProcessor
turns orange-concrete markers into dispensers. Preserve written trap NBT separately
from effective runtime contents. ItemFrameProcessor only corrects TileX/TileY/TileZ
for existing item and glow-item frames; it does not randomize their loot.

Pillar writes can extend outside the template bounds and remain a later size
attribution input. None of these component paths adds another independent root.
Source capture must be accompanied by root/component accounting before provider
closure. This capture alone does not complete family attributes or Item 8.
