# Item 10 sampling proposal

Status: DRAFT, not authorization to collect acceptance evidence. No observations
have been inspected to choose this design. This proposal resolves the spatial
sampling choices; the Item 5 methodology change and occurrence instrumentation
must be resolved before freezing it. The existing Item 5 contract remains active.

## Proposed separation from Item 5's generic observation matrix

Apply static spatial counting to fresh generated worlds without player-count,
warm-up or fixed-duration requirements. Generate one independent materialization
per seed, with one separately generated ordinary-seed pilot repeat to check
reproducibility. The repeat is validation, not an independent statistical sample.
This changes only static collection for structure count, structure distance and
static category densities. It does not convert combat into a static label.

Proposed Item 10 combat baseline: four solo sessions, one per frozen seed,
30 minutes of active observation each. Personal participation is capped at two
hours total. Allow up to ten minutes of unattended server stabilization before
each session, giving at most two hours forty minutes of scheduled server time,
excluding automated world generation and initial client troubleshooting. Do not
add discarded human replicates or extend sessions to reach a desired count.

This explicitly replaces the generic Item 5 player-case/repetition/duration
matrix for Item 10 baseline combat only. It does not revise later multiplayer
performance, balance, depletion or Item 11 human-exploration requirements. It
provides a limited solo baseline, not a multiplayer comparison or precise
all-dimension encounter estimate. User agreement and a reviewed methodology
amendment are required before this becomes the accepted contract.

Use a predeclared Overworld observation area for each seed, with its exact full
chunk coverage recorded. After the static pilot establishes what can be observed
within a session, freeze area, starting equipment, permitted interactions and
coverage recording before any accepted combat session. Do not select areas for
high encounter counts after inspecting results. Record encounters actually
engaged, not potential hostile sites, with timestamps, locations, participating
mobs, encounter boundaries and video or equivalent ground-truth evidence.

The combat event rule must distinguish one continuous engagement from renewed
engagement and simultaneous independent encounters. Record zero-event and
interrupted sessions, unvisited chunks and visibility limitations. Report the
numerator, fully generated area denominator and actual observation coverage
separately. A zero count during thirty minutes does not mean that area has no
possible combat. No rate precision or multiplayer generalization is promised.
Casual play in either operational profile is not an accepted run. This proposal
does not implement any Item 11 exploration workflow.

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
have a recorded hash and validate that it preserves generated content on the
pilot repeat. Do not claim all-family density until that boundary passes.

Report structures, actionable locations, Tier 2+ proper dungeons, Tier 3+ major
expeditions, exclusive tiers and villages with explicit numerators over the same
selected full-chunk denominator. Preserve the provisional classification's
confidence and ambiguity. Static hostility is a separate descriptor and never
the observed-combat numerator.

## Spatial summaries and uncertainty

Use horizontal Euclidean distance in blocks within each seed and dimension/stratum.
Report nearest-neighbor distances by category. A target's nearest observed
neighbor is exact only when that distance is no greater than its distance to the
sampling boundary; otherwise retain it as boundary-censored. Do not calculate an
uncensored mean by silently dropping those cases. Zero or one observed member
does not have an estimable nearest-neighbor mean.

Partition each rectangle into aligned 16 by 16 chunk cells. Report count
distributions and variance/mean by category as a descriptive clustering measure.
Report all zero-count cells and the largest axis-aligned rectangle of zero cells
fully inside the sample, resolving equal-area ties lexicographically by bounds.
This measures emptiness at 256-block resolution, not the exact largest empty disk.

For biome comparisons, retain the biome at every occurrence anchor and count
selected chunk-center biomes at every stored quart-height, reporting height bands
separately. Do not divide underground starts by an unrelated surface-only biome
denominator. Sparse biome/category cells remain visible, with raw denominators.

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
still requires observed combat, Sparse Structures attribution, clean Codex PR
review, merged main delivery and the subsequent Items 2 through 10 consistency
audit. Neither this protocol nor a completed static subset closes Item 10.
