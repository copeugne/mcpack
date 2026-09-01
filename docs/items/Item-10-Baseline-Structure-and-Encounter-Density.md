# Item 10 — Baseline Structure and Encounter Density

**Status:** `COMPLETE`
**Scope:** pristine Minecraft 1.21.1 / NeoForge 21.1.249 control, zero gameplay mods
**Protocol:** `structure-density-v0.1`
**Accepted run:** `item10-chunkpregen-full-r19`
**Decision state:** baseline diagnosis only; no mod or spacing solution selected

## Outcome

The exact protocol ceiling was measured: 32,768 fully generated Overworld chunks per seed across four deterministic terrain roles, for 131,072 aggregate chunks. Every final target slot decoded at `minecraft:full`, stored the coordinate belonging to its Anvil location-table slot, and passed an independent offline rescan. Nested-stage membership and two independently generated Stage 1 controls also matched exactly.

The pristine baseline contains 1,007 unique structure starts, or 7.683 per 1,000 chunks. It contains 831 provisionally actionable locations (6.340/1,000), a static 762-location hostility proxy (5.814/1,000), 100 Tier 2 proper dungeons (0.763/1,000), 47 Tier 3 major expeditions (0.359/1,000), and 31 villages (0.237/1,000).

These counts do **not** establish good exploration pacing. Mineshafts account for 476 of 831 actionable starts (57.3%), and many other counted locations are underground, underwater, buried, or otherwise difficult to notice. Item 11 must measure actual player discoveries, encounters, repetition, and dead travel. Item 12 must measure discoverability directly.

## Frozen Method

### Counting rules

- Denominator: target chunks whose saved `Status` is exactly `minecraft:full`.
- Structure: one non-`INVALID` entry in `structures.starts` whose start chunk lies within the exact target rectangle.
- Deduplication: registry ID plus authoritative start-chunk coordinate.
- Actionable: every Item 9 provisional category except Tier 0 ambient landmarks.
- Proper dungeon: Item 9 Tier 2.
- Major expedition: Item 9 Tier 3.
- Village: the consolidated vanilla village family.
- Distance: horizontal Euclidean distance between structure bounding-box centers, with start-chunk center as fallback.
- Biome: saved quart biome in the structure's start chunk; rates use each full chunk's center at its `MOTION_BLOCKING_NO_LEAVES` height.
- Combat: a **static hostile-location proxy**, derived from Item 8 hostility classification. It is not an observed mob encounter count. Actual hostile encounters belong to Items 11 and 14.

### Nested sampling rule

| Stage | Rectangle per seed | Chunks/seed | Aggregate chunks |
|---:|---|---:|---:|
| 1 | x −32..31, z −32..31 | 4,096 | 16,384 |
| 2 | x −64..63, z −32..31 | 8,192 | 32,768 |
| 3 | x −64..63, z −64..63 | 16,384 | 65,536 |
| 4 | x −128..127, z −64..63 | 32,768 | 131,072 |

Expansion stops only if every provisional category reaches 30 observations. That did not happen, so the measurement continued to Stage 4. Tier 4 remains right-censored at the ceiling with four observations.

### Generation instrumentation

The zero-mod worlds temporarily used two hash-pinned server-side tools solely to generate the bounded survey area:

- `Chunk-Pregenerator-Neoforge-1.21-4.5.4.jar` — SHA-512 `db7737f59dca328e297ff52099abf93ce5cdd8c4b74006fb303259893e9adc66c5cc29477b5f1190b9ab1745ba88ad8e5def7814ec965f697dc123abfa839a76`;
- `CarbonConfig-Neoforge-1.21-2.0.0.jar` — SHA-512 `196888d12a369ae09689a727f0cc94b8157035c703403d409b14e26fa04e1422c051538cde192a38f0324eb1eb1ca7bab5e337d695488db65c62ccbee66553ea`.

They add no counted structure/content registry and are not admitted to the baseline or tentative pack. The pregenerator's completion message was never accepted as sufficient evidence. Each pass used `save-all flush`, a clean shutdown, and an offline exact-slot scan.

## Generation Integrity

Every seed needed a bounded second pass because some generated/saved chunks had not reached final status after pass 1. No accepted pass contained a coordinate mismatch or unreadable slot.

