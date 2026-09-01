# Item 11 — Baseline Exploration Pacing and Repetition Runbook

**Status:** `PREPARED — DEPENDENCY/HUMAN OBSERVATION GATE OPEN`
**Protocol:** `exploration-pacing-v0.1`
**Baseline:** Minecraft 1.21.1, NeoForge 21.1.249, zero gameplay mods
**Prerequisite:** accepted Item 10 density evidence for the same four seeds

## Purpose

Item 11 measures what a player actually experiences while traveling. It is not a second structure-counting exercise. A structure can exist without being seen, be seen without offering gameplay, or offer gameplay without interrupting enough dead travel. The controlled runs therefore preserve player video, movement, event timestamps, and post-run structure-family review.

The Item 10 offline inventory remains hidden from operators. After each run, a reviewer may compare the traveled corridor with that inventory to separate low generation density from low discoverability. That comparison does not rewrite the operator's observations.

## Bound Decisions

| Decision | Value | Rationale |
|---|---|---|
| Trial endpoints | Separate 60-minute and 10,000-horizontal-block trials | Measures both experience per hour and content per distance without conflating transport speed with density. |
| Replication | 3 valid runs per applicable seed × mode × endpoint cell | Matches the binding Item 5 human-gameplay replication rule. |
| Operators | At least 2; each operator tests every mode | Reduces one observer's play style becoming the result. |
| Route bearings | Time: 0°, 120°, 240°; distance: 60°, 180°, 300° | Predeclared coverage prevents selecting attractive routes after seeing the world. |
| World reuse | Never; restore a pristine seed snapshot for every run | Prevents depleted loot, altered terrain, or operator memory from contaminating a replicate. |
| Horse | Fixed, recorded attributes | Random horse quality is not allowed to become the independent variable. |
| Boat | Natural water only; no ice road | Preserves the intended ordinary boat role. |
| Boat infeasibility | Explicit `not-applicable`; no scenic-route substitution | Avoids cherry-picking only navigable or content-rich coastlines. |
| Visibility judgment | Human, blind during run | Offline structure positions cannot substitute for actual visual discovery. |
| Classification | Post-run using the Item 9 inventory | Keeps the player blind while applying consistent family/tier labels. |
| Activity time | Union of timestamped meaningful intervals | Prevents overlapping combat/loot/traversal labels from double-counting time. |
| Outliers | Retain and explain | Terrain, death, and unusual encounters are part of expedition behavior unless the protocol was violated. |

## Test Matrix

The full applicable matrix contains:

- 4 deterministic seeds;
- 3 transport modes: foot, standardized horse, and vanilla boat;
- 2 endpoint types: fixed time and fixed distance;
- 3 replicates per cell.

The maximum is 72 valid human runs. A boat cell can be replaced only by an explicit reviewed `not-applicable` record when its assigned route lacks a continuous natural navigable-water corridor. Foot and horse cells cannot be waived for ordinary terrain difficulty.

## Operator Isolation

Before a run, the operator must not know structure coordinates, biome-map results beyond the seed's declared role, or prior observations on that route. The operator may know:

- the transport mode;
- the endpoint rule;
- the assigned bearing;
- controls and recording procedure;
- ordinary Minecraft mechanics.

The operator must not use `/locate`, spectator mode, free camera, seed-map websites, debug structure displays, or the Item 10 evidence. An operator cannot repeat a route already seen, even if the earlier run was performed with another transport mode.

## Run Preparation

1. Initialize a draft manifest with `tools/create_exploration_run.py`; it refuses to overwrite an existing run and derives the assigned bearing from the protocol.
2. Record the current Git commit and confirm a clean working tree for the tested configuration.
3. Restore the selected seed's pristine snapshot into a unique run directory.
4. Verify the restore receipt and world seed.
5. Confirm Normal difficulty, Survival mode, no speed effects, and no gameplay mods.
6. Start server logging and client video before joining.
7. Start the five-second position trace before the expedition clock.
8. For horse trials, create the standardized horse, record its movement, jump, and health attributes, and supply one saddle.
9. For boat trials, supply one oak boat. Record shoreline-access time separately; the measured boating clock starts only at the blindly reached navigable shoreline.
10. Record the assigned bearing and replicate number. Do not preview the route.

