# Ordinary repetition-1 without-Sparse control

Status: CONTROL-WORLD ACCEPTANCE PASS. Two of sixteen planned worlds now have
complete individual acceptance; Item 10 remains IN PROGRESS.
Protocol: `item10-full-v1`; seed: `42`.
Generation source: `5ceb171ce09c241c613cabb0dc1b34a4d1efe619`.

The unchanged [run receipt](run.json) records all eleven completed selections,
readiness, correlated save flush and clean stop with Java exit 0. Duration was
559.034 seconds. The runtime omits only Sparse Structures: deployed candidate
count including Chunky is 136, SHA-256
`84a884f99e4ac48defb9ea0b2c9e45bf3d0f4f6e881a4be4d8968dc2be14d4da`.
All 228 frozen configuration files pass the existing semantic comparison;
eleven declared Chunky files are captured. The collector source/JAR hashes match
the frozen protocol. Full incoming-class and observation acceptance passed during
the analysis below. No configuration was tuned or world reused.

Direct comparison of both committed run receipts confirms equal `probe`,
`preset`, `repetition`, fixture/pre-generation commands, Java version and lifecycle
selections. The only differences between their `run.preflight` objects are
`instrumented_candidate_count` (137 versus 136), `sparse_structures_omitted`
(false versus true) and `instrumented_runtime_sha256` (the two protocol-pinned
arm hashes). Seed, retained source, frozen configuration, audit and Chunky
identities therefore match. The baseline's separately retained configuration
revalidation resolves its original capture rejection; it is not silently ignored.

The console retains 355 `Tried to load invalid item: 'Item must not be
minecraft:air'` messages; the matched baseline retains 300. These are existing
item-loading diagnostics, not missing structure observations or accepted loot
validation. Their full context remains in the raw logs. Structure/placement
acceptance relies on the explicit census and saved-content checks, not log silence.

## Raw custody

The stopped world backup contains 504 files totaling 434,558,526 bytes.
`world.tar.gz` is 169,798,947 bytes, SHA-256
`44c2327cac7a47ff0c7f10a57f10eddbe892e46b14d4ec7b0836b72f41dfb7b4`.
The [world restore](world-restore.json) verified all 504 members into a separate
world. No server restart was required for this offline evidence restore.

