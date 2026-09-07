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

## Small Dungeon assessment

Scope: one active family, ten attributes, sixteen reachable templates. Reuse
existing packaged JSON, templates, world-bounds and frozen configuration. No
missing traced components. All139 effective biomes intersect only Overworld;
no unresolved or missing required tags. The root has empty spawn_overrides,
underground_structures, absolute anchorY-50..50 and no surface-heightmap projection.
This describes a concealed cave/excavation room, not a surface landmark or a
measured human discovery distance.

Six rigid small_dungeon/shells/small_shell variants5x5,7x5,7x7,9x5,9x7,9x9
have actual XYZ sizes7x7x7,9x7x7,9x7x9,11x7x7,11x7x9,11x7x11.
Each has four internal horizontal loot-pile connectors atY1, with sufficient
inset for at-most2x2x2 pieces; empty pile is1x1x1. These remain in the shell
footprint. Nominal height is7, with variable downward supports described below.
World-bounds full-start indexes174/268/273 (repeat571/657/662) corroborate
11x7x7,11x7x11,11x7x9. Index174 is mountainous chunk5,0 at run-a line13347;
268 is ocean-heavy chunk26,-13 at line12632;273 is ocean-heavy chunk27,0 at
line13369. Non-full indexes259/288/293 and repeats remain excluded from this
corroboration. No new capture or estimate of frequency/extrema is needed.

Each shell's palette/state_counts records exactly one ordinary spawner. Lack
of saved spawner NBT is not absence of a spawner block. The start pool has each
size with skeleton/spider/zombie processor themes weighted1/1/2. MobSpawnerProcessor
processBlock offsets0..109 identifies SpawnerBlock, builds singleton spawn
potentials and sets the selected entity, returning new spawner data. Its lambda
writes the spawner_mob resource ID. These are authored assignments; ambient
spawns remain conditional. All16 templates have no direct saved entities.

Shell chest NBT uses minecraft:chests/simple_dungeon. Loot-pile1 block_entities
1/2/3, pile3 index2 and pile5 index1 use betterdungeons:small_dungeon/chests/loot_piles
in barrels. No nonempty fixed Items lists exist in these templates. The empty
pile has weight7/max_count2; each other pile weight1/max_count1. These YUNG
single-element limits are component selection rules, not encounter measurements.

SmallDungeonChestProcessor.processBlock offsets14..138 uses DungeonContext
count: below minimum preserve/increment; at maximum replace with cave_air;
between limits preserve/increment only when nextFloat<=0.2. Frozen minimum1,
maximum2 are source controls, not guaranteed observed final totals across chunk
placement. Existing DungeonContextMixin resets context at template placement.
SmallDungeonOreProcessor gates ore-tagged props on enableOreProps; frozen Allow
Ore Blocks in Corners=true preserves this salvage source, separate from table loot.

Direct immutable archive inspection used pinned javap on the same
YungsBetterDungeons-1.21.1-NeoForge-5.1.4.jar SHA-256 recorded above. The eight
exact class member hashes are in family-decisions.json processor_inspection:
MobSpawnerProcessor and small_dungeon SmallDungeonChestProcessor,LegProcessor,
CeilingProcessor,CeilingLampPropProcessor,CeilingPropProcessor,OreProcessor,
CobblestoneProcessor (each name includes SmallDungeon prefix where applicable).
LegProcessor.processBlock offsets86..207 extends yellow-marker support columns
down through air/fluid until solid terrain/build limits, at unchanged X/Z.
CeilingProcessor treats orange markers using existing terrain or cobblestone
for water/lava. Ceiling props/lamp processors choose chain or cave_air based
on support/randomness at their template position; CobblestoneProcessor responds
to the existing terrain. Thus seven-block nominal room height excludes downward
support extension; it is not fixed total occupied height.

Reproduce direct class inspection with the exact dotted member name from
processor_inspection.members (remove .class and replace slashes with dots):

