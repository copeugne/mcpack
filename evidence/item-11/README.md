# Item 11 automated route opportunities and repetition

Status: **IN PROGRESS; local exit gate PASS after visibility, cost and report corrections**.
Final Codex review and verified main delivery are governed by
[PR37](https://github.com/copeugne/mcpack/pull/37).
The [complete generated report](report.md) is the authoritative version 2 numerical result.
The [predeclared protocol](protocol.md), `item11-routes-v2`, defines every route,
capability, radius, window, denominator, failure rule and uncertainty boundary.
No Item 12 work was performed.

## Result and scope

All sixteen accepted Item 10 worlds were analyzed read-only: four seeds, two
repetitions and baseline/omit-Sparse arms. Four fixed 768-block Overworld transects
per world give 64 geometric routes and 192 route/mode evaluations. Each has
32/64/96-block radius sensitivity and 256/512/768-block prefix windows. Results
retain adjacent candidates, ray outcomes, saved top-cell observations, provisional
categories, gaps, censored boundaries, family repetitions and modeled costs.

At primary radius 64 and window 768, the baseline has 8,347 adjacent memberships,
20 ray-clear memberships and 1,160 covered blocks out of 24,576 sampled blocks.
Omit-Sparse controls have 8,771, 67 and 2,800 respectively. These are overlapping
route memberships, not unique world-location totals or human discoveries.
Zero projected first-repeat distances can arise from several candidate anchors
in a route's starting endcap. They are not instantaneous player encounters.

All 64 walking and 64 horse corridors are model-infeasible under the declared
straight-route, no-swimming, one-block-step assumptions. Boats have 16 model-feasible
and 48 infeasible routes. Every failed station and reachable prefix is retained.
This does not establish that walking or horses cannot explore these worlds:
detours, swimming, breaching and other capabilities are outside these scenarios.
The models do not validate collision shapes, cave navigation or actual travel.

Placement density is the accepted Item 10 quantity. Anchor adjacency, height-field
ray-clear targets and modeled accessibility are separate estimands. Registry
envelope-top targets are geometric proxies, not verified recognizable silhouettes.
Repetition is canonical-family repetition, not identical-layout repetition.
Human recognition, actual fights, meaningful-interaction time, enjoyment and human
Adventure Activity Ratio are **NOT MEASURED**. No gameplay quality threshold,
subjective satisfaction or population-level confidence interval is inferred.

## Dependencies and exact inputs

Item 10 and the Items 2 through 10 audit are delivered through PR35/36. Fetched
main was `5ec24115b9394ef162bdff6f65a31180dbb7d7ff` at startup. PR36's completed
clean review identifies `0201d5e7737ce033875a498317a8a470bcb1853e`, and its issue
reaction records the Codex bot thumbs-up at 2026-09-08 20:53:29 UTC. Main contains
that reviewed head. The prior Item 7 continuation exception remains unchanged.

Reuse [Item 10's complete evidence/custody index](../item-10/README.md),
[its protocol](../item-10/protocol.md), the
[exact identity audit](../item-10/cross-item-audit.md),
[448-family inventory](../item-8/inventory.json), and
[provisional classification](../item-9/classification.md). The accepted
[comparison index](../item-10/accepted-biome-comparisons.json.gz) supplies the exact
sixteen census names and SHA-256 values. Each result binds its census, archive
manifest, archive-bound world-backup manifest, protocol and analyzer hashes.

Frozen pins remain Minecraft 1.21.1, NeoForge 21.1.249, Temurin
21.0.12.1+1-LTS and construction heap `-Xms1G -Xmx4G`. The audit records exact
retained, instrumented baseline and omit-only control runtime identities and the
unchanged Item 6 configuration identity. No runtime tree was booted or tuned.
Existing restores pass complete file-inventory verification before and after
analysis under the Java-compatible POSIX lock. Operational `session.lock` is
excluded from preserved world content; no game-world bytes are changed.

The two prior housekeeping commits `1f70f395` and `022990e3` are preserved ancestors
in this branch and included in PR37. They were not claimed as PR36-reviewed main
delivery. Recovery refs, ignored archives, `.codegraph` and the reconstruction
bundle remain protected. No upstream audit, classification or world generation
was repeated.

## Implementation and preservation

[The analyzer](../../tools/analyze_route_opportunities.py) reuses Item 10's category
join and saved-block lookup, Item 7's Anvil/NBT and safe-file readers, and Item 4's
world lock and lock-excluding inventory enumeration. Missing route measurements
required only the fixed geometry, ray and transport models and their summaries.
[The report builder](summarize.py) consumes the existing producer digest records
and rejects incomplete/misbound matrices, including archive-manifest and backup
identity mismatches against committed Item 10 manifests. It keeps only the report view in memory;
raw observations remain in the checked result files. No new schema, archive
revision, generalized validator or storage service was introduced.

[All accepted compressed JSON results](results/) are committed, with exact digests
in the generated report and [original producer outputs](validation/full/).
They total 19,363,394 bytes. The sixteen accepted invocation times sum to 900.942
seconds, range 45.156 to 84.892 seconds; see [resource totals](validation/resource-totals-cost.txt).
Derivation: sum result sizes and each producer log's `real` minutes/seconds over
the sixteen names in the accepted comparison index. Diagnostics and clean-code
reproduction cost extra. Timings include normal cache effects and some concurrent
validation work; they are operational costs, not performance benchmarks. A pilot
process sample showed 256,372 KiB RSS, not a measured peak. Output and elapsed
costs fit the predeclared 1 GiB and provisional 160-minute allowances.

## Rejected attempts and correction

The [initial pilot](pilot/ordinary-r1.json.gz) was an interim result before adjacent
repeat-cost integration. The initial representative acceptance and two expansion
outputs were later rejected for a reproduced POSIX lock-release defect. They are
preserved under [rejected-lock-attempt](rejected-lock-attempt/), including the
[interrupted biome-diverse r2 log](rejected-lock-attempt/timing/full-biome-diverse-r2-baseline.txt).
The inventory reader opened and closed `session.lock` even while filtering it from
its result. Closing that descriptor released the process's POSIX lock.

The [failing competing-process probe](validation/lock-regression-before.txt)
reproduces the defect. The narrow fix reuses `_backup_paths` so the lock path is
excluded before opening; safe regular-file checks and exact full inventory
comparison remain. The [corrected focused suite](validation/lock-regression-after.txt)
passes. All sixteen worlds were then reanalyzed under corrected source `ff77c6f6`.
The [representative comparison](validation/corrected-pilot-comparison.txt) confirms
identical measurements, with only the analyzer identity changed. No original
world or Item 10 evidence was repaired. Raw failed-test whitespace is preserved.
Initial package-marker, syntax/type and shell quoting mistakes were corrected
before their dependent processing; they did not create accepted evidence.

Item 10's two rejected ocean-heavy control worlds remain excluded with their
original failure dispositions. The accepted route matrix uses the delivered
third-attempt r2 control, not a smaller or repaired failed world.

## Reproduction

Use the locked Python environment (`uv sync --locked`). To rebuild the report
from committed results alone, run the following into an absent output file:

```sh
PYTHONPATH=. uv run --no-sync python evidence/item-11/summarize.py \
  --results evidence/item-11/results --output /tmp/item11-report-rebuild.md
cmp evidence/item-11/report.md /tmp/item11-report-rebuild.md
```

To reproduce world-derived results, first follow the linked Item 10 per-world
restore and census commands. Default input locations are
`evidence/raw/item10/NAME-custody/restored-world/world`, adjacent
`restored-local/world-backup.json`, and `NAME-analysis/all-strata.json`.
The analyzer verifies their identities; existing source worlds are never booted.
The final cost-correction representative was ocean-heavy r1 without-Sparse. These are the
executed cost-correction commands (the scratch output paths must be absent):

```sh
uv run --no-sync python -m tools.analyze_route_opportunities \
  --name full-ocean-heavy-r1-without-sparse \
  --output evidence/raw/item11/cost-correction/full-ocean-heavy-r1-without-sparse.json.gz
uv run --no-sync python - <<'PYCODE' > /tmp/item11-cost-remaining.txt
from tools.analyze_route_opportunities import accepted_inputs
print('\n'.join(n for n in sorted(accepted_inputs()) if n != 'full-ocean-heavy-r1-without-sparse'))
PYCODE
while IFS= read -r name; do
  { time uv run --no-sync python -m tools.analyze_route_opportunities --name "$name" --output "evidence/raw/item11/cost-correction/$name.json.gz"; } > "evidence/raw/item11/cost-correction/$name.txt" 2>&1 || exit 1
  mv "evidence/raw/item11/cost-correction/$name.json.gz" "evidence/item-11/results/$name.json.gz"
  mv "evidence/raw/item11/cost-correction/$name.txt" "evidence/item-11/validation/full/$name.txt"
done < /tmp/item11-cost-remaining.txt
```

The representative output and timed producer log were promoted to the same
canonical paths after focused regression and comparison passed. Reproduction
must use distinct absent output/log paths; the `mv` commands above describe the
original integration, not permission to replace accepted evidence casually.

The version 1 clean tracked export of `ff77c6f6` with a separate `uv sync --locked` environment
[reproduced the representative bytes](validation/clean-reproduction.txt) in 52.475
seconds, SHA-256 `d59cc1ddfe3924ddef69e0efdde2d3477889401d7fd68fa16bcc12e13fd64672`.
It used the existing independently hash-checked raw restores; this is clean-code
reproduction, not a fresh-machine or new-download claim. The
[dependency log](validation/clean-sync.txt) records the exact Python/packages and
cross-filesystem copy fallback. No operational cache or downloaded binary is committed.

The earlier visibility-corrected clean tracked export of `1609ac96` and its separate locked environment
[reproduce the v2 representative byte for byte](validation/clean-reproduction-v2.txt)
in 55.553 seconds, SHA-256 `807a369277b3079559acaaa4f681951b78617af9b838f30797fdddf317039fb0`.
The [v2 environment log](validation/clean-sync-v2.txt) records dependency installation.
It uses the same accepted raw restores with independent inventory verification.

## Corrected local exit gate and delivery

| Requirement | Evidence and disposition |
| --- | --- |
| Declared routes/endpoints/capabilities | Original protocol committed at `7a12cff9`; corrected selection predeclared in v2 at `1609ac96`; full fixed 64-route matrix. PASS. |
| Failures and limitations | Every route/mode status, failed station, reachable prefix and rejected processing attempt retained. PASS. |
| Adjacent locations and geometric visibility | Hash-bound candidate joins, saved geometry and per-station ray outcomes in all sixteen results. PASS. |
| Required candidate categories | Ten overlapping/exclusive groups retain C/T1/T2/T3/T4, actionable, encounter, village and all-location counts, including zeroes. PASS. |
| Fixed-distance gaps and repetition | Three windows, ordered events, family IDs, zero ties, censored boundaries and intervals. PASS. |
| Geometric coverage | Explicit sampled covered-block numerator, full/prefix denominators and unknown-only coverage. PASS. |
| Modeled costs and uncertainty | Central/range speed assumptions, null infeasible completed costs, prefix and unconstrained costs, radius sensitivity and descriptive dispersion. PASS. |
| Measurement boundaries | Placement, ray geometry, accessibility and all NOT MEASURED human quantities remain distinct. PASS. |
| Reproducibility and custody | Complete before/after world inventories, preserved raw archives, competing lock regression, deterministic full report and clean-code representative reproduction. PASS. |
| Validation | Full applicable gate: [600 tests passed](validation/final-tests-v2.txt). After the final report fixes, [all 22 affected tests pass](validation/final-tests-category.txt), including per-route categories, report reproduction and world-provenance rejection. Final [Ruff](validation/final-ruff-category.txt), [formatting](validation/final-format-category.txt) and [BasedPyright](validation/final-types-category.txt) pass. |
| Final review and main delivery | PENDING through PR37. No completion claim before a clean final review, merge and fetched-main verification. |

Reproduce the final applicable checks with:

```sh
uv run --no-sync pytest -q tests/item7 tests/item10 tests/item11
uv run --no-sync ruff check tools/analyze_route_opportunities.py evidence/item-11/summarize.py tests/item11
uv run --no-sync basedpyright tools/analyze_route_opportunities.py evidence/item-11/summarize.py tests/item11
```

Manual surface inspection checked the generated per-world and per-route tables
against raw candidate, ray, category and failure records, including the ordinary
water corridors and biome-diverse dry-route obstacles. No gameplay observation
is inferred. The next action is the required PR37 review/fix/merge loop, not Item 12.


## PR37 visibility correction

[Finding 3962853986](https://github.com/copeugne/mcpack/pull/37#discussion_r3962853986)
is valid. The version 1 analyzer filtered the visibility population through
anchor adjacency and projection windows. The retained desert outpost at anchor
(216,328), target (207.5,112,319.5), has anchor distance 72 but ray-clear distances
63.5963835449784 and 63.65924913160695 at stations 588 and 596 on biome-diverse r1
control / east-north. It was omitted at radius 64. Anchors beyond 96 were also
dropped before their targets could be tested.

The narrow fix uses independent candidate-category populations: anchor geometry
for adjacency, target/ray eligibility at sampled stations for visibility. It also
retains eligible targets whose anchors exceed the maximum radius. Routes,
endpoints, worlds, all radii/windows, target/ray definitions, transport models and
configuration are unchanged. This repairs the demonstrated omission within the
existing analyzer and result format. No new evidence class, schema, validator,
archive revision or scope expansion is needed. Protocol version 2 records the
corrected selection rule before corrected extraction.

[Three regressions fail before the fix](validation/visibility-regression-before.txt):
the retained outpost, a target with anchor beyond 96, and visibility inside a
prefix whose anchor projects beyond its endpoint. All eleven core route tests
[pass after the fix](validation/visibility-regression-after.txt). The corrected
representative is the actual biome-diverse r1 control counterexample. Its
[comparison](validation/visibility-pilot-comparison.txt) preserves every adjacency,
transport and top-cell observation. East-north visible membership changes 7 to 8
and covered blocks 160 to 176; the other primary route counts are unchanged.
The corrected invocation takes 48.654 seconds and produces 1,877,092 bytes.
This fit the existing budget before the remaining fifteen analyses proceeded.
All sixteen corrected results are now integrated with their producer identities.

All rejected version 1 results, producer logs, report and protocol remain durably
preserved at immutable reviewed commit `506bc4fd4d9efd2f216f7b59c47b95b0fa1c38b3`.
For example, `git show 506bc4fd:evidence/item-11/report.md` retrieves that rejected
report. Current paths are replaced only by freshly reproduced version 2 derived
results with their new identities; raw Item 10 worlds/censuses remain unchanged.
The corrected matrix, report and final validation pass. The fresh Codex review
and verified main delivery remain open.

The [complete matrix comparison](validation/visibility-matrix-comparison.txt)
checks the same sixteen `results/NAME.json.gz` paths against immutable `506bc4fd`:
`top_cells`, each `routes[route].transport`, and every `summaries[].adjacent` are
identical after matching radius/window/category keys. The 158 changed summary
rows have different `geometric_visible` or `covered_blocks` fields across the
three radii, three windows and ten overlapping categories. This is a direct
comparison of retained JSON values, not additional world measurement.
At the primary radius/window, control ray-clear memberships increase 61 to 67
and covered blocks 2,464 to 2,800; the baseline primary totals are unchanged.
All source worlds, census inputs, routes and transport observations are unchanged.

The completed review of `24aa6af0` found one stale protocol label in ledger
STAT-004 ([finding 3963074296](https://github.com/copeugne/mcpack/pull/37#discussion_r3963074296)).
It is valid and corrected to `item11-routes-v2`. Direct inspection confirms the
ledger, protocol, analyzer, result identities and report builder now name v2.
This documentation-only correction does not invalidate the 600-test final gate
or require repeating derived analysis. Fresh Codex review remains required.

## Completed-cost correction

[Finding 3963125325](https://github.com/copeugne/mcpack/pull/37#discussion_r3963125325)
is valid. For ocean-heavy r1 control / east-south, boat mode is INFEASIBLE with
reachable prefix 756. The old summary emitted completed costs for windows 256
and 512, contradicting the existing protocol's MODEL_FEASIBLE-only rule. The
narrow fix gates `completed_cost` on the full route/mode status. Reachable-prefix
and unconstrained costs continue to describe the supported partial window.

The retained-world regression [fails before](validation/cost-regression-before.txt)
and all twelve route tests [pass afterward](validation/cost-regression-after.txt).
No protocol or sampling rule changes: this brings implementation into agreement
with the existing v2 requirement. All pre-cost-fix results, logs and report remain
preserved at reviewed commit `e52353ab148c91319e22b613917375d5777e6b8a`.
The actual ocean-heavy r1 control counterexample was rerun first, comparing all
other raw and summary fields, followed by the other fifteen read-only analyses through
the existing source-hash-bound analyzer. The prior complete pass took 894.423
seconds and retained 19,364,996 bytes, within the existing 160-minute/1-GiB budget.
This repairs one field within the existing path. No new result class, schema,
validator, archive or transformation framework is needed.

The [complete cost comparison](validation/cost-matrix-comparison.txt) checks the
same sixteen `results/NAME.json.gz` values against immutable `e52353ab`.
Remove `inputs.analysis_sha256` and each route/window/category/mode's
`completed_cost` from both decoded objects: the remaining objects are identical.
All 660 changed completed costs were non-null and are now null for a mode whose
full-route status is not MODEL_FEASIBLE. Every raw observation, other cost,
visibility result, category, gap, repetition and route status is unchanged.
The generated report's numerical tables are unchanged; only result hashes change.

The final clean tracked export of `f4e99bdf` with a separate locked environment
[reproduces the cost-corrected representative exactly](validation/clean-reproduction-cost.txt)
in 55.220 seconds, SHA-256 `4c3e24391c5d982b11c6ac716561b70db84af85bfbd65a6a02202aaf53e88e46`.
The [environment log](validation/clean-sync-cost.txt) records installation. As before,
the existing accepted raw restores are independently hash-checked read-only inputs.

Final validation after the cost fix reruns all affected Item 11 tests:
`uv run --no-sync pytest -q tests/item11` gives 19 passed in 17.51 seconds.
The earlier complete applicable gate gives 600 passed in 196.80 seconds.
The cost change does not affect Item 7/10 readers or custody; those unchanged
checks are not repeated solely for reassurance. Final affected lint, formatting
and type checks pass. The local exit gate is restored; a fresh completed clean
Codex review and verified main merge remain required.

## Report integration and provenance corrections

The completed review of `56b925f2` found two valid report defects:
[numerical costs omitted](https://github.com/copeugne/mcpack/pull/37#discussion_r3963289055)
and [world provenance not checked](https://github.com/copeugne/mcpack/pull/37#discussion_r3963289058).
The cost measurements already existed in all accepted results; they were available
but not integrated in the authoritative report. The report now shows completed,
prefix and unconstrained travel-time ranges plus adjacent/visible repeated-family
interval counts, medians, central ranges and speed envelopes for all 192 primary
route/mode rows. Nulls, zero ties, right censoring and unconstrained costs stay
explicit. Other category/window/radius details remain linked in the raw results.

The existing report builder also compares both recorded world-provenance hashes
with each committed Item 10 archive manifest and its `world-backup.json` entry.
It reuses the existing archive model and producer identity checks. No new schema,
validator framework or world processing is needed. All sixteen final result files
and producer logs are unchanged from `17ccd330`; the builder accepts their exact
world identities and rebuilds the report deterministically.

[Three regressions fail before the fix](validation/report-regression-before.txt),
and [all 22 affected tests pass](validation/final-tests-report.txt) in 28.69 seconds.
The numerical surface check includes the feasible ordinary boat cost 96.00
[76.80,128.00] seconds and the infeasible ocean boat's null completed cost with
94.50 [75.60,126.00] prefix seconds. Ordinary east-north's 59 adjacent repeat
intervals have central median 0.75 seconds, central range [0,18] and speed envelope
[0,24], explicitly modeled rather than human observations. The
[focused numerical regression](validation/report-numerical-regression.txt) checks
these retained values. The initial regression log is also preserved; the two
provenance cases were tightened to fail immediately if the first misbound result
was accepted, avoiding an unrelated later-world error masking the omission.

The completed review of `7dd94a65` identified
[missing per-route category reporting](https://github.com/copeugne/mcpack/pull/37#discussion_r3963365255).
The finding is valid: the values existed in retained summaries, while the report
aggregated the required category memberships by world. The report now contains
all 64 routes with all-location, actionable, encounter, T2, T3, T4 and village
adjacent counts, ray-clear counts and covered-block numerators, each with the
explicit 768-block denominator. Zeroes and overlapping categories remain clear.
The [retained-route regression fails before](validation/category-report-before.txt)
this integration; it checks the distinct ordinary control east-north village and
east-south dungeon profiles. No source results, protocol or measurement changes.

The final category-integrated report passes [all 22 affected tests](validation/final-tests-category.txt)
in 28.35 seconds, including exact report reproduction, provenance rejection and
the retained numerical/category checks. Final lint, formatting and types pass.
The local exit gate remains PASS; fresh clean review and verified main delivery
are still required.
