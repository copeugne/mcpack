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

## Stronghold content and placement

This assessment reuses the pinned provider capture above, frozen configuration,
packaged-json-redacted.json.gz, templates-redacted.json.gz, pool-traces-content.json.gz,
structure-inputs.json and dimension-r3/dimension-biomes.json. Their identities
are bound in family-decisions.json. Exact packaged paths below are relative to
YungsBetterStrongholds-1.21.1-NeoForge-5.1.3.jar. This is direct artifact inspection,
not a new measurement or a claim of live combat/reward acceptance.

The 84 templates reached from betterstrongholds:starts form one assembly.
The missing pool betterstrongholds:spiral_stairs remains explicit. The effective
biome set intersects only the captured Overworld. The root at
`data/betterstrongholds/worldgen/structure/stronghold.json` declares absolute
uniform anchor -30..11, max_y 60, size 15, max_distance_from_center 116,
strongholds step, no surface projection, ignore_waterlogging and top/bottom bury
adaptation (kernel size/distance 24). These support underground classification
and low surface visibility, not measured extents. The packaged
minecraft eye_of_ender_located tag includes this root; that alone does not prove
which retained replacement an Eye selects. The frozen Cristel toggle is true,
and its placement file retains salt 596441294, spacing 85 and separation 50.
The provider set additionally declares first-ring distance 80 chunks and ring
thickness 96. These are placement settings, not observed exploration pacing.

Under `data/betterstrongholds/structure/`, the following block-entity inputs
identify authored ordinary spawner sources. Both SpawnData and positive-weight
SpawnPotentials agree on the species:

- portal_rooms/portal_room.nbt, block_entities/1: silverfish.
- rooms/crypt_sm.nbt, block_entities/0: skeleton, encoded iron sword.
- rooms/grand_library.nbt, block_entities/0,1,8,15,16,36,37,38,39: spider.
- rooms/junction_md.nbt, block_entities/4: silverfish.
- rooms/library_md.nbt, block_entities/3: spider.
- rooms/prison_lg.nbt, block_entities/1,3,9,10: zombie.

The selected grand_library processor list removes matching spawners with
probability 0.75; prison_lg uses 0.70. Do not sum template inputs as a generated
stronghold count. ConfigModuleNeoForge.bakeConfig binds Enable Structure Ruin;
the frozen TOML is false and RuinProcessor.processBlock returns its input before
terrain inspection. Other custom processors handle banner, ore, rare-block,
redstone, support, portal-frame and frame/stand data. Frozen ore/rare-block
outputs contain no spawners. No trial-spawner block appears in the traced
palette or selected provider outputs. Main/statue/terminator rules turn red
stained glass into TNT; stone-brick random rules can create infested bricks.
The empty root spawn_overrides leaves natural spawning to biome/world conditions.
The traced entity records are frames and stands, not authored living enemies.

Twelve direct container table references are listed in loot_table_source:
nine betterstrongholds chest tables and three vanilla stronghold tables. Exact
references remain in each reachable template's loot_references. Fixed Items in
rooms/cmd_acarii.nbt include gold nugget, cookie, paper, water/healing potions and
dyed boots; rooms/sealed_collapse.nbt contains harming lingering potions. These
include props and trap payloads. Chest-removal rules and room selection preclude
calling the input lists guaranteed rewards.

ItemFrameProcessor.processEntity selects armouryItems for iron-sword markers
(armoury_sm/md), storageItems for bread markers (storeroom). AIR removes Item,
not the frame. Other items, including cmd_acarii's map, retain their data;
valid frames receive transformed Tile coordinates and random rotation.
ArmorStandProcessor selects rare equipment for the cmd_acarii diamond helmet
and common equipment for other readable helmets. It writes non-AIR slots to a
copy using id, legacy Count=1 and tag/Damage=0. AIR skips a slot. The final
new entity assignment is inside the non-AIR helmet branch: an AIR helmet returns
the original entity and discards prior copy edits. This detail prevents falsely
attributing every slot selection as an effective equipment replacement.
Frozen armorstands.json and itemframes.json are the selection inputs, loaded
by ConfigModuleNeoForge; do not substitute constructor defaults for those files.
Written legacy NBT is not proof of successful runtime equipment decoding.

OreProcessor maps nether-gold-ore markers through frozen ores.json;
RareBlockProcessor maps purpur through rareblocks.json. EndPortalFrameProcessor
uses the frozen filledPortalFrameChance 0.1. These are authored resource sources,
not additional chest tables or a yield measurement. All referenced processors,
selection consumers and config loader are in the existing pinned capture.

Reproduce the authoritative inventory after integrating the decision with:

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/stronghold-content-inventory.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

### Declared Stronghold geometry capture

Two required attributes remain: approximate footprint and vertical size.
No retained world-bounds observation exists for this root. Its sole start
starts/junction_lg.nbt is 31x24x31 with external hallway connectors, so that room
cannot substitute for assembled size. Reuse the existing seed42 Overworld gap
runner for one target, betterstrongholds:stronghold, 81 requested chunks and
900-second timeout. Require fresh frozen materialization, readiness, correlated
save-all flush, clean exit and configuration acceptance. Preserve a failure
rather than changing the baseline or silently expanding the experiment.

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
  --target instances/item8/stronghold-geometry-r1 \
  --log-path evidence/raw/item8/stronghold-geometry-r1/console.log \
  --captured-config evidence/raw/item8/stronghold-geometry-r1/configuration \
  --receipt evidence/raw/item8/stronghold-geometry-r1/run.json \
  --timeout-seconds 900 --structure betterstrongholds:stronghold
```

Use the existing stopped-world staging, decoder and observed_bounds, retaining
only full-start geometry for acceptance. Archive and verify local and downloaded
restores through the existing custody workflow. LegProcessor downward supports
and lateral stair/slab writes can extend beyond template boxes; keep those
separate from the saved assembly envelope. No new tools or world sampling system
are needed.
