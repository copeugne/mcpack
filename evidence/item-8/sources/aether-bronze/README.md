# Aether Bronze dungeon assembly and pieces

Captured using extractor revision 1b05806. The nine disassemblies and identities
reproduced byte for byte. This is direct source evidence, not a completed family
attribution or a world-placement measurement.

```sh
uv run -m tools.inspect_item8_pool_elements --archive aether-1.21.1-1.5.10-neoforge.jar --class-name com/aetherteam/aether/world/structurepiece/bronzedungeon/BronzeBossRoom.class --class-name 'com/aetherteam/aether/world/structurepiece/bronzedungeon/BronzeDungeonBuilder$Connection.class' --class-name 'com/aetherteam/aether/world/structurepiece/bronzedungeon/BronzeDungeonBuilder$RoomProvider.class' --class-name com/aetherteam/aether/world/structurepiece/bronzedungeon/BronzeDungeonBuilder.class --class-name com/aetherteam/aether/world/structurepiece/bronzedungeon/BronzeDungeonPiece.class --class-name com/aetherteam/aether/world/structurepiece/bronzedungeon/BronzeDungeonRoom.class --class-name com/aetherteam/aether/world/structurepiece/bronzedungeon/BronzeDungeonSurfaceRuins.class --class-name com/aetherteam/aether/world/structurepiece/bronzedungeon/BronzeProcessorSettings.class --class-name com/aetherteam/aether/world/structurepiece/bronzedungeon/BronzeTunnel.class --output evidence/raw/item8/aether-bronze-r1
```

BronzeDungeonRoom.handleDataMarker clears the marker position. For `Chest`,
nextInt(5) greater than 1 selects an ordinary chest; the other two outcomes
select CHEST_MIMIC. It calls createChest with AetherLoot.BRONZE_DUNGEON and
discards the success result. This is a source selection rule, not observed
chest or mimic counts. The inherited chest writer and mimic block behavior
still need attribution before claiming effective encounter generation.

BronzeBossRoom enables entity finalization in its placement settings. For
`Treasure Chest`, it assigns AetherLoot.BRONZE_DUNGEON_REWARD to a randomizable
container below the marker when present, sets dungeon type aether:bronze via
the treasure-chest helper, then clears the marker. That method itself does not
establish the boss entity identity. Join the selected template entities and
shared AetherTemplateStructurePiece behavior.

The builder references boss_room, chest_room, end_corridor, entrance, lobby
and square_tunnel. Its room-provider registrations and assembly conditions
remain to be read completely and joined to the packaged template catalog.
BronzeDungeonSurfaceRuins is a component of this builder, not a separate
family inferred from its class name. Processor settings distinguish generic
rooms, tunnels and boss rooms. Resolve the selected definitions before
attributing effective processor behavior from static helper fields.

Next: finish the builder and surface-ruins reading, join the six named template
candidates and selected processor lists, then resolve the shared piece writer,
loot constants and direct encounter-producing blocks where required. Reuse
these captures. No new measurement system or runtime acceptance claim.

Scoped extractor Ruff and Basedpyright passed before capture.

## Selected component catalog binding

The focused catalog test binds the six named template candidates to the frozen
Aether archive. Sizes (X, Y, Z) are boss_room (16, 14, 16), chest_room (12, 8, 12),
end_corridor (6, 8, 5), entrance (6, 8, 1), lobby (12, 12, 12), and square_tunnel
(6, 6, 6). These are component sizes, not assembled family dimensions.
The boss template has one authored aether:slider and a treasure chest with a
Treasure Chest marker. The chest room has a Chest marker; the other four
candidates have no entity or block-entity entries. These template inputs do
not establish effective processor results, successful placement or populations.

The selected definition sets maxrooms=8, aboveBottom=32, belowTop=24 and twelve
piece-bound spawn overrides with empty lists. This is a natural-spawn override
input, not proof of no enemies or no external spawn modifications. Its selected
processor lists are aether:bronze_boss_room, aether:bronze_room and
aether:bronze_tunnel. The test binds processor type order, including custom
boss_room and double_drops processors. Their behavior remains a direct source
dependency, alongside the inherited piece writer and marker-generated blocks.

```sh
uv run pytest -q tests/item8/test_aether_bronze_components.py
```

Both focused tests and scoped Ruff/Basedpyright passed. No world measurement.

## Assembly and conditional surface clue

These findings derive from the preserved BronzeDungeonBuilder and
BronzeDungeonSurfaceRuins disassemblies in this directory, not a simulation.

initializeDungeon selects a boss room, square tunnel and first chest room
when boss rotation and orientation permit. It then attempts further room
propagation, a final lobby propagation, an end tunnel and a surface component.
Propagation tries three relative directions in random order, follows existing
connections recursively, and checks candidate collision, distance and terrain
coverage. The distance check permits candidate template origins within three
chunks in chessboard distance of the starting chunk. This is not a bound on
the complete occupied footprint. The coverage check samples four base columns
one block outside the candidate's horizontal corners; it does not inspect
an entire generated roof. A propagation attempt can fail, so maxrooms=8 is
not a guarantee of eight placed rooms.

buildEndTunnel tries three directions. It accepts the first attempt returning
success, otherwise retains the attempt with the most pieces. buildTunnelFromRoom
starts with an entrance, adds end_corridor pieces until collision, sampled air,
or the coordinate-distance limit stops it. Its success requires a corridor
addition and air checks at the sampled position's bottom and piece maximum Y.
checkForAirAtPos reads the generator base column, not the final world. A retained
unsuccessful attempt is therefore not evidence of an open exit. The coordinate
limit is checked after addition and does not establish an exact family width.

