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

## Jungle Temple content and placement assessment

Batch: one family, ten required explicit attributes and125 traced templates,
with no missing components. Eight content/placement attributes are integrated;
two assembly-size attributes remain pending the declared capture below. Existing
source manifests and catalogs are reused. No new tooling is needed.

Direct artifact references use the exact archive identified above, catalogued in
packaged-json-redacted.json.gz and templates-redacted.json.gz, and the trace at
structures[betterjungletemples:jungle_temple]. The family evidence map pins these
inputs, effective biomes, dimension memberships and the retained manifest.
All component paths below are relative to data/betterjungletemples/structure/.

- worldgen/structure/jungle_temple.json projects onto WORLD_SURFACE_WG with
  anchor offset-30..-25, step surface_structures and enhanced adaptation
  yungsapi:none. All13 effective biomes intersect only the captured Overworld.
  Its monster, creature and ambient piece-bounded spawn overrides are empty.
- treasure_room/treasure_room_1.nbt entities[0..3].nbt.id are silverfish.
  The crocodile pit's pool entry requires alexsmobs and the forge loader condition;
  alexsmobs is absent from the retained manifest. Its two packaged entities must
  not be attributed to the active encounter. Create/Supplementaries predicates
  match retained mods; the sawblade room additionally restricts rotations to
  none/counterclockwise_90. Mod predicates alone do not guarantee room selection
  or functioning machinery. Item/glow-item frames, super_glue and minecart data
  represent objects, not authored enemies.
- worldgen/processor_list/main.json runs EmptyDispenserProcessor before
  FireballDispenserProcessor. The former processes an empty dispenser Items list;
  ArrowData.getArrow(random,0.2,0.1) selects ordinary arrow for random<0.2,
  poison-tipped arrow for random<0.3, otherwise EMPTY, independently for nine slots.
  The latter converts orange concrete to an upward dispenser, writes fire_charge
  in slot4 and includes each other slot when nextFloat<0.1. Both use uppercase
  Count=1. Preserve this actual source encoding, not an assertion of loaded
  ammunition, successful firing or a repaired baseline.
- The same main list replaces pink_concrete with infested_cobblestone and allows
  infested outputs from polished_granite and chiseled_red_sandstone. These are
  conditional silverfish sources, distinct from natural spawn lists and ordinary
  spawner blocks. Template palettes/state_counts and block entities contain no
  ordinary or trial spawner. Other processors affect blocks, supports, decoration
  or frame coordinates; none registers another encounter family.
- Four direct loot-table IDs occur: minecraft:chests/jungle_temple;
  betterjungletemples:archaeology/emerald (gravel challenges);
  betterjungletemples:chests/campsite (campsite props); and
  betterjungletemples:chests/treasure (treasure-room alternatives).
  Exact template and block-entity paths remain in template_contents loot_references.
- Fixed Items lists include puzzle/filter materials and trap inputs as well as
  valuables. Examples: gravel challenges encode emeralds/brushes; serpent and
  statue-trade rooms encode flint_and_steel; serpent-back variants encode colored
  concrete, redstone and golden swords; statue props encode botanical resources,
  metals, bone, candles and related items. Treasure-room0 encodes lava buckets,
  room1 splash potions, room2/sakura lingering potions, and water-fill alternatives
  water buckets. Frame Item data contains emeralds or honeycomb. These are not
  all chest rewards, nor are source amounts verified collection yields.
- PillarProcessor.processBlock starts one block below a matching marker, writes
  configured pillar states through air or nonempty fluid, and stops at solid
  terrain or the build-height boundary. The loop uses DOWN directly. Do not infer
  a different extension from its serialized direction/length fields. Pillar
  extent remains separate from saved assembly bounds.

The existing preserved processor disassemblies and identity manifest support
these direct derivations. Short-form inspection uses the pinned javap:

```sh
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -p -c \
  -classpath downloads/item3/candidates/YungsBetterJungleTemples-1.21.1-NeoForge-3.1.2.jar \
  com.yungnickyoung.minecraft.betterjungletemples.world.processor.EmptyDispenserProcessor \
  com.yungnickyoung.minecraft.betterjungletemples.world.processor.FireballDispenserProcessor \
  com.yungnickyoung.minecraft.betterjungletemples.world.processor.PillarProcessor \
  com.yungnickyoung.minecraft.betterjungletemples.world.util.ArrowData
uv run -m tools.build_item8_inventory --output evidence/raw/item8/jungle-content-inventory.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

## Declared Jungle Temple geometry capture

Unmet requirement: approximate complete-assembly footprint and vertical size.
Existing observations372/752 are minecraft:carvers, not full starts. Three start
shells (start_0/1/2) are52x54x51,60x54x43 and60x54x51, with attached stairs,
entrance, room, hallway, challenge and prop pools. These shell dimensions alone
are not the complete connected envelope. Use the existing frozen gap-target
workflow for one target,81 requested chunks, seed42, timeout900 seconds. No
frequency, yield, trap functionality, player visibility or all-layout extrema
claim is added. Preserve a failed locate/run if it occurs. Accept geometry only
from a full start, retaining pillar extensions as a separate limitation.

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
  --target instances/item8/jungle-geometry-r1 \
  --log-path evidence/raw/item8/jungle-geometry-r1/console.log \
  --captured-config evidence/raw/item8/jungle-geometry-r1/configuration \
  --receipt evidence/raw/item8/jungle-geometry-r1/run.json \
  --timeout-seconds 900 \
  --structure betterjungletemples:jungle_temple
```

The established runner materializes fresh hash-verified inputs, waits for
readiness, requests correlated save-all flush, then clean stop, and checks frozen
configuration. Stage the stopped world, decode with the existing decoder, and
use observed_bounds for the saved envelope. Publish immutable raw evidence with
its source revision, SHA-256 manifest and local/downloaded restore using existing
custody tools before accepting the geometry. Do not modify the frozen baseline.
