# WDA provider generation boundary

Extractor revision f3ac5ab. All six archive classes are captured, including the
complete custom jigsaw implementation. The output reproduced byte for byte.

```sh
uv run -m tools.inspect_item8_pool_elements --archive DungeonsArise-1.21.1-2.1.68-release.jar --output evidence/raw/item8/wda-provider-scope-r1
```

identities.json SHA-256:
1878d9890c8dbb9dae7b3edb7e07b760b1e59f0cb560519ef9b257ec79135d5f.

DungeonsAriseMain registers WDAStructures on the supplied mod bus. WDAStructures
registers one structure type, dungeons_arise:generic_structures, with the
WDAGenericStructures codec. Its generation point consumes the configured start
pool and calls ModifiedJigsawPlacement with an empty alias lookup. Placement
selects pool elements, reads child pool keys from template jigsaw NBT, follows
fallback pools and assembles PoolElementStructurePiece instances. PieceState is
an assembly record. The public ServerLevel placement overload also consumes a
caller-supplied pool; it supplies no additional authored root or registration.

These captures establish the executable candidate routes. Full packaged-resource
reconciliation, including function commands and disconnected components, belongs
to the provider-scope disposition. Do not count this source capture alone as
provider closure or as evidence of observed successful placement.

## Five named ship assessments

Fifty attributes assess Ceryneian Hind, Illager Corsair, Illager Galley, Typhon
and Undead Pirate Ship, five roots/22 templates. Use the pinned packaged-json,
templates-redacted and pool-traces-content catalogs, archive
DungeonsArise-1.21.1-2.1.68-release.jar, data/dungeons_arise/structure/<family>/
and worldgen/structure/<family>.json. These five roots use minecraft:jigsaw,
not the provider's custom generic_structures codec. All selected pools are
rigid single elements with empty processors and no missing/unresolved templates.

Hind/Typhon start at part1, a48x48x48 central section. Its west connector(0,0,0)
joins part0 east connector(47,0,0), giving part0 origin(-48,0,0). Part1 east
connector(47,0,0) joins part2 west connector(0,0,0), giving origin(48,0,0).
Named side0/1 and side2/3 pairs select the correct neighbors. Inclusive union
X-48..95,Y0..47,Z0..47 gives144x48x48. These are architectural envelopes with
air/padding. Corsair/Galley/Undead select part0 or part1 as start; the32x48x31
part0 east connector(31,0,0) joins31x48x31 part1 west connector(0,0,0), giving
part1 origin(32,0,0), union63x48x31. Starting from the other half translates
the same layout; whole rotation exchanges X/Z. Mob/spawner pieces are1x3x1 or
1x2x1 and attach within the section envelopes. Their connector names and top
orientations govern attachment, not pool weight alone; no live counts are inferred.

Galley has two retained full starts, each repeated in run-a/run-b. Ordinary
seed42 at chunk7,5 has box[80,62,80,142,109,110],63x48x31 (world-bounds71/474).
Ocean-heavy at chunk5,0 has box[80,62,-30,110,109,32],31x48x63 (272/661).
Do not count repeat runs as four distinct samples. Other four families have no
retained starts. No new capture is needed for the source approximation. Boxes
are not occupied blocks, visible mast height or proof every attached mob survived.

Hind/Typhon templates have no authored entities or ordinary/trial spawners.
Corsair has saved evoker Health60/PersistenceRequired0 and pillager
Health24/PersistenceRequired1; Galley has the latter. Both pillagers save
movement_speed0/knockback_resistance1 and crossbow plus16 legacy tipped arrows.
Corsair arrow effect is Id7/Amplifier0/Duration1; Galley Id2/Amplifier2/Duration10.
Corsair entities also wear banner data. Each ship's vindicator spawner saves
Health30, iron axe and custom attributes. These are source values, not proof
that legacy NBT converts correctly or that effective balance matches them.

Undead captain is skeleton Health60 with tripwire hook, diamond boots and dyed
leather armor. Ranged skeleton is Health20 with movement_speed0, PunchII/FlameI
bow and legacy ProjectileProtectionV armor. Three spawner templates retain:
dolphin with golden-axe skeleton passenger Health60; iron-sword skeleton Health80
with parrot passenger; iron-sword skeleton Health40 carrying silverfish carrying
another silverfish. Full nested source NBT remains in generated_spawners.
These non-hostile carrier/passenger types must not obscure the authored hostile
skeletons. Every ordinary spawner uses delay200..800, nearby6, count4, range4,
player range16; source piece counts are not placed/active block or enemy counts.

All root spawn_overrides are empty. No nonempty fixed Items/Book container
payload occurs in the22 templates; saved enemy gear remains separate. Exact
per-template loot references distinguish treasure, supply, barrels and enchants.
Hind/Typhon have treasure references but no authored encounter path in these
sources. Empty processors add no enemy, spawner or container transformation.

Resolved biome intersections are Overworld only. Hind projects WORLD_SURFACE_WG
with offset-16 and ignores waterlogging. Typhon projects OCEAN_FLOOR with offset-4
and applies waterlogging. Other three project WORLD_SURFACE_WG at offset0 and
apply waterlogging. All disable expansion; packaged adapt_noise is not evidence
that a minecraft:jigsaw root runs the provider custom codec. Source placement
supports qualitative burial/aquatic discovery cues, not measured exposure or pace.

