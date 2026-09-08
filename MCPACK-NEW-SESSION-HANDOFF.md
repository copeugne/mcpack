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

The observer source/JAR are now pinned in the full runner. Full census analysis
must use `--require-complete-observer` to require all 50 declared incoming classes
and matching installations. The provider reader now rejects the reproduced
missing/misattributed gateway metadata and incorrect completion events; retained
traces are unchanged. See protocol for hashes, derivation and focused checks.
The full applicable gate passed 535 Item 7/10 tests in 152.60 seconds. The existing
runner now accepts full sampling with explicit arm/repetition and rejects its
older uninstrumented control mode. Commands and operational timeout are in the
protocol. Next: run the first full ordinary baseline, verify all 50 actual
installations and selected saved chunks, preserve/restore raw custody, and
measure storage/runtime before proceeding to the other 15 worlds.
The shared harness now accepts the eleven fixed Item 10 generation selections.
Chunky's odd-width square requests 65 by 65 chunks; the fixed 64 by 64 census
excludes the positive edge. See protocol for the pinned bytecode derivation and
34 passing geometry/lifecycle checks. The control materialization now verifies
the full baseline before omitting only Sparse Structures. Its derived manifest,
deployed hash and focused preservation checks are in the protocol. No real
control boot or full collection has completed. Runner tests build the real collector
for both arms while substituting server execution.
Then confirm measured runtime/storage costs on the first full ordinary-seed run,
collect all frames with durable raw custody, complete paired/biome/seed analysis,
finish the consolidated PR review/merge and the Items 2 through 10 audit.
The first full run, `full-ordinary-r1-baseline`, finished all eleven selections
and stopped cleanly after 497.453 seconds from generation source `7b977af6`.
Session `89854` is terminal. The original post-capture rejection is preserved:
the Item 7 allowlist omitted seven custom-dimension Chunky task files. The narrow
fix revalidated all 239 unchanged captured files without regenerating the world.
See [first full run](evidence/item-10/full-ordinary-r1-baseline/README.md) for the
original run receipt, recovery command, focused checks and initial sizes.
All 50 incoming classes and 28,908 complete attempts pass direct trace checks.
The stopped-world backup exists. Next: durable raw archive/restore and complete
saved-world census/location analysis. No second world may start before acceptance.
Do not create another tooling PR or Item 11 work.

Two local free-roaming/task servers are stopped and preserved. Official launcher
profiles and matching client files are prepared; first client launch/join remains
unverified. [Setup evidence](evidence/item-10/server-setup/README.md) is operational
context, not Item 10 measurement acceptance. Keep this handoff concise in place.