| Seed | Pass 1 full/correct | Pass 1 deficit | Pass 2 full/correct | Final mismatch/unreadable | Result |
|---|---:|---:|---:|---:|---|
| ordinary | 30,235 | 2,533 | 32,768 | 0 / 0 | pass |
| mountainous | 31,783 | 985 | 32,768 | 0 / 0 | pass |
| ocean-heavy | 31,509 | 1,259 | 32,768 | 0 / 0 | pass |
| biome-diverse | 31,669 | 1,099 | 32,768 | 0 / 0 | pass |

All pass counts were monotonic. Every lifecycle was clean. The independent validator confirmed:

- exact Minecraft, NeoForge, seed, denominator, and instrumentation identities;
- exact pristine snapshot restore for every seed;
- only the two instrumentation JARs in each generated server's `mods/` directory;
- one complete console artifact per pass;
- no fatal server-log signature;
- 32,768 full and coordinate-correct final target slots per seed;
- SHA-256 manifests for raw region and console artifacts.

### Retained failures

Earlier methods were rejected rather than normalized away:

- loaded/ticket and heightmap probes did not prove final saved status;
- immediate Chunky shutdown left 1,637 of 4,096 target chunks non-full;
- live `save-all flush` was not a reliable per-tile serialization oracle;
- a broad completion expression could match the wrong line;
- Chunk Pregenerator area mode did not cover the exact requested rectangle;
- r18's diverse region had one unreadable slot, three shifted coordinates, and only 28,863 full/correct target slots;
- r19's first mountain process was interrupted before completion/checkpoint and its partial world was preserved but never measured.

The accepted ordinary result's canonical JSON SHA-256 remained `43c6500dc8cfef7f74c5cdf2a2b9951efb4778e3c10f9495f4ec550196bae865` across the verified resume.

## Aggregate Density

| Metric | Starts | Per 1,000 chunks | Sampling state |
|---|---:|---:|---|
| All structures | 1,007 | 7.6828 | ≥30 |
| Actionable locations | 831 | 6.3400 | ≥30 |
| Combat-location proxy | 762 | 5.8136 | ≥30 |
| Proper dungeons | 100 | 0.7629 | ≥30 |
| Major expeditions | 47 | 0.3586 | ≥30 |
| Villages | 31 | 0.2365 | ≥30 |

### Provisional categories

| Category | Starts | Per 1,000 chunks | Sampling state |
|---|---:|---:|---|
| Tier 0 — ambient landmark | 176 | 1.3428 | ≥30 |
| Civilization | 31 | 0.2365 | ≥30 |
| Tier 1 — small encounter | 649 | 4.9515 | ≥30 |
| Tier 2 — proper dungeon | 100 | 0.7629 | ≥30 |
| Tier 3 — major expedition | 47 | 0.3586 | ≥30 |
| Tier 4 — world objective | 4 | 0.0305 | **right-censored** |

Tier 4's observed rate is descriptive only. Four stronghold starts are not enough to treat 0.0305/1,000 as a stable population estimate.

### Family composition

| Family | Starts | Per 1,000 chunks | Share of all starts |
|---|---:|---:|---:|
| Mineshaft | 476 | 3.6316 | 47.3% |
| Ocean ruin | 127 | 0.9689 | 12.6% |
| Trial chambers | 100 | 0.7629 | 9.9% |
| Shipwreck | 89 | 0.6790 | 8.8% |
| Ruined portal | 84 | 0.6409 | 8.3% |
| Ancient city | 33 | 0.2518 | 3.3% |
| Village | 31 | 0.2365 | 3.1% |
| Buried treasure | 29 | 0.2213 | 2.9% |
| Ocean monument | 14 | 0.1068 | 1.4% |
| Trail ruins | 9 | 0.0687 | 0.9% |
| Stronghold | 4 | 0.0305 | 0.4% |
| Igloo | 3 | 0.0229 | 0.3% |
| Pillager outpost | 3 | 0.0229 | 0.3% |
| Jungle temple | 2 | 0.0153 | 0.2% |
| Swamp hut | 2 | 0.0153 | 0.2% |
| Desert pyramid | 1 | 0.0076 | 0.1% |
| Woodland mansion | 0 | 0.0000 | observed zero |

The baseline's apparent abundance is therefore highly concentrated. Mineshafts are 73.3% of Tier 1 starts and 57.3% of all actionable starts. The sample contains no woodland mansion. Rare-family absence is not proof that the family cannot generate.

## Seed Comparison