Rebuild: `uv run -m tools.build_item8_inventory --output <absent-path>`.
Validation: `uv run pytest -q tests/item8/test_wda_provider_scope.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py`.

Eight focused tests pass. Semantic comparison changes only these five family
assessments and the decisions identity; registry membership, biome constraints
and retained observations remain unchanged. Inventory SHA-256:
`ad560639057b709679115139b5b65772a8565bfc5aa86244efe3ac299060fd9d`.

## Hut, tree house, lighthouse, blimp and well

Fifty attributes assess fishing_hut, jungle_tree_house, lighthouse, small_blimp
and wishing_well: five roots,20 selected templates. Same exact WDA archive and
catalog paths as above. Templates catalog SHA-256:
b4a2ed8ff0d16ff06c224119f623f248e75e9c8c838fbf2455bf37936c6d3705.
Each root is minecraft:jigsaw with empty spawn_overrides, WORLD_SURFACE_WG
projection, ignore_waterlogging and expansion disabled. Offsets in the order
above are -2,-5,-1,20,-7. Fishing depth3, others7; max distance114 throughout.
Resolved dimension-biome intersections are Overworld only. No retained start
is linked for these five. The existing world observations remain unchanged.
Selected pools have empty processors and rigid elements; Fishing uses
legacy_single_pool_element, the other four single_pool_element. Traces have
no missing components or unresolved elements. No new capture is required.

Geometry is a nominal connector-compatible envelope, including air/padding,
not observed occupied blocks or a guarantee every component places. Whole
rotation exchanges horizontal axes. Incoming connectors are placed adjacent
to the parent connector, then the rotated incoming coordinate is subtracted.

- Fishing main21x14x17 has up_west(10,5,5); spawner1x2x1 has
  down_west(0,1,0). Aligned attachment origin(10,5,5) fits main21x14x17.
- Jungle main31x48x31 down_north(15,0,15) matches roots31x16x31
  up_north(15,15,15), putting roots at(0,-16,0). Union31x64x31.
  The selected main pool contains both, so either may start. This preserves
  shape up to translation but changes surface-relative placement. Eleven
  main up-facing mob connectors accept1x3x1 saved-entity pieces within its
  envelope. These are not physical spawners or a measured population.
- Lighthouse starts part1(31x31x31). Its up_south(15,30,20) joins
  part2(31x37x31) down_south(15,0,20), origin(0,31,0), union31x68x31.
  Only these complementary architecture connectors occur; the tower pool
  containing both pieces does not establish an arbitrarily repeating tower.
- Blimp starts only ladders_0(2x48x1). Its aligned up_north(1,47,0)
  joins part0 down_north(28,0,11), origin(-27,48,-11). Part0 east(30,0,0)
  joins part1 west(0,0,0), origin(4,48,-11), using side1/side0 names.
  Hull parts are31x25x31. UnionX-27..34,Z-11..19,Y48..72 is62x25x31;
  ladderY0..47 stays within that XZ envelope, making62x73x31 overall.
  Ladder bottom points down into main pool, which contains only part0/part1;
  neither has the matching upward ladders connector. Do not invent a repeated
  ladder chain. Four hull spawner attachment points fit within the hull.
- Well16x25x16 up_north(7,1,7) joins effect5x2x5 down_south(2,0,2).
  Both are rollable. Unrotated origin(5,2,5) and allowed rotations keep the
  centered effect piece inside the well. Envelope stays16x25x16. The separate
  wishing_well_0_no_effects template/pool is not selected by this root and is
  not a seventh selected template or an additional family.

Fishing spawner_0 block_entities0 saves zombie with fishing rod, dyed leather
chestplate and redacted player head. Jungle husk_0/skeleton_0 entities0 save
Health40 and PersistenceRequired1: stone-axe husk or bow skeleton, with chain/
leather armor and bone/golden helmet respectively. Lighthouse saves neither
entities nor spawners. Source equipment is not proof of effective legacy NBT.

Blimp skeleton_0/1/2 block_entities0 each saves an ordinary spawner. Variant0
is Health30 golden-axe skeleton;1 is Health20 skeleton holding FireAspectI
flint-and-steel with Health20 Size0 magma-cube passenger;2 is Health20 skeleton
with minecraft:potion passenger whose Item is soul_lantern with legacy
CustomPotionEffects Id7/Amplifier0/Duration1 and Id15/Amplifier0/Duration400.
Preserve that unusual payload without claiming a functioning potion attack.
Full nested NBT is retained in generated_spawners. All four source spawner
variants across hut/blimp have Delay0,min/max200/800,nearby6,count4,range4,
player range16. Source variant counts are not placed spawner or enemy counts.
Blimp part0 block_entities26 hopper has one diamond;31 dispenser has arrows
2+2+4+6+6+6+2=28. These fixed contents are separate from loot-table references
and do not prove a working trap. Other selected templates have no nonempty
fixed Items/Book container payload. Per-template table pointers are retained
in loot_table_source; entity equipment is separate.

