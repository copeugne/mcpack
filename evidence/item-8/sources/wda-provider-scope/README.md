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