buildSurfaceTunnel searches backward for a node with both X and Z spans greater
than six. It samples OCEAN_FLOOR_WG first occupied height at that node's center.
It returns without a surface piece when no such node exists or node maxY+1
exceeds that height. Otherwise it adds BronzeDungeonSurfaceRuins above the room,
with each horizontal side inset by three and maximum Y at sampled height+4.
This is a conditional component, not a separate family or guaranteed entrance.

The surface piece processes its horizontal perimeter using local terrain
heights, randomized column placement, holystone/mossy holystone and slab
providers. Column writes use world setBlock directly after an initial clipping
check; the saved maximum Y alone is not a complete occupied-envelope proof.
It also attempts a flower patch when the supplied clipping box contains the
piece center. The patch anchor uses the supplied clipping box's center projected
to OCEAN_FLOOR_WG, not necessarily the piece center. Placement results are
ignored. These paths support a potential surface clue; they do not establish
successful surface placement, guaranteed visual prominence or discovery range.

Still unresolved: exact effective room-provider callback binding, boss rotation
and coverage helper details where required for placement attribution, inherited
writers and retained modifications, actual assembled envelopes and visual
observations. Do not repeat these source reads to infer measured geometry.

## Bronze geometry assessment

The two outstanding Item8 size descriptions are resolved from the preserved
builder, piece constructors and surface-ruin implementation. Architectural
footprint has a conservative211x211-block enclosing square, including the exit
corridor. Underground template height is14 blocks. The optional surface ruins
have a terrain-dependent vertical extension described below. Neither the square
nor the height is a measured whole-world occupied envelope or a typical layout.

Let O be the original generation-context chunk minimum and A the selected boss
anchor. BronzeDungeonStructure.searchNearbyChunks searches offsets[-1,1] on
each chunk axis, so A.x/z-O.x/z is one of -16,0,16. The boss uses a half-template
pivot; ordinary rooms and tunnels rotate about zero. Component sizes are bound
in the selected component catalog above. Coordinate intervals below are inclusive.

New propagated chest/lobby origins pass isCloseToCenter against the ORIGINAL
context chunk, limiting each origin coordinate to O+[-48,63]. The first chest
origin, which bypasses that check, is A+(2,20),(-4,2),(14,-4), or(20,14) in X/Z
for NONE,CLOCKWISE_90,CLOCKWISE_180,COUNTERCLOCKWISE_90 respectively. It too is
inside O+[-48,63]. Relative to A, room origins therefore fit[-64,79]; rotated
12-wide rooms fit[-75,90] on either axis. Boss16-wide placement also fits.

BlockLogicUtil.tunnelFromEvenSquareRoom returns the source box minY. For a
12-wide room and6-wide connection it offsets the box center by at most6 blocks
on either horizontal axis; the center is within[-5,6] of a zero-pivot room origin.
A6-cube connection then adds at most5 further blocks in either direction.
Thus even connection pieces fit A+[-80,96]. The initial boss connection fits
inside that interval as well. Collision and coverage tests can only reject
these attempted pieces. maxrooms=8 is not assumed to guarantee eight rooms.

buildTunnelFromRoom places a6x8x1 entrance from the final room and advances its
origin one block in the selected direction. The entrance origin fits
A+[-75,91], its bounds[-80,96], and the first corridor origin[-76,92]. The loop
uses the ENTRANCE template Z size,1, as its increment, although each selected
end_corridor template is6x8x5. After each addition it tests whether either
origin coordinate differs from A by at least100. Consequently corridor origins
never exceed A+[-100,100]; their zero-pivot rotated templates extend at most5
further blocks. All architecture fits A+[-105,105] on X/Z, giving211x211.
This is a conservative common bound, not a claim that a single layout spans
both extremes. The three exit attempts retain one attempt; failed attempts may
be retained and are not claimed as open entrances.

For Y, the boss spans A.y..A.y+13. The first connection uses the boss box moved
up2, and the helper returns that minimum. Every later room/connection uses its
source box minimum without another upward offset. Thus chest rooms span
A.y+2..+9, lobby+2..+13, square tunnels+2..+7 and entrance/end corridors+2..+9.
The underground template union is14 blocks high.

The optional surface piece is horizontally inset3 on each side of a selected
room, so it does not enlarge that architectural footprint. If B is that room's
box and H is OCEAN_FLOOR_WG first occupied height at its center, the piece exists
only when B.maxY+1<=H. Its saved Y interval is[B.maxY+1,H+4]. The architectural
union INCLUDING that saved component therefore has height max(14,H+5-A.y).
This formula preserves the terrain dependency instead of inventing a fixed
full-family height.

Saved surface bounds are not an occupied-write bound. At each perimeter column,
BronzeDungeonSurfaceRuins uses local world height h and offset k in[-2,1]. Its
scan visits from the surface piece minY up to h+k-1, filters eligible positions,
and the cap writes at h+k. Gap endpoint writes stay between scan positions.
If local terrain differs from the sampled center, writes can lie outside the
saved surface box, including a cap below its minimum. The column X/Z stays on
the inset perimeter. A conditional flower patch is an additional decoration:
its anchor is the clipping-box center projected to terrain. No flower-patch
extent or measured occupied full-family height is asserted.

The shared helper was directly inspected from the pinned Aether JAR; its member
identity is bound in family-decisions.processor_inspection. For reproduction:

```sh
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -p -c \
  -classpath downloads/item3/candidates/aether-1.21.1-1.5.10-neoforge.jar \
  com.aetherteam.aether.world.BlockLogicUtil
```

BoundingBox center and StructureTemplate rotation conventions use the same
pinned Minecraft sources and identities recorded in the Gold geometry assessment
in `../aether-provider/README.md`. The arithmetic here is a direct derivation,
not a simulation or executable measurement. No new runtime capture, runner
extension or measurement framework is required for these approximate dimensions.
