# Ocean-heavy repetition-2 control, attempt 2

Status: CENSUS FAILED. Generation, configuration and raw custody passed.
Protocol: `item10-full-v1`, observer coverage
`item10-observer-coverage-v2`, post-failure amendment `item10-retry-policy-v1`.
Seed: `95920844204830198`. Source: `ffa51fb9981c438b802f5ae28e4796750636d5da`.

This is the single predeclared fresh retry of the
[retained failed attempt](../full-ocean-heavy-r2-without-sparse/README.md).
Its lifecycle completion does not erase that failure or identify the allocation that caused it.
The original instance and raw evidence remain at their original paths.

The unchanged [run receipt](run.json) explicitly records attempt 2. All eleven
selections, readiness, correlated save flush and clean stop pass, with Java exit
0 and no process-group kill or rejection. Duration: 549.011 seconds. All 228
frozen files and eleven Chunky paths pass configuration capture. No fixtures,
before-generation commands or configuration tuning were used. The heap-failure
shutdown path was not triggered; no `chunky pause` command was issued.

Direct comparison with the [first control](../full-ocean-heavy-r1-without-sparse/run.json)
finds identical `run.preflight`, `probe` and lifecycle `selections`. The observer
source and JAR remain frozen, and the runtime is the unchanged omit-only-Sparse
Structures control. The console contains no `OutOfMemoryError`, `Failed to load
chunk` or `Error upgrading chunk` signatures. Other raw warnings remain retained;
this is not performance, loot or observed-gameplay acceptance.

## Raw custody

The stopped world backup contains 502 files totaling 434,642,367 bytes.
`world.tar.gz` is 168,099,314 bytes, SHA-256
`7ac74bc1560d2baf3386d2cb4d76486290dd603b3a0fee83c08e0ad47e7af0ae`.
The [world restore](world-restore.json) verifies all 502 files in a new target.

