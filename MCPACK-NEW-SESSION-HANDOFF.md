# mcpack current handoff

Updated: 2026-09-08. This is the single active continuation checkpoint.

## Authority and preservation

Read [AGENTS.md](AGENTS.md), [SPECS.md](SPECS.md), and the
[execution ledger](Adventure-Engineering-Pack-Execution-Ledger.md). Read
[infrastructure instructions](INFRASTRUCTURE-INSTALLATION-AND-SERVER-TESTING.md)
before server or infrastructure work. Verify dated claims against Git and evidence.

GitHub `copeugne/mcpack` and fetched `origin/main` are delivery authority.
Last verified main is `0c98eeecfaf2cf6ffd6bd7671783f9d76530f893` after PR34.
Current local branch is `codex/item10-pillar-coverage`, based on the Extras branch.
Do not create another tooling PR from this branch. Preserve coherent intermediate
commits for the one consolidated remaining Item 10 delivery.

Preserve local changes to AGENTS.md, the CLOUD_HANDOFF.md deletion, `.codegraph`,
`.omo/`, `mcpack-reconstructed-28(1).bundle`, backups and all existing evidence.
The local archive `docs/history/HISTORICAL-MCPACK-HANDOFF-2026-09-07-REFERENCE-ONLY.md`
is untracked and unchanged. Never stage it or use it as startup instructions.
The prior `codex/item9-delivery-record` branch remains pushed at `3f758cb2`,
with only an unmerged historical-reference rename. Preserve that reference.
The [immutable earlier handoff](https://github.com/copeugne/mcpack/blob/be64d458fee3539e5132049d871d1c32ebc3655b/MCPACK-NEW-SESSION-HANDOFF.md)
is for specific unresolved historical questions only. Do not reread its diary or
repeat its commands. Inspect actual staged/unstaged/untracked state before edits.

## Delivered dependencies

Item 8 is COMPLETE through merged PR18 and PR19. Item 9 is COMPLETE through
merged PR20, with completion records in merged PR21 (`edd1dcf9`). Reuse the
[448-family inventory](evidence/item-8/inventory.json),
[Item 8 evidence](evidence/item-8/README.md),
[completed classification](evidence/item-9/classification.md) and
[Item 9 evidence](evidence/item-9/README.md). Do not repeat audits, classification,
preservation or history consolidation. Exact runtime/configuration dependency
hashes and reusable Item 5/7 evidence are in [Item 10 README](evidence/item-10/README.md).

PR22 delivered the [authorized automated scope](evidence/item-10/methodology-amendment.md)
and narrow Item 5 methodology amendment. No human sessions, recordings or blind
operators are required under current SPECS for Items 10/11. No recording/logger
was started. Do not interpret earlier six/ten-hour availability as an approved
workload. Do not implement, run, repair or lint Item 11 until Item 10 and the
Items 2 through 10 cross-item audit pass.

## User-directed reassessment and current gate

The user-directed experiment pause covered the reassessment. Follow the
[exit-gate reassessment](evidence/item-10/README.md#exit-gate-reassessment-2026-09-08).
Natural positive capture for every generator is not an Item 10 requirement.
Preserve failed/unmet pilots without making them prerequisites for more tiny
pilots. Complete observation, correct location numerators, the full fixed sample,
required comparisons, raw custody, uncertainty and final review remain mandatory.

Finish existing review obligations, then consolidate the remaining implementation,
full measurement, report and audit into one delivery PR with coherent commits.
Prioritize completed exit requirements over new tools or per-generator milestones.
The [protocol](evidence/item-10/protocol.md) is now frozen as `item10-full-v1`
for the first full ordinary baseline run. Its 720,896 selected chunks, four seeds, eleven strata, two repetitions
and two arms are method choices, not specification-mandated sample sizes. The
user confirmed retaining the original 16-world plan and roughly 30 GiB storage
budget. The first run is stopped as recorded below; do not reduce to eight worlds.

Storage capacity is now available: direct `df -B1` reports 48,890,408,960 bytes
(about 45.5 GiB) free after authorized library deduplication and uv cache cleanup.
The side task reports `uv cache clean` exited 0, removing 38 GiB of disposable
cache while preserving installed environments and project artifacts. Dependency
operations may resume. The original 16-world plan and roughly 30 GiB working
budget are retained by explicit user decision. See the
[cleanup outcome](evidence/item-10/server-setup/README.md#additional-duplicate-cleanup).
The edge-adjusted proxy estimates 11.05 generation hours and 13.92 GiB of original
worlds. Confirm actual collector costs on the first complete ordinary-seed run
before continuing the full protocol. Sampling and observer readiness still gate
collection; available space alone does not authorize bypassing them.

## Existing review obligations

PR23 through PR33 delivered bounded collector/analysis increments, not Item 10.
PR33 is cleanly reviewed and merged. Its
[delivery record](evidence/item-10/bridge-pilot-r1/README.md#reviewed-main-delivery)
links the final review and resolves trace-integrity and exception-cleanup findings.

[PR34](https://github.com/copeugne/mcpack/pull/34) is cleanly reviewed and merged.
Its [delivery record](evidence/item-10/extras-pilot-r1/README.md#reviewed-main-delivery)
binds the reviewed head, completed cycle and verified main merge. No existing
review obligation remains. The integrated Extras gate passed all 408 Item 7/10
tests in 99.62 seconds. This does not establish full Item 10 measurement acceptance.

## Evidence to reuse and remaining work

- [Registry spatial pilot](evidence/item-10/pilot-r1/README.md): 24 starts in 3,969
  full chunks; category joins, distances, clustering, empty regions and biome
  processing exist. These do not replace the full four-seed/control measurement.
- [Placement report](evidence/item-10/placement-probe.md): collector preservation,
  exact classes and retained failures. Scarecrow r3 whole-world equality failed;
  Item 7 already establishes semantic nondeterminism. Do not repeat that test.
- [BOP](evidence/item-10/bop-fixture-r1/README.md),
  [Monster Box](evidence/item-10/monster-box-pilot-r1/README.md),
  [Nether spikes](evidence/item-10/nether-spike-pilot-r1/README.md),
  [urns](evidence/item-10/urn-pilot-r1/README.md): bounded capture/corroboration.
- [Spiral](evidence/item-10/spiral-pilot-r1/README.md),
  [fairy](evidence/item-10/fairy-run-r1/README.md),
  [bridge](evidence/item-10/bridge-pilot-r1/README.md),
  [Extras](evidence/item-10/extras-pilot-r1/README.md): preserve limited/no-positive
  outcomes. Bridge/Extras raw archives and deterministic readers are validated.
- [BetterEnd r6](evidence/item-10/betterend-tags-r6/README.md): unresolved runtime
  tag population, not proof of false tag membership or zero density. Do not tune
  frozen tags or repeat failed fixtures without new causal evidence.

The integrated census CLI now combines registry starts, archive-bound placement
traces, exact family attribution, source grouping, saved-content dispositions,
classification, spatial summaries and actual-anchor biomes. Reuse the
[urn integration](evidence/item-10/urn-pilot-r1/README.md#integrated-offline-analysis)
for its complete command, current output hash and diagnostic limits. It retains
1,291 attempts and 429 saved block matches; eight locations are observed in 81
full Overworld chunks (one T0 registry start and seven provisional T1 caches).
All seven cache anchors have saved biome attribution. This is a diagnostic,
not the full Item 10 sample or proof of complete observer coverage.

The [protocol](evidence/item-10/protocol.md) records the implemented rules:
exact 40-family nonregistry membership and six ambient exclusions; explicit
unknown/disconnected-template handling; refused/exception/zero-content outcomes;
source and arena-component grouping; shared-content overlaps; manifest-bound
saved states; and in-frame ordinary-generation location observations. Collector
coverage includes the pillar helpers, BetterEnd erosion/repair and End routes.
End lifecycle accessors remain separate; no arrival/dragon campaign is required.
Fairy cleanup uses raw site 1, not bytecode offset 193; observed flower states do
not establish complete ring visibility. Do not require new positive tiny pilots.

The full runner pins the observer source/JAR, arm/repetition and eleven fixed
selections. `--all-strata` applies `item10-observer-coverage-v2` (see protocol);
single-stratum full analysis must pass `--require-complete-observer`. Provider
metadata and completion validation remain strict. See protocol for identities.
Chunky requests 65 by 65 chunks per selection; the census excludes the positive
edge to retain the frozen 64 by 64 frame. Control materialization verifies the
full baseline before omitting only Sparse Structures, with unchanged configuration.
Full measurements, paired/biome/seed comparisons, durable custody, the consolidated
PR review/merge and Items 2 through 10 audit remain the delivery scope.

## Current full-sample block

Six of sixteen worlds have individual census and raw-custody acceptance:

- [Ordinary r1 baseline](evidence/item-10/full-ordinary-r1-baseline/README.md).
- [Ordinary r1 control](evidence/item-10/full-ordinary-r1-without-sparse/README.md).
- [Ordinary r2 control](evidence/item-10/full-ordinary-r2-without-sparse/README.md).
- [Ordinary r2 baseline](evidence/item-10/full-ordinary-r2-baseline/README.md).
- [Mountainous r1 baseline](evidence/item-10/full-mountainous-r1-baseline/README.md).
- [Mountainous r1 control](evidence/item-10/full-mountainous-r1-without-sparse/README.md).

The fifth census (session `22204`, terminal 0) passed in 10m38.455s using
`760aa2f5`. Output SHA-256:
`bb0f1eeb9f638f050541bf1cb1ee88b4abbbba51ead99264bb77b7962a50f149`.
All 45,056 selected chunks passed. Its record retains the original gateway
coverage rejection, the JVM fixture finding and the coverage-v2 correction.
The frozen observer JAR is archive-bound; 49 captured targets plus the unused
Gateway target pass the corrected rule. No observer or configuration changed.
Full Item 7/10 suite: 548 passed in 173.38s; two subsequently added archive-binding
cases pass in the focused 41-test run. Fifth-world acceptance is pushed at
`3fa7f311`; sixth-world acceptance is pushed at `1632e3de`.

Mountainous Overworld has 4,039 locations, including 3,784 observed cave-urn
caches, but only six provisional T2 dungeons. Two content mismatches remain
excluded. Do not translate those counts into observed gameplay. Per-world
commands, complete category counts, failures, biomes, spatial outputs and custody
are linked above; final cross-seed/repetition synthesis remains pending.
The fifth and sixth working footprints are about 1.98 and 2.06 GiB. Latest free
space is about 33.1 GiB; continue checking costs against the roughly 30 GiB plan.

[Mountainous r1 control](evidence/item-10/full-mountainous-r1-without-sparse/README.md)
finished from `3fa7f311` in 666.194s; session `9871` is terminal 0. Configuration
and published/downloaded/restored raw custody pass (313 raw and 501 world files).
Its census (session `61273`, terminal 0) passed in 10m17.617s, SHA-256
`ced960a70c4c34581b19c68b2bdcbf76f003894191ae62537aa1a85072e968b7`.
All 45,056 chunks and 50 observer classes pass. The record retains three content
exclusions and the matched contrast: Overworld T2 6 to 22, T3 2 to 7, total
locations 4,039 to 4,083. Do not infer a global ratio from this one pair.
[Mountainous r2 control](evidence/item-10/full-mountainous-r2-without-sparse/README.md)
finished from `1632e3de` in 663.491s; session `23508` is terminal 0. Configuration
and published/downloaded/restored raw custody pass (313 raw and 501 world files).
Its census is active as session `95707`. Poll that handle and record the complete
result and repetition comparison before acceptance. No server is active.
Next run mountainous r2 baseline,
followed by the ocean-heavy and biome-diverse blocks in the frozen order. Use
fresh hash-verified materializations and existing custody/census paths. Complete
the remaining ten worlds, final synthesis, consolidated PR review/merge and
Items 2 through 10 audit. Do not create another tooling PR or Item 11 work.

Two local free-roaming/task servers are stopped and preserved. Official launcher
profiles and matching client files are prepared; first client launch/join remains
unverified. [Setup evidence](evidence/item-10/server-setup/README.md) is operational
context, not Item 10 measurement acceptance. Keep this handoff concise in place.