| Seed role | All /1,000 | Actionable /1,000 | Combat proxy /1,000 | Tier 2 /1,000 | Tier 3 /1,000 | Villages /1,000 |
|---|---:|---:|---:|---:|---:|---:|
| Ordinary | 7.7820 | 6.5308 | 5.8289 | 0.8240 | 0.0916 | 0.1831 |
| Mountainous | 5.2490 | 4.4861 | 3.9978 | 0.5188 | 0.8240 | 0.3662 |
| Ocean-heavy | 9.9487 | 7.9651 | 7.4463 | 0.8240 | 0.3357 | 0.2441 |
| Biome-diverse | 7.7515 | 6.3782 | 5.9814 | 0.8850 | 0.1831 | 0.1526 |

The ocean-heavy seed has 1.90× the all-structure rate and 1.78× the actionable rate of the mountainous seed. This is composition, not simply “better density”: the ocean-heavy seed contains 53 ocean ruins and 43 shipwrecks, while the mountain seed contains 27 ancient cities and only five combined ocean ruins/shipwrecks.

Tier 3 also changes meaning by terrain. The mountainous seed's 27 Tier 3 starts are all ancient cities; the ocean-heavy seed's 11 are ocean monuments. A single aggregate Tier 3 rate would hide this gameplay difference.

## Biome Comparison

The raw evidence records all 52 sampled surface biomes. To avoid treating tiny denominators as stable comparisons, this report summarizes only biome rows with at least 1,000 aggregate full chunks; smaller rows remain available in the machine evidence.

| Selected biome | Full chunks | All /1,000 | Actionable /1,000 |
|---|---:|---:|---:|
| Beach | 2,590 | 21.6216 | 20.0772 |
| Swamp | 1,400 | 10.7143 | 9.2857 |
| Cold ocean | 12,396 | 11.2133 | 8.2285 |
| Lukewarm ocean | 3,539 | 9.6072 | 8.1944 |
| Ocean | 9,846 | 10.4611 | 8.1251 |
| Deep cold ocean | 11,157 | 9.6800 | 7.6185 |
| Warm ocean | 9,586 | 9.5973 | 7.3023 |
| Desert | 2,343 | 7.2557 | 6.8289 |
| Taiga | 3,319 | 7.8337 | 6.3272 |
| Plains | 14,568 | 6.6584 | 5.9034 |
| Forest | 14,164 | 5.7187 | 5.0127 |
| Meadow | 1,907 | 4.1951 | 3.6707 |
| Dark forest | 3,361 | 3.5704 | 3.5704 |
| Snowy slopes | 1,831 | 3.8230 | 2.7307 |
| Jagged peaks | 2,196 | 2.2769 | 1.8215 |
| Grove | 2,902 | 2.0675 | 1.3784 |

Beach and ocean rates are elevated by ocean ruins, shipwrecks, buried treasure, and monuments. Mountain-surface biomes have low start rates even while the mountainous seed contains many underground ancient cities. The result reinforces the need to keep surface discoverability separate from underground density.

## Spacing, Clustering, and Empty Regions

### Nearest neighbor

| Seed | Actionable median | Actionable p95 | Tier 2 median | Tier 3 median | Village median |
|---|---:|---:|---:|---:|---:|
| Ordinary | 100 blocks | 224 | 370 | 510 | 611 |
| Mountainous | 120 | 238 | 464 | 358 | 463 |
| Ocean-heavy | 86 | 175 | 449 | 552 | 307 |
| Biome-diverse | 98 | 210 | 377 | 321 | 523 |

These are within-seed nearest-neighbor distances between structure centers. Low values do not imply surface visibility. Underground mineshafts and trial chambers strongly reduce the actionable statistic.

### 16×16-chunk cell diagnostics

| Seed | Empty cells, all starts | Empty cells, actionable | Actionable variance/mean |
|---|---:|---:|---:|
| Ordinary | 13.3% | 18.0% | 0.917 |
| Mountainous | 25.8% | 31.3% | 0.886 |
| Ocean-heavy | 3.1% | 9.4% | 0.785 |
| Biome-diverse | 14.1% | 18.8% | 0.946 |

The mountain seed has the most empty 256-chunk cells; the ocean seed has the fewest. Variance-to-mean below one for actionable starts indicates no strong aggregate over-clustering at this grid scale. Structure-family-specific placement and environmental concentration still matter and are preserved in the raw evidence.

### Distance from every target chunk to an actionable start

| Seed | Median | p95 | Maximum | Beyond 512 blocks |
|---|---:|---:|---:|---:|
| Ordinary | 94 blocks | 196 | 327 | 0% |
| Mountainous | 113 | 239 | 361 | 0% |
| Ocean-heavy | 83 | 180 | 467 | 0% |
| Biome-diverse | 94 | 203 | 360 | 0% |

