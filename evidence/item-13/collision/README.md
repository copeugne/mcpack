# Saved-view collision pilot

Status: first capture PASSED for empty-context geometry only. This resolves the specific missing collision
geometry for the first selected Medium House. It does not establish playable
rooms, actor movement, traversal time or combat outcomes. The original selected
[raw house](../fixed-blocks/mns-medium-house.json.gz) remains authoritative for
terrain. Its SHA-256 is
`a61dc454a22b0058d765da277fbd6c7e450dc597f1ff8b42da66b288247e7496`.

## Bounded experiment

One fresh, hash-verified retained-136 materialization uses the existing Item 7
preflight, pinned Java, frozen configuration and construction heap. Runtime
startup supplies registered block behavior. Its incidental spawn terrain is not
sampled and is not new dungeon evidence. The probe's BlockGetter reads only the
already verified house dataset. No accepted world is opened or mutated.

The actor is absent. CollisionContext.empty is used, with the original saved
states and no neighbor updates, interactions, equipment, navigation or encounters.
There are no permitted gameplay bypasses because this is not a traversal trial.
The query starts after server readiness and evaluates all 8,500 saved positions
in YZX order, including padding. Each palette state must survive exact codec
round-trip validation. Shapes are local AABB unions; position-specific results
are retained even when palette entries are identical. Dynamic-shape flags are
reported per palette entry. Unsupported saved-view queries, including block
entities and outside-view neighbors, produce explicit censored cells with index
-1 and reason. They are never treated as empty collision. Unexpected exceptions
reject the experiment. No player-shaped collision equivalence is claimed.

Only Nether build limits (minimum 0, height 256) are supported by this pilot.
Context-sensitive collision, fluid movement, climbability, opening doors and
trapdoors, jumping, step height and continuous actor clearance remain separate
requirements before a route can be scored. Empty-context output alone cannot
satisfy them. Expansion to another input requires a new declaration and fresh
materialization, not reuse of a running or stopped instance.

The query has a 30-second server-thread limit, attach process 45 seconds, server
readiness/capture 600 seconds and clean exit 120 seconds. Build commands each
have 45 seconds. The existing correlated save-all flush and clean-stop lifecycle
is reused without registry dumps. Timeout or I/O failure kills the complete
process group and preserves the failure. One initial run is planned; another
fresh run is needed only for a demonstrated defect or a reproducibility claim.

Storage estimate: 485,621,323 bytes of retained mod inputs plus the existing
181 MiB platform copy, configuration and startup outputs. Budget 2 GiB for the
fresh instance and 20 MiB for logs and projection; require 5 GiB free (the host
had 40,519,127,040 bytes free at planning). These are planning ceilings, not
measured results or enforced disk quotas. Stop expansion if observed sizes
exceed them. No additional downloads or installations are planned.

## Reproduction and acceptance

Commit the producer and declaration first, then run with absent paths:

```sh
uv run python -m evidence.item-13.collision.run evidence/raw/item13/collision-r1 instances/item13-collision-r1
```

The runner retains its preflight, lifecycle, configuration audit, exact source
revision, agent JAR and input/output hashes in capture.json. Input and runtime
identities must match this declaration; clean shutdown alone is insufficient.
After inspection, commit the projection and relevant logs/identity result under
this directory, preserving failures and removing no raw observations. Inspect
logs for prohibited operational identifiers before committing any log; retain
original bytes outside Git when a redacted projection is needed. Existing raw
storage/custody mechanisms apply if retained outputs exceed ordinary Git size.
The throwaway startup world is not an empirical input or accepted world and
requires no new dungeon archive. Preserve it locally until the result is accepted.

The Java agent reuses the unchanged Item 8 attach launcher. A narrow lifecycle
extension permits an empty registry selection and a validated JSON output
basename. This prevents repeating the completed registry survey. Tests exercise
probe-only correlated flush and path rejection alongside existing failure cleanup.
The agent compiles with the pinned JDK and explicit classpath, -Xlint:all -Werror.
The first build attempt without explicit classpath failed on an inherited invalid
classpath entry; no server ran. The explicit-classpath build passes.

