# Better Dungeons provider entries

Extractor 96a45c2 captures sixteen remaining entry, registration and context
classes. Existing betterdungeons-code preserves the seven specialized generator
classes. Independent r1 extraction matches every generated file.
Manifest SHA-256: a5b208a65d4a97e7fb79d6a1211cc90517c7a5dce8d03bfe5c697bdc0392718f.

```sh
uv run -m tools.inspect_item8_pool_elements --archive YungsBetterDungeons-1.21.1-NeoForge-5.1.4.jar --class-name com/yungnickyoung/minecraft/betterdungeons/BetterDungeonsCommon.class --class-name com/yungnickyoung/minecraft/betterdungeons/BetterDungeonsNeoForge.class --class-name com/yungnickyoung/minecraft/betterdungeons/mixin/DungeonContextMixin.class --class-name com/yungnickyoung/minecraft/betterdungeons/mixin/LocateSmallNetherDungeonCommandMixin.class --class-name com/yungnickyoung/minecraft/betterdungeons/mixin/accessor/BoundingBoxAccessor.class --class-name com/yungnickyoung/minecraft/betterdungeons/module/ConfigModuleNeoForge.class --class-name com/yungnickyoung/minecraft/betterdungeons/module/StructurePieceTypeModule.class --class-name com/yungnickyoung/minecraft/betterdungeons/module/StructureProcessorTypeModule.class --class-name com/yungnickyoung/minecraft/betterdungeons/module/StructureTypeModule.class --class-name com/yungnickyoung/minecraft/betterdungeons/services/IModulesLoader.class --class-name com/yungnickyoung/minecraft/betterdungeons/services/IPlatformHelper.class --class-name com/yungnickyoung/minecraft/betterdungeons/services/NeoForgeModulesLoader.class --class-name com/yungnickyoung/minecraft/betterdungeons/services/NeoForgePlatformHelper.class --class-name com/yungnickyoung/minecraft/betterdungeons/services/Services.class --class-name com/yungnickyoung/minecraft/betterdungeons/world/DungeonContext.class --class-name com/yungnickyoung/minecraft/betterdungeons/world/DungeonType.class --output evidence/raw/item8/dungeons-provider-r1
```

Common initialization scans the module package with YUNG API and loads services.
NeoForge initialization registers the configuration loader. The module service
calls an empty default. Configuration events/world loading bind the eleven
existing settings to configuration fields; they do not add another generation
registration. Effective attribute values remain separate work.

Structure registration supplies spider and small-Nether types, both already
represented in the packaged/runtime root list. Four piece types are spider
components. The processor module supplies 29 component codecs; their detailed
block, loot and encounter effects remain attribute inputs rather than additional
family entries.

DungeonContextMixin initializes thread-local banner/chest counters at the start
of StructureTemplate.placeInWorld. DungeonType enumerates six mob-theme labels,
not six independently registered structure families. The locate mixin rejects
the exact small-Nether root query when its enabled field is false. Bounding-box
accessors expose coordinates. These hooks affect existing component placement
and discovery, not additional independent designs.

Provider payload/root/component accounting is still required before closure.
This capture does not establish successful generation, effective configuration
values or complete Item 8 attributes.
