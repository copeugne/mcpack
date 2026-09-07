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

## Aviary and Fort geometry

Four attributes finish these two families from the same immutable template and
packaged-JSON catalogs identified above. Exact archive:
DungeonsArise-1.21.1-2.1.68-release.jar. Template paths are
`data/dungeons_arise/structure/<family>/<family>_<piece>.nbt`.
Inspect document.size and block_entities[].nbt jigsaw name/target/joint,
block_entities[].pos and the indexed palette orientation. Pools under
worldgen/template_pool/eerie/aviary and fortified/illager_fort use rigid
projection, empty processors and empty fallbacks.

Aviary parts0..26 all measure48x32x48. Relative to part4 origin(0,0,0),
parts0..8 have XZ origins respectively(-48,-48),(0,-48),(48,-48),(48,0),
(0,0),(-48,0),(-48,48),(0,48),(48,48). Side pairs0/1,2/3,4/5,6/7 join
center4 to1,3,7,5; pairs8/9,10/11,12/13,14/15 join the corners. Every
boundary connector is at0 or47 and joins an adjacent block, giving48 steps.
Parts9..17 repeat at Y32 with side names suffixed_top; parts18..26 repeat
at Y64 with suffix_top_two. Centers4/13/22 join aligned up_west/down_west
at(23,31,24)/(23,0,24), names18/19 and21/20. Start pool selects part13.
Thus the nominal full assembly is144x96x144, with at most four architectural
edges from the starting center, within depth7. Five1x2x1 spawner alternatives
have their incoming connector at(0,1,0); upward receivers keep their two-block
height inside the architecture. This is a source envelope, not a retained start.

Fort lower parts0/1/2/3 have origins(0,0,0),(32,0,0),(32,0,27),(0,0,27)
and sizes32x43x27,23x43x27,23x43x20,32x43x20. Side pairs0/1,3/2,4/5,6/7
join matching boundaries. Aligned upper pairs0/1,3/2,4/5,6/7 (side_up prefix)
place parts4/5/7/6 above those lower parts at Y43. Their height17 yields
55x60x47. Note that part6 belongs above part3, not part2.

All nine room alternatives are9x9x14, incoming down_north at(4,0,13).
Aligned receivers yield these global XZ ranges: part0 north receiver(27,17)
gives23..31,4..17; part0 west(22,22) gives9..22,18..26; part1 east(0,22)
gives32..45,18..26; part3 south(27,0) gives23..31,27..40. Receiver Y values
are1,11,22,32 (north omits22); room origins are receiver Y+1 and maximum
room Y is41. Four1x3x1 entity alternatives attach above receivers inside
these rooms or lower architecture and remain within the full envelope.
Consequently interior alternatives do not enlarge55x60x47. Horizontal
rotation exchanges the footprint axes. Placement success and occupied-block
volume are not established by these source bounding boxes.

Rebuild with `uv run -m tools.build_item8_inventory --output <absent-path>`.
Focused check: `uv run pytest -q tests/item8/test_wda_provider_scope.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py`.
Semantic comparison permits only the two families' geometry attributes,
corresponding grouping decisions and the decisions input hash to change.

## Infested Temple and Kisegi geometry

Four geometry attributes complete these two families using the same immutable
WDA archive and catalogs cited above. Exact template paths:
`data/dungeons_arise/structure/infested_temple/infested_temple_<piece>.nbt`
and `data/dungeons_arise/structure/kisegi_sanctuary/kisegi_sanctuary_<piece>.nbt`.
Read size, jigsaw positions/name/target/joint and indexed palette orientations.
The respective start pools select main_0 only; all selected pools use rigid
projection and empty fallbacks. Their material/loot processors were already
attributed above and do not append architectural pieces.