Well effects pool has five equal-weight alternatives, each with one saved
area_effect_cloud at entities0. Speed/regen/wither/resistance/haste save legacy
Effects IDs1/10/20/11/3; speed amplifier1, others0; wither duration200, others3200.
Every cloud saves Radius3,Duration19999980,DurationOnUse0,RadiusOnUse0,
RadiusPerTick0,ReapplicationDelay0,WaitTime0. Saved Ages are394/389/403/163/273.
Particles are large_smoke for speed/regen/haste and cloud for wither/resistance.
These are authored effect choices, not enemies or spawners, and no container
loot is assigned. Neither full persistence nor successful legacy effect
conversion is claimed. Natural spawning remains conditional for all families.

Rebuild and focused validation use the commands above. This increment changes
only these five assessments, their direct template-source reference and the
builder's decisions identity. It adds no tool, runtime or measurement system.

Eight focused tests pass. Inventory SHA-256:
4f0cde2359d75f890e8ef1be793eb6f522b374e3e59c98e694f1b64cc2179c7c.

## Heavenly fleet, Coliseum and Keep Kayra

Fifty attributes assess heavenly_challenger, heavenly_conqueror, heavenly_rider,
coliseum and keep_kayra: five roots/49 selected templates. Use the same pinned
WDA archive and catalogs above, structure/<family>/<template>.nbt and
worldgen/structure/<family>.json. All selected pool elements are rigid with
minecraft:empty processors; traces have no missing or unresolved elements.
All roots use minecraft:jigsaw, depth7,max distance114, ignore_waterlogging,
expansion disabled and empty spawn_overrides. No retained start is linked for
these five. No capture or new tooling was needed for this source assessment.

The Heavenly roots start at absolute Y200 without heightmap projection, not
surface+200. Their resolved biome intersections include both Overworld and End.
Coliseum intersects Overworld, projects WORLD_SURFACE_WG at offset-3 and uses
beard_box adaptation. Keep intersects Overworld and starts at absolute Y54
without heightmap projection. Its start_jigsaw_name keep_kayra_start matches
main_0 block_entities0 at(88,0,81). Architecture relative to terrain is not
verified by an unobserved nominal source envelope.

Connected geometry uses adjacent matching connectors. Rotation exchanges X/Z;
envelopes include saved air/padding and do not guarantee complete placement.

- Challenger starts part2 or3. Place part2 at(0,0,0). Its north(0,0,0)
  side9 joins part1 south(0,0,47) side8, putting part1 at(0,0,-48).
  Part1 east(30,0,0) side1 joins part0 west(0,0,0) side0, origin(31,0,-48).
  Part2 east side3 joins part3 west side2, origin(31,0,0).
  Part2 south(0,0,47) side6 joins part5 north(0,0,0) side7, origin(0,0,48).
  Part5 east side5 joins part4 west side4, origin(31,0,48).
  Left column width31, right30; row lengths48,48,35; all height48.
  Inclusive unionX0..60,Y0..47,Z-48..82 is61x48x131.
- Conqueror has four32x48x32 quadrants. Part0 east(31,0,0) joins part1
  west(0,0,0); part1 south(31,0,31) joins part2 north(31,0,0);
  part0 south(0,0,31) joins part3 north(0,0,0). Origins are
  (0,0,0),(32,0,0),(32,0,32),(0,0,32), union64x48x64.
  Coliseum uses the same quadrant positions with32x32x32 pieces, union64x32x64.
  The remaining side connectors close each square consistently. Horizontal
  front directions fix the relevant rotation even where joints are rollable.
- Rider lower parts0..3 follow that64x32x64 square. Part0 up_north(0,31,0)
  matches part4 down_north(0,0,0), both aligned, origin(0,32,0).
  Top parts4..7 use matching suffixed side names and32x16x32 quadrants above
  the corresponding lower pieces. Overall64x48x64. The top pool is reached
  through part0; its pieces are not additional root families.
- Keep main_0 is163x250x163. Its nine spawner alternatives are1x2x1 and
  compatible vertical attachments stay inside that envelope. Preserve the
  south-facing connector at(90,59,141): the middle alternatives have downward
  incoming connectors, so this particular connector cannot attach them under
  horizontal template rotations. It does not invalidate the main template.
  The starting connector targets minecraft:empty, not another keep copy.

Coliseum enemy_0 entities0 saves persistent Health20 iron-axe skeleton with
iron chest/helmet and dyed leather boots. Spawner_0 block_entities0 saves
Health50 Size16 phantom with skeleton passenger. Passenger equipment includes
PowerV/PunchIII bow, enchanted armor and legacy tipped arrows. Its explicit
DeathLootTable is dungeons_arise:entities/gladiator_loot. This is the only
selected table reference, not chest loot. Delay30,min/max11420,SpawnCount2
must not be replaced with the other designs' common200..800 interval.

Challenger has six ordinary spawner alternatives: hoglin_rider_0 (Health40
hoglin with Health50 wither skeleton); phantom_rider_0/1 (wither-skeleton
passengers Health40); skeleton_juggernaut_0/1 (wither skeletons Health60/40,
first with potion passenger); skeleton_theater_0 (Health30 wither skeleton
with Health20 slime passenger). Two saved-entity templates skeleton_theater_2
and skeleton_theater_3_main contain persistent wither skeletons Health30/60,
respectively bow/legacy tipped arrows and netherite sword. Source armor,
attributes and effects remain in each exact NBT document.

