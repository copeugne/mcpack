# Item 10 sampling protocol

Status: FROZEN FOR FIRST FULL RUN, `item10-full-v1` (2026-09-08). The user-authorized
[scope amendment](methodology-amendment.md), `item10-automated-v1`, removes human
sessions and recording from both Items 10 and 11. The former combat collection
contract and blind-operator requirement are superseded for these items. No
human workload is scheduled or deferred as a completion condition.

## Current execution constraint

The [exit-gate reassessment](README.md#exit-gate-reassessment-2026-09-08)
supersedes prospective per-generator positive-pilot prerequisites. Historical
pilot outcomes remain unchanged. The reassessment, storage cleanup and existing
review obligations are complete. The applicable Item 7/10 gate passed all 535
tests in 152.60 seconds with `uv run --no-sync pytest -q tests/item7 tests/item10`.
Proceed with the first complete ordinary-seed baseline world, then verify actual
observer coverage, saved-world acceptance and resource costs before the remaining
15 worlds. Consolidate measurement/report into one delivery PR. Complete observation and correct
occurrence processing remain mandatory. Do not hunt for natural positive examples
or reinterpret a missing/broken observation mechanism as zero.

## Measurement boundary

Item 10 measures placement and provisional location categories. Encounter sites
are T1 through T4, actionable candidates are C and T1 through T4, proper dungeons
are exclusive T2, major expeditions exclusive T3, and T4 objectives are separate.
Villages use the accepted Item 9 `village` comparison group. These definitions
are potential location roles, not observed fights or meaningful human activity.
Retain confidence, ambiguity and the scope limitations in every final result.

The Item 5 methodology delta passed clean PR22 review and main delivery. The spatial
frame below is frozen for full collection. The fresh
registry pilot and its diagnostic processing remain reusable evidence. Complete
nonregistry occurrence coverage, biome attribution and the Sparse Structures
control must pass their implemented runtime/analysis gates for each world. Do not implement Item 11 workflows until
Item 10 delivery and the cross-item audit pass.

## Fixed spatial frame

Use all four exact seeds and the server/configuration hashes in [README](README.md).
Include all ten dimensions in the accepted
[runtime capture](../item-8/runtime/dimension-r3/dimension-biomes.json).
Treat the End as separate central and outer strata, giving eleven strata per seed.
Never pool different dimensions' coordinates or convert their distances by portal
scaling. The inclusion of space dimensions permits measured zeroes rather than
assuming the lack of structures from their names.

Use one 64 by 64 chunk rectangle per stratum: inclusive X and Z `[-32, 31]`,
translated by `(512, 512)` for outer End only (both axes `[480, 543]`).
The central and outer End rectangles are disjoint. Select every target chunk,
not only chunks that contain starts. This replaces the draft's four-stage ladder;
no full sampling run used that ladder and no observed count selected this area.
The historical scaffold remains unchanged and is not an active stopping rule.

Generation uses the existing Chunky square selection with radius `32c`, centered
at block `(0, 0)` or outer End `(8192, 8192)`. This requests 4,225 chunks per
stratum, including 129 edge chunks outside the 4,096-chunk census. The positive
edge at chunk 32 (544 for outer End) is excluded from all density denominators.
There are 46,475 requested generation chunks and 45,056 census chunks per world,
or 743,600 requested and 720,896 census chunks across 16 worlds. Further natural
generation halo remains possible. The explicit edge adds 3.1494140625 percent
to requested generation relative to the census; it does not change sampling.

This choice follows direct inspection of the pinned Chunky 1.4.23 JAR (SHA-256
`d72f235cf1f56f2c374f52c00bdda5034524b28142305a84cfc123a3f92ad274`). Its
`org.popcraft.chunky.iterator.Loop2ChunkIterator(Selection)` uses inclusive
`centerChunk +/- radiusChunks` bounds (bytecode offsets 31 through 60).
`CornersCommand.execute` converts corners to center and radii (179 through 323),
so corners alone do not avoid the odd-width iterator. Reproduce this inspection
with the pinned JDK's `bin/javap -c -p -classpath
downloads/item3/candidates/Chunky-NeoForge-1.4.23.jar` followed by either fully
qualified class name. `ITEM10_SELECTIONS` in the existing selection module binds
all eleven requests in lexical dimension order; `WorldgenRequest(mode="item10")`
rejects selection drift. Existing Item 7 pilot/run geometry remains fixed.
The focused regression command is `uv run --no-sync pytest -q
tests/item10/test_full_selections.py tests/item7/test_worldgen_lifecycle.py
tests/item7/test_protocol.py` (34 passed). This validates request geometry and
the reused lifecycle, not full collection or complete saved-chunk coverage.

Collect two independent fresh worlds per seed and arm, for four seeds, eleven
strata, two repetitions and two arms: 720,896 selected chunks in 16 worlds.
Each world contains all eleven fixed strata (45,056 selected chunks). Do not
reuse a baseline world for its control or a prior repetition. Use seed order
ordinary, mountainous, ocean-heavy, biome-diverse. Within each seed, run baseline
then control for repetition 1, control then baseline for repetition 2. Use the
same dimension order in every world, sorted by resource location, central End
before outer End. Keep both raw repetitions, even when their counts disagree.

### Full runner invocation

The existing runner accepts one full world at a time:

```sh
uv run --no-sync python -m tools.run_item10_probe \
  --name full-ordinary-r1-baseline --mode probe --preset item10 \
  --role ordinary --arm baseline --repetition 1
```

This is the first planned invocation. Its completed observation, saved-world,
custody and cost checks gate subsequent worlds. Use `without-sparse` for the matched control.
The runner requires the name `full-ROLE-rREPETITION-ARM`, explicit arm/repetition,
and probe mode for both arms. Its older `--mode control` disables the observer
and is rejected for full sampling. Placement fixtures are also rejected. Repeat
the command for each declared seed role, using `(1, baseline)`,
`(1, without-sparse)`, `(2, without-sparse)`, `(2, baseline)` in that order.
Each invocation requires absent instance/output paths and retains its existing
`diagnostic.json`, collector build identity and lifecycle outputs. The filename
is retained for compatibility with the existing custody path; its scope field
distinguishes full collection from diagnostic evidence. Report repetition and
arm are explicit, independent of the filename.

The full lifecycle ceiling is 14,400 seconds per world, an operational timeout,
not a measured duration or a new sampling stopping rule. Failure retains raw
outputs and cannot be accepted as a smaller census. The earlier 900-second
diagnostic ceiling remains unchanged. Actual time and storage must still be
checked on the first complete ordinary world before continuing the series.
Runner tests compile the real collector with the pinned JDK and substitute only
server execution; they verify both arms retain the observer and reject invalid
combinations. They do not establish runtime observer coverage.

The area is a finite-region census with a per-run density increment of
`1000 / 4096 = 0.244140625` locations per 1,000 chunks. It supplies 16 complete
256-block spatial cells per stratum, with explicit boundary censoring for
nearest neighbors. Two repetitions expose variability but do not establish its
population distribution. Report sparse categories and zeroes without asserting
absence elsewhere or precise global rates. These deliberately selected seeds
and fixed regions do not support random-world confidence intervals. This is
adequate for the specified descriptive comparisons, not stable rare-event rate
estimation; expanding until rare categories reach a target would change the
estimand and is not authorized by this protocol.

The spatial and repetition design is selected before collection. The full
protocol pins collector and control identities before launch. Complete runtime
occurrence coverage and measured storage costs are acceptance gates on the first
full world, not prerequisites requiring another small pilot. Failures remain
retained failures; changing this frozen protocol requires an explicit revision.

The [retained ocean-heavy failure](full-ocean-heavy-r2-without-sparse/README.md#narrow-lifecycle-correction-after-preservation)
exposed delayed shutdown on Java heap exhaustion. Failure handling now pauses
Chunky and attempts the existing correlated flush/stop with a 60-second save
confirmation allowance bounded by the run deadline. Timeout or console I/O
failure uses the existing whole-process-group termination path. Such a run is
always rejected, including after a confirmed emergency save. Successful-run
commands, sampling, observer identity and the pinned heap remain unchanged.

### Bounded retry amendment after the retained resource failure

Amendment identity: `item10-retry-policy-v1`, declared after the first failed
`full-ocean-heavy-r2-without-sparse` attempt and before any retry. This is a
post-failure operational amendment, not part of the original predeclaration.
The sixteen planned seed/repetition/arm cells and all spatial, classification,
observer and runtime identities in `item10-full-v1` remain unchanged.

Allow exactly one additional fresh attempt for this failed cell. The same seed
and complete frame passed in the first control repetition with identical
preflight, observer and selections; the preserved reports identify Java heap
exhaustion but not its allocation source. This supports a bounded same-identity
retry, not a claim that the cause was repaired. Do not increase heap, change
configuration, reuse the partial world or change the generation order.

Use `--attempt 2` and the distinct name
`full-ocean-heavy-r2-without-sparse-attempt2`. Default attempt 1 retains existing
names; new reports state the attempt number explicitly. Both output and instance
must be absent. Existing failed paths remain untouched. The runner adds only
this bounded naming option, without automatic retry or reset logic. It rejects
attempt numbers beyond two and attempt options on diagnostic presets.

Keep the first attempt as FAILED in the final run matrix with its incomplete
selections, raw custody, emergency save and unknown allocation cause. If the
retry passes, report seventeen attempted worlds for sixteen completed planned
cells, with one retained failed attempt. A failed attempt is neither a zero
observation nor an extra successful repetition. Results are conditional on
completed runs, with the resource failure disclosed; do not claim unbiased
random-world estimates. If this retry fails, stop collection for another explicit
resource/protocol decision. This amendment does not authorize retries for other
cells or repeated attempts until success.

The additional materialization and custody are estimated at roughly 2 GiB from
completed controls, beyond the original sixteen-world estimate. Before retry,
direct host inspection reports 24,166,539,264 free disk bytes (about 22.5 GiB)
and 9,385,078,784 available memory bytes. No cleanup is needed or authorized.
These current capacity observations are not a promise that Java allocation will
succeed within the unchanged 4 GiB heap. The heap-failure shutdown correction
must be present, and all normal full-census and durability gates still apply.

### Authorized continuation and final bounded retry

Status: USER AUTHORIZED, 2026-09-08. Amendment `item10-retry-policy-v2`.
The user approved the five remaining planned worlds, followed by exactly one
additional fresh attempt of ocean-heavy repetition-2 control. The user explicitly
rejected reducing the target to fifteen complete worlds. This supersedes the
unaccepted fifteen-world proposal and the exhausted v1 retry limit for this cell.

Execute in this order: ocean-heavy r2 baseline, biome-diverse r1 baseline,
biome-diverse r1 control, biome-diverse r2 control, biome-diverse r2 baseline,
then `full-ocean-heavy-r2-without-sparse-attempt3` with `--attempt 3`.
The original five cells each retain their planned first attempt. The final retry
uses a fresh absent instance/output path and the unchanged frozen configuration,
runtime, observer, heap, seed and complete selections. Both previous failures,
their raw archives and their original paths remain unchanged. No tuning, world
repair, reused proof world or further automatic retry is authorized.

The target remains sixteen complete planned cells and eight matched pairs.
If all six runs pass, report eighteen attempts, sixteen complete cells and the
two retained failed attempts. Failed attempts are not zeros or successful
repetitions. Preserve actual failures and censoring if any new run fails; do not
claim sixteen complete worlds or revise the target silently. Complete all five
planned runs before the final retry; assess any new failure without authorizing
an additional retry. Full census, custody, review, merge and cross-item audit
requirements remain unchanged. Successful-run results remain conditional on
completion, not proof of runtime reliability or a repaired Aether defect.

Reserve about 12 GiB for the six further materializations, censuses and custody,
based on the first ocean pair's approximately 1.86 and 1.92 GiB totals per world.
Generation plus census in that pair took about 16 to 18 minutes per world;
allow roughly two hours plus custody overhead, not a guaranteed bound. The
four-hour generation ceiling remains per attempt. Before this batch, free disk
is 21,946,347,520 bytes and available memory is 9,743,626,240 bytes. Recheck
capacity before each launch. No cleanup or human play is required.

The existing runner now accepts attempt 3 only for this exact role/repetition/arm.
Its focused collection tests pass 14 cases in 4.10 seconds, including preservation
of both previous attempt directories and rejection of other third-attempt arms
and attempt 4. Ruff check/format and focused test-file BasedPyright pass.

## Occurrences and denominators

### Frozen observer and full-trace gate

The full runner pins `tools/Item10PlacementProbe.java` to SHA-256
`b07ebcacb9043ee7d1fb187a7d93e5b788d890ccd8edc3decc07060609a74396`
and its compiled JAR to
`d2051d5d5eb38aeda3dfc5c1d61d11ebf2e18a1fb3222ac46c12863556c5a782`.
Two independent pinned-JDK builds in the baseline/control runner tests produced
that same JAR hash. Reproduce with `uv run --no-sync pytest -q
tests/item10/test_collection_runner.py`; the existing runner contains the exact
compiler, manifest and deterministic JAR timestamp commands. Both hashes are
checked before a full server launch. Failed builds retain their rejection report.
These pins establish collector identity, not empirical placement counts.

Full analyses must pass `--require-complete-observer` to the existing census CLI.
The corresponding `collection_attempts(require_complete_observer=True)` gate
originally required exactly the 50 targeted incoming classes, their archived
bytes and matching installation events, complete attempt pairing and healthy
shutdown. The coverage correction below supersedes only the all-classes-loaded
requirement; the original mountainous rejection remains recorded.
`FULL_COLLECTION_CLASSES` in `tools/validate_item10_trace.py` reuses the existing
Extras-era class inventory and adds Scarecrow, four End island classes, two
procedural pillar classes and BCLib's `BlocksHelper`. This matches the pinned
collector's `premain` transformation predicate. Incoming hashes remain recorded
per actual runtime transformation; packaged bytes are not substituted for
loader-transformed input. Missing installations reject complete coverage, even
when the remaining trace is structurally valid. No positive placement is required
for each class or family, and no failed hook is interpreted as zero density.

#### Coverage correction `item10-observer-coverage-v2`

The [mountainous class-loading investigation](full-mountainous-r1-baseline/README.md#bounded-class-loading-check)
reproduces that the exact frozen observer does not load unused target classes.
Requiring an unused class to load therefore imposed an unintended positive-route
condition on the fixed sample. Starting with the preserved fifth world, accept
either all 50 captures or the same set minus only `BetterEndGatewayFeature`.
This narrow exception is supported by the existing conditional caller and JVM
fixture. Other missing targets still reject pending specific evidence.

Full analysis now requires the archive manifest to bind the frozen `probe.jar`
and hashes the actual nonsymlink JAR against its pin. An absent gateway must have
neither an incoming class file nor an installation event. Every supplied capture
still needs its hash and matching installation; any gateway attempt without an
installation, installation failure, incomplete attempt or unhealthy shutdown
rejects. Record captured and uncaptured targets in `observer_coverage`.

With the pinned transformer's exhaustive target predicate, healthy complete trace
and preserved archive, gateway absence is interpreted as an unexercised target,
not a failed hook. This is an inference from the verified observer behavior, not
a retrospective JVM class-load measurement in the world. It does not establish
absence of gateways outside the sampled generation or from other mechanisms.
Sampling, runtime, configuration, observer source/JAR and location acceptance are
unchanged. The first four all-50-class results retain their original acceptance;
no world regeneration or new archive revision is required by this reader change.

Provider metadata is also checked before an attempt reaches location processing.
Island context, urn parents and YUNG configured-feature markers must be present
for their respective providers; provider-specific metadata cannot move between
families, and boolean versus void completion must match the instrumented method.
The regression reproduced three prior false acceptances: removing a gateway's
feature marker, relabeling it Scarecrow, or replacing its boolean completion with
a void completion. All are now rejected. Retained diagnostic raw traces remain
unchanged and usable without claiming the complete 50-class observer.
The focused check is `uv run --no-sync pytest -q
tests/item10/test_collection_trace.py tests/item10/test_saved_content.py
tests/item10/test_density_census.py` (45 passed). Full-frame saved-content and
denominator acceptance, uncertainty and durable custody still apply separately.

Decode every selected Anvil slot with the existing Item 7 decoder after correlated
save-flush and clean exit. Require stored coordinates equal slot coordinates and
status exactly `minecraft:full`. A missing, malformed or incomplete selected slot
invalidates that stage's complete-census claim; report it, retain it and diagnose
before retrying. Generated halo chunks are retained but outside the denominator.

Registry occurrences are unique non-INVALID starts keyed by dimension, structure
ID and authoritative start chunk, joined to the accepted 448-family inventory.
References, pieces and templates are not extra occurrences. Assign inclusion by
the start chunk, including starts whose bounding boxes cross the rectangle.
Retain start position and bounds for analysis. Unmapped IDs are errors, not drops.

The 40 nonregistry families require successful generator or lifecycle occurrence
records with dimension, anchor, selected design where applicable, and a stable
event identity. The existing inventory supplies contribution-to-family mappings.
Record attempted, failed and successful placement separately; a Boolean feature
return alone must not be assumed to equal one location without checking that
provider's existing writer evidence. Nested delegated writes must not duplicate
their parent location. Lifecycle-triggered End arrival and dragon/gateway events
must be reported separately from ordinary terrain-generated density. This is a
route distinction, not a blanket exclusion of those families: their packaged
chunk-generation routes remain in scope as specified below.

No current generic start counter satisfies that nonregistry requirement. Before
implementation, select direct tracing or prove a saved-world reconstruction for
each mechanism using existing provider evidence. Any tracing instrument must
have a recorded hash and pass the collector validation below. The original
whole-world equality requirement failed in diagnostic r3 and is superseded for
future validation because Item 7 already demonstrates semantic nondeterminism.
Do not claim whole-world noninterference or uninstrumented counterfactual density.
Do not claim all-family coverage until every applicable writer is observable.

Report structures, actionable candidates, provisional encounter sites, exclusive
T2 proper dungeons, exclusive T3 major expeditions, T4 objectives and villages with explicit numerators over the same
selected full-chunk denominator. Preserve the provisional classification's
confidence and ambiguity. Static hostility is a separate descriptor and never
the observed-combat numerator.

### Existing nonregistry mechanism coverage to integrate

Reuse `non_registry_content.contributions` in the accepted Item 8 inventory.
The following is a measurement-method grouping of its existing 40 canonical
families, not a new inventory or classification. Source mechanisms are available;
occurrence collection beyond the scarecrow diagnostic is still missing.

| Existing contribution | Canonical families | Existing mechanism relevant to collection |
| --- | ---: | --- |
| `betterend:biome_buildings` | 6 | Selected complete building templates. |
| `betterend:biome_ruins` | 10 | Selected complete ruin templates. |
| `betterend:crashed_ship` | 1 | Configured feature with template placement and erosion. |
| `betterend:ruined_obsidian_pillar` | 1 | Two direct procedural writers. |
| `betterendisland:platform_gateway` | 3 | Conditional End feature/lifecycle routes; preserve route-specific applicability. |
| `biomesoplenty:anomaly` | 1 | Direct anomaly-block construction. |
| `biomesoplenty:monolith` | 1 | Direct obsidian construction. |
| `explorations:scarecrow` | 1 | Five direct writes; bounded r3 capture corroborated. |
| `quark:fairy_ring` | 1 | Zeta generator with delegated flower placement and buried ore. |
| `quark:monster_box` | 1 | Zeta generator placing an encounter block. |
| `quark:nether_obsidian_spike` | 1 | Zeta direct procedural generator. |
| `quark:spiral_spire` | 1 | Zeta direct procedural generator. |
| `supplementaries:cave_urn_cache` | 1 | Random patch delegates urn placements; patch and block counts differ. |
| `yungsbridges:bridges` | 1 | Multiple-attempt random selection of inline bridge features. |
| `yungsextras:feature_entrypoints` | 10 | Configured feature/template entrypoints for canonical designs. |

The existing evidence supplies family mappings and nested delegation distinctions.
Choose hooks or saved-world reconstruction from those records following the
clean, merged PR23 diagnostic; do not audit providers again or count each delegated write as a site.

Existing BetterEnd code establishes three concrete constraints for that extension:

- In the retained [NBTFeature disassembly](../item-8/sources/betterend-entry-template-consumers/BetterEnd-21.0.31.jar/org.betterx.betterend.world.features.NBTFeature.txt),
  `place` discards `StructureTemplate.placeInWorld`'s result at bytecode offsets
  259/262 and returns true at 657/658. The retained
  [CrashedShipFeature](../item-8/sources/betterend-feature-scope/BetterEnd-21.0.31.jar/org.betterx.betterend.world.features.CrashedShipFeature.txt)
  does the same at 250/253 and 311/312, with erosion between those points.
  Neither outer success value proves a placed location.
- The retained [StructureTemplate disassembly](../item-8/sources/missing-template-code/server-1.21.1-20240808.144430-srg.jar/net.minecraft.world.level.levelgen.structure.templatesystem.StructureTemplate.txt)
  skips blocks outside the clipping box at 250/256, branches past refused content
  writes at 351/356, and still returns true at 1151/1152. Template success alone
  also cannot supply a nonempty occurrence. Preserve successful content writes
  separately from temporary barrier writes, terrain merge and erosion. Empty or
  fully refused placements must remain distinguishable from observed sites.
- `BuildingListFeature` stores its selection in a mutable field. The retained
  [StructureInfo](../item-8/sources/betterend-entry-template-consumers/BetterEnd-21.0.31.jar/org.betterx.betterend.world.features.BuildingListFeature$StructureInfo.txt)
  instead exposes a final `structurePath` and the actual returned template at
  `getStructure` offsets 18 through 22. Attribution must bind the template used
  by the placement to its selected path, rather than reread the feature's mutable
  selection later. This is an attribution constraint, not a diagnosis of the
  already observed baseline nondeterminism.

These are direct derivations from accepted Item 8 code evidence, not additional
measurements or accepted nonregistry counts. The next collector validation must
exercise these failure paths before BetterEnd occurrences enter density numerators.

## Collector validation under established baseline variability

This is a prospective correction to an inappropriate instrument-validation
criterion, not a passing reinterpretation of r3. Its predeclared equality gate
remains FAILED and all mismatches remain retained in
[the diagnostic](placement-probe.md). The accepted Item 7 result already showed
that even unchanged fresh runs differ semantically; another Item 7 repeat would
not resolve the instrument's causal effect. No frozen configuration is changed.

Separate collector correctness from world-generation reproducibility:

- Bind each hook to exact retained class identity and declared call sites. Verify
  original arguments, invocation counts, returned values and exceptions are
  preserved by the transformation, with actual retained-class transformation
  and focused executable preservation checks. Do not consume game random values.
- Require complete installation, event and shutdown evidence. Report refused
  writes, exceptions, unfinished attempts and observation failures separately;
  none can disappear into a zero occurrence count.
- Corroborate representative recorded coordinates against the retained world.
  This tests that the collector observed the claimed writer/location, not that
  its timing has no effect on other generation. Retain state differences caused
  by later updates rather than treating logged input state as final world state.
- Describe results as placements observed under the exact frozen gameplay
  configuration plus the recorded measurement overlay. Observer-free equivalence
  and causal attribution of between-run differences remain unproven, consistently
  with the accepted Item 7 Chunky-control limitation.

The full sampling design must include independent fresh repetitions to retain
already established run-to-run variability; deterministic reprocessing of one
world is a separate check. Before collection, update its runtime/storage budget
and freeze the repetition count and ordering. No new repetition is authorized by
this paragraph solely to re-establish Item 7's known nondeterminism. Neither the
six scarecrow attempts nor a passed collector fixture supplies 40-family coverage.

## Spatial summaries and uncertainty

Use horizontal Euclidean distance between authoritative start-chunk centers
`(16 * ChunkX + 8, 16 * ChunkZ + 8)`, in blocks, within each seed and
dimension/stratum. This is a declared chunk-based placement distance, not a
measured entrance, bounding-box gap or walking distance.
Report nearest-neighbor distances by category. A target's nearest observed
neighbor is exact only when that distance is no greater than its distance to the
sampling boundary; otherwise retain it as boundary-censored. Do not calculate an
uncensored mean by silently dropping those cases. Zero or one observed member
does not have an estimable nearest-neighbor mean. Report the finite-window
nearest-observed mean separately from the uncensored nearest-neighbor mean;
the latter remains null if any member is boundary-censored. Preserve each
observed distance and its lower bound rather than dropping censored cases.

Partition each rectangle into globally aligned 16 by 16 chunk cells. Preserve
partial boundary cells with their actual denominators. Only completely sampled
cells enter equal-area dispersion and largest-empty-rectangle calculations. Use
population variance divided by the mean, or null when the mean is zero. Report count
distributions and variance/mean by category as a descriptive clustering measure.
Report all zero-count cells and the largest axis-aligned rectangle of zero cells
fully inside the sample, resolving equal-area ties lexicographically by bounds.
This measures emptiness at 256-block resolution, not the exact largest empty disk.

For biome comparisons, retain the biome at every occurrence anchor and count
selected chunk-center biomes at every stored quart-height, reporting height bands
separately. Do not divide underground starts by an unrelated surface-only biome
denominator. Sparse biome/category cells remain visible, with raw denominators.

For registry starts, predeclare the biome anchor as the authoritative start chunk's
center X/Z and floor((minimum piece Y + maximum piece Y) / 2). Retain every
stored piece bound and their union envelope. This is a geometric attribution
proxy, not an entrance or Minecraft's placement-time biome predicate. Use the
anchor's floor(Y/4) band for its biome denominator. Missing bounds and anchors
outside stored biome height remain explicit unavailable observations, never
surface substitutions or silent drops. Inverted piece bounds reject attribution.
Nonregistry writer coordinates will supply their own recorded anchors.
The same `chunk_biome_column` reader accepts an explicit block X/Z anchor for
nonregistry attribution. It verifies that the integer coordinates belong to the
supplied chunk and reads their actual horizontal quart, including negative world
coordinates. Omitting the anchor preserves the registry chunk-center convention
and existing height-band exposure. This does not change biome denominators or
substitute a center biome when a traced anchor is unavailable. The integrated
`--biomes` path now joins these values and quart heights into observed nonregistry
classification rows. Arena location Y remains unavailable rather than selecting
a component height. The saved-content/biome/census integration passes 30 tests,
including all seven retained cache anchors. The earlier focused biome/spatial/census
suite passes 40 tests; Ruff and test-file basedpyright checks pass.
The existing `--biomes` reader now implements this registry attribution alongside
height-band exposure. Focused Item 10 validation passes 29 tests, including
negative heights, missing bounds, out-of-height attribution and inverted bounds;
Ruff and the changed test's type check pass. The retained r3 control integrates attribution for all 64 registry starts
without gaps, as linked in the placement diagnostic. This does not alter the
generation-equivalence projection.

Report per-seed and per-stratum results first. These four deliberately selected
seeds and origin-centered regions are not a random sample of all Minecraft worlds.
Report finite-area counts exactly and cross-seed range descriptively. Do not call
deterministic repeat agreement a confidence interval. Categories with fewer than
30 occurrences remain sparse; absent observations are not proof of impossibility.

## Resource and delivery bounds

### Sparse Structures control contrast

Use the complete frozen baseline against an explicitly labeled control whose
only candidate-manifest change is omission of
`sparsestructures-neoforge-1.21.1-3.0.jar` (SHA-256
`5aca0b33c0c83154810bbdd8ddc0d3e6a3e4591577274e2d27c10de0b45f2a45`).
The baseline remains 136 candidates, or 137 with the declared Chunky overlay;
the control has 135, or 136 with that same overlay. Preserve every configuration
file unchanged, including the now-unused Sparse Structures configuration. Use
the same collector, seed, selected regions, generation commands and lifecycle
contract in both arms. Produce the exact derived control manifest before launch.

The derived [135-candidate control manifest](control-server-candidates.txt) has
SHA-256 `a598513faef1248fd4a41da9137c1c721f9d34d307d12166141010bf815a20b4`.
It preserves the frozen baseline manifest order and omits exactly the one JAR
above. The shared `prepare_worldgen` path first materializes and verifies all
136 frozen candidates, then unlinks only that JAR in the fresh control instance
when `WorldgenRequest(mode="item10", omit_sparse_structures=True)` is requested.
Item 7 modes reject that option. Configuration materialization is identical.
The original source JAR and baseline instance remain untouched.

Direct SHA-256 and size verification of the retained acquisition artifacts on
2026-09-08 gives the baseline plus Chunky identity
`e2dab4c80cff137d747bd035588882797f85fa8d4d5b6ccb98a5d717fa0749c8`
and control plus Chunky identity
`84a884f99e4ac48defb9ea0b2c9e45bf3d0f4f6e881a4be4d8968dc2be14d4da`.
Derivation: select the filenames from each candidate manifest plus the pinned
Chunky filename, verify their bytes against Item 3's acquisition manifest, sort
`(filename, SHA-256)` pairs by filename, serialize with Python
`json.dumps(rows, separators=(",", ":"))`, and hash its UTF-8 bytes. This is the
existing runtime `_hash_rows` convention. The preflight receipt retains the
136-candidate source identity and explicitly records the omission, actual
deployed count and deployed hash. Collector JAR identity is recorded separately.
These are verified input identities, not a claim that the control has booted.

Validation: `uv run --no-sync pytest -q tests/item10/test_sparse_control.py
tests/item10/test_full_selections.py tests/item7/test_worldgen_preflight.py
tests/item7/test_worldgen_lifecycle.py`. Tests cover exact omission, preservation
of source and baseline JARs, byte-identical configurations, receipt consistency,
rejection of nonfrozen runtime input, and unchanged Item 7 lifecycle behavior.

This contrast measures removal of Sparse Structures within the retained stack,
not a spacing-only effect or a recommended configuration change. The accepted
[MakeStructuresSparse code](../item-8/sources/sparsestructures-provider/sparsestructures-neoforge-1.21.1-3.0.jar/io.github.maxencedc.sparsestructures.mixin.MakeStructuresSparse.txt)
changes spacing/separation and, independently at bytecode 205 through 235,
conditionally replaces the placement salt. Factor 1 alone is therefore not the
chosen control. Direct inspection of all `candidates[].dependencies` in
[Item 3's retained inspection source](../item-3/jar-inspection.json) finds no
dependency with `mod_id == "sparsestructures"`; this supports attempting the
control, but does not replace its runtime validation.

Both arms require fresh independent repetitions. Retain per-run counts and
within-arm variation alongside between-arm differences; do not infer that each
individual changed location was caused by the omitted mod. Generation order,
repetition count, sample size and combined resource budget must be frozen before
collection. This resolves the control contrast, not the remaining sampling gate.

### Runtime and storage estimate

The r3 uninstrumented mountainous diagnostic supplies a measured planning proxy:
366.501 seconds for 6,852 selected chunks and 137,748,133 retained world bytes,
including halo and lifecycle data. Linear scaling to 743,600 requested generation
chunks gives about 11.05 generation hours and 13.92 GiB of uncompressed world data
across both arms and repetitions, before archives, derived output and restore
workspace. Each 46,475-requested-chunk world has a proxy of 41.43 minutes and
0.870 GiB. The 720,896-chunk census and 16-world design are unchanged; these
updated proxies include the explicit generation edge. This single mixed-stratum run does
not predict custom dimensions or the farther outer End reliably. Offline
processing, collector overhead, installation and archiving are additional.
These are automated machine-time estimates, not a player workload.

Direct `df -B1 .` on 2026-09-08 reports 48,890,408,960 bytes available after the
authorized cleanup. The user's roughly 30 GiB working budget is retained.
Process one world at a
time, using the existing clean-save/archive/publish/download/restore path. Keep
at least 5 GiB available before starting a world as a provisional workspace floor.
The earlier floor allowed three world copies and four archive copies using the
r3 control compression ratio. It is provisional and excludes the full observer's
unmeasured output. Verify this against actual collector and first-world
storage before scaling.
The floor is not a disk quota or a guarantee based on the proxy. Archive without
`session.lock` and retain immutable raw custody and committed evidence references.
Release disposable measurement materializations only after verified custody and
within explicit authorization. Never remove operational player worlds, prior
backups or protected artifacts to satisfy this budget. A failed resource gate
stops collection before another world; it does not reduce the declared sample.

Complete the first full ordinary baseline world through deterministic analysis and retained evidence
before scaling across seeds and dimensions. Then integrate all final results,
uncertainty and failure dispositions into the Item 10 report. The final gate
still requires full automated occurrence coverage, Sparse Structures attribution, clean Codex PR
review, merged main delivery and the subsequent Items 2 through 10 consistency
audit. Neither this protocol nor a completed static subset closes Item 10.

## Frozen diagnostic pilot r1

Declared before launch on 2026-09-08. Purpose: exercise the new registry counter
against a fresh frozen-runtime world through the existing generation, correlated
flush and clean-stop path. This is a method diagnostic, not acceptance of the
remaining full-coverage requirements or the full Item 10 sampling frame.

Use ordinary seed 42 and the hash-verified Item 7 `run` preset. Its unchanged
four selections generate 3,969 Overworld chunks plus 961 chunks each in Nether,
central End and outer End. Retaining this existing preset avoids changing its
validated selection/lifecycle contract solely for a diagnostic. It does not repeat
an Item 7 audit or reuse an old proof world. All generated bytes remain raw inputs.

The declared census is only Overworld chunks x=-31 through 31 and z=-31 through
31, inclusive: exactly 3,969 target chunks. No count-based stopping or selection
adjustment is permitted. Missing target chunks reject the complete-census claim;
retain the attempt before any corrective generation. Other selections and halo
chunks do not enter this denominator. Report the raw registry count only, with
its limitations, before canonical classification and other Item 10 integration.

Source command is the existing `tools.run_item7_worldgen run`, using the frozen
paths recorded in README, target `instances/item10/pilot-r1` and diagnostics in
`evidence/raw/item10/pilot-r1`. Use a 900-second generation/lifecycle deadline,
the pinned Temurin and 1 to 4 GiB heap. The existing preflight must pass before
launch. Current available RAM is 9.4 GiB and persistent free storage 14 GiB.
The Item 7 proxy predicts roughly 116 MiB of raw world data for 6,852 selected
chunks; reserve 4 GiB for instance, logs, archive and a restored copy. Neither
storage nor runtime estimate is an acceptance result.

After clean stop, run the counter once over the declared rectangle, retain its
output or failure, measure actual elapsed time and storage, then archive and
verify a restored copy with the existing custody tools before releasing any
materialization or scaling. No player participation or screen recording is used.

## BetterEnd runtime diagnostic r1

Predeclared before launch on 2026-09-08. Use the unchanged existing diagnostic
runner with `--name betterend-probe-r1 --mode probe --role mountainous` and the
Item 7 `run` selections: 3,969 Overworld chunks and 961 each in Nether, central
End and outer End (6,852 total). This tests the extension committed as `3594b2be`;
the diagnostic receipt records the exact launch revision and built agent hash.
It is not one of the full-frame sampling worlds or a repeat equality experiment.

The fresh materialization must pass the existing frozen-input preflight. Keep
the 900-second lifecycle timeout, 1 to 4 GiB heap, unchanged configurations and
correlated save-flush/clean-stop requirements. Current capacity is 8.8 GiB disk
and 9.2 GiB available RAM, with no Java process found. The prior same-seed r3
run took about six minutes and retained about 138 MB of world data. Reserve
1 GiB for this bounded diagnostic and custody as a planning allowance, with
additional trace cost measured from this run rather than assumed negligible.

Require installation records for all four new target classes, matching the
exact input class hashes in the existing Item 8 identities used by the fixture.
Any changed runtime class identity, installation failure, malformed or incomplete
trace, unsuccessful lifecycle or missing expected region coverage rejects the
runtime capture gate and remains retained. At least one paired BetterEnd template
attempt with successful content writes is required to proceed to saved-world
corroboration. Zero eligible attempts is INSUFFICIENT, not an accepted zero density.
Preserve empty, refused and exceptional attempts. Validate source-path attribution
against the existing canonical family mapping before accepting any occurrence.
No full-world equality or observer-free equivalence claim is required or implied.

```sh
uv run --no-sync python -m tools.run_item10_probe --name betterend-probe-r1 --mode probe --role mountainous
```

## BetterEnd incoming-class diagnostic r2

Predeclared before launch on 2026-09-08. Use `betterend-identity-r2`, probe mode,
mountainous seed and the existing `pilot` preset: 81 chunks in each of the same
four dimension/End strata, totaling 324 selected chunks. The runner now exposes
that existing validated preset; its default remains the larger `run` preset.
The only collector change from r1 is retention of incoming target class bytes.
Keep the same frozen runtime/configuration, lifecycle, heap and 900-second limit.

Purpose: retain and inspect the incoming Minecraft class that differed from its
packaged form in r1. Require the four new class files and their emitted SHA-256
identities, exact provider input identities, complete lifecycle, and no failed
installation. Compare the incoming Minecraft class against the packaged Item 8
class using the pinned JDK disassembler. Inspect the actual content-write call
site and every difference affecting that method before accepting a runtime hook
identity. The r1 observed Minecraft hash is a comparison input, not a substitute
for r2's own retained bytes. This is an identity diagnostic, not a density sample;
no minimum template-placement count is required to inspect the class.

Current disk headroom is 8.0 GiB. Keep the prior diagnostic's 1 GiB planning
allowance for raw outputs and custody; startup/halo costs prevent extrapolating
runtime or storage in direct proportion to the smaller selected area. Preserve
failures and archive/verify the stopped world through the existing tools.

```sh
uv run --no-sync python -m tools.run_item10_probe --name betterend-identity-r2 --mode probe --role mountainous --preset pilot
```

## BetterEnd positive-placement fixture r3

Predeclared before launch on 2026-09-08. Use fresh `betterend-fixture-r3`,
mountainous seed, probe mode and the existing 324-chunk pilot preset. After the
four generation selections, the runner sends exactly two recorded commands:

```text
execute in minecraft:the_end run fill 0 80 0 15 80 15 minecraft:end_stone
execute in minecraft:the_end run place feature betterend:blossoming_spires_structures 8 81 8
```

The first creates a small flat terrain fixture in an even-parity chunk; the
second exercises the registered building-list configuration identified in the
accepted Item 8 configured-feature registry. The normal feature implementation
still decides whether placement succeeds. No configuration, provider code or
predicate is bypassed. This intentionally altered world is permanently excluded
from density sampling and does not establish natural placement frequency.
Selection RNG is whatever the real command uses; retain its observed template
path rather than preselecting or rewriting the outcome.

The existing lifecycle now accepts an optional tuple of commands after generation
and before its unchanged correlated save-flush. Its default is empty. The fixture
flag is restricted to probe mode and the pilot preset; all commands enter the raw
receipt. Focused lifecycle/probe validation passes 17 tests, including command
ordering before flush; Ruff and changed Python type checks pass.

Require a successful platform command, a paired real template call with at least
one successful non-air content write, validated source-path attribution, complete
trace, inspected retained incoming classes, and saved-world corroboration. Record
refusals, exceptions and later state differences. A successful server lifecycle
or outer feature result alone does not pass this gate. Use the frozen preflight,
1 to 4 GiB heap, 900-second timeout and the previous small pilot's 1 GiB custody
planning allowance; recheck host capacity before launch.

```sh
uv run --no-sync python -m tools.run_item10_probe --name betterend-fixture-r3 --mode probe --role mountainous --preset pilot --betterend-fixture
```


## BetterEnd loaded placement fixture r4

Predeclared before launch. Repeat the r3 diagnostic in fresh
`betterend-fixture-r4`, with its same seed, pilot selections, heap, timeouts and
positive-placement gate. Correct only the demonstrated unloaded-target defect:
after readiness and before the first generation selection, send
`execute in minecraft:the_end run forceload add -32 -32 47 47`.
This requests 25 central End chunks around the fixture, leaving the four generation
selections before the two original placement commands. Require the loading command
and both fixture commands to succeed; asynchronous loading is not assumed complete
merely because a ticket was requested. Any refusal still rejects the fixture.
The retained ticket and artificial platform make this a diagnostic world only.
Neither changes the frozen configuration or supplies density observations.

The existing lifecycle receives an optional empty-by-default command tuple before
generation, using its existing send/error path and command receipt. This narrow
addition fixes the reproduced r3 precondition failure; no new runner is introduced.
The focused lifecycle and probe suite passes 23 tests, including command order
with empty and nonempty setup/fixture tuples. Changed Python type checks pass.
The host check before launch found 7.5 GiB free and no Java server process;
retain the 1 GiB diagnostic custody allowance.

```sh
uv run --no-sync python -m tools.run_item10_probe --name betterend-fixture-r4 --mode probe --role mountainous --preset pilot --betterend-fixture
```


## BetterEnd ground diagnostic r5

Predeclared before launch. Fresh `betterend-ground-r5` repeats the r4 fixture,
including loading, with one observer addition: duplicate and record the actual
position returned by NBTFeature.getGround at its single call site. The original
reference remains on the operand stack. No extra world query, predicate call or
RNG draw is made. Strict transformation requires exactly one matching call.
This fixes the missing observation that prevents diagnosing r4, whose saved chunk
retains WORLD_SURFACE but not WORLD_SURFACE_WG. Do not substitute the former for
the latter. The new ground row is diagnostic evidence, not a location occurrence.
The existing probe fixtures check its coordinates and attempt linkage in normal,
isolated-loader and failure modes, and retain vanilla/observed argument equality.

Use the same 324 selected chunks, seed, frozen runtime/configuration, 1 to 4 GiB
heap, 900-second timeout and 1 GiB custody allowance. Retain rejection if no
positive template placement occurs. Compare the observed ground with immutable
saved blocks to narrow the failed predicate, disclosing possible later changes.

```sh
uv run --no-sync python -m tools.run_item10_probe --name betterend-ground-r5 --mode probe --role mountainous --preset pilot --betterend-fixture
```


## BetterEnd tag diagnostic r6

Predeclared before launch. Fresh `betterend-tags-r6` repeats r5 with four
read-only command checks between platform fill and feature placement: both
`if` and `unless` checks for air at `[8,81,8]` and for
`#wover:surfaces/terrain` at `[8,80,8]`. Each successful branch emits its unique
`item10-fixture-air-true/false` or `item10-fixture-terrain-true/false` marker.
Require exactly one of each pair; syntax errors, unknown tags or missing output
are not false-membership evidence. Retain full commands and raw responses.

The resource identifier derives from CommonBlockTags.TERRAIN's
`surfaces/terrain` path, TagRegistryImpl.makeWorldWeaverTag, LibWoverTag's `wover`
namespace and ModCore.mk in retained worldweaver-21.0.24.jar. Its BlockTagProvider
prepareBlockTags adds end stone to END_STONES and includes that tag optionally
in TERRAIN. This packaged intent is not runtime membership proof. No tags or
configuration will be modified if runtime behavior disagrees.

Use the same frozen identity, 324-chunk pilot, seed, heap, 900-second deadline
and 1 GiB custody allowance. This run resolves the predicate discrepancy; it
remains excluded from density samples even if placement succeeds.

```sh
uv run --no-sync python -m tools.run_item10_probe --name betterend-tags-r6 --mode probe --role mountainous --preset pilot --betterend-fixture
```


## BOP direct-write fixture r1

Predeclared before launch. Use fresh `bop-fixture-r1`, mountainous seed, existing
324-chunk pilot, pinned runtime/configuration and the probe overlay. Request the
same 25 central End chunks to stay loaded before generation. After all selections,
fill `[0,80,0]` through `[15,80,15]` with vanilla end stone and `[32,80,0]` through
`[47,80,15]` with BOP unmapped end stone. Place configured `biomesoplenty:anomaly`
at `[8,81,8]`, then `biomesoplenty:monolith` at `[36,81,8]`.
The accepted configured-feature registry contains both IDs. The Item 8 source
predicates permit end stone/unmapped end stone for anomaly and require unmapped
end stone for monolith. The commands supply substrate, not predicate bypasses.
This altered world is excluded permanently from density samples.

Require all fixture commands to succeed, paired feature attempts, retained and
inspected incoming helper identity, actual non-air successful writes for both
features, and saved-world corroboration before accepting capture. Preserve flags
3 helper writes separately from anomaly's direct flags-2 writes, failed writes,
exceptions, unfinished attempts and later state changes. The anomaly's downward
construction may attempt out-of-height writes; do not silently omit refusals.
Count one feature location per successful attempt, never each written block.

Use the existing 1 to 4 GiB heap and 900-second lifecycle timeout. Prior small
fixtures took approximately 90 seconds; this is a planning proxy, not a promised
runtime. Keep the 1 GiB custody allowance, measure actual trace/storage/runtime
cost, and stop before full sampling if the allowance is inadequate. The current
host has 6.8 GiB free; recheck for Java processes before launch.
The direct-write fixture and BetterEnd fixture flags are mutually exclusive and
require probe/pilot mode. Existing default commands remain empty.

```sh
uv run --no-sync python -m tools.run_item10_probe --name bop-fixture-r1 --mode probe --role mountainous --preset pilot --bop-fixture
```


## Monster Box natural pilot r1

Predeclared before launch. Use fresh `monster-box-pilot-r1`, ordinary seed 42,
the unchanged 324-chunk pilot (81 chunks each in Overworld, Nether, central End
and outer End), frozen Item 6 configuration and the current recorded probe
source. Use no forced placements, terrain commands or configuration changes.
This run checks runtime capture, not representative density. Preserve all
attempts, including void returns without writes; a generator_end is completion
only. Count successful monster-box writes separately from attempts and other
feature classes. Snapshot the actual write coordinates before mutable positions
can move. Retain incoming classes, failures and the complete raw trace.

Acceptance requires installation of the exact incoming MonsterBoxGenerator hook,
paired generator attempts with actual write results, correlated save and clean
shutdown, durable raw custody and saved-block corroboration. Zero successful
writes are an insufficient positive diagnostic, not proof of zero density; do
not adapt the area or seed based on counts. Other family hooks retain their
existing scope. Full sampling remains gated on complete occurrence coverage.

Use the existing 1 to 4 GiB heap and 900-second lifecycle timeout. Previous
324-chunk diagnostics took approximately 90 seconds. Reserve 1 GiB for this
pilot and custody; available storage was 6.3 GiB before declaration. No Java
server was running. These are resource allowances and planning proxies, not
measured costs for this new collector. Record actual time and trace/archive sizes.

```sh
uv run --no-sync python -m tools.run_item10_probe --name monster-box-pilot-r1 --mode probe --role ordinary --preset pilot
```


## Nether spike natural pilot r1

Predeclared before launch. Use fresh `nether-spike-pilot-r1`, ordinary seed 42,
and the existing unchanged 324-chunk pilot with frozen runtime/configuration and
the current source-bound observer. No commands alter terrain, force placements
or change settings. The accepted frozen settings remain chancePerChunk 0.1,
triesPerChunk 4, bigSpikeChance 0.03 and bigSpikeSpawners true.

The new observed attempt is one static placeSpikeAt invocation, not an outer
generateChunk call and not an individual block. Outer calls failing the chance
or lava search are outside this event population. Preserve the placement anchor,
individual write results, zero-write returns and exceptions. Keep other feature
classes in the raw trace. Require incoming class identity, complete lifecycle,
positive spike writes, durable custody and saved-block corroboration before
accepting this diagnostic. Unexercised conditional large-spike/reward paths stay
explicit; successful block capture does not prove their gameplay behavior.

Use the existing 1 to 4 GiB heap and 900-second timeout. The previous same-sized
ordinary pilot took 88.452 seconds, a planning proxy only. Reserve 1 GiB for raw
outputs and custody; the host has 6.0 GiB free and no running Java server before
launch. Measure actual time and sizes. Do not expand or change seed in response
to counts. Zero successful writes are insufficient positive capture, not a zero
density result. This diagnostic cannot substitute for the full sampling frame.

```sh
uv run --no-sync python -m tools.run_item10_probe --name nether-spike-pilot-r1 --mode probe --role ordinary --preset pilot
```

## Spiral spire capture decision before implementation

A makeSpike call is a chunk contribution, not the canonical source occurrence.
The retained Zeta MultiChunkFeatureGenerator.generateChunk loops over source
chunks, obtains getSourcesInChunk at offset 201, and passes each source as
generateChunkPart argument 1 at offset 237. Argument 4 is the destination chunk
anchor. The retained SpiralSpireGenerator then delegates eligible contributions
to makeSpike at offset 133. Capturing only makeSpike would lose the shared source
and could inflate a single multi-chunk site into several counted locations.

Use generateChunkPart as the attempt boundary, retaining both source and target
chunk anchors. Capture its delegated makeSpike writes without creating nested
occurrences. Group successful contributions by run, dimension, canonical family
and source anchor, while retaining each attempt and refused/zero-write outcome.
Assign density inclusion by the source chunk, and retain boundary-censored
contributions separately. Multiple successful chunks must not multiply the
source numerator. This decision does not accept any occurrence counts.

Before a live pilot, fixtures must prove two target chunks sharing one source
remain distinct raw attempts with one processing key, distinct sources remain
distinct, early returns and refused writes remain present, and the original
write arguments/results/exceptions survive. Direct makeSpike calls outside the
outer attempt must retain their original behavior and must not be mislabeled
as complete source observations. Extend existing collector/tests only.

Reproduce the Zeta derivation with pinned javap -p -c, classpath
downloads/item3/candidates/Zeta-1.1-40.jar, class
org.violetmoon.zeta.world.generator.multichunk.MultiChunkFeatureGenerator.
Archive SHA-256: 4f17d1a2b9fd6d18ddb7697aa451db7fb154053b8648f79de279ae0d7e68a2fa.
Class SHA-256: 3ed69dd1642e62c29d55ffa015e90c885e5d0f217887bdd4565b90b80ffc7e4b.
Reuse the accepted Item 8 Quark end-generator source evidence for the consumer.
No experiment, configuration tuning or inventory reclassification occurred.

## Spiral natural pilot r1

Predeclared before launch: fresh spiral-pilot-r1, ordinary seed 42, unchanged
324-chunk pilot (81 selected chunks in each of four strata), frozen runtime and
configuration, collector source committed with this declaration. No terrain,
placement or tuning commands. Preserve all source/part attempts and other
feature events, including failures and zero writes. Require a complete lifecycle,
incoming class identities, positive spiral writes and saved-block corroboration
before positive capture acceptance. A zero-result run is retained as insufficient
coverage, not a density estimate, and will not trigger seed/area expansion.

Use existing 1 to 4 GiB heap and 900-second lifecycle timeout. The same-sized
Nether pilot took 88.346 seconds, only a planning proxy. The host has 5.7 GiB
free; reserve 1 GiB for this bounded pilot and its archive/restore custody. Check
for running Java before launch. Record actual elapsed time and sizes. Full
collection remains gated on remaining coverage and measured observer costs.

```sh
uv run --no-sync python -m tools.run_item10_probe --name spiral-pilot-r1 --mode probe --role ordinary --preset pilot
```

## Fairy-ring capture boundary

Use the retained spawnFairyRing invocation as one attempted source location.
Its four direct write sites include flower removal, surface copies, ore center
and ore neighbors. Record each result, but cleanup-only successful writes are
not a constructed location. Retain a separate delegated flower observation:
requested origin, actual return and the post-call block state at that origin.
The caller requires empty space before this call and rereads that same position
afterward; the delegated return alone does not establish visible content.

The accepted Item 8 landmark generator source identifies direct setBlock sites
at offsets 193, 315, 457 and 510, the delegated PlacedFeature.place at 292 and
the post-call state read at 299. Keep surface, reward and cleanup outcomes
distinct in processing; a partial or invisible ring remains partial, not a
complete visible landmark. Do not count a deposit and its ring as two families.
This bounded capture does not enumerate the delegated flower feature's entire
footprint. It establishes origin content and direct generator contributions,
not that every nested decoration block was observed.

Before a live pilot, preserve ordinary calls/results/exceptions under normal,
refused, zero-write and isolated-loader fixtures, including a delegated false
return that leaves non-air and a true return that leaves air. Neither boolean
may be substituted for the observed origin state. No sample or positive
occurrence count is accepted by this method declaration.

## Fairy natural diagnostic r1

Predeclared before launch: fresh fairy-run-r1, ordinary seed 42, the existing
RUN_SELECTIONS frame of 6,852 chunks (3,969 Overworld and 961 each Nether,
central End and outer End). This reuses the earlier scarecrow diagnostic frame
rather than adapting the area to fairy counts. Frozen forest/plains chances
remain 0.00625/0.0025, with the accepted ore list and Overworld allowlist.
No placement commands, terrain edits or configuration changes.

Preserve every attempt, direct writer role, actual write result, delegated flower
return/exception and caller-read origin state. Require positive non-cleanup
content, all incoming class identities, complete lifecycle, raw custody and
saved-world corroboration before positive capture acceptance. Cleanup-only,
zero-result or failed runs remain insufficient and will not trigger automatic
seed/area changes. Other captured generator events stay in the trace.

The previous same-frame ordinary control took 366.501 seconds, a planning proxy
only. Use the existing 1 to 4 GiB heap and 900-second timeout. Before launch the
host has 5.5 GiB free and no Java process. Reserve 1.5 GiB for instance/world,
raw outputs, archive and restored custody; measure actual costs. This diagnostic
is not the full density sample and cannot close Item 10.

```sh
uv run --no-sync python -m tools.run_item10_probe --name fairy-run-r1 --mode probe --role ordinary --preset run
```

## Cave urn occurrence boundary

Reuse the accepted contribution `supplementaries:cave_urn_cache` in
[Item 8 inventory](../item-8/inventory.json), its
[patch geometry identity](../item-8/sources/urn-patch-geometry/identities.json)
and the [galleon reuse assessment](../item-8/sources/supplementaries-generation/README.md).
The nine patch tries and six cave placement repetitions are different levels.
Neither individual urn blocks nor one outer chunk invocation is the cache count.

Direct inspection of the retained server archive resolves the missing write
semantics. Archive SHA-256 is
`26ca9c40d7e1681190b428583c38816852218e78df3f8bdb60a59a78503aec71`.
The following class paths are relative to `net/minecraft/world/level/levelgen/`:

| Class | SHA-256 | Relevant bytecode |
| --- | --- | --- |
| `placement/PlacedFeature.class` | `bb5076d73ed849bfb377ffe117575ab98a3cef8134c674de7b39a8eab62e1f9d` | `placeWithContext` applies placement modifiers before `forEach` at 96; `lambda$placeWithContext$4` invokes the configured feature at 12 for each resulting origin. |
| `feature/RandomPatchFeature.class` | `a1ade9f8d487ec9744034a3ce5e50b709733db26975614a8c24ff6fc5006bbff` | `place` delegates each candidate at 145 and increments a success counter at 151 from the delegated boolean. |
| `feature/SimpleBlockFeature.class` | `17907c21c8e522ac39fa9dcc838dd8f4afdcd7bcfc200480b14187b7a01875e2` | `place` invokes `WorldGenLevel.setBlock` with flags 2 at 90, discards its boolean at 95, and returns true at 96/97. |

Derivation: a patch return can be true despite a refused urn write. Therefore
record each actual write result within each post-modifier patch attempt, retaining
zero-write attempts and exceptions. Accept a successful patch only with successful
urn content writes and the required saved-content corroboration. Retain the exact
patch origin and parent placement identity. A `urns_patch` configured-feature key
alone cannot distinguish cave placement from the galleon's reused component.
Only a verified `supplementaries:cave_urns` calling placement belongs to the
standalone cave-cache population; retain excluded component context separately.
Retain distinct attempt IDs when origins coincide and expose overlapping written
positions. Do not infer distinct locations from repeated writes to one block;
the final overlap disposition remains part of occurrence acceptance.

The next implementation should extend the existing probe at the placed-feature
context, patch-attempt and direct-write boundaries. Preserve nested context through
normal and exceptional exits, exclude unrelated patches and galleon reuse, and
verify runtime registry identity rather than relying on Java class names or
configured-feature text. These are required observation boundaries, not completed
collector coverage. No urn density has been measured. Validate retained incoming
class identity and original call/result preservation before a controlled run.

Reproduce the direct inspection with the pinned Temurin `javap -c -p`, using
`instances/pristine-baseline-v0/libraries/net/minecraft/server/1.21.1-20240808.144430/server-1.21.1-20240808.144430-srg.jar`
as the classpath and the three fully qualified classes above. Verify archive and
class hashes before relying on offsets; runtime transformation can change bytes.
No new server run, archive or validator was needed for this source-derived fact.

### Bounded urn diagnostic r1

Before collection, select one ordinary-seed (`42`) fresh `pilot` using the existing
four 81-chunk selections, 324 selected chunks total. Reuse the fixed centers
(0,0 for Overworld, Nether and central End; 1536,0 for outer End), radius four
chunks, and existing generation order. Do not expand the frame for positive
counts, command-place urns, change tags or tune configuration. This diagnostic
checks natural callback execution and identity, not density acceptance.

Use the collector implemented in `3a9453f5` and the run's exact source revision,
recorded by the existing harness. The retained baseline and frozen configuration
remain unchanged; the harness verifies fresh materialization, pinned Java and
artifact hashes and retains the agent source/JAR identity. Command:

```sh
uv run --no-sync python -m tools.run_item10_probe --name urn-pilot-r1 --mode probe --role ordinary --preset pilot
```

Prelaunch storage is 4.8 GiB free; no Java process is running. Reserve 1.5 GiB for
this bounded diagnostic and sequential archive/download/restore workspace. Prior
324-chunk diagnostics took approximately 89 seconds and compressed to about
6 MB; those are cost proxies, not a promised urn trace size. The harness timeout
is 900 seconds. The full experiment's separate 5 GiB workspace floor is not
satisfied and full collection is not authorized by this diagnostic.

Acceptance requires all selections, correlated save and clean exit, installed
hook identities, no unclosed attempts, and positive cave-parent urn writes whose
saved positions can be corroborated. Retain refused writes, non-cave/null-parent
contexts, exceptions, halo writes and zero-call outcomes. A missing positive path
fails that gate without implying zero density. Retain and publish raw observations
and incoming classes with the existing archive and restore tools even if the
positive gate fails. Do not start the full sampling frame on this result alone.

## YUNG bridge occurrence and writer boundary

Reuse `non_registry_content.contributions["yungsbridges:bridges"]` in the accepted
[Item 8 inventory](../item-8/inventory.json). Its generation record already
establishes first-success variant selection, sea-level anchoring, processor order
and the discarded template-placement boolean. Do not repeat that assessment or
count its 22 configured variants as separate families. Observe each attempted
BridgeFeature placement, retaining the selected configuration/template, actual
anchor, rotation, original return and exceptional completion.

The current template observer can supply the initial template-write boundary.
It must be extended through the subsequent custom processors before this family
has complete write coverage. Ending observation at placeInWorld would miss
material replacement, removal and support extension; a non-null template or true
BridgeFeature return alone is insufficient acceptance evidence.

The retained archive is `YungsBridges-1.21.1-NeoForge-5.1.1.jar`, SHA-256
`bf93a85422a6b457358c3b56352641a97ec09cc37dec18b2cedcac2bd1ff9bec`.
Archive and class bytes were checked against the existing
[processor identities](../item-8/sources/yungs-bridge-processors/identities.json).
Pinned `javap -c -p` direct inspection identifies these 37 direct
WorldGenLevel.setBlock call sites, using their original `(BlockPos, BlockState,
int)boolean` descriptor. Class names below are under
`com/yungnickyoung/minecraft/yungsbridges/world/processor/`:

| Class | Direct sites | Bytecode offsets |
| --- | ---: | --- |
| FenceBiomeProcessor | 4 | 188, 210, 294, 378 |
| ITemplateFeatureProcessor | 2 | 12, 75 |
| LanternRotProcessor | 3 | 64, 128, 192 |
| LogBiomeProcessor | 1 | 72 |
| OptionalBlockProcessor | 7 | 65, 129, 193, 257, 321, 404, 426 |
| OptionalSlabProcessor | 7 | 74, 147, 220, 293, 376, 398, 471 |
| OptionalStairProcessor | 4 | 74, 147, 220, 291 |
| OptionalWallProcessor | 1 | 64 |
| PlanksBiomeProcessor | 1 | 63 |
| SlabBiomeProcessor | 1 | 72 |
| StairBiomeProcessor | 1 | 72 |
| StoneVariationProcessor | 5 | 55, 128, 201, 274, 338 |

The inspected FeatureProcessorModule and DynamicLegProcessor have no direct
setBlock sites. Dynamic support writes use the shared interface helper already
listed. This is a count of bytecode sites, not executed writes or a claim about
all external effects. Reproduce with pinned `javap -c -p -classpath` against the
hash-verified archive and classes from the existing identity manifest.

Bind loaded template identity in AbstractTemplateFeature.createTemplateWithPlacement
before its placeInWorld call at 85. Its processor iteration occurs at 108, after
the discarded boolean at 88. These offsets refer to the class bound in the
[existing generator identities](../item-8/sources/yungs-bridge-generation/identities.json).
Retain phase attribution for template versus processor writes so later removal
cannot be mistaken for missing initial capture. Saved-content checks must compare
last successful writes and retain earlier observations. Count one accepted bridge
placement, not processors, support blocks or template attempts independently.

Implement within the existing probe and fixture path. Require original call,
argument, refusal and exception preservation; template-path/rotation attribution;
processor coverage including support and removal; no tracing outside the active
bridge attempt; and incoming class identities. Then predeclare a bounded runtime
diagnostic and its storage cost before launch. No bridge experiment or accepted
bridge occurrence measurement has been performed by this increment.

## Bridge r1 bounded natural diagnostic

Predeclared 2026-09-08 before launch. Use ordinary seed 42, the unchanged frozen
runtime/configuration and construction heap, and the existing pilot selections:
81 chunks each in Overworld, Nether, central End and outer End, 324 selected
chunks total. Outer End uses the existing center at (1536, 0); no selection is
chosen from observed bridge locations. Use a fresh hash-verified materialization.

```sh
uv run --no-sync python -m tools.run_item10_probe --name bridge-pilot-r1 --mode probe --role ordinary --preset pilot
```

The source revision is the commit containing this predeclaration. Retain the
incoming transformed classes, raw trace, lifecycle logs and stopped world using
the existing archive/download/restore path. This diagnostic tests natural bridge
capture, not selected-area density. Require complete selections, correlated flush,
clean exit, installed hook identities and no unfinished attempts. A positive
bridge result additionally requires configured variant, template/rotation and
complete template/processor write observations, followed by saved last-successful
block-ID corroboration. Retain all earlier writes, refused writes, zero-write
attempts, exceptions and halo coordinates. A missing positive path fails positive
capture without establishing zero density; do not expand the frame to hunt for it.

The prelaunch host check reports 4.2 GiB free and no running Java process. Reserve
1.5 GiB for this bounded diagnostic and sequential raw archive/download/restores.
Prior 324-chunk runs took about 89 seconds and produced about 6 MB compressed raw
archives; those are cost proxies, not a prediction of bridge output. The existing
900-second timeout remains. The provisional 5 GiB full-experiment workspace floor
is not met, so this declaration does not authorize full sampling. No baseline
configuration, bridge placement rule or Sparse Structures setting is changed.

## YUNG Extras occurrence and writer boundary

Reuse the accepted `yungsextras:feature_entrypoints` contribution in
[Item 8](../item-8/inventory.json), including its ten canonical families,
eleven configured feature types, template links and processor bindings. Do not
reclassify designs or count template variants as families. The existing records
already distinguish non-null template returns from successful block placement.

The exact archive is `YungsExtras-1.21.1-NeoForge-5.1.1.jar`, SHA-256
`0cd26474e514f5dc3114aaf5ec7e049bcd285f0c5db191bb45223193f35df70d`.
All 17 class records from the existing
[generator identities](../item-8/sources/yungs-extras-generators/identities.json)
and [desert/helper identities](../item-8/sources/yungs-extras-desert-code/identities.json)
were byte-verified against that archive before inspecting hook sites with pinned
`javap -c -p -classpath`. No replacement Item 8 source archive is needed.

Observe all eleven concrete feature entrypoints with configured key, original
origin and actual template anchor/pivot/rotation. Reuse the existing placement
callback for configured identity and template observer for write results.
AbstractNbtFeature has two placeInWorld sites: offset 87 in
createTemplateFromCenterWithPlacement, and offset 85 in
createTemplateFromCornerWithPlacement. In both, local 1 is the template resource
location. Their discarded results occur at 90 and 88, then processor iteration at
110 and 108 respectively. Retain both template and subsequent processor phases.

There are eleven direct WorldGenLevel.setBlock sites in the three bound processor
classes, under `com/yungnickyoung/minecraft/yungsextras/world/processor/`:

| Class | Sites | Bytecode offsets |
| --- | ---: | --- |
| DesertWellProcessor | 3 | processTemplate: 114, 298; placeSusSand: 9 |
| INbtFeatureProcessor | 2 | generatePillarDown: 12, 75 |
| SwampFeatureProcessor | 6 | processTemplate: 54, 121, 222, 285, 440, 561 |

These are call-site counts, not observed writes. Shared interface invocation must
retain an interface method reference. Existing Item 8 rules govern empty
processor lists, sand-marker replacement, archaeology loot assignment and swamp
supports. Block-ID occurrence corroboration does not claim loot-table or block
entity equality. The actual last successful write determines saved block-ID
comparison; earlier writes and refusals remain raw evidence. Never truncate a
support column at the template envelope or infer placement from the helper return.

Extend the existing probe and fixtures, without a new collector framework.
Acceptance of the extension requires exact retained-class transformation, original
call/argument/result and exception preservation, configured/template attribution,
post-template capture and absence of capture outside an active Extras attempt.
Natural capture and saved-world corroboration remain missing. Predeclare any
runtime diagnostic and storage reservation before launch; no Extras experiment
has run for this increment.

## Extras r1 bounded natural diagnostic

Predeclared 2026-09-08 before launch. Use ordinary seed 42 and the existing fixed
pilot selections: 81 chunks each in Overworld, Nether, central End and outer End
(center 1536, 0), totaling 324 selected chunks. Use fresh hash-verified frozen
runtime/configuration materialization, construction heap and the current observer.
Do not choose coordinates from observed Extras locations or change biome rules.

```sh
uv run --no-sync python -m tools.run_item10_probe --name extras-pilot-r1 --mode probe --role ordinary --preset pilot
```

The source identity is the commit containing this predeclaration. This is a
collector diagnostic, not density sampling. Require completed selections,
correlated save, clean exit, incoming class identities and no unfinished attempts.
Positive Extras capture requires actual configured/template identity and complete
template/processor observations, then saved last-successful block-ID
corroboration. Preserve earlier writes, refusals, exceptions, zero-write attempts
and halo positions. A missing positive path remains unmet, not zero density; no
frame expansion is authorized to hunt for a positive result. Mixed traces must
pass the existing archive-bound reader before being accepted as capture evidence.

Prelaunch storage is 4.0 GiB free and no Java process is running. Reserve 1.5 GiB
for this bounded run and sequential archive/download/restore. The most recent
same-frame bridge diagnostic took 89.441 seconds and archived 5,688,682 bytes;
these are cost proxies, not guaranteed Extras output. Use the existing 900-second
harness timeout. Full sampling remains gated on the separate provisional 5 GiB
workspace floor and complete occurrence coverage. Preserve the raw result and
stopped world with existing tools even if positive capture fails. No tuning,
client recording, Item 11 execution or new measurement framework is included.

## BetterEnd procedural pillar write boundary

Reuse the accepted `betterend:ruined_obsidian_pillar` contribution in
[Item 8](../item-8/inventory.json). FallenPillarFeature and
ObsidianPillarBasementFeature are two independently placed variants of one
canonical family. Their geometry, replacement and mossy-obsidian callbacks are
already assessed. Do not recount them as two families or infer voxel occupancy
from the shape envelope.

The retained [generator classes](../item-8/sources/betterend-pillar-end-hooks/identities.json)
call `SDF.fillRecursive(ServerLevelAccessor, BlockPos)` at offsets 287 and 372,
respectively. Observe each feature attempt and that actual fill anchor. Capture
normal and exceptional completion, and preserve refusal and zero-write results.
The fill is void and the outer generator return is not a successful-write count.

Direct inspection used pinned `javap -c -p -classpath` on `bclib-21.0.24.jar`,
whose archive SHA-256 was verified against the existing
[shape identities](../item-8/sources/pillar-shape-semantics/identities.json):
`a7efd02dd3409dbac9c8455c5ed4fa4ca340e2af1c39f211038198dfa1c92093`.
The two inspected classes are:

| Class | SHA-256 |
| --- | --- |
| `org/betterx/bclib/sdf/SDF.class` | `048c1c86a07b43ef4ecc6ed4c6b44d66fb119e7bbf4b55ffd100c61c2115a59d` |
| `org/betterx/bclib/util/BlocksHelper.class` | `4196c4a40a0d71d38061a084f005343262eb9d49d18c79e3a62ac6d03d90da72` |

The server-level fill path invokes the writer callbacks lambda$fillRecursive$3
and lambda$fillRecursive$6. Both call the BlockState overload of
BlocksHelper.setWithoutUpdate, at offsets 9 and 37. The second callback first
rechecks canReplace against the current world state. The helper invokes
LevelAccessor.setBlock at offset 5 with flags 18, discards its result at 10 and
returns. Capture that actual boolean, position and state without changing the
original discard or consuming additional randomness. The StructureWorld overload
and unrelated SDF fills are separate paths, not additional pillar occurrences.

Extend the existing feature observer and direct-write path. Gate the shared
BlocksHelper hook on the two exact active pillar classes, leaving other callers
untraced. Preserve the original LevelAccessor invocation outside that gate.
Record the actual fill anchor rather than assuming it equals the initial feature
origin. Require retained-class transformation and focused original-versus-observed
checks for successful writes, refusal, exceptions followed by same-thread recovery,
and outside calls before full collection. No pillar experiment has started.
Natural occurrence inclusion and saved-block corroboration remain incomplete.

The collector now brackets both pillar feature entrypoints, records the actual
`pillar_fill` anchor, and observes the shared helper's real boolean write result
only during those attempts. It reuses feature completion and exception cleanup.
The LevelAccessor invocation remains unchanged for unrelated callers; no random
calls or configuration edits were added. Hash-verified retained transformations
pass for both BetterEnd classes and BlocksHelper. Synthetic execution compares
original and observed outputs for normal writes, refusals, early exits, unrelated
fills, exception-object preservation followed by same-thread recovery, and an
isolated class loader, for each pillar variant.

Validation: `uv run --no-sync pytest -q tests/item10/test_placement_probe.py`
passed all 50 collector tests in 66.41 seconds. Focused Ruff and basedpyright
checks pass. These tests establish observer preparation, not natural occurrence
measurements. Full-sample reader integration must accept and validate these new
events and installation identities before collection. No new pilot or PR was
created for this change.

### BetterEnd template auxiliary writes

The accepted disassemblies were rechecked against their existing identity hashes:
[NBTFeature](../item-8/sources/betterend-entry-template-consumers/identities.json),
[StructureErode](../item-8/sources/crashed-ship-erosion/identities.json) and
[BlockFixer](../item-8/sources/betterend-lake-helpers/identities.json).
NBTFeature.place performs terrain-merge writes through BlocksHelper at offsets
558, 569, 622 and 633. CrashedShipFeature.place calls erodeIntense at 259 and
BlockFixer.fixBlocks at 308. Erosion and its drop helper use both Block and
BlockState overloads of BlocksHelper.setWithoutUpdate; BlockFixer's synchronized
wrapper delegates to the BlockState overload. Its IntStream.range/forEach and
Set.forEach calls do not introduce parallel execution in the inspected code.

Both BlocksHelper overloads call LevelAccessor.setBlock directly with flags 18,
at offsets 8 (Block) and 5 (BlockState). The Block overload does not delegate to
the already observed BlockState overload. The collector now intercepts both
actual write calls while a pillar, NBTFeature/BuildingListFeature or crashed-ship
attempt is active. Shared caller behavior outside those attempts is preserved.
This reuses the pillar helper hook and existing write events, including air
removal, rather than adding separate erosion or repair observers. Existing event
order retains template and subsequent auxiliary writes within the same attempt.
NBTFeature and crashed-ship exceptional exits now use the existing cleanup path.

Synthetic original-versus-observed checks cover both helper overloads after
template placement, refusals and an original exception followed by a successful
placement on the same thread. Earlier diagnostic raw traces remain unchanged.
Full-sample interpretation and saved-world corroboration remain required; a
successful template call does not establish that all its blocks survived erosion.
All 53 collector tests pass in 63.98 seconds, including hash-verified retained
NBTFeature, crashed-ship and BlocksHelper transformations. Focused Ruff and
basedpyright checks pass. Reproduce with the collector test command above.

### End generation and lifecycle applicability

Reuse `betterendisland:platform_gateway` in the accepted Item 8 inventory,
especially its `packaged_biome_entrypoints`, `packaged_feature_placement`,
`spike_podium_generators`, `runtime_activation` and `generated_world_observations`.
The following existing disassemblies were checked against their committed hashes:
[platform/gateway](../item-8/sources/better-end-island-platform-gateway/identities.json),
[spike/podium](../item-8/sources/better-end-island-spike-podium/identities.json),
[exit portal](../item-8/sources/better-end-island-exit-portal/identities.json) and
[vanilla platform caller](../item-8/sources/vanilla-end-platform-caller/identities.json).
No new Item 8 measurement or classification is needed.

| Accepted family | Ordinary generation exposure | Location accounting |
| --- | --- | --- |
| `betterendisland:arrival_platform` | `minecraft:end_platform` in the central End biome, fixed caller origin `(100,49,0)` with a biome filter. | One distinct platform at its caller anchor, not one location per placement retry or per template block. Record the fixed-position nature; do not extrapolate a uniform spatial rate. |
| `betterendisland:gateway` | `minecraft:end_gateway_return` in the accepted vanilla/BetterEnd/BOP biome consumers, with rarity 700 and terrain-relative placement. | Distinct gateway anchor positions from the ordinary feature route are eligible for the sampled density. Dragon-fight and travel-triggered gateway events are separate lifecycle observations. |
| `betterendisland:dragon_arena` | `minecraft:end_spike` in the central End biome. The retained custom layout has ten spike centers at radius 42. | One arena location anchored at central `(0,0)` X/Z when observed, with spikes and podium retained as components. Ten spikes, their template parts and later rebuilds must not become ten or more arena locations. |

The full central-End frame contains the fixed platform and arena coordinates;
this establishes exposure, not successful placement. Gateways remain subject to
actual biome filtering and observed writes. Record runtime accessor/route context
alongside attempt and component identity so ordinary chunk generation can be
distinguished from ServerLevel lifecycle invocation. Unresolved route attribution
must remain explicit rather than being silently assigned to the density numerator.

No player arrival, dragon death, respawn or missing-portal recovery campaign is
required for Item 10. Record such events only if they occur during the prescribed
run, separately from ordinary generation. Absence of a triggered event is not a
failed placement or evidence that its design cannot generate. Existing central-End
block aggregates establish material presence only and cannot replace missing
platform/gateway/podium occurrences.

The collector now brackets BetterEndGatewayFeature.place,
BetterEndSpawnPlatformFeature.place, BetterEndPodiumFeature.place and
BetterSpikeFeature.placeSpike. It records actual caller anchors and the runtime
accessor class with a WorldGenRegion instance check in `island_context` events.
Spike input center/height is retained as a component anchor; each actual template
position is separately observed. Runtime accessor context supports route attribution
but does not justify labeling an unknown caller as a known lifecycle event.

The existing template observer captures each helper's selected resource path,
placement result and content writes. Gateway and spike direct setBlock calls are
captured with their real results and flags. Multiple spike templates remain under
one component attempt. Void completion, failed writes and exceptions retain their
distinct existing event types; exceptional exits clear the attempt for subsequent
calls. No random calls or configuration changes were added.

Validation: all 77 tests in `tests/item10/test_placement_probe.py` pass in 92.58
seconds, including hash-verified transformations of all four retained generator
classes. Synthetic comparisons cover early exits, refused writes, caught template
exceptions followed by another attempt, generation-region versus other accessor
context, direct writes and an isolated class loader for all four entrypoints.
Focused Ruff and basedpyright checks pass. Full-sample event validation, occurrence
aggregation and saved-world corroboration remain incomplete. No End experiment
or new PR was started for this collector increment.

### Spatial integration for observed anchors

The shared spatial summary now accepts explicit integer `anchor_x`/`anchor_z`
block coordinates for traced locations. Registry records without these fields
retain their declared start-chunk-center convention. Both explicit coordinates
must be present, must belong to the supplied inclusion chunk using floor division
(including negative coordinates), and must lie within the selected chunk frame.
Distances and boundary censoring use these actual anchors; cell occupancy and
empty-region denominators retain the existing chunk grid. This prevents distinct
within-chunk locations from being incorrectly assigned zero separation.

The focused spatial/census suite passes 29 tests, including actual-anchor distance,
negative-coordinate inclusion and rejection of incomplete, coerced or out-of-frame
coordinates. Ruff passes for the analysis tool and tests; basedpyright passes for
the spatial tests, matching the existing validation surface. All eleven spatial
categories recomputed from the committed pilot occurrence records equal the
retained `pilot-r1/spatial-census.json` results exactly. No pilot was regenerated.
This enables the downstream location table; trace-to-location aggregation remains
incomplete and no new density result is claimed.

### Full collection trace reader

`collection_attempts` in the existing `tools/validate_item10_trace.py` streams
the collector's full event vocabulary, retaining every event within completed
attempts instead of loading an entire world's writes at once. It verifies the
declared trace SHA-256 before reading and again while processing, checks declared
installation digests and dimensions, rejects malformed fields and duplicate
metadata, pairs template/flower delegates and requires healthy terminal shutdown.
Failed attempts and refused writes remain explicit output, not accepted locations.

The caller must supply independently verified archive/class identities and exhaust
the iterator before publishing any result. Before yielding attempts, the reader
hashes every declared incoming class in the adjacent `trace.jsonl.classes` tree.
Missing files, digest mismatches, linked class files and paths escaping that tree
reject processing. Trace installation hashes must match those same identities.
This binds retained bytes, not just installation claims. It does not establish
that the caller supplied the complete required observer set; full-protocol
identity selection remains mandatory. Provider-specific success validation and
location counting also remain required. Existing fixed-diagnostic readers are
unchanged.

Validation: 88 collection/retained-trace tests pass in 0.37 seconds. Both actual
Bridge and Extras archived traces retain exactly their accepted attempt/write
counts through this reader. Mutation tests reject mismatched hashes/installations,
missing ends/shutdown, duplicate attempts/metadata, malformed values, unpaired
delegates and undeclared dimensions. Focused Ruff and basedpyright checks pass.
The subsequent incoming-file integration passes 91 collection/retained-trace
tests, including both restored Bridge/Extras class trees and missing, altered or
linked incoming files. Reproduce with `uv run --no-sync pytest -q
tests/item10/test_collection_trace.py tests/item10/test_retained_trace.py`.

### Nonregistry family attribution

`nonregistry_membership` and `attribute_nonregistry_attempt` in the existing
analysis tool join structurally validated attempts to the unchanged, hash-verified
Item 8 inventory. The 27 generator class bindings and 151 exact template paths
cover exactly its 40 accepted nonregistry families. Building designs use their
configured resource paths; aliases and multiple arena templates retain one family.
Cave urn attribution additionally requires the observed cave placed-feature parent.

Attribution does not establish a successful location. Early building failures
without a selected design remain `NO_DESIGN_SELECTED`; unknown template paths
remain `UNMAPPED_TEMPLATE`, and missing cave parent identity remains
`UNRESOLVED_URN_PARENT`. Conflicting class/template family identities are rejected.
The six existing ambient-template dispositions are reused directly from that
same inventory: five small ruin fixtures and the Lantern Woods light. Their
attempts remain explicit excluded decoration. An observed Blossoming Spires
house raises an inventory-conflict error because Item 8 establishes no active
route for that template. It cannot silently become excluded decoration or an
accepted family. Other unmapped paths remain unresolved. Provider success rules
and distinct-location aggregation still require integration before counts can
be accepted.

Reproduce the focused attribution and downstream regression check with:

```sh
uv run --no-sync pytest -q tests/item10/test_nonregistry_membership.py tests/item10/test_collection_trace.py tests/item10/test_density_census.py tests/item10/test_density_spatial.py
```

All 57 tests pass. The retained Bridge and Extras traces reproduce their accepted
cave-parent attempt counts through the family join. These are attribution checks,
not additional density measurements or new experiments.

### Ordered attempt outcomes for saved-world integration

`nonregistry_attempt_outcome` consumes structurally paired attempts in event order.
It retains refused writes, the last successful block ID at each written position,
source and selected template/fill anchors, and explicit exception outcomes.
Template-derived families require writes inside the template phase for observed
content; later terrain/support writes alone cannot create a template occurrence.
Later successful removal to air removes that position from surviving content.
Cave-cache content requires actual urn writes, while fairy collector site 1 is
excluded from constructive writes. Boolean generator/template returns alone do
not establish content.

These are attempt outcomes, not accepted location counts. `CONTENT_OBSERVED` and
`EXCEPTION_WITH_CONTENT` must still undergo provider completeness, saved-world
corroboration, overlap/component aggregation and sample inclusion. Fairy delegated
flower origins and observed post-call block IDs now enter content and saved-world
processing separately from direct successful writes. A false delegate return with
non-air origin content remains content; a true return leaving air does not.
This does not establish complete ring visibility or the delegated feature's full
footprint. Arena components
retain their original coordinates but use central X/Z for the eventual location.
End accessors distinguish `ordinary_generation`, `non_worldgen_accessor` and
`unresolved`; a non-worldgen accessor does not identify a specific lifecycle cause.

The 35 focused attribution/collection tests pass. Both retained mixed traces
reproduce their cave-parent attempt counts and successful urn content-position
counts. Synthetic cases retain multiple urn blocks in one attempt, refused writes,
post-template erosion and exceptions with partial content. Scoped Ruff and test
basedpyright checks pass. No new runtime observation or density result is claimed.

`nonregistry_location_groups` reduces one world's outcomes by dimension, family,
accessor route and exact source/placement anchor. Spiral contributions sharing
their source remain one candidate with every attempt ID retained. Arena height
is not part of the key: its components share central X/Z, with location Y left
unavailable instead of choosing a spike height. Other coincident anchors group
without inventing additional sites from repeated attempts. Distinct anchors that
share observed content remain separate candidates with explicit overlap pairs
and shared-position counts, pending overlap acceptance. No proximity threshold
or adaptive clustering rule is introduced.

Frame membership uses floor-divided anchor X/Z and dimension. Sources outside
all selected frames, zero-content outcomes and unattributed attempts remain in
the result; overlapping frame membership is rejected. Output order is deterministic
under reordered input, and the status remains `CANDIDATES_AWAITING_ACCEPTANCE`.
Saved-world corroboration and provider acceptance must precede density totals.
The focused attribution/collection/spatial/census suite passes 68 tests, including
the retained mixed traces' exact spiral source counts. Scoped Ruff and test-file
basedpyright checks pass.

### Saved content integration

The analysis tool's `saved_content_observations` reads requested coordinates from
a stopped world under the existing POSIX world lock. Region and external-chunk
bytes must match the caller's verified world manifest, remain within the world
tree and remain unchanged during inspection. Input hashes are retained. The
result preserves saved block states and chunk status, including explicit
`MISSING_CHUNK` and `MISSING_BLOCK_SECTION` observations. Missing evidence is
never inferred to be air or a matching placement. The caller must bind the world
manifest to accepted custody before using these observations for acceptance.

Palette lookup is shared with the retained `scarecrow-probe-r3/inspect-writes.py`
diagnostic instead of maintaining duplicate decoding logic. Negative coordinates,
singleton/packed palettes, chunk ownership and duplicate sections retain explicit
handling. The focused saved-content/census suite passes 17 tests, including the
restored urn world's exact saved states. Re-running the shared urn diagnostic
produces JSON equal to committed `urn-pilot-r1/write-corroboration.json`, retaining
all 429 mixed recorded writes. Ruff and saved-content test basedpyright pass.

```sh
uv run --no-sync pytest -q tests/item10/test_saved_content.py tests/item10/test_density_census.py
PYTHONPATH=. uv run --no-sync python evidence/item-10/scarecrow-probe-r3/inspect-writes.py --urn-r1
```

This supplies saved observations for candidate acceptance; it does not equate
block-ID agreement with full-state equality, noninterference or an accepted
location count. No fresh world generation was performed.

The existing census CLI accepts paired `--trace-root` and `--trace-manifest`
arguments to add `nonregistry_candidates` to its registry result. The raw archive
manifest binds the trace, incoming classes and world manifest; the latter must
also match every registry census input hash. Candidate processing consumes the
complete stream, then joins saved block observations while preserving missing
and mismatched results. With trace inputs, classification and spatial summaries
now combine registry starts and `OBSERVED_LOCATION` nonregistry sources over the
same selected denominator, using `all_locations` rather than `all_registry`.
Other dispositions remain explicit outside those numerators. Full observer
coverage and sampling remain separate acceptance gates. Per-attempt last-write checks are not
claims about global ordering across concurrent attempts. The retained
[urn integration](urn-pilot-r1/README.md#integrated-offline-analysis) supplies the
reproduction command, output hash and explicit diagnostic denominators.

The fairy cleanup reader initially compared the collector's ordinal writer value
to bytecode offset 193. Inspection of the retained instrumentation establishes
that raw sites are 1 through 4, with site 1 corresponding to offset 193. The
reader now uses site 1. The correction and origin-state integration pass 48
focused attribution/collection/saved-content tests, including false-return
non-air and true-return air cases. No recorded raw event was changed.

### Location observation acceptance

For the integrated reader, a location observation is one canonical source group
with constructive content confirmed at a recorded position in the stopped world.
It is not proof of an intact dungeon, usable loot or a complete visible ring.
Require an in-frame anchor, ordinary generation context, no exceptional attempt
in the group and no unresolved shared-content overlap. Compare the last observed
constructive block IDs, including post-call flower states, to saved observations.
Missing required saved content remains unavailable; content with no surviving
match remains not preserved. Retain the matching and nonmatching position counts
even when some content survives. Report partial failures and overlaps separately
instead of accepting them or treating them as generation zeros. Full density
acceptance still requires the independently complete observer identity/coverage
gate and full predeclared sampling; diagnostic location observations do not pass
that gate on their own.

The integrated command implements these dispositions in `location_observations`,
retaining the candidate records and per-position check counts. The retained urn
pilot confirms seven in-frame cache observations, with 468 zero-content and 811
out-of-frame source groups preserved. Its README records the reproducible output
identity. The 56 focused attribution/collection/saved-content tests pass, including
missing evidence, changed content, exceptions, non-worldgen context and overlaps.

The shared classification join preserves Item 9 confidence, rationale and ambiguity
for both populations. It rejects wrong-dimension/out-of-frame nonregistry locations
and families outside the accepted nonregistry inventory. Registry-only invocations
retain their previous results. The combined retained urn pilot contains eight
locations: one registry start and seven cave caches, with the latter retaining
their provisional T1 role. These are encounter-site candidates, not fights.
The 86 focused integration/census/spatial tests pass; Ruff and census-test
basedpyright checks pass.
