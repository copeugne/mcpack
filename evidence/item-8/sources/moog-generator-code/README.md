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
