# Better Ocean Monuments provider consumers

Extractor 2cabf38 captures 25 classes in addition to the three already preserved
in monument-suppression. The two captures cover all 28 packaged classes. The
independent r1 capture reproduced generated files byte for byte before this README.
Archive SHA-256:
cdcf8fe0e08c75261048d43c6ed4898972d23e096dd04a2524c136f06416ab02.
Manifest SHA-256:
8eea5e78334604ab4ff0f9e02bdf127030a4a5bc07a418bc9461ff835c03bab2.

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive YungsBetterOceanMonuments-1.21.1-NeoForge-4.1.2.jar \
  --class-name com/yungnickyoung/minecraft/betteroceanmonuments/BetterOceanMonumentsCommon.class \
  --class-name com/yungnickyoung/minecraft/betteroceanmonuments/BetterOceanMonumentsNeoForge.class \
  --class-name com/yungnickyoung/minecraft/betteroceanmonuments/config/BOMConfigForge.class \
  --class-name com/yungnickyoung/minecraft/betteroceanmonuments/mixin/LocateVanillaMonumentCommandMixin.class \
  --class-name com/yungnickyoung/minecraft/betteroceanmonuments/mixin/PersistentTridentMixin.class \
  --class-name com/yungnickyoung/minecraft/betteroceanmonuments/mixin/accessor/ProjectileAccessor.class \
  --class-name 'com/yungnickyoung/minecraft/betteroceanmonuments/module/ConfigModule$General.class' \
  --class-name com/yungnickyoung/minecraft/betteroceanmonuments/module/ConfigModule.class \
  --class-name com/yungnickyoung/minecraft/betteroceanmonuments/module/StructureProcessorTypeModule.class \
  --class-name com/yungnickyoung/minecraft/betteroceanmonuments/module/TagModule.class \
  --class-name com/yungnickyoung/minecraft/betteroceanmonuments/services/IModulesLoader.class \
  --class-name com/yungnickyoung/minecraft/betteroceanmonuments/services/IPlatformHelper.class \
  --class-name com/yungnickyoung/minecraft/betteroceanmonuments/services/NeoForgeModulesLoader.class \
  --class-name com/yungnickyoung/minecraft/betteroceanmonuments/services/NeoForgePlatformHelper.class \
  --class-name com/yungnickyoung/minecraft/betteroceanmonuments/services/Services.class \
  --class-name com/yungnickyoung/minecraft/betteroceanmonuments/world/processor/AirProcessor.class \
  --class-name com/yungnickyoung/minecraft/betteroceanmonuments/world/processor/LegProcessor.class \
  --class-name com/yungnickyoung/minecraft/betteroceanmonuments/world/processor/RandomDarkPrismarineSlabDecorationProcessor.class \
  --class-name com/yungnickyoung/minecraft/betteroceanmonuments/world/processor/RandomOxidizationProcessor.class \
  --class-name com/yungnickyoung/minecraft/betteroceanmonuments/world/processor/RandomPrismarineSlabDecorationProcessor.class \
  --class-name com/yungnickyoung/minecraft/betteroceanmonuments/world/processor/RandomSpongeProcessor.class \
  --class-name com/yungnickyoung/minecraft/betteroceanmonuments/world/processor/SandGravelProcessor.class \
  --class-name com/yungnickyoung/minecraft/betteroceanmonuments/world/processor/SeagrassProcessor.class \
  --class-name com/yungnickyoung/minecraft/betteroceanmonuments/world/processor/StructureVoidProcessor.class \
  --class-name com/yungnickyoung/minecraft/betteroceanmonuments/world/processor/WaterlogProcessor.class \
  --output evidence/raw/item8/ocean-monument-provider-r1
```

The package preserves the NeoForge entry, common initialization, configuration,
module registration, service providers, structure tag, two remaining mixin hooks,
and ten block processors. The modules service default is empty. Shared YUNG API
registration remains a separate provider dependency; reuse the prior vanilla
suppression and frozen configuration captures.

All ten processors consume existing template blocks. Their roles cover sea-level
air/water treatment, waterlogging/postprocessing, support legs, prismarine slab
ornament variation, copper oxidation variation, sponge variation, gravel markers,
seagrass markers and preserving world blocks at structure-void markers. LegProcessor
writes prismarine-brick supports down from blue stained-glass markers. Preserve
its direct writes outside template bounds for later vertical-size attribution.
None registers an independent authored root or consumes an extra template family.

PersistentTridentMixin checks a server-side thrown trident, the exact packaged
owner-marker constant and a valid piece in the better_ocean_monuments tag before
cancelling the despawn callback. ProjectileAccessor reads that owner field. The
constant is authored JAR code, not a captured player's identity. The packaged tag
contains the existing ocean_monument root. This is not a general guarantee for
all tridents or a runtime gameplay acceptance claim. LocateVanillaMonumentCommandMixin
handles the direct vanilla locate request; reuse the existing suppression proof.

Provider closure also requires the preserved root/pool/template partition. This
capture alone does not complete family attributes or Item 8.
