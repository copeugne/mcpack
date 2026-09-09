# Item 12 discoverability assessment protocol

Status: PREDECLARED. Identifier: `item12-discoverability-v3`. Date: 2026-09-09.

Revision 3 is predeclared before corrected processing. It fixes PR39 finding
3969034729: candidate observers inside the target's horizontal saved envelope
cannot count as external discoverability. Their ray outcomes and the complete
ring's low/high selection become UNKNOWN. Retain their measured heights for
placement context. Version 2 and its rejected local-gate claim remain at
`eb2742a2`; version 1 remains at `aa9f700f`. The v2 strict top-boundary fix remains.
Worlds, family selection, targets and candidate observer cells do not change.

## Authorized method and acceptance boundary

The user separately authorized inspection and automated assessment for Item 12,
with explicit limits, on 2026-09-09. This is a new Item 12 decision, not an extension
of the Items 10/11 amendment. Visual/artifact inspection can assess architectural
cues and discovery risks; it cannot measure human recognition, discovery rates,
search time or actual command dependence. Those human quantities remain NOT
MEASURED. Interpret the Item 12 /locate requirement as an evidence-supported risk
assessment under declared navigation assumptions, never proof that a command is
necessary for every player. No human trials are required under this decision.

## Smallest complete proof

Reuse all 448 Item 8 family descriptions and Item 9 roles without reclassification.
Reuse Item 10 density, saved placements, biome attribution and immutable custody,
and Item 11 route results without route processing. Add only a bounded saved-world
viewpoint measurement, architectural entrance/silhouette assessments and a report
joining these independent quantities. Existing Anvil/NBT, saved-block lookup,
archive binding, safe file readers and POSIX world lock are the implementation path.
No server, world generation, configuration tuning or new preservation system.

Definition of done: every requirement in README has a result and explicit scope;
predeclared samples, raw outcomes, failures and uncertainty are retained; all
reported quantities have denominators and reproducible derivations; source/world
identities verify; a representative is completed before expansion; focused tests,
manual visual check and clean reproduction pass; coupled work is pushed in coherent
milestones; the final PR has completed clean Codex review and is merged with main
verified. Item 13 remains unstarted. No desirable visibility score is required.

## Sampling and viewpoints

Use the sixteen accepted Item 10 worlds and their existing Overworld 4,096-chunk
frames [-32,31] on each axis. Both arms and repetitions remain separate; baseline
is the product assessment and omit-Sparse is contextual sensitivity. Other dimensions
retain source-based assessment and accepted density only, not new viewpoint claims.
For each world and each canonical family present in that frame, select one location
by minimum SHA-256 of its stable Item 11 location ID, with ID as tie-breaker. This
bounds common cache dominance without selecting for good visibility. Retain the
full family occurrence count as the density denominator context. Samples are
family-balanced case studies, not a probability estimate over all placements.
Missing/out-of-frame geometry remains UNKNOWN; never replace the selected case.

For registry cases reuse saved piece envelopes and preserve the root ID/variant.
For nonregistry cases use the actual saved block anchor. Envelope targets are
explicit geometric proxies, not verified authored blocks or entrance coordinates.
At the envelope center and four horizontal corners, target Y is inclusive maximum
Y plus one. Single-block cases have one target. These targets test potential
external exposure; internal entrances need separate artifact assessment.

For each case take eight candidate observer cells at offsets (64,0), (45,45),
(0,64), (-45,45), (-64,0), (-45,-45), (0,-64), (45,-45) from floored envelope center
(or nonregistry anchor). Use saved MOTION_BLOCKING_NO_LEAVES plus 2.62 for eye Y.
This reduces canopy bias but is not a walkability/collision guarantee; logs,
buildings and fluids can still support the proxy. Retain all observer heights and
WORLD_SURFACE height. A registry observer cell inside the inclusive horizontal
envelope (minX <= cellX <= maxX and minZ <= cellZ <= maxZ) is ineligible for
external visibility, regardless of its eye Y. Retain each ray as UNKNOWN with
reason observer_inside_envelope; never reinterpret roof or courtyard arrival as
external discovery. Nonregistry anchors have no wide envelope. Lowest and highest observer cells are respectively the
local low and high viewpoint, ties broken by the listed offset order. Call these
valley/high-terrain proxies, not geomorphological valley classification. Report
actual relief so flat cases are distinguishable. Missing any observer height or any internal observer cell makes
extremum selection UNKNOWN rather than selecting a biased partial ring.