The immutable [release](https://github.com/copeugne/mcpack/releases/tag/item10-full-ordinary-r1-without-sparse-5ceb171c)
contains `item10-full-ordinary-r1-without-sparse-5ceb171c.tar.gz` and the
[archive manifest](archive-manifest.json). Its fetched tag resolves to the exact
generation source above. The outer archive is 170,417,446 bytes, SHA-256
`d183a00212cf4f1449e533d407319e3d7d181d4df2371273a8561c8bd64d2b93`,
with 313 files totaling 203,068,750 uncompressed bytes.
Both [local](local-restore.json) and [downloaded](download-restore.json) restores
verified all 313 files. The downloaded manifest is byte-identical to the committed
manifest. This release is evidence custody, not the Item 10 completion boundary.

The initial outer archive command failed before creation because its manifest
parent directory did not exist. Creating that directory and retrying succeeded.
No raw capture or world was modified by the failed invocation.

## Reproduction

Generation command (requires absent instance and raw output):

```sh
uv run --no-sync python -m tools.run_item10_probe --name full-ordinary-r1-without-sparse --mode probe --preset item10 --role ordinary --arm without-sparse --repetition 1
```

The existing backup, archive and restore tools are used without modification.
Create destination parents first; each output must be absent. Executed archive:

```sh
uv run --no-sync python -m tools.archive_item7_evidence create --root evidence/raw/item10/full-ordinary-r1-without-sparse --archive evidence/raw/item10/item10-full-ordinary-r1-without-sparse-5ceb171c.tar.gz --manifest evidence/item-10/full-ordinary-r1-without-sparse/archive-manifest.json --revision 5ceb171ce09c241c613cabb0dc1b34a4d1efe619
```

Download with `gh release download item10-full-ordinary-r1-without-sparse-5ceb171c
--repo copeugne/mcpack --dir DOWNLOAD`, then use `tools.archive_item7_evidence
restore` with the downloaded archive, this manifest, a new target and receipt.
Restore its nested world using `tools.manage_item4_environment restore` and the
world SHA-256 above. The exact restored paths are recorded in the receipts.

Executed full analysis invocation:

```sh
uv run --no-sync python -m tools.analyze_structure_density evidence/raw/item10/full-ordinary-r1-without-sparse-custody/restored-world/world evidence/raw/item10/full-ordinary-r1-without-sparse-analysis/all-strata.json --all-strata --dimension-geometry evidence/item-10/dimension-geometry.json --trace-root evidence/raw/item10/full-ordinary-r1-without-sparse-custody/restored-local --trace-manifest evidence/item-10/full-ordinary-r1-without-sparse/archive-manifest.json
```

Its timing/diagnostics are retained in the same analysis directory as
`all-strata-runtime.txt`. Generation completion is not census acceptance.

## Full census and first matched contrast

The full analysis exited 0 after 8m21.506s (user 8m16.051s, system 0m1.562s),
using the unchanged implementation delivered at `14680b79`. The result is
110,369,600 bytes, SHA-256
`84181564564b2c5bb5f804852214e6d1105df901a238ef51775dabdd6a5618a4`.
All eleven selected strata contain 4,096 complete chunks, totaling 45,056. The
full observer and archive-bound saved-content gates pass. No code changed for
this run; the applicable 541-test result recorded with the baseline remains valid.

The following table projects `strata[label].total_starts` and
`classification.categories[category].count` from the hash-bound output above.
Densities are the counts multiplied by `1000 / 4096`. Raw starts include terrain;
classified locations retain the accepted provisional Item 9 roles.

| Stratum | Registry starts | Classified locations | T0 | C | T1 | T2 | T3 | T4 | Villages |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| aether | 135 | 19 | 0 | 0 | 1 | 18 | 0 | 0 | 0 |
| earth-orbit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| mars | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| mars-orbit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| moon-orbit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| moon | 57 | 57 | 57 | 0 | 0 | 0 | 0 | 0 | 0 |
| venus | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| overworld | 86 | 1027 | 27 | 2 | 973 | 23 | 2 | 0 | 2 |
| end-central | 9 | 11 | 10 | 0 | 0 | 0 | 0 | 1 | 0 |
| end-outer | 45 | 91 | 89 | 0 | 2 | 0 | 0 | 0 | 0 |
| nether | 110 | 497 | 67 | 3 | 410 | 12 | 5 | 0 | 0 |

Aether retains 116 explicitly excluded cloud terrain starts. Central End includes
the arrival platform (T0) and arena (T4) as lifecycle sites; its other nine
locations are registry placements. Outer End includes two lifecycle gateways
among its 91 locations. These sites are not relabeled repeatable dungeons.
The arena has NO_LOCATION_HEIGHT and no biome attribution; the other 1,375
observed nonregistry locations have biome attribution.

Nonregistry dispositions: 24,261 NO_CONSTRUCTIVE_CONTENT, 3,060 OUTSIDE_FRAME,
1,376 OBSERVED_LOCATION and six CONTENT_NOT_PRESERVED. The latter are Overworld
cave urn candidates 10116, 19595, 20436, 21054, 21198 and 24129; each has one
saved-content mismatch and contributes no observed location. Their anchors and
raw writes remain retained. This applies the predeclared saved-content rule,
not a discarded generation failure or an inference that the writer never ran.

For the first matched contrast, each delta below is the control count minus the
same baseline stratum/category count. Both denominators are 4,096 chunks;
multiply these deltas by `1000 / 4096` for density changes. The baseline output
is pinned in its [acceptance record](../full-ordinary-r1-baseline/README.md).

| Stratum | Registry delta | Location delta | Actionable delta | Encounter-site delta | T2 delta | T3 delta | T4 delta | Village delta |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| aether | 104 | 14 | 14 | 14 | 13 | 0 | 0 | 0 |
| earth-orbit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| mars | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| mars-orbit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| moon-orbit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| moon | 46 | 46 | 0 | 0 | 0 | 0 | 0 | 0 |
| venus | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| overworld | 62 | 72 | 53 | 52 | 16 | 2 | 0 | 1 |
| end-central | 9 | 9 | 0 | 0 | 0 | 0 | 0 | 0 |
| end-outer | 28 | 65 | -1 | -1 | 0 | 0 | 0 | 0 |
| nether | 70 | 67 | 22 | 19 | 8 | 1 | 0 | 0 |

These are exact finite-region contrasts under the measurement overlay. They
measure the omission intervention, including salt changes; they do not isolate
spacing alone. One pair cannot separate that contrast from the already-established
run-to-run variation. Cross-repetition/seed comparisons and final spatial/biome
synthesis remain outstanding. No observed playtime, combat or enjoyment is claimed.

Generation plus analysis took 1,060.540 seconds, about 17m41s. With shared source
inodes counted first, `du -s -B1` reports 626,675,712 bytes for the control instance,
203,976,704 for raw capture, 1,013,198,848 for custody copies, 110,374,912 for
analysis and 170,418,176 for its outer archive: about 1.98 GiB. Filesystem free
space is 44,664,889,344 bytes (about 41.6 GiB). This remains close to the earlier
working-budget projection; continue checking actual growth rather than deleting
preserved evidence. Next is the fresh ordinary repetition-2 without-Sparse world,
then ordinary repetition-2 baseline, as predeclared.