## First capture result

Source revision: `7320840758736e360697d6f932b5f524ec94a2aa`. The declared command
completed in 206.424 seconds. The fresh instance occupied 650 MiB and capture
folder 6.4 MiB by du, within the planning ceilings. Preflight verified all 136
retained candidates, runtime identity and frozen manifest/audit. Readiness,
correlated flush, stop and exit code 0 passed without process-group killing.
The post-run audit retained 228 configuration files and only the four permitted
comment-only normalizations. No registry dump or gameplay trial ran.

The [projection](r1-collision.json.gz) records 8,500 cells, 151 saved palette
states and 42 distinct local AABB unions. All cells have valid shape indices,
no unsupported query was reported, and all palette dynamic-shape flags are false.
Bounds and palette/voxel lengths were checked against the hash-bound raw input.
An initial verification assertion incorrectly expected 146 palette states from
working notes; comparison against the actual saved input corrected that check to
151. No producer or raw output was changed to satisfy it.

The original output SHA-256 is
`e594135780e485250a7be9145904f588d591118302dd626862a3cb64759e3fb3`.
The [capture result](r1-capture.json.gz) records lifecycle, identities, elapsed
time and configuration audit. The [console](r1-console.txt.gz) preserves startup,
warnings and lifecycle text with only its bind endpoint redacted. Empty attach
and build logs are retained too. These five compressed outputs total 43,482 bytes.
[Retention identities](r1-retention.json) bind original and published hashes;
`uv run python -m evidence.item-13.collision.retain` reproduces them from the
original capture into absent destination files. It refuses overwrites. Original
console, full debug/latest logs, compiled probe and captured configuration remain
under `evidence/raw/item13/collision-r1/`; their broader raw custody remains pending.
Do not claim that local retention is independent redundant storage.

Source inspection of the hash-verified mapped server JAR
`26ca9c40d7e1681190b428583c38816852218e78df3f8bdb60a59a78503aec71`
shows `BlockBehaviour$BlockStateBase.initCache` offsets 36-58 populate a cache when
hasDynamicShape is false. However, the three-argument getCollisionShape used by
this probe delegates directly to Block.getCollisionShape at offsets 0-14. The
two-argument overload's cache return is not the call made here. Accordingly,
non-dynamic flags alone do not prove actor-context independence. Reproduce this
inspection with the pinned javap, `-p -c -classpath` pointing to the existing
mapped server JAR and quoted class name
`net.minecraft.world.level.block.state.BlockBehaviour$BlockStateBase`.
This is source inspection, not evidence that every retained override is context
independent. The 42 unions support the declared empty-context geometric view;
actor clearance, interaction changes and playable topology remain unresolved.

## Predeclared standing-clearance pass

For the first house only, compute static standing positions at each X/Z block
center inside the original structure envelope. Candidate feet heights are the
upper faces of retained collision AABBs directly beneath that center. Require
positive-height support and a collision-free 0.6-wide, 1.8-high upright box.
Touching a face is allowed; positive overlap is collision. Use the captured
empty-context shapes exactly, including neighboring padding where a box crosses
a cell boundary. Doors, gates and trapdoors retain their saved states. No opening,
mining, jump, step, climbing, fluid travel or enemy interaction is modeled in this
pass. It establishes static clearance, not reachability or room membership.
Actor-context equivalence remains conditional as described above.

Denominator is every envelope column and every supported candidate height within
the envelope's Y range. Output each accepted center and feet height plus counts
by height. Unsupported collision cells would reject this pass rather than appear
passable. Restrict queries to the retained bounds. Budget: 60 seconds, 100 MiB RSS,
1 MiB output, no runtime or world reads. This directly addresses the missing
occupiable-space geometry before graph links are inferred. Do not count these
positions, disconnected air regions or height bands as rooms.

