# Small-dungeon representative

Status: representative analysis PASS under the separate Item 13 inspection/model
scope. This is two samples of one of 192 included families, not Item 13 completion.
It validates the compact-chamber measurement path before larger designs. The full
material-variant sampling matrix remains unfinished.

## Inputs, method and denominators

The [predeclared representative protocol](../protocol.md#frozen-representative-declaration-small-dungeon)
selected two of six eligible natural baseline occurrences from distinct seed roles without looking
at their contents. [Raw observations](observations.json.gz) retain source start NBT,
every block in the envelope plus a three-block border, block entities, surface
heights and world/census/protocol/producer identities. SHA-256:
`15860fb3692153b2bc6ac96cc0611655d498a7a976cfa5b953f424942712686e`.
The full restored inventory passed before and after extraction under the existing
Java-compatible world lock. No server launched and neither world was modified.

[Exact block plans](block-plans.svg) were visually inspected by the agent, including
floor, feet, head, upper and centre section. [Manual coding](coding.json) defines
one unpartitioned room per case, the staged entry and route assumptions before
calculation. Source shell/pile counts did not determine rooms. The floor is flat,
corner furnishings do not divide activity spaces, and ceiling decorations do not
create reachable upper floors. All supported standing cells inside each declared
interior connect to the entry: 51/51 ocean, 33/33 mountainous. Restricted standing
cells are a conservative navigation substrate, not another room denominator.

[Deterministic results](results.json) retain every target, path and return path.
The actor knows the layout, visits the spawner first, then sorted reward nodes,
and returns. Target visits require a clear geometric ray within three blocks.
They do not establish usable chest lids, opening, looting or spawner destruction.
Survey time excludes all approach, breaching, drainage, interactions and combat.
Combat is the separate [nominal source-supported workload](../model-source/README.md).
Do not sum these into a claimed observed clear time.

## Results against every quality requirement

| Requirement | Ocean-heavy baseline r1, start chunk (27,0) | Mountainous baseline r1, start chunk (5,0) |
| --- | --- | --- |
| Family and material design | `betterdungeons:small_dungeon`, 9x7 shell, skeleton theme, rotation 180 degrees | Same family, 9x5 shell, spider theme, no rotation |
| Rooms and branching | 1 reachable room R1, 0 inter-room edges, 0 junctions, 0 cycles | Same |
| Vertical progression | 0 required ascent/descent; one accessible floor at Y20 | 0 required ascent/descent; one accessible floor at Y41 |
| Playable depth | Deepest room graph depth 0 edges. Shortest entry-to-spawner interaction path 3 blocks | Same |
| Burial context | Saved surface top minus envelope top: 36 blocks | 159 to 164 blocks |
| Conditional traversal | 22-block closed survey; 5.5 seconds at 4 blocks/second; 4.4 to 7.33 seconds at 5 and 3 | Same |
| Authored enemy potential | One saved skeleton spawner, one configured enemy type; one-wave successful-count scenarios 0 to 4 | One saved spider spawner, one configured enemy type; one-wave scenarios 0 to 4 |
| Conditional combat workload | 0 to 10.4 active-attack seconds; 0 to 20.8 at 50% contact duty | 0 to 7.8 active-attack seconds; 0 to 15.6 at 50% contact duty |
| Spawner scheduling | Saved initial delay 20 ticks; repeated activation possible; real clear time UNKNOWN | Same |
| Meaningful hazards | Conditional central encounter source. Water immediately outside the west wall can flood a breach. No interior lava/damaging floor/trap circuit observed | Conditional central encounter source; outside west water and southeast cave-edge drop affect possible approach. Nearby sculk/veins do not prove a triggered encounter |
| Chokepoints | 0 internal authored connections between rooms. Proposed access requires a two-block-tall side breach | 0 internal authored connections. Existing southeast opening reaches a local narrow rim; whole-cave safe access not established |
| Empty/dead rooms | 0/1 empty, 0/1 dead: R1 contains encounter/reward potential | Same |
| Reward distribution | 5 chests with `minecraft:chests/simple_dungeon`, 3 barrels with `betterdungeons:small_dungeon/chests/loot_piles`; 8/8 in R1 | 6 chests with `minecraft:chests/simple_dungeon`; 6/6 in R1. Saved furnace is empty |
| Final room | NONE. No distinct terminal encounter or reward space | Same |
| External access/bypass | A side-wall breach can reach perimeter reward positions without passing the central spawner; water makes the dry route conditional | Existing southeast opening reaches perimeter rewards without first crossing the central spawner position |
| Visually large but shallow | Not a giant-form case: compact 11x7x9 saved shell envelope and one activity room | Not a giant-form case: compact 11x7x7 saved shell envelope and one activity room |

Burial figures are height differences, not counts of solid blocks that must be
mined: water and caves can intervene. External terrain outside the retained border
is not reconstructed. Bypasses avoid the central position, not necessarily enemy
activation or damage; each chamber is within the saved spawner activation range.
Ordinary mining capability is allowed, but no mining speed, drainage cost, safe
extraction or live bypass success is claimed. No route protection is proposed.

Finale dimensions are explicit: separate goal clarity ABSENT, distinctive final
challenge ABSENT, terminal reward linkage ABSENT, inter-room route integration
ABSENT. External reward exposure CONDITIONAL on approach and live encounter state.
The central spawner and perimeter rewards do supply a legible compact encounter
loop. Absence of a separate finale is descriptive, not a claim that a T1 room
should become a large progression dungeon.

## Variation, replay and limits

The existing [Item 8 generator evidence](../../item-8/sources/dungeons-provider/README.md)
identifies six shell-size alternatives and three enemy processor themes (skeleton,
spider, zombie), plus loot-pile variation. The two samples cover two shell sizes
and two themes, not all alternatives or all combinations. Source weights are not
measured occurrence frequencies. Each sample retains one configured enemy type;
three family-level alternatives are not three simultaneous encounter types.

Expected replay value is limited for route discovery in these two flat chambers:
the same single-room loop persists despite different sizes, props and enemy types.
Generator variation can change encounter inputs in another dungeon. Revisiting a
persistent saved chamber does not reroll its layout. The saved active spawner can
support further encounters subject to its conditions; repeated loot availability,
actual respawn populations and player motivation were not tested. This assessment
is supported by architecture and source alternatives, not invented player outcomes.

Human traversal/combat times, realized enemies/encounters, generated loot contents,
acquired items and enjoyment are NOT MEASURED. Stored LootTable/LootTableSeed fields
are unresolved loot potential. Nominal generator chest limits alone are insufficient
to count all final containers, as the observed five-plus-three and six demonstrate;
Item 8 already distinguishes those limits from final loot-pile outcomes.

No population confidence interval follows from two purposively separated seed roles.
The timing sensitivity range is chosen input variation, not a prediction interval.
No conclusion about all remaining small-dungeon variants or larger dungeons is
accepted from this pilot. Their material-variant coverage remains required.

## Reproduction and checks

From repository root, with existing accepted restores:

```sh
uv run --no-sync python -m evidence.item-13.measure --output /tmp/item13-pilot-reproduction.json.gz
cmp evidence/item-13/pilot/observations.json.gz /tmp/item13-pilot-reproduction.json.gz
uv run --no-sync python evidence/item-13/render_pilot.py
uv run --no-sync python evidence/item-13/analyze_pilot.py
uv run pytest -q evidence/item-13/test_pilot.py
```

The output path must be absent. Model-source reproduction is documented separately.
Extraction took 59.627 seconds for 6,188 voxels and 4,551 compressed bytes, below the
declared 600-second and 1-MiB limits. The retained [extraction output](extraction.txt)
is operational timing evidence; timing is excluded from deterministic raw bytes.
Focused tests exercise disconnected navigation, invalid entry, blocked/out-of-range
interaction rays and conservative corner occlusion. Exact block plans were rendered
and visually checked; orange envelope boundaries and both sample rows are visible.
Initial lint/type issues were corrected. An optional `/usr/bin/time` invocation
failed because that utility is unavailable; it did not execute the producer or
change evidence. Memory measurement uses Python's existing resource module instead.

A [second extraction](reproduction.txt) reproduced the exact compressed bytes in
54.701 seconds. Peak process RSS was 714,504 KiB, below the declared 2-GiB budget.
This is a reproduction check of new logic, not a new world or independent sample.
