# Terralith provider entry boundaries

Selector 21eac3c captures all eleven classes from the frozen Terralith archive.
The second capture reproduced exactly before this README was added.
Archive SHA-256: d38bd304897731b42f6c013cdc07e082e74411e80c74aabcee385251beb3b546.
Identity manifest SHA-256:
cf0cdfa21a06651e123ae119eadc733c62cc9457fc1131311aac614d5148b1c9.

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive Terralith_1.21.1_v2.6.2_Neoforge.jar \
  --output evidence/raw/item8/terralith-provider-r1
```

TerralithNeoforge loads ConfigHandler from the loader configuration directory
and attaches RegisterEvent. Its callback registers only the terralith:config
condition codec. TerralithNeoforgeClient installs the configuration screen.
The remaining classes implement configuration state, serialization, the screen
and list entries, identifiers and logging. These classes do not implement a
separate authored generator. The declared mixin list is empty.

ConfigResourceCondition.test returns config.test(key) != invert. The codec's
default invert is false. ConfigState delegates keys to its Modules record;
ConfigHandler loads and saves that state. The packaged NeoForge overlays use
this condition. Their disposition must use the frozen configuration rather
than assuming that all packaged overlay resources are active.

This capture closes the executable entry inspection, not the complete provider
row. Packaged roots, disconnected components, features, functions and overlays
still require their data reconciliation. Preserve that distinction until the
provider scope check is delivered.

## Six single-template family assessments

Forty-five attributes finish Desert Outpost, Igloo, Witch Hut, Frosted Dungeon,
Old Refinery and Sunken Tower. Seven registry roots select six unique templates;
Witch Hut's two roots share one template. Existing source geometry is preserved.
Exact source identities and per-template refs are integrated in family-decisions.
All selected pools use empty processors; templates have no jigsaw attachments.

Desert Outpost has no saved enemies or spawners; its full-bounds override permits
natural single pillagers. Its source includes terralith:desert_outpost container
loot and vanilla desert_well/desert_pyramid archaeology tables. Igloo saves a
snow-type fox, Health 10 and PersistenceRequired 0, and terralith:igloo loot.
It does not select a vanilla-style basement encounter.

Frosted Dungeon's underground/dungeon1 block_entities 3 is an ordinary stray
spawner (delay 200..800, nearby 6, count 4, range 4, player range 16).
No other selected template has spawners. Old Refinery and Sunken Tower have no
saved entities, spawners or natural spawn overrides beyond the ordinary world.
Their industrial/tower forms do not prove machinery or an authored encounter.
All three underground roots use absolute uniform start Y -40..40, beard_box,
ignore_waterlogging and no surface projection. The surface_structures step
label is not evidence of surface placement. Loot refs use terralith:underground/chest.

Witch Hut saves two minecraft:item entities containing moss_carpet, each with
Age2229. It does not save witches/cats. Its active regular root configures
piece-bounded natural witches (group1..2) and cats (group1). The underground-ID
root also declares surface projection but uses the empty has_structure/none
biome tag and empty spawn overrides. Preserve that ineligible variant rather
than inferring underground placement or additional family identity from its ID.
Both select terralith:witch_hut loot. Saved item lifetime is not guaranteed loot.

Runtime biome intersections are Overworld except the ineligible Witch Hut root.
No direct retained starts are asserted. Visibility is qualitative template and
placement inference; no exposed-height, sight-distance or pacing measurement.
No nonempty fixed Items/item container payload occurs in these six templates.

Rebuild: `uv run -m tools.build_item8_inventory --output <absent-path>`.
Validation: `uv run pytest -q tests/item8/test_terralith_provider_scope.py tests/item8/test_inventory_sources.py`.
Seven tests pass. Semantic comparison changes only these six families and the
decisions pin; existing geometry, identities, biomes and observations remain
unchanged. Inventory SHA-256:
`9d18d1d522871d0f25c2e95a0e392ba858f167147746098416830fecbc5274ea`.

## Six residence, rubble and underground-cache families

Fifty-seven attributes finish Glacial Hut, Rubble, Giant Bee Hive, Mining Outpost,
Underground Cabin and Valley Lodge: twelve roots and 34 unique present templates.
Each architecture is a standalone alternative with empty processors. Only
Glacial/Lodge add small villagers, which fit their architecture envelope.
Glacial interior1/interior2/interior216 receivers are (4,1,9), (6,3,6), (5,5,5).
Lodge receivers are (8,1,13), (5,6,14), (9,6,12), (20,6,12). All point upward;
1x2x1 or 1x3x1 villagers attach above them without extending architectural bounds.
Their snowy/plains pools select nitwit/baby/unemployed with weights1/1/10.

Source XYZ sizes are retained individually in the assessment. Glacial choices
are 10x11x15, 11x13x13 and 11x21x11; Lodge is 29x19x19. Rubble small/medium/large
are 5x5x5, 5x7x5 and 5x10x5 across all six material sets, weights5/4/3.
Hive alternatives are 13x9x8 and 17x14x17, equal weight. Mining alternatives
are 12x6x9 and 7x6x7, weights6/7. Cabin alternatives are 12x7x8 and 9x7x6,
weights4/7; two root definitions select these same alternatives. Do not add
alternative footprints or count shared components twice.

Hive top-level entity lists are empty, but nested source occupancy is not.
In underground/giant_bee_hive_1.nbt, block_entities 1/2/3 save 1/2/1 bees.
In giant_bee_hive_2.nbt, indices1..7 save 1/1/0/1/3/1/2 bees. Each EntityData
ID is minecraft:bee. These are saved occupants, not measured releases or a
hostile dungeon population. No selected template has an ordinary/trial spawner.
All root spawn overrides are empty; ordinary conditional world spawning remains.

Rubble brushable blocks use trail_ruins_common; large decorated pots additionally
bind trail_ruins_rare, unlike medium pots. Glacial junk/main_cs, Lodge village
and drinkables, hive-specific barrels and underground/chest sources retain exact
per-template ownership. No nonempty fixed Items/item container payload was found.
Hive and underground shelter roots use uniform absolute Y -40..40. Hive uses
bury, cabins/mining beard_box; both cabin definitions retain their explicit
liquid-setting difference. No projected surface exposure is implied by step names.

Seven applicable tests pass using the command above. Semantic comparison changes
only these six families and the decisions pin; identities, biomes and original
observations remain unchanged. No runtime capture or tooling addition.
Inventory SHA-256:
`81f98410e22ee9605e4f18ea741842b2ef00a2d7ef3b8814f0a998908ab5f100`.

## Mage Tower and Spire

Twenty attributes assess two families, six roots and sixteen unique templates.
Use the pinned templates-redacted catalog, archive
Terralith_1.21.1_v2.6.2_Neoforge.jar, paths data/terralith/structure/mage/
and data/terralith/structure/spire/, together with their selected pool traces
and packaged worldgen definitions. These are direct source assessments, not
new runtime measurements. No selected template is missing or unresolved.

All five tower architectures are 24x58x24. Seven upward connectors attach
1x2x1 mob templates inside that envelope; the highest receiver Y is 34 in
the ordinary tower and 35 in seasonal towers. The other receiver coordinates
also remain inside the architecture. Ordinary/autumn/spring/summer use pillager,
evoker, vindicator and witch components; winter substitutes stray for pillager.
The saved vindicator has empty hands, so an axe is not inferred. Pillager saves
a crossbow and stray a bow. Each architecture saves an axolotl; ordinary tower
additionally saves an item containing two arrows. No ordinary/trial spawners
occur. Pool mage/ground replaces grass_block over existing calcite with calcite;
it does not inject entities, spawners or loot. Mob processors are empty.

Spire starts at layer2. Its rigid pieces have XYZ sizes: layer2 37x26x34,
layer1 94x27x98, base_r 107x31x54, base_l 107x31x53, layer3 35x37x32,
layer4 18x51x19. For each edge, child origin equals parent origin plus
outgoing connector position plus its facing unit vector minus incoming position:

| Edge | Outgoing position/facing | Incoming position/facing | Child origin |
| --- | --- | --- | --- |
| layer2 to layer1 | 36,0,0 down_south | 65,26,33 up_south | -29,-27,-33 |
| layer1 to base_r | 93,0,0 down_east | 95,30,6 up_east | -31,-58,-39 |
| base_r to base_l | 106,30,53 south_up | 106,30,0 north_up | -31,-58,15 |
| layer2 to layer3 | 36,25,0 up_east | 34,0,0 down_east | 2,26,0 |
| layer3 to layer4 | 23,36,7 up_west | 17,0,0 down_west | 8,63,7 |

The vertical joints are aligned with matching top directions. The horizontal
base join is rollable, but its opposing horizontal faces already fix relative
rotation under the generator's horizontal rotations. All names/targets are
terralith:spire. Each pool selects one weight-one rigid piece with empty
processors/fallback. The furthest edge is three connections from the root,
within size6. The nominal union has inclusive minimum -31,-58,-39 and maximum
75,113,67, giving 107x172x107. This is intended connected architecture, not proof
that every placement succeeds or a measurement of occupied/exposed blocks.

Base_l spawner block-entity indices11/12/13 assign zombie/stray/silverfish.
Base_r indices3/9/10/16/17/20/21 assign drowned/cave_spider/skeleton/zombie/
cave_spider/skeleton/cave_spider. Their retained NBT uses delay200..800,
nearby limit6, spawn count4, spawn range4 and player range16. Ten source blocks
are not ten observed active spawners or a live enemy count. Base_l saves eleven
bats, base_r six bats, layer4 an armor stand. The latter saves a diamond helmet
with legacy ProtectionIII, UnbreakingII, BindingI, netherite/silence trim and
attribute modifiers. Its source equipment is preserved, without claiming those
legacy effects survive runtime loading or are recoverable loot.

Exact per-template loot paths remain in the assessments. Towers use
terralith:mage/treasure. Spire bases use common/junk/rare, base_r additionally
treasure, and layer4 treasure. No nonempty fixed Items/Book container payload
occurs in these sixteen templates. All six root spawn overrides are empty.
Captured biome overlap is Overworld; no retained start observations exist here.
Ordinary tower projects to WORLD_SURFACE_WG; seasonal starts are absolute
243/224/194/264 without heightmap projection. Spire starts at absolute92 with
no terrain adaptation. Source silhouettes support qualitative discoverability,
not measured visibility distance, exposure, live encounters or exploration pace.

Rebuild and focused validation use the commands above. The semantic change is
limited to these two families and the decisions identity; existing observations,
biome constraints and registry assignments are preserved.

Seven focused tests pass. Inventory SHA-256:
`01cae86e2773d7656a307672fd58f4ce6e3e8ad49b9138ef850dcad613a70f25`.