Standing pass result: [r1-standing.json](r1-standing.json) retains 352 accepted
positions out of 1,411 distinct supported candidate positions across the 209
original-envelope columns. It took 0.039 seconds, 43,652 KiB peak RSS and 18,101
output bytes. A second execution reproduced the output byte for byte. Focused
face-touching and positive-overlap checks pass, including floor and ceiling
boundaries. Use `uv run python -m pytest evidence/item-13/collision/test_clearance.py`
from repository root; the initial bare pytest invocation lacked the repository
on its import path and failed collection before any test ran.

Reproduce with an absent output path:

```sh
uv run python -m evidence.item-13.collision.clearance /tmp/item13-standing-new.json
```

Direct block inspection validates a lower-floor strip from center 461.5,45,432.5
through 466.5,45,432.5. Its six floor blocks at Y44 are deepslate bricks, polished
blackstone bricks or stripped warped hyphae. Y45 contains air, wall signs and
buttons; Y46 is air. This supports the local clearance result, not entry-to-exit
connectivity. Buttons are not assumed harmless working mechanisms without their
trigger context. The upper reward bands need crouching and connection checks.
Existing Player source in `../model-source/captured/world.entity.player.Player.txt.gz`,
static initializer offsets 136-143, supplies the 0.6 by 1.5 crouching dimensions
for that next declared sensitivity pass. No crouched result is claimed here.


Crouching sensitivity predeclaration: repeat the identical saved-state geometry
at height 1.5, width 0.6, using the Player source dimensions cited above. Keep
all columns, support rules, bounds, door states and failure rules unchanged.
Compare accepted positions with the retained upright result; report additions
without treating crouching clearance as a climbing or navigation connection.
The same 60-second/100-MiB/1-MiB ceiling applies. No new runtime experiment occurs.


Crouching result: [r1-crouching.json](r1-crouching.json) accepts 358 of the same
1,411 candidates. All 352 upright positions remain accepted. The six additions
are 458.5,54.5,431.5; 459.5,48.5,431.5; 459.5,48.5,433.5;
469.5,48.5,431.5; 469.5,48.5,433.5; and 471.5,48,428.5. None adds standing
clearance in the central upper reward bands. This is not proof that rewards
cannot be reached by interaction, crawling, climbing, mining or external access.
A second execution reproduced this output byte for byte; focused collision tests
and type/lint checks pass. Reproduce using the command above with `--height 1.5`.
For exact original upright output reproduction, use the producer at commit
`40bc9f43`; the later optional height parameter changes its producer hash but
preserves the default calculation. Do not overwrite the historical upright result.

## Predeclared local route verification

The next geometric check uses the upright actor and the saved-open right-hand
door. Start/end is its center at 467.5,45,435.5, excluding external approach.
Follow the lower floor west to the twisting vines at 461.5,45,431.5, climb to
47.5, and transfer east onto the storage balcony. Traverse its two slab spans
and the central trapdoor, with a 0.3125 descent/ascent, to 466.5,47.5,431.5.
Return by the same connection. Coordinates are retained by the route producer.

Check the complete swept actor box of each cardinal or vertical segment against
all captured AABBs, not just its endpoints. Floor support and vine contact are
separately inspected at the recorded blocks; collision freedom alone is not a
movement rule. The model permits continuous vine climbing and 0.3125-block steps,
without block changes, jumping, flight, combat or container interaction. It has
full layout knowledge. No actor-context equivalence or realized gameplay is
inferred. Use the same 60-second/100-MiB/1-MiB processing budget as clearance.
A collision or missing support rejects the proposed connection before scoring.


First route attempt: [r1-route.json](r1-route.json) is REJECTED for upright
crossing. Eight of sixteen swept segments intersect the soul lantern at
464,49,431, whose local world AABB is
[464.3125,49.0625,431.3125,464.6875,49.5,431.6875]. The lower doorway/floor
segments and vertical vine segment are clear. The proposed raising maneuver at
the central trapdoor also intersects the lantern. No successful complete route
or room graph is inferred from this failure. The next attempt will crouch before
crossing this known obstruction, using the already declared 1.5-high profile.

