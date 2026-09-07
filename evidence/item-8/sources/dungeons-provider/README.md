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

## Small Nether Dungeon inactive disposition

The two-family small-dungeon assessment batch initially contained20 attributes
and99 reachable templates:16 Small Dungeon and83 Small Nether Dungeon. Inspecting
frozen enablement first resolves the latter as inactive, without assessing the
83 inactive component templates or changing the baseline. This is a denominator
correction, not a completed active assessment:448 active families,355 assessed,
93 remaining. Registry groups remain426:408 active,17 inactive,one excluded;
all887 runtime roots remain assigned exactly once. Forty nonregistry families
remain assessed. Small Dungeon still needs its ten attributes.

Frozen config/betterdungeons-neoforge-1_21.toml, Small Nether Dungeons section,
sets Enable Small Nether Dungeons=false. Direct immutable archive inspection:
YungsBetterDungeons-1.21.1-NeoForge-5.1.4.jar SHA-256
61816c3b7c9d92c6b44f93dce87ceb0a22827f20285d5d9c4d10d519d734de04,
member com/yungnickyoung/minecraft/betterdungeons/config/ConfigSmallNetherDungeonsNeoForge.class
SHA-2564c003a33419279dc99568d133a0d633f4964cc1429dfdd176438cc18bab48d92.
Its constructor offsets26..32 defines that exact key with false default and
stores enabled. Preserved ConfigModuleNeoForge offsets171..189 reads this
ConfigValue into CONFIG.smallNetherDungeons.enabled. Preserved
SmallNetherDungeonStructure.findGenerationPoint offsets0..15 checks the field
and returns Optional.empty when false, before any assembly. These sources,
configuration and precise member identity are bound in the authoritative decision.

The existing locate mixin also rejects this disabled root, but is not the basis
for claiming generation is disabled. Preserve the root, pools and83 templates.
This disposition concerns normal generation in the frozen stack, not modified
configuration or pre-existing worlds. No new runtime or tooling is needed.

Direct inspection command (pinned javap, exact hash-verified archive):

```sh
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -p -c -classpath downloads/item3/candidates/YungsBetterDungeons-1.21.1-NeoForge-5.1.4.jar com.yungnickyoung.minecraft.betterdungeons.config.ConfigSmallNetherDungeonsNeoForge
uv run -m tools.build_item8_inventory --output evidence/raw/item8/small-nether-inactive-inventory.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

The inventory comparison changes only the inactive family's disposition/evidence
and corresponding input identity. No root membership or component trace changes.

All85 focused tests passed. Small Dungeon remains unassessed; do not count this
inactive disposition as completing an active family.