The immutable [release](https://github.com/copeugne/mcpack/releases/tag/item10-full-ocean-heavy-r2-without-sparse-attempt2-ffa51fb9)
contains the raw archive and [manifest](archive-manifest.json). Its fetched tag
resolves to the source above. Archive size: 168,492,818 bytes; SHA-256
`9ffb3fc05d75e6b84807913ca6c5061c3ccd1a1897ec3282fc914f00ed0a5f7b`.
Its 313 files total 192,219,554 bytes before compression. Manifest SHA-256:
`1138d6b8d0096546e654d5ed85bb95333da71665eaa70c4c62e6032d0be5c6a3`.
The [local restore](local-restore.json) and [downloaded restore](download-restore.json)
each verify all 313 members; the downloaded manifest is byte-identical.
Fifty incoming target classes are preserved; complete trace analysis was not
reached because the earlier chunk-status gate failed. The failed first attempt
retains its separate immutable archive.

## Reproduction

Use the [existing custody procedure](../full-ordinary-r1-without-sparse/README.md#reproduction)
with this attempt's name, source, archive and world hash. Create output parents
first; every output must be absent. Executed generation and archive commands:

```sh
uv run --no-sync python -m tools.run_item10_probe --name full-ocean-heavy-r2-without-sparse-attempt2 --mode probe --preset item10 --role ocean-heavy --arm without-sparse --repetition 2 --attempt 2
uv run --no-sync python -m tools.archive_item7_evidence create --root evidence/raw/item10/full-ocean-heavy-r2-without-sparse-attempt2 --archive evidence/raw/item10/item10-full-ocean-heavy-r2-without-sparse-attempt2-ffa51fb9.tar.gz --manifest evidence/item-10/full-ocean-heavy-r2-without-sparse-attempt2/archive-manifest.json --revision ffa51fb9981c438b802f5ae28e4796750636d5da
```

The census ended as session `98243`, exit 1, with the unchanged census implementation
last modified at `760aa2f5`. Executed command:

```sh
uv run --no-sync python -m tools.analyze_structure_density evidence/raw/item10/full-ocean-heavy-r2-without-sparse-attempt2-custody/restored-world/world evidence/raw/item10/full-ocean-heavy-r2-without-sparse-attempt2-analysis/all-strata.json --all-strata --dimension-geometry evidence/item-10/dimension-geometry.json --trace-root evidence/raw/item10/full-ocean-heavy-r2-without-sparse-attempt2-custody/restored-local --trace-manifest evidence/item-10/full-ocean-heavy-r2-without-sparse-attempt2/archive-manifest.json
```

Timing and diagnostics are retained beside the output in `all-strata-runtime.txt`.
Ten planned cells remain accepted; this retry failed census acceptance.
The total attempted world count includes the failed first attempt; it is never a zero-density result.

## Census rejection and exact chunk diagnosis

The [unchanged rejection output](census-rejection.txt) records failure after
4.354 seconds: selected Aether chunk (-16,-22) is incomplete or duplicated.
No `all-strata.json` result was published. Subsequent direct inspection with the
existing decoder resolves the disjunction: all 4,096 selected Aether coordinates
are present exactly once. There are 4,095 `minecraft:full` records and one
`minecraft:initialize_light` record at (-16,-22). There are no missing or
duplicated selected coordinates. These are failure-diagnostic counts, not an
accepted reduced-area density denominator.

The affected immutable restored region is
`dimensions/aether/the_aether/region/r.-1.-1.mca`, SHA-256
`a20e9a3243e17609934158b1a45c5ab01ca7162cd63d034ec747d050b5138a10`.
Its slot is 336: local X 16 plus local Z 10 times 32. The existing decoder
requires stored chunk coordinates to match that slot. Derivation: iterate
`world_regions(restored_world, dimension_geometry=geometry)`, select
`aether:the_aether`, decode each region with `decode_region_payloads`, retain
inclusive X/Z bounds [-32,31], count records by `status` and coordinates, and
compare coordinates with the 64 by 64 Cartesian frame. Geometry is the unchanged
[dimension file](../dimension-geometry.json). This direct inspection ended with
exit 0 and did not modify the world or repeat generation.

Chunky's 100% progress, the normal save flush and Java exit 0 did not establish
complete saved chunk status. The frozen protocol requires `minecraft:full` and
the existing census correctly rejects this record. Do not relabel
`initialize_light` as full, omit the chunk, substitute a denominator of 4,095,
repair the preserved world, or claim that all other strata passed. The census
stopped at this first failure. No heap-exhaustion signature was recorded in this
attempt. The save exception below explains the distinct incomplete saved record.
The original raw archive remains valid and unchanged.

## Save exception and supplemental raw diagnostic

The archived `console.log`, line 2685, records `Failed to save chunk -16,-22`
at 17:30:16, followed by `java.util.ConcurrentModificationException` in
`LargeAercloudChunk.addAdditionalSaveData` (Aether 1.5.10, source line 50).
This is the exact coordinate rejected by the census. The subsequent log names
`debug/chunk-world-2026-09-08_17.30.16-server.txt`. The report was still present
in the stopped instance but omitted from the original archive.

The [supplemental release](https://github.com/copeugne/mcpack/releases/tag/item10-ocean-r2-control-save-diagnostic-852b2929)
preserves that unchanged 82,391-byte report, SHA-256
`f7733b582f3ffa1b9976929ae12780dcfbe2a215dad9158a81fe043cbb445332`.
The [manifest](save-diagnostic-manifest.json) binds its 9,860-byte archive to
`852b2929bd8eaf0b253215843e5d6debf4df10f6`; the fetched release tag matches.
[Local restore](save-diagnostic-local-restore.json) and
[downloaded restore](save-diagnostic-download-restore.json) verify its sole file.
The downloaded manifest is byte-identical. This supplement preserves an omitted
raw diagnostic, not a replacement world or revised original archive. Reproduce
custody with the existing `tools.archive_item7_evidence` create/restore commands,
using the manifest's archive name, revision and single-file source directory.

Reuse of the [existing Item 8 source inspection](../../item-8/sources/aether-custom-entry/README.md)
shows that `LargeAercloudChunk` stores positions in a `HashSet`;
`addAdditionalSaveData` iterates it, while `postProcess` calls `removeIf` on it.
The retained disassembly's method bytecode directly establishes these accesses.
Concurrent generation and serialization of that mutable set is a plausible
mechanism, not a proven attribution to a particular scheduler or mod. The report
does not capture the mutating thread. Do not claim a root-cause repair.

Targeted signature check: `rg -n -F 'Failed to save chunk'
evidence/raw/item10/full-*/console.log` returns only this retry's line 2685.
Thus none of the ten accepted full-run consoles contains this exact signature.
Their complete saved-chunk census remains accepted; this check does not prove
general persistence safety or reopen their density measurements by itself.

## Collection harness correction

The existing `item7_lifecycle` emergency shutdown now also recognizes Minecraft's
server-thread ERROR `Failed to save chunk X,Z` with signed integer coordinates.
It pauses Chunky once, uses the existing correlated flush/stop, and always rejects
the run. The existing 60-second emergency allowance remains bounded by the overall
deadline; timeout uses whole-process-group termination. Subsequent completion
markers cannot start more selections or erase the failure. The first fatal reason
is retained. Successful generation commands and all runtime identities are unchanged.
This fixes wasted continuation after an explicit save failure, not the Aether defect.
The original run receipt remains unchanged and records the behavior actually used.

Validation: `uv run --no-sync pytest tests/item7/test_worldgen_lifecycle.py
tests/item7/test_item7_console.py tests/item10/test_collection_runner.py -q`
passed 42 tests in 3.53 seconds. The save-error regression covers zero, two and
four completed selections, repeated error lines, confirmed save/stop with rejection,
and emergency timeout with process-group termination. Ruff check/format and focused
BasedPyright pass for the changed lifecycle and test files. These are simulated
harness tests, not a new Minecraft experiment or proof that the runtime is repaired.

The one-retry policy was exhausted at rejection. The subsequent user-authorized
[v2 continuation](../protocol.md#authorized-continuation-and-final-bounded-retry)
runs the five untouched worlds before one final fresh control retry, keeping
the target at sixteen complete worlds. Both prior attempts remain failures in the
run matrix: the first failed generation, the second failed complete census.
The full planned sample and final report/review/audit remain incomplete.