At each viewpoint test all targets using one-block-or-finer horizontal ray samples,
excluding the eye and including the target cell. Compare with WORLD_SURFACE plus
one as the top boundary of the opaque height field. A sample strictly below
that boundary is occluded; equality is clear at that sample, including at the
target endpoint. A later blocking sample can still occlude the ray. Also test MOTION_BLOCKING_NO_LEAVES with the SAME eye
and targets. Retain both outcomes and obstruction locations/heights. Their contrast
is a foliage-sensitive heightmap model, not a counterfactual world with trees
removed. Fluids, transparent blocks, roofs and overhangs limit both models; neither
models cave interiors. Group by accepted target biome with its existing attribution
limitations, not a new inferred biome. UNKNOWN stays separate from occluded.

## Entrances, silhouettes and navigation assessment

Assess sampled family source forms using exact Item 8 references, retaining variant
and evidence limitations. Explicitly distinguish a surface landmark, internal
architectural cue, no established surface entrance and unknown entrance position.
Do not label an envelope target an entrance. For representative surface and
underground cases inspect saved-world cross-sections with bounding boxes and both
height fields. These are technical diagrams, not Minecraft screenshots or textured
human-view renders. Existing source/template inspection supplies architecture;
world sections supply placement context. Neither alone establishes recognition.

Silhouette rubric: potentially distinctive architectural form; small/terrain-like
form; internal-only form; or insufficient evidence. Entrance-importance rubric:
external architectural lead established by source; internal cue only; no dedicated
entrance for a cache; or insufficient evidence. Explain judgments with cited forms,
not names, tiers or bounding-box size alone. A large box is not a recognizable form.

Navigation assumes ordinary exploration, cave travel and legitimately obtainable
maps/leads where verified. No admin coordinates, prior seed knowledge, spectator
vision or /locate information is given to a hypothetical explorer. Engineering
breaching is possible but not an explanation of how an unknown target is found.
Assess command-dependence risk as elevated when content has no established external
cue or verified survival lead; lower when an external landmark or verified lead
exists; unresolved where evidence cannot distinguish them. Verify relevant existing
map/lead evidence before calling a buried objective command-dependent. These are
bounded assessments, not player outcomes or proposed Item 31 implementation.

## Denominators, failures and uncertainty

Report per world/family selected cases, eligible target/viewpoint rays, clear,
occluded and UNKNOWN outcomes, and both low/high outcomes separately. Give exact
counts for all sampled cases; do not pool overlapping targets as independent
worlds. Compare density independently: full accepted family counts / 4,096 chunks,
not sample counts / chunks. Frequent and rare are comparative descriptors tied to
explicit counts, never undocumented cutoffs or universal generation rates.
Zero cases in a finite frame do not prove absence. No binomial/population confidence
intervals for purposive seeds or family-balanced samples. Report per-world values,
range and paired differences where meaningful; two repetitions and saved-world
nondeterminism limit generalization. Do not silently drop errors or change selection
rules after inspecting results. Preserve failed producer output; resolve code defects
without changing accepted source bytes or tuning configuration.

## Resource gate and representative

Fresh availability inspection verified all sixteen restored file inventories and
census hashes in 11.099 seconds: 6,806,284,224 world bytes and 1,784,216,273 census
bytes. Free space was 44,555,952,128 bytes. See validation/input-availability.txt.
Reuse those restores read-only with a full inventory check under the existing
Java-compatible lock before and after analysis. Recheck archive-bound backup
manifest and census hashes at consumption. A new controlled experiment, if ever
needed, would require fresh materialization and a separate predeclaration.

The original representative was ordinary r1 baseline and included ships, buried
temples/chambers, underground caches and an elevated settlement. Revision 2 first
completed biome-diverse r1 baseline for the top-boundary defect. Revision 3 first
completes ordinary r1 baseline, including the elevated settlement with internal
viewpoints. Complete its raw observations, report, updated assessment and focused
checks before expanding to the remaining fifteen unchanged worlds.

Version 2 measured 787.711 summed producer seconds and 814,577 result bytes for
all sixteen worlds. Revision 3 uses the same read/verification path and reduces
ray work, so budget 20 minutes and 1 MiB for the full matrix, still within the
original 160-minute and 1-GiB limits. Retain the 2-GiB memory target and 5-GiB
free-space floor. Record actual representative time/size before expansion. No
peak-memory or server-performance claim follows from these budgets.
