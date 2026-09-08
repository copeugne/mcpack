# Mountainous repetition-2 Sparse Structures control

Status: CONTROL-WORLD ACCEPTANCE PASS, with two reviewed overlap exclusions.
Seven of sixteen worlds are individually accepted. Protocol: `item10-full-v1`, with
`item10-observer-coverage-v2`. Seed: `6671238423019257953`.
Generation source: `1632e3de907f7c2c63a48677926ffe0de71324b2`.

The unchanged [run receipt](run.json) records all eleven selections completed,
readiness, correlated save flush, clean stop, Java exit 0 and no process-group
kill or rejection. Duration: 663.491 seconds. All 228 frozen files and eleven
declared Chunky files pass capture. No fixture or before-generation commands
were used. Both arms use probe mode with the frozen observer.

Direct comparison with the [first control](../full-mountainous-r1-without-sparse/run.json)
finds identical `run.preflight`, `probe` and lifecycle `selections`; only the
repetition and fresh instance change. This reuses the same exact Sparse Structures
omission, seed, configuration and sampling identity rather than tuning the control.

## Raw custody

The stopped world backup contains 501 files totaling 444,441,718 bytes.
`world.tar.gz` is 179,912,028 bytes, SHA-256
`d51f2724b033e788becb2a4b04f93c96bab53384c3afed0df9eb3ae58783a760`.
The [world restore](world-restore.json) verifies all 501 files in a new target.

