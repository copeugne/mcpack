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

## Effective spawners and placement

Batch: one family, ten required attributes,197 traced templates and no missing
components. Four attributes are now integrated: dimension, generated spawners,
visual discoverability and surface/underground classification. Six remain:
footprint, vertical size, intended hostility, mob source, loot source and
complete authored/natural-enemy attribution. The latter source assessments still
need Pharaoh/reward processor reconciliation. No new capture or tooling was
added for this increment; do not count the family fully assessed.

The exact archive YungsBetterDesertTemples-1.21.1-NeoForge-4.1.5.jar and four
processor class-member SHA-256 values are recorded in family-decisions.json
processor_inspection. Direct pinned-javap inspection establishes these conversions:

| Source block | Processor | Spawner entity | Explicit settings |
|---|---|---|---|
| gravel | GravelProcessor | husk | maxNearbyEntities8, requiredPlayerRange24 |
| bone_block | BoneBlockProcessor | skeleton | requiredPlayerRange32; empty HandItems in nextSpawnData |
| infested_cracked_stone_bricks | InfestedCrackedStoneBricksProcessor | silverfish | requiredPlayerRange24 |
| yellow_wool | YellowWoolProcessor | husk | maxNearbyEntities8, requiredPlayerRange24; equipment NBT in nextSpawnData |

Each processBlock matches the incoming block type, builds MobSpawnerData, saves
it and returns minecraft:spawner with that NBT. BoneBlockProcessor's HandItems
consumer has an empty body, so the written list is empty. YellowWoolProcessor
writes golden sword/shield and armor item data using uppercase Count and legacy
tag fields. Preserve that encoding without claiming effective worn equipment.
Do not infer additional builder defaults or realized populations from these
explicit source arguments.

Catalog references: templates-redacted.json.gz, exact archive above, paths under
`data/betterdeserttemples/structure/`. Palette indices joined to state_counts show:

- hall_room/parkour/parkour_bottom_2.nbt: two bone_block markers.
- hall_room/parkour/parkour_bottom_3.nbt: two infested_cracked_stone_bricks markers.
- hall_room/throne_room.nbt: four yellow_wool markers.
- puzzle_big/puzzle_big_2_{0,1,2,4}.nbt,
  puzzle_big/puzzle_big_7_{0,1,2,3,4,5}.nbt and rooms/room_tomb_{0,1,3}.nbt:
  one gravel marker in each of these13 alternatives.

All are in structures[betterdeserttemples:desert_temple].templates in the pinned
pool trace. The197 templates have no literal ordinary/trial spawner states or
spawner block entities. This is not evidence of absent generated spawners:
worldgen/processor_list/main.json invokes all four conversion classes. The
remaining block processors supply decoration, support, TNT, pots and archaeology
rather than another trial-spawner conversion. Component counts are not assembly
counts, and available alternatives are not guaranteed placements.

The packaged worldgen/structure/desert_temple.json projects temple_anchor onto
WORLD_SURFACE_WG with uniform offset-24..-4, step surface_structures and
ignore_waterlogging. Its three effective biomes intersect only the captured
Overworld, with no unresolved tag references. These establish source-relative
placement and a partly buried entrance/room design, not complete dimensions or
human visibility. Required complete geometry remains open; there is no accepted
full-start example. Existing catalog and dimension identities are pinned in the
family evidence map.