## During the Run

The operator follows the assigned bearing within ±45°. Terrain, combat, and discovered content may cause detours; after the interaction, the operator resumes the bearing. Ordinary route finding is part of exploration and is not paused.

Timestamp these events at their first qualifying moment:

- visual discovery;
- actionable discovery;
- hostile encounter episode;
- proper-dungeon discovery;
- major-structure discovery;
- village discovery.

Record meaningful-activity intervals. Routine forward travel and routine eating are dead travel. Approaching, inspecting, interacting, fighting, traversing, looting, recovering, or making a consequential route decision because of current conditions is meaningful activity. Multiple simultaneous meanings form one interval in the Activity Ratio.

Pause only for a client/server fault, measurement correction, or real-world interruption, and record both pause boundaries. Teleportation, admin structure knowledge, route reuse, creative/spectator travel, or an unrecorded pause invalidates the run.

## Endpoints

- A fixed-time run ends at 3,600 seconds of valid expedition time. Pauses and boat shoreline access do not count.
- A fixed-distance run ends at 10,000 horizontal path blocks. Vertical movement does not inflate the distance.
- A death does not automatically invalidate the run. Recovery time remains part of the expedition when gameplay continues normally; an admin recovery invalidates it.
- Reaching the endpoint inside an interaction does not erase that interaction. Finish recording the active event, preserve its beyond-end tail separately, and cap Activity Ratio arithmetic at the endpoint.

## Blind Review

After the run, a reviewer who has the Item 9 inventory and Item 10 evidence:

1. watches the complete video;
2. verifies each observation timestamp;
3. assigns exact structure IDs and primary structure families where determinable;
4. confirms repeated-family events;
5. verifies meaningful-activity interval boundaries;
6. hashes all required artifacts;
7. checks the route trace, endpoint, and bearing tolerance;
8. marks the run valid, invalidated, or not-applicable with reasons.

The reviewer must not add a visual discovery that the operator did not recognize. Such a structure belongs only in the generated-but-unnoticed comparison.

## Required Artifacts Per Valid Run

- complete client video;
- five-second position trace;
- event log;
- dedicated server log;
- post-run world archive;
- run manifest conforming to `measurement/exploration-run.schema.json` (the analyzer records its hash as an input).

The five external artifacts are identified by SHA-256, and the analyzer independently hashes the manifest itself. A valid run with a missing or mismatched artifact is rejected.

## Automated Analysis

Run:

```bash
python3 tools/analyze_exploration_pacing.py \
  --protocol measurement/exploration-pacing-v0.1.json \
  --seed-suite test-environment/seed-suite.json \
  --runs evidence/exploration-pacing/runs \
  --output evidence/exploration-pacing/item11-analysis.json
```

The analyzer checks seed identity, endpoints, bearings, standardized mount evidence, review gates, artifacts, interval bounds, duplicate run IDs, cell coverage, and operator count. It calculates:

- discoveries and encounters per hour and per 1,000 path blocks;
- Adventure Activity Ratio and dead-travel percentage;
- unique structure families per hour;
- time to first repeated family;
- repeats per 10,000 path blocks;
- median, range, and interquartile range for every cell.

## Current Gate

The protocol, schema, and analyzer are ready. Item 11 cannot honestly be marked `MEASURED` or `COMPLETE` without real client observation by at least two operators and retained videos. Headless generation can prepare worlds and ground truth, but it cannot decide when a human notices a silhouette, regards a location as actionable, or experiences travel as meaningful.

No question is currently required from the absent owner. This gate is logged and kept on the back burner while all non-human preparation proceeds.

