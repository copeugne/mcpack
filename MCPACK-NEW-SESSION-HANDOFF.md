# mcpack current handoff

Updated: 2026-09-09. This is the single active continuation checkpoint.

## Authority and preservation

Read [AGENTS.md](AGENTS.md), [SPECS.md](SPECS.md), and the
[execution ledger](Adventure-Engineering-Pack-Execution-Ledger.md). Read
[infrastructure instructions](INFRASTRUCTURE-INSTALLATION-AND-SERVER-TESTING.md)
before server or infrastructure work. Verify dated claims against Git and evidence.
GitHub `copeugne/mcpack` and fetched `origin/main` are delivery authority.

The user authorized committing the AGENTS.md changes, CLOUD_HANDOFF.md deletion
and this completion checkpoint. Preserve the ignored local `.codegraph`, `.omo/`,
`mcpack-reconstructed-28(1).bundle`, backups and all existing evidence.
The local archive `docs/history/HISTORICAL-MCPACK-HANDOFF-2026-09-07-REFERENCE-ONLY.md`
is ignored and unchanged. Never stage it or use it as startup instructions.
The prior `codex/item9-delivery-record` remains pushed at `3f758cb2`, with only
an unmerged historical-reference rename. Preserve that reference. Git preserves
prior active handoffs; consult historical context only for specific open questions.

## Current delivery gate

Branch: `codex/item11-route-opportunities`. PR37 is the current delivery PR:
https://github.com/copeugne/mcpack/pull/37 . Its final report/closure commit follows
measurement head `28d544b8`; use current Git/PR head metadata for the exact candidate.
Last verified main remains `5ec24115b9394ef162bdff6f65a31180dbb7d7ff` (merged PR36).
Item 10 and the Items 2 through 10 audit are COMPLETE through reviewed PR35/36.
The two prior housekeeping commits `1f70f395` and `022990e3` are preserved ancestors
and included in PR37; they were not PR36-reviewed main delivery.

Item 11: local exit gate PASS after visibility, completed-cost and report corrections.
The [numerical report](evidence/item-11/report.md),
[protocol](evidence/item-11/protocol.md) and
[closure/reproduction record](evidence/item-11/README.md) are authoritative.
All sixteen accepted worlds provide 64 fixed routes and 192 transport evaluations,
retaining failures, categories, gaps, repetitions, costs, censoring and sensitivity.

PR37 findings are dispositioned: visibility selection (3962853986) fixed in
`1609ac96`; stale ledger protocol (3963074296) fixed in `e52353ab`; completed costs
for infeasible modes (3963125325) fixed in `f4e99bdf`. The final full matrix/report
is pushed at `17ccd330`. Compared with `e52353ab`, only analyzer identities and
660 completed-cost fields change; every other raw/summary value is identical.
Rejected versions remain in Git at `506bc4fd` and `e52353ab`. The earlier rejected
POSIX lock attempt remains under `evidence/item-11/`; the existing lock fix is
preserved. No original worlds were regenerated, tuned or repaired.

Validation: full applicable gate 600 passed in 196.80 seconds before the narrow
cost fix; all 19 affected Item 11 tests pass in 17.51 seconds afterward. The later report-only fixes pass all 22 affected tests; the final all-modeled-times report passes in 26.71 seconds. Final
lint/types/formatting pass. A clean export of `f4e99bdf` with a separate locked
environment reproduces the final representative bytes. No repeat of unchanged
Item 7/10 checks is needed for the isolated summary-cost change.

The completed review of `56b925f2` found omitted numerical report costs
(3963289055) and unchecked report world provenance (3963289058). Both are fixed
in the existing report path using retained evidence. All sixteen result files
and producer logs remain unchanged from `17ccd330`; no new world analysis.

The completed review of `7dd94a65` found per-route category counts missing from
the report (3963365255), though retained in JSON. The report now integrates all
64 routes with required category counts and geometric coverage. Raw evidence
is unchanged.

The completed review of `8cad4c41` found omitted UNKNOWN visibility reporting
(3963434898). Retained UNKNOWN-only numerators are now explicit per route/category
and radius/window sensitivity, with denominators. All current values are zero;
no raw data changed.

