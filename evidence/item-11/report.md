# Item 11 complete automated route measurements

Local matrix: PASS. Review and main delivery are separate gates recorded in README.md.

Sixteen accepted saved worlds, 64 fixed Overworld transects and 192 route/mode evaluations.
Each route is 768 blocks. Primary adjacency radius is 64 blocks. Coverage is sampled
eight-block segments with a ray-clear proxy target, not observed human discovery.
Route membership totals below can count a location on several overlapping transects.
C/T1/T2/T3/T4 roles are provisional, retaining confidence and ambiguity in each raw row.

## Per-world primary candidate membership

| World | All | Actionable | Encounter sites | T2 | T3 | T4 | Village | Ray-clear all | Covered blocks / 3072 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| biome-diverse-r1-baseline | 1777 | 1769 | 1768 | 5 | 0 | 0 | 0 | 3 | 152 |
| biome-diverse-r1-without-sparse | 1785 | 1758 | 1756 | 6 | 0 | 0 | 0 | 18 | 520 |
| biome-diverse-r2-baseline | 1748 | 1740 | 1739 | 5 | 0 | 0 | 0 | 3 | 176 |
| biome-diverse-r2-without-sparse | 1835 | 1807 | 1805 | 6 | 0 | 0 | 0 | 17 | 520 |
| mountainous-r1-baseline | 1655 | 1647 | 1644 | 5 | 0 | 0 | 0 | 3 | 112 |
| mountainous-r1-without-sparse | 1741 | 1715 | 1713 | 8 | 3 | 0 | 0 | 7 | 344 |
| mountainous-r2-baseline | 1660 | 1651 | 1648 | 5 | 0 | 0 | 0 | 3 | 96 |
| mountainous-r2-without-sparse | 1783 | 1756 | 1754 | 8 | 3 | 0 | 0 | 9 | 360 |
| ocean-heavy-r1-baseline | 422 | 418 | 418 | 4 | 0 | 0 | 0 | 2 | 136 |
| ocean-heavy-r1-without-sparse | 466 | 457 | 456 | 6 | 1 | 0 | 1 | 4 | 224 |
| ocean-heavy-r2-baseline | 457 | 453 | 453 | 4 | 0 | 0 | 0 | 2 | 136 |
| ocean-heavy-r2-without-sparse-attempt3 | 461 | 452 | 451 | 6 | 1 | 0 | 1 | 4 | 224 |
| ordinary-r1-baseline | 325 | 320 | 320 | 2 | 0 | 0 | 0 | 2 | 176 |
| ordinary-r1-without-sparse | 328 | 320 | 317 | 7 | 0 | 0 | 3 | 4 | 304 |
| ordinary-r2-baseline | 303 | 298 | 298 | 2 | 0 | 0 | 0 | 2 | 176 |
| ordinary-r2-without-sparse | 372 | 364 | 361 | 7 | 0 | 0 | 3 | 4 | 304 |

## Per-route primary gaps, repetition and transport

All-location gaps include censored beginning/end intervals. First repeat is distance from
route start; NR means no repeat, right-censored at 768. Prefixes are walking/horse/boat
model-reachable blocks. F denotes MODEL_FEASIBLE, I INFEASIBLE, U UNKNOWN.
Raw rows retain every failure station, cost range and category-specific interval.

