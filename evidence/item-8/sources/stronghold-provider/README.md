# Better Strongholds provider consumers

Extractor fee4d62 captures the 31 classes not in stronghold-suppression. The two
captures cover all 32 packaged classes. An independent r1 extraction reproduced
all generated files byte for byte before this README was added.
Archive SHA-256:
a9cab2fc01538368862365691f7d215309801aed0b390351681b6b60a1db7b58.
Manifest SHA-256:
3a72121dbd2da8c4b5cc66a419c0f03e0fefc7f329542cb9750e94cbae707a72.

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive YungsBetterStrongholds-1.21.1-NeoForge-5.1.3.jar \
  --class-name com/yungnickyoung/minecraft/betterstrongholds/BetterStrongholdsCommon.class \
  --class-name com/yungnickyoung/minecraft/betterstrongholds/BetterStrongholdsNeoForge.class \
  --class-name com/yungnickyoung/minecraft/betterstrongholds/config/BSConfigNeoForge.class \
  --class-name com/yungnickyoung/minecraft/betterstrongholds/config/ConfigGeneralNeoForge.class \
  --class-name com/yungnickyoung/minecraft/betterstrongholds/mixin/LocateStrongholdCommandMixin.class \
  --class-name 'com/yungnickyoung/minecraft/betterstrongholds/module/ConfigModule$General.class' \
  --class-name com/yungnickyoung/minecraft/betterstrongholds/module/ConfigModule.class \
  --class-name com/yungnickyoung/minecraft/betterstrongholds/module/ConfigModuleNeoForge.class \
  --class-name com/yungnickyoung/minecraft/betterstrongholds/module/StructurePlacementTypeModule.class \
  --class-name com/yungnickyoung/minecraft/betterstrongholds/module/StructureProcessorTypeModule.class \
  --class-name com/yungnickyoung/minecraft/betterstrongholds/services/IModulesLoader.class \
  --class-name com/yungnickyoung/minecraft/betterstrongholds/services/IPlatformHelper.class \
  --class-name com/yungnickyoung/minecraft/betterstrongholds/services/IProcessorProvider.class \
  --class-name com/yungnickyoung/minecraft/betterstrongholds/services/NeoForgeModulesLoader.class \
  --class-name com/yungnickyoung/minecraft/betterstrongholds/services/NeoForgePlatformHelper.class \
  --class-name com/yungnickyoung/minecraft/betterstrongholds/services/NeoForgeProcessorProvider.class \
  --class-name com/yungnickyoung/minecraft/betterstrongholds/services/Services.class \
  --class-name com/yungnickyoung/minecraft/betterstrongholds/world/ArmorStandChances.class \
  --class-name com/yungnickyoung/minecraft/betterstrongholds/world/ItemFrameChances.class \
  --class-name com/yungnickyoung/minecraft/betterstrongholds/world/OreChances.class \
  --class-name com/yungnickyoung/minecraft/betterstrongholds/world/RareBlockChances.class \
  --class-name com/yungnickyoung/minecraft/betterstrongholds/world/placement/BetterStrongholdsPlacement.class \
  --class-name com/yungnickyoung/minecraft/betterstrongholds/world/processor/ArmorStandProcessor.class \
  --class-name com/yungnickyoung/minecraft/betterstrongholds/world/processor/BannerProcessor.class \
  --class-name com/yungnickyoung/minecraft/betterstrongholds/world/processor/EndPortalFrameProcessor.class \
  --class-name com/yungnickyoung/minecraft/betterstrongholds/world/processor/ItemFrameProcessor.class \
  --class-name com/yungnickyoung/minecraft/betterstrongholds/world/processor/LegProcessor.class \
  --class-name com/yungnickyoung/minecraft/betterstrongholds/world/processor/OreProcessor.class \
  --class-name com/yungnickyoung/minecraft/betterstrongholds/world/processor/RareBlockProcessor.class \
  --class-name com/yungnickyoung/minecraft/betterstrongholds/world/processor/RedstoneProcessor.class \
  --class-name com/yungnickyoung/minecraft/betterstrongholds/world/processor/RuinProcessor.class \
  --output evidence/raw/item8/stronghold-provider-r1
```

The capture preserves common/NeoForge initialization, configuration, annotated
placement/processor modules, three service interfaces and their NeoForge
implementations, custom placement and the nine component processors with their
four item/block selection consumers. Reuse the prior vanilla suppression source.

BetterStrongholdsPlacement extends RandomSpreadStructurePlacement. It first
requires the candidate chunk selected by the inherited random-spread calculation,
then applies its radial section check using chunk_distance_to_first_ring,
ring_chunk_thickness and optional max_ring_section. Its packaged structure set
names only betterstrongholds:stronghold. Preserve the exact integer operations;
this source is not an empirical density or exploration-pacing measurement.

Armor stands and item frames are existing-template entity consumers. Their
processors rewrite item/equipment NBT using the captured selection tables.
Other processors modify banner data, end-portal frames, support legs, ore/rare
block markers, redstone and ruined blocks. Shared YUNG API randomizers and banner
building remain separate provider dependencies. None of these component paths
introduces another independent root. Preserve support writes outside template
bounds and written item NBT for later effective size/content attribution.

The direct locate mixin and configuration source complement existing suppression
evidence. Provider closure still requires the root/pool/template partition and
entry/service reconciliation. This capture alone is not gameplay acceptance or
Item 8 completion.
