# AdoraBuild provider code

All seven packaged classes captured with extractor 6fcc20c and reproduced byte
for byte before adding this README. Identity manifest SHA-256:
446d2811b3bd46642a1ae419f030e7d78b24fa061eb12c8e37f2702b086f038d.
Archive SHA-256: 6f399680da36dbb95b9a0dbf8b600f173e650be4d6bc25f50fcac792dcce081e.

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive adorabuild-structures-2.11.0-neoforge-1.21.3.jar \
  --output evidence/raw/item8/adorabuild-provider-r1
```

AdorabuildStructuresMod registers end_jigsaw_structure, nether_jigsaw_structure
and overworld_jigsaw_structure in STRUCTURE_TYPE and attaches that registration
to the mod bus. Verbose bootstrap bindings associate each supplier with its
corresponding codec. ModRegistry forwards caller-supplied registrations to
DeferredRegister; RegistryEntries and RegistryEntry retain and return them.
There is no separate feature, event-based placement or authored root declaration.

Each custom generator uses its configured start pool and calls vanilla
JigsawPlacement.addPieces with configured aliases, padding and liquid settings.
The Overworld generator checks configured height limits when projecting to a
heightmap, including its special ocean-floor projection branch. The End generator
uses surface height plus sampled offset when projection is absent. The Nether
generator searches a base column for non-air below and air at the candidate and
two blocks above, then delegates assembly. These are placement differences for
existing roots, not independent families or extra hardcoded template designs.
Exact height behavior remains available here for later attribute attribution.

The separate provider check reconciles all packaged pools/templates against the
existing graph and runtime-root regression. Keep the basalt chambers reference
to missing minecraft:basalt_chambers/chambers unresolved as a component failure;
do not silently substitute a differently namespaced pool. Candidate coverage
does not certify successful generation or canonical grouping of all 106 roots.

## Twelve single-template source assessments

The following families now retain all eleven Item 8 descriptions: acacia_well,
bamboo_cache, bamboo_campfire, birch_beehive, birch_tree_workshop,
dark_oak_mansion, mushroom, oak_hut, red_sand_shrine, red_sand_temple,
sand_castle and sand_pyramid (all adorabuild_structures namespace).
This batch supplies 36 missing hostility, enemy-origin and discoverability
answers and reconciles 48 existing dimension/mob/loot/spawner answers. Existing
geometry, placement and resolved biome answers are retained. No new source
capture, world run, measurement or schema is needed.

Direct inspection: each family has one root and one fully traced template in
pool-traces-content.json.gz, no missing references, unresolved elements, marker
entries or unresolved entity IDs. Each retained definition is minecraft:jigsaw
with empty spawn_overrides. Ten use minecraft:empty processors. The mansion's
structure/dark_oak_mansion_medium_1 processor removes glass and randomly removes
dark-oak leaves. The red-sand hall's randomize_stone processor replaces stone
with ores. Their full rules are in packaged-json-redacted.json.gz; neither
contains an entity, spawner or loot assignment. Template IDs, exact loot tables
and entity ownership remain in the authoritative family rows.

The raw templates in templates-redacted.json.gz establish that the apiary's
three hive block entities have empty Bees lists; its explicit entity list supplies
bees. The mansion supplies evoker, pillager and vindicator entities. Mushroom's
armor stand is an object; sand castle's turtles and turtle eggs are animal and
block content, not a hostile encounter. Other batch templates have no explicit
entities. All have no physical-spawner or generation-marker inputs. These are
source descriptions, not generated population claims. Empty spawn overrides do
not disable ambient biome spawning.

Previously inspected comparison views and retained palettes support the visual
forms. Negative offsets, bury adaptation and room-enclosing terrain remain
explicit. Dispensers, tripwire, pistons, trapped chests, magma, TNT and lava are
hazard ingredients where present, not tested mechanisms. No visibility distance,
observed safe interaction or realized reward is inferred. The existing biome
answers have no missing required values or unresolved tags. Dimension attribution
uses those biomes and the captured dimension source overlap; occurrence remains
separate in world_observations.

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-adora-single-descriptions.json
uv run pytest -q tests/item8/test_adorabuild_provider_scope.py tests/item8/test_inventory_sources.py
uv run ruff check tools/build_item8_inventory.py
uv run basedpyright tools/build_item8_inventory.py
```

## Eleven variant-family source assessments

The next batch covers buried_sand_castle, frozen_shelter, house, library, prison,
raft, raised_house, riverboat, tree, tree_house and watercraft: 11 families and
55 roots. Each root has exactly one fully traced template. Directly read its
size_xyz from pool-traces-content template_contents to retain per-root X/Z and
Y envelopes. No concatenation of unrelated variant dimensions or observed bounds
is performed. Twenty geometry answers join the riverboat's existing geometry.
Four fixed-height placement answers retain frozen-shelter/raft/riverboat Y=63
and ship Y=62 or 63, without interpreting absolute height as terrain projection.
Existing surface-relative and buried placement answers remain unchanged.

