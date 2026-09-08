# Item 11 automated route opportunities and repetition

Status: **IN PROGRESS; local exit gate REOPENED by PR37 finding 3962853986**.
The numerical report and complete-matrix claims below describe rejected version 1
until the corrected version 2 matrix is integrated. Final Codex review and verified
main delivery are governed by [PR37](https://github.com/copeugne/mcpack/pull/37).
The [complete generated report](report.md) is the authoritative numerical result.
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
Omit-Sparse controls have 8,771, 61 and 2,464 respectively. These are overlapping
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
and rejects incomplete/misbound matrices. It keeps only the report view in memory;
raw observations remain in the checked result files. No new schema, archive
revision, generalized validator or storage service was introduced.

[All accepted compressed JSON results](results/) are committed, with exact digests
in the generated report and [original producer outputs](validation/full/).
They total 19,351,171 bytes. The sixteen accepted invocation times sum to 896.573
seconds, range 45.509 to 85.163 seconds; see [resource totals](validation/resource-totals.txt).
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
The executed representative command was:

```sh
uv run --no-sync python -m tools.analyze_route_opportunities \
  --name full-ordinary-r1-baseline \
  --output evidence/item-11/results/full-ordinary-r1-baseline.json.gz
```

It was followed by the executed remaining-world loop. Existing output paths are
refused; point `--output` and timing redirects at absent paths for another run.

```sh
uv run --no-sync python - <<'PY' > /tmp/mcpack-item11-remaining.txt
from tools.analyze_route_opportunities import accepted_inputs
print('\n'.join(n for n in accepted_inputs() if n != 'full-ordinary-r1-baseline'))
PY
while IFS= read -r name; do
  { time uv run --no-sync python -m tools.analyze_route_opportunities --name "$name" --output "evidence/item-11/results/$name.json.gz"; } > "evidence/item-11/validation/full/$name.txt" 2>&1 || exit 1
done < /tmp/mcpack-item11-remaining.txt
```

A clean tracked export of `ff77c6f6` with a separate `uv sync --locked` environment
[reproduced the representative bytes](validation/clean-reproduction.txt) in 52.475
seconds, SHA-256 `d59cc1ddfe3924ddef69e0efdde2d3477889401d7fd68fa16bcc12e13fd64672`.
It used the existing independently hash-checked raw restores; this is clean-code
reproduction, not a fresh-machine or new-download claim. The
[dependency log](validation/clean-sync.txt) records the exact Python/packages and
cross-filesystem copy fallback. No operational cache or downloaded binary is committed.

## Local exit gate and delivery

| Requirement | Evidence and disposition |
| --- | --- |
| Declared routes/endpoints/capabilities | Protocol committed at `7a12cff9`, before extraction; full fixed 64-route matrix. PASS. |
| Failures and limitations | Every route/mode status, failed station, reachable prefix and rejected processing attempt retained. PASS. |
| Adjacent locations and geometric visibility | Hash-bound candidate joins, saved geometry and per-station ray outcomes in all sixteen results. PASS. |
| Required candidate categories | Ten overlapping/exclusive groups retain C/T1/T2/T3/T4, actionable, encounter, village and all-location counts, including zeroes. PASS. |
| Fixed-distance gaps and repetition | Three windows, ordered events, family IDs, zero ties, censored boundaries and intervals. PASS. |
| Geometric coverage | Explicit sampled covered-block numerator, full/prefix denominators and unknown-only coverage. PASS. |
| Modeled costs and uncertainty | Central/range speed assumptions, null infeasible completed costs, prefix and unconstrained costs, radius sensitivity and descriptive dispersion. PASS. |
| Measurement boundaries | Placement, ray geometry, accessibility and all NOT MEASURED human quantities remain distinct. PASS. |
| Reproducibility and custody | Complete before/after world inventories, preserved raw archives, competing lock regression, deterministic full report and clean-code representative reproduction. PASS. |
| Validation | [598 tests passed in 181.81 seconds](validation/final-tests.txt); [Ruff](validation/final-ruff.txt), [formatting](validation/final-format.txt) and [BasedPyright](validation/final-types.txt) pass. |
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


## PR37 visibility correction in progress

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
This fits the existing budget before the remaining fifteen analyses proceed.

All rejected version 1 results, producer logs, report and protocol remain durably
preserved at immutable reviewed commit `506bc4fd4d9efd2f216f7b59c47b95b0fa1c38b3`.
For example, `git show 506bc4fd:evidence/item-11/report.md` retrieves that rejected
report. Current paths are replaced only by freshly reproduced version 2 derived
results with their new identities; raw Item 10 worlds/censuses remain unchanged.
The local exit gate stays open until the full corrected matrix, report, affected
checks and fresh Codex review pass.