The immutable [release](https://github.com/copeugne/mcpack/releases/tag/item10-full-mountainous-r2-without-sparse-1632e3de)
contains the raw archive and [manifest](archive-manifest.json). The fetched tag
resolves to the generation source above. Archive size: 180,748,230 bytes;
SHA-256 `2587ce92a4153006394c7350a5d4137bd1d51fc4a6d4ea79ef8c0be3fd22ad73`.
Its 313 files total 218,269,209 bytes before compression. Manifest SHA-256:
`fb689f40dc8a5651e99afd6e78e83b41a1bea723bedb8b64aaa094ac3a021cd5`.
The [local restore](local-restore.json) and [downloaded restore](download-restore.json)
each verify all 313 members; downloaded and local manifests match byte-for-byte. There are 50
incoming target classes; complete trace acceptance still awaits census analysis.

## Reproduction

Use the existing [custody procedure](../full-ordinary-r1-without-sparse/README.md#reproduction)
with this run's name, source, archive and world hash. Create output parents first;
each output must be absent. Executed generation and archive commands:

```sh
uv run --no-sync python -m tools.run_item10_probe --name full-mountainous-r2-without-sparse --mode probe --preset item10 --role mountainous --arm without-sparse --repetition 2
uv run --no-sync python -m tools.archive_item7_evidence create --root evidence/raw/item10/full-mountainous-r2-without-sparse --archive evidence/raw/item10/item10-full-mountainous-r2-without-sparse-1632e3de.tar.gz --manifest evidence/item-10/full-mountainous-r2-without-sparse/archive-manifest.json --revision 1632e3de907f7c2c63a48677926ffe0de71324b2
```

Raw observations and existing diagnostics remain unchanged. Generation and raw
custody do not establish density, gameplay, or Item 10 completion.

The full census completed as session `95707`, exit 0, using analysis implementation
`760aa2f5`. Executed command:

```sh
uv run --no-sync python -m tools.analyze_structure_density evidence/raw/item10/full-mountainous-r2-without-sparse-custody/restored-world/world evidence/raw/item10/full-mountainous-r2-without-sparse-analysis/all-strata.json --all-strata --dimension-geometry evidence/item-10/dimension-geometry.json --trace-root evidence/raw/item10/full-mountainous-r2-without-sparse-custody/restored-local --trace-manifest evidence/item-10/full-mountainous-r2-without-sparse/archive-manifest.json
```

Timing and diagnostics are retained beside the output in `all-strata-runtime.txt`.

## Overlap review and disposition

The census initially flags two in-frame candidates as OVERLAP_REVIEW_REQUIRED:
31442 (`biomesoplenty:anomaly`, anchor 8634,57,8358, attempt 31515) and
31487 (`biomesoplenty:monolith`, anchor 8639,62,8359, attempt 31516). Both are
ordinary generation in outer End and are provisionally T0 under Item 9.
Their constructive-content sets share exactly (8639,53,8359) and (8639,53,8361).
The archive-bound trace records successful null_end_stone writes by attempt
31515 and successful obsidian writes by attempt 31516 at both positions. Saved
observations are obsidian. The anomaly retains 993 matching constructive positions
and two mismatches; the monolith retains 75 matches. These are overlapping source
groups, not evidence of an observer failure or two generation zeros.

Disposition: REVIEWED, EXCLUDED UNDER THE EXISTING PROTOCOL. The protocol's
[location observation rule](../protocol.md#location-observation-acceptance)
requires overlaps to be reported separately rather than accepted as locations.
Keep both candidates excluded from density and spatial numerators. Do not invent
a proximity merge or change the reader to accept this observed case. The raw
OVERLAP_REVIEW_REQUIRED labels remain unchanged; this paragraph records the
completed review and exclusion, not an alteration of the raw result.

The outer-End accepted count is therefore 108, with two additional overlapping
T0 candidates reported separately. Counting both would add two to total/T0 only
(0.48828125 per 1,000 chunks); this sensitivity is not a confidence interval or
a correction to the declared count. Two other overlap pairs, 31473/31502 and
31479/31481, share three and twelve positions respectively, but all four anchors
are OUTSIDE_FRAME and remain excluded by sample geometry.

Derivation: inspect `nonregistry_candidates.overlaps`, `locations`,
`location_observations` and `saved_content.observations` in the hash-bound result
below. The existing `collection_attempts` iterator was fully consumed with this
archive's trace/class hashes and `require_complete_observer=True`; the listed
write events were selected by attempt ID and shared position. This validates
the source evidence without rerunning generation or modifying accepted data.

## Full census and control repetition comparison

Analysis passed in 10m50.946s (user 10m44.342s, system 0m1.621s).
Output size: 147,929,941 bytes; SHA-256
`a96a0a04bbf370871ce4aa51821cd8b7d5e00876ebf2d227ab981fcb731f8873`.
All eleven strata contain 4,096 complete selected chunks, totaling 45,056.
All 50 target classes and installations pass complete trace validation. The
reader and its previously recorded tests are unchanged; the overlap review
above resolves the only new acceptance question without a new rule.

This table projects `strata[label].total_starts` and
`classification.categories[category].count`. Density is count times `1000/4096`.
All categories retain the provisional Item 9 rationale, confidence and ambiguity.

| Stratum | Registry starts | Classified locations | T0 | C | T1 | T2 | T3 | T4 | Villages |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| aether | 117 | 10 | 0 | 0 | 1 | 9 | 0 | 0 | 0 |
| earth-orbit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| mars | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| mars-orbit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| moon-orbit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| moon | 53 | 53 | 53 | 0 | 0 | 0 | 0 | 0 | 0 |
| venus | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| overworld | 130 | 4182 | 59 | 9 | 4085 | 22 | 7 | 0 | 3 |
| end-central | 6 | 8 | 7 | 0 | 0 | 0 | 0 | 1 | 0 |
| end-outer | 68 | 108 | 101 | 0 | 5 | 0 | 2 | 0 | 0 |
| nether | 153 | 527 | 98 | 2 | 398 | 20 | 9 | 0 | 1 |

Aether retains 107 excluded cloud starts. Central End includes arrival-platform
and dragon-arena lifecycle sites; outer End includes one lifecycle gateway.
The arena alone lacks anchor height and biome (NO_LOCATION_HEIGHT); the other
4,467 observed nonregistry locations have biome attribution. Per-category spatial
outputs retain observed distances, censoring, cell dispersion and empty regions;
biome exposure retains its quart-height denominators.

The 32,854 attempts produce 25,332 NO_CONSTRUCTIVE_CONTENT, 2,877 OUTSIDE_FRAME,
4,468 OBSERVED_LOCATION, two CONTENT_NOT_PRESERVED and two reviewed overlap
exclusions. Attempts and grouped locations have different denominators. Content
exclusions are cave-urn candidates 21271 at Overworld (223,-40,27) and 26168 at
(40,-12,-122), each with one saved-content mismatch. No excluded candidate enters
the accepted numerator, and its raw observations remain retained.

Against the [first mountainous control](../full-mountainous-r1-without-sparse/README.md),
all category counts agree except Overworld, outer End and Nether. Overworld
locations rise 4,083 to 4,182 (T0 +1, T1 +98), while T2 stays 22, T3 stays seven
and villages stay three. Its accepted nonregistry locations comprise 3,856 cave
urns, 191 monster boxes, four scarecrows and one fairy ring. Outer-End locations
rise 85 to 108 despite raw registry starts falling 80 to 68; T0 rises 79 to 101
and T3 rises one to two. Nether locations rise 461 to 527, T2 rises 19 to 20,
T3 stays nine and villages fall two to one. These direct category projections
retain repetition variability rather than claiming deterministic counts.

Allocated working bytes for this instance, raw, custody, analysis and outer
archive total 2,249,265,152 (about 2.09 GiB), using the existing shared-inode
accounting. Free space after analysis is 33,113,833,472 bytes (about 30.8 GiB).
Nine worlds and the final synthesis/review/audit remain; this is not Item 10 closure.
