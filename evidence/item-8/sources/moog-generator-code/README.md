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
