# Fresh registry diagnostic

The predeclared r1 attempt failed before Java launch: `/usr/bin/time` was absent
(exit 127). Its ignored raw output directory is retained. No world was created.
The corrected command uses Bash timing and fresh `pilot-r2` paths, with identical
seed, generation preset and census bounds. Run from the repository root:

```sh
bash evidence/item-10/pilot-r1/run.sh
```

Source code and predeclaration revision: `5f9ef4af`. The script is preserved here
with the corrected invocation; r1's failed invocation was the same command
preceded by `/usr/bin/time -p -o evidence/raw/item10/pilot-r1/time.txt` instead of
Bash timing. Results and verified custody follow below.

## Result and limits

The corrected r2 run completed under source/predeclaration revision
`5f9ef4af72ce780640984a2051e638aa2f0bf882`. [Run receipt](run-r2.json)
records the frozen runtime/configuration identity, readiness, all four generation
selections, correlated save confirmation, clean stop and exit 0. Lifecycle time
was 258.153 seconds; Bash elapsed time was 260.046 seconds. The stopped world
occupied 127,167,697 bytes before backup. These costs describe this diagnostic,
not a prediction of full-baseline runtime.

[Registry census](registry-census.json) accepted all 3,969 selected full Overworld
chunks, with 24 registry starts: 6.046863189720333 starts per 1,000 chunks.
The other three generated selections are retained but excluded from this
predeclared denominator. This does not count all canonical families, nonregistry
features, actionable locations or actual combat. It does not establish exploration
pacing, representativeness across seeds, or Item 10 completion.

## Reproduction and custody

After generation and clean shutdown:

```sh
uv run --no-sync python -m tools.analyze_structure_density instances/item10/pilot-r2/world evidence/raw/item10/pilot-r2/registry-census.json --dimension minecraft:overworld --bounds -31 31 -31 31
uv run --no-sync python -m tools.manage_item4_environment backup --world instances/item10/pilot-r2/world --archive evidence/raw/item10/pilot-r2/world.tar.gz --receipt evidence/item-10/pilot-r1/world-backup.json
```

