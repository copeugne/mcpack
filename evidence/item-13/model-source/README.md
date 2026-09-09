# Item 13 nominal melee model inputs

These are source inputs for a declared mathematical workload, not a live-player
combat benchmark. No Item 14 encounter/pathfinding experiment is performed.

`capture.sh` verifies the existing mapped Minecraft server SHA-256 and retained
Better Combat SHA-256, then disassembles only the actor, basic enemy, armor and
spawner classes needed by the small-dungeon representative. Full disassemblies
are retained losslessly in `captured/*.txt.gz`; `SHA256SUMS` binds their bytes.
The pinned javap is from the existing Temurin 21.0.12.1+1 toolchain. Reproduce
from repository root into an absent directory:

```sh
bash evidence/item-13/model-source/capture.sh /tmp/item13-model-source-reproduction
```

The capture was executed initially into `captured`; Attributes was added through
the same javap command before the final lossless compression. The script reproduces
that final set. It does not alter the runtime, configuration or accepted worlds.

## Explicit derivation

- `world.item.Items`, static initializer offsets 10480-10516: iron sword uses
  Tiers.IRON and SwordItem.createAttributes with damage parameter 3 and attack-speed
  adjustment -2.4. `world.item.Tiers` initializer offsets 59-81 gives iron attack
  bonus 2. `SwordItem.createAttributes` offsets 13-26 sums the two damage inputs;
  Player.createAttributes adds base attack damage 1. Nominal damage is 1+3+2 = 6.
- `world.entity.ai.attributes.Attributes` initializer offsets 98-123 gives base
  attack speed 4; the nominal equipped speed is 4-2.4 = 1.6 attacks/second.
  Player.getCurrentItemAttackStrengthDelay returns 20 / attack speed in ticks.
  PlayerAttackHelper.getAttackCooldownTicksCapped uses max(that value, configured
  attack_interval_cap). Frozen `evidence/item-6/frozen/config/bettercombat/server.json5`
  sets that cap to 2 ticks. The model therefore reserves ceil(12.5) = 13 ticks
  per single-target fully charged swing, including the final swing's full cycle.
  Tick rounding and complete-cycle reservation are model assumptions, not measured
  client input or attack completion times.
- `iron_sword.json` inherits the retained `sword.json`. All three sword combo hits
  have damage multiplier 1 and upswing 0.5. The frozen upswing multiplier is 0.5.
  Single-target hits avoid assumptions about Better Combat's reworked sweep
  damage. No dual wielding, criticals, enchantments, buffs or incoming damage are
  included in this nominal workload.
- Attributes initializer offsets 484-509 gives default maximum health 20. The
  captured Zombie.createAttributes and AbstractSkeleton.createAttributes do not
  replace maximum health; Spider.createAttributes sets 16. Zombie supplies base
  armor 2; the naked skeleton/spider scenario uses armor 0. Spawn equipment,
  effects, reinforcements, jockeys and modified runtime attributes are not assumed
  absent in real play; they are outside this explicitly naked-adult scenario.
- CombatRules.getDamageAfterAbsorb gives, for toughness 0 and no enchantments,
  `effective_armor = clamp(armor - damage/2, armor*0.2, 20)` and
  `received = damage * (1 - effective_armor/25)`. At nominal damage 6, naked zombie
  received damage is 5.904, while naked skeleton/spider receive 6. Required hits
  are respectively ceil(20/5.904)=4, ceil(20/6)=4, ceil(16/6)=3.
- BaseSpawner constructor sets spawnCount=4, minSpawnDelay=200, maxSpawnDelay=800,
  maxNearbyEntities=6, requiredPlayerRange=16 and spawnRange=4. Actual saved NBT
  overrides these; the producer must retain and use saved values. These are
  attempts/potential and scheduling parameters, not guaranteed spawned enemies.

## Model meaning and limitations

For one declared activation wave, enumerate successful-count scenarios from zero
through the saved SpawnCount. Each potential enemy uses the above nominal hits;
active-attack seconds = hits * 13 / 20. Report continuous-contact and 50%-contact
scenarios separately; the latter doubles the attack budget. The 50% duty fraction
is a declared sensitivity assumption, not an estimated player skill statistic.
Report saved initial activation delay separately, never hide it in traversal.

