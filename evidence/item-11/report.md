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
| biome-diverse-r1-without-sparse | 1785 | 1758 | 1756 | 6 | 0 | 0 | 0 | 17 | 504 |
| biome-diverse-r2-baseline | 1748 | 1740 | 1739 | 5 | 0 | 0 | 0 | 3 | 176 |
| biome-diverse-r2-without-sparse | 1835 | 1807 | 1805 | 6 | 0 | 0 | 0 | 16 | 504 |
| mountainous-r1-baseline | 1655 | 1647 | 1644 | 5 | 0 | 0 | 0 | 3 | 112 |
| mountainous-r1-without-sparse | 1741 | 1715 | 1713 | 8 | 3 | 0 | 0 | 7 | 344 |
| mountainous-r2-baseline | 1660 | 1651 | 1648 | 5 | 0 | 0 | 0 | 3 | 96 |
| mountainous-r2-without-sparse | 1783 | 1756 | 1754 | 8 | 3 | 0 | 0 | 9 | 360 |
| ocean-heavy-r1-baseline | 422 | 418 | 418 | 4 | 0 | 0 | 0 | 2 | 136 |
| ocean-heavy-r1-without-sparse | 466 | 457 | 456 | 6 | 1 | 0 | 1 | 2 | 72 |
| ocean-heavy-r2-baseline | 457 | 453 | 453 | 4 | 0 | 0 | 0 | 2 | 136 |
| ocean-heavy-r2-without-sparse-attempt3 | 461 | 452 | 451 | 6 | 1 | 0 | 1 | 2 | 72 |
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
| biome-diverse-r1-without-sparse / east-north | 483 | 7 | 13 | 0 | 29/29/0 | I/I/I |
| biome-diverse-r1-without-sparse / east-south | 401 | 2 | 12 | 0 | 5/5/0 | I/I/I |
| biome-diverse-r1-without-sparse / south-east | 499 | 5 | 11 | 0 | 13/13/0 | I/I/I |
| biome-diverse-r1-without-sparse / south-west | 402 | 3 | 25 | 0 | 29/29/0 | I/I/I |
| biome-diverse-r2-baseline / east-north | 459 | 1 | 13 | 0 | 89/89/0 | I/I/I |
| biome-diverse-r2-baseline / east-south | 432 | 0 | 18 | 0 | 5/5/0 | I/I/I |
| biome-diverse-r2-baseline / south-east | 506 | 2 | 8 | 0 | 13/13/0 | I/I/I |
| biome-diverse-r2-baseline / south-west | 351 | 0 | 18 | 1 | 32/32/0 | I/I/I |
| biome-diverse-r2-without-sparse / east-north | 477 | 7 | 10 | 0 | 25/25/0 | I/I/I |
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
| ocean-heavy-r1-without-sparse / east-north | 98 | 2 | 87 | 0 | 0/0/37 | I/I/I |
| ocean-heavy-r1-without-sparse / east-south | 130 | 0 | 76 | 134 | 0/0/756 | I/I/I |
| ocean-heavy-r1-without-sparse / south-east | 158 | 0 | 88 | 0 | 0/0/623 | I/I/I |
| ocean-heavy-r1-without-sparse / south-west | 80 | 0 | 175 | 179 | 0/0/768 | I/I/F |
| ocean-heavy-r2-baseline / east-north | 101 | 0 | 63 | 0 | 0/0/37 | I/I/I |
| ocean-heavy-r2-baseline / east-south | 128 | 0 | 189 | 208 | 0/0/756 | I/I/I |
| ocean-heavy-r2-baseline / south-east | 170 | 2 | 56 | 0 | 0/0/446 | I/I/I |
| ocean-heavy-r2-baseline / south-west | 58 | 0 | 249 | 363 | 0/0/768 | I/I/F |
| ocean-heavy-r2-without-sparse-attempt3 / east-north | 111 | 2 | 80 | 0 | 0/0/37 | I/I/I |
| ocean-heavy-r2-without-sparse-attempt3 / east-south | 114 | 0 | 94 | 181 | 0/0/756 | I/I/I |
| ocean-heavy-r2-without-sparse-attempt3 / south-east | 165 | 0 | 83 | 0 | 0/0/623 | I/I/I |
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
| baseline | 32 | 768 | 3938 | 4 | 136 / 24576 |
| baseline | 64 | 256 | 2933 | 0 | 0 / 8192 |
| baseline | 64 | 512 | 5153 | 6 | 272 / 16384 |
| baseline | 64 | 768 | 8347 | 20 | 1160 / 24576 |
| baseline | 96 | 256 | 4817 | 2 | 72 / 8192 |
| baseline | 96 | 512 | 8214 | 8 | 504 / 16384 |
| baseline | 96 | 768 | 13601 | 36 | 2144 / 24576 |
| without-sparse | 32 | 256 | 1373 | 5 | 128 / 8192 |
| without-sparse | 32 | 512 | 2598 | 5 | 128 / 16384 |
| without-sparse | 32 | 768 | 4123 | 11 | 352 / 24576 |
| without-sparse | 64 | 256 | 3077 | 10 | 224 / 8192 |
| without-sparse | 64 | 512 | 5432 | 18 | 520 / 16384 |
| without-sparse | 64 | 768 | 8771 | 61 | 2464 / 24576 |
| without-sparse | 96 | 256 | 5016 | 23 | 936 / 8192 |
| without-sparse | 96 | 512 | 8608 | 38 | 1568 / 16384 |
| without-sparse | 96 | 768 | 14106 | 98 | 5192 / 24576 |

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
      "iqr": 90.0,
      "max": 160,
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
| biome-diverse-r1 | 8 | 352 |
| biome-diverse-r2 | 87 | 328 |
| mountainous-r1 | 86 | 232 |
| mountainous-r2 | 123 | 264 |
| ocean-heavy-r1 | 44 | -64 |
| ocean-heavy-r2 | 4 | -64 |
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
| [results/full-biome-diverse-r1-baseline.json.gz](results/full-biome-diverse-r1-baseline.json.gz) | `35c10172bf6a31f1121978380c7238a0ca94c88ff40ad259b8f59177498947f4` |
| [results/full-biome-diverse-r1-without-sparse.json.gz](results/full-biome-diverse-r1-without-sparse.json.gz) | `d161189e52a53f4fcbec92f2b37292c0888f795b108ec64e4530ac575d7e139f` |
| [results/full-biome-diverse-r2-baseline.json.gz](results/full-biome-diverse-r2-baseline.json.gz) | `72d5db5130651359f27d189e892773716b282d89173eca53f4a48f5b20e63355` |
| [results/full-biome-diverse-r2-without-sparse.json.gz](results/full-biome-diverse-r2-without-sparse.json.gz) | `2b050cd1616ddf9a1d6dcb74a3b995640819d79981ec4ddc02bc127cc45e7439` |
| [results/full-mountainous-r1-baseline.json.gz](results/full-mountainous-r1-baseline.json.gz) | `61fbd17668f6176b4009ca2f498fee4e392a5799a90edced3612af9693a83eab` |
| [results/full-mountainous-r1-without-sparse.json.gz](results/full-mountainous-r1-without-sparse.json.gz) | `aa941e546d4494858e4d222c5a4e4bd1cc4dc30ce8416d65065e207ec611cf62` |
| [results/full-mountainous-r2-baseline.json.gz](results/full-mountainous-r2-baseline.json.gz) | `bc428469f2c4b70281c09a9587cc7bfa221f2f3e427832ed300c49c44897da95` |
| [results/full-mountainous-r2-without-sparse.json.gz](results/full-mountainous-r2-without-sparse.json.gz) | `41ebbbaa962791b250af377bb9d350aca5f5792c718f1d1acfbe371f8b3ca176` |
| [results/full-ocean-heavy-r1-baseline.json.gz](results/full-ocean-heavy-r1-baseline.json.gz) | `ad5f3cca623fa4b6a359f57ef5962dde729d4621d1da60fc57b1bb8ab0ecd3a7` |
| [results/full-ocean-heavy-r1-without-sparse.json.gz](results/full-ocean-heavy-r1-without-sparse.json.gz) | `7b9d9aee0d79360d1c304e8de0a1c791a2db5b61e2debadde449e5939fa7cc55` |
| [results/full-ocean-heavy-r2-baseline.json.gz](results/full-ocean-heavy-r2-baseline.json.gz) | `0dc1f7960e502135f8b418a43f0913ed8bab1a80540de214f3d53ff186bb9ba6` |
| [results/full-ocean-heavy-r2-without-sparse-attempt3.json.gz](results/full-ocean-heavy-r2-without-sparse-attempt3.json.gz) | `24b0812fa3fa01d431147e5da35cf131dadeed2817fa9b5bc5f3ef7d80e7f1d6` |
| [results/full-ordinary-r1-baseline.json.gz](results/full-ordinary-r1-baseline.json.gz) | `d59cc1ddfe3924ddef69e0efdde2d3477889401d7fd68fa16bcc12e13fd64672` |
| [results/full-ordinary-r1-without-sparse.json.gz](results/full-ordinary-r1-without-sparse.json.gz) | `c2d246a5dc04457a8af5cfe2c03d01d9d140bac084f014d275d3b06ace0b63d5` |
| [results/full-ordinary-r2-baseline.json.gz](results/full-ordinary-r2-baseline.json.gz) | `a8baf43579122389e7ddb9634e507ee74e8a11a7296efe0b1f5e016417d8c207` |
| [results/full-ordinary-r2-without-sparse.json.gz](results/full-ordinary-r2-without-sparse.json.gz) | `3b0aeb4036d87c6c68f77e9b76b0349a14227d6446cd3f5b9521e72f505889d7` |
