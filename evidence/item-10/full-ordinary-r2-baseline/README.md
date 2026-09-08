# Ordinary repetition-2 baseline

Status: BASELINE-WORLD ACCEPTANCE PASS. All four ordinary-seed worlds are
individually accepted; twelve worlds remain. Protocol: `item10-full-v1`; seed: `42`.
Generation source: `004b1724a3242c0bf8fc9faf43e4b4e4f37dc23e`.

The unchanged [run receipt](run.json) records all eleven selections completed,
readiness, correlated save flush and clean stop with Java exit 0 after 513.589
seconds. Its entire `run.preflight`, `probe` and lifecycle `selections` objects
equal the [first baseline](../full-ordinary-r1-baseline/run.json), with repetition
2 and a fresh instance. All 228 frozen files and eleven declared Chunky files
pass capture. The console retains 300 invalid-air-item diagnostics, matching the
first baseline's count. Raw log context remains preserved; this is not loot or
gameplay validation. The original first-baseline capture rejection and subsequent
revalidation remain separately documented, not rewritten.

## Raw custody

The stopped world backup contains 503 files totaling 427,985,630 bytes.
`world.tar.gz` is 162,071,075 bytes, SHA-256
`b13e992bc23b96c4d6e382b4103185ac85953cab7e912a8fa3fa910a0d8fc61a`.
The [world restore](world-restore.json) verified all 503 files into a new world.

