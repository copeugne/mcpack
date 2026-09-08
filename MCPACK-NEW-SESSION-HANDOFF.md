# mcpack current handoff

Updated: 2026-09-08. This is the single active continuation checkpoint.
## Authority and reading order

Read [AGENTS.md](AGENTS.md) for standing instructions and
[SPECS.md](SPECS.md) for dependency-ordered requirements. Use the
[execution ledger](Adventure-Engineering-Pack-Execution-Ledger.md) for status
vocabulary and decisions, checking dated status against current delivery evidence.
Read [infrastructure instructions](INFRASTRUCTURE-INSTALLATION-AND-SERVER-TESTING.md)
before infrastructure installation or server testing.

The [previous handoff archive](https://github.com/copeugne/mcpack/blob/be64d458fee3539e5132049d871d1c32ebc3655b/MCPACK-NEW-SESSION-HANDOFF.md)
is preserved verbatim for targeted historical lookup only. Its commands, next
steps, counters and status claims are historical, not current instructions.
Relative paths inside that archive refer to the repository root. Do not read the
entire archive at startup or resume work merely because it appears there.

## Verified delivery checkpoint

- Item 8 is COMPLETE. Its inventory gate and reviewed delivery are recorded in
  [Item 8 evidence](evidence/item-8/README.md).
- [PR18](https://github.com/copeugne/mcpack/pull/18) merged as
  `326979dd2eee7da3f881f1316eb845fb16e8ea6b`, including reviewed head
  `2023a22a84372483841f7ad286a868584df564fa`.
- [PR19](https://github.com/copeugne/mcpack/pull/19), the delivery-status follow-up,
  is also merged. Its head is `ad65a6eb6c2e3f85746bd696296f177be6d2e87d`.
- Fetched `origin/main` at this checkpoint is
  `12c9bfd998e0704561e476d00518acbcd11f5301` after PR31.
- The accepted inventory accounts for 136 providers and 887 runtime roots,
  with 448 assessed active canonical families and 18 separately dispositioned
  inactive/excluded registry groups. These are different populations.
- The evidence report records 495 passing clean-checkout acceptance tests.
  This handoff cleanup does not rerun or replace that acceptance evidence.
- Items 9 through 11 were not performed in the Item 8 work.

## Where to find the result

- [Canonical inventory](evidence/item-8/inventory.json): accepted family records.
- [Family decisions](evidence/item-8/family-decisions.json): grouping and attribution.
- [Provider scope](evidence/item-8/provider-scope.md): provider dispositions.
- [Item 8 report](docs/items/Item-8-Baseline-Structure-Inventory.md): assessment summary.
- [Evidence and reproduction](evidence/item-8/README.md): delivery, test prerequisites,
  source references, limitations and validation commands. Use its latest delivery
  section rather than historical continuation prose lower in that file.
- [Preservation](evidence/item-8/preservation.md): backups, restore verification
  and history consolidation. Preserve those artifacts and recovery references.

## Item 9 completion and next dependency

Item 9 is COMPLETE. [PR20](https://github.com/copeugne/mcpack/pull/20) merged
reviewed head `5073af269d6e253edb0d314346d671acf7d294cf` as
`7cbe06c7d8b074fa6121c1143432d28d02996712`, verified in fetched main.
The final Codex cycle completed with a thumbs-up and no new findings.
[Matrix](evidence/item-9/classification.md),
[evidence and review dispositions](evidence/item-9/README.md), and
[current report](docs/items/Item-9-Provisional-Structure-Classification.md)
record all 448 classifications and the passing local gate. No classification,
measurement, Item 8 preservation or PR20 review work remains.

## Item 10 active work

PR21 merged the Item 9 completion records as `edd1dcf9`, verified against
GitHub metadata and fetched main on 2026-09-08. PR22 merged the methodology, setup and diagnostic
preparation as `0a1d9f8f6e0df266eb1f9e1080611c648babf2de`. The completed
Codex cycle reviewed `362a3e703be51f7487354f83149a7e6e3669f201`, posted no
findings and returned a thumbs-up; fetched main contains that exact head.
This is preparation delivery, not Item 10 completion.
[Item 10 evidence](evidence/item-10/README.md) records verified dependency hashes,
reusable evidence, missing measurements, proposed batches and resource estimates.
A [fresh registry diagnostic](evidence/item-10/pilot-r1/README.md) measured 24
starts in 3,969 selected Overworld chunks. Local and downloaded archives passed
restore verification; a restored-world census reproduced byte for byte. No Item 8
or Item 9 audit was repeated.

Before full experiments, freeze sampling, retention and measurement semantics.
Recheck storage before experiments. Apply the user-authorized automated scope in the
[authorized amendment](evidence/item-10/methodology-amendment.md); its narrow
Item 5 methodology gate is complete through reviewed PR22 main delivery.
The user requested local free-roaming and task servers for later login.
[Server setup](evidence/item-10/server-setup/README.md) records both separate
profiles and successful startup, correlated save and clean shutdown checks.
Both are stopped. Two official-launcher profiles contain 108 hash-verified JARs each. First Play may download assets; client launch and join
remain unverified. The observed-fight requirement is superseded by provisional encounter-site density. Sparse Structures is present with
spread factor 2; the historical absent-mod result is superseded context.
The 40 nonregistry families need occurrence coverage beyond structure starts.
The user rejected the long recorded-play plan and proposed combat logger. Both
are withdrawn; no capture or logger was started. Do not interpret the six-hour
availability or tentative ten-hour offer as an approved workload.
[Protocol reassessment](evidence/item-10/protocol.md) distinguishes spatial census
from actual combat. The authorized revision removes human collection in both
items; no recording or operator workload is deferred to Item 11.
[Decoder validation](evidence/item-10/decoder.md) records the custom-dimension
fix and raw-coordinate census. It now rejects incomplete denominators and
inconsistent starts. The accepted family/category join now covers all 24 pilot
starts, retaining confidence and ambiguity. Spatial diagnostics retain boundary
censoring, partial-cell denominators, clustering and empty rectangles; 41 focused
tests passed before the biome addition. Biome exposure now covers all 96
quart-height bands with 3,969 chunks each; 46 focused tests pass. Next complete nonregistry occurrence coverage and biome attribution,
then freeze the full sampling design and Sparse Structures control. The pilot does not close Item 10.
The [placement probe diagnostic](evidence/item-10/placement-probe.md) now passes
a synthetic preservation test and transforms the exact retained scarecrow class.
r1 had no eligible writer calls and is insufficient. r2 exercised the target
but failed helper classloading and timed out; its incomplete world is rejected.
The isolated-loader regression now passes with an explicit system-loader bridge.
r3 completed all four selections in 348.93 seconds with correlated flush and
clean exit. Its trace retains six complete attempts and 30 successful block
writes with no unfinished attempts. The fresh control also completed cleanly
in 366.501 seconds, with identical preflight and selections. Both content readers completed all 6,852 chunks. The declared equality gate
failed: central End matches; Overworld 3,969, Nether 960 and outer End 671 chunks
differ. Both worlds are stopped. The r3 498-file archive and both nested world restores
passed download verification and are durably published; see the placement diagnostic.
Accepted Item 7 already documents frozen-stack semantic nondeterminism, so this
pair cannot establish probe causality. That fact was missed during predeclaration.
Do not launch r4 to repeat the equality test. The prospective protocol now
separates collector correctness from established world variability. All 30
recorded scarecrow block IDs were corroborated in the restored world. Local
capture/preservation checks pass; observer-free equivalence remains unproven.
PR23 delivered the bounded diagnostic through merge
`eabc9ce30f731e9a3471267e09fff615293c1b26`, verified in fetched `origin/main`.
The [clean review](https://github.com/copeugne/mcpack/pull/23#issuecomment-5578556110)
completed on `73f25aed57bcdc952ea6d65a1c93ae92ff8dc9b2` with no new findings
and a Codex thumbs-up. All four valid findings from earlier cycles were fixed.
The placement diagnostic retains validation, raw custody and corrected typed
comparison evidence. All 64 control registry starts have biome attribution.
Item 10 remains IN PROGRESS; no nonregistry density counts are accepted.

## Current collector coverage and next batch

PR24 through PR31 are cleanly reviewed and merged. Authoritative results and
review records are in the linked reports:

- [BetterEnd diagnostics](evidence/item-10/placement-probe.md): retained r1 through
  r6 failures and source follow-ups. Positive template capture remains unmet.
  [Tag r6](evidence/item-10/betterend-tags-r6/README.md) distinguishes unavailable
  command lookup from false tag membership. Do not patch the frozen tags or rerun
  failed fixtures without new evidence about the runtime population mechanism.
- [BOP fixture](evidence/item-10/bop-fixture-r1/README.md): artificial positive
  capture and 22,769 saved block IDs. Excluded from density.
- [Monster Box](evidence/item-10/monster-box-pilot-r1/README.md) and
  [Nether spikes](evidence/item-10/nether-spike-pilot-r1/README.md): natural capture,
  archive-bound traces and saved block-ID corroboration pass.
- [Spiral](evidence/item-10/spiral-pilot-r1/README.md): six zero-write parts from one
  source; saved biome outside frozen allowlist. Positive capture remains unmet.
- [Fairy](evidence/item-10/fairy-run-r1/README.md): no helper calls in the fixed
  frame. Raw custody and mixed-trace validation pass, not positive capture.
- [Registry spatial pilot](evidence/item-10/pilot-r1/README.md): PR31 delivers
  combined actionable, encounter and village categories with unchanged raw data.

Current branch: `codex/item10-urn-coverage`. The
[urn pilot](evidence/item-10/urn-pilot-r1/README.md) completed cleanly; raw download
and both restores pass. The existing collector records parent placement identity
and actual write results. Its extended reader and saved-world inspector validate
all 429 mixed writes, including 161 urn writes at distinct coordinates. The
summary preserves 87 successful and 987 zero-successful-write patch attempts.
All 371 Item 7/10 tests pass; the final summary adjustment passes four affected
checks. Complete review/delivery of this bounded milestone next.

Do not count these raw totals as selected-area density. Full collection still
requires the remaining nonregistry mechanisms, occurrence inclusion, biome
attribution, exact Sparse Structures control and observer cost/storage checks.
The [protocol](evidence/item-10/protocol.md) remains DRAFT for the full frame.
Use accepted Item 8 mechanisms rather than repeating its inventory. Do not expand
fixed diagnostics to hunt for positive counts. The last prelaunch storage check
was 4.8 GiB free, below the provisional 5 GiB full-experiment floor.

After Item 10 delivery, audit Items 2 through 10 together. Do not implement,
run, repair or lint Item 11 workflows before the audit passes. The user removed
the human requirement for both items; automated proxies remain explicitly limited.

## Local workspace to preserve

The prior branch `codex/item9-delivery-record` remains pushed at `3f758cb2`.
That unmerged commit changes only the historical reference filename. Preserve it.
Inspect actual staged, unstaged and untracked state before mutation. A clean
checkout does not reproduce another workstation's uncommitted edits, deletions
or private backups; do not invent or recreate those changes from this handoff.
Preserve any existing local changes and archives. The local historical archive
at `docs/history/HISTORICAL-MCPACK-HANDOFF-2026-09-07-REFERENCE-ONLY.md` is not a tracked dependency;
the immutable link above supplies durable historical context.
Protected artifacts include `.codegraph`, `.omo/` and
`mcpack-reconstructed-28(1).bundle` wherever present. Do not stage or delete them.

## Maintaining this checkpoint

Update current sections in place. Keep this file roughly within 100 to 200 lines,
preferably shorter when sufficient. Link evidence rather than duplicating logs,
commands, per-batch reports or the ledger. Git preserves routine prior versions;
do not append a new checkpoint or create a new archive for every batch.
Requirement counters describe coverage, not commit or validation granularity.
Use coherent milestones and proportionate checks as defined in AGENTS.md.