| World / route | Adjacent | Ray-clear | Maximum empty gap | First repeat | Prefixes | Mode status |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| biome-diverse-r1-baseline / east-north | 471 | 1 | 11 | 0 | 25/25/0 | I/I/I |
| biome-diverse-r1-baseline / east-south | 439 | 0 | 16 | 0 | 5/5/0 | I/I/I |
| biome-diverse-r1-baseline / south-east | 484 | 2 | 14 | 0 | 13/13/0 | I/I/I |
| biome-diverse-r1-baseline / south-west | 383 | 0 | 17 | 5 | 26/26/0 | I/I/I |
| biome-diverse-r1-without-sparse / east-north | 483 | 8 | 13 | 0 | 29/29/0 | I/I/I |
| biome-diverse-r1-without-sparse / east-south | 401 | 2 | 12 | 0 | 5/5/0 | I/I/I |
| biome-diverse-r1-without-sparse / south-east | 499 | 5 | 11 | 0 | 13/13/0 | I/I/I |
| biome-diverse-r1-without-sparse / south-west | 402 | 3 | 25 | 0 | 29/29/0 | I/I/I |
| biome-diverse-r2-baseline / east-north | 459 | 1 | 13 | 0 | 89/89/0 | I/I/I |
| biome-diverse-r2-baseline / east-south | 432 | 0 | 18 | 0 | 5/5/0 | I/I/I |
| biome-diverse-r2-baseline / south-east | 506 | 2 | 8 | 0 | 13/13/0 | I/I/I |
| biome-diverse-r2-baseline / south-west | 351 | 0 | 18 | 1 | 32/32/0 | I/I/I |
| biome-diverse-r2-without-sparse / east-north | 477 | 8 | 10 | 0 | 25/25/0 | I/I/I |
| biome-diverse-r2-without-sparse / east-south | 439 | 2 | 17 | 0 | 5/5/0 | I/I/I |
| biome-diverse-r2-without-sparse / south-east | 526 | 4 | 16 | 0 | 13/13/0 | I/I/I |
| biome-diverse-r2-without-sparse / south-west | 393 | 3 | 17 | 0 | 29/29/0 | I/I/I |
| mountainous-r1-baseline / east-north | 402 | 1 | 23 | 0 | 12/12/0 | I/I/I |
| mountainous-r1-baseline / east-south | 429 | 0 | 12 | 0 | 34/34/0 | I/I/I |
| mountainous-r1-baseline / south-east | 396 | 2 | 13 | 0 | 42/42/0 | I/I/I |
| mountainous-r1-baseline / south-west | 428 | 0 | 11 | 0 | 22/22/0 | I/I/I |
| mountainous-r1-without-sparse / east-north | 397 | 1 | 11 | 0 | 12/12/0 | I/I/I |
| mountainous-r1-without-sparse / east-south | 467 | 1 | 10 | 0 | 45/45/0 | I/I/I |
| mountainous-r1-without-sparse / south-east | 449 | 3 | 17 | 0 | 52/52/0 | I/I/I |
| mountainous-r1-without-sparse / south-west | 428 | 2 | 15 | 0 | 22/22/0 | I/I/I |
| mountainous-r2-baseline / east-north | 397 | 1 | 13 | 0 | 12/12/0 | I/I/I |
| mountainous-r2-baseline / east-south | 417 | 0 | 11 | 0 | 4/4/0 | I/I/I |
| mountainous-r2-baseline / south-east | 424 | 2 | 12 | 0 | 0/0/0 | I/I/I |
| mountainous-r2-baseline / south-west | 422 | 0 | 13 | 0 | 8/8/0 | I/I/I |
| mountainous-r2-without-sparse / east-north | 388 | 1 | 10 | 0 | 13/13/0 | I/I/I |
| mountainous-r2-without-sparse / east-south | 487 | 2 | 10 | 0 | 40/40/0 | I/I/I |
| mountainous-r2-without-sparse / south-east | 466 | 3 | 15 | 0 | 9/9/0 | I/I/I |
| mountainous-r2-without-sparse / south-west | 442 | 3 | 17 | 0 | 8/8/0 | I/I/I |
| ocean-heavy-r1-baseline / east-north | 97 | 0 | 115 | 0 | 0/0/37 | I/I/I |
| ocean-heavy-r1-baseline / east-south | 95 | 0 | 210 | 213 | 0/0/756 | I/I/I |
| ocean-heavy-r1-baseline / south-east | 174 | 2 | 61 | 0 | 0/0/446 | I/I/I |
| ocean-heavy-r1-baseline / south-west | 56 | 0 | 352 | 372 | 0/0/768 | I/I/F |
| ocean-heavy-r1-without-sparse / east-north | 98 | 3 | 87 | 0 | 0/0/37 | I/I/I |
| ocean-heavy-r1-without-sparse / east-south | 130 | 0 | 76 | 134 | 0/0/756 | I/I/I |
| ocean-heavy-r1-without-sparse / south-east | 158 | 1 | 88 | 0 | 0/0/623 | I/I/I |
| ocean-heavy-r1-without-sparse / south-west | 80 | 0 | 175 | 179 | 0/0/768 | I/I/F |
| ocean-heavy-r2-baseline / east-north | 101 | 0 | 63 | 0 | 0/0/37 | I/I/I |
| ocean-heavy-r2-baseline / east-south | 128 | 0 | 189 | 208 | 0/0/756 | I/I/I |
| ocean-heavy-r2-baseline / south-east | 170 | 2 | 56 | 0 | 0/0/446 | I/I/I |
| ocean-heavy-r2-baseline / south-west | 58 | 0 | 249 | 363 | 0/0/768 | I/I/F |
| ocean-heavy-r2-without-sparse-attempt3 / east-north | 111 | 3 | 80 | 0 | 0/0/37 | I/I/I |
| ocean-heavy-r2-without-sparse-attempt3 / east-south | 114 | 0 | 94 | 181 | 0/0/756 | I/I/I |
| ocean-heavy-r2-without-sparse-attempt3 / south-east | 165 | 1 | 83 | 0 | 0/0/623 | I/I/I |
| ocean-heavy-r2-without-sparse-attempt3 / south-west | 71 | 0 | 121 | 159 | 0/0/768 | I/I/F |
| ordinary-r1-baseline / east-north | 65 | 1 | 152 | 0 | 0/0/768 | I/I/F |
| ordinary-r1-baseline / east-south | 82 | 0 | 120 | 160 | 0/0/768 | I/I/F |
| ordinary-r1-baseline / south-east | 119 | 1 | 144 | 0 | 0/0/768 | I/I/F |
| ordinary-r1-baseline / south-west | 59 | 0 | 246 | 0 | 0/0/768 | I/I/F |
| ordinary-r1-without-sparse / east-north | 51 | 1 | 137 | 0 | 0/0/589 | I/I/I |
| ordinary-r1-without-sparse / east-south | 105 | 1 | 112 | 160 | 0/0/768 | I/I/F |
| ordinary-r1-without-sparse / south-east | 118 | 1 | 163 | 0 | 0/0/616 | I/I/I |
| ordinary-r1-without-sparse / south-west | 54 | 1 | 244 | 30 | 0/0/768 | I/I/F |
| ordinary-r2-baseline / east-north | 55 | 1 | 152 | 0 | 0/0/768 | I/I/F |
| ordinary-r2-baseline / east-south | 83 | 0 | 120 | 160 | 0/0/768 | I/I/F |
| ordinary-r2-baseline / south-east | 110 | 1 | 145 | 0 | 0/0/768 | I/I/F |
| ordinary-r2-baseline / south-west | 55 | 0 | 127 | 0 | 0/0/768 | I/I/F |
| ordinary-r2-without-sparse / east-north | 54 | 1 | 137 | 0 | 0/0/589 | I/I/I |
| ordinary-r2-without-sparse / east-south | 109 | 1 | 104 | 112 | 0/0/768 | I/I/F |
| ordinary-r2-without-sparse / south-east | 135 | 1 | 167 | 0 | 0/0/616 | I/I/I |
| ordinary-r2-without-sparse / south-west | 74 | 1 | 237 | 0 | 0/0/768 | I/I/F |