Conqueror has four ordinary spawner alternatives: juggernaut_0/1 Health30
wither skeletons, mounted_0 hoglin with Health20 wither skeleton, and
phantom_rider_0 Size5 phantom with Health20 wither skeleton. Rider has three:
husk_0, mounted_melee_0 hoglin with Health60 wither skeleton, and
mounted_skeleton_0 Health10 Size5 phantom with wither skeleton. The latter
uses min/max2400/4800; other Heavenly spawners use200/800. Initial Delays vary
and are preserved in source NBT. No direct saved entities occur in the
Conqueror/Rider hulls. Pool equal weights do not establish encounter frequencies:
connector names select compatible alternatives and generation may reject pieces.

Keep main_0 entities0..19 are paintings;20..42 are frogs with positive saved
Health. These are not43 hostile enemies. Nine spawner pieces use connector
classes high0..3, middle4..5, low6..8. Variant3 is Health30 Size1 slime carrying
Health2 creeper with Fuse10/ExplosionRadius3. Others include skeleton/wither
skeleton and potion passengers; some potion Items are rotten_flesh/slime_ball.
Preserve these unusual legacy payloads rather than assert functioning attacks.
Main block_entities619 and637..644 each save27 strong_harming splash potions
in barrels. Dispensers621..628 each save seven strong_harming, one
strong_slowness and one strong_poison splash potion. Fixed inventory and a
source dispenser do not prove working trap activation. No other family in
this batch has nonempty fixed Items/Book container payloads.

The inventory records distinct loot-table IDs by template and points to
pool-traces-content template_contents[template_id].loot_references for every
exact source pointer. Spawner attributes similarly link the existing full
spawner_blocks records, including SpawnData, SpawnPotentials and passengers,
without duplicating that NBT again. Selected Heavenly/Keep chest tables and
Coliseum entity drops remain separate. Legacy conversion, realized rewards,
natural populations and difficulty are not measured by this attribution.

Rebuild and focused validation use the commands above. This increment changes
only these five assessments and direct source identities. It adds no runtime,
measurement system, validator or generalized helper.

Eight focused tests pass. Inventory SHA-256:
97446b913ab5d36ba54899805ffd963ee66b2e4a733f0462fb63a751f06ee73a.

## Four mushroom designs and Illager Windmill

Fifty attributes assess giant_mushroom, mushroom_house, mushroom_mines,
mushroom_village and illager_windmill: five roots/57 selected templates.
Exact WDA archive/catalog identities and paths are those above. All root traces
have no missing templates or unresolved pool elements; this does not establish
loot-table completeness. No retained start is linked for these five. Resolved
biome intersections are Overworld only. All roots use minecraft:jigsaw with
WORLD_SURFACE_WG projection, max distance114, ignore_waterlogging, expansion
false and empty spawn_overrides. Offsets in that order are -5,0,-8,0,-2;
house/village depth6 with beard_thin; others depth7. Mushroom Mines adapt_noise
true is not evidence that a standard minecraft:jigsaw root uses WDA's codec.

Nominal geometry comes from adjacent matching connectors, not a new world
measurement. Whole rotation exchanges axes. Air/padding, failed attachment,
terrain and visibility prevent equating source envelopes with occupied/exposed
blocks. Derive origins by adding the parent's outward unit vector then
subtracting the rotated incoming connector coordinate.

- Giant red starts part0. Part0 east(31,0,0) joins part1 west(0,0,0),
  origin(32,0,0); part1 south(20,0,31) joins part2 north(20,0,0),
  origin(32,0,32); part0 south(0,0,31) joins part3 north(0,0,0),
  origin(0,0,32). Widths32/21,lengths32/21,height38 give53x38x53.
  Twin starts part0 and has analogous widths32/9,lengths32/19,height32.
  Its aligned up_south(31,31,31) joins part4 down_south(31,0,31), adding
  the second identical layer at Y32. Twin envelope41x64x51. Red/twins side
  names prevent mixing the two architectural designs into one giant envelope.
- Mushroom House starts one of four15x8x15 bottoms. Bottom down_north(7,0,7)
  joins roots up_north(15,12,15), giving roots origin(-8,-13,-8), size31x13x31.
  Bottom up_north(7,7,7) joins one of five tops down_north(15,0,15), origin
  (-8,8,-8), size31x31x31. All aligned. Union31x52x31; alternatives share
  geometry but retain their contents. Compatible spawner attachments fit inside.
- Mushroom Mines has eight32-cube architectural sections. Lower parts0..3
  form a64x32x64 square using origins(0,0,0),(32,0,0),(32,0,32),(0,0,32).
  Part0 up_north(0,31,0) joins part4 down_north(0,0,0); corresponding top
  parts4..7 sit at Y32. Named top side connectors give64x64x64 overall.
- Mushroom Village starts one45x45x45 big house. Its twelve perimeter
  connectors at Y1 target terminal small houses with one incoming connector
  also at Y1. Small sizes are11x16x11,12x16x11 and11x21x11. Their attachment
  edges are11 or12 blocks deep. The central envelope plus at most12 outside
  each face gives a conservative69x69 horizontal bound; small houses remain
  below the central45 height. This is an upper source envelope, not a predicted
  full village or measured range. Some neighboring attachments can collide.
