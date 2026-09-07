# mcpack current handoff

Updated: 2026-09-08. This is the single active continuation checkpoint.

## Authority and reading order

Read [AGENTS.md](AGENTS.md) for standing instructions and
[SPECS.md](SPECS.md) for dependency-ordered requirements. Use the
[execution ledger](Adventure-Engineering-Pack-Execution-Ledger.md) for status
vocabulary and decisions, checking dated status against current delivery evidence.
Read [infrastructure instructions](INFRASTRUCTURE-INSTALLATION-AND-SERVER-TESTING.md)
before infrastructure installation or server testing.

The [previous handoff archive](docs/history/MCPACK-HANDOFF-2026-09-07-ARCHIVE.md)
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
  `be64d458fee3539e5132049d871d1c32ebc3655b`.
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

## Item 9 current work and next action

The user authorized Item 9 end to end. Branch `codex/item9-classification`
contains all 448 provisional classifications and passes its focused local gate.
[Matrix](evidence/item-9/classification.md),
[rubric and evidence](evidence/item-9/README.md), and
[current report](docs/items/Item-9-Provisional-Structure-Classification.md)
are authoritative. All five provider batches are committed and delivered;
final local-gate/report commit is `59ee0490`. Push the remaining checkpoint,
open the main PR, request `@codex review`, inspect completed reviews and all
comments, resolve valid findings, and repeat until clean. Merge only after the
clean final cycle, then verify main delivery and reconcile completion status.
Item 9 remains IN PROGRESS until those gates pass.

No Item 8 family assessment, measurement, preservation or PR18/PR19 delivery
work remains. Its accepted inventory and raw evidence were reused unchanged.
The old 21-family Item 9 report is superseded. No Item 10 work was performed.
After Item 9, Item 10 remains the next dependency, outside this task's scope.
The cross-item audit and human-observation restrictions for Item 11 remain
in AGENTS.md and SPECS.md.

## Local workspace to preserve

The checkout is `codex/item9-classification`, tracking its origin branch. Existing unstaged AGENTS.md edits and a CLOUD_HANDOFF.md deletion predate
this cleanup. Preserve their intent; do not restore or stage unrelated changes.
The existing shortened handoff is delivered with its byte-identical historical
archive; no new history consolidation or preservation experiment was performed.
Protected untracked artifacts include `.codegraph`, `.omo/` and
`mcpack-reconstructed-28(1).bundle`. Recheck status before any mutation or delivery.

## Maintaining this checkpoint

Update current sections in place. Keep this file roughly within 100 to 200 lines,
preferably shorter when sufficient. Link evidence rather than duplicating logs,
commands, per-batch reports or the ledger. Git preserves routine prior versions;
do not append a new checkpoint or create a new archive for every batch.
Requirement counters describe coverage, not commit or validation granularity.
Use coherent milestones and proportionate checks as defined in AGENTS.md.
