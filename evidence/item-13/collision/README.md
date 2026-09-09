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
