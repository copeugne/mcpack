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
