# BOP fixture r1: captured writes corroborated in saved blocks

Source `a9db20957a9a1f2806f73c131b16545f162e5353`. The [diagnostic](diagnostic.json) records frozen
preflight, all 324 selected chunks, correlated save-flush and clean exit 0 in
88.171 seconds. Archived `minecraft-latest.log` lines 2650 to 2653 confirm both
256-block fills and both requested feature placements. This artificial fixture
world is excluded from density samples.

The archived `trace.jsonl` has 25 begin/feature/end sequences, no unfinished
attempts, 22,769 successful writes and no refused-write records. Filtering writes
by the attempt's feature class gives anomaly 21,493 flags-3 writes and 807
flags-2 writes, plus monolith 469 flags-3 writes. These totals include natural
attempts and the two commanded fixtures; they are not 22,769 locations.
The trace is 2,752,225 bytes and is retained in the raw release rather than
ordinary Git. The [trace validation](trace-validation.json) binds these counts and all eight
incoming classes to the published archive. All attempts are paired and both
writers are exercised. This establishes capture integrity, not saved-block acceptance.

## Incoming helper inspection

All seven feature installation hashes match their retained incoming class files.
Incoming Minecraft Feature SHA-256 is `204f8d01187fb13dd72201d5588a632475991cb1aac5931153e654a88a204fce`. The archived
`Feature-incoming.txt` was produced with pinned `javap -p -c` on those retained
bytes. Its setBlock(LevelWriter,BlockPos,BlockState) still loads flags 3, calls
LevelWriter.setBlock at offset 4, then POP at 9 and RETURN at 10. Thus the chosen
call site observes the actual result before the helper discards it.
This inspection does not prove the whole collector noninterfering.

The existing validator now has a bounded BOP mode. Reproduce from the restored
raw root (no server run):

```sh
uv run --no-sync python -m tools.validate_item10_trace --bop-r1 evidence/raw/item10/bop-fixture-r1-custody/restored
uv run --no-sync pytest -q tests/item10/test_retained_trace.py
```

All 21 trace tests pass, including refusal denominators, missing lifecycle events,
missing installation, duplicate feature attribution, malformed arguments, changed
archive bytes and escaped inputs. Changed-file Ruff and basedpyright checks pass.
The parser consumes the same bytes whose archive hash was checked.
## Saved-block corroboration

The [crosscheck](saved-block-crosscheck.json) binds all four read region files to
the archived world manifest under the existing Java-compatible world lock. All
22,769 successful writes match saved block IDs at 22,769 distinct coordinates.
There are no repeated coordinates or last-recorded-write mismatches. All 25
attempts remain in the result, including 11 with zero writes. The saved palette
is decoded with the existing Anvil/NBT reader, with stored/slot coordinate checks.
This compares block IDs, not block-state properties or collector noninterference.

17,096 writes lie in chunks saved at `minecraft:full`; 5,673 lie in generated
neighbors saved at `minecraft:initialize_light`. The initial inspection rejected
these neighbors with `Write coordinate is not in a fully generated chunk`.
That full-chunk restriction belongs to density exposure, not diagnostic block
corroboration. The corrected inspection retains status counts and reads the
saved neighbors without admitting them into a density denominator. No raw data
or world was changed. This fixture remains excluded from density measurements.

Reuse the existing bounded inspector's BOP mode:

```sh
uv run --no-sync python -c "import runpy; runpy.run_path('evidence/item-10/scarecrow-probe-r3/inspect-writes.py')" --bop-r1
```

Its original scarecrow mode still reproduces all 30 prior observations. The
regressions now cover both modes' archive/region integrity; injected wrong block
IDs fail both acceptance commands after retaining explicit BOP mismatches in the report.
The first full test run failed four tests because their runpy calls inherited
pytest arguments. Tests now declare the inspection arguments explicitly.
Positive BOP capture and block-ID corroboration are established. Full Item 10
occurrence coverage, observer cost and density collection remain open.

## Verified raw custody

[Release](https://github.com/copeugne/mcpack/releases/tag/item-10-bop-fixture-2026-09-08-r1).
Archive 5244936 bytes, SHA-256 `4e6e22ca65a1fc6226bd605b1bc71c45db86386ee597d05e9400966559906162`.
[Download restore](download-restore.json) verifies 258 raw files; its downloaded
manifest is identical. [World restore](world-restore.json) matches all 97 paths,
sizes and hashes in [world backup](world-backup.json), without booting it.
Existing archive tools used root `evidence/raw/item10/bop-fixture-r1` and revision
`a9db2095`. Restore the downloaded archive with [manifest](archive-manifest.json),
then its nested world archive with SHA-256 `cb8904398b15172a7a2f3b7b39b0d0d500cdd684fa7ca9605bc517c1b25a8aa5`.

Validation: `uv run --no-sync pytest -q tests/item7 tests/item10` passes all
312 tests in 53.59 seconds. Changed inspection/test Ruff checks and test
basedpyright checks pass. Item 11 was not run or linted.

## PR25 review dispositions

The completed first review identified a valid missing BOP acceptance exit: the
inspector reported saved-block mismatches but exited zero. It now prints the
complete mismatch report and raises afterward. Both modes' injected-block
regressions require failure. Raw evidence and the accepted crosscheck are unchanged.

The ancestry finding is not applicable to the actual PR history. The recorded
source a9db20957a9a1f2806f73c131b16545f162e5353 is an ancestor of reviewed head
7ca8ebc8cfc5660bc28905b4f37408103e106829 (`git merge-base --is-ancestor` exits 0).
All six split commits remain in this PR. The finding's 4fa70ec reference is not
the reviewed PR head. Delivery will use a merge commit, preserving this ancestry.

The review correction passes all 312 Item 7/10 tests in 53.92 seconds,
changed-file Ruff and test type checks. The healthy archived BOP command still
exits zero and reproduces saved-block-crosscheck.json byte for byte.

The second review correctly identified that positive-path coverage counted
refused writes and did not require anomaly's flags-2 path. The validator now
requires successful writes on all three provider/flag paths while retaining
refusals in the total denominator. The unchanged archived capture has 807
anomaly flags-2, 21,493 anomaly flags-3 and 469 monolith flags-3 successes.
Focused regressions reject each refused-only path and an omitted final-write
path. No new generation or raw archive revision is needed.

This correction passes all 316 Item 7/10 tests in 53.83 seconds, plus changed
validator/test Ruff and basedpyright checks.

## Reviewed delivery

[PR25](https://github.com/copeugne/mcpack/pull/25) merged on 2026-09-08 at
05:31:10 UTC as `6d6ba32dd1526859aa0f0f3aa8d485f62e136705`, verified in fetched
origin/main. The [final clean review](https://github.com/copeugne/mcpack/pull/25#issuecomment-5579781691)
completed on `677eb2502ad499021eac774c12e8e6d1c2418c1a` at 05:29:53 UTC,
introduced no findings and returned the Codex bot thumbs-up. Both valid findings
are fixed; the incorrect ancestry finding is dispositioned above. Merge ancestry
retains the exact source and reviewed commits. This closes the BOP diagnostic
milestone, not Item 10 full measurement or acceptance.