- Windmill starts part0(48x32x34); up_south(0,31,33) joins part1
  down_south(0,0,33), giving core48x64x34. Both rigid. Fields are
  terrain_matching. Example: core west(0,9,16) joins field4 east(31,3,15),
  nominal source origin(-32,6,1). Core plus that32x4x32 field gives80x64x34
  in a level reference assembly. This example excludes other fields and is
  not a family maximum or an observed terrain layout. Core connectors accept
  field0(19x4x19) or field4; field4 additionally targets terminal small
  fields1/2/3 of12x4x12,9x4x9,6x4x6. Terrain and other attachments change
  both footprint and the whole vertical span. Preserve the64-high core
  separately rather than invent a fixed whole-field height.

Giant has two skeleton spawner pieces, each block_entities0, saving Health40,
PunchI bow and legacy tipped arrow Id2/Amplifier4/Duration80. No direct saved
entities. Mushroom House has three spawner pieces piglin_0/1/2 at
block_entities0: Health20 golden-sword brute, crossbow piglin, and brute with
crimson fungus/strong_harming potion plus potion passenger. All declare
IsImmuneToZombification1. No actual conversion/effect behavior is claimed.

Mines uses saved entities in skeleton_ranged_0, zombie_armored_0/1, entities0:
persistent skeleton Health20/bow; zombie Health20/iron pickaxe; zombie
Health19.200000762939453/diamond pickaxe. These are not physical spawners.
Village big house block_entities30,35,60 are ordinary spawners saving Health25
piglin brutes with golden swords and IsImmuneToZombification1. Small house7
entities0 is persistent Health30 turtle. A village name does not prove villagers.

Windmill has no physical spawners. Saved mob pool weights20/1/1 select
pillager/vindicator/witch pieces with persistent Health24/24/26. Fields0/4
save three persistent Health30 zombie villagers each, fields1/2 two each,
all holding iron hoes. Field3 saves one Health24 pillager, PersistenceRequired0.
These are source counts per selected piece, not live enemies or guaranteed
placement. Windmill part0 block_entities3 hopper saves one diamond, slot1.
Village small_4 block_entities1 lectern saves a ten-page writable book about
mushrooms and fictional mushroom scripture. Those fixed payloads are distinct
from table loot. No other selected template in this batch has nonempty fixed
Items/Book container contents.

Village's mushroom_village_houses processor applies two world-location tests:
existing red or brown mushroom block, random probability0.5, with always_true
incoming predicate, produces the opposite cap block. These predicates do not
merely recolor incoming cap blocks; other incoming blocks can be replaced when
the location matches. Another rule changes incoming light_gray_wool to
mushroom_stem. No entity/spawner/loot injection is declared. Original payload
preservation under every location is not asserted. Other selected processors
are empty. All non-field elements are rigid.

Preserve exact loot IDs and pointers in the existing pool-trace catalog.
Mushroom House references singular mushroom_house_barrel and
mushroom_village_weaponry, absent at their exact data/dungeons_arise/loot_table/
chests paths in the WDA packaged catalog. Plural mushroom_house_barrels exists.
These are unresolved source reward references, not permission to substitute a
similar table or claim delivered rewards. Template/pool completeness did not
prove those table paths existed. No frozen content is repaired in Item8.

Rebuild and focused validation use the commands above. Source references,
explicit derivations and existing validation suffice; no new capture/tool.

Eight focused tests pass. Semantic comparison changes only these five family
assessments and direct source identities; biome constraints, membership and
observations remain unchanged. Inventory SHA-256:
a5e17f2b481b5091b7d1add14652242bcac38356c8a9624d7dd584dd119f6c19.

## Temple, Bathhouse, Monastery and campsite attribution

Forty-six attributes integrate five roots/83 templates: abandoned_temple,
bathhouse, monastery, merchant_campsite and illager_campsite. Three families
are assessed; campsite footprint/vertical size (four attributes) remain open.
Their eight supported attributes each are integrated now. No new capture/tool.
Same pinned WDA archive and source catalogs as above, exact structure/<family>/
template paths and worldgen/structure/<family>.json. Template traces are complete.

All roots are minecraft:jigsaw, WORLD_SURFACE_WG projected, Overworld biome
compatible, max distance114, ignore_waterlogging and expansion disabled.
Abandoned offset-2, others0; Bathhouse/Illager depth5, others7. Bathhouse
beard_box, others beard_thin. Packaged adapt_noise true does not establish
execution of the WDA custom codec. Empty processors except Bathhouse middle/
top bathhouse_main, which changes incoming calcite to diorite with probability0.1.
That rule has no entity, spawner or loot injection.

Abandoned full-start world-bounds observations181/578 repeat one mountainous
seed6671238423019257953 location in run-a/run-b, chunk7,5. Box
[15,161,-17,204,290,207] yields190x130x225 by inclusive subtraction. Its temple
core is31x48x31 but terrain-matching roads greatly enlarge the whole envelope.
Monastery observations183/580 repeat one location in the same seed, chunk5,8,
box[51,241,83,80,281,157],30x41x75. These are full start-chunk piece envelopes,
not occupied/exposed blocks, complete placement of all referenced pieces,
family-wide extrema or independent samples. Existing observation links remain.

