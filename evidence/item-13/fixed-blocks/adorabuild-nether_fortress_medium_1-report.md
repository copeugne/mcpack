# Adorabuild wart house: quality assessment

Status: selected fixed case locally assessed; geometry and arithmetic checks pass.
This fixed root is Adorabuild's nether_fortress_medium_1, not a vanilla Fortress.

Sample: full-ordinary-r1-baseline|minecraft:the_nether|adorabuild_structures:nether_fortress_medium_1|10|-9.
[Raw](adorabuild-nether_fortress_medium_1.json.gz), SHA-256
4dc9b8bb6668ffbbd590c8d39ae854f29a656ef23675e401855372712cabff96,
retains envelope [152,31,-144,160,39,-136]. Frozen source identity, one rigid
clockwise component, empty processor, entities[] and three chest assignments are
in the [batch intake](README.md#remaining-four-selected-adorabuild-inputs).
No new runtime or world changes occurred. The inspected
[nine-layer sheet](adorabuild-nether_fortress_medium_1-slices.png) converted in
0.33 seconds (0.34 user, .02 system). SVG409,927 plus PNG50,062 bytes totals
459,989, within the predeclared 30-second/2-MiB case cap.

## Room and access measurements

R1 is the covered lower crop room, X153..159,Z-143..-137, soul-sand floor Y32,
with three southwest cells occupied by stair supports instead of crops. All
46 retained nether-wart plants have age0. R2 is the upper chest room over the
same footprint, full floor Y35, feet36 and ceiling39. The southwestern stair
opening and one southeast vegetation column are excluded from clear floor.
Count **two activity rooms**; the four-block stair is a connector, not four rooms.
R1 has 2.125 blocks from soul-sand surface32.875 to ceiling35; R2 has three.

The complete modeled objective is to visit R1, empty all three R2 chests and
return to the local southern start. Harvesting/replanting 46 crops and ordinary
building-material salvage are explicitly outside this expedition objective;
their source potential is still part of the quality assessment. This is not a
claim to time exhaustive stripping of every useful block.

Actor: one adult width.6/height1.8, full health/food, unenchanted iron armor,
diamond pickaxe, full route knowledge, ordinary half-block stepping, sufficient
durability/inventory, 20 TPS. No enemies, effects, Soul Speed, healing, jumping,
flight or external help in this conditional scenario. Natural enemies are
excluded explicitly; zero authored entities/spawners does not prove an empty
live world. Start (153.5,33,-135.5) on the top north half of the bottom north-
facing stair at (153,32,-136), with .3 blocks of supporting body overlap.
External travel to this local step is excluded.

A direct east entry is blocked by two walls, at (154,33,-136) and (154,34,-136).
Remove the upper then lower wall from the start, through their west post faces;
body position remains on the stair. This rejects a one-wall breach: the upper
post would block the adult's head. Full floorY32 remains, ceilingY35 remains.
Walk one east into the resulting one-cell-wide, two-high passage, then one north
to (154.5,32.875,-136.5) in R1. SoulSandBlock's collision surface is14/16;
Blocks declares its .4 speed factor and the crop has no collision. AirY34 and
ceiling35 give clear adult occupancy. Return one south with a .125 step up,
then one west to the original stair. No unvalidated stair-side drop into the
crop room is assumed. Mine costs include both walls but no crop removal.

Continue north up the existing stairs at X153, (Y,Z)=(32,-136),(33,-137),
(34,-138),(35,-139), all bottom, straight, north-facing. Successive half-treads
give .5 rises, with full support blocks below. At their declared center stations
feet33,34,35,36 the body overlaps the upper supporting half by .3; air above
the stair run admits the adult. Reach (153.5,36,-138.5), three horizontal and
three vertical blocks above start. Walk three east, then one north to hub
(156.5,36,-139.5). Every crossed upper floor is full nether brick, with air
at Y36/37. From that hub take three out-and-back branches, each two blocks out:

- North to (156.5,36,-141.5), use chest (156,36,-143) through south inset face.
- East to (158.5,36,-139.5), use chest (159,36,-140) through west inset face.
- South to (156.5,36,-137.5), use chest (156,36,-137) through north inset face.

Each ray ends at chest center-height36.5, .5625 horizontal from eye37.62,
through air before the chest. All three single chests have air above atY37,
no Lock and no Items. Opening/transfers remain conditional on no blocking
entities and free inventory. Return from hub one south/three west, descend
three horizontal/three vertical stair blocks, end at the start.

The complete route totals **30 horizontal blocks**: four for R1 and26 for R2.
Charge two R1 blocks at .4 times upright speed, the other28 at upright speed.
This deliberately charges the whole approach/return segments for soul-sand
slowdown instead of asserting a measured boundary-crossing speed. Total ascent
and descent are3.125 each, floor span3.125, distinct from the nine-layer envelope.
Use the existing 1/.5/.25 step-speed sensitivities for the6.25 vertical total.
The two removals use hardness2, copied by nether_brick_wall from nether_bricks,
and the effective diamond-pick speed8: ceil(2*30/8)=8 ticks each, .8 seconds.
The pickaxe tag includes #minecraft:walls, which contains this wall; checking
only direct tag entries would incorrectly reject effective tool use.

## Complete timing declaration

Use approved A/B/C stationary allowances. Count12 decisions: initial breach,
field entry, field return, stair ascent, hub/north choice, north return, east
choice, east return, south choice, south return, stair descent and final exit.
Count89 interactions: two wall-target inputs plus3*29 chest menu operations.
One initial pickaxe selection, three inventory acquisition checks and one final
verification. No construction. Zero combat work is conditional on the declared
no-enemy state; it is not observed combat time or a forecast of natural spawning.
The full formula is T=28/u+2/(.4*u)+6.25/step+.8+12*n+89*a+s+3*k+v.
Censor death, extra enemies, required healing, movement/input beyond allowances,
failed chest opening/transfer, inventory overflow or changed conditions. Crop
harvest time is not hidden inside acquisition allowances.

Validated formula results: **47.15/88.55/164.8 seconds**, approximately
**47/89/165**, for the complete declared visit-and-three-chest task. These are
conditional sensitivity budgets, not percentiles, actual clear times or farming
yield measurements. Human traversal/combat and generated/acquired loot remain
NOT MEASURED.

## Quality synthesis

The validated graph is entry E linked separately to R1 by the two-wall breach
and R2 by the native stair. It has two room nodes plus the explicit exterior
entry node, two links, one connected component, zero degree-three junctions and
zero independent cycles. A direct interior R1-R2 connection was not validated
and is not invented. Both rooms are graph depth one from E; the deepest floor
is R2. R1's visited station is two horizontal blocks from E; the upper hub is
seven. Shortest cardinal entry-to-station routes are nine horizontal blocks
for the north/east chests and seven for the south chest, each with three ascent
blocks. The declared hub circuit takes nine to the south chest as well; that
extra hub detour is not labeled shortest depth. The stair and breach each constrain a .6-wide adult to a one-cell
corridor; live use as a combat funnel is NOT MEASURED.

Placed template residents and spawner blocks are0/0. The structure-level monster
override supplies five potential types, detailed below; it must not be erased
by the empty template entity list. No working damage trap is established. Soul sand is a supported
movement-pressure mechanism on the lower visit, not an invented damaging floor.
The intrusive warped-wart block at (158,34,-143) reduces part of R1's headroom;
the column at (159,36..38,-138) blocks part of R2. Neither intersects the declared
route and neither creates another room. WORLD_SURFACE=127 minus envelope top39
is an88-block heightmap offset, not proof of88 solid blocks over the roof.

Empty/dead rooms are **0/2**: the lower room has46 planted crops and the upper
room three loot containers. Quiet agricultural use prevents calling R1 dead
merely because there is no enemy. All3/3 container arrangements are in R2; the
lower crop field is recorded separately, not as46 treasure chests. Each chest
references minecraft:chests/nether_bridge, whose pinned base table SHA-256 is
56fceac267476866f2381335b4ac1b3eeab33993610d854752cd2f011c2062e6.
It includes resource, equipment, saddle/horse-armor, wart and rib-trim alternatives.
The nether_wart block table SHA-256 is
205549738d20027a55381b8dcc2f47110c9669fdb6661d32e6db12ea9a7a583b.
Age0 is an observed block state, not mature crop output or an acquired quantity.
These resources are in the pinned Minecraft extra jar identified in the batch's
linked local reports; table potentials are not measured loot quality/value.

R2 is a terminal reward space under the declared chest objective: clarity and
reward linkage PRESENT, route integration PRESENT through the ascending stair,
distinctive terminal challenge ABSENT, completion trigger ABSENT. No boss is
invented. External bypass exposure is CONDITIONAL: upper wall windows are visible
but do not alone prove body access. A concrete partial-task bypass is simpler:
start directly up the native stair, take the same26-horizontal-block upper
circuit, return. It skips R1 and its breach while reaching all three chests.
The full declared task includes R1 to retain the building's usable lower level.

Expected layout replay variation is limited to this fixed two-level plan;
loot rolls, crops and surrounding vegetation vary. The one-block movement
bottleneck and ascent are real progression. The source-defined monster override
adds conditional encounter pressure, although realized spawning remains unmeasured. The building is not nine floors or a deep dungeon because its enclosing
walls/roof are tall. It is a shallow two-room agricultural/loot site, rather than
an assumed vanilla-Fortress encounter. Crop renewal and persistent revisit
behavior are not timed here; no player enjoyment or actual return outcome is
claimed. The selected occurrence satisfies the fixed-family local assessment
minimum. Item 13's wider coverage and review/merge/delivery gate remain open.

## Reproduction and focused checks

Read exact coordinates through the existing state_at reader. For source mechanics,
use the established pinned javap procedure on SoulSandBlock and Blocks. The
wall tag resource data/minecraft/tags/block/walls.json has SHA-256
f6eb92fb38b0122f7d18c3b1a9a234848493a5ab3727961f460ebe6e3160a822;
its parent pickaxe tag and pinned runtime identity are reused from model-source.

```sh
uv run python -m evidence.item-13.render_pilot --input evidence/item-13/fixed-blocks/adorabuild-nether_fortress_medium_1.json.gz --output /tmp/item13-wart-house.svg
timeout 30 convert -background white /tmp/item13-wart-house.svg /tmp/item13-wart-house.png
uv run python - <<'WART_HOUSE'
import gzip, hashlib, importlib, json
from pathlib import Path
raw = Path('evidence/item-13/fixed-blocks/adorabuild-nether_fortress_medium_1.json.gz').read_bytes()
assert hashlib.sha256(raw).hexdigest() == '4dc9b8bb6668ffbbd590c8d39ae854f29a656ef23675e401855372712cabff96'
c = json.loads(gzip.decompress(raw))['cases'][0]
s = importlib.import_module('evidence.item-13.render_pilot').state_at
cells = {(x,-139) for x in range(154,157)} | {(156,z) for z in range(-142,-137)} | {(x,-140) for x in range(156,159)}
for x,z in cells:
    assert s(c,x,35,z)['Name'] == 'minecraft:nether_bricks'
    for y in (36,37):
        assert s(c,x,y,z)['Name'] == 'minecraft:air'
for x,z in [(156,-143),(159,-140),(156,-137)]:
    assert s(c,x,37,z)['Name'] == 'minecraft:air'
plants = [s(c,x,33,z) for x in range(153,160) for z in range(-143,-136)
          if s(c,x,33,z)['Name'] == 'minecraft:nether_wart']
assert len(plants) == 46 and all(p['Properties']['age'] == '0' for p in plants)
for name,u,step,n,a,sel,k,v in [
        ('A',5,1,.5,.25,.25,1,2),('B',4,.5,1,.5,.5,2,4),('C',3,.25,1.5,1,1,4,8)]:
    print(name,28/u+2/(.4*u)+6.25/step+.8+12*n+89*a+sel+3*k+v)
WART_HOUSE
```


## Correction: structure-level monster potential and declared combat case

The earlier no-enemy task is retained as an explicitly conditional scenario.
Its initial source synthesis omitted a material fact already recorded by Item 9:
`data/adorabuild_structures/worldgen/structure/nether_fortress_medium_1.json`,
SHA-256441646d1a6e583170a2598cb1a4c20d94bb959da32bcd2100f3d76457d2c330a,
defines a piece-bounded monster spawn override in the pinned Adorabuild jar.
Template residents, spawner blocks and natural-spawn override entries are three
separate mechanisms. This correction supersedes the initial zero-type inference.

| Potential type | Source weight | Source min..max count |
| --- | ---: | ---: |
| Blaze | 10 | 2..3 |
| Zombified piglin | 5 | 4..4 |
| Wither skeleton | 8 | 5..5 |
| Skeleton | 2 | 5..5 |
| Magma cube | 3 | 4..4 |

These are five alternatives, not a simultaneous enemy census. The values do
not establish realized spawning, population, successful packs, encounter frequency
or independent spawn probability. Biome/world spawning conditions still matter.
Enemy diversity potential is five structure-override types, zero template types.

Predeclare one additional complete-task sensitivity case using two ordinary blazes,
the minimum count of the highest-weight override entry, not a claim that it is
the most frequent realized encounter. Stipulate health20, armor0, no effects or
extra enemies, at clear upper-floor positions (156.5,36,-139.5) and
(157.5,36,-141.5). After ascending, clear them during the upper hub phase, then
perform all three transfers and return. Reuse the prior actor with an unenchanted
iron sword added; charge one additional sword selection and one combat-phase
decision. Contact duty includes defense, pursuit and return to the hub. Censor
unreachable airborne targets, extra spawning, necessary healing, death, persistent
fire/hazard effects, or inability to finish and return within duty assumptions.
No natural spawning or actual encounter was performed to manufacture this pair.

Pinned Blaze.createAttributes uses Monster defaults without replacing maximum
health or armor; the existing captured Attributes derivation gives default health20.
The six-damage, thirteen-tick model therefore needs four hits,2.6 active seconds
per ordinary blaze. BlazeAttackGoal has melee and SmallFireball attack paths;
flying/projectile pressure is retained, not treated as stationary passive targets.
The declared pair adds5.2/duty plus one decision and one selection to the prior
complete task. The no-enemy task remains47/89/165 seconds, not generic combat time.

The additional declared case gives **53.1/96.983333/177.7 seconds** for A/B/C.
It is a conditional two-blaze workload, not a measured or typical clear.

```sh
uv run python - <<'OVERRIDE_CASE'
import gzip, importlib, json
from pathlib import Path
c = json.loads(gzip.decompress(Path('evidence/item-13/fixed-blocks/adorabuild-nether_fortress_medium_1.json.gz').read_bytes()))['cases'][0]
s = importlib.import_module('evidence.item-13.render_pilot').state_at
for x,y,z in [(156, 36, -140), (157, 36, -142)]:
    assert s(c,x,y-1,z)['Name'] == 'minecraft:nether_bricks'
    assert s(c,x,y,z)['Name'] == s(c,x,y+1,z)['Name'] == 'minecraft:air'
for name,base,n,sel,duty in zip('ABC',(47.15,88.55,164.8),(.5,1,1.5),(.25,.5,1),(1,.75,.5),strict=True):
    print(name,base+5.2/duty+n+sel)
OVERRIDE_CASE
```