Infested main_0 measures101x181x101. Its ten level receivers at(50,Y,50),
Y70,78,86,94,102,110,118,126,134,142 alternate aligned up_east/up_west.
All five level alternatives measure39x8x39 with incoming down_north at
(19,1,19). Rotation preserves the centered square: global X/Z31..69 and
origin Y equal to receiver Y because incoming local Y is1. Maximum level Y149.
Level room receivers have local X/Z coordinates between7 and31, at Y0.
All ten13x6x13 rooms have centered incoming down_west at(6,0,6), and the
parent joint is rollable. Every allowed horizontal rotation keeps rooms
inside local X/Z1..37 and Y1..6 of the level. Five trial-spawner and three
vault alternatives are1x2x1, incoming down at(0,1,0). Their upward receivers
in rooms/levels leave these attachments inside those pieces. Main receivers
are X37..63,Z36..63,Y55..152, also contained. No compatible child enlarges
the main envelope101x181x101.

Kisegi main_0 measures125x215x125. Its four architectural receivers point
down_south and are aligned. Corresponding rooms point up_south, so there
is no horizontal rotation relative to main. Matching adjacent connector
positions give these origins and inclusive boxes:

| Piece | Origin XYZ | Size XYZ | Inclusive maximum XYZ |
|---|---|---|---|
| lower_room_0 | 0,90,44 | 125,13,81 | 124,102,124 |
| middle_room_0 | 0,103,0 | 125,13,125 | 124,115,124 |
| top_room_0_0/1/2 alternatives | 27,148,47 | 71,13,31 | 97,160,77 |
| top_room_1_0 | 27,161,47 | 71,13,31 | 97,173,77 |

Main receiver positions are(62,91,124),(62,104,124),(62,149,62),
(62,162,62); incoming room positions are(62,0,80),(62,0,124),
(35,0,15),(35,0,15). The lower and middle room connectors sit at local
Y0 despite pointing up. The origin therefore is main receiver Y minus1,
not minus room height. All boxes still lie inside main.

Twelve trial-spawner and four vault alternatives measure1x2x1 and have
incoming down_west at(0,1,0). Upward receivers in lower/middle/top rooms
have local Y at most7/9/9, respectively, keeping attachments within their
13-block height. Main receivers occupy X18..99,Z19..112,Y32..195 and
remain contained. Thus the nominal source envelope is125x215x125.
Neither result proves placement success, occupied-block volume or live
encounter behavior. No retained start or additional capture is claimed.

Rebuild and focused check commands are the same as the preceding geometry
increment. Semantic comparison changes only these two families' geometry,
corresponding grouping decisions and the input identity.

## Plague Asylum geometry target declaration

Remaining requirement: approximate whole-family footprint and vertical size.
The retained world-bounds catalog contains no Plague Asylum start. Packaged
33 templates establish a branching rigid assembly, not a fixed envelope:
start corridor_4_crossing_pit17x18x17 links corridor, room and passage pools;
stairway changes elevation by9, rooms reach34x18x17, and terminal cells attach
to passages. Individual piece dimensions cannot substitute for whole-layout
geometry. A source maximum-distance limit alone is not a useful example size.

Reuse the existing capture path for exactly one target, seed42,
`dungeons_arise:plague_asylum`, requesting81 chunks with timeout900 seconds.
This supplies one illustrative saved-piece envelope, not extrema, density,
encounter balance, occupied volume or complete distant-piece placement.
No new measurement system or generalized geometry simulator is justified.
Use fresh verified frozen materialization, readiness, correlated flushed save,
clean stop, decoded full start, existing observed_bounds, immutable archive
and verified local/published-download restores. Preserve failures and warnings.

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
  --target instances/item8/wda-asylum-geometry-r1 \
  --log-path evidence/raw/item8/wda-asylum-geometry-r1/console.log \
  --captured-config evidence/raw/item8/wda-asylum-geometry-r1/configuration \
  --receipt evidence/raw/item8/wda-asylum-geometry-r1/run.json \
  --timeout-seconds 900 \
  --structure dungeons_arise:plague_asylum