Floor/source inspection: the lower six-block strip at Z432 has full solid support
at Y44. The west vine column at 461,431 contains twisting_vines_plant at Y45-46
and twisting_vines at Y47. The balcony has bottom slabs at X462-463 and465-466,
Y47,Z431, with the central trapdoor top at47.1875. These are authored floor and
vine transitions, not structure-piece counts. The mapped Player/LivingEntity
source and vanilla climbable tag support a conditional vine-climbing model.
The hash-verified vanilla extra JAR SHA-256 is
24a5d2d162cfad2a1a574c4d552e99dc6c6303a49d1e68b43a7b638f3b0930fd;
its data/minecraft/tags/block/climbable.json includes both twisting-vine IDs.
Direct inspection of that tag path in the hash-verified 136 retained candidates
found ten additive declarations and no replacement: BetterEnd, Biomes O' Plenty,
Farmer's Delight, Quark, YUNG's Cave Biomes, Chipped, Create, Deep Aether,
Regions Unexplored and Supplementaries. This packaged-source check is not a new
runtime tag measurement. LivingEntity.onClimbable offsets19-38 test CLIMBABLE.

Exact raw producer/helper hashes are retained. This rejected iteration has two
style findings (successive-pair iteration and a now-unnecessary complexity
suppression), to be corrected with the next producer version while preserving
this one for exact reproduction. Focused types pass; the shared AABB expansion
preserves every default upright clearance value apart from producer identity.


Second route attempt predeclaration: use the identical route and states, but
shrink to the source-supported 1.5-high pose before balcony travel and restore
upright pose at the vine transfer point before descending. Keep the lower floor
and vertical vine segments upright. The capture already contains both pose
clearance inputs; this is deterministic geometric processing, not a second
runtime experiment. No lantern removal, changed block or unreported bypass is
permitted. Reuse the same processing budget and preserve the rejected upright
result unchanged. This resolves one demonstrated obstruction only.


Second route result: [r2-route.json](r2-route.json) passes all sixteen swept
segments with crouched balcony movement and upright lower-floor/vine movement.
The complete result reproduces byte for byte. This is conditional geometry and
manual support validation, not observed gameplay or container opening. Original
rejected route and its exact producer remain at commit375ceb5d. Shared expansion
now rejects omitted collision cells; two focused tests and focused types pass.
One minor literal-style finding remains in this producer version and will be
fixed separately without rewriting its raw output. The related initial pairwise
and unused-suppression findings have been fixed.

The [house quality assessment](../fixed-blocks/mns-medium-house-report.md) integrates
room sensitivity, connections, roof-cavity exclusion, contents and unresolved
requirements. Its source-derived statements are not additional runtime samples.


The literal-style finding is now resolved by using the declared entry's floor
height as the pose boundary. Focused lint, types and two collision tests pass.
Both rejected upright and accepted crouched outcomes remain unchanged. For exact
r2 output reproduction use producer/helper commitc35c925c; later style cleanup
changes only the producer identity field. No raw capture was rewritten.

## Predeclared route-time model

Apply only to retained r2-route.json, SHA-256
1174496c1e0629df468b31516a0d70ca583d9c485094b9a39bc808e9720c9aca.
The actor, knowledge, poses, no-block-change rule, route start/end and movement
sequence remain those of the accepted geometric route. Reuse the pilot equipment:
unenchanted iron armor, iron sword and pickaxe, with no buffs, flight, teleport,
sprinting or additional building. Speeds remain stipulated model inputs. This is a local inspection
circuit visiting the lower space and balcony, not a shortest route, whole-building
clear or completed all-container survey. No encounters are simulated. No combat,
activation wait, menu time, looting, external approach, roof breaching or reaction
time is included. The sealed roof cavity is outside this circuit.

Separate upright horizontal, crouched horizontal, vine vertical and small
trapdoor vertical distances. Use rate vectors in that order, in blocks/second:
nominal (4,1.2,1,0.5), faster (5,1.5,2,1), slower (3,0.9,0.5,0.25).
The upright values reuse the declared pilot/Item 11 rate assumptions; all other
rates are explicit sensitivity inputs, not measurements or source-derived speed
claims. Charge both descent and ascent, including each modeled trapdoor height
adjustment. Do not call the faster/slower values empirical bounds or confidence
intervals. Runtime stalls, navigation, encounter interruption and failure can
produce arbitrarily longer real times. A rejected/nonclosed route or input hash
mismatch rejects modeling. Report feet-height span and accumulated ascent/descent
separately from distance. Graph depth and terrain cover are separate quantities.

