# Item 10 baseline density

Status: IN PROGRESS, 2026-09-08.
The [sampling protocol](protocol.md) is frozen as `item10-full-v1`, with
`item10-observer-coverage-v2`: sixteen fresh worlds covering four seeds, two
repetitions and baseline/control arms. All sixteen worlds have individual census and
raw-custody acceptance. The [current handoff](../../MCPACK-NEW-SESSION-HANDOFF.md#current-full-sample-block)
links their authoritative records and current continuation state. The
[second ocean-heavy control](full-ocean-heavy-r2-without-sparse/README.md) failed
with heap exhaustion and remains preserved. The single predeclared
[same-identity retry](full-ocean-heavy-r2-without-sparse-attempt2/README.md) passed
generation and custody but failed census on one incomplete saved Aether chunk.
All five remaining planned worlds and the [final fresh retry](full-ocean-heavy-r2-without-sparse-attempt3/README.md)
passed. The sample contains sixteen complete worlds after eighteen attempts, with
both failures preserved and the frozen configuration unchanged. The complete
category, biome, seed, repetition and spatial comparison follows. Final validation,
review, main delivery and the Items 2 through 10 audit remain incomplete. No tuning
was performed.

The [authorized automated scope](methodology-amendment.md) removes human phases
from Items 10 and 11. No playing workload or recording is required. Provisional
encounter-site density is not observed fights or exploration pacing. The Item 5
methodology amendment passed clean review and main delivery through
[PR22](https://github.com/copeugne/mcpack/pull/22). Earlier diagnostics below retain
their original limited scope and cannot substitute for the full sample.

## Complete Overworld comparisons

All sixteen hash-bound census outputs are integrated below. Every row has exactly
4,096 full selected chunks. Rates are locations per 1,000 chunks, rounded to three
decimals for display. B is the frozen baseline; C omits only Sparse Structures.
Ocean-heavy r2 C uses the final authorized attempt 3. Actionable candidates are
C plus T1 through T4; encounter sites are T1 through T4. These provisional roles
do not establish utility, fights or experienced pacing.

| Accepted world | All | Actionable | Encounter sites | T2 | T3 | Villages |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ordinary r1 B](full-ordinary-r1-baseline/README.md) | 233.154 | 231.201 | 230.957 | 1.709 | 0.000 | 0.244 |
| [Ordinary r1 C](full-ordinary-r1-without-sparse/README.md) | 250.732 | 244.141 | 243.652 | 5.615 | 0.488 | 0.488 |
| [Ordinary r2 B](full-ordinary-r2-baseline/README.md) | 228.271 | 226.318 | 226.074 | 1.709 | 0.000 | 0.244 |
| [Ordinary r2 C](full-ordinary-r2-without-sparse/README.md) | 249.512 | 242.920 | 242.432 | 5.615 | 0.488 | 0.488 |
| [Mountainous r1 B](full-mountainous-r1-baseline/README.md) | 986.084 | 980.469 | 978.516 | 1.465 | 0.488 | 0.732 |
| [Mountainous r1 C](full-mountainous-r1-without-sparse/README.md) | 996.826 | 982.666 | 980.469 | 5.371 | 1.709 | 0.732 |
| [Mountainous r2 B](full-mountainous-r2-baseline/README.md) | 980.713 | 975.342 | 973.389 | 1.465 | 0.488 | 0.732 |
| [Mountainous r2 C](full-mountainous-r2-without-sparse/README.md) | 1020.996 | 1006.592 | 1004.395 | 5.371 | 1.709 | 0.732 |
| [Ocean-heavy r1 B](full-ocean-heavy-r1-baseline/README.md) | 315.918 | 313.232 | 312.988 | 1.709 | 0.488 | 0.244 |
| [Ocean-heavy r1 C](full-ocean-heavy-r1-without-sparse/README.md) | 342.041 | 334.717 | 334.473 | 4.639 | 0.732 | 0.244 |
| [Ocean-heavy r2 B](full-ocean-heavy-r2-baseline/README.md) | 327.393 | 324.463 | 324.219 | 1.709 | 0.488 | 0.244 |
| [Ocean-heavy r2 C](full-ocean-heavy-r2-without-sparse-attempt3/README.md) | 331.543 | 323.975 | 323.730 | 4.639 | 0.732 | 0.244 |
| [Biome-diverse r1 B](full-biome-diverse-r1-baseline/README.md) | 1006.104 | 1000.488 | 999.756 | 1.465 | 0.000 | 0.244 |
| [Biome-diverse r1 C](full-biome-diverse-r1-without-sparse/README.md) | 1031.982 | 1013.916 | 1009.277 | 3.662 | 0.000 | 0.977 |
| [Biome-diverse r2 B](full-biome-diverse-r2-baseline/README.md) | 1015.869 | 1010.010 | 1009.277 | 1.465 | 0.000 | 0.244 |
| [Biome-diverse r2 C](full-biome-diverse-r2-without-sparse/README.md) | 1042.725 | 1024.414 | 1019.775 | 3.662 | 0.000 | 0.977 |

Across both repetitions, Overworld T2 counts are 7 versus 23 for ordinary,
6 versus 22 for mountainous, 7 versus 19 for ocean-heavy, and 6 versus 15 for
biome-diverse. Omitting Sparse Structures increases the observed T2 count in all
eight pairs. T3 counts are respectively 0 versus 2, 2 versus 7, 2 versus 3, and
0 versus 0. Village counts increase from 1 to 2 in ordinary and 1 to 4 in
biome-diverse, while mountainous stays at 3 and ocean-heavy at 1.

This is a distribution contrast under the measurement overlay, including the
mod's spacing/separation and salt interventions. It is not an observer-free causal
effect or permission to tune. T2 control/baseline count ratios range from 2.5 to
22/6 (about 3.667), not a universal fourfold effect. The two repeated T2/T3 totals
agree within each seed/arm, but other locations and raw states vary.

Mountainous and biome-diverse baselines have much larger all-location totals
than ordinary and ocean-heavy, yet fewer T2 dungeons. T1 cache locations dominate
those totals. Ocean-heavy r2 actionable density is slightly lower in control
(323.975 versus 324.463) despite more T2 dungeons. All-location density is not a
dungeon or combat proxy, and unchanged category totals do not prove deterministic
generation.

### Spatial observations

Each of the ten categories has per-stratum nearest-observed distances, boundary
censoring, full-cell dispersion and empty-region measurements in its accepted
output. No coordinate or distance is pooled across dimensions or End strata.
The following ranges summarize those separate outputs; they are not pooled
means, confidence intervals or population bounds. Each category has 176 stratum
results. A finite-window mean needs at least two locations; an uncensored mean
is null if there are no usable neighbors or any boundary-censored neighbor.
Dispersion is population variance/mean across sixteen full 256-chunk cells.
Empty area is the largest rectangle of empty full cells, not an exact empty disk.

| Category | Finite-window mean range, blocks (available strata / 176) | Uncensored means available / 176 | Dispersion range | Empty area range, chunks |
| --- | --- | ---: | --- | --- |
| all_locations | 7.820 to 752.170 (96/176) | 4 | 0.209 to 78.176 | 0 to 4096 |
| T0 | 37.307 to 297.321 (76/176) | 0 | 0.209 to 21.314 | 0 to 4096 |
| C | 117.272 to 913.262 (17/176) | 1 | 0.562 to 2.000 | 768 to 4096 |
| T1 | 7.933 to 819.912 (40/176) | 1 | 0.688 to 78.566 | 0 to 4096 |
| T2 | 118.258 to 1097.605 (51/176) | 1 | 0.352 to 1.625 | 256 to 4096 |
| T3 | 178.811 to 730.414 (27/176) | 0 | 0.625 to 1.420 | 768 to 4096 |
| T4 | null (0/176) | 0 | 0.938 to 0.938 | 2048 to 4096 |
| actionable_candidates | 7.894 to 752.170 (58/176) | 0 | 0.575 to 78.102 | 0 to 4096 |
| encounter_sites | 7.922 to 752.170 (58/176) | 0 | 0.575 to 78.160 | 0 to 4096 |
| villages | 214.730 to 912.140 (9/176) | 0 | 0.875 to 1.479 | 1024 to 4096 |

T4 has one central-End objective in each world and none in other sampled strata.
Its nearest-neighbor means are therefore null, rather than zero distance. Empty
strata retain 4,096 empty chunks; zero-count dispersion remains null. Individual
neighbor lower bounds, censored flags and rectangle coordinates remain available.

Overworld T2 spatial results agree across the two repetitions within each seed
and arm, so each pair of repeated values is displayed once below. Every
corresponding uncensored nearest-neighbor mean is null.

| Seed role, both repetitions | T2 finite-window mean B / C | T2 dispersion B / C | T2 empty area B / C, chunks |
| --- | ---: | ---: | ---: |
| ordinary | 202.078 / 150.040 | 1.420 / 0.693 | 1536 / 256 |
| mountainous | 187.960 / 157.017 | 0.958 / 0.352 | 1024 / 256 |
| ocean-heavy | 214.750 / 139.508 | 1.420 / 0.760 | 1024 / 256 |
| biome-diverse | 250.198 / 139.294 | 0.958 / 0.863 | 2304 / 768 |

The control has smaller observed T2 neighbor means and empty full-cell rectangles
in all eight pairs. Biome-diverse baseline has the largest Overworld T2 empty
rectangle, 2,304 chunks, versus 768 in control. These finite-frame observations
do not establish travel time or perceived exploration gaps.

Derivation: each linked report binds its `all-strata.json` by SHA-256 and gives
the executable census and restore commands. All sixteen input hashes were checked
against those reports. Density fields are `strata.<label>.classification.categories`;
rates equal count times 1,000 / 4,096. Spatial fields are
`strata.<label>.spatial.<category>`: `mean_nearest_observed_blocks`,
`mean_nearest_neighbor_blocks`, `full_cell_variance_over_mean` and
`largest_empty_full_cell_rectangle.area_chunks`. Ranges use non-null values;
availability counts retain null cases. No measurement was rerun for these tables.

## Complete counts outside the Overworld

The same sixteen outputs supply the following all-location counts. Every entry
has a denominator of 4,096 full chunks. Earth orbit, Mars orbit, Moon orbit and
Venus have zero accepted locations in every selected frame, not proven absence
throughout those dimensions. Aether totals exclude the Item 8 terrain-cloud group.

| World | Aether | Mars | Moon | Central End | Outer End | Nether |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Ordinary r1 B | 5 | 0 | 11 | 2 | 26 | 430 |
| Ordinary r1 C | 19 | 0 | 57 | 11 | 91 | 497 |
| Ordinary r2 B | 5 | 0 | 11 | 2 | 26 | 426 |
| Ordinary r2 C | 19 | 0 | 57 | 11 | 70 | 502 |
| Mountainous r1 B | 3 | 0 | 12 | 3 | 19 | 426 |
| Mountainous r1 C | 10 | 1 | 53 | 8 | 85 | 461 |
| Mountainous r2 B | 3 | 0 | 12 | 3 | 48 | 398 |
| Mountainous r2 C | 10 | 1 | 53 | 8 | 108 | 527 |
| Ocean-heavy r1 B | 3 | 0 | 11 | 2 | 19 | 437 |
| Ocean-heavy r1 C | 10 | 0 | 49 | 9 | 57 | 532 |
| Ocean-heavy r2 B | 3 | 0 | 11 | 2 | 73 | 474 |
| Ocean-heavy r2 C | 10 | 0 | 49 | 9 | 57 | 583 |
| Biome-diverse r1 B | 2 | 0 | 12 | 5 | 29 | 452 |
| Biome-diverse r1 C | 8 | 0 | 54 | 11 | 48 | 597 |
| Biome-diverse r2 B | 2 | 0 | 12 | 5 | 39 | 446 |
| Biome-diverse r2 C | 8 | 0 | 54 | 11 | 77 | 560 |

Control all-location totals exceed baseline in Aether, Moon, central End and
Nether for every matched pair. This is not universal across all strata: ocean-heavy
r2 outer End has 73 baseline versus 57 control locations, whereas r1 has 19 versus
57. Mountainous baseline outer End changes from 19 to 48 across repetitions;
biome-diverse control changes from 48 to 77. These differences, including reviewed
exclusions, remain part of the comparison. Mars has one observed location in each
mountainous control and zero in the other frames. Category-specific counts and
spatial fields for all dimensions remain in the linked outputs.

## Complete biome comparisons

The [accepted biome comparisons](accepted-biome-comparisons.json.gz) integrate all
sixteen outputs, 176 strata and 68,217 separate height/biome rows. Every row retains
chunk-center exposure, all ten category counts and corresponding rates. Positive
exposure with no occurrences is an explicit zero; zero exposure gives a null rate.
Eighteen unavailable anchors retain their identities and reasons:

- Every world has one central-End arena with `NO_LOCATION_HEIGHT`.
- Both mountainous controls have `explorify:end_shipwreck` at chunk (505,514),
  anchor (8088,-7,8232), quart Y -2, outside stored biome height.

Five observed locations have zero chunk-center exposure in their biome/height band:
the four mountainous urn caches at (-57,19,-319), quart Y 4, in
`regions_unexplored:muddy_river`, and biome-diverse r1 control urn candidate 28296
at (476,24,354), quart Y 6, in `terralith:desert_canyon`. Their counts remain
positive and rates null. No other unavailable anchor or positive zero-exposure
case occurs in the complete output. These are anchor-versus-column sampling
limitations, not evidence of broken biome placement.

For a readable same-height example, the table shows the two largest baseline
chunk-center exposures at quart Y -8 (block heights -32 through -29) in each
seed's first repetition, with the matching control biome. Selection is by exposure
descending, then biome ID, not by the largest outcome difference. This display
does not replace the complete artifact or pool height bands. Counts are all
provisional locations anchored in that band, not all locations in the biome.

| Seed | Biome | Exposed chunks B / C | Locations B / C | Rate per 1,000 B / C |
| --- | --- | ---: | ---: | ---: |
| ordinary | minecraft:deep_ocean | 1706 / 1706 | 0 / 2 | 0.000 / 1.172 |
| ordinary | minecraft:ocean | 1501 / 1501 | 33 / 33 | 21.985 / 21.985 |
| mountainous | minecraft:deep_dark | 3330 / 3330 | 153 / 134 | 45.946 / 40.240 |
| mountainous | biomesoplenty:redwood_forest | 209 / 209 | 12 / 12 | 57.416 / 57.416 |
| ocean-heavy | minecraft:deep_cold_ocean | 1883 / 1883 | 2 / 2 | 1.062 / 1.062 |
| ocean-heavy | minecraft:cold_ocean | 845 / 845 | 24 / 24 | 28.402 / 28.402 |
| biome-diverse | biomesoplenty:wasteland | 1803 / 1803 | 75 / 75 | 41.597 / 41.597 |
| biome-diverse | terralith:cave/deep_caves | 830 / 830 | 43 / 33 | 51.807 / 39.759 |

At equal exposure in this slice, several biome counts stay identical between
arms, while mountainous deep dark and biome-diverse deep caves have fewer observed
locations in control. This reinforces that total biome opportunity does not
uniformly follow the T2 contrast. It does not isolate a causal biome effect:
the selected seeds, anchor geometry and fresh-world variability remain confounded.
Counts below 30 remain sparse under the protocol; zeroes do not establish absence.

The complete artifact is 463,442 compressed bytes (24,501,837 JSON bytes), SHA-256
`fddc0442ad711866d1d07d3d4aac97df414981a9aaaa213cc92ca192a23d4f9f`.
Each entry binds the accepted census input by SHA-256. The existing
`summarize_biomes` function joins registry anchors by registry ID and chunk X/Z,
uses recorded nonregistry anchors, retains unavailable reasons, and joins exposure
by `(quart_y, biome)`. Its output conserves every stratum's all-location count.
Earlier worlds and accepted census outputs are unchanged. Reproduction uses the
same committed function and commands below, with no new sampler or framework.

Reproduce the committed comparison after restoring/reproducing its accepted
inputs at the paths given in their individual reports. The following command
checks each input identity and deterministically regenerates the complete output,
using only the input identities from the committed comparison:

```sh
uv run --no-sync python - <<'PY'
import gzip
import hashlib
import json
from pathlib import Path
from tools.analyze_structure_density import summarize_biomes

path = Path('evidence/item-10/accepted-biome-comparisons.json.gz')
expected = path.read_bytes()
inputs = json.loads(gzip.decompress(expected))
output = {}
for name, prior in inputs.items():
    raw = Path(f'evidence/raw/item10/{name}-analysis/all-strata.json').read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != prior['input_sha256']:
        raise ValueError(f'accepted census identity mismatch: {name}')
    strata = json.loads(raw)['strata']
    summaries = {label: summarize_biomes(value) for label, value in strata.items()}
    for label, summary in summaries.items():
        counted = sum(row['counts']['all_locations'] for row in summary['rows'])
        counted += len(summary['unavailable_anchors'])
        if counted != strata[label]['classification']['categories']['all_locations']['count']:
            raise ValueError(f'location count not conserved: {name}/{label}')
    output[name] = {'input_sha256': digest, 'strata': summaries}
raw = json.dumps(output, sort_keys=True, separators=(',', ':')).encode() + b'\n'
if gzip.compress(raw, mtime=0) != expected:
    raise ValueError('biome comparison reproduction mismatch')
print('All accepted inputs, location counts and comparison bytes verified.')
PY
```

Validation: the focused biome, census and spatial suite passes 47 tests, including
height separation, overlapping category membership, zero exposure, zero counts,
unavailable anchors and missing/duplicate joins. Ruff check/format and focused
test-file BasedPyright pass. Every real stratum's attributed counts plus unavailable
anchors equals its accepted all-location count. The complete sixteen-world artifact was reproduced byte-for-byte. Final delivery
validation is recorded separately below.

## Failure denominators and uncertainty

All sixteen planned cells have accepted complete censuses, eight matched pairs
and 720,896 selected full chunks. Eighteen attempts include two rejected attempts
for ocean-heavy r2 control: heap exhaustion, then an incomplete saved Aether chunk
following a save exception. The final authorized fresh retry passed after all five
remaining planned worlds. Neither earlier failure is erased, repaired or counted
as zero density. All attempted-run outcomes remain part of the sampling record.

Within the sixteen accepted worlds, the observer's call count differs from grouped
location candidates. The following are direct lengths and disposition counts
from `nonregistry_candidates.attempts`, `locations` and `location_observations`
in their accepted, hash-bound outputs. The five disposition columns partition
the grouped candidates; they do not partition individual observer calls.

| World | Calls | Groups | No constructive content | Outside frame | Observed location | Content not preserved | Reviewed overlap exclusion |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Ordinary r1 B | 28908 | 28632 | 24261 | 3039 | 1332 | 0 | 0 |
| Ordinary r1 C | 29008 | 28703 | 24261 | 3060 | 1376 | 6 | 0 |
| Ordinary r2 B | 28958 | 28667 | 24301 | 3061 | 1304 | 1 | 0 |
| Ordinary r2 C | 28979 | 28713 | 24313 | 3065 | 1333 | 2 | 0 |
| Mountainous r1 B | 32822 | 32615 | 25380 | 2858 | 4375 | 2 | 0 |
| Mountainous r1 C | 32787 | 32601 | 25418 | 2858 | 4322 | 3 | 0 |
| Mountainous r2 B | 32800 | 32650 | 25411 | 2858 | 4375 | 0 | 6 |
| Mountainous r2 C | 32854 | 32681 | 25332 | 2877 | 4468 | 2 | 2 |
| Ocean-heavy r1 B | 28579 | 28394 | 24105 | 2617 | 1669 | 3 | 0 |
| Ocean-heavy r1 C | 28648 | 28427 | 24078 | 2630 | 1718 | 1 | 0 |
| Ocean-heavy r2 B | 28700 | 28531 | 24122 | 2625 | 1773 | 1 | 10 |
| Biome-diverse r1 B | 33034 | 32772 | 25400 | 2859 | 4511 | 2 | 0 |
| Biome-diverse r1 C | 33086 | 32777 | 25388 | 2857 | 4526 | 6 | 0 |
| Biome-diverse r2 C | 33020 | 32766 | 25350 | 2855 | 4561 | 0 | 0 |
| Biome-diverse r2 B | 33074 | 32775 | 25357 | 2860 | 4553 | 5 | 0 |
| Ocean-heavy r2 C attempt3 | 28688 | 28503 | 24194 | 2627 | 1678 | 2 | 2 |

No constructive content means the candidate did not produce the required content;
it is not a failed server run. Outside-frame candidates remain excluded by the
declared geometry. Saved-content mismatches remain excluded under the existing
acceptance rule, even if a writer previously reported a successful operation.
The individual records retain coordinates and content checks. Registry starts
are counted separately, so observed nonregistry locations alone do not equal
the all-location totals in the complete dimension tables above.

The raw overlap disposition stays `OVERLAP_REVIEW_REQUIRED`; the two mountainous
r2 reports supply its completed human-readable review and exclusion. They do not
rewrite the raw flags. Counting all six excluded baseline T0 candidates would
raise its outer-End total from 48 to 54; counting the two control candidates would
raise its total from 108 to 110. Their contributions are respectively 1.46484375
and 0.48828125 locations per 1,000 chunks. These are explicit sensitivity cases,
not corrected estimates, confidence intervals or permission to change numerators.
They affect total/T0 counts, not T2/T3 counts. Content mismatches, biome attribution
limits and boundary-censored distances remain separate issues with their own
denominators; none is converted into an omnibus failure rate.
The new ocean-heavy r2 baseline separately excludes ten reviewed T0 candidates;
its linked report gives the 73-to-83 outer-End sensitivity and all five overlap pairs.
The [final ocean-heavy control](full-ocean-heavy-r2-without-sparse-attempt3/README.md)
excludes two reviewed T0 anomalies, with a 57-to-59 sensitivity (0.48828125 per
1,000 chunks). Its raw overlap flags also remain unchanged.

The four selected seeds are not a random sample. All four now have accepted
worlds. The [biome-diverse r1 baseline](full-biome-diverse-r1-baseline/README.md)
and [its control](full-biome-diverse-r1-without-sparse/README.md), together with
[repetition 2](full-biome-diverse-r2-baseline/README.md), form two matched pairs.
Ordinary and mountainous also each have two complete matched pairs;
ocean-heavy now also has two. Fresh-repetition
variation remains visible in the tables and raw outputs. Two repetitions do not
support a reliable tail estimate or a confidence interval for all generated worlds.
The raw sampling boundaries censor distances, and all sparse categories retain
their small counts. Successful-run results are conditional on completion; these
runtime failures preclude a claim that the full planned sample completed reliably.

## Verified dependencies and delivery

Initial dependency inspection used main `edd1dcf9f210097934b17aaa0e054d954077feb4`.
PR22 subsequently delivered the preparation to main at `0a1d9f8f6e0df266eb1f9e1080611c648babf2de`.
GitHub metadata confirms PR18, PR19, PR20 and PR21 are MERGED, respectively at
`326979dd2eee7da3f881f1316eb845fb16e8ea6b`,
`be64d458fee3539e5132049d871d1c32ebc3655b`,
`7cbe06c7d8b074fa6121c1143432d28d02996712` and that main commit.
The pushed `3f758cb2114c9e4880e43307e74ca3ddf4df9977` is not a main ancestor;
its single change is the historical archive reference filename.

Items 5 through 9 supply accepted methodology, configuration, worldgen,
inventory and classification. Reuse their evidence, without redoing their gates.
The existing Item 7 missing-final-review exception remains as recorded in the
execution ledger section 5.7. No missing review is inferred to have occurred.

Direct SHA-256 inspection matched these accepted inputs:

| Input | SHA-256 |
| --- | --- |
| `../item-3/runtime/retained-server-candidates.txt` | `78e5bdc0697299782a535400ad5b313c088e8db10cfe075085ae4c8a531e30cb` |
| `../item-6/generated-config-manifest.json` | `2e0aaeb0f84747a3cb17146eb435d34cc7d6703b9372211e8fc8cff2df2b436f` |
| `../item-6/config-audit.json` | `181e0c299f44ded319d93c84f7b983738364b4090286251b00421fa041b989dd` |
| `../../test-environment/seed-suite.json` | `de5e5e89bd04b6f75dac4eab2e84524956f46faa91660b5315c8eade269d39ae` |
| `../item-8/inventory.json` | `4f7853b7b6531f99d3f0592b2129291d2e0cf24b4ad5d1381b3883dbdcfbc52d` |
| `../item-9/classification.md` | `dc78d81691401bad9fc646f1fe790b14bbf1341f595db5e6cbec9a4f1111b710` |

Runtime pins remain Minecraft 1.21.1, NeoForge 21.1.249, Temurin
21.0.12.1+1-LTS, archive SHA-256
`ce79869e1307ed8ee1e2baa86a412b1eb5b75d10a01006d788a6f968bcfaee94`,
and `-Xms1G -Xmx4G`. Item 7's 136-JAR retained runtime digest is
`4062d6179218916c703269f113663b1e078adebbf6d43a691e692d972e07ac50`.
Its hash-verified Chunky overlay uses `Chunky-NeoForge-1.4.23.jar`, SHA-256
`d72f235cf1f56f2c374f52c00bdda5034524b28142305a84cfc123a3f92ad274`;
the instrumented 137-JAR digest is
`e2dab4c80cff137d747bd035588882797f85fa8d4d5b6ccb98a5d717fa0749c8`.
These are accepted source identities, not verification of a new runtime tree.
Each future materialization must verify its actual files and Java executable.

## Available evidence versus missing measurements

The [Item 5 protocol](../../measurement/item5/protocol-v1.json) defines
denominators, repetitions, retained failures and uncertainty. Its original density
contracts use player cases, 900-second warm-up and 3,600-second observations.
The later [authorized amendment](methodology-amendment.md) supersedes those
collection contracts for Items 10 and 11. The original observed-combat metric
remains historical; the active automated metric is provisional encounter-site
density. Exclusive T2 and T3 categories supply proper-dungeon and
major-expedition counts, with T4 objectives reported separately.

The [reconstructed stage geometry](../../measurement/structure-density-v0.1.json)
is a proposal scaffold, not accepted raw evidence. Its four nested rectangles
have 4,096, 8,192, 16,384 and 32,768 chunks per seed, stopping at 30 observations
per category or the ceiling with sparse categories retained. Historical Item 10
counts and its claimed absent Sparse Structures runtime are not reusable results.

The accepted [Item 7 protocol](../item-7/protocol/worldgen-audit-v1.json), r14
archives, Anvil/NBT decoder, frozen-config materializer and archive/restore tools
are reusable. Its selections and targeted provider-gap observations were designed
for worldgen inspection, not Item 10's density stopping rule. They can inform
cost and methods, but cannot be silently relabeled as new Item 10 experiments.
The old density counter accepts a caller-supplied denominator and has no spatial
analysis; it cannot establish Item 10's exit gate as written.

The accepted inventory and classification are integrated without reinvestigation:
448 active canonical families, comprising 408 registry and 40 nonregistry
families. The latter have empty `structure_ids`; saved structure-start counting
cannot observe them. Their existing provider evidence supplies the separate
occurrence method in the
[frozen protocol](protocol.md#location-observation-acceptance).
Pieces, references, pools and aliases must not become additional starts.

Sparse Structures is present in the retained manifest, artifact SHA-256
`5aca0b33c0c83154810bbdd8ddc0d3e6a3e4591577274e2d27c10de0b45f2a45`.
Its [untouched configuration](../item-6/frozen/config/sparsestructures.json5)
has `spreadFactor: 2`, `idBasedSalt: true` and a mansion override of 2.
These configuration facts resolve presence and intent. The eight accepted
matched pairs across all four seeds measure realized differences above.
Do not infer a fourfold density reduction or a zero contribution.

Direct reuse of the accepted disassemblies resolves the mutation mechanism.
The three disassembly files below were hash-checked against
[existing identities](../item-8/sources/sparsestructures-provider/identities.json)
on 2026-09-08. Their parent is
`../item-8/sources/sparsestructures-provider/sparsestructures-neoforge-1.21.1-3.0.jar/`:

- `io.github.maxencedc.sparsestructures.mixin.MakeStructuresSparse.txt`,
  `loadElementFromResource` offsets 0 to 59: only resource-loaded
  `worldgen/structure_set` JSON enters this path; `minecraft:concentric_rings`
  returns before any change. Offsets 100 to 202 multiply present spacing and
  separation by the selected factor, truncate to Java integers, and repair
  separation greater than or equal to spacing by setting spacing to at least 1
  and separation to spacing minus 1. Missing fields initially use 1. This is
  a JSON-load intervention, not evidence that every runtime-generated placement
  traverses it.
- `io.github.maxencedc.sparsestructures.SparseStructuresConfig.txt`,
  `getSpreadFactor` offsets 0 to 116: the first custom entry matching the set ID
  or any member structure replaces the global factor. It does not multiply the
  global factor. The mansion override of 2 therefore remains 2, not 4.
- `io.github.maxencedc.sparsestructures.mixin.MakeStructuresSparse.txt`,
  offsets 205 to 235, and `io.github.maxencedc.sparsestructures.IdBasedSalt.txt`,
  `getSalt` offsets 0 to 10: enabled ID-based salt replaces the salt with Java
  `Math.abs(setId.hashCode()) % 2147483647`. Reproduction must preserve Java
  signed-integer behavior, not substitute a Python hash or unsigned hash.

Consequently, a factor-1 configuration with ID-based salt still enabled would
not isolate the mod's total contribution. No such control has been run. The
[declared control](protocol.md#sparse-structures-control-contrast) instead omits
only Sparse Structures and retains both fresh repetitions. It measures removal
within the retained stack, including spacing/separation and salt interventions.
Individual changed locations cannot all be causally assigned to that omission:
within-arm generation variability remains in the matched results. The complete
four-seed comparison above resolves the declared descriptive contrast, with that
causal limitation retained.

The accepted [dimension capture](../item-8/runtime/dimension-r3/dimension-biomes.json)
includes Aether and CreatingSpace. The frozen eleven-stratum frame includes those
dimensions and supersedes the incomplete four-stratum draft. Unobserved families
remain unobserved, not impossible or absent from the runtime.

## Exit-gate reassessment (2026-09-08)

The user paused new experiments and PR creation and directed one consolidated
remaining Item 10 delivery after the existing reviews. SPECS Item 10 requires
representative regions across the four selected seeds, all declared category
densities, category distances, clustering, empty regions, biome/seed comparisons
and Sparse Structures attribution. Identity, complete denominators, retained raw
observations, failure/censoring/uncertainty, deterministic processing, durable
restore, review/merge and the subsequent Items 2 through 10 audit remain required.

Natural positive capture for every generator is not a specification requirement.
The separate positive-pilot gates were implementation choices. Their failed or
unmet outcomes remain unchanged, but they do not require further searches for
positive examples before the full fixed sample. What is required is evidence that
every applicable occurrence mechanism is observable, preserves behavior and is
attributed correctly. A completed trace with correctly installed hooks can record
no calls; a failed hook, unavailable event stream or unhandled failure cannot be
reported as zero. Corroborate representative actual writes when observed. Do not
invent a positive example, extrapolate from static density or erase uncertainty.

The following table records the gaps at the reassessment checkpoint. Current
implementation and collection status follows it.

| Requirement at reassessment | Evidence gap at that checkpoint | Required work |
| --- | --- | --- |
| Complete occurrence observation | Registry starts omit the 40 accepted nonregistry families. Existing hooks and source records cover many mechanisms, but procedural pillars, BetterEnd post-template effects and applicable End routes are not fully integrated. | Finish only the missing writer boundaries in the existing observer. Integrate accepted lifecycle applicability and report lifecycle observations separately; the specification does not require a new campaign to trigger every possible lifecycle event. |
| Accepted location numerators | Traces contain block writes, template parts, failed attempts and halo activity. Their totals are not distinct selected-area locations. | Implement the existing family join, occurrence identity/inclusion and last-write/anchor interpretation in the existing processing path. Preserve zeroes, refusals and uncertainty. |
| Full comparative measurements | The small pilots are not the declared four-seed, two-arm sample. Existing static analysis works for registry pilots but does not supply the missing populations or matched control. | Freeze the complete collector/control identities and sampling protocol, run the full sample, then apply deterministic category/spatial/biome analysis. |
| Sparse Structures contribution | Packaged placement rules explain a mechanism but are not the matched observed distribution. | Materialize the exact omit-only-Sparse-Structures control and retain matched repetitions without claiming observer-free causal certainty. |
| Storage, final report and delivery | Current capacity cannot hold full collection. No complete result or cross-item audit exists. | Resolve storage, retain and restore raw evidence, write the complete report, finish the existing PR33/34 obligations, then use one remaining delivery PR with coherent intermediate commits and the required audit. |

The 4,096 chunks per stratum, two repetitions and 16 total worlds are
sampling-design choices, not numbers mandated by SPECS. They are retained in
the frozen `item10-full-v1` protocol; this reassessment does not reduce the measurement scope.
No additional tiny per-generator pilots, new evidence framework or tooling-only
PR is authorized by this reassessment. Synthetic preservation checks and immutable
source inspection address collector correctness; the full declared sample supplies
the missing measurement. Existing diagnostics and their limitations remain intact.

The implementation portion of the table above is now integrated: the existing
collector covers the remaining writers, the reader joins actual locations and
saved biomes, and the runner materializes the exact Sparse Structures control.
The [frozen observer gate](protocol.md#frozen-observer-and-full-trace-gate) pins
source/JAR identity and enforces coverage-v2, including the narrowly verified
unexercised Gateway case. The [current handoff](../../MCPACK-NEW-SESSION-HANDOFF.md)
links the applicable validation and accepted full-world results. Storage and
prior reviews, all sixteen world censuses and combined synthesis are resolved.
Final validation and delivery remain incomplete; runtime acceptance is established
per world, not from tests.

### Storage decision before collection

Historical checkpoint: the pre-collection check reported 3,949,314,048 free bytes (about 3.7 GiB). The existing
r3-based estimate is 10.71 generation hours and 13.50 GiB of original worlds.
As a second retained proxy, the [fairy world backup](fairy-run-r1/world-backup.json)
has 127,859,839 world bytes; its [raw manifest](fairy-run-r1/archive-manifest.json)
has 81,693,301 raw member bytes and a 76,943,807-byte archive for 6,852 selected chunks. Scaling by
720,896 / 6,852 gives 12.53 GiB of original worlds, or 56.14 GiB if every original,
raw copy, archive, downloaded archive, restored raw tree and restored world is
kept locally. Those are planning proxies, not measured full-collector costs.

Avoid retaining redundant new verification workspaces indefinitely. Plan roughly
30 GiB of persistent free space for original worlds, one local raw archive set,
published redundant copies and sequential verification workspace, with the first
complete ordinary-seed run confirming actual cost before continuing. Remove only
new explicitly temporary download/restore copies after successful verification;
all preexisting evidence, worlds, backups and protected artifacts remain intact.
That capacity gate was subsequently resolved before full collection. The
[ninth accepted world](full-ocean-heavy-r1-baseline/README.md#full-census-acceptance)
records 1.86 GiB of allocated working storage and 26.4 GiB remaining free.
Continue capacity checks; no additional cleanup is authorized by this record.

## Smallest complete deliverable and batches

1. Resolve measurement semantics and storage, then freeze the Item 10 protocol
   before collection. Record exact geometry, population, dimension strata,
   occurrence rules, endpoints, repetitions and Sparse Structures attribution.
2. Complete one ordinary-seed stage end to end: fresh verified materialization,
   generation, marker-correlated flush, clean stop, offline slot verification,
   raw preservation and deterministic category/spatial analysis. Preserve any
   failure without silently replacing it. Use this to validate costs and method.
3. Apply the frozen stages across all four seeds. Retain every denominator,
   failure, missing slot, invalid start, nonregistry limitation and sparse result.
   Apply the authorized automated category definitions; do not claim observed fights.
4. Finish Sparse Structures attribution, final analysis, archive restore and
   clean-checkout reproduction. Push the coherent milestones, open the main PR,
   complete Codex review/fix cycles, merge and verify delivered main.
5. Audit Items 2 through 10 for identity and narrative consistency. Do not touch
   Item 11 workflows before the audit. Neither item requires human sessions.

The [protocol](protocol.md) selects one fixed 4,096-chunk rectangle in each of
four seeds and eleven strata, with two fresh repetitions in each of two arms.
It defines coordinate inclusion, spatial cells, biome attribution, boundary
censoring, sparse-category limits and a control omitting only Sparse Structures.
This supersedes the inherited nested-stage draft. Each full-world acceptance
requires complete occurrence capture and exact experiment identities; all sixteen
worlds have passed.

Done means every Item 10 bullet has a measured result or a specification-approved
disposition, source-bound deterministic processing, retained raw evidence with
hashes and tested restore, explicit uncertainty and failure dispositions, clean
final review, merged delivery and the subsequent cross-item audit. The authorized
scope does not require observed combat or human sessions in Items 10 or 11.

## Resource estimate and unresolved gates

The pre-collection [protocol resource estimate](protocol.md#runtime-and-storage-estimate)
was: 720,896 selected chunks across 16 worlds,
about 11.05 automated generation hours and 13.92 GiB cumulative uncompressed
world data, using the measured r3 proxy and including the requested generation
edge outside the census. Sequential custody has a provisional
5 GiB workspace floor. Actual per-world costs are recorded in each accepted
world report and supersede proxy estimates for the completed runs. Recheck
capacity before each experiment; these are estimates, not promised runtimes.
The human collection matrix is superseded by the delivered
[methodology amendment](methodology-amendment.md).

Measured resource totals from the eighteen attempt receipts are 10,498.585
seconds of generation lifecycle time, 7,624,672,105 uncompressed world-file bytes
and 2,881,277,781 bytes of outer raw archives. The sixteen accepted worlds alone
account for 9,248.937 seconds, 6,806,284,224 world bytes and 2,574,764,666 archive
bytes. These exclude census time, downloaded/restored copies, runtime binaries,
separate diagnostic supplements and other workspace overhead. They are not host
capacity requirements or a performance benchmark. Derivation: sum
`run.lifecycle.duration_seconds`, each raw `world-backup.json.world_files.size_bytes`,
and `archive-manifest.json.archive_size_bytes` over the sixteen comparison inputs
and the two explicitly linked failed attempts. The failed heap-run duration includes
its recorded emergency shutdown. No estimated total replaces these observations.

Remaining validation and delivery work:

- Preserve all accepted worlds and both failed attempts while completing delivery.
- Complete clean-checkout reproduction, final review, main delivery and the
  Items 2 through 10 audit. Keep Item 11 workflows untouched.

The observer and control methods are implemented. Reuse them; add no generic
framework or tuning while completing validation and delivery.

[Decoder preparation validation](decoder.md) records the custom-dimension
identification fix and validated authoritative-start-coordinate extraction.