The finite values describe that bounded encounter workload only. A still-active
spawner, blocked spawn attempts, delayed aggro, random equipment, reinforcement,
misses, retreat/death, terrain, server lag and player decisions can extend or
prevent completion. Real combat duration has no finite upper bound from this
model. Do not label these values an observed clear time, prediction interval,
measured fight or evidence of encounter quality. Other enemy mechanics need their
own supported model before their dependent batch; this simple profile is not a
universal boss or modded-enemy fallback.

## First-house piglin component and bed mechanism

Two additional classes are captured through the same pinned javap and mapped
server identity: world.entity.monster.piglin.Piglin and world.level.block.BedBlock.
All previous captured file hashes remain unchanged. The updated capture.sh
reproduces the complete set; no earlier disassembly or runtime was repeated.

Piglin.createAttributes offsets 0-9 explicitly assigns maximum health 16. This
supports extending the existing nominal melee workload to an ordinary adult
piglin with stipulated no armor, effects, equipment modifiers, reinforcements or
incoming damage. It does not establish actual runtime attributes or spawn gear.
The existing 6-damage iron-sword, 13-tick full-cycle model requires ceil(16/6)=3
hits per such enemy. Before calculating a house component total, use zero through
four successful enemies for its one explicit piglin spawner's saved SpawnCount 4,
100% and 50% contact duty, with the existing actor/equipment and attack start/end
conditions. Keep the stored Delay 733 as a separate ideal 20-tick/second activation
countdown, not an extra duration automatically added to the walking model. The
countdown and motion can overlap. Do not assign this profile to the other three
empty-entity spawners, or call the sum a whole-house clear time.

BedBlock.useWithoutItem offsets 58-144 branch on canSetSpawn; when false, the
source removes the bed and invokes an explosion with power 5 and fire enabled.
canSetSpawn offsets 0-7 reads dimensionType.bedWorks. The reused packaged catalog
contains data/minecraft/dimension_type/the_nether.json with bed_works=false,
resource SHA-256 26953e0426b058a44a4c1f2060a1a15823c03dd511f57dd7ef97dfa6327a3825.
This identifies bed interaction as a source-supported conditional Nether hazard.
It does not mean that walking past a bed triggers it, or that an explosion was
observed. No bed was used, and no block, world or frozen configuration was altered.
Actual blast reach, damage, modded interception and consequences were not measured.

The two new text payloads were initially compressed with Python's gzip helper.
Before acceptance they were losslessly recompressed with the existing gzip -n
command so capture.sh reproduces their headers as well as their contents. Both
original encodings remain in evidence/raw/item13/source-compression-r1; decompressed
payload equality was verified. This changes no disassembly or observation.

## First-house container access: declared inspection

Use the existing upright actor at feet(463.5,47.5,431.5) for the chest and
(466.5,47.5,431.5) for the balcony barrel. Both positions are in the retained
upright clearance set and lie on the accepted circuit. Permit standing at those
stops; the circuit's interaction time remains excluded. Use the existing modeled
1.62 eye offset and conservative3-block reach. Aim from the first eye point at
(463.5,49.5,430.5), and from the second at(466.5,48.85,430.99), slightly inside
the barrel's front face. Resolve intervening selection shapes, not just physical
collision. No item is generated, menu opened, block changed or runtime started.

For opening disposition, apply the inspected ordinary container source with an
unlocked container and no entity blocking the chest. This is a declared modeled
access condition, not a statement that cats or other entities were observed absent.
The raw block entities contain no Lock key. Keep generated/acquired loot and live
interaction outcomes NOT MEASURED. Modded interception is not tested by a ray.

Container derivation, using the hash-verified mapped Minecraft server JAR already
bound by capture.sh (SHA-256 26ca9c40d7e1681190b428583c38816852218e78df3f8bdb60a59a78503aec71):

- ChestBlock.getShape returns its single-chest AABB for the saved type=single.
  The retained runtime shape is [0.0625,0,0.0625,0.9375,0.875,0.9375].
  From eye(463.5,49.12,431.5) toward(463.5,49.5,430.5), only the air voxel
  at 463,49,431 precedes that chest. The first chest-face intersection is at
  z430.9375,y49.33375. The full aim distance is sqrt(1+0.38^2)=1.06977,
  below the declared 3-block limit. No template-volume proxy is involved.
- The barrel ray from(466.5,49.12,431.5) to(466.5,48.85,430.99) has length
  sqrt(0.27^2+0.51^2)=0.57706. It passes through air at Y49, then the sign
  voxel 466,48,431. WallSignBlock.getShape selects a facing-dependent AABB;
  every variant in its initializer lies between local Y 4.5/16 and 12.5/16.
  While the ray is in that sign voxel, its lowest Y is 48.855294, above the
  sign's maximum 48.78125. It then hits the full barrel front face at z431.
  Treating the whole sign voxel as opaque would have falsely rejected this line.
