# Adorabuild Crimson hall: quality assessment

Status: selected case locally assessed under the authorized modeled/inspection
scope. The declared one-occurrence fixed-layout sampling minimum is satisfied
locally; Item 13 review/delivery and other families remain IN PROGRESS.

Exact source, raw hashes, saved transforms and extraction costs are in the
[batch intake](README.md#remaining-four-selected-adorabuild-inputs).
Sample: full-ocean-heavy-r2-baseline|minecraft:the_nether|adorabuild_structures:crimson_house_medium_2|-19|-27.
[Raw blocks](adorabuild-crimson_house_medium_2.json.gz), SHA-256
d51a16444c2b161505231bb6b6c010fcf388d3b9e298fda70b050a7e74c6af61,
retain envelope [-312,31,-432,-304,36,-418] and padded bounds
[-315,28,-435,-301,39,-415]. No world or runtime was changed.

The [six-layer slice view](adorabuild-crimson_house_medium_2-slices.png) was
rendered and inspected. Conversion took 1.99 seconds (1.94 user, 0.04 system);
399,279 SVG bytes plus 46,544 PNG bytes totals 445,823, within the declared
30-second/2-MiB cap. It shows an enclosed small front room and a larger fenced
rear pen under a roof, not a floor per template layer. Exact partial-state
geometry below supplements the view.

## Source assignments and supported layout

The four template residents are two adult hoglins (Health40) in the northern pen
and two brutes (Health50) in the southern room. Applying the saved clockwise
transform to source `entities[].pos` locates those roles; source health and empty
equipment are inputs, not a saved entity census. There are no saved spawners.
The chest's source local(12,3,4) maps exactly to (-308,34,-420), retaining
minecraft:chests/bastion_treasure. It is single, north-facing, non-waterlogged,
with no Lock or Items field and air immediately above at Y35.

The applied processor `replace_glass_with_air`, source SHA-256
0ecb2f0ddb213ef45d014fad7a8b2da9969b172cbf36e480c0dafe54c4edf482,
replaces glass with air, not resident entities or rewards. The structure JSON
SHA-256 c24bf7364e026cace34b95830007828f8fcb01535ef3d1c0b67e5d27f4fd37e8
has empty spawn_overrides. This does not exclude natural biome enemies.
Both resources are at their standard worldgen/processor_list and
worldgen/structure paths in the already identified Adorabuild jar.

Define R1 as the southern chest room: interior X-309..-307,Z-424..-420 above
full floor Y32, with the last row partly occupied by display stairs, pots and
chest. Trapdoor walls and the western door delimit it. R2 is the northern pen,
interior X-310..-306,Z-430..-426, floor Y32, bounded by fences and the partition
at Z-425. Count **two activity rooms**, or **one enclosed room plus one pen**
when low open-sided fencing is excluded from the strict room convention.
Both use feet Y33. Pots, the display shelf, roof and the outside step are not
extra activity rooms or upper floors.

## Declared route and interaction checks

Predeclare one adult, width0.6/height1.8, full layout knowledge and ordinary hand
opening of the crimson door and fence gate. Start on the western stair at
(-310.5,33,-421.5). The bottom east-facing stair at (-311,32,-422) supports feet
Y33 over its eastern half, with 0.3 blocks of body overlap at this staged center.
Its body cells above are air. Outside travel to the step is excluded explicitly.

Open the door at (-310,33/34,-422), saved east-facing, right-hinged, closed.
The pinned ordinary crimson-door rule permits hand opening; its opened plate
lies along a Z edge, leaving 0.8125 blocks across the passage. The centered
0.6-wide actor clears either edge plate. Walk east three blocks through this
opened cell and air to hub (-307.5,33,-421.5). All interior support is full
crimson planks except the full redstone-lamp block below that hub.

Walk north five blocks to pen station (-307.5,33,-426.5). Before crossing the
closed south-facing gate at (-308,33,-425), open it from the southern adjacent
cell. Pinned FenceGateBlock.useWithoutItem toggles OPEN, and getCollisionShape
returns Shapes.empty when open (offsets0..19). The partition's two neighboring
full columns bound a one-cell opening; air at Y34 and the cap at Y35 give two
blocks of headroom. The 0.6-wide sweep fits without mining or jumping. The gate
and door remain open for return; no automatic closing is invented.

Return five blocks to the hub, move one south to (-307.5,33,-420.5), and use the
chest's north inset face at (-307.5,34.5,-419.9375). Its ray from eye Y34.62
passes only through air before that face, above the supporting stair at Y33.
Air above the single unlocked chest supports opening under the existing
no-blocking-entity model. Return one north, then three west to the start.
Total checked movement is **18 upright horizontal blocks**, zero ascent/descent
and feet-height span. No standing on the chest display or extra upper route is
required. Model changes are two ordinary openings only, not physical observations.

## Resident combat and complete conditional time

Stipulate the four authored residents actually present at their transformed
source positions, with source health, ordinary unarmored state and no extra
entities/effects. This is a conditional composition, not proof that four enemies
survived generation or exist in the accepted world. Use the accepted full-health/
food adult player with unenchanted iron armor/sword, sufficient durability and
inventory room, 20 TPS, no criticals/sweeps, healing, mining, building or external
help. Clear the two brutes from the hub phase, then enter the pen and clear the
two hoglins. Combat duty includes pursuit/repositioning and return to the named
hub or pen station. It does not add a second copy of survey movement.

Pinned Hoglin.createAttributes sets maximum health40, knockback resistance about
0.6, attack knockback1 and attack damage6, without added armor. It does not justify
copying old template attribute-key spellings into a claim about loaded state.
With the existing six-damage iron-sword, thirteen-tick full-hit model, one ordinary
hoglin requires ceil(40/6)=7 hits, 4.55 active seconds. The established brute
component is nine hits, 5.85 seconds. Both pairs therefore total **20.8 active
attack seconds**, or 20.8/27.733333/41.6 at A/B/C contact duty.
HoglinBase.hurtAndThrowTarget invokes throwTarget after a successful adult hit;
that method uses attack knockback minus target resistance for displacement.
This supports a meaningful displacement hazard, not a predicted player injury or
a constant damage-per-hit claim. Failed survival or return within duty assumptions
invalidates the worked task. No defense or healing time is silently set to zero.

| Complete-task component | Accounting |
| --- | --- |
| Travel | 18 upright blocks |
| Decisions | 8: initial door/orientation, hub/brute phase, gate choice, pen/hoglin phase, return hub, chest choice, return to hub and exit |
| Interactions | 31: door, gate, and 29 chest-menu operations (open, 27 conditional transfer attempts, close) |
| Tool selections | One initial sword selection |
| Acquisition | One inventory-confirmation allowance |
| Mining/building | None permitted or needed on this route |
| Combat | 20.8 active seconds divided by accepted contact duty |
| Completion | One accepted verification allowance: all four stipulated enemies cleared, chest contents transferred, live return |

Using the accepted A/B/C constants, noncombat budgets are 18.6/34.5/62.0 seconds;
complete tasks are **39.4/62.233333/103.6 seconds**, approximately **39/62/104**.
These are neither empirical averages nor guaranteed bounds. Censor on missing/
additional modeled residents, changed gear/effects, inability to clear or return
within duty assumptions, death, required healing, blocked opening or transfer,
inventory overflow, or input/tick conditions outside the scenario. No human
observation, realized encounter count or acquired loot is claimed.

## Quality dimensions and limits

R1-R2 has two nodes and one gate connection, zero degree-three junctions and zero
cycles. Entry reaches R1; R2 is depth one. Its declared pen station is eight
horizontal blocks from the starting step, while the chest station is four.
There is no required vertical progression despite the six-layer component.
The floor's lit lamp and decorative pots are not meaningful damage traps. No
working trap circuit or damaging floor on the checked route is established.
Live use of the gate as a combat funnel remains untested.

Empty/dead activity rooms are 0/2: R1 has two authored brutes and the chest, R2
two authored hoglins. The strict enclosed-room denominator is 0/1 empty/dead,
retaining the nonempty pen separately. Loot is concentrated in R1, one of one
container arrangements, rather than behind the pen. The pinned base chest table
`data/minecraft/loot_table/chests/bastion_treasure.json`, SHA-256
683c11f2cce5fc3e435b21d1b5a1e98fdff714349a7f55b5e0616becd12d05a4,
contains netherite/diamond alternatives, a resource pool, snout-trim alternative
and netherite-upgrade-template pool. These are table opportunities, not rolled
inventory, comparative value or a progression guarantee.

Finale NONE: no separate terminal room or completion trigger. R1's display chest
has resource clarity, but it is near entry, with no distinct terminal challenge
or ordered room progression. R2 is a terminal pen with no assigned container,
not an invented boss room. The shorter entry-chest-entry path is eight horizontal
blocks with one door opening. It skips entry into the pen and its gate, so it is
a concrete partial-objective bypass; it does not prove that live enemies cannot
interfere. The full clear model deliberately includes the pen's residents.

All saved WORLD_SURFACE columns are Y127; 127-36=91 is a heightmap offset, not
solid burial. At the hub column Y35 is air, Y36 a slab and Y37..39 air. Roof
height supplies no measured extra dungeon floor. Nearby vegetation and unmeasured
external approaches remain context, not additional authored rooms.

Expected replay is limited in route structure: one small room/pen pair and the
same source composition, with loot rolls, resident realization and surroundings
as supported variation sources. Clearing resident entities is not a recurring
spawner mechanism; no self-reset is authored in the inspected template. Actual
persistence/replenishment belongs to its later gate. No player preference or
repeat-visit outcome is invented. Relative to the long roof footprint, spatial
progression is shallow, while four conditional enemies can still supply combat
pressure. This is not classified as trivial solely from room count.

This selected case covers the local Item 13 dimensions and the declared one-
occurrence minimum for this single-root fixed family. No additional repetition is
required merely because other families remain unfinished. Broader Item 13
coverage and required review/merge delivery remain open.
The End ship is the next selected case; Items 14 through 18 remain UNSTARTED.

## Reproduction

Reuse the batch's source jar/template identity and decode its relative entity
positions with the saved clockwise transform. Pinned Minecraft methods above
reproduce using the existing javap procedure with classes
net.minecraft.world.entity.monster.hoglin.Hoglin,
net.minecraft.world.entity.monster.hoglin.HoglinBase and
net.minecraft.world.level.block.FenceGateBlock. No server trial is implied.

```sh
uv run python -m evidence.item-13.render_pilot --input evidence/item-13/fixed-blocks/adorabuild-crimson_house_medium_2.json.gz --output /tmp/item13-crimson-hall-view.svg
timeout 30 convert -background white /tmp/item13-crimson-hall-view.svg /tmp/item13-crimson-hall-view.png
uv run python - <<'CRIMSON_HALL'
import gzip, hashlib, importlib, json, math
from pathlib import Path
raw = Path('evidence/item-13/fixed-blocks/adorabuild-crimson_house_medium_2.json.gz').read_bytes()
assert hashlib.sha256(raw).hexdigest() == 'd51a16444c2b161505231bb6b6c010fcf388d3b9e298fda70b050a7e74c6af61'
c = json.loads(gzip.decompress(raw))['cases'][0]
s = importlib.import_module('evidence.item-13.render_pilot').state_at
cells = {(-309,-422)} | {(-308,z) for z in range(-427,-420)}
for x,z in cells:
    assert s(c,x,32,z)['Name'] in ('minecraft:crimson_planks','minecraft:redstone_lamp')
    assert s(c,x,34,z)['Name'] == 'minecraft:air'
    expected = 'minecraft:crimson_fence_gate' if z == -425 else 'minecraft:air'
    assert s(c,x,33,z)['Name'] == expected
assert s(c,-308,35,-420)['Name'] == 'minecraft:air'
work = (2*math.ceil(40/6)+2*math.ceil(50/6))*13/20
assert work == 20.8
for name,u,n,a,selection,k,verify,duty in [
        ('A',5,.5,.25,.25,1,2,1),('B',4,1,.5,.5,2,4,.75),('C',3,1.5,1,1,4,8,.5)]:
    base = 18/u+8*n+31*a+selection+k+verify
    print(name,'noncombat',base,'full four-resident model',base+work/duty)
CRIMSON_HALL
```
