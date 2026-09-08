# Mountainous repetition-2 baseline

Status: BASELINE-WORLD ACCEPTANCE PASS, with six reviewed overlap exclusions.
Eight of sixteen worlds are individually accepted. Protocol: `item10-full-v1`, with
`item10-observer-coverage-v2`. Seed: `6671238423019257953`.
Generation source: `b6df88877b7248f900ed3e40e3bf73a53183bc82`.

The unchanged [run receipt](run.json) records all eleven selections completed,
readiness, correlated save flush, clean stop, Java exit 0 and no process-group
kill or rejection. Duration: 618.366 seconds. All 228 frozen files and eleven
declared Chunky files pass capture. No fixture or before-generation commands
were used. The raw console retains generation-load warnings, including
"Can't keep up" messages; successful lifecycle checks are not a performance pass.

Direct comparison with the [first baseline](../full-mountainous-r1-baseline/run.json)
finds identical `run.preflight`, `probe` and lifecycle `selections`; this is a
fresh independent repetition under the same frozen sampling and runtime identity.
No configuration tuning was performed.

## Raw custody

The stopped world backup contains 501 files totaling 438,725,769 bytes.
`world.tar.gz` is 173,030,403 bytes, SHA-256
`8f22ac215a520998dacf606a3d774b1cc4ce96bc4323e82d0d26e0ca043fbd5b`.
The [world restore](world-restore.json) verifies all 501 files in a new target.

