# Ordinary repetition-2 without-Sparse control

Status: CONTROL-WORLD ACCEPTANCE PASS. Three of sixteen worlds are individually
accepted; Item 10 remains IN PROGRESS. Protocol: `item10-full-v1`; seed: `42`.
Generation source: `6747b6b1470b6e90a168fdec89a996b9f419d889`.

The unchanged [run receipt](run.json) records all eleven completed selections,
readiness, correlated save flush and clean stop with Java exit 0 after 561.808
seconds. Its complete `run.preflight`, `probe` and lifecycle `selections` objects
equal those in the [first control](../full-ordinary-r1-without-sparse/run.json).
This verifies the same seed, retained source, declared omission, frozen identities
and observer. Repetition is 2 and the instance was fresh. All 228 frozen files and
eleven declared Chunky files pass configuration capture. The console retains 355
invalid-air-item diagnostics, the same count as the first control; raw context is
preserved, not treated as gameplay or loot validation.

## Raw custody

The stopped world backup contains 504 files totaling 434,640,568 bytes.
`world.tar.gz` is 170,090,793 bytes, SHA-256
`369132c89161ec00228c4b9d1376474fb83f62559523280557405c098863b780`.
The [world restore](world-restore.json) verified all 504 files into a new world.

The immutable [release](https://github.com/copeugne/mcpack/releases/tag/item10-full-ordinary-r2-without-sparse-6747b6b1)
contains the outer archive and [manifest](archive-manifest.json). The fetched tag
resolves to the exact generation source above. Archive size is 170,501,208 bytes,
SHA-256 `0f65280924909cbde74146c0acfebd44fdf79ce7c404f0431f54d3aa6d19b287`;
313 files total 194,331,412 uncompressed bytes. Both [local](local-restore.json)
and [downloaded](download-restore.json) restores verified all members, and the
downloaded manifest matches byte-for-byte. No server was restarted for these
offline restore checks. This is custody, not Item 10 completion.

## Reproduction

The existing [first-control procedure](../full-ordinary-r1-without-sparse/README.md#reproduction)
applies with this run name, revision, archive and world hash. Create destination
parents first; every output must be absent. Executed generation and archive:

```sh
uv run --no-sync python -m tools.run_item10_probe --name full-ordinary-r2-without-sparse --mode probe --preset item10 --role ordinary --arm without-sparse --repetition 2
uv run --no-sync python -m tools.archive_item7_evidence create --root evidence/raw/item10/full-ordinary-r2-without-sparse --archive evidence/raw/item10/item10-full-ordinary-r2-without-sparse-6747b6b1.tar.gz --manifest evidence/item-10/full-ordinary-r2-without-sparse/archive-manifest.json --revision 6747b6b1470b6e90a168fdec89a996b9f419d889
```

Executed full analysis on the restored world:

```sh
uv run --no-sync python -m tools.analyze_structure_density evidence/raw/item10/full-ordinary-r2-without-sparse-custody/restored-world/world evidence/raw/item10/full-ordinary-r2-without-sparse-analysis/all-strata.json --all-strata --dimension-geometry evidence/item-10/dimension-geometry.json --trace-root evidence/raw/item10/full-ordinary-r2-without-sparse-custody/restored-local --trace-manifest evidence/item-10/full-ordinary-r2-without-sparse/archive-manifest.json
```

Timing/diagnostics are beside the output in `all-strata-runtime.txt`. Full class,
chunk, location and exclusion checks passed as recorded below.

## Full census and control repetition comparison

The analysis exited 0 after 8m2.261s (user 7m56.868s, system 0m1.602s).
Its unchanged implementation is delivered at `14680b79`, covered by the existing
541-test Item 7/10 gate. Result size is 84,637,179 bytes, SHA-256
`6cf7be9e778b6dc94b76afee86857fd93e9034e9891fa3a25ccf9ca37b5d6225`.
All eleven strata contain 4,096 complete selected chunks, totaling 45,056;
full observer and archive-bound saved-content checks pass.

The table projects each `strata[label].total_starts` and
`classification.categories[category].count`. Densities are these counts times
`1000 / 4096`. Registry starts include cloud terrain; classified locations use
Item 9's provisional roles and are not observed fights.

| Stratum | Registry starts | Classified locations | T0 | C | T1 | T2 | T3 | T4 | Villages |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| aether | 135 | 19 | 0 | 0 | 1 | 18 | 0 | 0 | 0 |
| earth-orbit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| mars | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| mars-orbit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| moon-orbit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| moon | 57 | 57 | 57 | 0 | 0 | 0 | 0 | 0 | 0 |
| venus | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| overworld | 86 | 1022 | 27 | 2 | 968 | 23 | 2 | 0 | 2 |
| end-central | 9 | 11 | 10 | 0 | 0 | 0 | 0 | 1 | 0 |
| end-outer | 66 | 70 | 66 | 1 | 2 | 0 | 1 | 0 | 1 |
| nether | 111 | 502 | 69 | 4 | 412 | 13 | 4 | 0 | 0 |

Aether's 116 cloud starts remain excluded terrain. Central End includes the
arrival platform and dragon arena as lifecycle sites among its eleven locations;
outer End includes four lifecycle gateways among its 70 locations. The arena has
NO_LOCATION_HEIGHT and no biome attribution; the other 1,332 observed nonregistry
locations have biome attribution.

Nonregistry dispositions are 24,313 NO_CONSTRUCTIVE_CONTENT, 3,065 OUTSIDE_FRAME,
1,333 OBSERVED_LOCATION and two CONTENT_NOT_PRESERVED. The latter are Overworld
cave urn candidates 10143 at (-362,-25,410) and 24226 at (478,-29,46), each with
one saved-content mismatch. They are retained exclusions, not observed locations.

Direct comparison against the hash-bound [first-control result](../full-ordinary-r1-without-sparse/README.md)
uses the same stratum and category keys. All category counts are equal except:

- Overworld: locations 1,027 to 1,022, T1 973 to 968, actionable candidates
  1,000 to 995 and encounter sites 998 to 993. Registry starts stay at 86.
- Outer End: registry starts 45 to 66, locations 91 to 70, T0 89 to 66,
  C 0 to 1, T3 0 to 1, actionable candidates 2 to 4, encounter sites 2 to 3
  and villages 0 to 1. T1 remains 2.
- Nether: registry starts 110 to 111, locations 497 to 502, T0 67 to 69,
  C 3 to 4, T1 410 to 412, T2 12 to 13, T3 5 to 4, actionable candidates
  430 to 433 and encounter sites 427 to 429.

All other registry-start counts also agree. Count agreement does not establish
identical placements or world content. The substantial outer-End variation must
remain visible in the final intervention comparison, rather than attributing a
single pair's difference solely to Sparse Structures. These two observations
supply a descriptive range, not a population confidence interval. Both raw runs,
all spatial censoring and biome denominators remain retained.

Generation plus analysis took 1,044.069 seconds, about 17m24s. With shared source
inodes counted first, `du -s -B1` reports 626,761,728 bytes for the instance,
195,235,840 for raw capture, 995,979,264 for custody, 84,643,840 for analysis and
170,504,192 for the outer archive, about 1.93 GiB. Free space is 42,488,418,304
bytes (about 39.6 GiB). The next fresh run is ordinary repetition-2 baseline,
which completes the ordinary seed's declared four-world block. Its acceptance,
the other twelve worlds and final synthesis/review/delivery remain outstanding.
