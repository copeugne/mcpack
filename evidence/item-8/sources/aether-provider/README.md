# Aether remaining candidate entry paths

Extractor 8976b7a captures 23 main-entry, mixin-plugin, custom-feature, holiday
decoration and Silver/Gold assembly classes. Existing Bronze and shared-piece
sources are reused. Independent r1 extraction matches every generated file.
Manifest SHA-256: 917c3ffbb199539bfbe375f4a7381d4498f327a2ce9d5cdc28ad01d978f604ee.

```sh
uv run -m tools.inspect_item8_pool_elements --archive aether-1.21.1-1.5.10-neoforge.jar --class-name com/aetherteam/aether/Aether.class --class-name com/aetherteam/aether/mixin/AetherMixinPlugin.class --class-name com/aetherteam/aether/world/feature/AetherFeatures.class --class-name com/aetherteam/aether/world/feature/AercloudFeature.class --class-name com/aetherteam/aether/world/feature/AetherLakeFeature.class --class-name com/aetherteam/aether/world/feature/CrystalIslandFeature.class --class-name com/aetherteam/aether/world/feature/ShelfFeature.class --class-name com/aetherteam/aether/world/treedecorator/HolidayTreeDecorator.class --class-name com/aetherteam/aether/world/structurepiece/golddungeon/GoldBossRoom.class --class-name com/aetherteam/aether/world/structurepiece/golddungeon/GoldDungeonPiece.class --class-name com/aetherteam/aether/world/structurepiece/golddungeon/GoldIsland.class --class-name com/aetherteam/aether/world/structurepiece/golddungeon/GoldProcessorSettings.class --class-name com/aetherteam/aether/world/structurepiece/golddungeon/GoldStub.class --class-name com/aetherteam/aether/world/structurepiece/golddungeon/GoldStubCave.class --class-name com/aetherteam/aether/world/structurepiece/golddungeon/GoldTunnel.class --class-name com/aetherteam/aether/world/structurepiece/silverdungeon/SilverBossRoom.class --class-name 'com/aetherteam/aether/world/structurepiece/silverdungeon/SilverDungeonBuilder$1.class' --class-name com/aetherteam/aether/world/structurepiece/silverdungeon/SilverDungeonBuilder.class --class-name com/aetherteam/aether/world/structurepiece/silverdungeon/SilverDungeonPiece.class --class-name com/aetherteam/aether/world/structurepiece/silverdungeon/SilverDungeonRoom.class --class-name com/aetherteam/aether/world/structurepiece/silverdungeon/SilverFloorPiece.class --class-name com/aetherteam/aether/world/structurepiece/silverdungeon/SilverProcessorSettings.class --class-name com/aetherteam/aether/world/structurepiece/silverdungeon/SilverTemplePiece.class --output evidence/raw/item8/aether-provider-r1
```

These sources support candidate/component reconciliation. Capture alone does
not establish provider closure, final family counts or runtime placement.

## Silver family assessment

Reuse the pinned Silver generation/piece classes above, aether-custom-entry,
aether-placement, aether-piece-binding, aether-trapped-block and
aether-trap-bindings captures. Exact identities are in family-decisions.json.
No new executable measurement or source capture is introduced. The selected
JSON and NBT below are from aether-1.21.1-1.5.10-neoforge.jar in the existing
packaged/template catalogs.

### Placement and architectural size

The dimension answer already joins15 effective biomes to aether:the_aether.
SilverDungeonStructure.findGenerationPoint reads the WORLD_SURFACE_WG base
height minus belowTerrain2, denoted h. If nextInt(5)<3, it starts at h+18 and
adds nextInt(128-(h+18)) only if h+18<128; otherwise it retains h+18. The other
branch uses max(h,35+nextInt(70)). Thus maxY128 is not an unconditional cap.
This is surface-adjacent/elevated architecture, not a buried underground room
inferred from its generation-step name.

Exact selected paths are `data/aether/structure/silver_dungeon/` plus:
rear, skeleton, boss_room, floor, wall, door, boss_door, staircase,
tall_staircase and chest_room, each with .nbt suffix. test_door is packaged
but unselected in these paths. Their role assignments are already recorded;
rooms and cloud chunks are not separate families.

The following derives architecture size directly, without treating a component
as the whole building. In generatePieces, take rotation NONE and rear origin
(0,0,0). SilverTemplePiece uses rotation with the default zero pivot:

