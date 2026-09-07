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

## Fortress family assessment

Batch: one family, ten explicit attributes,149 available traced templates and
one missing halls/hall_4 reference. No new capture or tooling. The family evidence
map pins packaged JSON/templates, pool trace, this source manifest, effective
biomes, captured dimensions and world bounds. Exact archive identity is above.

Direct derivations (paths under data/betterfortresses/):

- worldgen/structure/fortress.json declares15 effective biomes;14 intersect only
  the captured Nether. regions_unexplored:redstone_abyss intersects no captured
  dimension. Anchor80..100, surface_structures step, no heightmap projection,
  custom top-carve/bottom-none adaptation with kernel distance/size24.
- The root's piece-bounded monster entries are blaze (weight10,group2..3),
  zombified piglin (5,4..4), wither skeleton (8,5..5), skeleton (2,5..5), magma
  cube (3,4..4). FixMobSpawningMixin adds the nether-brick-floor/valid-start
  predicate already described above. These are spawning inputs, not live counts.
- structure/blaze/blaze_0.nbt block_entities[1].nbt has blaze SpawnData and
  empty SpawnPotentials. Its palette/state_counts contain one ordinary spawner.
  The pool entry requires min_required_depth28. No other ordinary or trial
  spawner occurs in the149 available templates. Main processors do not rewrite
  that spawner NBT. Missing hall_4 has no inspectable content and remains missing.
- mobs/piglin and mobs/wither_skeleton each encode one persistent entity; the
  latter has a stone sword. Matching targets occur in jail_md_l_0/r_0 and keep
  components respectively. mobs/skeleton has no matching target in the available
  templates. All three occur in worldgen/template_pool/mobs.json with distinct
  connector names; pool membership alone does not prove placement. Create gate/
  keep components have mod_loaded predicates; their super_glue is an object.
- Nine direct chest table IDs occur: minecraft:chests/nether_bridge and
  betterfortresses:chests/{hall,extra,obsidian,puzzle,quarters,storage,worship,keep}.
  Exact block-entity paths remain in template_contents loot_references.
  No nonempty fixed container Items list occurs in the available templates.
- ItemFrameProcessor.processEntity switches on original Item.id, not entity name.
  stone_sword/iron_ingot/cobweb/apple/nether_wart select weapon/loot/study/mess-hall/
  alchemy randomizers from ItemFrameChances. AIR removes the frame. glowstone_dust
  becomes blaze_powder or is removed. The study branch may encode an enchanted
  book; preserve its actual components write without claiming runtime enchantment
  acceptance. Other items pass through item selection; surviving frames have
  TileX/Y/Z and rotation rewritten. The201 source frames include all six selector
  types plus chiseled_nether_bricks and blaze_powder. Frame inputs are not yields.
- PillarProcessor, StairPillarProcessor and RedSandstoneStairsProcessor write
  downward through air/fluid to terrain or build limits. BridgeArchProcessor also
  writes neighboring arch blocks. Four configured pillar markers are orange/
  yellow terracotta and orange wool/concrete, with nether/red/cracked-brick and
  conditional magma outputs. Do not equate saved piece bounds to occupied bounds
  including all direct writes.

Full world-bounds observations124/524 are run-a/run-b mountainous seed
6671238423019257953, Nether chunk6,10, source line2357, envelope
[-20,6,64,207,97,273]:228x92x210. Observations216/610 are run-a/run-b ocean-heavy
seed95920844204830198, Nether chunk7,11, source line2385, envelope
[-2,11,73,183,110,263]:186x100x191. Each dimension is max-min+1. Source paths are
run-{a,b}/{mountainous,ocean-heavy}/chunks.jsonl. Nonfull observations21/433 are
excluded from accepted examples. These are illustrative saved assemblies,
not family extrema, occupied volume or proof every component chunk is populated.
Support/arch extensions remain separate. Visibility is source-described, not a
human sightline test. The missing hall reference does not create another family
or justify inventing missing content; it remains an explicit source limitation.

The already preserved disassemblies pin these direct class facts. Short-form
inspection and existing affected validation:

```sh
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -p -c \
  -classpath downloads/item3/candidates/YungsBetterNetherFortresses-1.21.1-NeoForge-3.1.5.jar \
  com.yungnickyoung.minecraft.betterfortresses.world.ItemFrameProcessor \
  com.yungnickyoung.minecraft.betterfortresses.world.ItemFrameChances \
  com.yungnickyoung.minecraft.betterfortresses.world.processor.BridgeArchProcessor \
  com.yungnickyoung.minecraft.betterfortresses.world.processor.StairPillarProcessor \
  com.yungnickyoung.minecraft.betterfortresses.world.processor.RedSandstoneStairsProcessor
uv run -m tools.build_item8_inventory --output evidence/raw/item8/fortress-assessed-inventory.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```
