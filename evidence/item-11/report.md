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

## Modeled travel costs

Primary 64-block radius, full 768-block window, all-location group; all 192 mode rows.
Values are central seconds [fast-speed seconds, slow-speed seconds], rounded to two decimals.
Completed costs are null for INFEASIBLE/UNKNOWN full-route modes. Prefix costs stop at
the retained reachable prefix; unconstrained costs ignore feasibility and are not actual travel.
Other windows/categories and exact unrounded values remain in the linked raw results.

| World / route / mode | Completed seconds | Prefix seconds | Unconstrained seconds |
| --- | --- | --- | --- |
| biome-diverse-r1-baseline / east-north / boat | null | 0.00 [0.00, 0.00] | 96.00 [76.80, 128.00] |
| biome-diverse-r1-baseline / east-north / horse | null | 4.04 [3.15, 5.66] | 136.09 [105.85, 190.52] |
| biome-diverse-r1-baseline / east-north / walking | null | 7.08 [5.66, 9.44] | 238.15 [190.52, 317.54] |
| biome-diverse-r1-baseline / east-south / boat | null | 0.00 [0.00, 0.00] | 96.00 [76.80, 128.00] |
| biome-diverse-r1-baseline / east-south / horse | null | 0.89 [0.69, 1.25] | 131.09 [101.96, 183.53] |
| biome-diverse-r1-baseline / east-south / walking | null | 1.56 [1.25, 2.08] | 229.41 [183.53, 305.88] |
| biome-diverse-r1-baseline / south-east / boat | null | 0.00 [0.00, 0.00] | 96.00 [76.80, 128.00] |
| biome-diverse-r1-baseline / south-east / horse | null | 1.98 [1.54, 2.77] | 128.80 [100.17, 180.31] |
| biome-diverse-r1-baseline / south-east / walking | null | 3.46 [2.77, 4.61] | 225.39 [180.31, 300.52] |
| biome-diverse-r1-baseline / south-west / boat | null | 0.00 [0.00, 0.00] | 96.00 [76.80, 128.00] |
| biome-diverse-r1-baseline / south-west / horse | null | 4.19 [3.26, 5.86] | 132.60 [103.13, 185.63] |
| biome-diverse-r1-baseline / south-west / walking | null | 7.33 [5.86, 9.77] | 232.04 [185.63, 309.39] |
| biome-diverse-r1-without-sparse / east-north / boat | null | 0.00 [0.00, 0.00] | 96.00 [76.80, 128.00] |
| biome-diverse-r1-without-sparse / east-north / horse | null | 4.62 [3.59, 6.46] | 136.80 [106.40, 191.52] |
| biome-diverse-r1-without-sparse / east-north / walking | null | 8.08 [6.46, 10.77] | 239.40 [191.52, 319.20] |
| biome-diverse-r1-without-sparse / east-south / boat | null | 0.00 [0.00, 0.00] | 96.00 [76.80, 128.00] |
| biome-diverse-r1-without-sparse / east-south / horse | null | 0.89 [0.69, 1.25] | 130.40 [101.42, 182.56] |
| biome-diverse-r1-without-sparse / east-south / walking | null | 1.56 [1.25, 2.08] | 228.20 [182.56, 304.26] |
| biome-diverse-r1-without-sparse / south-east / boat | null | 0.00 [0.00, 0.00] | 96.00 [76.80, 128.00] |
| biome-diverse-r1-without-sparse / south-east / horse | null | 1.98 [1.54, 2.77] | 128.46 [99.91, 179.84] |
| biome-diverse-r1-without-sparse / south-east / walking | null | 3.46 [2.77, 4.61] | 224.80 [179.84, 299.73] |
| biome-diverse-r1-without-sparse / south-west / boat | null | 0.00 [0.00, 0.00] | 96.00 [76.80, 128.00] |
| biome-diverse-r1-without-sparse / south-west / horse | null | 4.79 [3.73, 6.71] | 128.88 [100.24, 180.43] |
| biome-diverse-r1-without-sparse / south-west / walking | null | 8.39 [6.71, 11.19] | 225.54 [180.43, 300.71] |
| biome-diverse-r2-baseline / east-north / boat | null | 0.00 [0.00, 0.00] | 96.00 [76.80, 128.00] |
| biome-diverse-r2-baseline / east-north / horse | null | 14.43 [11.22, 20.20] | 130.70 [101.65, 182.97] |
| biome-diverse-r2-baseline / east-north / walking | null | 25.25 [20.20, 33.67] | 228.72 [182.97, 304.96] |
| biome-diverse-r2-baseline / east-south / boat | null | 0.00 [0.00, 0.00] | 96.00 [76.80, 128.00] |
| biome-diverse-r2-baseline / east-south / horse | null | 0.89 [0.69, 1.25] | 131.77 [102.49, 184.47] |
| biome-diverse-r2-baseline / east-south / walking | null | 1.56 [1.25, 2.08] | 230.59 [184.47, 307.46] |
| biome-diverse-r2-baseline / south-east / boat | null | 0.00 [0.00, 0.00] | 96.00 [76.80, 128.00] |
| biome-diverse-r2-baseline / south-east / horse | null | 1.98 [1.54, 2.77] | 126.83 [98.65, 177.56] |
| biome-diverse-r2-baseline / south-east / walking | null | 3.46 [2.77, 4.61] | 221.96 [177.56, 295.94] |
| biome-diverse-r2-baseline / south-west / boat | null | 0.00 [0.00, 0.00] | 96.00 [76.80, 128.00] |
| biome-diverse-r2-baseline / south-west / horse | null | 5.40 [4.20, 7.56] | 125.03 [97.24, 175.04] |
| biome-diverse-r2-baseline / south-west / walking | null | 9.45 [7.56, 12.60] | 218.80 [175.04, 291.73] |
| biome-diverse-r2-without-sparse / east-north / boat | null | 0.00 [0.00, 0.00] | 96.00 [76.80, 128.00] |
| biome-diverse-r2-without-sparse / east-north / horse | null | 3.99 [3.10, 5.58] | 139.57 [108.56, 195.40] |
| biome-diverse-r2-without-sparse / east-north / walking | null | 6.97 [5.58, 9.30] | 244.25 [195.40, 325.67] |
| biome-diverse-r2-without-sparse / east-south / boat | null | 0.00 [0.00, 0.00] | 96.00 [76.80, 128.00] |
| biome-diverse-r2-without-sparse / east-south / horse | null | 0.89 [0.69, 1.25] | 128.77 [100.15, 180.27] |
| biome-diverse-r2-without-sparse / east-south / walking | null | 1.56 [1.25, 2.08] | 225.34 [180.27, 300.46] |
| biome-diverse-r2-without-sparse / south-east / boat | null | 0.00 [0.00, 0.00] | 96.00 [76.80, 128.00] |
| biome-diverse-r2-without-sparse / south-east / horse | null | 1.98 [1.54, 2.77] | 126.27 [98.21, 176.77] |
| biome-diverse-r2-without-sparse / south-east / walking | null | 3.46 [2.77, 4.61] | 220.97 [176.77, 294.62] |
| biome-diverse-r2-without-sparse / south-west / boat | null | 0.00 [0.00, 0.00] | 96.00 [76.80, 128.00] |
| biome-diverse-r2-without-sparse / south-west / horse | null | 4.68 [3.64, 6.55] | 128.20 [99.71, 179.49] |
| biome-diverse-r2-without-sparse / south-west / walking | null | 8.18 [6.55, 10.91] | 224.36 [179.49, 299.14] |
| mountainous-r1-baseline / east-north / boat | null | 0.00 [0.00, 0.00] | 96.00 [76.80, 128.00] |
| mountainous-r1-baseline / east-north / horse | null | 1.95 [1.52, 2.73] | 160.20 [124.60, 224.27] |
| mountainous-r1-baseline / east-north / walking | null | 3.41 [2.73, 4.55] | 280.34 [224.27, 373.79] |
| mountainous-r1-baseline / east-south / boat | null | 0.00 [0.00, 0.00] | 96.00 [76.80, 128.00] |
| mountainous-r1-baseline / east-south / horse | null | 5.57 [4.33, 7.79] | 233.11 [181.31, 326.35] |
| mountainous-r1-baseline / east-south / walking | null | 9.74 [7.79, 12.99] | 407.94 [326.35, 543.92] |
| mountainous-r1-baseline / south-east / boat | null | 0.00 [0.00, 0.00] | 96.00 [76.80, 128.00] |
| mountainous-r1-baseline / south-east / horse | null | 7.24 [5.63, 10.14] | 213.05 [165.70, 298.26] |
| mountainous-r1-baseline / south-east / walking | null | 12.67 [10.14, 16.90] | 372.83 [298.26, 497.11] |
| mountainous-r1-baseline / south-west / boat | null | 0.00 [0.00, 0.00] | 96.00 [76.80, 128.00] |
| mountainous-r1-baseline / south-west / horse | null | 3.79 [2.95, 5.31] | 225.66 [175.52, 315.93] |
| mountainous-r1-baseline / south-west / walking | null | 6.64 [5.31, 8.85] | 394.91 [315.93, 526.55] |
| mountainous-r1-without-sparse / east-north / boat | null | 0.00 [0.00, 0.00] | 96.00 [76.80, 128.00] |
| mountainous-r1-without-sparse / east-north / horse | null | 1.77 [1.38, 2.48] | 172.33 [134.04, 241.26] |
| mountainous-r1-without-sparse / east-north / walking | null | 3.10 [2.48, 4.14] | 301.58 [241.26, 402.11] |
| mountainous-r1-without-sparse / east-south / boat | null | 0.00 [0.00, 0.00] | 96.00 [76.80, 128.00] |
| mountainous-r1-without-sparse / east-south / horse | null | 7.85 [6.10, 10.99] | 267.94 [208.40, 375.12] |
| mountainous-r1-without-sparse / east-south / walking | null | 13.74 [10.99, 18.31] | 468.90 [375.12, 625.20] |
| mountainous-r1-without-sparse / south-east / boat | null | 0.00 [0.00, 0.00] | 96.00 [76.80, 128.00] |
| mountainous-r1-without-sparse / south-east / horse | null | 9.09 [7.07, 12.72] | 205.54 [159.87, 287.76] |
| mountainous-r1-without-sparse / south-east / walking | null | 15.90 [12.72, 21.20] | 359.70 [287.76, 479.60] |
| mountainous-r1-without-sparse / south-west / boat | null | 0.00 [0.00, 0.00] | 96.00 [76.80, 128.00] |
| mountainous-r1-without-sparse / south-west / horse | null | 3.62 [2.81, 5.06] | 185.54 [144.31, 259.76] |
| mountainous-r1-without-sparse / south-west / walking | null | 6.33 [5.06, 8.44] | 324.70 [259.76, 432.93] |
| mountainous-r2-baseline / east-north / boat | null | 0.00 [0.00, 0.00] | 96.00 [76.80, 128.00] |
| mountainous-r2-baseline / east-north / horse | null | 2.01 [1.56, 2.81] | 161.14 [125.33, 225.60] |
| mountainous-r2-baseline / east-north / walking | null | 3.52 [2.81, 4.69] | 282.00 [225.60, 376.00] |
| mountainous-r2-baseline / east-south / boat | null | 0.00 [0.00, 0.00] | 96.00 [76.80, 128.00] |
| mountainous-r2-baseline / east-south / horse | null | 0.81 [0.63, 1.13] | 258.60 [201.13, 362.04] |
| mountainous-r2-baseline / east-south / walking | null | 1.41 [1.13, 1.89] | 452.55 [362.04, 603.40] |
| mountainous-r2-baseline / south-east / boat | null | 0.00 [0.00, 0.00] | 96.00 [76.80, 128.00] |
| mountainous-r2-baseline / south-east / horse | null | 0.00 [0.00, 0.00] | 214.74 [167.02, 300.64] |
| mountainous-r2-baseline / south-east / walking | null | 0.00 [0.00, 0.00] | 375.80 [300.64, 501.06] |
| mountainous-r2-baseline / south-west / boat | null | 0.00 [0.00, 0.00] | 96.00 [76.80, 128.00] |
| mountainous-r2-baseline / south-west / horse | null | 1.32 [1.03, 1.85] | 203.29 [158.11, 284.60] |
| mountainous-r2-baseline / south-west / walking | null | 2.31 [1.85, 3.08] | 355.75 [284.60, 474.33] |
| mountainous-r2-without-sparse / east-north / boat | null | 0.00 [0.00, 0.00] | 96.00 [76.80, 128.00] |
| mountainous-r2-without-sparse / east-north / horse | null | 1.92 [1.49, 2.68] | 172.56 [134.21, 241.58] |
| mountainous-r2-without-sparse / east-north / walking | null | 3.35 [2.68, 4.47] | 301.97 [241.58, 402.63] |
| mountainous-r2-without-sparse / east-south / boat | null | 0.00 [0.00, 0.00] | 96.00 [76.80, 128.00] |
| mountainous-r2-without-sparse / east-south / horse | null | 6.78 [5.27, 9.49] | 243.99 [189.77, 341.59] |
| mountainous-r2-without-sparse / east-south / walking | null | 11.86 [9.49, 15.82] | 426.99 [341.59, 569.32] |
| mountainous-r2-without-sparse / south-east / boat | null | 0.00 [0.00, 0.00] | 96.00 [76.80, 128.00] |
| mountainous-r2-without-sparse / south-east / horse | null | 1.64 [1.28, 2.30] | 207.15 [161.12, 290.01] |
| mountainous-r2-without-sparse / south-east / walking | null | 2.87 [2.30, 3.83] | 362.51 [290.01, 483.35] |
| mountainous-r2-without-sparse / south-west / boat | null | 0.00 [0.00, 0.00] | 96.00 [76.80, 128.00] |
| mountainous-r2-without-sparse / south-west / horse | null | 1.44 [1.12, 2.01] | 202.86 [157.78, 284.01] |
| mountainous-r2-without-sparse / south-west / walking | null | 2.52 [2.01, 3.36] | 355.01 [284.01, 473.34] |
| ocean-heavy-r1-baseline / east-north / boat | null | 4.62 [3.70, 6.17] | 96.00 [76.80, 128.00] |
| ocean-heavy-r1-baseline / east-north / horse | null | 0.00 [0.00, 0.00] | 110.42 [85.88, 154.59] |
| ocean-heavy-r1-baseline / east-north / walking | null | 0.00 [0.00, 0.00] | 193.24 [154.59, 257.65] |
| ocean-heavy-r1-baseline / east-south / boat | null | 94.50 [75.60, 126.00] | 96.00 [76.80, 128.00] |
| ocean-heavy-r1-baseline / east-south / horse | null | 0.00 [0.00, 0.00] | 110.81 [86.19, 155.13] |
| ocean-heavy-r1-baseline / east-south / walking | null | 0.00 [0.00, 0.00] | 193.92 [155.13, 258.56] |
| ocean-heavy-r1-baseline / south-east / boat | null | 55.75 [44.60, 74.33] | 96.00 [76.80, 128.00] |
| ocean-heavy-r1-baseline / south-east / horse | null | 0.00 [0.00, 0.00] | 141.34 [109.93, 197.88] |
| ocean-heavy-r1-baseline / south-east / walking | null | 0.00 [0.00, 0.00] | 247.35 [197.88, 329.80] |
| ocean-heavy-r1-baseline / south-west / boat | 96.00 [76.80, 128.00] | 96.00 [76.80, 128.00] | 96.00 [76.80, 128.00] |
| ocean-heavy-r1-baseline / south-west / horse | null | 0.00 [0.00, 0.00] | 109.71 [85.33, 153.60] |
| ocean-heavy-r1-baseline / south-west / walking | null | 0.00 [0.00, 0.00] | 192.00 [153.60, 256.00] |
| ocean-heavy-r1-without-sparse / east-north / boat | null | 4.62 [3.70, 6.17] | 96.00 [76.80, 128.00] |
| ocean-heavy-r1-without-sparse / east-north / horse | null | 0.00 [0.00, 0.00] | 289.52 [225.18, 405.33] |
| ocean-heavy-r1-without-sparse / east-north / walking | null | 0.00 [0.00, 0.00] | 506.66 [405.33, 675.55] |
| ocean-heavy-r1-without-sparse / east-south / boat | null | 94.50 [75.60, 126.00] | 96.00 [76.80, 128.00] |
| ocean-heavy-r1-without-sparse / east-south / horse | null | 0.00 [0.00, 0.00] | 110.81 [86.19, 155.13] |
| ocean-heavy-r1-without-sparse / east-south / walking | null | 0.00 [0.00, 0.00] | 193.92 [155.13, 258.56] |
| ocean-heavy-r1-without-sparse / south-east / boat | null | 77.88 [62.30, 103.83] | 96.00 [76.80, 128.00] |
| ocean-heavy-r1-without-sparse / south-east / horse | null | 0.00 [0.00, 0.00] | 147.16 [114.46, 206.03] |
| ocean-heavy-r1-without-sparse / south-east / walking | null | 0.00 [0.00, 0.00] | 257.53 [206.03, 343.38] |
| ocean-heavy-r1-without-sparse / south-west / boat | 96.00 [76.80, 128.00] | 96.00 [76.80, 128.00] | 96.00 [76.80, 128.00] |
| ocean-heavy-r1-without-sparse / south-west / horse | null | 0.00 [0.00, 0.00] | 109.71 [85.33, 153.60] |
| ocean-heavy-r1-without-sparse / south-west / walking | null | 0.00 [0.00, 0.00] | 192.00 [153.60, 256.00] |
| ocean-heavy-r2-baseline / east-north / boat | null | 4.62 [3.70, 6.17] | 96.00 [76.80, 128.00] |
| ocean-heavy-r2-baseline / east-north / horse | null | 0.00 [0.00, 0.00] | 112.74 [87.68, 157.83] |
| ocean-heavy-r2-baseline / east-north / walking | null | 0.00 [0.00, 0.00] | 197.29 [157.83, 263.05] |
| ocean-heavy-r2-baseline / east-south / boat | null | 94.50 [75.60, 126.00] | 96.00 [76.80, 128.00] |
| ocean-heavy-r2-baseline / east-south / horse | null | 0.00 [0.00, 0.00] | 110.93 [86.28, 155.30] |
| ocean-heavy-r2-baseline / east-south / walking | null | 0.00 [0.00, 0.00] | 194.12 [155.30, 258.83] |
| ocean-heavy-r2-baseline / south-east / boat | null | 55.75 [44.60, 74.33] | 96.00 [76.80, 128.00] |
| ocean-heavy-r2-baseline / south-east / horse | null | 0.00 [0.00, 0.00] | 141.34 [109.93, 197.88] |
| ocean-heavy-r2-baseline / south-east / walking | null | 0.00 [0.00, 0.00] | 247.35 [197.88, 329.80] |
| ocean-heavy-r2-baseline / south-west / boat | 96.00 [76.80, 128.00] | 96.00 [76.80, 128.00] | 96.00 [76.80, 128.00] |
| ocean-heavy-r2-baseline / south-west / horse | null | 0.00 [0.00, 0.00] | 109.71 [85.33, 153.60] |
| ocean-heavy-r2-baseline / south-west / walking | null | 0.00 [0.00, 0.00] | 192.00 [153.60, 256.00] |
| ocean-heavy-r2-without-sparse-attempt3 / east-north / boat | null | 4.62 [3.70, 6.17] | 96.00 [76.80, 128.00] |
| ocean-heavy-r2-without-sparse-attempt3 / east-north / horse | null | 0.00 [0.00, 0.00] | 289.24 [224.96, 404.93] |
| ocean-heavy-r2-without-sparse-attempt3 / east-north / walking | null | 0.00 [0.00, 0.00] | 506.16 [404.93, 674.89] |
| ocean-heavy-r2-without-sparse-attempt3 / east-south / boat | null | 94.50 [75.60, 126.00] | 96.00 [76.80, 128.00] |
| ocean-heavy-r2-without-sparse-attempt3 / east-south / horse | null | 0.00 [0.00, 0.00] | 110.81 [86.19, 155.13] |
| ocean-heavy-r2-without-sparse-attempt3 / east-south / walking | null | 0.00 [0.00, 0.00] | 193.92 [155.13, 258.56] |
| ocean-heavy-r2-without-sparse-attempt3 / south-east / boat | null | 77.88 [62.30, 103.83] | 96.00 [76.80, 128.00] |
| ocean-heavy-r2-without-sparse-attempt3 / south-east / horse | null | 0.00 [0.00, 0.00] | 147.16 [114.46, 206.03] |
| ocean-heavy-r2-without-sparse-attempt3 / south-east / walking | null | 0.00 [0.00, 0.00] | 257.53 [206.03, 343.38] |
| ocean-heavy-r2-without-sparse-attempt3 / south-west / boat | 96.00 [76.80, 128.00] | 96.00 [76.80, 128.00] | 96.00 [76.80, 128.00] |
| ocean-heavy-r2-without-sparse-attempt3 / south-west / horse | null | 0.00 [0.00, 0.00] | 109.71 [85.33, 153.60] |
| ocean-heavy-r2-without-sparse-attempt3 / south-west / walking | null | 0.00 [0.00, 0.00] | 192.00 [153.60, 256.00] |
| ordinary-r1-baseline / east-north / boat | 96.00 [76.80, 128.00] | 96.00 [76.80, 128.00] | 96.00 [76.80, 128.00] |
| ordinary-r1-baseline / east-north / horse | null | 0.00 [0.00, 0.00] | 109.71 [85.33, 153.60] |
| ordinary-r1-baseline / east-north / walking | null | 0.00 [0.00, 0.00] | 192.00 [153.60, 256.00] |
| ordinary-r1-baseline / east-south / boat | 96.00 [76.80, 128.00] | 96.00 [76.80, 128.00] | 96.00 [76.80, 128.00] |
| ordinary-r1-baseline / east-south / horse | null | 0.00 [0.00, 0.00] | 109.71 [85.33, 153.60] |
| ordinary-r1-baseline / east-south / walking | null | 0.00 [0.00, 0.00] | 192.00 [153.60, 256.00] |
| ordinary-r1-baseline / south-east / boat | 96.00 [76.80, 128.00] | 96.00 [76.80, 128.00] | 96.00 [76.80, 128.00] |
| ordinary-r1-baseline / south-east / horse | null | 0.00 [0.00, 0.00] | 109.71 [85.33, 153.60] |
| ordinary-r1-baseline / south-east / walking | null | 0.00 [0.00, 0.00] | 192.00 [153.60, 256.00] |
| ordinary-r1-baseline / south-west / boat | 96.00 [76.80, 128.00] | 96.00 [76.80, 128.00] | 96.00 [76.80, 128.00] |
| ordinary-r1-baseline / south-west / horse | null | 0.00 [0.00, 0.00] | 109.71 [85.33, 153.60] |
| ordinary-r1-baseline / south-west / walking | null | 0.00 [0.00, 0.00] | 192.00 [153.60, 256.00] |
| ordinary-r1-without-sparse / east-north / boat | null | 73.62 [58.90, 98.17] | 96.00 [76.80, 128.00] |
| ordinary-r1-without-sparse / east-north / horse | null | 0.00 [0.00, 0.00] | 176.02 [136.90, 246.43] |
| ordinary-r1-without-sparse / east-north / walking | null | 0.00 [0.00, 0.00] | 308.03 [246.43, 410.71] |
| ordinary-r1-without-sparse / east-south / boat | 96.00 [76.80, 128.00] | 96.00 [76.80, 128.00] | 96.00 [76.80, 128.00] |
| ordinary-r1-without-sparse / east-south / horse | null | 0.00 [0.00, 0.00] | 109.71 [85.33, 153.60] |
| ordinary-r1-without-sparse / east-south / walking | null | 0.00 [0.00, 0.00] | 192.00 [153.60, 256.00] |
| ordinary-r1-without-sparse / south-east / boat | null | 77.00 [61.60, 102.67] | 96.00 [76.80, 128.00] |
| ordinary-r1-without-sparse / south-east / horse | null | 0.00 [0.00, 0.00] | 258.89 [201.36, 362.45] |
| ordinary-r1-without-sparse / south-east / walking | null | 0.00 [0.00, 0.00] | 453.06 [362.45, 604.08] |
| ordinary-r1-without-sparse / south-west / boat | 96.00 [76.80, 128.00] | 96.00 [76.80, 128.00] | 96.00 [76.80, 128.00] |
| ordinary-r1-without-sparse / south-west / horse | null | 0.00 [0.00, 0.00] | 109.71 [85.33, 153.60] |
| ordinary-r1-without-sparse / south-west / walking | null | 0.00 [0.00, 0.00] | 192.00 [153.60, 256.00] |
| ordinary-r2-baseline / east-north / boat | 96.00 [76.80, 128.00] | 96.00 [76.80, 128.00] | 96.00 [76.80, 128.00] |
| ordinary-r2-baseline / east-north / horse | null | 0.00 [0.00, 0.00] | 109.71 [85.33, 153.60] |
| ordinary-r2-baseline / east-north / walking | null | 0.00 [0.00, 0.00] | 192.00 [153.60, 256.00] |
| ordinary-r2-baseline / east-south / boat | 96.00 [76.80, 128.00] | 96.00 [76.80, 128.00] | 96.00 [76.80, 128.00] |
| ordinary-r2-baseline / east-south / horse | null | 0.00 [0.00, 0.00] | 109.71 [85.33, 153.60] |
| ordinary-r2-baseline / east-south / walking | null | 0.00 [0.00, 0.00] | 192.00 [153.60, 256.00] |
| ordinary-r2-baseline / south-east / boat | 96.00 [76.80, 128.00] | 96.00 [76.80, 128.00] | 96.00 [76.80, 128.00] |
| ordinary-r2-baseline / south-east / horse | null | 0.00 [0.00, 0.00] | 109.71 [85.33, 153.60] |
| ordinary-r2-baseline / south-east / walking | null | 0.00 [0.00, 0.00] | 192.00 [153.60, 256.00] |
| ordinary-r2-baseline / south-west / boat | 96.00 [76.80, 128.00] | 96.00 [76.80, 128.00] | 96.00 [76.80, 128.00] |
| ordinary-r2-baseline / south-west / horse | null | 0.00 [0.00, 0.00] | 109.71 [85.33, 153.60] |
| ordinary-r2-baseline / south-west / walking | null | 0.00 [0.00, 0.00] | 192.00 [153.60, 256.00] |
| ordinary-r2-without-sparse / east-north / boat | null | 73.62 [58.90, 98.17] | 96.00 [76.80, 128.00] |
| ordinary-r2-without-sparse / east-north / horse | null | 0.00 [0.00, 0.00] | 176.02 [136.90, 246.43] |
| ordinary-r2-without-sparse / east-north / walking | null | 0.00 [0.00, 0.00] | 308.03 [246.43, 410.71] |
| ordinary-r2-without-sparse / east-south / boat | 96.00 [76.80, 128.00] | 96.00 [76.80, 128.00] | 96.00 [76.80, 128.00] |
| ordinary-r2-without-sparse / east-south / horse | null | 0.00 [0.00, 0.00] | 109.71 [85.33, 153.60] |
| ordinary-r2-without-sparse / east-south / walking | null | 0.00 [0.00, 0.00] | 192.00 [153.60, 256.00] |
| ordinary-r2-without-sparse / south-east / boat | null | 77.00 [61.60, 102.67] | 96.00 [76.80, 128.00] |
| ordinary-r2-without-sparse / south-east / horse | null | 0.00 [0.00, 0.00] | 258.89 [201.36, 362.45] |
| ordinary-r2-without-sparse / south-east / walking | null | 0.00 [0.00, 0.00] | 453.06 [362.45, 604.08] |
| ordinary-r2-without-sparse / south-west / boat | 96.00 [76.80, 128.00] | 96.00 [76.80, 128.00] | 96.00 [76.80, 128.00] |
| ordinary-r2-without-sparse / south-west / horse | null | 0.00 [0.00, 0.00] | 109.71 [85.33, 153.60] |
| ordinary-r2-without-sparse / south-west / walking | null | 0.00 [0.00, 0.00] | 192.00 [153.60, 256.00] |