Four nonempty processor lists occur in this batch: adapt_frozen_house changes
ice to water with probability 0.3; randomize_cobweb and randomize_vines remove
matching blocks with probability 0.5; replace_glass_with_air removes glass.
Read their complete packaged processor definitions. All remaining processor
references are minecraft:empty. None supplies mob, spawner or loot assignments.
Every root has empty spawn_overrides, all biome answers resolve without missing
required values or unresolved tags, and no template has unresolved entity IDs,
physical spawner inputs or generation markers.

Exact entity and loot references remain attributed to templates. In particular,
prisons supply illagers and villager captives with additional large-variant
entities; dark-oak ship supplies illagers, spruce ship a stray, and oak/mangrove
ships villagers. House animals are not hostile residents, armor stands/item frames
are objects, and cherry raft's chest boat is not a mob. Four birch_house_small_2
hive block entities have empty Bees lists; explicit template bees remain distinct.
Source-scoped absence does not exclude natural spawning, retaliation or material
hazards. Castle TNT/pressure plate and lava remain untested mechanism ingredients.

Previously inspected facility, house, tree and vessel views support qualitative
forms. Source template padding, terrain concealment, fixed-height placement and
variant differences prevent claims of realized visibility distance or population.
The batch integrates 57 missing descriptions and reconciles 44 existing source
attributions, retaining resolved biome answers and all original observations.

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-adora-variant-descriptions.json
uv run pytest -q tests/item8/test_adorabuild_provider_scope.py tests/item8/test_inventory_sources.py
uv run ruff check tools/build_item8_inventory.py
uv run basedpyright tools/build_item8_inventory.py
```

The 55 raw templates also contain no minecraft:jigsaw block entities, confirming
that their envelopes describe standalone variants rather than repeated pieces.

## Nine End-generator family assessments

Ancient palace, hall and pavilion, End bubble, gateway, house, raised house,
ship and temple cover 16 roots. This increment adds 46 missing descriptions
(ten geometry, nine placement and 27 design interpretations) and reconciles
36 existing dimension/mob/loot/spawner answers. No new capture or measurement.

EndJigsawStructure.findGenerationPoint bytecode offsets 65..184 handle absent
projectStartToHeightmap: get WORLD_SURFACE_WG base height at chunk minimum X/Z,
add sampled startHeight, check optional minimum/maximum and construct the start.
Offset 228 delegates to JigsawPlacement.addPieces. Every selected definition has
start_height absolute 0, min_absolute_height 10, no heightmap projection and
beard_box adaptation. These are surface-relative starts, not absolute Y=0.
Biome answers resolve without missing required values or unresolved tags; captured
dimension overlap remains the dimension evidence, not a guarantee of occurrence.

Each root traces one template, with no missing/unresolved graph edges, jigsaw
block entities, unresolved entity IDs, physical-spawner inputs or markers.
Missing geometry answers directly use retained template_size_xyz per root,
including padding. Five nonempty processor lists affect the bubble alternatives:
randomize_emerald_block, randomize_grass_and_flowers, and structure/
end_bubble_medium_1_birch, end_bubble_medium_1_cherry, end_bubble_medium_2.
Their complete packaged rules only substitute blocks: metals, wood/leaves,
flowers/grass, coral and water. No entity, spawner or loot assignment occurs.

Top-level template entities supply variant-specific shulkers, axolotls, tropical
fish and the large temple's end crystal. Direct raw NBT inspection additionally
finds three Bees[].EntityData.id=minecraft:bee entries in end_bubble_medium_1's
hive. Record these separately from top-level entities, preserving the legacy keys
and avoiding a claim of successful release. Both gateway block entities preserve
ExactTeleport=1 and ExitPortal=(100,50,0), which establishes authored inputs,
not safe or successful teleportation. None has a generated physical spawner.
Empty spawn overrides do not prevent ambient spawning.

Exact loot references remain template-owned. Gateway has no container-loot
reference; other families retain End-city and, for bubble, beehive loot sources.
Existing views and template contents supply distinct forms, while the generator
explains placement. These descriptions retire source assessment without asserting
realized populations, interaction outcomes or measured discoverability.

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-adora-end-descriptions.json
uv run pytest -q tests/item8/test_adorabuild_provider_scope.py tests/item8/test_inventory_sources.py
uv run ruff check tools/build_item8_inventory.py
uv run basedpyright tools/build_item8_inventory.py
```

## Eleven Nether-generator family assessments