Reproducible command after implementation, with absent output:

```sh
uv run python -m evidence.item-13.collision.house_route --measure /tmp/item13-house-route-model.json
```

This small arithmetic transformation reuses retained observations and needs no
world restore or runtime experiment. The existing 60-second/100-MiB/1-MiB
processing ceiling applies.


Route-time result: [r2-route-model.json](r2-route-model.json) records 36.25 blocks,
2.5 feet-height span and 3.125 ascent/descent each. Nominal 20.833333 seconds,
faster 14.416667 and slower 32.777778 are scenario budgets only. Direct arithmetic
20/4 +10/1.2 +5/1 +1.25/0.5 independently checks the nominal result. Reproduction
is byte-identical. Two collision tests plus focused lint/types pass. No accepted
raw route, collision capture, world or configuration was changed.

## Predeclared saved-spawner lookup experiment

The precise missing fact is whether the four first-house SpawnData assignments
resolve to registered entity types in the frozen runtime. Decode each saved
SpawnData through the runtime CODEC, then call EntityType.by on its decoded tag.
Record position, decoded ID, optional resolved entity type and saved potential-list
length. Denominator: all four saved ordinary spawners in the same hash-bound house
input. Reject any decode failure or count mismatch. No player, actor equipment,
combat, navigation, spawner tick, entity creation or world modification is part
of the query. The expected empty assignments are a question, not a forced result.
No observed spawning or encounter claim may be inferred from a type lookup.

Use the existing probe launcher, fresh retained-136 materialization, frozen
configuration audit and correlated save/clean-stop lifecycle. Skip the completed
collision pass and registry dumps. The new instance's incidental startup world
is not dungeon evidence; the query reads only saved input and runtime registry.
Each failure is retained and any retry requires fresh paths/materialization.
One run is planned. Reuse the30-second server-thread,45-second attach,600-second
readiness/capture and120-second clean-exit limits. Based on the previous capture,
budget2 GiB instance storage and20 MiB capture output with5 GiB free required;
39,830,286,336 bytes were free at planning. Expected duration is comparable to
the previous206-second startup/capture lifecycle, not a measured duration yet.

After committing the producer and declaration, run:

```sh
uv run python -m evidence.item-13.collision.run --spawner-lookup evidence/raw/item13/spawner-lookup-r1 instances/item13-spawner-lookup-r1
```

Source inspection already narrows the result: SpawnData's constructor does not
insert an ID into an empty entity tag. CompoundTag.getString returns an empty
string when the key is absent; ResourceLocation.parse then uses the default
namespace, and its path predicate permits the empty string. EntityType.by uses
DefaultedMappedRegistry.getOptional, which calls MappedRegistry.get directly and
does not substitute the default entity. The remaining registry-presence question
is what this experiment resolves. These methods are directly reproducible with
the pinned javap -p -c against the hash-bound mapped Minecraft JAR, using classes
net.minecraft.world.level.SpawnData, net.minecraft.nbt.CompoundTag,
net.minecraft.resources.ResourceLocation, net.minecraft.world.entity.EntityType
and net.minecraft.core.DefaultedMappedRegistry. No new source-extraction framework
is needed to restate those immutable artifact inspections.

The previous frozen-runtime debug log reports three BaseSpawner mixins: Servercore,
Aether's accessor and Collective. Direct inspection of their classes shows a
post-entity mob-cap check, a nextSpawnData getter and an existing-mob tag addition,
respectively. None inserts a missing entity ID. Their JAR hashes match the accepted
Item3 acquisition manifest. This is source/transform evidence, not a spawner tick.


### Saved-spawner lookup result

