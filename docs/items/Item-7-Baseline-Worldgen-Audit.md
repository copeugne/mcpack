# Item 7 — Pristine Baseline Terrain and Worldgen Audit

**Status:** `COMPLETE` for the existing zero-mod baseline
**Method:** `terrain-control-v0.1`
**Decision:** retain as the control; no modded terrain/worldgen candidate is admitted by this item

## Scope

The current baseline contains Minecraft 1.21.1 and NeoForge 21.1.249 with zero third-party mods. Therefore Tectonic, Terralith, Biomes O' Plenty, Regions Unexplored, TerraBlender, Lithostitched, BetterEnd, YUNG, When Dungeons Arise, IDAS, Integrated structures, Moog, Explorify, Explorations, Repurposed Structures, CTOV and Towns & Towers are **absent**, not silently presumed compatible.

This item establishes the unmodified control those candidates must later beat. Any admitted worldgen candidate reopens the relevant Item 7 interaction tests on an isolated branch.

## Controlled method

For each of the four verified seeds:

1. Restore the hash-backed initial world and require exact archive/file-manifest verification.
2. Add only a temporary data-only probe function; retain zero third-party JARs.
3. Sample two intentionally different 5×5 patches at 32-block spacing.
4. Force-load one bounded rectangle per patch, never a growing set of sparse tickets.
5. Query exact biome and `motion_blocking_no_leaves` height at every point.
6. Remove the rectangle, flush-save and stop.
7. Repeat the complete 200-sample experiment from fresh snapshots.
8. Require exact equality of every raw record and derived statistic.

Macro biome-role evidence comes from the already-verified Item 4 `/locate biome` suite. The local probe deliberately concentrates on origins, jagged peaks, coasts/oceans and biome transitions; it is not an unbiased global biome-frequency survey.

## Results

Both final runs contain 50 samples/seed, two clean lifecycles/seed, exact restores and zero warning/error lines matching worldgen, structure, chunk, biome, feature, carver or noise. The repeat verifier passed every seed.

| Seed / patch | Biomes in 25 cells | Same-biome edge ratio | Singleton cells | Stable Y range | Adjacent ΔY p95 / max |
|---|---:|---:|---:|---:|---:|
| ordinary / origin | 2 | 0.875 | 0% | 63–75 | 8.05 / 11 |
| ordinary / jagged peaks | 2 | 0.900 | 4% | 80–160 | 33.15 / 37 |
| mountain / origin peaks | 3 | 0.700 | 8% | 181–252 | 31.20 / 42 |
| mountain / ocean transition | 4 | 0.625 | 0% | 63–104 | 34.35 / 41 |
| ocean / origin plains | 1 | 1.000 | 0% | 64–82 | 9.15 / 14 |
| ocean / deep ocean | 4 | 0.725 | 4% | 63–63 | 0 / 0 |
| diverse / desert transition | 3 | 0.700 | 8% | 63–101 | 26.15 / 36 |
| diverse / deep ocean | 4 | 0.725 | 4% | 63–63 | 0 / 0 |

The high mountain deltas are expected control characteristics and a later gameplay/vehicle-design input, not evidence of a broken transition. Boundary-focused patches show at most 8% singleton cells; this does not support a claim of pervasive tiny-biome fragmentation. It also cannot prove the opposite globally, so candidate comparisons must use the same method plus wider sampling.

## Requested defect classifications

| Class | Baseline finding |
|---|---|
| Fragmented/tiny biomes | No local red flag in the deliberately difficult patches; no global conclusion from 200 boundary-focused samples |
| Unnatural terrain transitions | No numeric discontinuity beyond expected mountain/coastal controls; visual aesthetic judgment remains a candidate comparison task |
| Buried/floating/cliff-intersecting structures | Not applicable: none of the named structure mods is installed; vanilla families are inventoried in Item 8 |
| Bad underwater placement | No modded structures exist; deep-ocean surface controls are stable at Y=63 |
| Overlap/failed placement/impossible restrictions | No modded structure stack exists; zero relevant warning/error lines |
| Excessive terrain modification around structures | Not applicable until a structure candidate is installed |
| Cosmetic issues | Server-only numeric control cannot ratify aesthetics; later visual QA is mandatory per candidate |
| Gameplay issues | Steep mountain/control transitions are flagged for walking, vehicle and discoverability testing, not rejected |
| Performance issues | Formal Item 17 measurement still required; see harness-failure lesson below |
| Outright generation failure | None in either final run |

## Harness failures and correction

The audit deliberately retains its failed methods:

- a direct invocation permission error before Minecraft launch;
- an exact console-response parser mismatch;
- sparse discontiguous force-loads accumulated roughly 3,800 resident chunks and triggered the default 60-second watchdog;
- repeated sparse-probe batching produced an unreliable console stream.

The accepted method does **not** disable the watchdog. It uses bounded rectangular tickets, removes them, and restarts per patch. Minecraft's own current and rotated debug logs—not the intermittently incomplete parent-console mirror—are authoritative lifecycle evidence. The sparse-probe crash is a test-harness artifact, not representative gameplay performance, but it proves later worldgen tools must bound tickets/backlog and remain under watchdog policy.

## Evidence

- `test-environment/terrain-sampling-v0.1.json`
- `tools/sample_vanilla_terrain.py`
- `evidence/worldgen/item7-terrain-control-r7.json`
- `evidence/worldgen/item7-terrain-control-r8.json`
- `evidence/worldgen/item7-terrain-repeat-verification.json`
- `evidence/worldgen/harness-failures/`

## Exit decision

The existing terrain/worldgen baseline is reproducibly characterized and issue types are separated without inventing mod interactions. Item 8 may inventory the structures actually present in this zero-mod control. Every later admitted terrain, biome, dimension or structure mod must repeat the relevant Item 7 probes and add visual placement inspection before retention.

