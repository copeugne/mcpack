# Mountainous repetition-1 Sparse Structures control

Status: CONTROL-WORLD ACCEPTANCE PASS. Six of sixteen worlds are individually
accepted. Protocol: `item10-full-v1`, with
`item10-observer-coverage-v2`. Seed: `6671238423019257953`.
Generation source: `3fa7f3117d0f9a5fff3fb4545a4fe51144b16dfa`.

The unchanged [run receipt](run.json) records all eleven selections completed,
readiness, correlated save flush, clean stop, Java exit 0 and no process-group
kill or rejection. Duration: 666.194 seconds. All 228 frozen files and eleven
declared Chunky files pass capture.

Direct comparison with the [matched baseline](../full-mountainous-r1-baseline/run.json)
finds identical `probe` and lifecycle `selections`. `run.preflight` differs only
in `instrumented_candidate_count` (137 to 136), `sparse_structures_omitted`
(false to true) and `instrumented_runtime_sha256` (baseline to the frozen
`84a884f99e4ac48defb9ea0b2c9e45bf3d0f4f6e881a4be4d8968dc2be14d4da` control).
No fixture or before-generation commands were used. Collection runs in probe
mode, with the same frozen observer, not the legacy unobserved control mode.

## Raw custody

The stopped world backup contains 501 files totaling 446,862,457 bytes.
`world.tar.gz` is 182,141,550 bytes, SHA-256
`8c9f214680935a4e3370e4e435ef409ed8774c1c526770f266850995f3958a88`.
The [world restore](world-restore.json) verifies all 501 files in a new target.