| Component | Origin | Template size X,Y,Z | Inclusive box |
| --- | --- | --- | --- |
| rear | 0,0,0 | 32,30,31 | X0..31,Y0..29,Z0..30 |
| boss_room | 5,3,5 | 22,17,26 | X5..26,Y3..19,Z5..30 |
| skeleton | 0,0,31 | 32,27,26 | X0..31,Y0..26,Z31..56 |

The two shells therefore span32x30x57. Quarter turns swap the horizontal axes.
The constructor passes3,3,3 to SilverDungeonBuilder. assembleDungeon starts its
interior grid at skeleton+(5,5,-1), horizontal spacing7 and vertical spacing5.
For NONE, grid origins are X5/12/19,Z30/37/44,Y5/10/15. Floors are6x1x6 at
(+1,-1,+1); first walls/doors are6x4x1 at(+1,0,0); perpendicular walls use the
quarter-turned6x4x1 template at(0,0,+1). Staircases are4x9x4 or4x14x4 at(+2,0,+2),
chest rooms2x2x2 at(+3,0,+3), and boss doors2x2x1 at(+3,0,0).
All lie inside the shell union; even a tall staircase on the highest grid level
ends atY28. SilverDungeonRoom's size/2-minus4 pivot adjusts rotated small rooms;
the outer temple pieces use zero pivot. No room choice enlarges the shell.
This is architectural extent, not occupied block volume or a saved world sample.

buildCloudBed supplies separate random-walk cloud bedding using the shared
LargeAercloudChunk writer. It can extend outside the temple shell. Do not call
32x30x57 the complete cloud envelope or an observed maximum. The exposed temple
and cloud support are potential visual landmarks, with terrain/viewer-dependent
occlusion; no live sightline or discovery-distance measurement is asserted.

### Encounter and spawner sources

boss_room.nbt contains one aether:valkyrie_queen; the other selected templates
contain no entities. No ordinary/trial spawners occur in selected palettes.
Selected silver_room, silver_floor and silver_boss_room processor lists do not
create spawner blocks. SilverFloorPiece receives silver_floor: its sequential
rules can turn locked_angelic_stone into trapped_angelic_stone or
trapped_light_angelic_stone. Preserve rule ordering and do not turn their
individual probabilities into an observed whole-floor trap frequency.

AetherBlocks registrations bind InvokeDynamic96 to lambda$static$80 and97 to
lambda$static$82. Both construct TrappedBlock with AetherEntityTypes.VALKYRIE;
the facade differs between locked angelic/light angelic stone. The existing
verbose aether-trap-bindings capture contains those exact bootstrap bindings.
Reuse TrappedBlock.stepOn and the uncancelled TriggerTrapEvent path: a Player
step can lead to a server TRIGGERED spawn attempt. Spawn/write results are
ignored. These are authored trap sources, not conventional spawners or natural
spawns. This attribution does not mean a Valkyrie attacks immediately.

SilverDungeonRoom Chest markers supply chest/mimic alternatives. nextInt(5)>1
chooses CHEST, the other outcomes CHEST_MIMIC. The retained ChestMimicBlock
implementation attempts a MIMIC on unblocked server interaction or after break.
Source selection is not a guarantee of either successful placement or spawning.

SilverBossRoom enables entity finalization and installs a border-box material
rule before its configured processors. The material rule changes locked stone,
not entity types. Shared BossRoomProcessor writes Dungeon tracking metadata.
SilverDungeonStructure.afterPlace finds queens in the supplied clipping AABB and
updates their dungeon bounds from the piece container (inclusive maxima+1).
That tracking box, which may include cloud pieces, is distinct from architecture.
The root has empty full-box overrides for all twelve declared vanilla/Aether
spawn categories. They constrain natural spawning, not authored enemies or
external arrivals. No live combat or completed encounter is claimed.

### Loot assignment

There are no direct loot-table references or fixed container Items in the ten
selected templates. Loot comes from marker code. AetherLoot binds the exact IDs
`aether:chests/dungeon/silver/silver_dungeon` and
`aether:chests/dungeon/silver/silver_dungeon_reward`.

SilverDungeonRoom.handleDataMarker clears Chest, chooses random X/Z inside its
room bounds, and uses that candidate only if inside the supplied clipping box;
otherwise it uses the marker position. placeChestOrMimic selects a block as above
and passes SILVER_DUNGEON to inherited createChest. It discards success. Its
random-facing setValue result is also discarded, so random chest orientation
is not an accepted behavior. A mimic is not an ordinary loot-bearing chest.