[World backup receipt](world-backup.json) hashes 158 files and excludes
`session.lock`. [Archive manifest](archive-manifest.json) covers 243 raw files,
including that backup, logs, captured configuration, timing and original census.
The immutable archive is 75,841,389 bytes, SHA-256
`4b554017bd8fe320cff91d0a9b69290d8d4822a86417e2fdecc50531749e036d`.
The [release](https://github.com/copeugne/mcpack/releases/tag/item-10-pilot-raw-2026-09-08-r1)
retains the archive and manifest; [release metadata](release.json) records assets.
The fetched release tag resolves to the full source revision above.

[Local restore](local-restore.json) and [download restore](download-restore.json)
verified every archive member. [Nested world restore](world-restore.json) restored
all 158 world files. Running the census against the restored `world` with the same
dimension and bounds produced byte-identical JSON, checked with `cmp` against
`registry-census.json`. Commands for restoring downloaded evidence into absent
paths, from the repository root:

```sh
gh release download item-10-pilot-raw-2026-09-08-r1 --repo copeugne/mcpack --dir RESTORE_INPUT
uv run --no-sync python -m tools.archive_item7_evidence restore --archive RESTORE_INPUT/item10-pilot-r2-5f9ef4af.tar.gz --manifest evidence/item-10/pilot-r1/archive-manifest.json --target RESTORED_RAW --receipt RESTORE_RECEIPT.json
uv run --no-sync python -m tools.manage_item4_environment restore --archive RESTORED_RAW/world.tar.gz --sha256 cd08d41dc64f86950e50380a0c37c2486f3de8bdc6b859c78ef3b6952f654e9f --target RESTORED_WORLD
uv run --no-sync python -m tools.analyze_structure_density RESTORED_WORLD/world RESTORED_CENSUS.json --dimension minecraft:overworld --bounds -31 31 -31 31
cmp evidence/item-10/pilot-r1/registry-census.json RESTORED_CENSUS.json
```

The initial outer manifest mistakenly received an incorrect revision argument.
It was rejected before publication and corrected against `git rev-parse HEAD`;
archive contents and hash were unchanged. The rejected metadata remains locally
at `evidence/raw/item10/pilot-custody-r1/rejected-wrong-revision-manifest.json`.
No accepted measurement uses that revision. The prelaunch timer failure above
and this metadata correction do not become successful experiment observations.

## Accepted category integration

[Classified census](classified-census.json) adds the exact Item 8 family join and
Item 9 provisional role, confidence, flags, comparison groups, rationale and
ambiguity to every observed start. The source hashes are embedded in the output
and checked before joining. All 24 starts mapped. Distinct starts of the same
family remain distinct observations. Missing mappings fail instead of reducing
the count. The original raw census remains unchanged in the immutable archive.
Removing the added `classification` field gives exactly the original census.

| Provisional role | Starts | Per 1,000 selected chunks |
| --- | ---: | ---: |
| T0, ambient landmark | 8 | 2.015621 |
| C, civilization | 1 | 0.251953 |
| T1, small encounter | 8 | 2.015621 |
| T2, proper dungeon | 7 | 1.763668 |
| T3, major expedition | 0 | 0 |
| T4, world objective | 0 | 0 |

These are exclusive source-supported roles, not measured fights, clear times or
realized dungeon quality. Zeroes apply only to this selected registry sample.
The 40 nonregistry families remain outside its coverage. To reproduce after
restoring the world using the commands above, with a new output path:

```sh
uv run --no-sync python -m tools.analyze_structure_density RESTORED_WORLD/world CLASSIFIED_CENSUS.json --dimension minecraft:overworld --bounds -31 31 -31 31 --classify
```

Validation: 34 focused tests pass, covering the census/decoder boundaries and
new tests for preserving distinct starts in one family, rejecting unmapped
observations, and rejecting changed accepted-input hashes. Ruff passes for the
changed tool and test; basedpyright reports no errors or warnings for Item 10
tests. The real CLI was run on the restored pilot, then its base observations
were compared with the original census. Reproduce the focused checks:

```sh
uv run --no-sync pytest tests/item10 tests/item7/test_anvil_decoder.py tests/item7/test_world_region_dimensions.py -q
uv run --no-sync ruff check tools/analyze_structure_density.py tests/item10/test_density_census.py
uv run --no-sync basedpyright tests/item10
```

## Spatial diagnostic

[Spatial census](spatial-census.json) adds deterministic spatial summaries for all
registry starts and each exclusive provisional role. This is a diagnostic
application of the draft spatial method to retained pilot data, not acceptance
of the full sampling protocol. Removing `spatial` yields exactly the classified
census above. No generation, configuration or classification was changed.

Coordinates are the centers of authoritative start chunks, not entrances or
structure edges. Of 24 starts, five have boundary-censored nearest neighbors.
The mean distance to the nearest observed start inside the finite window is
93.77346215097855 blocks. The uncensored nearest-neighbor mean is UNKNOWN
(JSON null); it is not calculated by discarding the five censored observations.
Every observed distance, boundary distance and lower bound is retained.

Globally aligned 16 by 16 chunk cells retain all 3,969 selected chunks, including
partial cells at the edges. Nine complete cells cover 2,304 chunks. Equal-area
population variance divided by mean count is 2.7863247863247866 for those cells.
The largest fully observed rectangle of empty cells covers 768 chunks at
inclusive bounds X [-16, 31], Z [-16, -1]. Empty means no selected registry
start, not no structures crossing into the area, nonregistry features, enemies
or gameplay activity. Resolution is 256 blocks per cell side. Category results,
including zero and single-observation cases, remain in the JSON.

Reproduce against the restored pilot with a new output path:

```sh
uv run --no-sync python -m tools.analyze_structure_density RESTORED_WORLD/world SPATIAL_CENSUS.json --dimension minecraft:overworld --bounds -31 31 -31 31 --spatial
```

The complete focused surface now has 41 passing tests. Seven spatial cases cover
coincident starts, boundary censoring, exact interior distances, empty and
single-start cases, partial-cell denominators, and maximal empty rectangles
against an independent exhaustive oracle for all 64 occupancies of a 3 by 2
cell grid, including tie resolution. Ruff and Item 10 test type checks pass:

```sh
uv run --no-sync pytest tests/item10 tests/item7/test_anvil_decoder.py tests/item7/test_world_region_dimensions.py -q
uv run --no-sync ruff check tools/analyze_structure_density.py tests/item10
uv run --no-sync basedpyright tests/item10
```
