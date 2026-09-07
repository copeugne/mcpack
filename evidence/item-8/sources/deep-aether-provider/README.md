# Deep Aether provider entry boundaries

Extractor 9b16faf5107dccced26837bd66dd3e9b0a9ab2e5. Manifest SHA-256: 71c441da5bd3213d84b0ce9f1f38f098979d158b3f16146397428b99e958d5c4. Independent r1 matches every generated file.

This capture contains the fourteen annotated entries, eleven declared common mixins, feature registration and nine remaining feature implementations, and eight Brass/jigsaw consumers. The existing totem capture and inactive disposition are reused. Verbose output preserves side annotations and callback bindings so client-only entries are not inferred from names. These are the concrete provider boundaries left by the candidate partition, using the existing extractor. Source capture alone is not provider closure.

```sh
uv run -m tools.inspect_item8_pool_elements --archive deep_aether-1.21.1-1.1.5.1.jar --class-name io/github/razordevs/deep_aether/DeepAether.class --class-name io/github/razordevs/deep_aether/block/behavior/DABlockInteractionBehavior.class --class-name io/github/razordevs/deep_aether/client/DeepAetherKeys.class --class-name io/github/razordevs/deep_aether/client/renderer/DAOverlays.class --class-name io/github/razordevs/deep_aether/event/DAClientGameBusEvents.class --class-name io/github/razordevs/deep_aether/event/DAClientModBusEvents.class --class-name io/github/razordevs/deep_aether/event/DAGeneralEvents.class --class-name io/github/razordevs/deep_aether/init/DAEntities.class --class-name io/github/razordevs/deep_aether/init/DAEntityRenderers.class --class-name io/github/razordevs/deep_aether/init/DATabs.class --class-name io/github/razordevs/deep_aether/item/dungeon/brass/StormSwordItem.class --class-name io/github/razordevs/deep_aether/item/gear/ArmorAbilityListener.class --class-name io/github/razordevs/deep_aether/item/gear/DaAbilityListener.class --class-name io/github/razordevs/deep_aether/item/gear/ToolAbilityListener.class --class-name io/github/razordevs/deep_aether/mixin/BrewingFuelMenuMixin.class --class-name io/github/razordevs/deep_aether/mixin/BrewingFuelMixin.class --class-name io/github/razordevs/deep_aether/mixin/GlovesMixin.class --class-name io/github/razordevs/deep_aether/mixin/TriviaGeneratorMixin.class --class-name io/github/razordevs/deep_aether/mixin/block/AercloudMixin.class --class-name io/github/razordevs/deep_aether/mixin/block/BlockBehaviourMixin.class --class-name io/github/razordevs/deep_aether/mixin/block/LavaFluidMixin.class --class-name io/github/razordevs/deep_aether/mixin/block/PointedDripstoneBlockMixin.class --class-name io/github/razordevs/deep_aether/mixin/block/PowderedSnowMixin.class --class-name io/github/razordevs/deep_aether/mixin/entity/AerwhaleMixin.class --class-name io/github/razordevs/deep_aether/mixin/entity/ItemEntityMixin.class --class-name io/github/razordevs/deep_aether/world/feature/DAFeatures.class --class-name io/github/razordevs/deep_aether/world/feature/features/AercloudCloudFeature.class --class-name io/github/razordevs/deep_aether/world/feature/features/CloriteColumnsFeature.class --class-name io/github/razordevs/deep_aether/world/feature/features/ConfiguredBoulder.class --class-name io/github/razordevs/deep_aether/world/feature/features/DAHugeMushroomFeature.class --class-name io/github/razordevs/deep_aether/world/feature/features/FallenTreeFeature.class --class-name io/github/razordevs/deep_aether/world/feature/features/PoisonLakeFeature.class --class-name io/github/razordevs/deep_aether/world/feature/features/RainAercloudCloudFeature.class --class-name io/github/razordevs/deep_aether/world/feature/features/RockSpikeFeature.class --class-name io/github/razordevs/deep_aether/world/feature/features/RootFeature.class --class-name io/github/razordevs/deep_aether/world/structure/DAJigsawStructure.class --class-name io/github/razordevs/deep_aether/world/structure/HeightSpawningChecks.class --class-name io/github/razordevs/deep_aether/world/structure/brass/BrassDungeonPiece.class --class-name io/github/razordevs/deep_aether/world/structure/brass/BrassDungeonStructure.class --class-name 'io/github/razordevs/deep_aether/world/structure/brass/BrassRoom$BossRoom.class' --class-name io/github/razordevs/deep_aether/world/structure/brass/BrassRoom.class --class-name io/github/razordevs/deep_aether/world/structure/brass/processor/BrassDungeonRoomProcessor.class --class-name io/github/razordevs/deep_aether/world/structure/brass/processor/BrassProcessorSettings.class --output evidence/raw/item8/deep-aether-provider-r1
```

## Brass family assessment

Reuse the pinned BrassDungeonStructure, BrassDungeonPiece, BrassRoom,
BrassRoom$BossRoom and BrassDungeonRoomProcessor capture above, the Aether
placement/trapped-block captures, and the packaged JSON/template catalogs.
Exact identities are bound in family-decisions.json. This assessment uses direct
artifact inspection and explicit geometric derivation, not a new experiment.

### Dimension and placement

The effective Brass biome requirement resolves two biomes, both intersecting
only aether:the_aether in dimension-r3/dimension-biomes.json. The same join for
Aether Bronze, Silver and Gold resolves15 biomes each in that dimension. None
has missing required or unresolved biome references. These four dimension
answers have been integrated together; they are eligibility, not observation.

