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
  `0a1d9f8f6e0df266eb1f9e1080611c648babf2de` after PR22.
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
GitHub metadata and fetched main on 2026-09-08. Item 10 work is now on
`codex/item10-density`. PR22 merged the methodology, setup and diagnostic
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
About 15 GiB is now free after authorized cleanup and client setup. The user now requires no human phase in either Item 10 or Item 11. Apply the
[authorized amendment](evidence/item-10/methodology-amendment.md); its narrow
Item 5 methodology gate is complete through reviewed PR22 main delivery.
The user requested local free-roaming and task servers for later login.
[Server setup](evidence/item-10/server-setup/README.md) records both separate
profiles and successful startup, correlated save and clean shutdown checks.
Both are stopped. Two official-launcher client profiles are installed with 108
hash-verified JARs each. First Play may download assets; client launch and join
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
r1 installed and shut down cleanly but had no eligible biome exposure or writer
calls, so it is insufficient. r2 is predeclared on the mountainous seed using
existing Item 7 eligibility evidence; run its control only after actual writer
execution and capture health pass. No nonregistry counts are accepted yet.

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
