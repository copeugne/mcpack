# BOP fixture r1: positive runtime observations, acceptance pending

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
Next corroborate saved blocks, preserving overlaps and later changes. No further
generation is needed for this remaining check on the restored evidence.

## Verified raw custody

[Release](https://github.com/copeugne/mcpack/releases/tag/item-10-bop-fixture-2026-09-08-r1).
Archive 5244936 bytes, SHA-256 `4e6e22ca65a1fc6226bd605b1bc71c45db86386ee597d05e9400966559906162`.
[Download restore](download-restore.json) verifies 258 raw files; its downloaded
manifest is identical. [World restore](world-restore.json) matches all 97 paths,
sizes and hashes in [world backup](world-backup.json), without booting it.
Existing archive tools used root `evidence/raw/item10/bop-fixture-r1` and revision
`a9db2095`. Restore the downloaded archive with [manifest](archive-manifest.json),
then its nested world archive with SHA-256 `cb8904398b15172a7a2f3b7b39b0d0d500cdd684fa7ca9605bc517c1b25a8aa5`.