The immutable [release](https://github.com/copeugne/mcpack/releases/tag/item10-full-mountainous-r1-without-sparse-3fa7f311)
contains the raw archive and [manifest](archive-manifest.json). The fetched tag
resolves to the generation source above. Archive size: 182,743,035 bytes;
SHA-256 `8da0f327a407250cc9ac57eaaacb50f0ca6a28c80b9e26c03528869068aee776`.
Its 313 files total 211,519,630 bytes before compression. Manifest SHA-256:
`c1bdd51b6a8d8574c01005cd5b91e5c4c0a6e74c7e80a9b814e43059c5997f3f`.
The [local restore](local-restore.json) and [downloaded restore](download-restore.json)
each verify all 313 members; the downloaded manifest matches byte-for-byte.
The archive includes
50 incoming target classes; their full trace validation still awaits the census.

## Reproduction

Use the existing [custody procedure](../full-ordinary-r1-without-sparse/README.md#reproduction)
with this run's name, source, archive and world hash. Create output parents first;
each output must be absent. Executed generation and archive commands:

```sh
uv run --no-sync python -m tools.run_item10_probe --name full-mountainous-r1-without-sparse --mode probe --preset item10 --role mountainous --arm without-sparse --repetition 1
uv run --no-sync python -m tools.archive_item7_evidence create --root evidence/raw/item10/full-mountainous-r1-without-sparse --archive evidence/raw/item10/item10-full-mountainous-r1-without-sparse-3fa7f311.tar.gz --manifest evidence/item-10/full-mountainous-r1-without-sparse/archive-manifest.json --revision 3fa7f3117d0f9a5fff3fb4545a4fe51144b16dfa
```

Raw observations and existing diagnostics remain unchanged. Generation and raw
custody do not establish density, gameplay, or Item 10 completion.

The full census completed as session `61273`, exit 0, using analysis implementation
`760aa2f5`. Executed command:

```sh
uv run --no-sync python -m tools.analyze_structure_density evidence/raw/item10/full-mountainous-r1-without-sparse-custody/restored-world/world evidence/raw/item10/full-mountainous-r1-without-sparse-analysis/all-strata.json --all-strata --dimension-geometry evidence/item-10/dimension-geometry.json --trace-root evidence/raw/item10/full-mountainous-r1-without-sparse-custody/restored-local --trace-manifest evidence/item-10/full-mountainous-r1-without-sparse/archive-manifest.json
```

Timing and diagnostics are retained beside the output in `all-strata-runtime.txt`.

## Full census and mountainous matched contrast

The full census passed in 10m17.617s (user 10m11.463s, system 0m1.375s).
Output: 117,578,014 bytes, SHA-256
`ced960a70c4c34581b19c68b2bdcbf76f003894191ae62537aa1a85072e968b7`.
All eleven strata contain 4,096 complete selected chunks, totaling 45,056.
All 50 incoming classes and installations pass the full trace checks. The
existing coverage-v2 implementation and its recorded tests are unchanged.

The table projects `strata[label].total_starts` and
`classification.categories[category].count`; density is count times `1000/4096`.
The categories retain Item 9's provisional rationale, confidence and ambiguity.

| Stratum | Registry starts | Classified locations | T0 | C | T1 | T2 | T3 | T4 | Villages |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| aether | 117 | 10 | 0 | 0 | 1 | 9 | 0 | 0 | 0 |
| earth-orbit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| mars | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| mars-orbit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| moon-orbit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| moon | 53 | 53 | 53 | 0 | 0 | 0 | 0 | 0 | 0 |
| venus | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| overworld | 130 | 4083 | 58 | 9 | 3987 | 22 | 7 | 0 | 3 |
| end-central | 6 | 8 | 7 | 0 | 0 | 0 | 0 | 1 | 0 |
| end-outer | 80 | 85 | 79 | 0 | 5 | 0 | 1 | 0 | 0 |
| nether | 99 | 461 | 44 | 6 | 383 | 19 | 9 | 0 | 2 |

Aether's 107 cloud starts remain excluded terrain. Central End includes the
arrival platform and dragon arena lifecycle sites. One gateway is in the outer
frame; another raw gateway group is outside the sample. The arena alone lacks
an anchor height/biome (NO_LOCATION_HEIGHT); the other 4,321 observed nonregistry
locations have biome attribution. Raw exposure remains separated by quart height.

The 32,787 attempts produce 25,418 NO_CONSTRUCTIVE_CONTENT, 2,858 OUTSIDE_FRAME,
4,322 OBSERVED_LOCATION and three CONTENT_NOT_PRESERVED grouped dispositions.
Attempts and grouped locations have different denominators. The rejected cave-urn
candidates are 11100 at Overworld (-335,24,194), with three content mismatches;
21265 at (223,-40,27), with one; and 31398 at (98,29,236), with one. Their raw
writes remain retained, and none contributes to the accepted location count.

Compared directly with the [matched baseline](../full-mountainous-r1-baseline/README.md),
control-minus-baseline classified-location differences are Aether +7, Mars +1,
Moon +41, Overworld +44, central End +5, outer End +66 and Nether +35. The other
four strata remain zero. Overworld T2 rises 6 to 22 and T3 rises 2 to 7, while
T1 falls 4,000 to 3,987 and villages remain three. Nether T2 rises 7 to 19 and
T3 rises 1 to 9. These are paired finite-region observations, not universal
ratios or evidence that every placement mechanism is affected identically.

The control's accepted Overworld nonregistry locations are 3,757 cave-urn caches,
192 monster boxes, three scarecrows and one fairy ring. These counts join
`locations` to OBSERVED_LOCATION dispositions by candidate ID. Small caches
dominate the total, so the +44 overall difference does not describe the much
larger proportional change in provisional dungeons. Neither measure is observed
combat or human exploration pacing.

The Overworld all-location nearest-observed mean changes from 8.12949 to 8.02635
blocks; its uncensored nearest-neighbor mean remains null in both arms because
of boundary censoring. These use chunk-center anchors and can include colocated
locations. Cell variance/mean changes from 2.10199 to 2.15930, with no empty full
cell rectangle in either arm. These values directly project `spatial.all_locations`;
all category-specific distances, censoring, cell counts and empty rectangles
remain in the full result rather than being replaced by this illustration.

Allocated working bytes for this instance, original raw, custody, analysis and
outer archive total 2,207,494,144 (about 2.06 GiB), using the same shared-inode
accounting as the baseline. Free space after analysis is 35,492,941,824 bytes
(about 33.1 GiB). Continue checking costs as the remaining ten worlds are collected.
