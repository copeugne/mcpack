# Ocean-heavy repetition-1 baseline

Status: BASELINE-WORLD ACCEPTANCE PASS.
Nine of sixteen worlds are individually accepted. Protocol: `item10-full-v1`, with
`item10-observer-coverage-v2`. Seed: `95920844204830198`.
Generation source: `5367d2dd664311033b57da448d0fc4a781ca0e8c`.

The unchanged [run receipt](run.json) records all eleven selections completed,
readiness, correlated save flush, clean stop, Java exit 0 and no process-group
kill or rejection. Duration: 512.546 seconds. All 228 frozen files and eleven
declared Chunky files pass capture. No fixture or before-generation commands
were used. No configuration tuning was performed.

Direct comparison with the [preceding baseline](../full-mountainous-r2-baseline/run.json)
finds identical `probe` and lifecycle `selections`. `run.preflight` differs only
in the declared `seed` and `seed_role`, preserving exact runtime/configuration
identity across these seed blocks. Generation is not observed gameplay validation.

## Raw custody

The stopped world backup contains 502 files totaling 425,870,731 bytes.
`world.tar.gz` is 159,097,965 bytes, SHA-256
`500ea7c8f66cbdf42913fece569adcb486e35b554962cf5bd43d759aeebb6ff0`.
The [world restore](world-restore.json) verifies all 502 files in a new target.

The immutable [release](https://github.com/copeugne/mcpack/releases/tag/item10-full-ocean-heavy-r1-baseline-5367d2dd)
contains the raw archive and [manifest](archive-manifest.json). Its fetched tag
resolves to the generation source above. Archive size: 159,477,835 bytes;
SHA-256 `055608001b2b17a070a41ae8622f4cfd2ff1ce37f34094f94524bb2611c26b71`.
Its 313 files total 183,094,130 bytes before compression. Manifest SHA-256:
`ec89d0df58d22b96576453d410774b4976cee5b0f896ffca82f23c513f078d7d`.
The [local restore](local-restore.json) and [downloaded restore](download-restore.json)
each verify all 313 members, and the downloaded manifest matches byte-for-byte. There are 50
incoming target classes; all pass complete trace validation.

## Reproduction

Use the existing [custody procedure](../full-ordinary-r1-without-sparse/README.md#reproduction)
with this run's name, source, archive and world hash. Create output parents first;
each output must be absent. Executed generation and archive commands:

```sh
uv run --no-sync python -m tools.run_item10_probe --name full-ocean-heavy-r1-baseline --mode probe --preset item10 --role ocean-heavy --arm baseline --repetition 1
uv run --no-sync python -m tools.archive_item7_evidence create --root evidence/raw/item10/full-ocean-heavy-r1-baseline --archive evidence/raw/item10/item10-full-ocean-heavy-r1-baseline-5367d2dd.tar.gz --manifest evidence/item-10/full-ocean-heavy-r1-baseline/archive-manifest.json --revision 5367d2dd664311033b57da448d0fc4a781ca0e8c
```

Raw observations and existing diagnostics remain unchanged. Generation and raw
custody do not establish density, gameplay, or Item 10 completion.

The full census completed as session `96485`, exit 0, using analysis implementation
`760aa2f5`. Executed command:

```sh
uv run --no-sync python -m tools.analyze_structure_density evidence/raw/item10/full-ocean-heavy-r1-baseline-custody/restored-world/world evidence/raw/item10/full-ocean-heavy-r1-baseline-analysis/all-strata.json --all-strata --dimension-geometry evidence/item-10/dimension-geometry.json --trace-root evidence/raw/item10/full-ocean-heavy-r1-baseline-custody/restored-local --trace-manifest evidence/item-10/full-ocean-heavy-r1-baseline/archive-manifest.json
```

Timing and diagnostics are retained beside the output in `all-strata-runtime.txt`.

## Full census acceptance

Analysis passed in 7m43.150s (user 7m38.158s, system 0m1.292s).
Output size: 83,901,297 bytes; SHA-256
`9c2ed4cf58b38f20a0cf7f65c50b2a9f90ac9539722220c67d2cfa7556d3dec7`.
All eleven strata contain 4,096 complete selected chunks, totaling 45,056.
All 50 target classes and installations pass complete trace validation; no target
is unexercised. The existing implementation and its recorded tests are unchanged.

The table projects `strata[label].total_starts` and
`classification.categories[category].count`. Density is count times `1000/4096`.
Categories retain Item 9's provisional rationale, confidence and ambiguity.

| Stratum | Registry starts | Classified locations | T0 | C | T1 | T2 | T3 | T4 | Villages |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| aether | 32 | 3 | 0 | 0 | 0 | 3 | 0 | 0 | 0 |
| earth-orbit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| mars | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| mars-orbit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| moon-orbit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| moon | 11 | 11 | 11 | 0 | 0 | 0 | 0 | 0 | 0 |
| venus | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| overworld | 28 | 1294 | 11 | 1 | 1273 | 7 | 2 | 0 | 1 |
| end-central | 0 | 2 | 1 | 0 | 0 | 0 | 0 | 1 | 0 |
| end-outer | 16 | 19 | 18 | 0 | 0 | 0 | 0 | 1 | 0 |
| nether | 39 | 437 | 22 | 1 | 407 | 5 | 2 | 0 | 0 |

Aether's 29 cloud starts remain excluded terrain. The arena alone lacks anchor
height and biome (NO_LOCATION_HEIGHT); the other 1,668 observed nonregistry
locations have biome attribution. Per-category spatial data preserve distances,
censoring, clustering and empty rectangles. Biome exposure preserves separate
quart-height denominators. Lifecycle sites remain distinguishable from ordinary
generation and do not establish observed gameplay.

The 28,579 attempts produce 24,105 NO_CONSTRUCTIVE_CONTENT, 2,617 OUTSIDE_FRAME,
1,669 OBSERVED_LOCATION and three CONTENT_NOT_PRESERVED grouped source locations.
Attempt and grouped-location denominators differ. No overlaps were reported.
The three excluded cave-urn caches are candidates 13814 at (-58,-47,326), 13913
at (-62,-47,331) and 24662 at (487,-30,180), with two, one and two mismatching
positions respectively. These retained failures remain outside accepted counts.
The derivation uses `location_observations` joined to `locations` by candidate ID.

This completes the first ocean-heavy baseline. Its matched control and second
repetition remain necessary before attributing differences to Sparse Structures.
Allocated working bytes for this instance, raw, custody, analysis and outer
archive total 1,998,974,976 (about 1.86 GiB), using shared-inode accounting with
candidate, pristine and preceding instance trees counted first. Free space after
analysis is 28,393,357,312 bytes (about 26.4 GiB). Seven worlds and final
synthesis/review/audit remain; this is not Item 10 closure.
