# Item 11 automated route protocol

Status: PREDECLARED before corrected visibility extraction. Identifier: `item11-routes-v2`.
Revision 2 fixes review finding 3962853986: target eligibility must be independent
of anchor adjacency. Version 1 remains preserved at reviewed commit `506bc4fd`.
Routes, seeds, worlds, radii, windows, targets, ray and transport models are unchanged.
Authority: SPECS.md Item 11 and [the scope amendment](../item-10/methodology-amendment.md).
This is descriptive automated analysis, not a human study or a tuning experiment.

## Inputs and sample

Use the sixteen accepted names and census SHA-256 values in
[accepted-biome-comparisons.json.gz](../item-10/accepted-biome-comparisons.json.gz).
Use their unchanged Item 10 archive manifests, world-backup manifests and existing
hash-verified world restores. Verify the archive binding of each backup manifest,
the complete restored file inventory and consumed census bytes before analysis.
Hold the existing Java-compatible POSIX world lock during reading and recheck
consumed region/external files before publication. No server starts, configuration
changes, new worlds, rejected-world repairs or new archive revision are needed.

Use only the Overworld census rectangle, inclusive chunks [-32,31] on both axes.
The accepted Item 10 report remains authority for other dimensions and placement
density. Surface transport in other dimensions is outside this route estimand.
Four deliberately selected seeds, two saved-world repetitions and both arms give
16 world observations. Modes and overlapping routes are not independent worlds.
The two rejected Item 10 attempts remain excluded inputs with their original
failure dispositions linked; no route or zero can be inferred for those worlds.

Four fixed oriented straight transects per world, independent of placements:

| Route | Start X,Z | End X,Z | Horizontal length |
| --- | --- | --- | --- |
| east-south | -384,-256 | 384,-256 | 768 blocks |
| east-north | -384,256 | 384,256 | 768 blocks |
| south-west | -256,-384 | -256,384 | 768 blocks |
| south-east | 256,-384 | 256,384 | 768 blocks |

This gives 64 geometric routes and 192 route/mode evaluations. Analyze fixed
prefix windows [0,256], [0,512], [0,768]. Do not move endpoints, reroute toward
locations or extend a route to obtain a rare category. Sample visibility at the
96 eight-block segment midpoints (distances 4,12,...,764); transport geometry at
all 769 integer-distance stations and their adjacent cells. All radius-96 disks
are contained in the selected saved region. No additional generation is needed.

## Candidate and visibility definitions

Reuse accepted `classification.occurrences`, including canonical family, role,
confidence, ambiguity and comparison groups. Do not recount aliases or pieces.
Registry inclusion anchors remain start-chunk centers. Join their saved piece
bounds from `occurrence_biomes`; a geometric target is the top of the envelope
at its horizontal center, one block above its inclusive maximum Y. Nonregistry
targets use their observed X,Y,Z anchors, one block above Y. Missing bounds or Y
produce UNKNOWN visibility, never an inferred visible point.

Primary adjacency uses the accepted inclusion anchor's Euclidean distance to the
finite horizontal transect, at most 64 blocks. Preserve the target separately:
an anchor near the route does not imply the whole structure is near it. Report
32 and 96 block sensitivity alongside the primary 64. Each location counts once
per route/window; cross-route duplicates remain possible and are not world totals.
For adjacency windows only, require nearest anchor projection in [0,window), except the final
768 endpoint is included. Preserve route-end censoring. Visibility membership
instead requires a ray-eligible target at a sampled station within the window,
independently of anchor distance or anchor projection. Retain targets whose
anchors are beyond the largest adjacency radius; never prefilter them by anchor.
The population remains accepted Item 10 census locations. Targets of starts
outside that census and missing target geometry cannot establish visibility absence.

At each midpoint, test candidate geometric targets within the same radius.
Eye point is the saved WORLD_SURFACE height plus 2.62 blocks (standing feet one
block above the top stored block, plus assumed 1.62 eye height). This height is
shared across modes to isolate transport assumptions from visibility geometry.
Test the straight eye-to-target ray at horizontal increments no larger than one
block, using floor X,Z cells and WORLD_SURFACE as a conservative opaque height
field. A ray sample at or below the stored top block plus one is occluded. Include
the target cell and exclude the eye endpoint. Missing height data gives UNKNOWN.
No lighting, fog, facing direction, texture, transparency, silhouette size,
entrances or human recognition is modeled. Trees can occlude, and a canopy eye
point can overstate access. Envelope-top points are geometric proxies, not
verified visible authored blocks. Underground anchors normally remain occluded;
a surface height field cannot model caves, tunnels or interiors.

Report adjacency independently from ray-clear opportunity counts, with UNKNOWN
counts. Coverage numerator is the number of sampled eight-block segments with
at least one ray-clear target, times eight; denominator is the full window length.
Report all locations and separately actionable C/T1/T2/T3/T4, encounter T1/T2/T3/T4,
exclusive T2, exclusive T3, T4 and village comparison-group membership. This is a
sampled geometric route fraction, not continuous visible distance or Activity Ratio.