- ChestBlock.isBlockedChestByBlock offsets 0-17 test the block above with
  isRedstoneConductor, not mere non-air occupancy. The saved block above is a
  top, north-facing straight crimson stair. Its runtime AABB union omits the
  local region with y<0.5,z>0.5, so it is not a full collision cube.
  Blocks' crimson_stairs registration invokes legacyStair(CRIMSON_PLANKS).
  legacyStair uses Properties.ofLegacyCopy, which retains the new default
  redstone predicate. StairBlock passes those properties directly to its Block
  superclass constructor. Properties constructor bootstrap 3 points to lambda$new$4,
  which tests isCollisionShapeFullBlock. This gives an unblocked-by-block
  source disposition; the separately declared no-sitting-cat condition still
  matters. No live lid animation or menu was observed.
- BarrelBlock.useWithoutItem directly obtains its BarrelBlockEntity and calls
  Player.openMenu; it has no chest-style block-above or sitting-cat check.
  Both the chest and barrel use paths invoke PiglinAi.angerNearbyPiglins.
  That source call is not an observed aggro outcome or an Item 14 AI experiment.

Reproduce the direct source inspection with the pinned javap -p -c, using classes
net.minecraft.world.level.block.ChestBlock, BarrelBlock, WallSignBlock, Blocks,
and net.minecraft.world.level.block.state.BlockBehaviour$Properties. Use -v for
Properties to inspect bootstrap 3's lambda binding. Resolve the short block class
names under net.minecraft.world.level.block. The saved voxel references and
runtime AABBs above are retained in the existing first-house dataset/collision
projection. Direct immutable-artifact inspection requires no additional capture
or validator solely to restate these facts.

## First-house route context and movement support

The corrected r3 swept volumes intersect twelve saved palette states: air;
closed top crimson trapdoor; crimson and warped wall signs; floor and wall
polished-blackstone buttons; twisting vines and twisting-vines plant;
the saved-open warped door's two halves; bottom warped slab; and closed bottom
warped trapdoor. These are voxel intersections, not collision counts. None is a
fluid or saved waterlogged state. The full retained AABB sweep still includes
neighboring shapes, including any extension beyond its originating voxel.

Direct pinned javap inspection of the hash-verified mapped server JAR, SHA-256
26ca9c40d7e1681190b428583c38816852218e78df3f8bdb60a59a78503aec71,
finds no getCollisionShape override in AirBlock, TrapDoorBlock, DoorBlock,
SlabBlock, SignBlock, WallSignBlock, ButtonBlock, GrowingPlantBlock,
GrowingPlantHeadBlock, GrowingPlantBodyBlock, TwistingVinesBlock or
TwistingVinesPlantBlock. Their inspected intermediate bases Block, BaseEntityBlock,
HorizontalDirectionalBlock and FaceAttachedHorizontalDirectionalBlock also have
no override. BlockBehaviour.getCollisionShape offsets 0..19 tests hasCollision,
then returns either Shapes.empty or state.getShape(BlockGetter,BlockPos), without
reading the supplied CollisionContext. Therefore these mapped implementations
supply the same collision result regardless of supplied actor context. This is
source support for the declared static model, not proof against every runtime
transformation or a full-stack actor experiment. The captured frozen-runtime
empty-context shapes remain the actual geometric input. Do not relabel their
352 standing centers as observed reachable player positions.

Reproduce this direct inspection using the pinned javap from repository root:

```sh
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -p -c \
  -classpath instances/pristine-baseline-v0/libraries/net/minecraft/server/1.21.1-20240808.144430/server-1.21.1-20240808.144430-srg.jar \
  net.minecraft.world.level.block.state.BlockBehaviour
```

For the inheritance checks substitute each named class under
net.minecraft.world.level.block. The existing captured Attributes initializer
742..769 gives default step height 0.6; LivingEntity.createLivingAttributes
39..42 adds that attribute and maxUpStep reads it. Combined with the retained
vine/tag derivation, this supports the explicitly default, unmodified-capability
kinematic route. R3's 0.3125 step/drop transitions occur at slab contact/loss
boundaries; the checker rejects the earlier unsupported center ascent. This
supports modeled movement only, not literal tick trajectories or measured speeds.