Bathhouse uses one base, middle and top. All are31x31 horizontally, with central
aligned up_south/down_south connectors at(15,height-1,15)/(15,0,15).
Base heights are12,11,11,13,6,21; middle17,17,17,22; top13,19,27,20,13,21,21.
Origins stack at YbaseHeight and YbaseHeight+middleHeight, so nominal complete
height is36..70. Small spawner pieces fit the architecture. No retained start
exists; this is a source range, not exposed height or observed generation.

Abandoned illusioner_normal_0 entities0 saves Health32/PersistenceRequired0;
skeleton_armored_0/1 entities0 save Health20/PersistenceRequired1. All save
empty hands. Root full-bounds monster spawn override is stray weight1/group1.
That conditional natural list is separate from authored saved entities; no
physical spawner blocks occur. Monastery villager_normal_0 and
iron_golem_normal_0 entities0 save Health20/100, both PersistenceRequired0.
No authored monster or spawner occurs there; ordinary spawning remains possible.

Bathhouse spawner_0/1/2 block_entities0 select weight5/5/1: Health40 husk with
legacy invisibility and potion passenger, Health20 skeleton, cold frog carrying
Health20 PowerIII-bow skeleton. Full NBT remains in source spawner_blocks.
Paintings/item frames/armor stands are decoration and fixed items, not enemies.
Middle3 entities2/3/4 are tropical fish Health3. Entities8 is area_effect_cloud,
Radius5,Duration200000390, legacy Effects Id10/11,Amplifier1,Duration200.
Effective conversion and full cloud lifetime are not asserted.

Bathhouse base3 block_entities24 has a five-page writable book of golden-themed
sayings; top0 block_entities4 a three-page written book about a steam machine.
Middle3 block_entities9 saves nine splash potions named Bathhouse's Curse,
weakness plus legacy effects Id4/A3,Id9/A5,Id33/A1,Duration1200. Source contents
are not proof of dispenser activation or working potion effects. Item frames
include food/potions and middle3 entities19 enchanted_golden_apple; middle3
armor stand entities16 has diamond helmet. These are separate from table loot.
Other selected templates in this batch have no nonempty fixed Items/Book payload.

Merchant villager_normal_0 entities0 saves Health20/PersistenceRequired0. Its
iron_golem_normal_0 template is1x2x1, with only one jigsaw and no saved entities
or spawner. Do not invent an iron golem from the filename. Villagers pool weights
are1 for that empty named piece and2 for villager; incoming connector names still
control compatibility. Illager enemies pool weights1/3/2 select persistent
vindicator Health24/iron axe, pillager Health24/crossbow, and pillager
Health50/MultishotI QuickChargeII crossbow. Deco0 entities0 adds persistent
Health20 zombie villager. Neither campsite has physical spawner blocks.

Campsite geometry remains a specific four-attribute gap. Existing sources show
15-block street modules with terrain_matching projection and rigid tents,
branching under root depths7/5. No retained start is linked. Merchant starts
street4_main15x6x15, Illager street6_main15x7x15. Single-street or single-tent
examples would not establish a complete camp envelope, so they are not marked
assessed. Resolve a supported whole-layout approximation using the existing
sources before considering any additional measurement.

Rebuild and focused validation use the commands above. Exact source loot
pointers and full spawner NBT remain in pool-traces-content; table IDs and
family-specific descriptive attribution are integrated into the inventory.

Eight focused tests pass. Only the five intended families and direct source
identities change. Inventory SHA-256:
3bb272edbb4c9c7213be4a81ce924d2292862b1bc5d5e4c169d92f7b7f1d5b8d.

## Predeclared campsite geometry capture

Resolve the four remaining Merchant/Illager Campsite geometry attributes with
one ordinary-seed42 run, two roots,81 requested chunks per target,162 total,
timeout900 seconds. Existing source modules establish branching and terrain
matching but do not provide a complete observed camp; no retained starts exist.
This narrowly addresses required assembled dimensions. Do not measure pacing,
frequency, all-layout extrema or gameplay. No new tool/schema is required.
Reuse fresh hash-verified Item6 materialization, existing Chunky instrument,
readiness, correlated save and clean stop. Preserve failed attempts. Decode the
stopped world, require full start chunks, derive bounds with existing
item8_world_bounds.observed_bounds, retain archive manifest and tested local/
published-download restores using the same commands as the Towns Village run.

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
  --target instances/item8/wda-camps-geometry-r1 \
  --log-path evidence/raw/item8/wda-camps-geometry-r1/console.log \
  --captured-config evidence/raw/item8/wda-camps-geometry-r1/configuration \
  --receipt evidence/raw/item8/wda-camps-geometry-r1/run.json \
  --timeout-seconds 900 \
  --structure dungeons_arise:merchant_campsite \
  --structure dungeons_arise:illager_campsite