```

This declaration does not claim a successful capture or resolved geometry.

### Plague Asylum result and custody

Source revision9a3221a528768f711ce50a8d4f824e2793ca4a67. The one requested
seed42 target completed, ready, correlated flushed save, clean exit0,
accepted frozen configuration. No runtime remains. The decoded stream has
1,803 records including locate-created/partial chunks, not a sampling denominator.
Line1729 is a full Overworld start in chunk305,-99, with171 piece boxes and
inclusive envelope[4779,-37,-1652,4974,16,-1480], size196x54x173.
These resolve the two geometry attributes as an illustrative whole-start
example only. Baseline world_observations indexes remain unchanged; the
supplemental observation is bound through the archive manifest in attributes.

Archive257 files,3,002,188 bytes,20,820,169 uncompressed bytes. SHA-256:
770e3993d9d9d7a9d3668102f4bf0fbcc9d9c5b4b5191ec468ef9b0385e89fe1.
Decoded stream SHA-256:
f31c4975b34477a761e33b4190b5b317010b18b8e0c2955acd0f5ea6a64e220c.
Manifest SHA-256:
32f56868b26ec38c2ea67b4e6fe3758541683c3037503e5869b19eee899d4b9d.
The archive retains stopped world excluding session.lock, logs, decoded records,
sanitized configuration and its sanitization receipt, and complete run receipt.
Warnings, including overload and source probability warnings, remain in logs;
this geometry observation does not disposition them as a gameplay pass.
One offline inspection initially imported the nonexistent item7_decode module;
it failed before reading records or changing evidence. The corrected existing
model import below produced the result. No runtime attempt was rejected.

Both local and published-download restores verified257 files. Local copies
share one disk; independent storage is the
[published archive](https://github.com/copeugne/mcpack/releases/tag/item-8-wda-asylum-geometry-2026-09-07-r1).
Its remote tag was verified against the exact source revision.

```sh
uv run python -c 'from pathlib import Path; from tools.stage_item7_world import copy_world_boundary; copy_world_boundary(Path("instances/item8/wda-asylum-geometry-r1"), Path("evidence/raw/item8/wda-asylum-geometry-r1/world"))'
uv run -m tools.decode_item7_world evidence/raw/item8/wda-asylum-geometry-r1/world --output evidence/raw/item8/wda-asylum-geometry-r1/chunks.jsonl
uv run -m tools.archive_item7_evidence create --root evidence/raw/item8/wda-asylum-geometry-r1 --archive evidence/raw/item8/item8-wda-asylum-geometry-r1-9a3221a5.tar.gz --manifest evidence/item-8/raw-custody/wda-asylum-geometry-r1-manifest.json --revision 9a3221a528768f711ce50a8d4f824e2793ca4a67
uv run -m tools.archive_item7_evidence restore --archive evidence/raw/item8/item8-wda-asylum-geometry-r1-9a3221a5.tar.gz --manifest evidence/item-8/raw-custody/wda-asylum-geometry-r1-manifest.json --target evidence/raw/item8/wda-asylum-geometry-r1-restored --receipt evidence/item-8/raw-custody/wda-asylum-geometry-r1-local-restore.json
 gh release download item-8-wda-asylum-geometry-2026-09-07-r1 --repo copeugne/mcpack --dir evidence/raw/item8/wda-asylum-geometry-download --pattern item8-wda-asylum-geometry-r1-9a3221a5.tar.gz
uv run -m tools.archive_item7_evidence restore --archive evidence/raw/item8/wda-asylum-geometry-download/item8-wda-asylum-geometry-r1-9a3221a5.tar.gz --manifest evidence/item-8/raw-custody/wda-asylum-geometry-r1-manifest.json --target evidence/raw/item8/wda-asylum-geometry-downloaded-restore --receipt evidence/item-8/raw-custody/wda-asylum-geometry-r1-downloaded-restore.json
uv run python - <<'PY'
from pathlib import Path
from mcpack_evidence.item7_nbt_models import ChunkRecord
from mcpack_evidence.item8_world_bounds import observed_bounds
source = Path('evidence/raw/item8/wda-asylum-geometry-downloaded-restore/chunks.jsonl')
for line, raw in enumerate(source.open(), 1):
    for observation in observed_bounds(ChunkRecord.model_validate_json(raw)):
        if observation['structure_id'] == 'dungeons_arise:plague_asylum':
            print(line, {key: value for key, value in observation.items() if key != 'piece_boxes'}, 'pieces', len(observation['piece_boxes']))
