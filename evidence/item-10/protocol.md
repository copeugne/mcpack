# Item 10 sampling protocol

Status: DRAFT AUTOMATED PROTOCOL. The user-authorized
[scope amendment](methodology-amendment.md), `item10-automated-v1`, removes human
sessions and recording from both Items 10 and 11. The former combat collection
contract and blind-operator requirement are superseded for these items. No
human workload is scheduled or deferred as a completion condition.

## Measurement boundary

Item 10 measures placement and provisional location categories. Encounter sites
are T1 through T4, actionable candidates are C and T1 through T4, proper dungeons
are exclusive T2, major expeditions exclusive T3, and T4 objectives are separate.
Villages use the accepted Item 9 `village` comparison group. These definitions
are potential location roles, not observed fights or meaningful human activity.
Retain confidence, ambiguity and the scope limitations in every final result.

The Item 5 methodology delta passed clean PR22 review and main delivery. The spatial
frame below remains a draft, not a frozen full experiment protocol. The fresh
registry pilot and its diagnostic processing remain reusable evidence. Complete
nonregistry occurrence coverage, biome attribution and the Sparse Structures
control design before full collection. Do not implement Item 11 workflows until
Item 10 delivery and the cross-item audit pass.

## Fixed spatial frame

Use all four exact seeds and the server/configuration hashes in [README](README.md).
Include all ten dimensions in the accepted
[runtime capture](../item-8/runtime/dimension-r3/dimension-biomes.json).
Treat the End as separate central and outer strata, giving eleven strata per seed.
Never pool different dimensions' coordinates or convert their distances by portal
scaling. The inclusion of space dimensions permits measured zeroes rather than
assuming the lack of structures from their names.

Use the four nested rectangles in
`measurement/structure-density-v0.1.json`, translated by chunk offset `(0, 0)`
for every stratum except the outer End, translated by `(512, 512)`.
The outer End rectangle does not overlap the central rectangle at any stage.
Select every target chunk in each rectangle, not only chunks that contain starts.
Freeze all four stages; do not use a count-based early stopping rule. This avoids
letting an observed category count determine the sampled area. Retain stage
results as nested convergence descriptions, never as independent replicates.

Stage sizes per stratum are 4,096, 8,192, 16,384 and 32,768 chunks. Across four
seeds and eleven strata, final target size is 1,441,792 chunks. The initial
ordinary-seed, Overworld-only stage is a pipeline pilot and does not represent
the complete baseline. Preserve a rejected pilot and its disposition.

## Occurrences and denominators

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
their parent location. Lifecycle sites, including End arrival and dragon/gateway
events, must be reported separately from ordinary terrain-generated density.

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
The existing `--biomes` reader now implements this registry attribution alongside
height-band exposure. Focused Item 10 validation passes 29 tests, including
negative heights, missing bounds, out-of-height attribution and inverted bounds;
Ruff and the changed test's type check pass. Real-world attribution integration
remains to be run, and does not alter the generation-equivalence projection.

Report per-seed and per-stratum results first. These four deliberately selected
seeds and origin-centered regions are not a random sample of all Minecraft worlds.
Report finite-area counts exactly and cross-seed range descriptively. Do not call
deterministic repeat agreement a confidence interval. Categories with fewer than
30 occurrences remain sparse; absent observations are not proof of impossibility.

## Resource and delivery bounds

Using Item 7's planning proxy of 17,687 raw bytes per selected chunk, the final
frame is approximately 23.75 GiB raw before tracing, logs and derived data. One
32,768-chunk stratum is approximately 0.54 GiB raw. These estimates exclude the
extra pilot and any causal Sparse Structures control. The first pilot must replace
the proxy with actual runtime and storage measurements before scaling.

Process strata sequentially. Before beginning another stratum, archive the clean
world without `session.lock`, publish under immutable identity, verify download
and restore, and retain the committed manifest and durability references under
`evidence/item-10/`. Release disposable measurement materializations only after
that custody gate and within explicit authorization. Never remove the operational
player worlds, prior-item backups or protected artifacts to satisfy this budget.

Complete the ordinary pilot through deterministic analysis and retained evidence
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