## Modeled repeated-family interval times

Same primary group/window and all 192 modes. Adjacent-anchor and first-ray-clear events
remain separate. Each cell gives interval count, central-speed median, central-speed
minimum/maximum, and the envelope across all intervals and the declared speed range.
All times are unconstrained modeled seconds, including for infeasible modes. The speed
envelope expresses assumptions plus interval spread, not a population confidence interval.
Zero ties are retained. No-repeat rows are right-censored at 768 blocks, not infinite variety.
Category-specific and other window/radius intervals remain in the linked raw results.

| World / route / mode | Adjacent-family interval seconds | Ray-clear-family interval seconds |
| --- | --- | --- |
| biome-diverse-r1-baseline / east-north / boat | 464; median 0.12; central [0.00, 8.00]; speed [0.00, 10.67] | 0; No repeat: right-censored at 768 blocks |
| biome-diverse-r1-baseline / east-north / horse | 464; median 0.20; central [0.00, 12.95]; speed [0.00, 18.13] | 0; No repeat: right-censored at 768 blocks |
| biome-diverse-r1-baseline / east-north / walking | 464; median 0.35; central [0.00, 22.67]; speed [0.00, 30.22] | 0; No repeat: right-censored at 768 blocks |
| biome-diverse-r1-baseline / east-south / boat | 436; median 0.12; central [0.00, 10.00]; speed [0.00, 13.33] | 0; No repeat: right-censored at 768 blocks |
| biome-diverse-r1-baseline / east-south / horse | 436; median 0.20; central [0.00, 14.86]; speed [0.00, 20.80] | 0; No repeat: right-censored at 768 blocks |
| biome-diverse-r1-baseline / east-south / walking | 436; median 0.35; central [0.00, 26.00]; speed [0.00, 34.67] | 0; No repeat: right-censored at 768 blocks |
| biome-diverse-r1-baseline / south-east / boat | 474; median 0.12; central [0.00, 10.00]; speed [0.00, 13.33] | 0; No repeat: right-censored at 768 blocks |
| biome-diverse-r1-baseline / south-east / horse | 474; median 0.20; central [0.00, 11.67]; speed [0.00, 16.33] | 0; No repeat: right-censored at 768 blocks |
| biome-diverse-r1-baseline / south-east / walking | 474; median 0.35; central [0.00, 20.41]; speed [0.00, 27.22] | 0; No repeat: right-censored at 768 blocks |
| biome-diverse-r1-baseline / south-west / boat | 379; median 0.25; central [0.00, 12.00]; speed [0.00, 16.00] | 0; No repeat: right-censored at 768 blocks |
| biome-diverse-r1-baseline / south-west / horse | 379; median 0.29; central [0.00, 19.25]; speed [0.00, 26.95] | 0; No repeat: right-censored at 768 blocks |
| biome-diverse-r1-baseline / south-west / walking | 379; median 0.50; central [0.00, 33.69]; speed [0.00, 44.92] | 0; No repeat: right-censored at 768 blocks |
| biome-diverse-r1-without-sparse / east-north / boat | 469; median 0.12; central [0.00, 8.00]; speed [0.00, 10.67] | 0; No repeat: right-censored at 768 blocks |
| biome-diverse-r1-without-sparse / east-north / horse | 469; median 0.20; central [0.00, 12.45]; speed [0.00, 17.42] | 0; No repeat: right-censored at 768 blocks |
| biome-diverse-r1-without-sparse / east-north / walking | 469; median 0.35; central [0.00, 21.78]; speed [0.00, 29.04] | 0; No repeat: right-censored at 768 blocks |
| biome-diverse-r1-without-sparse / east-south / boat | 395; median 0.12; central [0.00, 50.00]; speed [0.00, 66.67] | 1; median 50.00; central [50.00, 50.00]; speed [40.00, 66.67] |
| biome-diverse-r1-without-sparse / east-south / horse | 395; median 0.20; central [0.00, 69.12]; speed [0.00, 96.76] | 1; median 65.89; central [65.89, 65.89]; speed [51.25, 92.25] |
| biome-diverse-r1-without-sparse / east-south / walking | 395; median 0.35; central [0.00, 120.96]; speed [0.00, 161.27] | 1; median 115.31; central [115.31, 115.31]; speed [92.25, 153.75] |
| biome-diverse-r1-without-sparse / south-east / boat | 489; median 0.12; central [0.00, 44.00]; speed [0.00, 58.67] | 2; median 0.50; central [0.00, 1.00]; speed [0.00, 1.33] |
| biome-diverse-r1-without-sparse / south-east / horse | 489; median 0.20; central [0.00, 58.15]; speed [0.00, 81.40] | 2; median 0.57; central [0.00, 1.14]; speed [0.00, 1.60] |
| biome-diverse-r1-without-sparse / south-east / walking | 489; median 0.35; central [0.00, 101.76]; speed [0.00, 135.67] | 2; median 1.00; central [0.00, 2.00]; speed [0.00, 2.67] |
| biome-diverse-r1-without-sparse / south-west / boat | 390; median 0.12; central [0.00, 48.00]; speed [0.00, 64.00] | 0; No repeat: right-censored at 768 blocks |
| biome-diverse-r1-without-sparse / south-west / horse | 390; median 0.29; central [0.00, 58.25]; speed [0.00, 81.56] | 0; No repeat: right-censored at 768 blocks |
| biome-diverse-r1-without-sparse / south-west / walking | 390; median 0.50; central [0.00, 101.95]; speed [0.00, 135.93] | 0; No repeat: right-censored at 768 blocks |
| biome-diverse-r2-baseline / east-north / boat | 452; median 0.12; central [0.00, 8.00]; speed [0.00, 10.67] | 0; No repeat: right-censored at 768 blocks |
| biome-diverse-r2-baseline / east-north / horse | 452; median 0.20; central [0.00, 12.65]; speed [0.00, 17.71] | 0; No repeat: right-censored at 768 blocks |
| biome-diverse-r2-baseline / east-north / walking | 452; median 0.35; central [0.00, 22.13]; speed [0.00, 29.51] | 0; No repeat: right-censored at 768 blocks |
| biome-diverse-r2-baseline / east-south / boat | 429; median 0.12; central [0.00, 10.00]; speed [0.00, 13.33] | 0; No repeat: right-censored at 768 blocks |
| biome-diverse-r2-baseline / east-south / horse | 429; median 0.14; central [0.00, 15.03]; speed [0.00, 21.05] | 0; No repeat: right-censored at 768 blocks |
| biome-diverse-r2-baseline / east-south / walking | 429; median 0.25; central [0.00, 26.31]; speed [0.00, 35.08] | 0; No repeat: right-censored at 768 blocks |
| biome-diverse-r2-baseline / south-east / boat | 495; median 0.12; central [0.00, 89.75]; speed [0.00, 119.67] | 0; No repeat: right-censored at 768 blocks |
| biome-diverse-r2-baseline / south-east / horse | 495; median 0.20; central [0.00, 119.10]; speed [0.00, 166.74] | 0; No repeat: right-censored at 768 blocks |
| biome-diverse-r2-baseline / south-east / walking | 495; median 0.35; central [0.00, 208.42]; speed [0.00, 277.90] | 0; No repeat: right-censored at 768 blocks |
| biome-diverse-r2-baseline / south-west / boat | 347; median 0.25; central [0.00, 12.00]; speed [0.00, 16.00] | 0; No repeat: right-censored at 768 blocks |
| biome-diverse-r2-baseline / south-west / horse | 347; median 0.29; central [0.00, 15.84]; speed [0.00, 22.18] | 0; No repeat: right-censored at 768 blocks |
| biome-diverse-r2-baseline / south-west / walking | 347; median 0.50; central [0.00, 27.73]; speed [0.00, 36.97] | 0; No repeat: right-censored at 768 blocks |
| biome-diverse-r2-without-sparse / east-north / boat | 462; median 0.12; central [0.00, 8.00]; speed [0.00, 10.67] | 0; No repeat: right-censored at 768 blocks |
| biome-diverse-r2-without-sparse / east-north / horse | 462; median 0.20; central [0.00, 17.82]; speed [0.00, 24.95] | 0; No repeat: right-censored at 768 blocks |
| biome-diverse-r2-without-sparse / east-north / walking | 462; median 0.35; central [0.00, 31.19]; speed [0.00, 41.59] | 0; No repeat: right-censored at 768 blocks |
| biome-diverse-r2-without-sparse / east-south / boat | 432; median 0.12; central [0.00, 50.00]; speed [0.00, 66.67] | 1; median 49.00; central [49.00, 49.00]; speed [39.20, 65.33] |
| biome-diverse-r2-without-sparse / east-south / horse | 432; median 0.17; central [0.00, 69.40]; speed [0.00, 97.16] | 1; median 64.27; central [64.27, 64.27]; speed [49.99, 89.98] |
| biome-diverse-r2-without-sparse / east-south / walking | 432; median 0.30; central [0.00, 121.45]; speed [0.00, 161.93] | 1; median 112.47; central [112.47, 112.47]; speed [89.98, 149.96] |
| biome-diverse-r2-without-sparse / south-east / boat | 517; median 0.12; central [0.00, 44.00]; speed [0.00, 58.67] | 2; median 0.50; central [0.00, 1.00]; speed [0.00, 1.33] |
| biome-diverse-r2-without-sparse / south-east / horse | 517; median 0.14; central [0.00, 58.74]; speed [0.00, 82.23] | 2; median 0.57; central [0.00, 1.14]; speed [0.00, 1.60] |
| biome-diverse-r2-without-sparse / south-east / walking | 517; median 0.25; central [0.00, 102.79]; speed [0.00, 137.05] | 2; median 1.00; central [0.00, 2.00]; speed [0.00, 2.67] |
| biome-diverse-r2-without-sparse / south-west / boat | 380; median 0.25; central [0.00, 48.00]; speed [0.00, 64.00] | 0; No repeat: right-censored at 768 blocks |
| biome-diverse-r2-without-sparse / south-west / horse | 380; median 0.29; central [0.00, 57.92]; speed [0.00, 81.09] | 0; No repeat: right-censored at 768 blocks |
| biome-diverse-r2-without-sparse / south-west / walking | 380; median 0.50; central [0.00, 101.36]; speed [0.00, 135.15] | 0; No repeat: right-censored at 768 blocks |
| mountainous-r1-baseline / east-north / boat | 395; median 0.12; central [0.00, 48.00]; speed [0.00, 64.00] | 0; No repeat: right-censored at 768 blocks |
| mountainous-r1-baseline / east-north / horse | 395; median 0.29; central [0.00, 76.45]; speed [0.00, 107.03] | 0; No repeat: right-censored at 768 blocks |
| mountainous-r1-baseline / east-north / walking | 395; median 0.50; central [0.00, 133.79]; speed [0.00, 178.39] | 0; No repeat: right-censored at 768 blocks |
| mountainous-r1-baseline / east-south / boat | 424; median 0.12; central [0.00, 20.00]; speed [0.00, 26.67] | 0; No repeat: right-censored at 768 blocks |
| mountainous-r1-baseline / east-south / horse | 424; median 0.29; central [0.00, 86.14]; speed [0.00, 120.59] | 0; No repeat: right-censored at 768 blocks |
| mountainous-r1-baseline / east-south / walking | 424; median 0.50; central [0.00, 150.74]; speed [0.00, 200.99] | 0; No repeat: right-censored at 768 blocks |
| mountainous-r1-baseline / south-east / boat | 386; median 0.12; central [0.00, 26.00]; speed [0.00, 34.67] | 0; No repeat: right-censored at 768 blocks |
| mountainous-r1-baseline / south-east / horse | 386; median 0.32; central [0.00, 44.60]; speed [0.00, 62.44] | 0; No repeat: right-censored at 768 blocks |
| mountainous-r1-baseline / south-east / walking | 386; median 0.56; central [0.00, 78.05]; speed [0.00, 104.06] | 0; No repeat: right-censored at 768 blocks |
| mountainous-r1-baseline / south-west / boat | 423; median 0.12; central [0.00, 20.00]; speed [0.00, 26.67] | 0; No repeat: right-censored at 768 blocks |
| mountainous-r1-baseline / south-west / horse | 423; median 0.29; central [0.00, 56.57]; speed [0.00, 79.20] | 0; No repeat: right-censored at 768 blocks |
| mountainous-r1-baseline / south-west / walking | 423; median 0.50; central [0.00, 99.00]; speed [0.00, 132.00] | 0; No repeat: right-censored at 768 blocks |
| mountainous-r1-without-sparse / east-north / boat | 386; median 0.12; central [0.00, 32.00]; speed [0.00, 42.67] | 0; No repeat: right-censored at 768 blocks |
| mountainous-r1-without-sparse / east-north / horse | 386; median 0.30; central [0.00, 69.40]; speed [0.00, 97.17] | 0; No repeat: right-censored at 768 blocks |
| mountainous-r1-without-sparse / east-north / walking | 386; median 0.53; central [0.00, 121.46]; speed [0.00, 161.94] | 0; No repeat: right-censored at 768 blocks |
| mountainous-r1-without-sparse / east-south / boat | 456; median 0.12; central [0.00, 62.00]; speed [0.00, 82.67] | 0; No repeat: right-censored at 768 blocks |
| mountainous-r1-without-sparse / east-south / horse | 456; median 0.34; central [0.00, 170.55]; speed [0.00, 238.76] | 0; No repeat: right-censored at 768 blocks |
| mountainous-r1-without-sparse / east-south / walking | 456; median 0.60; central [0.00, 298.45]; speed [0.00, 397.94] | 0; No repeat: right-censored at 768 blocks |
| mountainous-r1-without-sparse / south-east / boat | 437; median 0.12; central [0.00, 20.00]; speed [0.00, 26.67] | 0; No repeat: right-censored at 768 blocks |
| mountainous-r1-without-sparse / south-east / horse | 437; median 0.29; central [0.00, 46.15]; speed [0.00, 64.62] | 0; No repeat: right-censored at 768 blocks |
| mountainous-r1-without-sparse / south-east / walking | 437; median 0.50; central [0.00, 80.77]; speed [0.00, 107.69] | 0; No repeat: right-censored at 768 blocks |
| mountainous-r1-without-sparse / south-west / boat | 417; median 0.12; central [0.00, 53.00]; speed [0.00, 70.67] | 1; median 37.00; central [37.00, 37.00]; speed [29.60, 49.33] |
| mountainous-r1-without-sparse / south-west / horse | 417; median 0.20; central [0.00, 118.59]; speed [0.00, 166.03] | 1; median 58.75; central [58.75, 58.75]; speed [45.69, 82.24] |
| mountainous-r1-without-sparse / south-west / walking | 417; median 0.35; central [0.00, 207.53]; speed [0.00, 276.71] | 1; median 102.81; central [102.81, 102.81]; speed [82.24, 137.07] |
| mountainous-r2-baseline / east-north / boat | 390; median 0.25; central [0.00, 48.00]; speed [0.00, 64.00] | 0; No repeat: right-censored at 768 blocks |
| mountainous-r2-baseline / east-north / horse | 390; median 0.33; central [0.00, 76.27]; speed [0.00, 106.77] | 0; No repeat: right-censored at 768 blocks |
| mountainous-r2-baseline / east-north / walking | 390; median 0.58; central [0.00, 133.47]; speed [0.00, 177.96] | 0; No repeat: right-censored at 768 blocks |
| mountainous-r2-baseline / east-south / boat | 411; median 0.12; central [0.00, 18.00]; speed [0.00, 24.00] | 0; No repeat: right-censored at 768 blocks |
| mountainous-r2-baseline / east-south / horse | 411; median 0.32; central [0.00, 94.41]; speed [0.00, 132.17] | 0; No repeat: right-censored at 768 blocks |
| mountainous-r2-baseline / east-south / walking | 411; median 0.56; central [0.00, 165.22]; speed [0.00, 220.29] | 0; No repeat: right-censored at 768 blocks |
| mountainous-r2-baseline / south-east / boat | 414; median 0.12; central [0.00, 26.00]; speed [0.00, 34.67] | 0; No repeat: right-censored at 768 blocks |
| mountainous-r2-baseline / south-east / horse | 414; median 0.32; central [0.00, 45.92]; speed [0.00, 64.28] | 0; No repeat: right-censored at 768 blocks |
| mountainous-r2-baseline / south-east / walking | 414; median 0.56; central [0.00, 80.35]; speed [0.00, 107.14] | 0; No repeat: right-censored at 768 blocks |
| mountainous-r2-baseline / south-west / boat | 417; median 0.12; central [0.00, 10.00]; speed [0.00, 13.33] | 0; No repeat: right-censored at 768 blocks |
| mountainous-r2-baseline / south-west / horse | 417; median 0.29; central [0.00, 35.92]; speed [0.00, 50.29] | 0; No repeat: right-censored at 768 blocks |
| mountainous-r2-baseline / south-west / walking | 417; median 0.50; central [0.00, 62.86]; speed [0.00, 83.81] | 0; No repeat: right-censored at 768 blocks |
| mountainous-r2-without-sparse / east-north / boat | 377; median 0.25; central [0.00, 30.00]; speed [0.00, 40.00] | 0; No repeat: right-censored at 768 blocks |
| mountainous-r2-without-sparse / east-north / horse | 377; median 0.29; central [0.00, 47.15]; speed [0.00, 66.01] | 0; No repeat: right-censored at 768 blocks |
| mountainous-r2-without-sparse / east-north / walking | 377; median 0.50; central [0.00, 82.51]; speed [0.00, 110.01] | 0; No repeat: right-censored at 768 blocks |
| mountainous-r2-without-sparse / east-south / boat | 476; median 0.12; central [0.00, 62.00]; speed [0.00, 82.67] | 0; No repeat: right-censored at 768 blocks |
| mountainous-r2-without-sparse / east-south / horse | 476; median 0.29; central [0.00, 161.43]; speed [0.00, 226.00] | 0; No repeat: right-censored at 768 blocks |
| mountainous-r2-without-sparse / east-south / walking | 476; median 0.50; central [0.00, 282.50]; speed [0.00, 376.66] | 0; No repeat: right-censored at 768 blocks |
| mountainous-r2-without-sparse / south-east / boat | 454; median 0.12; central [0.00, 16.00]; speed [0.00, 21.33] | 0; No repeat: right-censored at 768 blocks |
| mountainous-r2-without-sparse / south-east / horse | 454; median 0.32; central [0.00, 39.01]; speed [0.00, 54.61] | 0; No repeat: right-censored at 768 blocks |
| mountainous-r2-without-sparse / south-east / walking | 454; median 0.56; central [0.00, 68.26]; speed [0.00, 91.01] | 0; No repeat: right-censored at 768 blocks |
| mountainous-r2-without-sparse / south-west / boat | 431; median 0.12; central [0.00, 53.00]; speed [0.00, 70.67] | 2; median 36.00; central [35.00, 37.00]; speed [28.00, 49.33] |
| mountainous-r2-without-sparse / south-west / horse | 431; median 0.20; central [0.00, 135.66]; speed [0.00, 189.92] | 2; median 83.87; central [59.39, 108.36]; speed [46.19, 151.70] |
| mountainous-r2-without-sparse / south-west / walking | 431; median 0.35; central [0.00, 237.40]; speed [0.00, 316.54] | 2; median 146.78; central [103.94, 189.62]; speed [83.15, 252.83] |
| ocean-heavy-r1-baseline / east-north / boat | 93; median 0.75; central [0.00, 44.00]; speed [0.00, 58.67] | 0; No repeat: right-censored at 768 blocks |
| ocean-heavy-r1-baseline / east-north / horse | 93; median 0.86; central [0.00, 50.29]; speed [0.00, 70.40] | 0; No repeat: right-censored at 768 blocks |
| ocean-heavy-r1-baseline / east-north / walking | 93; median 1.50; central [0.00, 88.00]; speed [0.00, 117.33] | 0; No repeat: right-censored at 768 blocks |
| ocean-heavy-r1-baseline / east-south / boat | 92; median 0.25; central [0.00, 9.88]; speed [0.00, 13.17] | 0; No repeat: right-censored at 768 blocks |
| ocean-heavy-r1-baseline / east-south / horse | 92; median 0.29; central [0.00, 11.29]; speed [0.00, 15.80] | 0; No repeat: right-censored at 768 blocks |
| ocean-heavy-r1-baseline / east-south / walking | 92; median 0.50; central [0.00, 19.75]; speed [0.00, 26.33] | 0; No repeat: right-censored at 768 blocks |
| ocean-heavy-r1-baseline / south-east / boat | 167; median 0.25; central [0.00, 20.00]; speed [0.00, 26.67] | 0; No repeat: right-censored at 768 blocks |
| ocean-heavy-r1-baseline / south-east / horse | 167; median 0.29; central [0.00, 47.63]; speed [0.00, 66.68] | 0; No repeat: right-censored at 768 blocks |
| ocean-heavy-r1-baseline / south-east / walking | 167; median 0.50; central [0.00, 83.35]; speed [0.00, 111.14] | 0; No repeat: right-censored at 768 blocks |
| ocean-heavy-r1-baseline / south-west / boat | 53; median 1.00; central [0.00, 14.00]; speed [0.00, 18.67] | 0; No repeat: right-censored at 768 blocks |
| ocean-heavy-r1-baseline / south-west / horse | 53; median 1.14; central [0.00, 16.00]; speed [0.00, 22.40] | 0; No repeat: right-censored at 768 blocks |
| ocean-heavy-r1-baseline / south-west / walking | 53; median 2.00; central [0.00, 28.00]; speed [0.00, 37.33] | 0; No repeat: right-censored at 768 blocks |
| ocean-heavy-r1-without-sparse / east-north / boat | 90; median 0.81; central [0.00, 44.00]; speed [0.00, 58.67] | 0; No repeat: right-censored at 768 blocks |
| ocean-heavy-r1-without-sparse / east-north / horse | 90; median 1.07; central [0.00, 226.11]; speed [0.00, 316.56] | 0; No repeat: right-censored at 768 blocks |
| ocean-heavy-r1-without-sparse / east-north / walking | 90; median 1.88; central [0.00, 395.70]; speed [0.00, 527.59] | 0; No repeat: right-censored at 768 blocks |
| ocean-heavy-r1-without-sparse / east-south / boat | 122; median 0.25; central [0.00, 78.00]; speed [0.00, 104.00] | 0; No repeat: right-censored at 768 blocks |
| ocean-heavy-r1-without-sparse / east-south / horse | 122; median 0.29; central [0.00, 89.14]; speed [0.00, 124.80] | 0; No repeat: right-censored at 768 blocks |
| ocean-heavy-r1-without-sparse / east-south / walking | 122; median 0.50; central [0.00, 156.00]; speed [0.00, 208.00] | 0; No repeat: right-censored at 768 blocks |
| ocean-heavy-r1-without-sparse / south-east / boat | 153; median 0.25; central [0.00, 38.00]; speed [0.00, 50.67] | 0; No repeat: right-censored at 768 blocks |
| ocean-heavy-r1-without-sparse / south-east / horse | 153; median 0.29; central [0.00, 80.88]; speed [0.00, 113.23] | 0; No repeat: right-censored at 768 blocks |
| ocean-heavy-r1-without-sparse / south-east / walking | 153; median 0.50; central [0.00, 141.53]; speed [0.00, 188.71] | 0; No repeat: right-censored at 768 blocks |
| ocean-heavy-r1-without-sparse / south-west / boat | 72; median 0.62; central [0.00, 42.00]; speed [0.00, 56.00] | 0; No repeat: right-censored at 768 blocks |
| ocean-heavy-r1-without-sparse / south-west / horse | 72; median 0.71; central [0.00, 48.00]; speed [0.00, 67.20] | 0; No repeat: right-censored at 768 blocks |
| ocean-heavy-r1-without-sparse / south-west / walking | 72; median 1.25; central [0.00, 84.00]; speed [0.00, 112.00] | 0; No repeat: right-censored at 768 blocks |
| ocean-heavy-r2-baseline / east-north / boat | 97; median 0.75; central [0.00, 44.00]; speed [0.00, 58.67] | 0; No repeat: right-censored at 768 blocks |
| ocean-heavy-r2-baseline / east-north / horse | 97; median 0.86; central [0.00, 50.29]; speed [0.00, 70.40] | 0; No repeat: right-censored at 768 blocks |
| ocean-heavy-r2-baseline / east-north / walking | 97; median 1.50; central [0.00, 88.00]; speed [0.00, 117.33] | 0; No repeat: right-censored at 768 blocks |
| ocean-heavy-r2-baseline / east-south / boat | 125; median 0.25; central [0.00, 9.38]; speed [0.00, 12.50] | 0; No repeat: right-censored at 768 blocks |
| ocean-heavy-r2-baseline / east-south / horse | 125; median 0.29; central [0.00, 10.71]; speed [0.00, 15.00] | 0; No repeat: right-censored at 768 blocks |
| ocean-heavy-r2-baseline / east-south / walking | 125; median 0.50; central [0.00, 18.75]; speed [0.00, 25.00] | 0; No repeat: right-censored at 768 blocks |
| ocean-heavy-r2-baseline / south-east / boat | 163; median 0.25; central [0.00, 20.00]; speed [0.00, 26.67] | 0; No repeat: right-censored at 768 blocks |
| ocean-heavy-r2-baseline / south-east / horse | 163; median 0.29; central [0.00, 47.63]; speed [0.00, 66.68] | 0; No repeat: right-censored at 768 blocks |
| ocean-heavy-r2-baseline / south-east / walking | 163; median 0.50; central [0.00, 83.35]; speed [0.00, 111.14] | 0; No repeat: right-censored at 768 blocks |
| ocean-heavy-r2-baseline / south-west / boat | 55; median 0.75; central [0.00, 32.50]; speed [0.00, 43.33] | 0; No repeat: right-censored at 768 blocks |
| ocean-heavy-r2-baseline / south-west / horse | 55; median 0.86; central [0.00, 37.14]; speed [0.00, 52.00] | 0; No repeat: right-censored at 768 blocks |
| ocean-heavy-r2-baseline / south-west / walking | 55; median 1.50; central [0.00, 65.00]; speed [0.00, 86.67] | 0; No repeat: right-censored at 768 blocks |
| ocean-heavy-r2-without-sparse-attempt3 / east-north / boat | 103; median 0.62; central [0.00, 44.00]; speed [0.00, 58.67] | 0; No repeat: right-censored at 768 blocks |
| ocean-heavy-r2-without-sparse-attempt3 / east-north / horse | 103; median 0.92; central [0.00, 226.11]; speed [0.00, 316.56] | 0; No repeat: right-censored at 768 blocks |
| ocean-heavy-r2-without-sparse-attempt3 / east-north / walking | 103; median 1.60; central [0.00, 395.70]; speed [0.00, 527.59] | 0; No repeat: right-censored at 768 blocks |
| ocean-heavy-r2-without-sparse-attempt3 / east-south / boat | 106; median 0.38; central [0.00, 78.00]; speed [0.00, 104.00] | 0; No repeat: right-censored at 768 blocks |
| ocean-heavy-r2-without-sparse-attempt3 / east-south / horse | 106; median 0.43; central [0.00, 89.14]; speed [0.00, 124.80] | 0; No repeat: right-censored at 768 blocks |
| ocean-heavy-r2-without-sparse-attempt3 / east-south / walking | 106; median 0.75; central [0.00, 156.00]; speed [0.00, 208.00] | 0; No repeat: right-censored at 768 blocks |
| ocean-heavy-r2-without-sparse-attempt3 / south-east / boat | 160; median 0.25; central [0.00, 38.00]; speed [0.00, 50.67] | 0; No repeat: right-censored at 768 blocks |
| ocean-heavy-r2-without-sparse-attempt3 / south-east / horse | 160; median 0.29; central [0.00, 80.88]; speed [0.00, 113.23] | 0; No repeat: right-censored at 768 blocks |
| ocean-heavy-r2-without-sparse-attempt3 / south-east / walking | 160; median 0.50; central [0.00, 141.53]; speed [0.00, 188.71] | 0; No repeat: right-censored at 768 blocks |
| ocean-heavy-r2-without-sparse-attempt3 / south-west / boat | 63; median 1.25; central [0.00, 42.00]; speed [0.00, 56.00] | 0; No repeat: right-censored at 768 blocks |
| ocean-heavy-r2-without-sparse-attempt3 / south-west / horse | 63; median 1.43; central [0.00, 48.00]; speed [0.00, 67.20] | 0; No repeat: right-censored at 768 blocks |
| ocean-heavy-r2-without-sparse-attempt3 / south-west / walking | 63; median 2.50; central [0.00, 84.00]; speed [0.00, 112.00] | 0; No repeat: right-censored at 768 blocks |
| ordinary-r1-baseline / east-north / boat | 59; median 0.75; central [0.00, 18.00]; speed [0.00, 24.00] | 0; No repeat: right-censored at 768 blocks |
| ordinary-r1-baseline / east-north / horse | 59; median 0.86; central [0.00, 20.57]; speed [0.00, 28.80] | 0; No repeat: right-censored at 768 blocks |
| ordinary-r1-baseline / east-north / walking | 59; median 1.50; central [0.00, 36.00]; speed [0.00, 48.00] | 0; No repeat: right-censored at 768 blocks |
| ordinary-r1-baseline / east-south / boat | 78; median 0.38; central [0.00, 24.00]; speed [0.00, 32.00] | 0; No repeat: right-censored at 768 blocks |
| ordinary-r1-baseline / east-south / horse | 78; median 0.43; central [0.00, 27.43]; speed [0.00, 38.40] | 0; No repeat: right-censored at 768 blocks |
| ordinary-r1-baseline / east-south / walking | 78; median 0.75; central [0.00, 48.00]; speed [0.00, 64.00] | 0; No repeat: right-censored at 768 blocks |
| ordinary-r1-baseline / south-east / boat | 113; median 0.12; central [0.00, 32.00]; speed [0.00, 42.67] | 0; No repeat: right-censored at 768 blocks |
| ordinary-r1-baseline / south-east / horse | 113; median 0.14; central [0.00, 36.57]; speed [0.00, 51.20] | 0; No repeat: right-censored at 768 blocks |
| ordinary-r1-baseline / south-east / walking | 113; median 0.25; central [0.00, 64.00]; speed [0.00, 85.33] | 0; No repeat: right-censored at 768 blocks |
| ordinary-r1-baseline / south-west / boat | 55; median 0.62; central [0.00, 64.00]; speed [0.00, 85.33] | 0; No repeat: right-censored at 768 blocks |
| ordinary-r1-baseline / south-west / horse | 55; median 0.71; central [0.00, 73.14]; speed [0.00, 102.40] | 0; No repeat: right-censored at 768 blocks |
| ordinary-r1-baseline / south-west / walking | 55; median 1.25; central [0.00, 128.00]; speed [0.00, 170.67] | 0; No repeat: right-censored at 768 blocks |
| ordinary-r1-without-sparse / east-north / boat | 46; median 0.81; central [0.00, 18.00]; speed [0.00, 24.00] | 0; No repeat: right-censored at 768 blocks |
| ordinary-r1-without-sparse / east-north / horse | 46; median 0.93; central [0.00, 20.57]; speed [0.00, 28.80] | 0; No repeat: right-censored at 768 blocks |
| ordinary-r1-without-sparse / east-north / walking | 46; median 1.62; central [0.00, 36.00]; speed [0.00, 48.00] | 0; No repeat: right-censored at 768 blocks |
| ordinary-r1-without-sparse / east-south / boat | 96; median 0.38; central [0.00, 81.00]; speed [0.00, 108.00] | 0; No repeat: right-censored at 768 blocks |
| ordinary-r1-without-sparse / east-south / horse | 96; median 0.43; central [0.00, 92.57]; speed [0.00, 129.60] | 0; No repeat: right-censored at 768 blocks |
| ordinary-r1-without-sparse / east-south / walking | 96; median 0.75; central [0.00, 162.00]; speed [0.00, 216.00] | 0; No repeat: right-censored at 768 blocks |
| ordinary-r1-without-sparse / south-east / boat | 111; median 0.12; central [0.00, 92.00]; speed [0.00, 122.67] | 0; No repeat: right-censored at 768 blocks |
| ordinary-r1-without-sparse / south-east / horse | 111; median 0.14; central [0.00, 199.96]; speed [0.00, 279.94] | 0; No repeat: right-censored at 768 blocks |
| ordinary-r1-without-sparse / south-east / walking | 111; median 0.25; central [0.00, 349.92]; speed [0.00, 466.56] | 0; No repeat: right-censored at 768 blocks |
| ordinary-r1-without-sparse / south-west / boat | 46; median 1.19; central [0.00, 52.00]; speed [0.00, 69.33] | 0; No repeat: right-censored at 768 blocks |
| ordinary-r1-without-sparse / south-west / horse | 46; median 1.36; central [0.00, 59.43]; speed [0.00, 83.20] | 0; No repeat: right-censored at 768 blocks |
| ordinary-r1-without-sparse / south-west / walking | 46; median 2.38; central [0.00, 104.00]; speed [0.00, 138.67] | 0; No repeat: right-censored at 768 blocks |
| ordinary-r2-baseline / east-north / boat | 49; median 0.88; central [0.00, 48.50]; speed [0.00, 64.67] | 0; No repeat: right-censored at 768 blocks |
| ordinary-r2-baseline / east-north / horse | 49; median 1.00; central [0.00, 55.43]; speed [0.00, 77.60] | 0; No repeat: right-censored at 768 blocks |
| ordinary-r2-baseline / east-north / walking | 49; median 1.75; central [0.00, 97.00]; speed [0.00, 129.33] | 0; No repeat: right-censored at 768 blocks |
| ordinary-r2-baseline / east-south / boat | 79; median 0.50; central [0.00, 24.00]; speed [0.00, 32.00] | 0; No repeat: right-censored at 768 blocks |
| ordinary-r2-baseline / east-south / horse | 79; median 0.57; central [0.00, 27.43]; speed [0.00, 38.40] | 0; No repeat: right-censored at 768 blocks |
| ordinary-r2-baseline / east-south / walking | 79; median 1.00; central [0.00, 48.00]; speed [0.00, 64.00] | 0; No repeat: right-censored at 768 blocks |
| ordinary-r2-baseline / south-east / boat | 104; median 0.12; central [0.00, 32.00]; speed [0.00, 42.67] | 0; No repeat: right-censored at 768 blocks |
| ordinary-r2-baseline / south-east / horse | 104; median 0.14; central [0.00, 36.57]; speed [0.00, 51.20] | 0; No repeat: right-censored at 768 blocks |
| ordinary-r2-baseline / south-east / walking | 104; median 0.25; central [0.00, 64.00]; speed [0.00, 85.33] | 0; No repeat: right-censored at 768 blocks |
| ordinary-r2-baseline / south-west / boat | 51; median 1.00; central [0.00, 64.00]; speed [0.00, 85.33] | 0; No repeat: right-censored at 768 blocks |
| ordinary-r2-baseline / south-west / horse | 51; median 1.14; central [0.00, 73.14]; speed [0.00, 102.40] | 0; No repeat: right-censored at 768 blocks |
| ordinary-r2-baseline / south-west / walking | 51; median 2.00; central [0.00, 128.00]; speed [0.00, 170.67] | 0; No repeat: right-censored at 768 blocks |
| ordinary-r2-without-sparse / east-north / boat | 49; median 0.88; central [0.00, 18.00]; speed [0.00, 24.00] | 0; No repeat: right-censored at 768 blocks |
| ordinary-r2-without-sparse / east-north / horse | 49; median 1.00; central [0.00, 20.57]; speed [0.00, 28.80] | 0; No repeat: right-censored at 768 blocks |
| ordinary-r2-without-sparse / east-north / walking | 49; median 1.75; central [0.00, 36.00]; speed [0.00, 48.00] | 0; No repeat: right-censored at 768 blocks |
| ordinary-r2-without-sparse / east-south / boat | 100; median 0.31; central [0.00, 81.00]; speed [0.00, 108.00] | 0; No repeat: right-censored at 768 blocks |
| ordinary-r2-without-sparse / east-south / horse | 100; median 0.36; central [0.00, 92.57]; speed [0.00, 129.60] | 0; No repeat: right-censored at 768 blocks |
| ordinary-r2-without-sparse / east-south / walking | 100; median 0.62; central [0.00, 162.00]; speed [0.00, 216.00] | 0; No repeat: right-censored at 768 blocks |
| ordinary-r2-without-sparse / south-east / boat | 128; median 0.12; central [0.00, 92.00]; speed [0.00, 122.67] | 0; No repeat: right-censored at 768 blocks |
| ordinary-r2-without-sparse / south-east / horse | 128; median 0.14; central [0.00, 199.96]; speed [0.00, 279.94] | 0; No repeat: right-censored at 768 blocks |
| ordinary-r2-without-sparse / south-east / walking | 128; median 0.25; central [0.00, 349.92]; speed [0.00, 466.56] | 0; No repeat: right-censored at 768 blocks |
| ordinary-r2-without-sparse / south-west / boat | 66; median 0.75; central [0.00, 52.00]; speed [0.00, 69.33] | 0; No repeat: right-censored at 768 blocks |
| ordinary-r2-without-sparse / south-west / horse | 66; median 0.86; central [0.00, 59.43]; speed [0.00, 83.20] | 0; No repeat: right-censored at 768 blocks |
| ordinary-r2-without-sparse / south-west / walking | 66; median 1.50; central [0.00, 104.00]; speed [0.00, 138.67] | 0; No repeat: right-censored at 768 blocks |

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