PY
```

Rebuild and eight focused checks use the existing commands above. Semantic
comparison changes only Asylum geometry and direct evidence/input identities.

## Bandit, Pub, Nest and Thornborn content

Forty attributes integrate five families with285 available templates:
Bandit Towers26, Bandit Village31, Greenwood Pub35, Mechanical Nest160,
Thornborn Towers33. Their ten geometry attributes remain open; none of these
five is counted assessed yet. No retained starts occur in world-bounds.
Use the same immutable WDA archive and template/packaged/trace catalogs above.
Exact paths are data/dungeons_arise/structure/<family>/<family>_<piece>.nbt,
worldgen/structure/<family>.json, and the traced template_pool paths.
All effective biome intersections select Overworld. Root spawn_overrides are
empty; natural spawning is separate from the authored sources below.

Bandit Towers starts at absoluteY135, Mechanical Nest190, Thornborn130,
without heightmap projection. These heights are not offsets above terrain.
Bandit Village projects WORLD_SURFACE_WG at offset0 with beard_thin;
Greenwood projects that heightmap at offset-18. Visual discoverability records
source inference about exterior silhouettes and concealed interiors, not
human sight distance or exploration pacing.

Bandit Towers has seven dedicated ordinary-spawner alternatives, block_entities0:
ranged_illager0 pillager Health40, ranged_skeleton1 Health26, skeleton_assassin0/1
Health16/5, skeleton_juggernaut0/1/2 Health46/24/40. Assassin1 saves legacy
invisibility; juggernaut2 has potion passenger. Three other ordinary spawners
occur in crossing5 indices8/18 and part0 index14: firework rocket carrying
persistent husk, min/max delay24000 and count3. These are authored payloads,
not proof of a functioning rocket encounter. No direct saved entities or
nonempty Items/Book payloads. Exact table references chests/desert_city_big,
chests/desert_city_medium,chests/desert_city_small are absent from the selected
WDA loot_table catalog; preserve unresolved reward references, not invented loot.

Bandit Village hoglin0/1 block_entities0 are ordinary spawners with
zombification-immune hoglin carrying wither skeleton/potion or husk.
House6 index1 spawns firework rocket carrying persistent husk. Archer0 and
assassin0 separately save persistent skeleton Health15 and husk Health10.
No nonempty fixed Items/Book payloads in available templates. Referenced
bandit_village_deco_3 is absent; this limits available-template absence claims.

Greenwood spawner0/1 ordinary payloads are skeleton Health30 with potion
passenger and zombie Health2. Furniture/rooms save17 villagers Health20 and
one Health19, PersistenceRequired0; these are counts across alternatives,
not one pub population. Room3 entities1 and room4 entities0 each save
persistent vindicator Health99 with empty hands. Two saved item frames are
decoration. Stairs2 block_entities2 has a ten-page writable book. Processor
greenwood_pub_main replaces red_stained_glass with structure_void, mud_bricks
with packed_mud at0.2, stone_bricks with mossy_stone_bricks at0.15. It does
not append rewards or entities.

Mechanical Nest ordinary spawner0..5 block_entities0 save skeleton Health40;
skeleton Health40/firework passenger; two equal-weight zombie Health6 payloads;
wither skeleton Health80; ravager Health60/creeper Health40 passenger; skeleton
Health20. Preserve full gear and both zombie payloads in existing spawner_blocks.
Crossing8 indices6/7/8/10/11/12 additionally spawn potion carrying lightning_bolt.
Crossing9 entities7..14 are eight persistent powered creepers Health20 with
legacy effects12/13. Bridge10 entities0/1/4/5 are effect clouds with legacy
Id25, duration60 effect, cloud durations1999980 or2001380 and positive ages;
this is not a claim of persistent live levitation. Roof2 entities6/7/8 are
glow squids with Health37/33.459999084472656/38. Frames, paintings and armor
stands are decoration. No trial spawners occur in the available batch templates.

Nest nonempty Items/Book locations are integrated with exact indices:
bridge5 barrels2..5 hold coarse dirt/rotten flesh/poisonous potatoes;
deco_machines4 index1 flint_and_steel; deco_machines5 index1 nine strong_harming
splash potions; mecha4 index2 lever; towers8_special index14 six strong_slowness
splash potions. Bridge11_special index18 holds writable book without pages;
roof0 index1 has18 pages. These fixed payloads are distinct from table rewards.
Processor mechanical_nest_main modifies campfire/lantern and mud/copper blocks
and then replaces magenta_glazed_terracotta with TNT. It appends neither loot
nor entities. Neither source TNT nor potion contents prove a working trap.

Thornborn seven ordinary spawner alternatives (block_entities0) save skeleton
Health36, skeleton Health36/potion passenger, ranged skeleton without explicit
Health, phantom Health30 Size5/skeleton Health60 passenger, top juggernaut
Health50, top ranged Health40 and witch. No direct entities or nonempty fixed
Items/Book payloads in available templates. Referenced
thornborn_towers_hanging_bridge_2_medium_terminator is absent. Bandit and
Thornborn selected template processors are empty; an empty pool element is
not an uninspected processor. Missing templates are retained in grouping data.

Loot-table IDs and nonempty fixed payload pointers are now in authoritative
attributes. Complete passenger/effect/gear/timing NBT stays in the retained
catalog at template_contents[template_id].spawner_blocks or the exact template
block_entities/entities index. Legacy serialization is not live-conversion
proof. Required next work is ten whole-layout geometry attributes, using
existing source evidence before any justified capture. No new measurement or
tooling was added. Rebuild and focused test commands remain those above.

## Five branching WDA geometry targets

Ten remaining geometry attributes require whole-layout examples for Bandit
Towers, Bandit Village, Greenwood Pub, Mechanical Nest and Thornborn Towers.
None has a retained start. Available templates establish branching, not fixed
main/interior containment. Towers starts with crossing0/1/2, each31x18x31,
with vertical main links and bridges to more crossings. Village starts with
terrain-matching street2. Pub main31x48x31 has an exterior north stairs
connector at(24,3,0); stairs lead to repeating/branching hallways and rooms
outside main. Nest start31x48x31 has three bridge exits leading to crossing
networks. Thornborn main17x17x17 links supports, tops, bridges and hanging
architecture. Main-only dimensions or maximum-distance limits would not
supply useful whole-layout approximations. Source simulation would require
more work and machinery than the existing capture path.

Reuse one fresh frozen seed42 run, five targets in the order below,81 requested
chunks each,405 total, timeout900 seconds. Require full saved starts, correlated
flushed save, clean exit and configuration parity. Existing observed_bounds
provides inclusive saved-piece envelopes, not occupied volume, placement of
every distant piece, family extrema, density or gameplay. Preserve missing
Village/Thornborn template references and failures; do not repair frozen
content. Reuse existing archive/local/download restore workflow. No new tool.

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
  --target instances/item8/wda-branching-geometry-r1 \
  --log-path evidence/raw/item8/wda-branching-geometry-r1/console.log \
  --captured-config evidence/raw/item8/wda-branching-geometry-r1/configuration \
  --receipt evidence/raw/item8/wda-branching-geometry-r1/run.json \
  --timeout-seconds 900 \
  --structure dungeons_arise:bandit_towers \
  --structure dungeons_arise:bandit_village \
  --structure dungeons_arise:greenwood_pub \
  --structure dungeons_arise:mechanical_nest \
  --structure dungeons_arise:thornborn_towers
```

