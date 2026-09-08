# Item 10 baseline density

Status: IN PROGRESS, 2026-09-08.
The [sampling protocol](protocol.md) is frozen as `item10-full-v1`, with
`item10-observer-coverage-v2`: sixteen fresh worlds covering four seeds, two
repetitions and baseline/control arms. Fifteen worlds have individual census and
raw-custody acceptance. The [current handoff](../../MCPACK-NEW-SESSION-HANDOFF.md#current-full-sample-block)
links their authoritative records and current continuation state. The
[second ocean-heavy control](full-ocean-heavy-r2-without-sparse/README.md) failed
with heap exhaustion and remains preserved. The single predeclared
[same-identity retry](full-ocean-heavy-r2-without-sparse-attempt2/README.md) passed
generation and custody but failed census on one incomplete saved Aether chunk.
The user has authorized the five remaining planned worlds, followed by exactly
one fresh attempt-3 control retry under the unchanged frozen configuration.
The target remains sixteen complete worlds; both failures remain preserved. Final combined
biome, seed, repetition and spatial synthesis, review, main delivery and the
Items 2 through 10 consistency audit remain incomplete. No tuning was performed.

The [authorized automated scope](methodology-amendment.md) removes human phases
from Items 10 and 11. No playing workload or recording is required. Provisional
encounter-site density is not observed fights or exploration pacing. The Item 5
methodology amendment passed clean review and main delivery through
[PR22](https://github.com/copeugne/mcpack/pull/22). Earlier diagnostics below retain
their original limited scope and cannot substitute for the full sample.

## Accepted Overworld comparisons (initial ten-world subset)

These are direct values from the ten accepted census outputs, not acceptance of
the full sampling gate. Each row has exactly 4,096 full selected chunks. Rates
are locations per 1,000 chunks, displayed to three decimals. B is the frozen
baseline; C omits only Sparse Structures. Actionable candidates are C plus T1
through T4; encounter sites are T1 through T4. These provisional categories do
not establish utility, fights or experienced pacing.

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

In these five matched pairs, omitting Sparse Structures increases T2 and T3
counts. T2 counts are 7 versus 23 in both ordinary repetitions, 6 versus 22 in
both mountainous repetitions, and 7 versus 19 in the first ocean-heavy pair.
T3 counts are respectively 0 versus 2, 2 versus 7, and 2 versus 3. Village counts
increase only in the ordinary pairs. This is a distribution comparison under the
measurement overlay, not an observer-free causal effect or a basis for tuning.

The much larger mountainous total does not mean more proper dungeons: its baseline
T2 count is six, versus seven in ordinary and ocean-heavy. T1 dominates the total
in these samples. Total counts also vary between fresh repetitions even where
T2/T3 counts remain equal. Do not use all-location density as a dungeon or combat
proxy, or infer deterministic generation from unchanged category totals.

T2 spatial summaries below use the same rows. Ordinary and mountainous values
are identical across their two accepted repetitions, so each is shown once.
Distances are finite-window nearest-observed means in blocks. **Every corresponding
uncensored nearest-neighbor mean is null** because boundary-censored cases remain.
Dispersion is population variance/mean across sixteen full 256-chunk cells;
empty area is the largest rectangle of empty full cells, not an exact empty disk.

| Seed role | T2 finite-window mean B / C | T2 dispersion B / C | T2 empty area in chunks B / C |
| --- | ---: | ---: | ---: |
| Ordinary, r1 and r2 | 202.078 / 150.040 | 1.420 / 0.693 | 1536 / 256 |
| Mountainous, r1 and r2 | 187.960 / 157.017 | 0.958 / 0.352 | 1024 / 256 |
| Ocean-heavy, r1 only | 214.750 / 139.508 | 1.420 / 0.760 | 1024 / 256 |

Derivation: each linked report binds its `all-strata.json` output by SHA-256 and
gives the executable census and raw restore commands. All ten output hashes were
checked against those reports before integration. Read
`strata.overworld.classification.categories.<category>.count` and
`per_1000_chunks` for the first table; the latter is count times 1,000 / 4,096.
For the second table, read `strata.overworld.spatial.T2` fields
`mean_nearest_observed_blocks`, `mean_nearest_neighbor_blocks`,
`full_cell_variance_over_mean` and `largest_empty_full_cell_rectangle.area_chunks`.
These tables directly display existing accepted fields, rounded only for prose.
Individual neighbors, censoring, grid counts and rectangle bounds remain in
those outputs. No world was regenerated and no measurements were recomputed.

Remaining seed/repetition coverage and final synthesis
remain incomplete. The rejected
ocean-heavy r2 control attempts supply no density row and no zero observation.
The [authorized continuation](protocol.md#authorized-continuation-and-final-bounded-retry)
runs the five untouched planned worlds before the final fresh control retry.

## Accepted counts outside the Overworld

The same ten linked census outputs supply the following all-location counts.
Every cell uses 4,096 full chunks; its density is count times 1,000 / 4,096.
Earth orbit, Mars orbit, Moon orbit and Venus each have zero accepted locations
in every one of these worlds. This is observed absence within the selected
frames, not proof that locations are impossible in those dimensions.

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

Direct source fields are `strata.<label>.classification.categories.all_locations.count`.
The census preserves category-specific densities and spatial fields alongside
these totals. Aether counts exclude the Item 8 terrain-cloud group; they are
not raw registry-start totals. Every accepted world has one central-End T4
objective and no T4 locations in the other sampled strata. This fixed objective
is not evidence of a uniform objective distribution. Central and outer End remain
separate exposures, not one contiguous region.

Fresh mountainous repetitions differ substantially in outer End and Nether
totals: baseline outer End is 19 then 48; control is 85 then 108. Nether is
426 then 398 in baseline and 461 then 527 in control. These measured differences
must remain visible rather than selecting the repetition with the preferred
contrast. All-location counts increase in each matched pair in Aether, Moon,
both End strata and Nether, but the increase is not identical across repetitions.

## Biome attribution limits found during integration

The [accepted biome comparisons](accepted-biome-comparisons.json.gz) integrate the initial
ten accepted outputs, covering 110 strata and 42,336 height/biome rows. Each row
retains its chunk-center exposure, all ten category counts and corresponding
rates. Positive exposure with no category occurrences is an explicit zero count;
zero exposure produces a null rate. Twelve unavailable anchors remain separate,
including their location identities and reasons. Direct joins identify these limits:

- Every accepted world has one central-End dragon-arena location with
  `NO_LOCATION_HEIGHT`. Retain its location count without assigning a biome band.
- Both mountainous controls have an `explorify:end_shipwreck` at chunk (505,514)
  with anchor (8088,-7,8232), quart Y -2. Its reason is
  `anchor outside stored biome height`. This is a second unavailable biome
  observation in those two worlds, not a rejected location or a surface-biome case.
- All four mountainous worlds have one `supplementaries:cave_urn_cache` at
  (-57,19,-319), quart Y 4, attributed to `regions_unexplored:muddy_river`.
  The exposure table has zero chunk-center columns for that biome in that band.
  Candidate IDs are 16603 (r1 B), 16616 (r1 C), 16630 (r2 B), and 16593 (r2 C).
  The exact-position numerator is valid, but its chunk-center exposure is zero.
  Its biome density must therefore remain unavailable, with the positive count
  and zero denominator retained. Do not substitute exposure from another height,
  use an infinite rate, erase the observation or resample the accepted world.

No other unavailable biome anchor or zero-exposure observed location was found
in these ten outputs. This follows a direct inspection of every classified
occurrence in every stratum, not just the examples above. For registry rows,
join `classification.occurrences` to `occurrence_biomes` by registry ID and chunk
X/Z within its stratum. Nonregistry rows already carry their biome and quart Y.
Join valid attributions to `biome_exposure.rows` by `(quart_y, biome)`; absent
keys have zero sampled chunk-center exposure. Retain unavailable reasons before
that join. The numerator uses the declared occurrence anchor, while exposure
uses chunk-center columns, so their horizontal sampling can differ. This is a
limitation of the declared proxy, not evidence that biome placement is broken.

The comparison is 284,430 compressed bytes (15,203,284 JSON bytes), SHA-256
`9b1cefc7317ced9a70391ebc8ce0d9aa1784337af6c20eb06e4cf3fc385a171b`.
Each world's entry binds its accepted census input by SHA-256. The existing census
tool's `summarize_biomes` function supplies this join and is also used by future
full-world censuses. Earlier raw worlds and accepted census outputs are unchanged.
This addition implements the required biome comparison; it does not add a new
measurement, schema, sampler or acceptance gate. Results remain descriptive
within each seed, stratum and height band; do not pool bands or interpret these
selected worlds as a random biome sample. Counts below 30 remain sparse under
the protocol. The four zero-exposure cases retain their positive numerators.

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
anchors equals its accepted all-location count. This integrates the ten accepted
worlds only; it does not close the pending full sampling requirement.

## Failure denominators and uncertainty

Fifteen planned cells have accepted complete censuses. The failed planned cell
(ocean-heavy r2 control) has two rejected attempts: heap exhaustion during
generation, then an incomplete saved Aether chunk following a save exception.
All planned cells have been attempted. Seventeen attempts cover sixteen cells,
with fifteen complete censuses and one failed cell awaiting its final retry.
The failed attempts retain their immutable archives and diagnoses. No missing
cell enters density, distance or matched-pair denominators. The user rejected the proposed fifteen-world target and authorized a final fresh
control retry after the five untouched planned worlds. Sixteen complete cells
remain required.

Within the fifteen accepted worlds, the observer's call count differs from grouped
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

No constructive content means the candidate did not produce the required content;
it is not a failed server run. Outside-frame candidates remain excluded by the
declared geometry. Saved-content mismatches remain excluded under the existing
acceptance rule, even if a writer previously reported a successful operation.
The individual records retain coordinates and content checks. Registry starts
are counted separately, so observed nonregistry locations alone do not equal
the all-location totals in the dimension tables. The new
[ocean-heavy r2 baseline](full-ocean-heavy-r2-baseline/README.md) supplies its
complete category and spatial results; initial ten-world tables above remain
explicit subsets until the final combined synthesis.

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

The four selected seeds are not a random sample. All four now have accepted
worlds. The [biome-diverse r1 baseline](full-biome-diverse-r1-baseline/README.md)
and [its control](full-biome-diverse-r1-without-sparse/README.md), together with
[repetition 2](full-biome-diverse-r2-baseline/README.md), form two matched pairs.
Ordinary and mountainous also each have two complete matched pairs;
ocean-heavy has one and an unpaired second baseline. Fresh-repetition
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
These configuration facts alone resolve presence and intent. The accepted
[ordinary](full-ordinary-r2-baseline/README.md) and
[mountainous](full-mountainous-r2-baseline/README.md) matched blocks now measure
realized differences; the remaining two seed blocks and combined analysis are incomplete.
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
within-arm generation variability remains in the matched results. Full four-seed
attribution awaits completion of the fixed sample.

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
prior reviews are resolved. One world, combined synthesis and final delivery
remain incomplete; runtime acceptance is established per world, not from tests.

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
requires complete occurrence capture and exact experiment identities; fifteen
worlds have passed so far.

Done means every Item 10 bullet has a measured result or a specification-approved
disposition, source-bound deterministic processing, retained raw evidence with
hashes and tested restore, explicit uncertainty and failure dispositions, clean
final review, merged delivery and the subsequent cross-item audit. The authorized
scope does not require observed combat or human sessions in Items 10 or 11.

## Resource estimate and unresolved gates

Use the [protocol resource estimate](protocol.md#runtime-and-storage-estimate)
as the current planning authority: 720,896 selected chunks across 16 worlds,
about 11.05 automated generation hours and 13.92 GiB cumulative uncompressed
world data, using the measured r3 proxy and including the requested generation
edge outside the census. Sequential custody has a provisional
5 GiB workspace floor. Actual per-world costs are recorded in each accepted
world report and supersede proxy estimates for the completed runs. Recheck
capacity before each experiment; these are estimates, not promised runtimes.
The human collection matrix is superseded by the delivered
[methodology amendment](methodology-amendment.md).

Remaining measurement and delivery work:

- Run the authorized final ocean-heavy control retry; continue
  capacity checks. Preserve all existing artifacts and failed observations.
- Combine all declared category, spatial, biome, seed and repetition results,
  including the matched Sparse Structures contrast and uncertainty.
- Complete clean-checkout reproduction, final review, main delivery and the
  Items 2 through 10 audit. Keep Item 11 workflows untouched.

The observer and control methods are implemented. Reuse them; add no generic
framework or tuning while completing the remaining sample and report.

[Decoder preparation validation](decoder.md) records the custom-dimension
identification fix and validated authoritative-start-coordinate extraction.
