# Shared Moog generator evidence

Tool revision: `d764903`. Retained archive:
`moogs_structures-neoforge-1.21.1-alpha-3.0.0.jar`, SHA-256
`9cdb525229470ac7801cc2ed74912eca610daa1d2bde10bf6afaf53c1afe66db`.
The existing archive-scoped extraction retains ten classes, including the newly
selected GenericJigsawStructure and its enum plus existing pool/version classes.
`identities.json` SHA-256:
`4287c67414d06b14d55cd69c4c76c5d164487ce4fe0cd70a962dddd9b1f01ee8`.
This is text disassembly, not committed binaries.

Executed from the repository root:

```sh
uv run -m tools.inspect_item8_pool_elements --archive moogs_structures-neoforge-1.21.1-alpha-3.0.0.jar --output evidence/item-8/sources/moog-generator-code
diff -rq evidence/raw/item8/moog-generator-pilot evidence/item-8/sources/moog-generator-code
```

Extraction reproduced the pilot exactly before adding this README. For a new
reproduction use an absent directory and compare identities and listed files.
The existing tool verifies the retained archive hash and uses pinned javap.

GenericJigsawStructure's codec reads `cannot_spawn_in_liquid` through BOOL
fieldOf followed by `iconst_0`, Boolean.valueOf and MapCodec.orElse. Omission
therefore selects false. Cherry River's omission and Birch River's explicit
false agree on this option; their biome references, start pools and layouts
still differ. This source finding is not proof of complete placement equivalence.
Other terrain, height, biome-radius and jigsaw placement behavior still requires
attribution to family requirements. No Item 8 completion is claimed.

## Ten Voyager Overworld descriptions

After c13eba18, this batch integrates eighty answers for barn, beach_bar,
bee_dome, desert_house, desert_pump, duck, gallows, horse_pen, lamp_chest and
lecturn_garden. Each already had two geometry descriptions, preserved unchanged.
Ten selected standalone templates use seven ordinary single elements and three
versioned selections across the ten roots: specifically desert_house, desert_pump
and gallows select their 1.21-1.21.8 resource for this frozen runtime. Other roots
use ordinary single elements. No newer fallback is substituted. No new capture,
measurement or tool is introduced.

All resolved family biome sets intersect only Overworld runtime possible biomes.
All roots use the shared generic-jigsaw generator, surface heightmap projection,
offset zero, beard_thin and cannot_spawn_in_liquid=true. Nine declare terrain
height range 3; radius inputs are 1 except lecturn_garden at 2. Desert Pump omits
those optional terrain fields, which remains explicit rather than borrowing a
neighbor's values. The captured generator checks the highest nonair block in the
chunk-center base column for fluid, not every block of the whole template.
Terrain and liquid checks constrain candidate placement, not guarantee exposure.

Direct inspection of template entities and block entities avoids three misleading
shortcuts:

