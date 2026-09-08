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

Pause new experiments and new PR creation. Follow the
[exit-gate reassessment](evidence/item-10/README.md#exit-gate-reassessment-2026-09-08).
Natural positive capture for every generator is not an Item 10 requirement.
Preserve failed/unmet pilots without making them prerequisites for more tiny
pilots. Complete observation, correct location numerators, the full fixed sample,
required comparisons, raw custody, uncertainty and final review remain mandatory.

Finish existing review obligations, then consolidate the remaining implementation,
full measurement, report and audit into one delivery PR with coherent commits.
Prioritize completed exit requirements over new tools or per-generator milestones.
The [protocol](evidence/item-10/protocol.md) remains DRAFT for full sampling.
Its proposed 720,896 selected chunks, four seeds, eleven strata, two repetitions
and two arms are method choices, not specification-mandated sample sizes. The
user confirmed retaining the original 16-world plan and roughly 30 GiB storage
budget. No full-frame run has started; do not reduce to eight worlds.

Storage capacity is now available: direct `df -B1` reports 49,406,545,920 bytes
(about 46 GiB) free after authorized library deduplication and uv cache cleanup.
The side task reports `uv cache clean` exited 0, removing 38 GiB of disposable
cache while preserving installed environments and project artifacts. Dependency
operations may resume. The original 16-world plan and roughly 30 GiB working
budget are retained by explicit user decision. See the
[cleanup outcome](evidence/item-10/server-setup/README.md#additional-duplicate-cleanup).
The existing proxy estimates 10.71 generation hours and 13.50 GiB of original
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

Pillar entrypoints, fill anchors and delegated writes, plus BetterEnd terrain
merge, ship erosion and block-repair writes now have focused collector coverage,
including retained-class transforms. End entrypoints, template/direct writes and
accessor context are now integrated too; all 77 collector tests pass.
The [pillar boundary](evidence/item-10/protocol.md#betterend-procedural-pillar-write-boundary)
records implementation and its limits. Full-sample reader integration remains.
End route applicability is resolved in the
[protocol](evidence/item-10/protocol.md#end-generation-and-lifecycle-applicability):
retain ordinary packaged feature routes and report lifecycle invocations separately.
No arrival/dragon/respawn campaign is required. Full-sample reader integration,
occurrence aggregation and saved-world corroboration remain.
Spatial analysis now supports actual traced anchors while preserving all eleven
retained pilot spatial category results. Its focused spatial/census gate has
29 passing tests. The existing trace tool now streams hash-bound complete attempts
with full event fields and structural pairing; 88 reader tests pass, including
the retained Bridge/Extras archives. Family attribution now joins exact classes
and template paths to all 40 accepted nonregistry families, with 57 focused tests
passing. Six existing ambient exclusions are integrated; an observed disconnected
house fails as an inventory conflict. Attribution does not imply placement success.
The full reader now binds retained incoming-class bytes before yielding attempts;
91 collection/retained-trace tests pass. Provider-specific success, the complete
full-protocol observer identity set and the location table remain.
Ordered attempt outcomes now retain last successful writes, content surviving
erosion, exceptions and actual anchors. The 35 attribution/collection tests pass
against retained urn observations. These are not accepted locations: provider
completeness, fairy visibility and saved-world corroboration remain. Candidate
aggregation now groups common sources, retains halo/zero outcomes and exposes
content overlaps; 68 focused tests pass, including retained spiral source counts.
Overlap dispositions and final acceptance still gate density numerators.
Saved-content lookup now binds requested coordinates to retained world-file hashes
under the existing world lock. Its 17 focused tests reproduce retained urn saved
states; the shared diagnostic's 429-write JSON is unchanged. Candidate acceptance
must still bind custody, provider rules and these observations together.
The census CLI now integrates archive-bound traces, groups and saved checks via
paired `--trace-root`/`--trace-manifest`. The retained
[urn integration](evidence/item-10/urn-pilot-r1/README.md#integrated-offline-analysis)
reproduces all 1,291 attempts and 429 block matches with identical output hashes.
Its 18 focused tests pass. This is diagnostic integration, not full measurement.
The biome reader now supports actual within-chunk traced anchors, with 40 focused
biome/spatial/census tests passing. Final location-table integration remains.
Genuine remaining capabilities: complete
nonregistry occurrence identity, coordinate inclusion and biome integration;
exact omit-only-Sparse-Structures materialization; full sampling and final analysis.
Source descriptions do not supply missing occurrence measurements. Traced blocks,
template parts and halo activity are not already accepted location numerators.
Do not turn remaining collector work into standalone experimental campaigns
or tooling PRs.

Two local free-roaming/task servers are stopped and preserved. Official launcher
profiles and matching client files are prepared; first client launch/join remains
unverified. [Setup evidence](evidence/item-10/server-setup/README.md) is operational
context, not Item 10 measurement acceptance. Keep this handoff concise in place.