## Transport and cost assumptions

These are deliberately simple capability scenarios, not measured vanilla speeds
or a collision/pathfinding simulation. All start at the declared endpoint. No
teleporting, portals, block edits, consumables, detours, dismounting, swimming or
mode substitution. Walking and horse follow the height-field top surface, permit
at most one block rise/fall per horizontal step, and require a non-air, non-water, non-lava top block as a dry-support proxy. Boat
requires water at the top surface, at least one block of water depth and a level
3 by 3 water neighborhood at each station; steps must remain at equal water level.
Read actual saved top block IDs to distinguish water from lava or vegetation;
WORLD_SURFACE minus OCEAN_FLOOR alone is not proof of water. Absent block sections remain UNKNOWN rather than traversable. Clearance above
the WORLD_SURFACE top is inferred from the height field, not collision-tested. These are height-field corridor
proxies and can be overly restrictive around cliffs/canopies or overly permissive
about block collision shapes. Boat width is a conservative three-cell scenario.

Record every failed station/step and its reason. A known blocked endpoint or step
makes the modeled route INFEASIBLE; incomplete geometry without a known obstacle
makes it UNKNOWN; otherwise MODEL_FEASIBLE. Retain reachable prefix length and
modeled opportunity coverage within that prefix, separately from full geometric
coverage. Never silently switch mode or discard infeasible rows.

Dry-mode cost is sum of sqrt(1 + height_delta squared) divided by assumed speed;
boat cost uses horizontal length. Central assumed speeds: walking 4, horse 7,
boat 8 blocks/second; sensitivity ranges respectively [3,5], [5,9], [6,10].
These user-independent declared model parameters are not measured mount attributes.
Report completed-route modeled time only if MODEL_FEASIBLE; otherwise null with
explicit reason. Report reachable-prefix costs and purely geometric unconstrained
costs separately. No setup, feeding, combat, looting or fatigue time is included.

## Gaps, repetition and uncertainty

Order adjacent candidates by projected route distance, tie-breaking by canonical
family then stable location identity. Keep same-position ties, including zero gaps.
For each category and fixed window retain successive gaps, first/last boundary
gaps as censored, maximum empty interval, unique families, repeat count and first
repeat distance. Repetition means the same accepted canonical family, not a claim
of identical generated layout. Also compute first-ray-clear events in station
order for the geometric visibility population, preserving ties and UNKNOWNs.
Repeat intervals run from the preceding event of the same family; report their
distance and model-speed time ranges. If the relevant prefix is infeasible,
interval times remain unconstrained model values, not reachable travel times.
No observed repeat means right-censored at the window end, not infinite variety.

Retain raw candidate joins, station heights/block states, ray outcomes, failures,
category membership, event distances and denominators. Report counts, median,
IQR/range and maxima where defined; show each seed/arm/repetition separately and
paired contrasts without random-population confidence intervals. Radius and speed
sensitivity quantify model dependence; route overlap, only two repetitions,
nonrandom seeds, finite windows and provisional classification constrain inference.
No numeric gameplay quality threshold is invented; this gate requires complete,
reproducible measurement and honest uncertainty, not a desirable pacing result.

Human recognition, actual fights, meaningful-interaction time, enjoyment and human
Adventure Activity Ratio are **NOT MEASURED**. Do not start Item 12.

## Small complete increment and resource budget

The original representative was ordinary repetition 1 baseline. For the version 2
correction, first complete biome-diverse repetition 1 without-Sparse (the actual
review counterexample) end to end: verified inputs, all
four routes, all modes/windows/radii, raw outputs, summary and focused validation.
Review its denominators and actual processing/storage cost before expanding to
the other fifteen worlds. This repeats derived read-only processing to repair
the demonstrated omission, not world generation or upstream measurement. Preserve failed processing attempts with diagnostics; fix
analysis defects without changing raw worlds or adapting the sampling frame.

Measured input availability: all sixteen census hashes pass; 1,784,216,273 bytes,
verified in 1.968 seconds. Existing restored worlds total 6,806,284,224 manifest
bytes, maximum 446,862,457 per world. Disk inspection found 45,849,010,176 free
bytes. These are input costs, not a new processing benchmark. Sequential processing
reuses restores; no second complete world set is required. Plan a 2 GiB memory
budget and 1 GiB new output budget, retaining a 5 GiB free-space floor. The prior
477.603-second complete-census reproduction gives a conservative provisional
16 x 10 minute processing allowance; route runtime is UNKNOWN until the pilot.
Stop to reassess if the pilot projects beyond these budgets. Do not add a new
storage service or evidence framework merely to perform this read-only analysis.