- Bee Dome has no top-level entities, but hive NBT at [3,2,2] stores two
  minecraft:bee records and [4,2,2] stores one under bees/*/entity_data. Each has
  AngerTime zero. These are three saved contained-animal records, not three
  observed released bees or a guarantee of permanent docility. Hive contents
  are not spawner blocks.
- Duck uses mvs:stone_to_diamond, a rule matching stone with probability 0.25
  and outputting diamond_ore. Its salvage input is recorded without claiming
  realized ore yield. The skull-decorated duck form does not author a live duck.
- mvs:empty is a real loot table: 0..2 rolls, cobweb/string entries with weights
  5/3 and count inputs 1..2. Horse Pen, Beach Bar and Gallows references therefore
  cannot be interpreted as guaranteed empty containers.

Other selected pool processor lists are minecraft:empty. No selected template
contains physical spawner NBT or generation markers. Inspected block-entity
payloads in the other nine reveal no contained mob source. Source hostility
therefore distinguishes environmental forms and hive animals from conditional
natural biome spawning. No safety guarantee is inferred.

Exact saved table ownership is integrated: Barn general/books/common/rare/uncommon;
Beach Bar empty/common/uncommon; Desert House houses_desert; Gallows empty/uncommon;
Horse Pen empty; Lamp Chest houses_uncommon, all with mvs namespace. Bee Dome,
Desert Pump, Duck and Lecturn Garden have no saved container table references.
Ordinary block drops, hive harvesting and the lectern book are separate source
contents, not fabricated container loot. Descriptive visibility comes from each
retained building/decorative form; no viewing distance or discovery rate is measured.

Ten affected Moog-provider/inventory tests and scoped builder checks pass. Only
these ten families and the decisions input hash changed. Existing geometry,
biomes, observation links and nonregistry content remain unchanged. Inventory
matches `evidence/raw/item8/inventory-mvs-overworld-small.json`, SHA-256
8f3e1a1c359e8f3fa72cd7a65277fa5540cc204746ebd2ac4b3a1b99c2e4f499.

## Ten Voyager ruins and decorative families

After bbb8b3ce, eighty answers finish castle_ruins, log_ruin, mushroom_statue,
large_mushroom, railway, ruined_beacon, small_ruin, snowy_fossil, statue_ruins and
stone_pillars. Existing geometry stays unchanged. Direct inspection of selected
templates, block entities, root definitions and pools supplies the remaining
source descriptions; no new capture, runtime measurement or tooling.

All ten resolved biome sets intersect only the Overworld runtime possible-biome
set. Roots use generic jigsaw, WORLD_SURFACE_WG offset zero, beard_thin and the
liquid check. Seven declare terrain range 3: castle_ruins/log_ruin/small_ruin use
radius input 2, railway/ruined_beacon/statue_ruins/stone_pillars use 1. Mushroom
Statue, Large Mushroom and Snowy Fossil omit these optional terrain fields. Source
inputs remain distinct from successful placement or measured exposure.

Selected template contents have no authored entities, contained mobs, physical
spawners or generation markers. Block entities are containers, beds, campfires
or a lectern; the three mushroom/fossil templates and Ruined Beacon contain none.
This supports environmental intent with conditional natural biome spawning,
not a safety guarantee. Nine pools are rigid ordinary single elements with empty
processors. Ruined Beacon uses the existing versioned element, selecting
mvs:ruins/ruined_beacon for 1.21.1 and processor mvs:tuff_to_iron. Its two ordered
rules match tuff with inputs 0.2 -> raw_iron_block, then 0.05 -> iron_block. These
are source substitution probabilities, not independently observed yields. The
selected template palette contains no beacon block; no active beacon beam or
beacon reward is inferred from the family name.

Container table ownership is recorded exactly: Castle Ruins general/common/rare/
uncommon; Log Ruin swamps; Railway common/uncommon; Small Ruin houses_uncommon;
Statue Ruins abandoned; Stone Pillars houses_rare, under mvs namespace with exact
houses_* IDs retained in inventory. Mushroom Statue, Large Mushroom, Snowy Fossil
and Ruined Beacon have no saved container tables. Ordinary salvage remains
separate. Qualitative visibility descriptions use the architectural forms and
recorded dimensions, without measurement of sight distance or discovery rate.

Ten affected Moog-provider/inventory tests and scoped builder checks pass. Only
these ten rows and the decisions input identity changed; existing geometry,
biomes, observations and nonregistry content are unchanged. Inventory matches
`evidence/raw/item8/inventory-mvs-ruins-decoration.json`, SHA-256
2d5db4d403447299020293b7564e1f41b6a0c4e38ed486675b2f219b02f5f346.

## Seven Voyager surface families

After c581177f, 56 descriptions finish shed, small_pillager_tower,
small_swamp_house, stone_fountain, sunzi_gate, tree_monument and villager_statue.
Existing geometry is preserved. Direct inspection uses the packaged JSON and
redacted template artifacts already hash-bound by each family, the corresponding
pool-traces-content entries, and the captured generic/versioned generator code.
No new capture, measurement or tooling is required.

All seven biome intersections are Overworld-only. Their roots use generic
jigsaw with WORLD_SURFACE_WG offset zero and beard_thin. Small Swamp House omits
cannot_spawn_in_liquid, selecting the captured codec's false default, and omits
optional terrain range/radius. Villager Statue also omits terrain range/radius.
Shed, Small Pillager Tower and Stone Fountain declare range 3/radius 1; Sunzi
Gate declares range 3/radius 2 and use_bounding_box_hack true; Tree Monument
range 4/radius 1. Stone Fountain retains liquid_settings ignore_waterlogging.
The remaining six explicitly enable the center-column liquid check. These are
placement inputs, not proof that the complete template is exposed or dry.

Small Pillager Tower's versioned single element selects mvs:small_pillager_tower
for 1.21-1.21.8. In that template, block_entities indices 10 and 28 at local XYZ
[8,6,6] and [5,9,6] contain legacy minecraft:mob_spawner NBT with
SpawnData/entity/id minecraft:pillager. Exact records are retained in the
assessment. They support authored hostility, not observed activation or counts.
The other six pools use ordinary single elements. All seven are rigid and
terminal; processors are minecraft:empty except Tree Monument's tuff_to_ores.

Top-level entity lists and generation markers are empty in all seven. The
Swamp House's 15 hive block entities each have an empty bees list; its smoker
Items list is empty. Other block entities are furnishings, containers and the
tower's explicit spawners, not hidden authored animals. Fountain, Tree Monument
and Villager Statue have no block entities. A villager-shaped statue therefore
does not establish an actual villager source. Natural biome spawning remains
conditional and no environmental family is claimed safe.

Container references are Shed mvs:houses_common/houses_uncommon, Small Pillager
Tower mvs:general/houses_uncommon/pillager, Swamp House mvs:swamps, and Sunzi Gate
mvs:empty/houses_books. The other three have none. Sunzi's empty table can produce
cobweb/string, as already established; its lectern book is separate. Tree
Monument's processor has ordered random tuff-match rules with input probabilities
0.3 to diamond_ore, 0.3 to emerald_ore, and 0.4 to coal_ore. These are salvage
inputs, not independent realized yield percentages. Qualitative discoverability
uses the already documented architectural forms and source dimensions, without
new sight-distance or discovery-rate claims.

Reproduction: run `uv run -m tools.build_item8_inventory --output` with an absent
output path and compare to inventory.json. Ten affected Moog-provider/inventory
tests and scoped builder Ruff/Basedpyright checks pass. Only the seven intended
rows and decisions input hash changed; geometry, biomes, observation links and
nonregistry content are unchanged. Inventory matches
`evidence/raw/item8/inventory-mvs-seven-surface.json`, SHA-256
37d8e2ffb6a778ac97ae7254ebd2d2f8f1248c08f54494918f208fb6643106cb.

## Four Voyager Nether, ocean and house families

After 2730cd27, 32 answers finish crimson_enchanting_table, nether_devil,
ocean_tower and warped_house. Their two existing geometry attributes are
unchanged. Direct attribution uses each family's hash-bound packaged JSON,
templates and pool trace, runtime biome intersections, and existing generic
and Nether generator disassembly. No new capture, measurement or tool.

All four start pools are terminal ordinary rigid single elements with empty
processors and no generation markers. Crimson Enchanting Table and Nether
Devil intersect only Nether runtime biomes; Ocean Tower and Warped House only
Overworld biomes. Warped materials do not make the house a Nether structure.

The existing moog-nether-generator-code identities manifest binds
GenericNetherJigsawStructure. Its codec field list does not read the two roots'
project_start_to_heightmap, allowed_terrain_height_range or
terrain_height_radius_check. Its constructor passes empty inherited optionals
for heightmap and terrain checks. The assessment preserves declared fields but
does not claim they control placement. In postLayoutAdjustments, HIGHEST_LAND
calls getHighestLand with the inverse of cannotSpawnInLiquid (both roots declare
true), then chooses land Y or the sea-level fallback for out-of-range land and
repositions pieces. Both omit ledge_offset_y, whose fallback is zero. This is
a Nether land-search feature, not ordinary Overworld surface projection.

Ocean Tower instead uses generic OCEAN_FLOOR_WG projection, zero start-height
input and y_allowance max_y_allowed 25. Omitted cannot_spawn_in_liquid defaults
false. Its 44-block source height is not claimed wholly below Y25 or visibly
above water. Warped House uses WORLD_SURFACE_WG, zero offset, explicit liquid
check and terrain range 3/radius 2. All four declare beard_thin.

In mvs:ocean_tower, /entities/0..59/nbt contain 44 guardian and 16 drowned
records, individually referenced by the existing trace. Physical spawners are
separate: /block_entities/0..5 target drowned and /block_entities/22..29 target
guardians through SpawnData/entity/id. Their exact NBT and positions are now
integrated. These are source records, not live counts or proven activation.
Other block entities are chests. Empty spawn_overrides does not remove those
authored sources; conditional natural spawning remains separate.

The other three templates have no saved entities, contained mobs or spawners.
Crimson's sole block entity is an enchanting table, an actual workstation.
Nether Devil has no block entities and depicts a creature without authoring it;
its fire details and Nether environment remain hazards. Warped House contains
furnishings and containers, with an empty furnace Items list. Its table owners
are mvs:empty, mvs:houses_common and mvs:houses_uncommon. The empty table can
produce cobweb/string. Ocean Tower owns mvs:crystal, mvs:general,
mvs:houses_uncommon, mvs:houses_rare and mvs:rare. Both Nether templates have
no saved container loot references. No reward roll or salvage yield is asserted.

Visibility is a qualitative architectural inference with explicit water/terrain
occlusion limits, not a measured discovery distance. Ten affected provider and
inventory tests pass; scoped builder Ruff/Basedpyright checks pass. Reproduce
with the existing build_item8_inventory command and an absent output path.
Only four family rows and the decisions input hash changed; geometry, biomes,
observation links and nonregistry content are unchanged. Inventory matches
`evidence/raw/item8/inventory-mvs-nether-ocean-house.json`, SHA-256
af705d1e244246e24e96faeb6dc0b6271daa8a0acdf411723458ff2f52d3a5cb.

## Voyager carts, camps and two facilities

After d42bb242, 40 required attributes finish Cart (four roots), Campsite
(three roots), Wheat Grain Bin and Windmill. Existing variant decisions supply
family boundaries; direct inspection of the same hash-bound templates, pool
traces, definitions and block-entity payloads supplies the integrated answers.
All nine roots select one terminal ordinary rigid single template each with
empty processors, no missing components and no unresolved pool elements.

Declared XYZ envelopes are Cart 3x4x3, Large Cart 1 9x8x11, Large Cart 2 9x8x7,
Bamboo Cart 4x4x6; Campsite 19x8x13, Fire Camp 7x2x8, Horse Campsite 9x3x6;
Wheat Grain Bin 7x13x7; Windmill 5x8x6. These are per-variant source envelopes,
including air/padding, with no jigsaw attachments. They are not occupied-world
bounds or exposed heights. Inventory stores XZ and Y separately by template.

All nine runtime biome intersections are Overworld-only. Generic jigsaw uses
WORLD_SURFACE_WG, offset zero and beard_thin. Bamboo Cart omits the liquid flag,
which defaults false; the other eight explicitly enable it. Large carts declare
terrain range 3/radius 1; Campsite 2/1, Fire Camp 3/1 and Horse Campsite 4/3.
Campsite's depth input is 3; others are 1. Grain Bin, Windmill and the two small
carts omit optional terrain range/radius. Full per-root definitions are preserved.
These candidate-placement inputs do not guarantee exposed or dry footprints.

Cart and Bamboo Cart each have one wandering_trader at /entities/0/nbt; large
carts have empty entity lists. All four retain a SAVE-mode structure block at
/block_entities/0 with empty metadata. The trace's generation_markers category
therefore contains authoring records, not demonstrated hostile-generation
markers. No physical spawners occur. The remaining five templates have no saved
entities or generation markers, including Horse Campsite: no authored horse is
inferred. Inspected block entities contain no hidden mob source. Grain Bin's
hopper Items list is empty. Natural spawning remains conditional.

Exact table ownership is integrated per template: Cart mvs:cart, both large
carts mvs:large_carts, Bamboo Cart none; Campsite mvs:general, mvs:abandoned,
mvs:houses_common and mvs:houses_uncommon; Fire Camp none; Horse Campsite
mvs:abandoned; Grain Bin mvs:houses_common and mvs:houses_uncommon; Windmill
mvs:empty. The last can yield cobweb/string. A hopper or windmill depiction
is not proof of a production loop, rotation or power output. Discoverability
uses retained forms and dimensions without a measured sight distance.

No new capture, measurement or tooling. Ten affected provider/inventory tests
and scoped builder Ruff/Basedpyright checks pass. Reproduce with the existing
build_item8_inventory command to an absent output path. Only four family rows
and the decisions input hash changed; biome constraints, observation links and
nonregistry content are unchanged. Inventory matches
`evidence/raw/item8/inventory-mvs-cart-camp-facilities.json`, SHA-256
25caadcfa0fbd1b542783357152283877b64430a607fc1e052e879da57d8e030.

## Voyager benches, paths and Out House

After 8f3cce21, 30 attributes finish Bench, Paths and Out House. Existing
family decisions and source forms are reused. Hash-bound packaged pools,
templates and trace entries provide direct dimensions, attachment and content
attribution. No new capture, measurement or tooling.

Bench selects five rigid ordinary single alternatives with empty processors:
large 7x4x2, medium 5x4x4, small_1 4x2x2, small_2 and small_3 4x3x2 XYZ.
Paths selects long 10x4x28 or short 10x4x13. These alternatives have no jigsaw
attachments and are not assembled together. Dimensions include air/padding,
not merely occupied blocks. Rotation can exchange horizontal axes.

Out House start_pool selects out_house/out_house (8x7x5). Its /block_entities/0
connector is down_east at [2,0,0], name mvs:out_house_top, target minecraft:empty,
and points to side_pool. That pool's only candidate is out_house_lower (8x1x5),
whose /block_entities/0 is up_east at [2,0,0], name minecraft:empty and target
mvs:out_house_top. Both joints are aligned and elements rigid. Adjacent matching
connectors place the lower origin at [0,-1,0] relative to upper. The resulting
nominal envelope is X0..7, Y-1..6, Z0..4, or 8x8x5 XYZ. No other connector
extends it; the lower connector participates in this join. The upper-only
height is 7. This derivation does not guarantee successful runtime attachment,
terrain exposure or a particular occupied-world envelope.

All three resolved biome sets intersect only Overworld runtime possible biomes.
Generic jigsaw uses WORLD_SURFACE_WG, offset zero, beard_thin and explicit
cannot_spawn_in_liquid true. Bench declares terrain range 3/radius 2, Out House
3/1, and Paths omits both. These checks do not guarantee exposed/dry footprints.
Out House has a surface-projected shelter and a lower attached component.

All selected entity lists are empty, with no spawners or generation markers.
Block entities are signs, campfires and containers, plus Out House's architectural
jigsaw connectors; no contained mob source is identified. Natural spawning and
terrain hazards remain conditional. Exact loot ownership: Bench medium and
small_2 use minecraft:chests/village/village_plains_house, small_3 uses
mvs:houses_common, and large/small_1 have none. Both Paths alternatives use
mvs:general, mvs:houses_common and mvs:houses_uncommon. Out House lower uses
mvs:houses_common; upper has none. Ordinary salvage is separate from these
container sources. Low benches, landscaped routes and the pitched-roof shelter
support qualitative discoverability descriptions, not a measured sight distance.

Ten affected provider/inventory tests and scoped builder Ruff/Basedpyright
checks pass. Reproduce using the existing build_item8_inventory command with an
absent output path. Only three family rows and the decisions input hash changed;
biomes, observation links and nonregistry content remain unchanged. Inventory
matches `evidence/raw/item8/inventory-mvs-benches-paths-outhouse.json`, SHA-256
ecf965d9df92ca1de317af3260e054458bebd76a6f8acdff36c576572bcceba8.

## Voyager Well family

After c971b6c6, ten attributes finish the 17-root Well family. Existing variant
boundaries remain unchanged. Direct inspection of hash-bound pools, templates,
connectors and captured generic/Nether codecs supports the descriptions; no
capture, measurement or tooling is added.

Fifteen variants are standalone templates: twelve biome wells are 5x7x5 XYZ,
Small Copper Well is 7x5x7, Small Tower Well 3x7x6, and Small Well 8x5x6. All
use versioned single elements. The frozen runtime selects the 1.21-1.21.8
resources except Small Tower Well, whose 1.21-1.21.4 entry explicitly selects
mvs:1_21_4/small_tower_well. Its path is not an incompatibility finding.
Rare Well's upper element also selects its 1.21-1.21.8 resource. Ordinary
Well upper/lower and Rare lower use ordinary single elements. All are rigid
with empty processors.

For ordinary Well, upper 4x6x4 has an aligned down_west connector at [1,0,0],
name mvs:welltop, target minecraft:empty. Each lower alternative 4x3x4 has
matching up_west at [1,2,0], name minecraft:empty. Adjacent connector alignment
places lower origin [0,-3,0], giving X0..3, Y-3..5, Z0..3: 4x9x4 XYZ. Rare
upper 9x9x8 has down_west at [4,0,0], name mvs:rare_well_top; lower 9x2x8 has
up_west at [4,1,0], name minecraft:empty. Its lower origin is [0,-2,0], giving
X0..8, Y-2..8, Z0..7: 9x11x8 XYZ. The matching lower connectors participate
in those joins, with no additional attachment. Upper-only heights are 6 and 9.
These are nominal fully attached source envelopes, not guaranteed placement
or exposed heights. Air/padding is included and rotation can exchange X/Z.

Runtime biome intersections identify End Well with the End, Nether Well with
the Nether, and the other 15 roots with Overworld. All definitions declare zero
start height, beard_thin, explicit liquid check and ignore_waterlogging. Generic
roots consume WORLD_SURFACE_WG; Rare Well alone declares terrain range 3/radius
2. Nether Well uses the captured HIGHEST_LAND repositioning path, whose codec
does not read the packaged heightmap field. Lower components extend below their
upper origin. No whole-footprint exposure or dryness guarantee is inferred.

All 20 selected templates have empty entity lists and no spawners or generation
markers. Inspected block entities are signs, barrels and architectural jigsaws,
without contained mobs. Natural spawning remains dimension/biome-dependent.
Ordinary lower with barrel references mvs:houses_uncommon; its alternative has
none. Rare lower uses mvs:houses_rare. Small Tower Well uses mvs:empty, which
can yield cobweb/string. All remaining selected templates have no container
LootTable reference. Exact owners are integrated; no rolled reward is asserted.
Compact upper well forms and potentially concealed lower contents support a
qualitative visibility description without a measured discovery distance.

Ten affected provider/inventory tests and scoped builder Ruff/Basedpyright
checks pass. Reproduce using build_item8_inventory with an absent output path.
Only Well and the decisions input hash changed; biomes, observation links and
nonregistry content are unchanged. Inventory matches
`evidence/raw/item8/inventory-mvs-wells.json`, SHA-256
c07384cf9665de83e8a0ae7a5a568e28f1cfe3ddc33badfaf1c2c50cd4b3f402.

## Voyager log piles, lanterns, stalls and End scraps

After d3b54c73, 40 attributes finish four families spanning 25 registry roots:
six Log Piles, eleven Lanterns, four Stalls and four End Scraps. Existing family
and variant decisions are retained. Direct inspection of hash-bound templates,
pools, block entities and runtime biome intersections supplies the integrated
answers. No capture, measurement or tooling is added.

Every root selects one standalone ordinary rigid single template with empty
processors and no attachments. Log Piles are each 7x4x5 XYZ. Nine small wood
lanterns are 2x5x1; Medium Oak is 3x6x1 and Small Campfire 3x7x3. Stalls are
Blue 11x10x8, Orange 9x9x10, Pink and Red 7x9x7. End Scraps 1..4 are respectively
10x6x9, 10x7x10, 9x6x8 and 9x7x9. Inventory separates XZ and Y by template.
These source envelopes include air/padding, with rotation potentially exchanging
X/Z. They do not establish occupied-world bounds or exposed height.

Log Pile, Lantern and Stall roots intersect only Overworld runtime biomes;
End Scraps only End biomes. All use generic jigsaw with WORLD_SURFACE_WG,
zero start height and beard_thin. Stall and End Scraps declare terrain range
3/radius 1; the others omit both optional fields. End Scraps omits the liquid
flag, selecting the captured false default. The other three families explicitly
enable the center-column liquid check. Complete dry/exposed footprints and
safety are not inferred from these candidate-placement inputs.

All 25 entity lists are empty with no spawner or generation-marker records.
Log Pile block entities are campfires. Lanterns have none except Medium Oak
and Small Campfire's campfire payloads. Stalls contain containers and banners;
End Scraps contain chests, plus variant 2's barrel. No contained mob source is
identified. Empty root spawn_overrides leaves natural spawning conditional on
dimension, biome and world state; no family is declared safe.

Log Piles and Lanterns have no saved LootTable references. Every Stall variant
references mvs:large_carts and mvs:large_carts_2. Each End Scraps variant uses
minecraft:chests/end_city_treasure, with mvs:end_scraps additionally in variant
2. These owners remain explicit per template, not equal reward values or
observed loot rolls. Ordinary salvage is separate. Qualitative visibility uses
low stacks, slender lanterns, colored stalls and compact scrap forms, without
measuring light range, viewing distance or discovery rate.

Ten affected provider/inventory tests and scoped builder Ruff/Basedpyright
checks pass. Reproduce with build_item8_inventory and an absent output path.
Only four family rows and the decisions input hash changed; biomes, observation
links and nonregistry content are unchanged. Inventory matches
`evidence/raw/item8/inventory-mvs-landmark-variants.json`, SHA-256
3f14a5d39bc684048f19422e3345ac16bdedb5fe782e7dfadd561f6b7b784e90.

## Voyager Dead Tree alternatives

After 5f02a697, ten attributes finish Dead Tree's eight roots and sixteen
alternatives. Direct inspection corrects the previous component interpretation:
each data/mvs/worldgen/template_pool/dead_tree/<wood>.json has two weight-1
ordinary rigid single elements with empty processors, selecting <wood> or
<wood>_trunk independently. None of the sixteen templates has a jigsaw block
entity. They are not attached pieces and their heights must not be summed.
The authoritative rationale now preserves and supersedes that earlier mistake.

Source XYZ dimensions (tree / trunk) are acacia 2x8x3 / 2x8x3, birch 6x9x4 /
1x3x1, cherry 7x9x6 / 1x3x4, dark_oak 6x9x7 / 3x6x3, jungle 8x18x9 / 3x7x4,
mangrove 6x9x6 / 3x4x2, oak 4x9x3 / 1x3x2, and spruce 4x8x4 / 1x4x2.
Inventory stores per-template XZ and Y. These include air/padding and possible
X/Z exchange on rotation, not observed occupied-world bounds or exposed height.

All roots intersect only Overworld runtime biomes and use generic jigsaw,
WORLD_SURFACE_WG, zero start height and beard_thin. Mangrove omits the liquid
flag and defaults false; seven others explicitly enable the center-column
check. Optional terrain range/radius are absent. Full definitions are retained.
All entity lists are empty with no loot references or physical spawners. The
only block entities are SAVE-mode structure blocks with empty metadata in
acacia, acacia_trunk and birch. Exact marker records remain integrated as
authoring payloads, not asserted mob-generation sources. Natural spawning and
terrain hazards remain conditional. Ordinary wood salvage is separate from
container loot. Bare tree and smaller trunk silhouettes support qualitative
visibility only, without sight-distance or discovery-rate measurements.

No capture, measurement or tooling was added. Ten affected provider/inventory
tests and builder Ruff/Basedpyright checks pass. Reproduce with the existing
build_item8_inventory command to an absent path. Only Dead Tree and the decisions
input hash changed; biomes, observations and nonregistry content are preserved.
Inventory matches `evidence/raw/item8/inventory-mvs-dead-trees.json`, SHA-256
3190d2277029a999b8383f5b1525e7ed97fa8d957b32127f2e90bddc6f00ef42.

## Voyager living trees, rocks and harvest heaps

After c82079a3, 28 attributes finish Living Tree (nine roots), Rock (two) and
Harvest Heap (two). Living Tree's two existing geometry answers are unchanged.
Direct inspection uses the hash-bound templates, pool traces, definitions and
runtime biomes. All 27 reachable templates are independent alternatives, without
jigsaw attachments. Big Oak's versioned entry selects mvs:nature/big_oak_tree
for 1.21-1.21.8; other elements are ordinary single. All are rigid with empty
processors. No capture, measurement or tooling is added.

Rock source XYZ sizes are boulder 5x5x6, both medium stone alternatives 5x4x5,
small diorite/granite 4x4x3, small stone 2x3x3 and small stone_2 3x4x3. Harvest
Heap sizes are haystack 6x5x6, small haystack 4x3x3, mixed 3x3x3, pumpkin 7x5x6,
and small pumpkin 3x4x2. Per-alternative XZ and Y are integrated with air/padding
and rotation caveats; these are not occupied-world bounds or exposed heights.

All thirteen roots intersect only Overworld runtime biomes and use generic
jigsaw, WORLD_SURFACE_WG, zero start height, beard_thin and explicit liquid
check. Big Oak alone declares terrain range 4/radius 2; others omit both.
Full root definitions preserve biome differences. These inputs do not guarantee
complete dry/exposed footprints or safety.

All entity lists are empty without spawner or generation-marker records. Rock
has no block entities; Living Tree has only Big Oak's chest. Harvest Heap
contains campfires and containers plus a sign, without contained mob sources.
Natural spawning remains conditional. Big Oak alone among living trees uses
mvs:general. Rock has no container loot. Large hay/pumpkin alternatives use
mvs:houses_common and mvs:houses_uncommon, mixed uses houses_common, and the two
small crop heaps have no LootTable references. Exact ownership is integrated.
Ordinary wood/stone/crop salvage is separate from container loot and does not
establish a sustainable production rate. Tree canopies, low rocks and crop heaps
support qualitative visibility descriptions without discovery-rate measurements.

Ten affected provider/inventory tests and scoped builder Ruff/Basedpyright
checks pass. Reproduce with build_item8_inventory to an absent output path.
Only three family rows and the decisions input hash changed; Living Tree geometry,
biomes, observation links and nonregistry content remain unchanged. Inventory
matches `evidence/raw/item8/inventory-mvs-tree-rock-harvest.json`, SHA-256
02f306b67b70385e756d6abf9de83ce02ef401798d9aa66f3d377e6739887cd7.

## Voyager Pond family

After 382ec3b5, ten attributes finish Mushroom Pond and Small Oak Pond as two
variants of one family. Existing hash-bound template/pool evidence is sufficient;
no capture, measurement or tooling. Each start pool selects its upper template
and side pool its lower, all ordinary rigid single elements with empty processors.

Mushroom upper is 11x8x15 XYZ, with aligned down_north jigsaw at [1,0,0], target
mvs:mushroom_pond_top. Lower is 11x1x15, with matching up_north at [1,0,0], name
mvs:mushroom_pond_top. Its origin moves to [0,-1,0], yielding Y-1..7 and a nominal
11x9x15 envelope. Oak upper is 12x8x16 with down_west at [7,0,0], target
mvs:small_oak_pond_top; lower is 12x2x16 with matching up_west at [7,1,0], name
mvs:small_oak_pond_top. Lower origin [0,-2,0] yields Y-2..7 and 12x10x16. The
only lower connector participates in each join; no further piece extends it.
Upper-only heights are 8. Source bounds include air/padding and possible X/Z
exchange on rotation; complete runtime attachment or exposure is not guaranteed.

Both root biome intersections are Overworld-only. Generic jigsaw uses
WORLD_SURFACE_WG, zero start height, beard_thin and explicit liquid check, with
no optional terrain range/radius. Lower components extend below upper origin;
the center-column liquid check does not remove authored pond water or guarantee
a dry/exposed footprint. All four entity lists are empty with no spawners or
generation markers. Inspected block entities are jigsaws, containers and Oak's
campfire with empty Items; no contained mob source. Natural spawning remains
conditional. Mushroom upper owns mvs:mushroom_pond, Oak upper mvs:pond, and
neither lower has container loot. No reward rolls or salvage yields are asserted.
Low landscaped pond forms and vegetation support qualitative discoverability,
without measured sight distance or guaranteed visible containers.

Ten affected provider/inventory tests and builder Ruff/Basedpyright checks pass.
Reproduce with build_item8_inventory to an absent path. Only Pond and decisions
input hash changed; biomes, observations and nonregistry are preserved. Inventory
matches `evidence/raw/item8/inventory-mvs-ponds.json`, SHA-256
19252b3a985f9aaf95edcd40bfe5458e5b547fb9946b42eec5a3ac6615a4da51.

## Voyager animal huts and igloos

After 377e3e5a, twenty attributes finish Animal Hut and Igloo across four roots.
Direct hash-bound template/pool inspection establishes the source geometry and
content; no capture, measurement or tooling. Fox Hut is 5x8x4 XYZ and Snowy Dog
Hut 5x4x6, each a standalone ordinary rigid template without entities, block
entities, spawners or loot. Their names do not establish authored animals.

Medium Igloo main is 9x7x14. Its up_north villager connector at [4,1,8]
places a 1x2-or-3x1 child at [4,2,8], inside the main envelope. Small Igloo main
is 7x5x10, placing its villager child at [3,1,5], also inside. Its down_west
connector at [5,0,0], name mvs:small_igloo_top, targets minecraft:empty;
the 7x1x10 lower has matching up_west at [5,0,0], name minecraft:empty.
The aligned rigid join places lower origin [0,-1,0], giving Y-1..4 and nominal
7x6x10 XYZ. No further lower connector extends it. Fully attached sizes include
air/padding and do not guarantee runtime attachment, occupied bounds or exposure.

Each main has one snowy-villager attachment position. The rigid legacy_single
pool selects nitwit/baby/unemployed with weights 1/1/10 and empty inline
processors. Each option stores one villager; three options do not mean three
guaranteed villagers. Architecture uses ordinary rigid single elements and
empty processors. Small lower alone has a stray spawner at local [2,0,6],
/block_entities/0, using legacy mob_spawner and SpawnData/entity/id. Exact NBT
is integrated as a source record, not observed activation or live population.
Architectural entity lists are empty; no contained mobs or generation markers.
Medium loot is mvs:houses_common; Small upper mvs:houses_uncommon. Lower and
villager pieces have none. Authored stray hostility remains specific to Small.

All four roots intersect only Overworld runtime biomes and use generic jigsaw,
WORLD_SURFACE_WG, zero start height, beard_thin and explicit liquid check.
Igloos omit terrain range/radius; Fox Hut declares 3/1, Snowy Dog Hut 3/2.
Full definitions preserve snowy/taiga constraints. Enclosed snowy dwellings and
small shelters support qualitative visibility only; natural spawning remains
conditional and no whole-footprint dryness or safety is inferred.

Ten affected provider/inventory tests and builder Ruff/Basedpyright checks pass.
Reproduce with build_item8_inventory to an absent output path. Only two family
rows and decisions input hash changed; biomes, observations and nonregistry are
preserved. Inventory matches `evidence/raw/item8/inventory-mvs-huts-igloos.json`,
SHA-256 836115beba40036735c4fb26f139761d34a18aada8aa6298c4ff9ffa8d3964f9.

## Voyager Small Ship

After 890ffc0f, ten attributes finish Small Ship. The versioned start element
selects mvs:small_ship for 1.21-1.21.8, with rigid projection and empty processors.
Its 15x10x9 XYZ main envelope contains the optional villager piece: up_south
connector [8,3,4] matches the rollable downward connector [0,0,0], placing a
1x2-or-3x1 child at [8,4,4]. It remains inside the main bounds with no further
attachment. Source dimensions include air/padding and possible X/Z exchange,
not guaranteed entity placement or occupied-world bounds.

The plains-villager pool uses rigid legacy_single options nitwit/baby/unemployed
with weights 1/1/10 and an empty inline processor list. Each contains one villager;
there is one attachment position, not three guaranteed occupants. Main entity
list is empty; its block entities are banners, barrels and that connector.
No contained mobs, spawners or generation markers. Both barrels reference
mvs:houses_common; villager options have no container loot. These are source
inputs, not observed populations, rolled rewards or a working moving vessel.

Runtime biome intersection is Overworld-only. Generic jigsaw uses
WORLD_SURFACE_WG offset -1, terrain adaptation none, valid biome radius input
3 and explicit cannot_spawn_in_liquid=true. Optional terrain range/radius are
absent. Preserve the liquid check despite the ship name; no actual flotation,
water placement or motion is inferred. Hull, deck details and banners support
qualitative visibility with possible concealed contents, not measured distance.

No capture, measurement or tooling. Ten affected provider/inventory tests and
builder Ruff/Basedpyright checks pass. Reproduce with build_item8_inventory to
an absent output path. Only Small Ship and decisions input hash changed; biomes,
observations and nonregistry remain unchanged. Inventory matches
`evidence/raw/item8/inventory-mvs-small-ship.json`, SHA-256
0b451177a4b41df207a2da02dac81bfe0626b3e0189270acabce2dcc7a93e564.

## Voyager Flower Hole

After 877019b1, ten attributes finish Flower Hole using existing hash-bound
architecture, pools, templates and runtime biome evidence. Main envelope is
27x8x25 XYZ. Its up_east rollable villager connectors [12,1,14] and [12,1,15]
match downward [0,0,0] connectors, placing 1x2-or-3x1 options at [12,2,14] and
[12,2,15], inside the main envelope. No other attachments extend it. Dimensions
include air/padding and rotation caveats, not guaranteed attachment or exposure.

Main ordinary single element is rigid with empty processors. Plains-villager
options are rigid legacy_single, empty inline processors, with nitwit/baby/
unemployed weights 1/1/10. Each option stores one villager; two positions do not
prove realized occupants. Main entity list is empty. Its containers, two furnaces
and smoker contain no mobs; furnace/smoker Items lists are empty. No physical
spawners or generation markers. Main owns mvs:houses_common and mvs:houses_flower
loot, while villager pieces have none. No rolled reward or production is inferred.

Runtime biome intersection is Overworld-only. Generic jigsaw uses
WORLD_SURFACE_WG, zero start height, beard_thin and explicit liquid checking,
without optional terrain range/radius. Recessed built spaces and planted covering
are source architecture, not evidence of measured underground burial depth.
Vegetation/enclosure can conceal contents; discoverability is qualitative, not
a measured sight distance. Natural spawning and terrain hazards remain conditional.

No capture, measurement or tooling. Ten affected provider/inventory tests and
builder Ruff/Basedpyright checks pass. Reproduce with build_item8_inventory to
an absent path. Only Flower Hole and decisions input hash changed; biomes,
observations and nonregistry remain unchanged. Inventory matches
`evidence/raw/item8/inventory-mvs-flower-hole.json`, SHA-256
fa055b9dc39da1ab98b962de354748e5651d22254ece92c3ee305d6f3f264165.
