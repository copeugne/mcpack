# Better Nether Fortresses provider consumers

Extractor 7d02f76 captures 23 classes not present in fortress-suppression. Together
the two captures cover all 26 packaged classes. An independent r1 extraction
reproduced the generated files byte for byte before this README was added.
Archive SHA-256:
5450a64a7036237f449496837e08f3e5b3aa1d7974a10df43944172def75d8ff.
Manifest SHA-256:
3dfe3d5fc9c799adcff26bc710001126477a9f8d712b227bed501f3612835598.

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive YungsBetterNetherFortresses-1.21.1-NeoForge-3.1.5.jar \
  --class-name com/yungnickyoung/minecraft/betterfortresses/BetterFortressesCommon.class \
  --class-name com/yungnickyoung/minecraft/betterfortresses/BetterFortressesNeoForge.class \
  --class-name com/yungnickyoung/minecraft/betterfortresses/config/BNFConfigNeoForge.class \
  --class-name com/yungnickyoung/minecraft/betterfortresses/mixin/FixMobSpawningMixin.class \
  --class-name com/yungnickyoung/minecraft/betterfortresses/mixin/LocateVanillaFortressCommandMixin.class \
  --class-name 'com/yungnickyoung/minecraft/betterfortresses/module/ConfigModule$General.class' \
  --class-name com/yungnickyoung/minecraft/betterfortresses/module/ConfigModule.class \
  --class-name com/yungnickyoung/minecraft/betterfortresses/module/StructureProcessorTypeModule.class \
  --class-name com/yungnickyoung/minecraft/betterfortresses/services/IModulesLoader.class \
  --class-name com/yungnickyoung/minecraft/betterfortresses/services/IPlatformHelper.class \
  --class-name com/yungnickyoung/minecraft/betterfortresses/services/IProcessorProvider.class \
  --class-name com/yungnickyoung/minecraft/betterfortresses/services/NeoForgeModulesLoader.class \
  --class-name com/yungnickyoung/minecraft/betterfortresses/services/NeoForgePlatformHelper.class \
  --class-name com/yungnickyoung/minecraft/betterfortresses/services/NeoForgeProcessorProvider.class \
  --class-name com/yungnickyoung/minecraft/betterfortresses/services/Services.class \
  --class-name com/yungnickyoung/minecraft/betterfortresses/world/ItemFrameChances.class \
  --class-name com/yungnickyoung/minecraft/betterfortresses/world/ItemFrameProcessor.class \
  --class-name com/yungnickyoung/minecraft/betterfortresses/world/processor/BridgeArchProcessor.class \
  --class-name com/yungnickyoung/minecraft/betterfortresses/world/processor/LiquidBlockProcessor.class \
  --class-name com/yungnickyoung/minecraft/betterfortresses/world/processor/NetherWartProcessor.class \
  --class-name com/yungnickyoung/minecraft/betterfortresses/world/processor/PillarProcessor.class \
  --class-name com/yungnickyoung/minecraft/betterfortresses/world/processor/RedSandstoneStairsProcessor.class \
  --class-name com/yungnickyoung/minecraft/betterfortresses/world/processor/StairPillarProcessor.class \
  --output evidence/raw/item8/fortress-provider-r1
```

The common entry scans the module package for YUNG API registration annotations
and calls the modules service. NeoForgeModulesLoader delegates to an empty
default. NeoForgePlatformHelper supplies platform/loader lookups, while
NeoForgeProcessorProvider exposes the captured ItemFrameProcessor codec.
NeoForge initialization also invokes the already captured configuration loader.

The remaining processors are component consumers: bridge-arch block placement,
liquid-marker replacement/tick scheduling, nether-wart variation, configured
pillars, and red-sandstone/stair marker support construction. Direct block writes
and world-region/build-height checks remain in the exact source. ItemFrameProcessor
rewrites existing template entity NBT using ItemFrameChances and YUNG API item
randomizers. Preserve the written serialization separately from runtime item
acceptance. These classes do not introduce another independently registered root.

FixMobSpawningMixin sets the fortress-spawn check result true for the monster
category when nether bricks are below the tested position and a valid
betterfortresses:fortress start contains it. This is an existing-family spawn
input, not an independently placed encounter. Reuse the prior vanilla suppression
and frozen configuration evidence. LocateVanillaFortressCommandMixin handles the
direct vanilla locate request. Shared YUNG API behavior remains a separate open
provider input.

Root/component partition and the final provider disposition must accompany this
capture. Source capture alone is not runtime gameplay evidence or Item 8 closure.