```

This declaration does not claim a successful run or resolved geometry.

### Campsite geometry result and custody

Run source revision f9e5fa8d57ecd3e5537999a9ca23ba75bcff9b98. Both targets
completed with readiness, correlated flushed save, clean exit0 and accepted
frozen configuration. No runtime remains. Decode retained2,768 chunks including
locate-created/partial chunks; that count is not the requested sampling denominator.

| Root | Decoded line | Start chunk XZ | Pieces | Envelope | Size XYZ |
| --- | --- | --- | --- | --- | --- |
| dungeons_arise:merchant_campsite | 594 | -393,302 | 50 | -6378,63,4787,-6222,69,4906 | 157,7,120 |
| dungeons_arise:illager_campsite | 2179 | 407,-296 | 81 | 6452,65,-4825,6550,77,-4699 | 99,13,127 |

Both saved starts are in full chunks. Bounds include all saved piece boxes,
not occupied volume, exposed tent height or proof distant pieces were fully
placed. These are two illustrative family examples, not extrema or pacing.
They resolve the four geometry attributes left open above. The two dimension
assessments now also reference these observations. Baseline world_observations
indexes remain unchanged because this is a separately archived supplemental run.

Archive264 files,4,288,483 bytes,30,970,089 uncompressed bytes. SHA-256:
3b5e0026b68889f5d3a4267a966df3e40429431f82ea2fbd219d48da9db4a4ae.
Decoded chunks SHA-256:
dd66df3963caf928ceb11b9bd89ab816ae0723a6efe4fad1e86fc308eab99b45.
The archive retains stopped-world files excluding session.lock, complete console
log, decoded records, sanitized configuration, sanitization receipt and run
receipt. Retained warnings include unknown legacy forge:entity_gravity and
Better Caves AquiferContext messages; successful lifecycle is not evidence
that all gameplay/compatibility warnings are resolved. No new balance claim.

Executed preservation commands (use absent destinations for reproduction):

```sh
uv run python -c 'from pathlib import Path; from tools.stage_item7_world import copy_world_boundary; copy_world_boundary(Path("instances/item8/wda-camps-geometry-r1"), Path("evidence/raw/item8/wda-camps-geometry-r1/world"))'
uv run -m tools.decode_item7_world evidence/raw/item8/wda-camps-geometry-r1/world --output evidence/raw/item8/wda-camps-geometry-r1/chunks.jsonl
uv run -m tools.archive_item7_evidence create --root evidence/raw/item8/wda-camps-geometry-r1 --archive evidence/raw/item8/item8-wda-camps-geometry-r1-f9e5fa8d.tar.gz --manifest evidence/item-8/raw-custody/wda-camps-geometry-r1-manifest.json --revision f9e5fa8d57ecd3e5537999a9ca23ba75bcff9b98
uv run -m tools.archive_item7_evidence restore --archive evidence/raw/item8/item8-wda-camps-geometry-r1-f9e5fa8d.tar.gz --manifest evidence/item-8/raw-custody/wda-camps-geometry-r1-manifest.json --target evidence/raw/item8/wda-camps-geometry-r1-restored --receipt evidence/item-8/raw-custody/wda-camps-geometry-r1-local-restore.json
gh release download item-8-wda-camps-geometry-2026-09-07-r1 --repo copeugne/mcpack --dir evidence/raw/item8/wda-camps-geometry-download --pattern item8-wda-camps-geometry-r1-f9e5fa8d.tar.gz
uv run -m tools.archive_item7_evidence restore --archive evidence/raw/item8/wda-camps-geometry-download/item8-wda-camps-geometry-r1-f9e5fa8d.tar.gz --manifest evidence/item-8/raw-custody/wda-camps-geometry-r1-manifest.json --target evidence/raw/item8/wda-camps-geometry-downloaded-restore --receipt evidence/item-8/raw-custody/wda-camps-geometry-r1-downloaded-restore.json
```

Both restores verified264 files. Local copies share a disk; the separate durable
copy is the [published archive](https://github.com/copeugne/mcpack/releases/tag/item-8-wda-camps-geometry-2026-09-07-r1).
The remote tag was verified to resolve to the run source revision above.
To reproduce the table from either restored decoded stream, use existing logic:

```sh
uv run python - <<'PY'
from pathlib import Path
from mcpack_evidence.item7_nbt_models import ChunkRecord
from mcpack_evidence.item8_world_bounds import observed_bounds
source = Path('evidence/raw/item8/wda-camps-geometry-downloaded-restore/chunks.jsonl')
for line, raw in enumerate(source.open(), 1):
    for observation in observed_bounds(ChunkRecord.model_validate_json(raw)):
        if observation['structure_id'] in ('dungeons_arise:merchant_campsite', 'dungeons_arise:illager_campsite'):
            print(line, {key: value for key, value in observation.items() if key != 'piece_boxes'}, 'pieces', len(observation['piece_boxes']))
