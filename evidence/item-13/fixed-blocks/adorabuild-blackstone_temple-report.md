# Adorabuild blackstone temple: quality assessment

Status: selected gold-outcome case locally assessed, including checked geometry,
complete conditional timing and quality synthesis. Family outcome coverage and
Item 13 delivery remain IN PROGRESS.
This is the first case in the [five-root batch](../coverage.md#next-fixed-layout-batch-five-observed-adorabuild-roots).
The local representative is complete; the other four cases may proceed.

Sample: full-ocean-heavy-r2-baseline|minecraft:the_nether|adorabuild_structures:blackstone_temple_small_1|29|-8.
The [saved blocks](adorabuild-blackstone_temple.json.gz) have SHA-256
4c95ea5111f2ddc86866fba1eabc739ee4f221149a940296a172e9b6d562796b.
The [execution record](adorabuild-blackstone_temple-execution.txt) reports
2,366 voxels, 2,158 compressed bytes, 6.157766 seconds and 45,012 KiB peak RSS.
All are within the predeclared per-case budget. The existing extractor verified
full accepted-world inventories before and after under its POSIX lock, with
complete selected chunks/sections. No server was started or world changed.
Original envelope [464,31,-128,470,38,-122], padded bounds
[461,28,-131,473,41,-119]. Input, producer and world identities remain inside raw.

## Source and saved content

The pinned jar is adorabuild-structures-2.11.0-neoforge-1.21.3.jar, SHA-256
6f399680da36dbb95b9a0dbf8b600f173e650be4d6bc25f50fcac792dcce081e.
Its filename is not a compatibility claim; the accepted Item 3 runtime remains
authoritative. Resource data/adorabuild_structures/structure/blackstone_temple_small_1.nbt
has SHA-256 4ca5c2ff86de36326b1075b09daef8f2eb4e21c035ec4d72126dbc8c805a942a.
The source is 7x8x7, with no entity records or block-entity NBT. Saved block
entities are also empty. There is no authored resident or ordinary-spawner
assignment in these inputs; natural spawning and realized enemies are separate.

The single saved component has rotation NONE, rigid projection, origin
(464,31,-128), and processor adorabuild_structures:randomize_gold_block.
Source local(u,v,w) maps to(464+u,31+v,-128+w). Source gold local(3,4,3)
remains a saved gold block at(467,35,-125). Eight gilded-blackstone positions
also match exactly: at each Y33 and Y37, (466,-125), (467,-126), (467,-124)
and (468,-125) in X/Z. These are placed material rewards, not container loot,
rolled nugget outcomes or acquired resources. They cannot be omitted because
there are no chests. Four lower and four upper positions describe distribution,
not eight rooms or a demonstrated upper playable floor.

The processor JSON resource
`data/adorabuild_structures/worldgen/processor_list/randomize_gold_block.json`,
SHA-256 10e1f4737dbaf0351575f87e9fd7b56ac9007ca52886a16e990eb137e867fd87,
contains two ordered gold-block rules: a random-block-match probability 0.2
outputs ancient debris, then a probability 0.1 rule outputs lodestone. Retain
these as rule parameters, not independent observed outcome frequencies or a
claim that either alternative occurred here. The selected saved block is gold.
Material-outcome coverage and consequences for harvesting remain explicit
sampling work; do not tune or reroll this accepted occurrence.

Reproduce by reading the exact jar entries above with zipfile and decoding
gzip NBT using mcpack_evidence.item7_nbt.decode_compound_nbt, then compare
transformed gold/gilded source positions against cases[0] using the existing
render_pilot.state_at helper. Read processors as ordered JSON. No new source
inventory, extraction or custom validator is required for these direct facts.

## Next bounded assessment

The saved core contains dense wall blocks rather than an automatically playable
7x7 room. Inspect its floor, supports and complete body clearances before room
coding. The north stair at (467,32,-128) is south-facing, bottom, straight.
A candidate engineered approach must explicitly account for the chiseled block
at (467,33,-127), the lower gilded block at (467,33,-126), and central wall
blocks at (467,Y33..34,-125). They are not saved air. Validate resource rays,
source drops/tool costs, pickup assumptions and return before timing the task.
Retain all nine material nodes, plus any added removals, in the objective budget.

Use the existing slice renderer once for the eight envelope layers, with the
retained padded X/Z footprint (its supported default), budget
30 seconds and 2 MiB combined SVG/PNG, as an overall layout aid. Exact state and
source-shape checks remain necessary for partial walls and stairs. Rendering
is not player-view observation or a collision trial. Local hazards, room/depth
sensitivity, finale, bypass, replay and shallow-form assessment remain required.
Items 14 through 18 remain UNSTARTED pending predecessor gates.

## Checked breach, resource access and complete task

The [slice sheet](adorabuild-blackstone_temple-slices.png) was rendered and
inspected: eight envelope layers with padded X/Z context. Conversion passed in
0.50 seconds (0.40 user, 0.03 system); SVG 280,911 bytes plus PNG 38,470 bytes
is 319,381 bytes, within budget. The renderer supports envelope layers, not the
initially described fourteen padded Y layers; that declaration was corrected
before running it. Exact cell/source checks below supply the geometry proof.

Predeclare the local task from north-step feet (467.5,33,-127.5): mine all nine
saved material nodes, acquire their drops, and return alive. The south-facing
bottom stair at Y32 supplies a full-height southern half ending at feet Y33.
At the starting center the 0.6-wide body overlaps that upper half by 0.3 blocks;
Y33/34 are air. This is an explicitly staged supported stance, not proof of the
external approach onto it. Use the accepted adult, full health/food, unenchanted
iron armor/sword and diamond pickaxe, grounded/dry at 20 TPS, no effects, flight,
healing, extra construction or assistance, full layout knowledge and sufficient
inventory capacity. No initial or natural enemies are stipulated; this temple
has no explicit source/resident assignment to add to that scenario.

The north route is straight along X467.5 at feet Y33:

1. From the starting step, mine chiseled polished blackstone at (467,33,-127).
   Step one block south into that cleared cell. Its full floor is at Y32.
2. Mine the lower northern gilded block at (467,33,-126), then step another block
   south to (467.5,33,-125.5), again over the unchanged full Y32 floor.
3. Mine central blackstone wall (467,34,-125), then central polished-blackstone-
   brick wall (467,33,-125). These are additional obstructions, not enemy sources.
4. From this northern station, aim at the gold block's north face
   (467.5,35.9,-125). The ray from eye Y34.62 is 1.374 blocks long, above the
   removed wall positions when entering the target. Mine that gold block.
5. Step south once to center (467.5,33,-124.5), now clear at body Y33/34.
   Mine the other three lower gilded blocks and all four upper gilded blocks.
   Return three blocks north on the unchanged floors and stair support.

All approach cells have air above the named removable obstacles. Center-directed
rays to the first two full blocks can hit their top faces through that air.
The central upper wall has an isolated post; its center lies in its selection
shape. Remove it before targeting the lower central wall, whose post is also
present. This avoids assuming that stacked wall blocks are transparent.

At the final central station, the three remaining lower gilded targets are
one cardinal cell away, with reachable faces after the center walls are gone.
For each upper target, aim at its bottom-face center at Y37, one cardinal cell
away from eye Y34.62. Distance is 2.581550 blocks. The ray exits the central
cell at Y35.81, below the retained central wall beginning at Y36, then crosses
only air Y35/36 in the target column before hitting the gilded underside. Thus
no upper floor, scaffold or extra cap removal is implicit. The central gold is
removed before these rays. Diagonal posts remain outside the centerline cells.
Walls and stairs do not extend their horizontal collision beyond their cells;
all continuous body sweeps fit the cleared single-cell corridor. State changes
are modeled only; neither mining nor movement occurred in a running world.

Total required removals are twelve: eight gilded blocks, one gold, one chiseled
block and two walls. The unchanged Y32 floor supports all interior standing
stations, so removing the Y33 material does not cut away the walking floor.
The geometric out-and-back is six upright blocks, zero ascent/descent. Apply
the accepted provisional four pickup blocks per reward (36 additional blocks)
and one acquisition allowance per node. These are conditional contact budgets,
not validated drop trajectories or permission to walk through retained posts.
If any randomized drop, including an upper drop, cannot be collected within the
allowance, censor the successful task. Do not substitute ray reach for pickup.

Pinned source costs are gold hardness3 (Blocks initializer 6492), and hardness1.5
for gilded blackstone, chiseled polished blackstone and both wall types. The
chiseled registration explicitly overrides its polished parent's hardness2 with
1.5 (34536..34542); gilded and blackstone wall copy blackstone, and the brick wall
copies polished blackstone bricks. All use the diamond pick's effective speed8
under the existing correct-tool source model. Whole-tick work is 12 ticks for
gold and six for each of the other eleven blocks: 78 ticks, **3.9 seconds**.
No axe, airborne penalty, enchantment or faster unsupported tool is assumed.

Reward outcome remains distinct from the block count. Pinned extra-JAR resource
`data/minecraft/loot_table/blocks/gilded_blackstone.json`, SHA-256
768372783184cff968ded9ef36e62dbdb58cad5d616d56330c03b356d38cdffb,
uses Silk Touch first; otherwise its no-Fortune nugget branch has parameter0.1
and yields 2..5 gold nuggets, falling back to a gilded-blackstone item. The
successful no-explosion diamond-pick scenario uses these alternatives, not a
claim of eight gold blocks or an observed nugget total. Gold-block resource
`data/minecraft/loot_table/blocks/gold_block.json`, SHA-256
a9f4d6ceb0979876daa7579b701ef60f8ac2ea69aae6d9a45d1a6752d20745e4,
supplies one gold-block item under its source conditions. Pickup delay, drops
and inventory behavior reuse the accepted Circle source/model limits.

| Complete-task component | Declared accounting |
| --- | --- |
| Travel | 42 upright blocks: six checked route blocks plus 36 conditional pickup blocks |
| Decisions | 13: initial orientation, breach strategy, inner-station choice, nine material-node choices and return choice |
| Targeting | 12 mined blocks |
| Selections | One initial diamond-pick selection |
| Acquisition | Nine provisional pickup/inventory-confirmation events |
| Breaking | 3.9 seconds source work |
| Combat | Zero in the no-initial/natural-enemy scenario; no authored source/resident count |
| Completion | One accepted verification allowance, all nine node drops held and live return |

A/B/C give **33.05 / 55.90 / 94.40 seconds**, approximately **33/56/94 seconds**.
They include the explicit pickup uncertainty; they are not observed harvests,
guaranteed bounds, usual player times or survival estimates. Censor on failed
support/access/pickup, unexpected enemies, death, required healing, inventory
failure, mining/input interruption beyond allowances or changed tick conditions.
The alternative processor outcomes require different material work and are not
covered by this saved-gold result.

## Local quality synthesis and remaining coverage

Delineate **one covered shrine activity site**, or **zero enclosed rooms** under
the strict interior-room convention. Its seven-by-seven outer form contains a
raised base, narrow posts, a central decorative/reward column and roof. The
lower full material pedestals can support individual higher stances, but those
are not separate authored rooms. The core is not an unmodified seven-by-seven
walkable room: the checked working corridor exists only after the declared
breach. Nearby terrain and the roof exterior are not additional dungeon rooms.

This site-level graph has one node, zero inter-room links, degree-three junctions
or cycles, and objective graph depth zero. The checked constructed center is
three horizontal blocks from the staged north step. All nine rewards have
supported rays from that floor; required feet-height span, ascent and descent
are zero. Material heights Y33,35,37 are not three playable floors. The eight-
block template height therefore does not measure dungeon depth. Alternative
native perch-to-perch movement and global shortest routes are not established.

All saved WORLD_SURFACE columns are Y127: 127-38=89 is a heightmap offset, not
89 solid cover blocks. At the central column, roof Y38 is followed by air at
Y39/40 and leaves at Y41. Preserve that immediate air break and surrounding
vegetation rather than describing the shrine as a deep buried chamber.

The engineered access corridor is one cell wide, with at least two clear body
blocks after removals. This is a geometric constraint, not demonstrated enemy
funneling. There is no authored enemy/spawner diversity: zero assigned types and
residents, with no live census. The structure definition's spawn_overrides is
empty (resource SHA-256 0061a5513736d3b987a542cba33f9187f81100fffd9402e803d87fae44e0fa87).
That does not suppress biome spawning or prove an encounter-free baseline.

No fire, lava or magma is in the source template palette. The saved southwest
corner (464,31,-122) is lava, with more lava/magma in padding below/around the
base. Fire is at (463,32,-129), outside the envelope. Neither intersects the
checked north-center route. Eastern brimwood/log-magma vegetation is saved
context, not an authored trap; its live behavior is not tested here. Displacement,
new flow, burning dropped items or leaving the supported route can invalidate the
worked harvest. No operating damaging circuit or forced combat chokepoint is
established by the source layout.

Empty/dead activity-site counts are 0/1 because the site has nine material rewards.
With zero enclosed rooms, room-only empty/dead fractions are N/A, not 0/0 scored
as zero percent. Distribution is four lower gilded nodes, one central gold and
four upper gilded nodes in the same site, with no containers. Finale is NONE:
no distinct terminal room, challenge escalation or authored completion trigger.
The central gold provides a visible resource focus, not a final-room encounter;
terminal challenge and ordered room integration are absent.

The direct north breach demonstrates external access to the central reward
without a sequence of rooms or an upper climb. After two approach removals and
two central-wall removals the gold is reachable; the broader task also harvests
all gilded nodes. This is a concrete earned-engineering bypass of the display
column, not an optimal-cost claim or a proposal to protect the shrine artificially.

Expected replay variation is supported by the processor's alternate central
material, nugget/block drop alternatives and surrounding terrain. No core room
rearrangement is established for this one-template design. The worked harvest
consumes finite placed resources and leaves its breach; no self-reset is authored
in these inspected inputs. Player enjoyment, repeat visits and actual persistence
outcomes remain unmeasured. Flag this as a **mechanically shallow ornamental
resource shrine**, not a demonstrated giant dungeon: layered roof/column height
adds no required vertical progression or room sequence to this task.

This closes the selected gold-outcome case locally. The other generated candidate
and the central ancient-debris/lodestone outcomes still need their applicable
coverage dispositions using existing evidence before any additional experiment.
The other four selected Adorabuild layouts may now proceed. Whole-family material
coverage, all remaining included families and Item 13 review/delivery remain open.

## Reproduction of the new local derivation

```sh
uv run python -m evidence.item-13.render_pilot --input evidence/item-13/fixed-blocks/adorabuild-blackstone_temple.json.gz --output /tmp/item13-blackstone-temple-view.svg
timeout 30 convert -background white /tmp/item13-blackstone-temple-view.svg /tmp/item13-blackstone-temple-view.png
uv run python - <<'TEMPLE_TASK'
import gzip, hashlib, importlib, json, math
from pathlib import Path
raw = Path('evidence/item-13/fixed-blocks/adorabuild-blackstone_temple.json.gz').read_bytes()
assert hashlib.sha256(raw).hexdigest() == '4c95ea5111f2ddc86866fba1eabc739ee4f221149a940296a172e9b6d562796b'
c = json.loads(gzip.decompress(raw))['cases'][0]
s = importlib.import_module('evidence.item-13.render_pilot').state_at
for z in (-127,-126,-125):
    assert s(c,467,32,z)['Name'] == 'minecraft:polished_blackstone_bricks'
for x,z in ((466,-125),(467,-126),(467,-124),(468,-125)):
    for y in (33,37):
        assert s(c,x,y,z)['Name'] == 'minecraft:gilded_blackstone'
    for y in (35,36):
        assert s(c,x,y,z)['Name'] == 'minecraft:air'
assert s(c,467,35,-125)['Name'] == 'minecraft:gold_block'
assert not c['block_entities']
print('upper ray length / central exit Y', math.hypot(1,2.38), (34.62+37)/2)
work_ticks = math.ceil(3*30/8)+11*math.ceil(1.5*30/8)
assert work_ticks == 78
for name,u,n,a,selection,k,verify in [
        ('A',5,.5,.25,.25,1,2),('B',4,1,.5,.5,2,4),('C',3,1.5,1,1,4,8)]:
    print(name, 'complete conditional task',
          42/u+work_ticks/20+13*n+12*a+selection+9*k+verify)
TEMPLE_TASK
```

## Supplementary baseline material check

The [predeclared remaining-candidate read](../coverage.md#temple-processor-outcome-availability-and-bounded-remaining-read)
completed for ocean-heavy r1 at29,-8. Its [raw extract](adorabuild-blackstone_temple-r1.json.gz)
has SHA-256fd836a1e3e4b7434dd47e19180273013b300e89e2941d7ce3e20a963ae68000b:
2366 voxels,2030 compressed bytes,5.189525 seconds,45,604 KiB peak RSS. The
[execution output](adorabuild-blackstone_temple-r1-execution.txt) is retained.
The unchanged reader passed its full before/after world inventories under the
existing POSIX lock. No server or world mutation occurred.

Its central cell (467,35,-125) is also minecraft:gold_block. Thus both indexed
baseline starts have gold; neither supplies generated debris or lodestone. This
is two raw occurrences of one fixed material outcome, not additional variant
coverage or proof of the processor's empirical probabilities. No duplicate full
quality report or render is necessary to establish that exact missing outcome.
The original r2 assessment remains the selected primary case.


## Alternate-material source inputs for the declared placement diagnostic

Pinned Blocks registers ancient debris with hardness30 and lodestone with
hardness3.5; both require the correct tool for drops. Both are full block
geometries in the packaged template replacement, not extra rooms. The captured
Items initializer explicitly applies fireResistant to the ancient-debris
BlockItem (offsets769..785); lodestone uses ordinary registerBlock at22841..22847.
This supports a difference in item fire resistance, not a claim that a player
can safely enter lava or that any drop has been acquired. The registered processor
changes the central block, not the surrounding route. Actual processed and saved
variant states must still pass the predeclared runtime check before integration.

For the same declared grounded dry diamond pick, the nominal work rule is
ceil(hardness*30/8) ticks. Preserve the existing complete task's movement, input,
construction, combat and conditional acquisition accounting; substitute only
central-block mining work when the saved replacement relationship is verified.
Do not silently delete the Nether temple catcher just because debris resists fire.
