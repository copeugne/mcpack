# Better Desert Temples provider entry paths

Extractor 92e7497 captures 27 entry, service, placement, mixin and state classes.
Reuse the three classes in desert-temple-suppression. The independent r1
extraction matches every generated file.
Manifest SHA-256: b64f030b80004ea67adeecadf91809f2f82e40526fa2fbe91905d9a2f53e66f2.

```sh
uv run -m tools.inspect_item8_pool_elements --archive YungsBetterDesertTemples-1.21.1-NeoForge-4.1.5.jar --class-name com/yungnickyoung/minecraft/betterdeserttemples/BetterDesertTemplesCommon.class --class-name com/yungnickyoung/minecraft/betterdeserttemples/BetterDesertTemplesNeoForge.class --class-name com/yungnickyoung/minecraft/betterdeserttemples/mixin/LocateVanillaPyramidCommandMixin.class --class-name com/yungnickyoung/minecraft/betterdeserttemples/mixin/ServerLevelMixin.class --class-name com/yungnickyoung/minecraft/betterdeserttemples/mixin/ServerPlayerTickMixin.class --class-name com/yungnickyoung/minecraft/betterdeserttemples/mixin/accessor/BoundingBoxAccessor.class --class-name com/yungnickyoung/minecraft/betterdeserttemples/mixin/accessor/ChunkGeneratorStructureStateAccessor.class --class-name com/yungnickyoung/minecraft/betterdeserttemples/mixin/accessor/StructureProcessorAccessor.class --class-name com/yungnickyoung/minecraft/betterdeserttemples/mixin/pharaoh/EntityMixin.class --class-name com/yungnickyoung/minecraft/betterdeserttemples/mixin/pharaoh/HuskMixin.class --class-name com/yungnickyoung/minecraft/betterdeserttemples/mixin/pharaoh/LivingEntityMixin.class --class-name com/yungnickyoung/minecraft/betterdeserttemples/mixin/pharaoh/ZombieMixin.class --class-name com/yungnickyoung/minecraft/betterdeserttemples/module/StructurePlacementTypeModule.class --class-name com/yungnickyoung/minecraft/betterdeserttemples/module/StructureProcessorModule.class --class-name com/yungnickyoung/minecraft/betterdeserttemples/module/TagModule.class --class-name com/yungnickyoung/minecraft/betterdeserttemples/services/IModulesLoader.class --class-name com/yungnickyoung/minecraft/betterdeserttemples/services/IPlatformHelper.class --class-name com/yungnickyoung/minecraft/betterdeserttemples/services/IProcessorProvider.class --class-name com/yungnickyoung/minecraft/betterdeserttemples/services/NeoForgeModulesLoader.class --class-name com/yungnickyoung/minecraft/betterdeserttemples/services/NeoForgePlatformHelper.class --class-name com/yungnickyoung/minecraft/betterdeserttemples/services/NeoForgeProcessorProvider.class --class-name com/yungnickyoung/minecraft/betterdeserttemples/services/Services.class --class-name com/yungnickyoung/minecraft/betterdeserttemples/util/PharaohUtil.class --class-name com/yungnickyoung/minecraft/betterdeserttemples/world/placement/BetterDesertTemplePlacement.class --class-name com/yungnickyoung/minecraft/betterdeserttemples/world/state/ITempleStateCacheProvider.class --class-name com/yungnickyoung/minecraft/betterdeserttemples/world/state/TempleStateCache.class --class-name com/yungnickyoung/minecraft/betterdeserttemples/world/state/TempleStateRegion.class --output evidence/raw/item8/desert-temple-provider-r1
```

Common initialization scans the module package through YUNG API; NeoForge loads
the existing configuration module. The module-loader default is empty. Three
services select module, platform and processor providers. The processor service
exposes armor-stand, item-frame and Pharaoh codecs alongside the module's other
23 component codecs. Detailed processor effects remain later attribute work.

Custom placement extends random-spread selection with biome search for the
existing temple. Accessors expose biome source, bounding-box and processor
operations. The locate hook handles the suppressed vanilla pyramid query.

The server-level mixin attaches dimension-local temple state. Player ticking
uses survival/configuration, loaded valid tagged temple and uncleared-state
conditions for mining fatigue. The tag names the existing temple root.
Pharaoh identity requires a Husk and the packaged head-texture marker. Death and
discard hooks clear the existing temple selected from stored original position,
or attempt current-position lookup if that position is absent. The utility also
handles sound and mining-fatigue removal. Zombie/Husk hooks preserve the original
spawn position. State cache/region classes persist cleared-state values; they do
not generate structures. Preserve the exact source predicates separately from
runtime behavior acceptance. The texture marker is packaged content, not player
data acquired from a server.

This capture supports provider reconciliation, not complete family attributes
or final Item 8 acceptance. No new runtime measurement was added.