This diagnostic proves there are no large *geometric* holes relative to all non-Tier-0 start centers in the measured rectangles. It does not prove a walking player can see, enter, or use the nearest start. The dominance of underground content makes that distinction load-bearing.

## Sparse Structures Contribution

Sparse Structures is absent from the pristine baseline. Its contribution to every measured control value is therefore exactly zero. No multiplier, spacing behavior, or interaction is inferred for the tentative future stack. Its actual contribution must be isolated after admission and configuration in the later combined-stack measurements.

## Findings Carried Forward

1. **Static density is not the likely sole explanation for perceived emptiness.** The control has an actionable start center within 467 blocks of every measured chunk center, but most actionable starts are not surface-visible content.
2. **Composition dominates the headline rate.** Mineshafts alone supply nearly half of all starts; ocean structures substantially inflate ocean-biome and ocean-seed rates.
3. **Seed/terrain dependence is material.** All-start density ranges from 5.249 to 9.949 per 1,000 chunks, a 1.90× spread.
4. **Tier 2 density is comparatively stable across three seeds but lower in mountains.** It ranges from 0.519 to 0.885 per 1,000 chunks.
5. **Tier 3 rate does not imply equivalent gameplay.** Ancient cities and ocean monuments produce different expedition pressure and discoverability.
6. **World objectives are too rare for a stable rate.** Tier 4 remains right-censored at four observations.
7. **No spacing solution is justified yet.** Item 11 must establish travel pacing/repetition, Item 12 discoverability, and Item 13 mechanical dungeon quality before Item 18 may diagnose root causes.

## Limitations

- This is a zero-gameplay-mod control because no prior instance existed. It does not estimate the tentative 190-JAR pool.
- The combat number is a static hostile-location proxy, not observed combat.
- Item 9 categories remain provisional until the final taxonomy in Item 19.
- Nearest-neighbor and empty-region distances use structure centers, not entrances, visibility, terrain-aware paths, or travel time.
- Biome rates use start-chunk surface biome, not every block occupied by a structure.
- The four-seed development suite is deterministic and broad, not a random sample of all Minecraft seeds.
- Instrumentation pass-1 incompleteness demonstrates why generation-tool completion signals cannot replace saved-world validation.

## Evidence Map

| Evidence | Role |
|---|---|
| `measurement/structure-density-v0.1.json` | Frozen counting, expansion, biome, clustering, and censoring protocol |
| `evidence/structure-density/item10-chunkpregen-full-r19.json` | Final per-seed generation lifecycle, attempts, hashes, and slot checks |
| `evidence/structure-density/item10-chunkpregen-full-validation-r19.json` | Independent offline/lifecycle/artifact validator |
| `evidence/structure-density/item10-stage1-analysis-r19.json` | 4,096 chunks/seed analysis |
| `evidence/structure-density/item10-stage2-analysis-r19.json` | 8,192 chunks/seed analysis |
| `evidence/structure-density/item10-stage3-analysis-r19.json` | 16,384 chunks/seed analysis |
| `evidence/structure-density/item10-stage4-analysis-r19.json` | 32,768 chunks/seed full analysis and raw starts |
| `evidence/structure-density/item10-stage-evaluation-r19.json` | Denominator, nesting, independent-repeat, ceiling, and censoring proof |
| `evidence/structure-density/item10-independent-controls-analysis-r3.json` | Independently generated ordinary/mountain Stage 1 controls |
| `evidence/structure-density/item10-anvil-decoder-validation.json` | 200/200 height checks and 10,190 selective/full NBT checks |
| `evidence/structure-density/item10-generation-failure-r18.json` | Rejected corrupt generation evidence |
| `evidence/structure-density/item10-generation-interruption-r19-mountain1.json` | Preserved interrupted-run disposition |

## Exit Gate

**PASS.** Structure abundance, actionable-location density, static combat-location density, proper-dungeon density, major-expedition density, village density, per-category/family composition, nearest-neighbor distance, clustering, empty-region distance, biome differences, seed differences, and Sparse Structures' pristine contribution are quantitatively recorded under a reproducible method. The sole right-censored category is explicitly identified. No final solution has been selected.

Item 11 is authorized to measure actual exploration pacing and repetition. Its protocol and runbook are prepared, but completion requires retained real-client observations from at least two human operators.