```sh
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -p -c \
  -classpath downloads/item3/candidates/YungsBetterDesertTemples-1.21.1-NeoForge-4.1.5.jar \
  com.yungnickyoung.minecraft.betterdeserttemples.world.processor.GravelProcessor \
  com.yungnickyoung.minecraft.betterdeserttemples.world.processor.BoneBlockProcessor \
  com.yungnickyoung.minecraft.betterdeserttemples.world.processor.InfestedCrackedStoneBricksProcessor \
  com.yungnickyoung.minecraft.betterdeserttemples.world.processor.YellowWoolProcessor
uv run -m tools.build_item8_inventory --output evidence/raw/item8/desert-spawner-placement-inventory.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

Next reuse the existing Pharaoh state/mixin evidence and directly inspect the
Pharaoh, frame, armor-stand, pot and archaeology processor paths for the remaining
four content attributes. Inspect connected layout before declaring the smallest
necessary geometry capture for the two size attributes. No optional live reward,
combat population or blind-client measurement is added to Item8.

## Pharaoh and reward attribution

Four additional required content attributes are integrated. Reuse the preceding
spawner assessment; only the two complete-assembly size attributes remain.
Direct inspection uses the same pinned archive/catalogs and the seven additional
class-member hashes in family-decisions.json processor_inspection. The existing
provider identities bind PharaohUtil, state and mixin sources. Frozen
betterdeserttemples-neoforge-1_21.toml has Apply Mining Fatigue=true and is now
pinned in the family evidence map.

Template paths below are under data/betterdeserttemples/structure/:

- mobs/creeper, mobs/slime and mobs/pharaoh each contain one persistent entity.
  parkour_bottom_5 has four matching creeper targets, parkour_bottom_6 six slime
  targets, throne_room one Pharaoh target. The slime has Size0. Pharaoh is
  encoded as a husk with Health/max_health60, sword/shield, armor and a player-head
  component. These are source alternatives/connector counts, not live populations.
- PharaohProcessor calls PharaohUtil.isPharaoh(nbt,registryAccess), then attaches
  transformed spawn position if recognized. Reuse the existing utility and
  death/discard hooks: recognition depends on Husk identity and head texture;
  clearance uses stored original position, or current position if absent.
  ServerPlayerTickMixin checks survival, periodic ticks, enabled config, loaded
  valid tagged temple and uncleared state before its mining-fatigue path. It
  constructs amplifier2/duration600. This is conditional source behavior, not
  proof of runtime profile decoding, effect application or clearance persistence.
- Root monster override is husk weight100/group10..32, piece-bounded. Creature
  entries are cat and rabbit, each weight100/group4..4. Ordinary natural husks
  are not automatically Pharaohs. Authored spawners are separately recorded.
- Eleven direct chest table IDs are preserved in trace loot_references:
  minecraft:chests/desert_pyramid and betterdeserttemples:chests/{storage,statue,
  library,pot,food_storage,wardrobe,tomb_pharaoh,lab,pharaoh_hidden,tomb}.
  OrangeStainedGlassProcessor additionally writes suspicious sand with
  minecraft:archaeology/desert_pyramid when nextFloat<0.01. Other branches supply
  sand/sandstone variants. This threshold is not an observed frequency.
- Fixed container Items encode splash potions, golden swords, blue/yellow/black
  concrete, arrows, water buckets, flint_and_steel, bows and a gold ingot. These
  include puzzle filters and traps. Frames contain swords/banners/bread or no
  item; ordinary frames alone enter ItemFrameProcessor, not glow frames.
- ItemFrameProcessor selects armory for iron_sword and storage for bread. AIR
  removes the Item field, preserving the entity. Other items retain selection/
  rotation after coordinate correction. The two randomizers remain exactly
  pinned through ItemFrameChances; their possibilities are not guaranteed loot.
- Armor stands in hall_room/5x5/hall_room_5x5_25 and _32 have leather and iron
  helmet markers respectively. ArmorStandProcessor chooses wardrobe for the
  former, armory for the latter; ArmorStandChances supplies chainmail/leather or
  chainmail/gold choices, including AIR. Preserve uppercase Count and legacy
  tag/Damage writes without asserting effective armor or durability.
- PotProcessor retains other input NBT while replacing sherds with four draws.
  Archer/miner/prize/skull sherds occupy successive0.05 intervals; remaining
  outputs are brick. Pot contents and loot references remain separate.

Short-form direct inspection (exact class hashes are in the family decision):

```sh
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -p -c \
  -classpath downloads/item3/candidates/YungsBetterDesertTemples-1.21.1-NeoForge-4.1.5.jar \
  com.yungnickyoung.minecraft.betterdeserttemples.world.processor.PharaohProcessor \
  com.yungnickyoung.minecraft.betterdeserttemples.world.processor.ItemFrameProcessor \
  com.yungnickyoung.minecraft.betterdeserttemples.world.processor.ArmorStandProcessor \
  com.yungnickyoung.minecraft.betterdeserttemples.world.processor.PotProcessor \
  com.yungnickyoung.minecraft.betterdeserttemples.world.processor.OrangeStainedGlassProcessor \
  com.yungnickyoung.minecraft.betterdeserttemples.world.ItemFrameChances \
  com.yungnickyoung.minecraft.betterdeserttemples.world.ArmorStandChances
uv run -m tools.build_item8_inventory --output evidence/raw/item8/desert-content-inventory.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

## Declared Desert Temple geometry capture

Unmet requirement: approximate full-assembly footprint and height. There is no
retained full-start observation. starts/center.nbt is11x23x11 with six main-pool
connections: tnt_bottom, front/right/left puzzle connectors, entrance_connector
and top_center. Its shell is not the full temple. Use one existing gap target,
seed42,81 requested chunks, timeout900. This is a geometry example, not a reward,
combat, clearance, frequency or human-visibility experiment. Retain failures if
any; require a full start before accepting saved assembly bounds. Yellow stained-
glass support behavior must remain distinct from saved piece bounds.

```sh
uv run -m tools.run_item7_gap_targets \
  --pristine instances/pristine-baseline-v0 \
  --artifact-manifest evidence/item-3/artifact-acquisition-manifest.json \
  --retained-manifest evidence/item-3/runtime/retained-server-candidates.txt \
  --seed-suite test-environment/seed-suite.json \
  --frozen-config evidence/item-6/frozen \
  --frozen-manifest evidence/item-6/generated-config-manifest.json \
  --config-audit evidence/item-6/config-audit.json \
  --java-home downloads/item2/temurin/extracted/jdk-21.0.12.1+1 \
  --target instances/item8/desert-geometry-r1 \
  --log-path evidence/raw/item8/desert-geometry-r1/console.log \
  --captured-config evidence/raw/item8/desert-geometry-r1/configuration \
  --receipt evidence/raw/item8/desert-geometry-r1/run.json \
  --timeout-seconds 900 \
  --structure betterdeserttemples:desert_temple
```

Use fresh hash-verified materialization, readiness, correlated save-all flush and
clean stop from the existing runner. Stage/decode the stopped world with existing
tools, inspect its full start through observed_bounds, and publish immutable raw
evidence with source revision, SHA-256 manifest and local/downloaded restore.
No new measurement framework or baseline tuning is authorized by this capture.