The [runtime projection](spawner-r1-spawners.json.gz) and
[capture result](spawner-r1-capture.json.gz) are from producer commit 48089961.
The run completed in 229.279 seconds, with readiness, correlated flush, clean
exit 0 and no process-group kill. Retained 136 runtime identity and the 228-file
configuration audit passed; only the four permitted comment normalizations
occurred. Instance/capture sizes were 650 MiB/6.4 MiB by du, within budget.

All four SpawnData values decoded successfully through the actual runtime CODEC
using JsonOps over their retained JSON projection. These particular entity data
contain only an ID string or an empty compound, so no numeric-NBT conversion
claim is involved. The assignment at 465,48,430 resolves to minecraft:piglin.
Assignments at 462,51,432;465,48,434;466,51,432 preserve empty decoded IDs and
return lookup_present=false. Their saved SpawnPotentials lists are empty.
No default pig or other entity type is substituted. Null optional type fields
are omitted by Gson, so the explicit lookup_present boolean is authoritative.

The [existing BaseSpawner source](../model-source/captured/world.level.BaseSpawner.txt.gz)
loads present SpawnData at offsets 21-71 and present SpawnPotentials at 85-139.
serverTick returns after delay when EntityType.by is empty, before entity
creation. delay offsets 51-67 only selects a replacement when the potential list
has a random entry. getOrCreateNextSpawnData retains a nonnull assignment.
Together with the runtime lookup and inspected mixins, this supports the baseline
disposition: these three assignments have no resolvable enemy potential and do
not reach creation through that path unless reconfigured. It is not an observed
activation, zero-mob gameplay session or proof about unrelated natural spawns.
Do not repair them or count them as independent enemy species.

The same disposition applies by input equivalence to the two empty assignments
in [Medium House 2](../fixed-blocks/mns-medium_house_2.json.gz), at 14,40,112 and
18,40,112: each has exactly SpawnData={entity:{}} and SpawnPotentials=[]. The
raw files already bind that world's same frozen runtime. This is reuse of the
verified decoding/type behavior, not another runtime sample or full variant
quality assessment.

The [retention record](spawner-r1-retention.json) binds original and published
hashes. Projection, capture, redacted console and two empty diagnostic logs total
42,046 compressed bytes. Reproduce retention with
`uv run python -m evidence.item-13.collision.retain --spawner-lookup` into absent
published files. Original logs/configuration remain at the declared raw path;
broader raw custody is still pending. No collision pass, registry survey or
accepted-world modification occurred.

## Movement-support correction and third route predeclaration

The r2 swept boxes prove collision freedom only. Subsequent support inspection
finds its ascent at X464.5,Y47.1875,Z431.5 is in the center of the lowered
trapdoor, away from a slab riser. The preceding horizontal segment also delays
the drop until that center. Preserve r2 and its timing as a rejected movement
sequence; do not treat collision freedom as validated support.

For r3, keep all lower-floor and vine waypoints, equipment, poses and timing
rates. Replace the balcony center descent/ascent with these ordered points:
(464.3,47.5,431.5), (464.3,47.1875,431.5),
(464.7,47.1875,431.5), (464.7,47.5,431.5), then the existing east endpoint.
The 0.6-wide actor loses overlap with the west slab at center X464.3 and
contacts the east riser at X464.7. Reverse the same sequence on return.
This is a piecewise kinematic drop/step model at the support boundaries, not
literal tick-by-tick physics. The captured Attributes static initializer
742..769 supplies default STEP_HEIGHT 0.6; LivingEntity.createLivingAttributes
39..42 adds it and maxUpStep reads it. The declared 0.3125 step is within that
source-supported default, assuming no modifier. Vine support remains as declared.
Recheck every swept segment with the existing checker. Retain failures, and
reject a collision before using the corrected route. Same 60-second/100-MiB/1-MiB
processing ceiling; no new world or runtime. Existing --measure remains the
historical r2 calculation with its explicit input hash, not the corrected model.
For r3 timing use the direct distance/rate derivation in the house report.