## Radius and distance sensitivity

Each row pools 32 routes within one arm. These are overlapping fixed transects, not
independent samples. Coverage denominator is 32 times the window length.

| Arm | Radius | Window | Adjacent memberships | Ray-clear memberships | Covered / denominator |
| --- | ---: | ---: | ---: | ---: | --- |
| baseline | 32 | 256 | 1358 | 0 | 0 / 8192 |
| baseline | 32 | 512 | 2481 | 2 | 112 / 16384 |
| baseline | 32 | 768 | 3938 | 6 | 216 / 24576 |
| baseline | 64 | 256 | 2933 | 0 | 0 / 8192 |
| baseline | 64 | 512 | 5153 | 6 | 272 / 16384 |
| baseline | 64 | 768 | 8347 | 20 | 1160 / 24576 |
| baseline | 96 | 256 | 4817 | 2 | 72 / 8192 |
| baseline | 96 | 512 | 8214 | 12 | 560 / 16384 |
| baseline | 96 | 768 | 13601 | 38 | 2160 / 24576 |
| without-sparse | 32 | 256 | 1373 | 5 | 128 / 8192 |
| without-sparse | 32 | 512 | 2598 | 9 | 168 / 16384 |
| without-sparse | 32 | 768 | 4123 | 17 | 424 / 24576 |
| without-sparse | 64 | 256 | 3077 | 12 | 432 / 8192 |
| without-sparse | 64 | 512 | 5432 | 30 | 856 / 16384 |
| without-sparse | 64 | 768 | 8771 | 67 | 2800 / 24576 |
| without-sparse | 96 | 256 | 5016 | 24 | 944 / 8192 |
| without-sparse | 96 | 512 | 8608 | 58 | 1960 / 16384 |
| without-sparse | 96 | 768 | 14106 | 102 | 5368 / 24576 |