The completed review of `b2b59760` found missing report failure reasons
(3963504006) and full category/window gap/repetition statistics (3963504008).
These are retained values awaiting report integration, not missing measurements.
The existing report builder now emits reason-code sets and a full statistics
appendix. The appendix has 16 x 4 x 3 x 3 x 10 x 2 = 11,520 rows. This directly
serves the protocol/SPECS reporting gate and remains within the 1-GiB output
budget. The 1,498,235-byte generated report expansion is isolated; no new schema, tool framework
or source/world processing is justified.

The completed review of `9b83183c` found missing reachable-prefix coverage
reporting (3963575258). The existing report now exposes all 5,760 category/window
rows with three modes, including explicit undefined 0/0 ratios. The final report
is 1,821,556 bytes and its generated expansion is isolated. This integrates
retained evidence only; no new measurement or framework.

The completed review of `b6d08dff` found nonprimary modeled repeat-time ranges
missing from the report (3963622347). Reassessment: the report view must preserve
the complete existing cost contract for the fixed category/window matrix, rather
than discarding fields as a memory optimization. The same builder now summarizes
all adjacent/visible interval-time arrays before releasing them and emits all
completed/prefix/unconstrained costs with the existing coverage rows. This directly
serves SPECS Item 11 and protocol cost/reporting requirements, without new data,
schema, framework or measurements. The 4,506,694-byte generated report expansion stays isolated.

Next action: request fresh `@codex review` on the pushed final PR37 candidate.
Complete the review/fix loop, obtain the current-head clean result, merge and
verify fetched main before declaring Item 11 COMPLETE. Do not repeat upstream
collection/audits or start Item 12.

Human recognition, actual fights, interaction time, enjoyment and human Adventure
Activity Ratio remain NOT MEASURED. Automated geometry/model results are not human
observations. The prior Item 7 final-review continuation exception remains explicit.

## Completed measurement and authoritative evidence

Item 8 is COMPLETE through merged PR18/19; Item 9 through merged PR20 and
completion records in merged PR21 (`edd1dcf9`). Reuse the
[448-family inventory](evidence/item-8/inventory.json),
[Item 8 evidence](evidence/item-8/README.md),
[completed classification](evidence/item-9/classification.md), and
[Item 9 evidence](evidence/item-9/README.md). Do not repeat their audits or collection.
Exact dependency identities and reusable Item 5/7 evidence are in
[Item 10 README](evidence/item-10/README.md#verified-dependencies-and-delivery).
PR23 through PR34 delivered collector/analysis increments, not full Item 10.
All their review obligations are resolved in their linked delivery records.

The [Item 10 report](evidence/item-10/README.md) is the authoritative result,
with the complete world index, category/spatial/biome/seed contrasts, limitations
and requirement-by-requirement local exit gate. The
[protocol](evidence/item-10/protocol.md) remains `item10-full-v1`, observer coverage
`item10-observer-coverage-v2`, and retry policy `item10-retry-policy-v2`.
The frozen runtime, configuration, observer, seeds and 64 by 64 census frames
are unchanged. Controls omit only Sparse Structures after baseline verification.

All five user-authorized planned worlds and the
[final fresh ocean-heavy r2 control](evidence/item-10/full-ocean-heavy-r2-without-sparse-attempt3/README.md)
passed. The original target is fulfilled: sixteen accepted worlds, eight pairs,
176 strata and 720,896 full selected chunks across eighteen attempts.
The [heap failure](evidence/item-10/full-ocean-heavy-r2-without-sparse/README.md)
and [save-failure retry](evidence/item-10/full-ocean-heavy-r2-without-sparse-attempt2/README.md)
remain rejected and preserved with immutable raw custody and tested restores.
Do not repair those worlds, tune configurations or erase failed attempts.

The complete biome comparison has 68,217 height/biome rows, 18 unavailable
anchors and five positive zero-exposure rows. The tracked reproduction function
verifies all sixteen accepted input hashes, count conservation and exact bytes.
The strengthened collection reader accepts all sixteen archive-bound raw traces,
including all 41 legacy Scarecrow attempts. Raw observations and censuses did not
change during review fixes. Density is not observed fights or experienced pacing.

## Operational context

No server or world-generation process was started for Item 11. Existing local
server/client setup remains operational context, not acceptance evidence. Original
Item 10 worlds and failed attempts remain under their immutable custody. No new
archives, history consolidation or infrastructure rollout are needed for Item 11.
The clean-code export at `/tmp/mcpack-item11-clean-jZCYoWsn` is retained local
reproduction context; accepted proof is committed under `evidence/item-11/`.