SilverBossRoom Treasure Chest checks the container below, assigns the reward
table if it is randomizable, sets dungeon type aether:silver and clears the
marker. This supports table attribution, not treasure accessibility, boss
clearance, successful loot decoding or measured yield. Double-drops processing
changes supported block-state properties; it is not another chest table.

All nine outstanding Silver attributes are integrated alongside its existing
dimension answer. Reproduce with fresh output paths:

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/silver-assessed-inventory.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

## Gold content and placement assessment

Seven outstanding descriptions are integrated for `aether:gold_dungeon`.
Dimension was already established. Approximate footprint and vertical size
remain outstanding; the central island template alone is insufficient.

Use the pinned `aether-custom-entry` GoldDungeonStructure, this directory's
Gold pieces, `aether-placement` AetherLoot/BossRoomProcessor/DoubleDropsProcessor
and the four selected templates in `templates-redacted.json.gz`. The selected
processor lists are `gold_boss_room`, `gold_island` and `gold_tunnel` in
`packaged-json-redacted.json.gz`. All identities are bound in family-decisions.

The templates are island38x43x38, stub15x15x15, boss_room23x9x28 and
 tunnel7x5x16. Only boss_room contains an entity: one `aether:sun_spirit`, with
`BossFight=0`. GoldBossRoom.makeSettings enables entity finalization. No selected
template palette contains an ordinary or trial spawner. Structure spawn
settings have twelve empty full-box lists. These facts distinguish authored
boss content from natural spawning; they do not prove activation or population.

The boss template contains a locked treasure chest with empty Items and initial
Kind `aether:bronze`. Its `Treasure Chest` marker sits one block above.
GoldBossRoom.handleDataMarker assigns GOLD_DUNGEON_REWARD with a random long seed
when the block below is a randomizable container, sets dungeon type `aether:gold`
and clears the marker. AetherLoot binds that key to
`aether:chests/dungeon/gold/gold_dungeon_reward`. No direct template LootTable
reference or fixed container contents occur. Accessibility and reward yield
are not inferred from the marker binding.

Selected rule processors replace locked hellfire stone with its light variant,
and holystone with mossy holystone. BossRoomProcessor supplies dungeon metadata;
DoubleDropsProcessor changes a block-state property. Direct inspection of
SurfaceRuleProcessor.process shows tagged dirt top-material replacement;
VerticalGradientProcessor.process may change underlying holystone to dirt;
NoReplaceProcessor.process preserves existing baseblock, configured as air.
These inspected paths add no conventional spawner. Their exact JAR and member
hashes are recorded in the existing processor_inspection field. Inspect with:

```sh
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -p -c \
  -classpath downloads/item3/candidates/aether-1.21.1-1.5.10-neoforge.jar \
  com.aetherteam.aether.world.processor.SurfaceRuleProcessor \
  com.aetherteam.aether.world.processor.VerticalGradientProcessor \
  com.aetherteam.aether.world.processor.NoReplaceProcessor
```

GoldDungeonStructure.findGenerationPoint initially anchors at
max(WORLD_SURFACE_WG base height minus20,40+nextInt(60)). generatePieces creates
the island, stubs, cave pieces, boss room and one tunnel. tunnelFromBossRoom
uses tunnelFromOddSquareRoom for the chamber connection, and
 tunnelFromEvenSquareRoom for the terrain query beyond the tunnel. A positive
difference between exit terrain height and tunnel origin Y shifts all pieces
upward. Initial anchor height is therefore not final height.

addIslandStubs selects8+nextInt(5) pieces around the island center, using radius
(nextFloat*0.125+0.7)*24 and negative vertical offset floor(24*nextFloat*0.3).
placeGumdropCaves selects18 point anchors with independent differences of two
nextInt(24) values on each axis. GoldStubCave.postProcess carves beyond those
point boxes, so saved point bounds alone would not describe carving extent.
afterPlace attempts configured golden oaks on island/stub upper surfaces.
The island and foliage can be landmarks while the chamber is enclosed. This is
source-based discoverability, without measured sightlines or a guarantee that
terrain leaves the tunnel visible.

No new runtime capture, measurement tool or validation framework was added.