This declaration does not claim a successful run or resolved geometry.

### Five branching geometry results and custody

Source revisionedd25249b8189e322c174a662bdee41304a87524. All five targets
completed, with readiness, correlated flushed save, clean exit0 and accepted
frozen configuration. Decode retained5,681 records including locate-created
and partial chunks; this is not the405 requested-chunk denominator.

| Family | Decoded line | Start chunk XZ | Pieces | Envelope | Size XYZ |
|---|---|---|---|---|---|
| Bandit Towers | 3666 | -1397,-899 | 285 | -22453,36,-14423,-22276,227,-14299 | 178,192,125 |
| Bandit Village | 1512 | -492,202 | 99 | -7914,144,3179,-7837,180,3258 | 78,37,80 |
| Greenwood Pub | 659 | -493,408 | 78 | -7952,37,6498,-7870,94,6569 | 83,58,72 |
| Mechanical Nest | 5401 | 801,8 | 796 | 12687,104,29,12888,295,257 | 202,192,229 |
| Thornborn Towers | 2025 | -91,-796 | 191 | -1511,27,-12798,-1394,206,-12635 | 118,180,164 |

All starts are in full chunks. Bounds include saved piece boxes, not occupied
volume, exposure or proof all distant pieces placed. These illustrative
examples resolve ten geometry attributes. They do not erase missing packaged
components or reward references, nor assert family-wide extrema or gameplay.
Baseline world_observations indexes are unchanged; supplemental attributes
bind the exact archive manifest and decoded lines. Downloaded restore yielded
the same five observations through existing observed_bounds logic.