R3 result: [r3-route.json](r3-route.json) passes eighteen swept segments and the
new adjacent-support/default-step checks. A focused regression rejects r2's
collision-free but unsupported center ascent. All three focused tests, lint,
formatting and types pass; r3 reproduces byte for byte. Initial geometric output
before the support-check addition remains in ignored
`evidence/raw/item13/route-support-draft/r3-route.json`; it is not the accepted
producer. The authoritative r3 includes the final producer hash. Distance and
rate arithmetic are integrated in the house report. Reproduce into an absent path:

```sh
uv run python -m evidence.item-13.collision.house_route --crouch-balcony /tmp/item13-r3-route.json
```

Mapped-source collision-context support is now recorded in the
[model derivation](../model-source/README.md#first-house-route-context-and-movement-support).
Earlier r2 support claims above are superseded by this correction; its raw
collision result and arithmetic remain preserved without rewriting.


## Second-house saved-view collision predeclaration

Requirement: validate the second fixed house layout's playable topology. Its
127 saved states and changed floor/door/ledge arrangement cannot be replaced
by the first house's shapes. Reuse the unchanged Java probe and lifecycle, adding
only a second pinned input choice and distinct retention prefix to the existing
runner. This is the same evidence class, not a new validator or framework.

Input: fixed-blocks/mns-medium_house_2.json.gz, SHA-256
c1fa53cbbae3cc48f56a48baacdfd80746bd937662a57db35d49f98b698447a6,
8,500 voxels, bounds [4,29,104,28,48,120], one preselected fixed-layout case.
One fresh frozen runtime materialization and one collision query are required.
No actor is present. Keep both doors closed as saved; do not create/open a door,
spawn mobs, populate containers or change the source world. The query returns
empty-context AABB unions, palette flags and unsupported queries just as before.
The already-resolved empty-spawner lookup is not repeated. Door-opening geometry
and actor movement are subsequent declared models, not observations from this run.

Runtime/configuration pins and readiness, correlated flush, clean-stop and failure
rules are unchanged. The existing runner verifies 136 artifacts, frozen config,
pinned Java and a new target. Before launch, free space is 39,374,368,768 bytes.
Budget: 2 GiB instance, 20 MiB capture, 600-second lifecycle readiness budget,
30-second server-thread query, 45-second attach and 120-second clean exit.
The earlier equivalent-size query took 206.424 seconds end to end; this is a
planning reference, not a promised duration or a second measurement. Preserve
any failed run and do not expand beyond the selected 8,500 voxels. A missing
shape remains unsupported and prevents dependent route acceptance.

Reproducible commands (new paths; execution result to follow):

```sh
uv run python -m evidence.item-13.collision.run --second-house evidence/raw/item13/house2-collision-r1 instances/item13-house2-collision-r1
uv run python -m evidence.item-13.collision.retain --second-house
```

The retained projection and capture record will bind the input and producer.
The original full logs/configuration remain preserved under raw custody, with
publication using the same explicit console bind-endpoint redaction. Broader
raw-capture durability remains an existing required follow-up.


Second-house result: [house2-r1-collision.json.gz](house2-r1-collision.json.gz)
retains all 8,500 cells, 127 palette states and 39 local AABB unions. Unsupported
queries=0 and dynamic-shape flags=0. Source revision
89270e5ad550e9487fde9ba7fad1d3389c00fccf; original projection SHA-256
abf226b25481338229c5e15074de548be576171ea6e9709057704cdfbf58f0df.
The [capture record](house2-r1-capture.json.gz) confirms readiness, matched flush,
clean exit code 0, no process-group kill, and 228 configuration files with the
same four permitted runtime comment normalizations. Elapsed time 211.427 seconds;
instance 650 MiB and raw capture 6.4 MiB, within the declared ceilings.

The [retention manifest](house2-r1-retention.json) binds 43,396 compressed bytes
of projection, capture, console and build/attach output. Hash and size checks
passed for every retained file. Console publication redacts only the bind
endpoint; original raw logs remain preserved. The full raw-capture custody
follow-up is still open. Both right-door halves retain the closed local AABB
[0,0,0.8125,1,1,1]; the probe did not open either door or simulate an actor.
Zero unsupported shapes is geometric coverage, not completed topology or gameplay.


## Second-house first route predeclaration

Use the previously declared right-door opening model and first-house actor,
equipment, full knowledge, rates and exclusions. Start/end at (19.5,34,115.5)
after opening; door interaction latency and external approach are excluded.
Lower route: (19.5,34,112.5), (15.5,34,112.5), (15.5,34,114.5),
(14.5,34,114.5). Climb the south vine to (14.5,36.5,114.5), crouch, then
travel north with points (14.5,36.5,112.7), (14.5,36.1875,112.7),
(14.5,36.1875,112.3), (14.5,36.5,112.3), (14.5,36.5,111.5).
Return in reverse, restoring upright pose for vine descent. The trapdoor
transitions occur at slab support-loss/contact boundaries for a 0.6-wide actor.
No jump, mining, flight or other door change is permitted.

Reuse the complete swept-box checker. Its only required extensions are the
second saved input/waypoint choice, the two explicit door-box substitutions,
and slab adjacency in Z as well as X. This avoids duplicating verification code.
Reject source/state mismatch, unsupported shapes, collision or missing step
support. Manual lower-floor and vine support remain required. Do not score a
failed route. Budget remains 60 seconds, 100 MiB memory and 1 MiB output; no
new world restore or runtime experiment. Retain this first attempt even if it
fails. A valid path supplies one connection, not proof of every possible route.


Second-house first route result: [house2-r1-route.json](house2-r1-route.json)
passes twenty swept segments with supported Z-axis slab transitions. The
original first-house r3 segments remain identical under the extended checker.
Four focused tests, lint, formatting and types pass; the new route reproduces
byte for byte. The new regression rejects an unsupported centered Z transition.
Reproduction (absent output):

```sh
uv run python -m evidence.item-13.collision.house_route --second-house --crouch-balcony /tmp/item13-house2-route.json
```

Historical first-house outputs retain their original producer references; the
additional modeled-state field and second-layout support do not rewrite them.
Manual floor/vine support, route arithmetic and three barrel rays are integrated
in the [second-house assessment](../fixed-blocks/mns-medium_house_2-report.md#validated-south-vine-circuit-and-storage-access).
The north-vine alternative remains pending before final graph and depth scoring.


## Second-house north-vine predeclaration

The remaining potential connection is the north vine at (14,110). Keep the
same input, right-door substitution, actor, capabilities, poses and exclusions.
Proposed outbound points: (19.5,34,115.5), (19.5,34,112.5),
(15.5,34,112.5), (15.5,34,110.5), (14.5,34,110.5),
(14.5,36.5,110.5), (14.5,36.5,111.5). Reverse them for return.
The lower route is upright, the vine climb upright and the upper segment
crouched. No trapdoor transition occurs on this connection. Use the existing
complete-sweep checker with a second-house north-vine waypoint choice; do not
alter either earlier route or repeat collision capture. Manual floor/vine
support is required in addition to the sweeps. Same 60-second/100-MiB/1-MiB
processing budget, input checks and rejection rules. If accepted, compare both
validated connection lengths to the same storage station before depth scoring.


North result: [house2-north-route.json](house2-north-route.json) passes twelve
swept segments and reproduces byte for byte. New lower-floor support and the
continuous vine were inspected directly in the retained raw blocks. Both earlier
routes' segment arrays remain unchanged under the current checker; four focused
tests, lint, formatting and types pass. An initial draft before the branch-count
lint correction is preserved under evidence/raw/item13/north-route-draft/.
Use the final producer for exact output reproduction:

```sh
uv run python -m evidence.item-13.collision.house_route --second-house --north-vine --crouch-balcony /tmp/item13-house2-north-route.json
```

The [second-house report](../fixed-blocks/mns-medium_house_2-report.md#north-connection-graph-and-depth)
now integrates both links, their graph sensitivity, scoped shortest distance,
traversal alternatives, reward access, finale and replay assessments. These
complete the local modeled assessment, not Item13 custody or final delivery.