## Descriptive dispersion and paired contrasts

JSON summaries below give n, median, minimum, maximum and inclusive IQR. No bootstrap
population intervals are justified for these nonrandom seeds and overlapping routes.

```json
{
  "baseline": {
    "adjacent_count": {
      "iqr": 333.0,
      "max": 506,
      "median": 262.5,
      "min": 55,
      "n": 32
    },
    "coverage_blocks": {
      "iqr": 74.0,
      "max": 136,
      "median": 0.0,
      "min": 0,
      "n": 32
    },
    "first_repeat_distance_uncensored": {
      "iqr": 0.25,
      "max": 372,
      "median": 0.0,
      "min": 0,
      "n": 32
    },
    "maximum_empty_gap": {
      "iqr": 131.25,
      "max": 352,
      "median": 39.5,
      "min": 8,
      "n": 32
    }
  },
  "without-sparse": {
    "adjacent_count": {
      "iqr": 335.75,
      "max": 526,
      "median": 276.5,
      "min": 51,
      "n": 32
    },
    "coverage_blocks": {
      "iqr": 78.0,
      "max": 184,
      "median": 104.0,
      "min": 0,
      "n": 32
    },
    "first_repeat_distance_uncensored": {
      "iqr": 0.0,
      "max": 181,
      "median": 0.0,
      "min": 0,
      "n": 32
    },
    "maximum_empty_gap": {
      "iqr": 99.75,
      "max": 244,
      "median": 50.5,
      "min": 10,
      "n": 32
    }
  }
}
```

Pair differences below are omit-Sparse minus baseline for the same seed/repetition.
The final ocean-heavy r2 control uses the accepted third attempt. Rejected attempts
remain in Item 10 custody and are not additional route samples.

| Seed / repetition | Adjacent membership difference | Covered-block difference |
| --- | ---: | ---: |
| biome-diverse-r1 | 8 | 368 |
| biome-diverse-r2 | 87 | 344 |
| mountainous-r1 | 86 | 232 |
| mountainous-r2 | 123 | 264 |
| ocean-heavy-r1 | 44 | 88 |
| ocean-heavy-r2 | 4 | 88 |
| ordinary-r1 | 3 | 128 |
| ordinary-r2 | 69 | 128 |

## Scope and input identities

Placement densities are retained per world in the raw result and remain Item 10 quantities.
Adjacency is distinct from ray-clear targets, which are distinct from modeled access.
Speeds (walking 4 [3,5], horse 7 [5,9], boat 8 [6,10] blocks/second) are assumptions.
Infeasible completed costs are null. Prefix and unconstrained costs remain separately labeled.
Repeated-family events do not demonstrate identical generated layouts. Missing targets and
geometry retain UNKNOWN outcomes; zeroes and censored gaps do not establish global absence.
Human recognition, actual fights, meaningful-interaction time, enjoyment and human
Adventure Activity Ratio are **NOT MEASURED**. No Item 12 result is claimed.

