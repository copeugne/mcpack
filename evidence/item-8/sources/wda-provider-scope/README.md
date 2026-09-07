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