The immutable [release](https://github.com/copeugne/mcpack/releases/tag/item10-full-ordinary-r2-baseline-004b1724)
contains the outer archive and [manifest](archive-manifest.json). The fetched tag
resolves to the exact generation source above. Archive size is 162,552,858 bytes,
SHA-256 `86207dadba050cb1f5ec00ba618d2847b614d19d463860693a306d9782d722c6`;
313 files total 190,621,130 uncompressed bytes. Both [local](local-restore.json)
and [downloaded](download-restore.json) restores verified all members, and the
downloaded manifest matches byte-for-byte. No server restart was required for
these offline restore checks. This is custody, not Item 10 completion.

## Reproduction

Use the existing [custody procedure](../full-ordinary-r1-without-sparse/README.md#reproduction)
with this name, revision, archive and world hash. Destination parents must exist;
outputs must be absent. Executed generation and archive commands:

```sh
uv run --no-sync python -m tools.run_item10_probe --name full-ordinary-r2-baseline --mode probe --preset item10 --role ordinary --arm baseline --repetition 2
uv run --no-sync python -m tools.archive_item7_evidence create --root evidence/raw/item10/full-ordinary-r2-baseline --archive evidence/raw/item10/item10-full-ordinary-r2-baseline-004b1724.tar.gz --manifest evidence/item-10/full-ordinary-r2-baseline/archive-manifest.json --revision 004b1724a3242c0bf8fc9faf43e4b4e4f37dc23e
```

Executed full census on the restored world:

```sh
uv run --no-sync python -m tools.analyze_structure_density evidence/raw/item10/full-ordinary-r2-baseline-custody/restored-world/world evidence/raw/item10/full-ordinary-r2-baseline-analysis/all-strata.json --all-strata --dimension-geometry evidence/item-10/dimension-geometry.json --trace-root evidence/raw/item10/full-ordinary-r2-baseline-custody/restored-local --trace-manifest evidence/item-10/full-ordinary-r2-baseline/archive-manifest.json
```

Timing/diagnostics are beside the output in `all-strata-runtime.txt`. Full class,
chunk and location checks passed; comparisons are recorded below.

## Full census and ordinary-seed block

The full analysis exited 0 after 7m41.104s (user 7m36.348s, system 0m1.170s).
Result size is 92,552,776 bytes, SHA-256
`df3ee4e68ee57ffc264b97260869f6510a42b4cf575de4fce45c2192912390ff`.
The unchanged implementation is `14680b79`, covered by the existing 541-test
Item 7/10 gate. All eleven strata contain 4,096 complete selected chunks,
totaling 45,056; full observer and archive-bound saved-content checks pass.

The table directly projects each `strata[label].total_starts` and
`classification.categories[category].count`. Multiply counts by `1000 / 4096`
for density. Registry starts include terrain; classified locations use provisional
Item 9 roles and do not establish observed fights or meaningful interaction.

| Stratum | Registry starts | Classified locations | T0 | C | T1 | T2 | T3 | T4 | Villages |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| aether | 31 | 5 | 0 | 0 | 0 | 5 | 0 | 0 | 0 |
| earth-orbit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| mars | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| mars-orbit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| moon-orbit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| moon | 11 | 11 | 11 | 0 | 0 | 0 | 0 | 0 | 0 |
| venus | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| overworld | 24 | 935 | 8 | 1 | 919 | 7 | 0 | 0 | 1 |
| end-central | 0 | 2 | 1 | 0 | 0 | 0 | 0 | 1 | 0 |
| end-outer | 17 | 26 | 23 | 0 | 3 | 0 | 0 | 0 | 0 |
| nether | 44 | 426 | 24 | 1 | 391 | 6 | 4 | 0 | 0 |

Aether's 26 cloud starts remain excluded terrain. Central End's two locations
are the arrival platform and dragon arena lifecycle sites; outer End includes
four lifecycle gateways among its 26 locations. The arena has NO_LOCATION_HEIGHT
and no biome attribution; the other 1,303 observed nonregistry locations have
biome attribution.

Nonregistry dispositions are 24,301 NO_CONSTRUCTIVE_CONTENT, 3,061 OUTSIDE_FRAME,
1,304 OBSERVED_LOCATION and one CONTENT_NOT_PRESERVED. The excluded cave-urn
candidate 23089 is at Overworld (438,-4,-316), with two saved-content mismatches.
Its raw writes and exclusion are retained rather than counted as a saved location.

Compared with the [first baseline](../full-ordinary-r1-baseline/README.md), all
category counts agree except Overworld and Nether. Overworld locations/T1/
actionable/encounter-site counts are each 20 lower, with registry starts unchanged
at 24. Nether registry starts rise 40 to 44; locations fall 430 to 426, T0 rises
22 to 24, C 0 to 1, T1 falls 400 to 391, T2 rises 4 to 6, T3 stays 4,
actionable candidates fall 408 to 402 and encounter sites 408 to 401. All other
registry-start counts agree. Equal counts do not imply equal placements.

The second matched contrast below is control repetition 2 minus baseline
repetition 2 for identical stratum/category keys, each with 4,096 chunks. Multiply
deltas by `1000 / 4096` for density changes. The control output is bound in its
[acceptance record](../full-ordinary-r2-without-sparse/README.md).

| Stratum | Registry delta | Location delta | Actionable delta | Encounter-site delta | T2 delta | T3 delta | T4 delta | Village delta |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| aether | 104 | 14 | 14 | 14 | 13 | 0 | 0 | 0 |
| earth-orbit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| mars | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| mars-orbit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| moon-orbit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| moon | 46 | 46 | 0 | 0 | 0 | 0 | 0 | 0 |
| venus | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| overworld | 62 | 87 | 68 | 67 | 16 | 2 | 0 | 1 |
| end-central | 9 | 9 | 0 | 0 | 0 | 0 | 0 | 0 |
| end-outer | 49 | 44 | 1 | 0 | 0 | 1 | 0 | 1 |
| nether | 67 | 76 | 31 | 28 | 7 | 0 | 0 | 0 |

Together with the [first matched contrast](../full-ordinary-r1-without-sparse/README.md)
and [control repetition comparison](../full-ordinary-r2-without-sparse/README.md),
this completes the four ordinary-seed individual measurements and count contrasts.
For example, Overworld registry starts are 24 in both baselines and 86 in both
controls; classified location counts are 955/935 versus 1,027/1,022. The retained
nonregistry variation must not be hidden by presenting registry counts as all-family
density. These are finite-region observations under the measurement overlay, not
population confidence intervals or a spacing-only causal effect. Full cross-seed,
spatial and biome synthesis remains required after the other twelve worlds.

Generation plus analysis took 974.693 seconds, about 16m15s. With shared source
inodes counted first, `du -s -B1` reports 620,015,616 bytes for this instance,
191,533,056 for raw capture, 973,963,264 for custody, 92,557,312 for analysis and
162,553,856 for the outer archive: about 1.90 GiB. Free space is 40,304,340,992
bytes (about 37.5 GiB). Continue checking actual storage per world against the
roughly 30 GiB working budget. Next is mountainous repetition-1 baseline, using
the existing frozen protocol and fresh-materialization checks.
