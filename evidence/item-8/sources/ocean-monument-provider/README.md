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

## Ocean Monument family assessment

Batch: one family, ten explicit required attributes,57 traced templates, no
missing components. Existing evidence suffices; no runtime capture or tooling
was added. `family-decisions.json` records the answers and the inventory builder
integrates them. Biome constraints remain builder-derived.

Artifact inspection uses the exact archive named above in
`packaged-json-redacted.json.gz` and `templates-redacted.json.gz`, joined to
`pool-traces-content.json.gz` at structures[betteroceanmonuments:ocean_monument].
The family evidence map pins these catalogs, the provider identities, effective
biomes, captured dimension memberships and world bounds. Paths below are under
`data/betteroceanmonuments/`; template paths use `structure/` and suffix `.nbt`.

- `worldgen/structure/ocean_monument.json`: six effective deep-ocean biomes
  intersect only the captured Overworld. Anchor54..64, surface_structures step,
  and a piece-bounded guardian monster override (weight1, group1..3).
- `worldgen/template_pool/mobs.json`: four weight1 entries have distinct names
  in their template jigsaw block entities. Battle/side-room targets match
  elder_guardian; start targets elder_guardian_heart_of_sea; battle room1 targets
  axolotl. No target in the57 templates matches guardian. Do not turn pool
  membership or equal weights into a claim of interchangeable/placed residents.
- `mobs/elder_guardian_heart_of_sea`, entities[0].nbt: HandItems[0] encodes
  one heart_of_the_sea, HandDropChances[0]=1.0. The other elder-guardian and
  axolotl components encode their respective entity IDs. Actual live population
  and successful drops are not measured.
- `start`, block_entities[523].nbt.LootTable references
  betteroceanmonuments:chests/upper_side_chamber. Its packaged loot JSON supplies
  nautilus shells, prismarine shards and crystals. No other direct loot reference
  or nonempty fixed container Items list occurs in the57 templates.
- `lower_middle_chamber/lower_middle_chamber_1`, `_2`, `_3`, entities[0].nbt:
  trident entity, item.id=minecraft:trident, pickup=1. These are authored objects,
  not enemies. PersistentTridentMixin's existing inspected hook only prevents
  despawn under its server/trident/owner-marker/valid-piece predicates.
- Template palettes and corresponding state_counts contain no ordinary or trial
  spawner blocks. The ten main processors remain block-decoration, water and
  support transformations, without spawner creation. Entities and natural spawn
  overrides are separate sources.
- `start` state_counts:18 gold blocks,31 wet sponges,32 orange stained-glass
  markers. `parthenon/parthenon_0` through `_4` have23,4,6,4,2 wet sponges.
  RandomSpongeProcessor.processBlock maps orange glass to wet sponge for
  nextFloat<0.75, otherwise water. These are component counts and a source
  threshold, not guaranteed assembly yield or observed frequency.
- AirProcessor.processBlock converts ordinary AIR below sea level to water,
  preserving AIR at or above sea level. LegProcessor.processBlock offsets53..197
  replaces blue glass with prismarine bricks, then extends down through air or
  nonempty fluid, stopping at solid terrain or a build-height boundary. Direct
  support writes can escape saved piece bounds.

`world-bounds.json.gz` observations280 and669 preserve the same full start in
run-a/run-b, ocean-heavy seed95920844204830198, Overworld chunk2,9,
`run-a/ocean-heavy/chunks.jsonl` and `run-b/ocean-heavy/chunks.jsonl`, line13632.
Each has1436 piece boxes and envelope[-31,16,57,94,79,171]. Inclusive subtraction
(max-min+1) gives126x64x115 blocks. Use126x115 for an illustrative footprint and
64 for saved assembly height, with variable downward supports separately stated.
This does not establish occupied volume, all possible layouts or exposed area.
The upper example extends above sea level; do not describe the entire monument
as necessarily submerged. The packaged minecraft:on_ocean_explorer_maps tag
includes the root, supporting map eligibility only, not an observed map trade.

Processor derivations above are direct inspection of the immutable class members
already pinned by this provider's identities. Short-form inspection command:

```sh
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -p -c \
  -classpath downloads/item3/candidates/YungsBetterOceanMonuments-1.21.1-NeoForge-4.1.2.jar \
  com.yungnickyoung.minecraft.betteroceanmonuments.world.processor.LegProcessor \
  com.yungnickyoung.minecraft.betteroceanmonuments.world.processor.RandomSpongeProcessor \
  com.yungnickyoung.minecraft.betteroceanmonuments.world.processor.AirProcessor
uv run -m tools.build_item8_inventory --output evidence/raw/item8/ocean-monument-assessed-inventory.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

Optional realized populations, pickups, drop quantities and visibility distances
are not an Item8 investigation backlog. Required source attributions and scoped
approximate geometry are recorded, without claiming runtime gameplay acceptance.
