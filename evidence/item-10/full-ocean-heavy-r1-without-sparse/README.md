# Ocean-heavy repetition-1 control

Status: CONTROL-WORLD ACCEPTANCE PASS.
Ten of sixteen worlds are individually accepted. Protocol: `item10-full-v1`, with
`item10-observer-coverage-v2`. Seed: `95920844204830198`.
Generation source: `6142e94b159a18ab68747b81a9daef206652cf7d`.

The unchanged [run receipt](run.json) records all eleven selections completed,
readiness, correlated save flush, clean stop, Java exit 0 and no process-group
kill or rejection. Duration: 553.698 seconds. All 228 frozen files and eleven
declared Chunky files pass capture. No fixture or before-generation commands
were used. No configuration tuning was performed.

Direct comparison with the [matched baseline](../full-ocean-heavy-r1-baseline/run.json)
finds identical `probe` and lifecycle `selections`. `run.preflight` differs only
in instrumented candidate count (137 to 136), Sparse Structures omission (false
to true), and instrumented runtime digest. The deployed control digest is
`84a884f99e4ac48defb9ea0b2c9e45bf3d0f4f6e881a4be4d8968dc2be14d4da`,
matching the [declared control](../protocol.md#sparse-structures-control-contrast).
Generation is not observed gameplay or performance acceptance.

## Raw custody

The stopped world backup contains 502 files totaling 432,430,406 bytes.
`world.tar.gz` is 166,275,156 bytes, SHA-256
`aaf5286b73e4dfedd2938c8ab3d38a074e51bae9fc9038f70226e17a3b454b53`.
The [world restore](world-restore.json) verifies all 502 files in a new target.

The immutable [release](https://github.com/copeugne/mcpack/releases/tag/item10-full-ocean-heavy-r1-without-sparse-6142e94b)
contains the raw archive and [manifest](archive-manifest.json). Its fetched tag
resolves to the generation source above. Archive size: 166,700,311 bytes;
SHA-256 `84d9341131df973c32d42d38056f270e76415ee260ef52ceb2d63b140152d0b3`.
Its 313 files total 191,505,513 bytes before compression. Manifest SHA-256:
`c269147861e4042f419a5eaffa08be413b85a03ebc36859b6e133620f002c996`.
The [local restore](local-restore.json) and [downloaded restore](download-restore.json)
each verify all 313 members, and the downloaded manifest matches byte-for-byte.
All 50 incoming target classes pass complete trace validation. Raw observations and diagnostics remain unchanged.

## Reproduction

Use the existing [custody procedure](../full-ordinary-r1-without-sparse/README.md#reproduction)
with this run's name, source, archive and world hash. Create output parents first;
each output must be absent. Executed generation and archive commands:

```sh
uv run --no-sync python -m tools.run_item10_probe --name full-ocean-heavy-r1-without-sparse --mode probe --preset item10 --role ocean-heavy --arm without-sparse --repetition 1
uv run --no-sync python -m tools.archive_item7_evidence create --root evidence/raw/item10/full-ocean-heavy-r1-without-sparse --archive evidence/raw/item10/item10-full-ocean-heavy-r1-without-sparse-6142e94b.tar.gz --manifest evidence/item-10/full-ocean-heavy-r1-without-sparse/archive-manifest.json --revision 6142e94b159a18ab68747b81a9daef206652cf7d
```

The census completed as session `89527`, exit 0, using analysis implementation
`760aa2f5`. Executed command:

```sh
uv run --no-sync python -m tools.analyze_structure_density evidence/raw/item10/full-ocean-heavy-r1-without-sparse-custody/restored-world/world evidence/raw/item10/full-ocean-heavy-r1-without-sparse-analysis/all-strata.json --all-strata --dimension-geometry evidence/item-10/dimension-geometry.json --trace-root evidence/raw/item10/full-ocean-heavy-r1-without-sparse-custody/restored-local --trace-manifest evidence/item-10/full-ocean-heavy-r1-without-sparse/archive-manifest.json
```

Timing and diagnostics are retained beside the output in `all-strata-runtime.txt`.
Generation and raw custody do not establish density or Item 10 completion.

## Full census and first ocean-heavy matched pair

Analysis passed in 8m0.325s (user 7m55.245s, system 0m1.291s).
Output size: 92,405,273 bytes; SHA-256
`b58570b27bf0ee532825f80a1ebcf9164223bcfc3d0a2426b957d60cbb0ae959`.
All eleven strata contain 4,096 complete selected chunks, totaling 45,056.
All 50 target classes and installations pass complete trace validation. No
observer target is unexercised. The implementation and recorded tests are unchanged.

The table projects `strata[label].total_starts` and
`classification.categories[category].count`. Density is count times `1000/4096`.
Categories retain Item 9's provisional rationale, confidence and ambiguity.

| Stratum | Registry starts | Classified locations | T0 | C | T1 | T2 | T3 | T4 | Villages |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| aether | 122 | 10 | 0 | 0 | 0 | 10 | 0 | 0 | 0 |
| earth-orbit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| mars | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| mars-orbit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| moon-orbit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| moon | 49 | 49 | 49 | 0 | 0 | 0 | 0 | 0 | 0 |
| venus | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| overworld | 90 | 1401 | 30 | 1 | 1348 | 19 | 3 | 0 | 1 |
| end-central | 7 | 9 | 8 | 0 | 0 | 0 | 0 | 1 | 0 |
| end-outer | 51 | 57 | 52 | 0 | 2 | 2 | 1 | 0 | 0 |
| nether | 133 | 532 | 80 | 7 | 418 | 24 | 3 | 0 | 0 |

Aether's 112 cloud starts remain excluded terrain. The arena alone lacks anchor
height and biome (NO_LOCATION_HEIGHT); the other 1,717 observed nonregistry
locations have biome attribution. Spatial outputs preserve each category's
nearest-neighbor distances and censoring, clustering and empty rectangles. Biome
exposure retains separate quart-height denominators. Lifecycle observations
remain distinguishable and do not establish observed human gameplay.

The 28,648 attempts produce 24,078 NO_CONSTRUCTIVE_CONTENT, 2,630 OUTSIDE_FRAME,
1,718 OBSERVED_LOCATION and one CONTENT_NOT_PRESERVED grouped source location.
Attempt and grouped-location denominators differ. No overlaps were reported.
The excluded cave-urn cache is candidate 20912 at (351,-24,-213), with one
mismatching position. It remains outside accepted counts. Derivation:
`location_observations` joined to `locations` by candidate ID.

Subtracting the [matched baseline](../full-ocean-heavy-r1-baseline/README.md)
from this control gives total differences of Aether +7, Moon +38, Overworld
+107, central End +7, outer End +38 and Nether +95. The other five strata
remain zero. Overworld T2/T3 counts are baseline 7/2 versus control 19/3;
Nether T2/T3 counts are 5/2 versus 24/3. Village counts do not change.
These are first-pair finite-area differences, not global density ratios or
observed fights. The second repetition remains necessary to retain within-arm
variation and complete the ocean-heavy block.

Allocated working bytes for the instance, raw, custody, analysis and outer
archive total 2,060,509,184 (about 1.92 GiB), counting shared candidate/pristine
and preceding instance inodes first. Free space after analysis is 26,226,556,928
bytes (about 24.4 GiB). Six worlds, combined synthesis, final review/merge and
the cross-item audit remain incomplete.