PY
```

Eight focused tests pass. Semantic comparison changes only the two campsite
geometry/dimension assessments, direct evidence identities and builder input.
Inventory SHA-256:
201360490224b28829da9a67a2de47898a0262ed44d10138e4ae046a813799d7.

## Aviary, Fort, Infested Temple, Kisegi and Asylum content

Forty attributes integrate five roots/133 templates: aviary, illager_fort,
infested_temple, kisegi_sanctuary and plague_asylum. Their ten footprint/height
attributes remain open. Do not count these families assessed yet. Same exact
WDA archive/catalog paths as above. Template traces have no missing components.
No retained starts exist and no new runtime/tool was added for this content.

Aviary biome intersection is End only; others Overworld. All roots use
minecraft:jigsaw,depth7,ignore_waterlogging,expansion false. Aviary starts at
absolute Y50 with no heightmap; its piece-bounded monster list is phantom
weight60/group2..3. Illager Fort projects WORLD_SURFACE_WG offset-7,beard_thin.
Infested/Kisegi project that heightmap offset-32,step fluid_springs,max distance104;
their full-bounds ambient,creature,monster lists are empty. Those normal spawn
lists do not remove authored trial encounters. Asylum is absolute Y0, no
heightmap,step strongholds,adaptation bury,max distance104. Aviary/Fort distance114
and step surface_structures. Fort/Asylum root spawn_overrides are empty.

Aviary ordinary spawner pieces each use block_entities0: charged_creeper_0
powered1/Health30; guardian_3 skeleton Health120 with guardian passenger;
phantom_0 Size40; skeleton_melee_1 Health120; skeleton_ranged_0 Health100.
Direct end crystals occur in parts10/11/12/13 in counts5/2/4/4, all Invulnerable0.
Part15 saves turtle Health30; other direct entities include paintings and armor
stands. These are potential hazards/decorations, not a measured live encounter.
Part5 block_entities20 and part7 block_entities17 droppers save lingering
potions, separately from table rewards; source potion NBT remains preserved.

Fort saved evoker/illusioner/pillager/vindicator pieces have Health24/32/60/60.
Its four cave-spider ordinary spawners are part4 block_entities5/8,part5 index1,
part6 index2. A spawners pool name does not make the direct saved entities into
spawner blocks. No trial spawners occur in Aviary, Fort or Asylum.

Infested has five trial-spawner pieces. Every piece block_entities0 contains
normal_config and ominous_config, with separate potentials, rewards and counts.
Spawner0 normal mode uses cave spider and guaranteed_omen reward; ominous uses
cave spider and ominous reward. Other pieces use cave spider, spider with cave
spider passenger, skeleton or wither skeleton, and normal/ominous reward tables.
The per-player additions and mode totals remain source declarations, not live
populations. Direct saved paintings are not enemies. Three vault alternatives
have exact configs: normal trial_key model2341668, treasure trial_key2341669,
ominous ominous_trial_key2341670, each count1 and its own vault table.

Kisegi has twelve trial-spawner alternatives with separate normal/ominous
configs and rewards. Types include cave spider; spider carrying skeleton;
skeleton; wither skeleton; wither skeleton carrying potion. Every complete
config and passenger chain is preserved in source spawner_blocks. Four vault
configs use normal trial_key2341671, normal-treasure trial_key2341673,
ominous key2341672, ominous-treasure key2341674. All config key counts are1;
normal-treasure lore saying two keys does not prove a configured two-key cost.
Direct main entities13/14 are chicken Health3 and an egg item, alongside
paintings/armor stands. Other rooms include item frames and display equipment.

Infested processor rules change calcite to smooth_quartz/diorite, spruce planks
to stripped_spruce_wood, cherry leaves to cobweb, and append decorated-pot loot
from pots/infested_temple/infested_temple_pots. Kisegi has analogous material
rules, magenta_glazed_terracotta to TNT, and append_loot assignments for pots
and suspicious sand/gravel using its pots and archeology tables. Source TNT
is not proof of triggered explosions. Neither processor injects mob/spawner
entities; all other selected processors in this batch are empty. Exact
processor JSON paths are worldgen/processor_list/<family>_main.json.

Asylum ordinary spawner pieces use block_entities0: evoker_fangs, skeleton
Health50, skeleton Health40 with potion passenger, wither skeleton Health40,
witch, husk Health4. An evoker_fangs entity is not an evoker mob. No direct
saved entities occur in its selected templates. Room4_pit block_entities14
contains one strong_slowness splash potion in dispenser slot4; it does not
prove a working trap. Existing source spawner timing and gear remain linked.

Loot attribution retains exact source pointers, including weighted
loot_tables_to_eject arrays in both trial modes. These arrays must not be
flattened into an invented common reward. Vault configs are recorded separately
from spawners and ordinary container tables. Fixed payload locations identify
template and block-entity index for Items/Book, including Infested bookshelves,
firework dispensers and brewing stands; Kisegi books, shelves, potion/arrows
and brewing stands. Inspect the exact preserved NBT for contents and component
format. Decorative gear and fixed objects are distinct from randomized rewards.
No conversion, reward realization, encounter balance or gameplay pass is claimed.

Remaining work for these five families is ten geometry attributes: derive
connected envelopes for Aviary/Fort and main/interior layouts for Infested/Kisegi;
resolve a supported whole-layout approximation for Asylum's branching rooms.
Rebuild and focused validation use the existing commands above.

Eight focused tests pass. Repeated string-table pointers are kept in the
existing catalog; the inventory lists distinct table IDs and preserves weighted
trial reward lists and their exact pointers. Only these five content assessments
and direct source identities change; geometry remains open. Inventory SHA-256:
d38dcfb6cbbe7f4ba2eb8fe4ebced9630a4d83985b94c6a959a29d89c162831e.