Archive357 files,12,164,719 bytes,65,952,568 uncompressed bytes. SHA-256:
64730ecea5cd213c448ee4b9d6496bc30f14e120b4eb833bb42e6d7986372659.
Decoded SHA-256:
89088b9f0efac7aee8edb3849d9aabafe4da36907e856fabef13fa4aedb58231.
Manifest SHA-256:
4a5c415d0755a3815790d27ebf15aee05d9a82b68caf9d8ab4faad7267b20ae1.
Stopped world excludes session.lock; archive includes logs, decoded records,
sanitized configuration and its receipt, and lifecycle/configuration receipt.
Runtime warnings remain preserved, not treated as a gameplay pass. Both local
and downloaded restores verified357 files. Local copies share one disk;
independent copy is the
[published archive](https://github.com/copeugne/mcpack/releases/tag/item-8-wda-branching-geometry-2026-09-07-r1).
Remote tag matches the source revision. No runtime remains.

```sh
uv run python -c 'from pathlib import Path; from tools.stage_item7_world import copy_world_boundary; copy_world_boundary(Path("instances/item8/wda-branching-geometry-r1"), Path("evidence/raw/item8/wda-branching-geometry-r1/world"))'
uv run -m tools.decode_item7_world evidence/raw/item8/wda-branching-geometry-r1/world --output evidence/raw/item8/wda-branching-geometry-r1/chunks.jsonl
uv run -m tools.archive_item7_evidence create --root evidence/raw/item8/wda-branching-geometry-r1 --archive evidence/raw/item8/item8-wda-branching-geometry-r1-edd25249.tar.gz --manifest evidence/item-8/raw-custody/wda-branching-geometry-r1-manifest.json --revision edd25249b8189e322c174a662bdee41304a87524
uv run -m tools.archive_item7_evidence restore --archive evidence/raw/item8/item8-wda-branching-geometry-r1-edd25249.tar.gz --manifest evidence/item-8/raw-custody/wda-branching-geometry-r1-manifest.json --target evidence/raw/item8/wda-branching-geometry-r1-restored --receipt evidence/item-8/raw-custody/wda-branching-geometry-r1-local-restore.json
gh release download item-8-wda-branching-geometry-2026-09-07-r1 --repo copeugne/mcpack --dir evidence/raw/item8/wda-branching-geometry-download --pattern item8-wda-branching-geometry-r1-edd25249.tar.gz
uv run -m tools.archive_item7_evidence restore --archive evidence/raw/item8/wda-branching-geometry-download/item8-wda-branching-geometry-r1-edd25249.tar.gz --manifest evidence/item-8/raw-custody/wda-branching-geometry-r1-manifest.json --target evidence/raw/item8/wda-branching-geometry-downloaded-restore --receipt evidence/item-8/raw-custody/wda-branching-geometry-r1-downloaded-restore.json
uv run python - <<'PY'
from pathlib import Path
from mcpack_evidence.item7_nbt_models import ChunkRecord
from mcpack_evidence.item8_world_bounds import observed_bounds
names = {'dungeons_arise:' + n for n in ('bandit_towers', 'bandit_village', 'greenwood_pub', 'mechanical_nest', 'thornborn_towers')}
source = Path('evidence/raw/item8/wda-branching-geometry-downloaded-restore/chunks.jsonl')
for line, raw in enumerate(source.open(), 1):
    for observation in observed_bounds(ChunkRecord.model_validate_json(raw)):
        if observation['structure_id'] in names:
            print(line, {key: value for key, value in observation.items() if key != 'piece_boxes'}, 'pieces', len(observation['piece_boxes']))
PY
```

Rebuild and focused checks use the existing commands above. Semantic comparison
changes only these ten geometry attributes and direct evidence/input identity.

## Mining System inactive disposition

Direct inspection of the exact WDA packaged resource
`data/dungeons_arise/tags/worldgen/biome/has_structure/mining_system_biomes.json`
finds replace:false, values:[]. The effective structure-inputs catalog entry
structure_biomes[dungeons_arise:mining_system] has biomes:[], no missing_required
and no unresolved_tags. No captured dimension can intersect this empty set.
Its registered root selects that tag and a jigsaw start at absoluteY5,
underground_structures, bury; those settings do not supply an eligible biome.

Record Mining System as registered but inactive, following existing inactive
family treatment. Preserve its root, eight available templates and grouping
rationale. No runtime probe or manual placement is necessary to establish
normal-generation ineligibility. This does not prove manual placement impossible
or remove the content from packaged coverage.

The previous450 active-family candidate denominator included this unresolved
candidate. Correct it to449:409 registry-based active candidates plus40
nonregistry families. Assessed remains347, remaining102. Registry-root coverage
remains887 assigned exactly once. Registry grouping rows remain426, now409
active,16 inactive and one excluded cloud formation. WDA has39 active families,
35 assessed and four remaining: Foundry, Mining Complex, Scorched Mines,
Shiraz Palace. Their available template counts45/59/21/41 total166. Foundry
references missing pool underworld/foundry/foundry_corridor_gears. No retained
start exists for these four; their40 attributes remain the next batch.

Rebuild and focused checks use existing commands above. Only Mining System's
disposition, direct supporting identities and builder input identity change;
no source templates, registered roots or existing family assessment is removed.

## Foundry, Mining Complex, Scorched Mines and Shiraz content

Thirty-two attributes integrate four families/166 traced templates: Foundry45,
Mining Complex59, Scorched Mines21, Shiraz Palace41. Eight geometry attributes
remain; none is counted assessed yet. Same immutable WDA archive and catalogs
as above, exact templates data/dungeons_arise/structure/<family>/<family>_<piece>.nbt,
root worldgen/structure/<family>.json. All effective biome intersections select
Overworld. Root spawn_overrides are empty; biome/world-condition spawning is
separate from authored ordinary spawners. No trial spawners occur in available
selected templates. Preserve complete NBT in existing spawner_blocks pointers,
including gear, effects, timing and passenger chains; no legacy conversion or
live encounter-frequency claim.

Foundry starts absoluteY-10, no heightmap, depth6, underground_structures.
Eight dedicated ordinary spawners, block_entities0: blaze0 Health55, magma0/1
Size8/4, piglin0 zombification-immune brute Health50, wither_skeleton0 Health55,
wither_skeleton1 zombification-immune hoglin carrying wither skeleton Health45,
wither_skeleton2 Health80, wither_skeleton3 phantom Health40 Size5 carrying
wither skeleton Health80. No direct entities or nonempty fixed Items/Book
payloads in available templates. Missing pool
underworld/foundry/foundry_corridor_gears remains in grouping data; absence
claims are limited to available components. Selected processors are empty.

Mining Complex starts absoluteY-5, no heightmap, depth7, bury and
underground_structures. Main0 measures57x197x57 and blimp components occur;
therefore underground generation step alone does not prove wholly buried
content. Exterior cues remain terrain-dependent. Seven ordinary spawner0..6
payloads at block_entities0 are skeleton Health8/14/24, pillager Health34,
skeleton Health34/26/34. Direct saved entities are four paintings, two armor
stands and24 item frames, not authored monsters. Counts span selected templates,
not a guaranteed population in one generated layout.

Mining main0 dispenser indices162/163/164/184/187 contain fixed wind_charge
stacks with lowercase count fields; exact Items remain preserved. Blimp1
index11 and intersection0 index40 contain writable books without saved pages.
Processor mining_complex_main changes deepslate, mossy cobblestone, spruce,
mud/copper and lantern materials; its second rule processor appends decorated
pot loot from dungeons_arise:pots/mining_complex/mining_complex_pots. It does
not inject entities. The ordinary loot references include Mechanical Nest's
normal table, retained as the exact source reference rather than renamed.

Scorched Mines projects WORLD_SURFACE_WG offset-14, depth7, surface_structures.
Hub can supply an exterior cue while connected corridors conceal content.
Ordinary spawner0..2 block_entities0 save wither skeleton Health36, skeleton
Health30, husk Health30. No direct entities. Corridor2_temptation index0
saves one splash potion in dispenser slot4 with legacy CustomPotionEffects
Id2,Amplifier5,Duration300. This is a fixed payload, not proof of a working
trap. Selected processors are empty.

Shiraz Palace projects WORLD_SURFACE_WG offset16, depth7, surface_structures.
Architectural sections, towers and gardens support an exterior landmark
inference, not human discovery range. Fourteen reachable ordinary spawner templates,
each block_entities0: axe_illusion2 skeleton Health15; crossbow_illusion1
pillager Health15; husk_garden0/2 Health60/40;
husk_garden_exterior0 cow Health30 carrying husk Health60; husk_tower0
Health50; skeleton_elite0 wither skeleton Health20; skeleton_garden1
Health40; skeleton_garden_exterior1 cow Health20 carrying skeleton Health40;
skeleton_illusion0 wither skeleton Health30; skeleton_library0 Health40;
skeleton_tower1 wither skeleton Health30; spider0 cave spider Health8;
spider1 cave spider Health8 carrying cave spider Health6. Names containing
illusion do not make these illusioner mobs. No direct entities or nonempty
fixed Items/Book payloads. Selected processors are empty.

All ordinary table IDs and nonempty fixed-payload locations are integrated in
attributes. Exact source references carry descriptive claims; no additional
validator or measurement was needed. Rebuild and focused checks use commands
above. Geometry remains eight explicit attributes for the same four families.

## Shiraz Palace geometry and spawner correction

Exact WDA templates data/dungeons_arise/structure/shiraz_palace/
shiraz_palace_part_0.nbt through part_26.nbt each measure48x32x48.
Start pool desertic/shiraz_palace/shiraz_palace_start selects part13.
The main pool uses rigid sections with empty processors. Relative to part4
origin(0,0,0), parts0..8 have XZ origins(-48,-48),(0,-48),(48,-48),(48,0),
(0,0),(-48,0),(-48,48),(0,48),(48,48). Named shiraz_palace_side pairs
0/1,2/3,4/5,6/7 connect center4 to1,3,7,5; pairs8/9,10/11,12/13,14/15
connect corners. Opposing connectors at0/47 join adjacent blocks, giving48
horizontal steps. Parts9..17 repeat atY32 with suffix_top and18..26 atY64
with suffix_top_two. Aligned up_west/down_west connectors at(23,31,24)/
(23,0,24), pairs18/19 and21/20, connect centers4/13/22. The resulting nominal
source envelope is144x96x144, within four architectural edges from start13.

Fourteen reachable spawner alternatives measure1x2x1 with incoming down_north
at(0,1,0). Upward receivers in the sections are within localXZ0..47 and
Y1..28, so attached boxes remain inside the architectural sections. No other
reachable nonarchitectural template enlarges the envelope. This is source
geometry, not a retained start or successful-placement claim.

A narrow attribution defect was found while reconciling the41-template trace:
27 architectural sections plus14 reachable spawner alternatives. The archive
also contains shiraz_palace_husk_elite_0, but no reachable pool selects it.
The preceding content increment counted this unreferenced Health50 husk among
15 alternatives. Correct the authoritative summaries to14, retain its explicit
unreferenced disposition, and correct the descriptive list above. The existing
source_templates list already excluded it and remains unchanged. A focused
comparison of spawner templates against the selected traces found no analogous
unselected spawner in Foundry, Mining Complex or Scorched Mines. No new tool
or broad regression framework is needed for this direct artifact distinction.

Rebuild and eight focused tests use the existing commands above. Only Shiraz
geometry and this direct spawner correction change. Six geometry attributes
remain for Foundry, Mining Complex and Scorched Mines.