Blackstone bastion/towers/temple, crimson hall/tower house, fortress courtyard/
wart house, fossil, portal, temple and warped house cover 14 roots. Integrated
52 missing descriptions (eight geometry, eleven placement and 33 interpretations)
and reconciled 44 existing attribution answers. No new source capture or world run.

NetherJigsawStructure.findGenerationPoint scans the base column at chunk minimum
X/Z from minAbsoluteHeight+offset through maxAbsoluteHeight. It selects the first
Y with non-air at Y-1 and air at Y and Y+2, then starts at selectedY+offset and
calls JigsawPlacement.addPieces. Y+1 is not explicitly tested; non-air is not a
solid-block test. All selected definitions use offset 0, min 32, max 96, no
heightmap projection and beard_box. This describes a Nether cavity/floor search,
not whole-footprint clearance, observed exposure or safe footing.

All traces are complete. Raw templates contain no jigsaw block entities; fossil
selects among three standalone 9x5x9 alternatives. Other roots each trace one
template. Preserve per-template nominal geometry with padding and rotations.
Biome answers resolve without missing/unresolved inputs. Processor lists are
empty or three vanilla rule lists: randomize_gold_block, replace_glass_with_air,
and structure/nether_fossil_1. They only replace gold with ancient debris/lodestone,
remove glass, or replace/remove decorative skull blocks. They do not supply mobs,
physical spawners or loot assignments. No template spawner/marker inputs occur.

Four families have monster overrides, correcting the initial progress estimate
of two: fortress courtyard, wart house, temple and fossil. The first three use
piece-bounded blaze/zombified-piglin/wither-skeleton/skeleton/magma-cube entries.
Fossil uses its distinct zombified-piglin/wither-skeleton/skeleton weights and
counts. Exact definitions are retained in both source attribution and enemy-origin
answers. Overrides configure natural spawn selection, not initial residents or
physical spawners. The fossil's lack of explicit template mobs is not peacefulness.
Authored piglins/brutes/hoglins and courtyard enemies remain template-owned.
Armor stand is an object; strider is an animal. Portal blocks are authored inputs,
not proof of a safe linked portal. Rewards remain exact saved loot references.

The first working inventory was superseded before acceptance by the final output
below, which distinguishes the fossil override from the fortress table. Existing
views and source contents supply the qualitative visual forms. No measured
visibility, population or interaction outcome is asserted.

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-adora-nether-descriptions-final.json
uv run pytest -q tests/item8/test_adorabuild_provider_scope.py tests/item8/test_inventory_sources.py
uv run ruff check tools/build_item8_inventory.py
uv run basedpyright tools/build_item8_inventory.py
```

## Four Overworld-generator family assessments

Mountain mine, ocean bubble, ocean shrine and ocean temple cover seven roots.
Integrated 22 missing descriptions and reconciled 16 existing attribution answers.
Every root has one fully traced template and no jigsaw block entities, unresolved
entities, physical-spawner inputs or generation markers. Retained per-template
sizes resolve six geometry answers; bubble's existing geometry is unchanged.

OverworldJigsawStructure.findGenerationPoint checks projected base height at chunk
minimum X/Z against configured minimum/maximum before applying the offset. Mine
uses WORLD_SURFACE_WG, bounds 80..144, offset -12 and bury adaptation. The normal
branch passes that projection/offset to JigsawPlacement. Ocean roots instead use
OCEAN_FLOOR_WG with maximum 48 and offset 0. The special ocean-floor branch adds
the offset to that base height and calls JigsawPlacement with empty projection,
preventing a second projection. These inputs do not measure effective burial,
submersion, occupied volume or visibility.

Only adapt_mine is nonempty: its complete packaged rules substitute stone/ores
and remove cobweb. Ocean pools have empty processors. Minecart in mountain_mine_2
is an authored object. Ocean temples declare guardian natural monster spawning,
shrines drowned, with full bounds; both suppress their listed axolotl and
underground-water-creature categories. Bubble declares empty lists for eight
categories including monster. Exact overrides are retained by root, not converted
to observed populations or protection from wandering mobs.

Raw ocean_bubble_1 palette declares sculk_shrieker can_summon=false,
shrieking=false and waterlogged=false; block-entity warning_level is 0. Record
these alongside sensor/catalyst content without inventing a Warden encounter.
The root's ignore_waterlogging liquid setting remains preserved. Bubble and
shrines have no saved loot-table references; temples retain underwater-ruin-small
loot. Architecture views omit water and do not establish underwater visibility.
No new measurement, code capture or interaction experiment is required for these
source descriptions.

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-adora-overworld-descriptions.json
uv run pytest -q tests/item8/test_adorabuild_provider_scope.py tests/item8/test_inventory_sources.py
uv run ruff check tools/build_item8_inventory.py
uv run basedpyright tools/build_item8_inventory.py
```