| Result | SHA-256 |
| --- | --- |
| [results/full-biome-diverse-r1-baseline.json.gz](results/full-biome-diverse-r1-baseline.json.gz) | `ce54267b9c2c6bd904b5099510d196ed4e51096bacb431ecae43c758dce7e9e7` |
| [results/full-biome-diverse-r1-without-sparse.json.gz](results/full-biome-diverse-r1-without-sparse.json.gz) | `491701bd5aad376adbc6f11276384ed17c6df88fdb268728c74204e783819f51` |
| [results/full-biome-diverse-r2-baseline.json.gz](results/full-biome-diverse-r2-baseline.json.gz) | `6e7f818e2feaaf3c4f3afa57f51ad1aacde624dc43e655245245a127c0ea3e09` |
| [results/full-biome-diverse-r2-without-sparse.json.gz](results/full-biome-diverse-r2-without-sparse.json.gz) | `28a77839a160e43e78ff4870915abcfa5276b8fcb4689697c8655201791d35d7` |
| [results/full-mountainous-r1-baseline.json.gz](results/full-mountainous-r1-baseline.json.gz) | `114c8d002e729284f1f0e2200e49a6ef6224347c27f478717c6c6a266b759729` |
| [results/full-mountainous-r1-without-sparse.json.gz](results/full-mountainous-r1-without-sparse.json.gz) | `0f3c22c76acee0b557c92dcc76132e6ab909ef30719b3186c449fd4d5f1b1365` |
| [results/full-mountainous-r2-baseline.json.gz](results/full-mountainous-r2-baseline.json.gz) | `e6d0150bb8faf9dfd18bc70e8f8f17ddb4c8b28207d1fee81687df0596c0e144` |
| [results/full-mountainous-r2-without-sparse.json.gz](results/full-mountainous-r2-without-sparse.json.gz) | `219605c824f5005075801e91d0732954a24206ca43a35684dfa78a7fde40a0cb` |
| [results/full-ocean-heavy-r1-baseline.json.gz](results/full-ocean-heavy-r1-baseline.json.gz) | `c80cfea6acce2eb80df6048e6e47e63de7a9397b520e84491254000834dd3c23` |
| [results/full-ocean-heavy-r1-without-sparse.json.gz](results/full-ocean-heavy-r1-without-sparse.json.gz) | `4c3e24391c5d982b11c6ac716561b70db84af85bfbd65a6a02202aaf53e88e46` |
| [results/full-ocean-heavy-r2-baseline.json.gz](results/full-ocean-heavy-r2-baseline.json.gz) | `9c3520a7ba29280b22d733fb259c2829057d5609b7dae840da4119f4779fb389` |
| [results/full-ocean-heavy-r2-without-sparse-attempt3.json.gz](results/full-ocean-heavy-r2-without-sparse-attempt3.json.gz) | `6748e59f6d8d6fe50c5a3f648fb009c51b411a3e78d596adc3ec10acd7266da8` |
| [results/full-ordinary-r1-baseline.json.gz](results/full-ordinary-r1-baseline.json.gz) | `ca23017a27c5e8334b6213e4d651bf6eaf05f1cf1f186e886831e5e74fa9d80b` |
| [results/full-ordinary-r1-without-sparse.json.gz](results/full-ordinary-r1-without-sparse.json.gz) | `8292441c124d9373c473c5f38b18479444a72c3c8ebc7a1757abb3e5f8fa9e65` |
| [results/full-ordinary-r2-baseline.json.gz](results/full-ordinary-r2-baseline.json.gz) | `3c6504cdfe11149d618494978db8896f3da2b0c764fc9f44c15754dbad5bbb00` |
| [results/full-ordinary-r2-without-sparse.json.gz](results/full-ordinary-r2-without-sparse.json.gz) | `4c10846d8588f158b11a2e1c43b8b7e5e4677d3b9bd328af4e778a70a6ad5f2c` |
