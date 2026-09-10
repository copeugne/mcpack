# Small-dungeon representative

Status: local inspection/model analysis and complete conditional task timing
recorded under protocol v2. Historical survey and combat components remain valid
within their original scope. This is two samples
of one of 192 included families, not Item 13 completion.
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
git show 6ba360fa:evidence/item-13/measure.py > /tmp/item13-original-measure.py
PYTHONPATH=. uv run --no-sync python /tmp/item13-original-measure.py --output /tmp/item13-pilot-reproduction.json.gz
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

## Complete conditional tasks under protocol v2

This section supersedes the earlier timing gap for these two local tasks. It
reuses the immutable observations, coding and 22-block routes without regenerating
worlds or reprocessing routes. Direct inspection resolves the missing container
opening check: all eleven chests are saved single, non-waterlogged chests with
cave air immediately above; all fourteen containers have no Lock or Items field.
The three other containers are barrels. The earlier target-center rays enter
inside the ordinary chest shape, so the inset chest face does not introduce an
unexamined neighboring block. With no blocking entities, the existing pinned
chest/barrel use rules support opening at the retained stations. This is conditional
source/geometry access, not generated contents or observed transfer.

Predeclare each complete objective from its existing staged interior boundary:
ocean (428.5,21,-1.5), mountainous (84.5,42,2.5). Disable the central source,
defeat its stipulated successful hostiles, transfer available contents from every
listed container, and return alive to that same station. These boundaries use
integer route cells plus 0.5 in X/Z, without adding 0.5 to feet Y. Outside cave
travel, discovering the structure and preparing ingress remain excluded from
this local objective. In particular, the ocean dry starting state presupposes
controlled ingress; this model does not price excavation, drainage or establish
a dry wall breach. The original water/cave-edge access limitations remain.

Use the accepted adult, full-health/food, unenchanted iron armor/sword and diamond
pickaxe actor, fully informed, dry and grounded, with sufficient durability and
inventory capacity, 20 TPS, no effects, critical/sweep attacks, healing, building
or assistance. Stipulate no initial or natural enemies, preserving source Delay20,
SpawnCount4 and MinSpawnDelay200. Take the recorded source-first path, mine the
source from its checked station, clear combat and return to that station, then
follow the existing sorted-container route and return path. Combat duty includes
pursuit/return and is not charged again as survey movement. Inventory overflow,
new water flow into the route or any excluded encounter invalidates completion.

The source approach is three upright blocks in either case. With speed u,
decision n, interaction a and selection s, ocean disablement is
3/u+0.95+3n+a+s, charging orientation, the approach turn and source ordering.
Mountainous uses 2n because its straight prefix has no turn. The source break
is the pinned diamond-pick 19-tick calculation. A/B/C give ocean
3.55/5.70/8.45 seconds and mountainous 3.05/4.70/6.95 seconds. These are all
strictly below (20+200)/20=11 seconds. At most one successful batch of up to four
is possible under this countdown schedule. Failed spawn attempts remain possible;
zero to four successful ordinary unarmored entities is the conditional population
grid, not an observed count. If disablement misses that deadline, censor this grid
instead of carrying its four-enemy ceiling into a later schedule.

| Complete-task component | Ocean | Mountainous |
| --- | ---: | ---: |
| Upright travel blocks | 22 | 22 |
| Decisions | 19 | 18 |
| Target/menu interactions | 233 | 175 |
| Tool selections | 2 | 2 |
| Acquisition confirmations | 8 | 6 |
| Source breaking seconds | 0.95 | 0.95 |
| Active combat work per stipulated enemy | 2.6 seconds, skeleton | 1.95 seconds, spider |

Decision counts are actual centerline direction changes (7 ocean, 8 mountainous),
plus initial orientation, source ordering, combat transition, one planning event
per container, and final return choice. A 180-degree reversal counts as a direction
change. Menu inputs are 29 per container (open, 27 conditional transfer attempts,
close), plus one source-mining target. Pickaxe then sword are the two selections;
no later resource mining requires another selection. Inventory confirmation is
separate from the menu-input allowance. One final verification allowance is added.
All counts use the accepted A/B/C event allowances, with no new timing constants.

| Conditional seconds | A | B | C |
| --- | ---: | ---: | ---: |
| Ocean noncombat task | 83.600000 | 162.950000 | 311.783333 |
| Ocean, two successful skeletons | 88.800000 | 169.883333 | 322.183333 |
| Mountainous noncombat task | 66.600000 | 128.950000 | 244.283333 |
| Mountainous, two successful spiders | 70.500000 | 134.150000 | 252.083333 |

Keep the composition visible. For other counts m=0..4, add 2.6m/duty or
1.95m/duty to the relevant noncombat task. These sensitivity results are not
probability intervals, typical human clears, guaranteed survival or global dungeon
arrival-to-extraction times. Censor on death, failed access/transfer, overflow,
water ingress, extra enemies/equipment, required healing, missed source deadline
or interaction/mining/tick conditions outside the model. No physical trial or
human observation occurred. All local quality dimensions now have their explicit
modeled/inspection dispositions; remaining shell/theme variants and family-wide
coverage are still required. Historical results.json retains its v1 survey and
unbounded general active-source-clear fields; those are not this conditional v2 task.

Reproduce these new direct checks and arithmetic with retained inputs:

```sh
uv run python - <<'PILOT_COMPLETE'
import gzip, hashlib, importlib, json
from pathlib import Path
raw = Path('evidence/item-13/pilot/observations.json.gz').read_bytes()
assert hashlib.sha256(raw).hexdigest() == '15860fb3692153b2bc6ac96cc0611655d498a7a976cfa5b953f424942712686e'
state = importlib.import_module('evidence.item-13.render_pilot').state_at
for case in json.loads(gzip.decompress(raw))['cases']:
    for b in case['block_entities']:
        if b['id'] not in ('minecraft:chest','minecraft:barrel'):
            continue
        assert 'Lock' not in b and 'Items' not in b
        if b['id'] == 'minecraft:chest':
            x,y,z = b['x'],b['y'],b['z']
            assert state(case,x,y,z)['Properties']['type'] == 'single'
            assert state(case,x,y+1,z)['Name'] == 'minecraft:cave_air'
profiles = [('A',5,.5,.25,.25,1,2,1),
            ('B',4,1,.5,.5,2,4,.75),
            ('C',3,1.5,1,1,4,8,.5)]
for name,u,n,a,s,k,verify,duty in profiles:
    for case,containers,decisions,prefix,attack in [
            ('ocean',8,19,3,2.6),('mountainous',6,18,2,1.95)]:
        disable = 3/u+.95+prefix*n+a+s
        assert disable < 11
        base = 22/u+.95+decisions*n+(29*containers+1)*a+2*s+containers*k+verify
        print(name,case,'disable',disable,'noncombat',base,
              'two successful enemies',base+2*attack/duty)
PILOT_COMPLETE
```