The raw archive and [manifest](archive-manifest.json) use immutable name
`item10-full-mountainous-r2-baseline-b6df8887.tar.gz`. Archive size: 173,830,470 bytes;
SHA-256 `f800636027c80823a0dab98916712731792dd4f85f9cdcd00eff7213814a8064`.
Its 313 files total 211,482,822 bytes before compression. Manifest SHA-256:
`d334938f7d8a01f0253b588bd2805b42ef38241c416f064c3c0b0b8b301df881`.
The immutable [release](https://github.com/copeugne/mcpack/releases/tag/item10-full-mountainous-r2-baseline-b6df8887)
contains both files; its fetched tag resolves to the exact generation source.
The [local restore](local-restore.json) and [downloaded restore](download-restore.json)
each verify all 313 members, and the downloaded manifest matches byte-for-byte. There are 50
incoming target classes; complete trace acceptance still awaits census analysis.

## Reproduction

Use the existing [custody procedure](../full-ordinary-r1-without-sparse/README.md#reproduction)
with this run's name, source, archive and world hash. Create output parents first;
each output must be absent. Executed generation and archive commands:

```sh
uv run --no-sync python -m tools.run_item10_probe --name full-mountainous-r2-baseline --mode probe --preset item10 --role mountainous --arm baseline --repetition 2
uv run --no-sync python -m tools.archive_item7_evidence create --root evidence/raw/item10/full-mountainous-r2-baseline --archive evidence/raw/item10/item10-full-mountainous-r2-baseline-b6df8887.tar.gz --manifest evidence/item-10/full-mountainous-r2-baseline/archive-manifest.json --revision b6df88877b7248f900ed3e40e3bf73a53183bc82
```

Raw observations and existing diagnostics remain unchanged. Generation and raw
custody do not establish density, gameplay, or Item 10 completion.

The full census completed as session `50314`, exit 0, using analysis implementation
`760aa2f5`. Executed command:

```sh
uv run --no-sync python -m tools.analyze_structure_density evidence/raw/item10/full-mountainous-r2-baseline-custody/restored-world/world evidence/raw/item10/full-mountainous-r2-baseline-analysis/all-strata.json --all-strata --dimension-geometry evidence/item-10/dimension-geometry.json --trace-root evidence/raw/item10/full-mountainous-r2-baseline-custody/restored-local --trace-manifest evidence/item-10/full-mountainous-r2-baseline/archive-manifest.json
```

Timing and diagnostics are retained beside the output in `all-strata-runtime.txt`.

## Overlap review and disposition

Three pairs contain all six in-frame OVERLAP_REVIEW_REQUIRED candidates. Each
is ordinary generation in outer End with surviving constructive content. Direct
intersection of `locations[].content_positions` agrees with `overlaps`:

| Candidates | Families | Shared positions | Shared-position bounds, inclusive X/Y/Z |
| --- | --- | ---: | --- |
| 31443 / 31474 | anomaly / monolith | 3 | (7929,53,8578) to (7929,55,8578) |
| 31445 / 31448 | anomaly / anomaly | 129 | (7953,17,8627) to (7954,56,8634) |
| 31450 / 31451 | anomaly / anomaly | 90 | (7981,21,8681) to (7988,57,8682) |

The families are `biomesoplenty:anomaly` and `biomesoplenty:monolith`, both
provisional T0. Candidates 31443, 31445, 31448, 31450, 31451 and 31474 have
1,122, 2,617, 2,255, 1,446, 1,959 and 61 matching constructive positions
respectively. Candidate 31443 also has three mismatches. Their raw observations
demonstrate overlap, not generation absence.

Disposition: REVIEWED, EXCLUDED UNDER THE EXISTING PROTOCOL, applying the same
[location observation rule](../protocol.md#location-observation-acceptance) as the
[second control's review](../full-mountainous-r2-without-sparse/README.md#overlap-review-and-disposition).
Keep all six outside density and spatial numerators, preserving raw flags.
No proximity merge, new acceptance exception or reader change is introduced.
The accepted outer-End total is 48 with six additional overlapping T0 candidates
reported separately. Counting all six would add 1.46484375 per 1,000 chunks to
total/T0 only. This sensitivity is not a confidence interval or an adjustment
to the declared numerator. The review uses the hash-bound result's `overlaps`,
`locations` and `location_observations`; no generation was repeated.

## Full census and completed mountainous block

Analysis passed in 10m28.578s (user 10m21.966s, system 0m1.497s).
Output size: 139,479,722 bytes; SHA-256
`a4567909cc50e7fff796c9854df788f47d888ded444488dac4b97b138a9d1959`.
All eleven strata contain 4,096 complete selected chunks, totaling 45,056.
All 50 target classes and installations pass complete trace validation. The
existing implementation and recorded tests are unchanged. The overlap review
above resolves the new disposition requirement under the original rule.

The table projects `strata[label].total_starts` and
`classification.categories[category].count`. Density is count times `1000/4096`.
All categories retain Item 9's provisional rationale, confidence and ambiguity.

| Stratum | Registry starts | Classified locations | T0 | C | T1 | T2 | T3 | T4 | Villages |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| aether | 30 | 3 | 0 | 0 | 0 | 3 | 0 | 0 | 0 |
| earth-orbit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| mars | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| mars-orbit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| moon-orbit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| moon | 12 | 12 | 12 | 0 | 0 | 0 | 0 | 0 | 0 |
| venus | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| overworld | 43 | 4017 | 22 | 8 | 3979 | 6 | 2 | 0 | 3 |
| end-central | 1 | 3 | 2 | 0 | 0 | 0 | 0 | 1 | 0 |
| end-outer | 13 | 48 | 47 | 0 | 0 | 0 | 1 | 0 | 0 |
| nether | 34 | 398 | 16 | 1 | 372 | 7 | 2 | 0 | 0 |

Aether's 27 cloud starts remain excluded terrain. Central End includes the
arrival-platform and dragon-arena lifecycle sites, and outer End includes six
lifecycle gateways. The arena alone lacks anchor height and biome
(NO_LOCATION_HEIGHT); the other 4,374 observed nonregistry locations have biome
attribution. Per-category spatial data retain distances, censoring, clustering
and empty rectangles, and biome exposure retains separate quart-height denominators.

The 32,800 attempts produce 25,411 NO_CONSTRUCTIVE_CONTENT, 2,858 OUTSIDE_FRAME,
4,375 OBSERVED_LOCATION and the six reviewed overlap exclusions. There are no
CONTENT_NOT_PRESERVED dispositions in this run. Attempts and grouped source
locations have different denominators. No excluded source enters accepted counts.

Against the [first baseline](../full-mountainous-r1-baseline/README.md), category
counts agree except Overworld, outer End and Nether. Overworld locations fall
4,039 to 4,017 (T0 -1, T1 -21), while T2 stays six, T3 stays two and villages
stay three. Outer-End locations rise 19 to 48 (T0 +28, T3 +1). Nether locations
fall 426 to 398 (T0 -20, C -1, T1 -8, T3 +1); T2 stays seven.

The second matched control-minus-baseline location differences, subtracting
this result from the [second control](../full-mountainous-r2-without-sparse/README.md),
are Aether +7, Mars +1, Moon +41, Overworld +165, central End +5, outer End +60
and Nether +129. The other four strata remain zero. Overworld T2/T3 differences
are +16/+5 in both repetitions: baseline 6/2 versus control 22/7. Total Overworld
differences vary from +44 to +165. Nether T2/T3 differences are +13/+7 in the
second pair, versus +12/+8 in the first. These comparisons preserve variability
and the separate overlap exclusions; they are not global ratios or measured
fight/interaction rates. All four mountainous worlds now have individual
acceptance; final synthesis must still include the other two seed blocks.

Allocated working bytes for this instance, raw, custody, analysis and outer
archive total 2,194,984,960 (about 2.04 GiB), using the existing shared-inode
accounting. Free space after analysis is 30,601,404,416 bytes (about 28.5 GiB).
Eight worlds and final synthesis/review/audit remain; this is not Item 10 closure.