BrassDungeonStructure.findGenerationPoint constructs an anchor at chunk middle
X/Z and minY+nextInt(rangeY). The selected definition supplies184 and5, giving
Y184..188, without a surface projection. generatePieces creates two cloud beds,
four quarter-turned room/upper-part pairs and one door. Only the first room uses
a boss-form template. All five lower room alternatives and their boss forms are
31x32x31; room_part_up is31x20x31 and door31x32x31. Exact catalog paths are
`data/deep_aether/structure/brass_dungeon/` followed by brass_dungeon_room_0
through _4 (and _boss variants), room_part_up or door, with .nbt suffixes.

### Architectural size derivation

BrassRoom.makeSettingsWithPivot sets pivot(31,0,0). BrassDungeonPiece passes these
settings through AetherTemplateStructurePiece, whose constructor adds processors
without replacing that pivot. createBossRoom puts the upper part at anchorY+32.
Thus lower Y0..31 and upper Y32..51 give52 inclusive blocks. Door height32 is
within that vertical union. Vegetation markers only write around lower-room
positions and do not replace this structural height with a boss tracking AABB.

For initial rotation NONE and anchor(0,0,0), applying generatePieces' quarter
turns and one-block relative offsets gives the four horizontal lower/upper boxes:

| Quadrant rotation | X interval | Z interval |
| --- | --- | --- |
| NONE | 0..30 | 0..30 |
| CLOCKWISE_90, rotated SOUTH offset | 0..30 | -31..-1 |
| CLOCKWISE_180, rotated SOUTH and EAST offsets | 31..61 | -31..-1 |
| COUNTERCLOCKWISE_90, rotated EAST offset | 31..61 | 0..30 |

The union is X0..61,Z-31..30, or62x62 blocks. The door uses initial rotation and
a four-block rotated EAST offset; for NONE it spans X4..34,Z0..30, inside the
union. Other initial quarter turns rotate/translate these equal-size quadrants
and the inset door, retaining62x62 extent. Room design selection does not alter
any template dimension. Hence the architecture is62x52x62. This is a source
assembly derivation, not a measured world or an occupied-block count.

Cloud support is separate: two buildCloudBed calls use horizontal sampling spans
55x55 and33x33 at different offsets/heights. Their random walks and block clusters
can extend beyond those spans, so neither the sampling span nor the architectural
box is the entire cloud footprint. The existing LargeAercloudChunk writer places
its supplied state only into empty positions. No cloud yield, whole-start maximum
or guaranteed occupied support volume is asserted. The exposed high-altitude
building/cloud design supports potential visual prominence, not a measured
sightline, visibility through terrain or fixed discovery distance.

### Authored and natural enemies

brass_dungeon_room_3.nbt and brass_dungeon_room_3_boss.nbt each contain two ordinary
spawners at block_entities/2 and /3. SpawnData is aether:cockatrice and
SpawnPotentials is empty. Other numbered choices have no conventional spawners.
The selected `data/deep_aether/worldgen/processor_list/bronze_boss_room.json`
applies rules for locked stone/planks, moss, cobweb and leaves, double_drops and
boss-room tracking. It has no spawner replacement or trial-spawner output.
All twelve selected templates lack trial-spawner blocks. Random room selection
means these component counts are not guaranteed whole-dungeon populations.

Each boss-form template authors deep_aether:eots_controller, while the entry
selects only one boss-form quadrant. BossRoom enables entity finalization;
BrassDungeonRoomProcessor attaches Dungeon tracking data around the processed
entity. That tracking box is not the architectural footprint. Direct inspection
of EOTSController.start and spawnSegments establishes its segmented encounter
source, without asserting successful activation, a realized segment count or
combat acceptance.

The selected processor list has two sequential 0.05 rules that can turn locked
skyroot planks into trapped_skyroot_planks. DABlocks static registration uses
bootstrap248, bound to lambda$static$218, which constructs Aether TrappedBlock
with DAEntities.BABY_ZEPHYR. Reuse the captured TrappedBlock.stepOn: player and
trigger-event predicates gate the facade replacement and server-side triggered
spawn attempt. This is not natural spawning or a conventional spawner block;
write/spawn results are discarded. No aggregate trap frequency is inferred.

The two newly inspected exact class members and archive hashes are recorded in
processor_inspection. Reproduce with the pinned javap, using -v for the bootstrap:

```sh
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -p -c -v -classpath downloads/item3/candidates/deep_aether-1.21.1-1.1.5.1.jar io.github.razordevs.deep_aether.init.DABlocks
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -p -c -classpath downloads/item3/candidates/deep_aether-1.21.1-1.1.5.1.jar io.github.razordevs.deep_aether.entity.living.boss.eots.EOTSController
```

The root's twelve vanilla/Aether spawn categories all have empty full-box
overrides. This suppresses those structure-level natural spawns, not the authored
controller, spawners, traps, external handlers or movement in from outside.

### Loot sources and scope

Direct selected template NBT identifies three exact table IDs under
`deep_aether:chests/dungeon/brass/`: brass_dungeon_loot,
brass_dungeon_combinder_loot (preserve this packaged spelling) and
brass_dungeon_reward. The combinder table occurs in room_1 alternatives; boss
forms include the treasure-chest reward reference. No nonempty fixed container
Items occur in these templates. Room markers write flowers, grass or squash,
and double_drops changes supported block-state properties; these are not extra
chest tables. Source attribution does not establish boss clearance, treasure
access, successful loot decoding or measured reward yield.

All ten explicit Brass attributes and the other three dungeon dimension answers
are integrated in family-decisions.json and regenerated into inventory.json.
No new runtime, measurement tool or baseline change was required.

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/brass-assessed-inventory.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```