```sh
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -p -c -classpath downloads/item3/candidates/YungsBetterDungeons-1.21.1-NeoForge-5.1.4.jar com.yungnickyoung.minecraft.betterdungeons.world.processor.MobSpawnerProcessor
uv run -m tools.build_item8_inventory --output evidence/raw/item8/small-dungeon-assessed-inventory.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

All ten attributes enter the authoritative inventory; semantic comparison changes
only Small Dungeon and the input identity. No new tooling or raw evidence class.

All85 focused tests passed. Total356/448 active families assessed,92 remaining.
This completes Small Dungeon attribution, not the final Item8 gate.

## Skeleton Dungeon assessment

Batch initially quantified Skeleton and Zombie Dungeon together:20 attributes,
58 and69 traced templates respectively. Skeleton is now assessed; Zombie's ten
attributes remain, with no retained world-bounds start and missing
betterdungeons:zombie_dungeon/big_stairs_crumbled_0 preserved. No missing
component was reported for Skeleton. No new measurement was needed for Skeleton.

Skeleton's139 effective biomes intersect only the captured Overworld, with no
missing/unresolved biome tags. Its root uses underground_structures, absolute
anchorY-50..-30, no surface heightmap projection and piece-bounded monster override
skeleton weight100,min4,max15. The58 templates have no direct saved entities or
nonempty fixed Items. Their two loot-table references are
betterdungeons:skeleton_dungeon/chests/common and chests/middle. This is source
attribution, not measured reward quantities or enemy counts.

Ordinary spawners occur once in each of ten selected component templates:
bridges/bridge_big_0 and bridge_big_2; stair1/stair1_0..3; stair2/stair2_1,2,3,5.
Paths are under betterdungeons:skeleton_dungeon/. Palette/state_counts and NBT
agree. These alternatives are not ten spawners in every dungeon. Raw pig NBT
is replaced by SkeletonMobSpawnerProcessor.processBlock offsets14..108:
skeleton singleton SpawnPotentials, requiredPlayerRange18,maxNearbyEntities8,
maxSpawnDelay650 and EntityType.SKELETON. Its lambda writes minecraft:skeleton.
Authored spawners and the separate natural override both remain explicit.

World-bounds index277 (repeat666) is a full-start example at ocean-heavy seed
95920844204830198, chunk27,5. Source run-a/ocean-heavy/chunks.jsonl line13529.
Envelope[417,-47,65,447,-35,95] gives31x13x31 inclusive saved-piece size.
This illustrative example is not family-wide extrema or occupied volume.
SkeletonDungeonLegProcessor uses blue glass markers and extends cobble support
columns downward through air/fluid until solid terrain/build limits. Record
that variable extension separately;13 is saved-piece height, not total occupied
height. RuinedStoneBrickProcessor varies/removes yellow-glass/prismarine-brick-slab markers according
to existing air and material selection at their original position. Underground
stairs/bridges may be exposed in caves; no measured surface visibility is claimed.

Exact archive and three class-member hashes are in processor_inspection in the
family decision. Direct inspection used pinned javap on the immutable retained
archive. An initial guessed ruined-brick class name failed; inspecting the archive
member list resolved the actual name RuinedStoneBrickProcessor. That failed
inspection changed no evidence. Reproduce each exact dotted member name with:

```sh
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -p -c -classpath downloads/item3/candidates/YungsBetterDungeons-1.21.1-NeoForge-5.1.4.jar com.yungnickyoung.minecraft.betterdungeons.world.processor.skeleton_dungeon.SkeletonMobSpawnerProcessor
uv run -m tools.build_item8_inventory --output evidence/raw/item8/skeleton-dungeon-assessed-inventory.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

All ten attributes enter the authoritative inventory. Semantic comparison changes
only Skeleton Dungeon and input identity. No new tooling or raw evidence class.

All85 focused tests passed. Total357/448 assessed,91 remaining. Zombie Dungeon
is not yet assessed; its ten attributes remain within this two-family batch.
