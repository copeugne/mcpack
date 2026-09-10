# Adorabuild Nether temple: gold-case assessment

Status: selected gold outcome assessed under the authorized modeled/inspection
scope; other processor outcomes and Item 13 delivery remain open.

Sample: full-mountainous-r1-baseline|minecraft:the_nether|adorabuild_structures:nether_temple_medium_1|20|31.
[Raw](adorabuild-nether_temple_medium_1.json.gz), SHA-256
ae02f5f37494fc594a80c81fd2f49483a8ebf102254df46a06a9d695e622c24f,
retains envelope [308,31,484,320,39,496]. The [batch intake](README.md#remaining-four-selected-adorabuild-inputs)
records the source template, clockwise180 transform, empty entity/block-entity
lists and randomize_gold_block processor. No world or server was changed.
The inspected [nine-layer sheet](adorabuild-nether_temple_medium_1-slices.png)
converted in2.00 seconds (1.98 user, .05 system), with629,828 SVG and58,165 PNG
bytes, 687,993 combined, within the declared30-second/2-MiB cap.

## Layout, hazard and objective

One open-sided shrine surrounds a7x7 lava basin at X311..317,Z487..493,Y33:
**49 saved level0 lava cells**, enclosed by a nether-brick rim atY33. Gold is
suspended at (314,35,490), under a vertical chain at (314,36,490), netherrack37
and fire38. Four corner posts and a raised perimeter frame are architectural
supports, not upper dungeon rooms. Count **one activity site, zero enclosed
rooms**. Rim feet34 and the engineered pickup floor35 are usable elevations;
the nine-layer envelope is not nine floors. Lava is a source-supported injury,
route-denial and dropped-item-loss hazard, not just a suspicious palette entry.

The complete task is to acquire the central gold block and return alive to the
western entry (309.5,34,490.5). Start is supported over the eastern half of the
bottom east-facing stair (309,33,490), with .3 body overlap. Distant travel is
excluded. Use the approved full-health/food adult with iron armor, diamond pick,
full knowledge,20 TPS, no enemies/effects/healing/flight or external help.
Required building inventory: **three cobblestone blocks, one nether-brick slab
and one cobblestone slab**. Ordinary half-block stepping and controlled edge
crouching are allowed. No lava contact is permitted in the successful scenario.
The one central gold reward is included; structural salvage is outside the goal.

A direct three-block bridge followed by mining would leave the drop over lava.
Extending a same-height bridge directly under the gold requires leaning into
its occupied body space. Neither rejected sketch is treated as a safe harvest.
The following staged lower slab, catcher and ramp avoid those obstructions.

## Staged geometry and placement checks

Walk east to rim center (310.5,34,490.5). Sequentially place cobblestone into
(311,33,490) and (312,33,490), then a **bottom nether-brick slab** into
(313,33,490), replacing three lava cells. At each placement, crouch toward the
current east edge: centers311.2,312.2,313.2, feet34, Z490.5, leaving .1 blocks
of support overlap behind the edge. The .6-wide body remains above the lava
surface and does not touch the gold. Aim back at the exposed east face of the
supporting block, below mid-height, Y33.25. EyeX is .2 beyond that face, so the
ray approaches from its exposed side rather than first hitting the floor's top.
Use the normal block interaction ray, not a fluid-targeting bucket action.
Advance only after the next support is placed. All vertical body cells in this
western corridor aboveY33 were saved air.

Move to the slab center (313.5,33.5,490.5), still crouched, eye34.77. Its full
XZ support surface isY33.5, and the actor stays wholly inside the dry slab cell.
Pinned SlabBlock.getStateForPlacement selects bottom for the declared lower-side
hit and sets WATERLOGGED only for water, not lava. Lava does not coexist inside
the placed slab as an invented lava-logged state. Do not stand with the body
hanging sideways into neighboring fluid belowY34.

Target the gold's bottom face (314.5,35,490.5) from that low crouched eye. The
ray passes through air atY34 and reaches the underside from below. Place the
third cobblestone at (314,34,490), directly under the gold, **before mining**.
This is the item-catching platform. Its full top isY35; no support removal is
required and it does not fall. Stand upright on the low slab (eye35.12), mine
the gold through its west face atY35.5, then the vertical chain through its
west face atY36.5. Both rays pass above the catcher'sY35 top. Chain removal is
required because its collision would obstruct the later adult pickup position.
The two mined blocks are ordinary dry grounded work, not swimming or airborne.

Retreat to (312.5,34,490.5), a .5 step up. Place the **different cobblestone slab**
at (313,34,490) by targeting the top of the lower nether-brick slab. Different
slab types do not merge into a double: this places the bottom slab in the next
Y cell, surface34.5. Its supporting geometry need not fill the half-block gap
beneath it. From this retreat station the downward ray reaches the old slab's
top after clearing the near support's east face. Walk east onto surface34.5,
then east onto catcher35, each a .5 step. After removal, goldY35 and chainY36
are air; ceiling netherrack37 leaves two blocks for the adult. Acquire the gold
under the approved local pickup/inventory allowance, then reverse the ramp and
bridge to the start. The fire atY38 is separated from this route by the ceiling.

This validates a conditional body/interaction route, not observed item physics.
The one-block catcher is not a guarantee against every random drop trajectory.
Retain the approved four additional horizontal pickup blocks and censor if the
item escapes, burns, cannot be reached safely or exceeds that allowance. No
successful pickup or construction has been fabricated.

## Complete timing declaration

The construction circuit is12 horizontal blocks: four from entry to the low
pad, one retreat, two to the final catcher and five back. Crouching covers2.4
of them (three .7 edge approaches and the final .3 onto the low pad);9.6 are
upright. Add four conditional upright pickup blocks, giving13.6 upright and2.4
crouched. Total ascent/descent is1.5 each, from the temporary low pad and ramp.
Use the established A/B/C upright, crouch and step speeds and stationary costs.

Five placement inputs plus two mining inputs give7 interactions. Count9 decisions:
initial approach, second support, low pad, catcher placement, gold, chain clearance,
retreat/ramp, pickup and final return. Count5 selections: initial cobblestone,
nether-brick slab, cobblestone catcher, pickaxe, cobblestone slab. One acquisition
and one final verification allowance. No container menus, combat or healing in
this declared scenario. Base source hardnesses3 and5, effective pick speed8,
give12+19=31 mining ticks, **1.55 seconds**. Full formula:
T=13.6/u+2.4/c+3/step+1.55+9*n+7*a+5*s+k+v.

Censor unsupported edge control, incorrect slab type/placement, lava contact,
blocked interaction, failed pickup, extra enemies, death, healing or movement/
input/tick conditions outside the scenario. These are conditional modeled
completion costs, never observed traversal/combat or predicted survival.

The declared formula gives **19.37/33.95/58.25 seconds**, approximately
**19/34/58**, including construction, both removals, conditional acquisition and
return. Zero modeled combat applies only to the stipulated no-enemy state.
Authored entities and spawners are both zero; actual populations are NOT MEASURED.

## Quality synthesis and coverage limit

The inspected template authors the same49 lava cells and one gold block, plus13
chains and five fire blocks. Thus the central lava hazard is authored, rather
than inferred from an unrelated nearby lava pool. The saved western corridor is
clear above its rim. Some outer eastern vegetation blocks are contextual
obstructions and are not added as authored rooms or traps. WORLD_SURFACE127
minus the39 envelope top is an88-block heightmap offset, not solid burial.

The site-level graph has one activity node, zero inter-room branches and zero
room-graph cycles. Corner pillars interrupt the narrow native rim; no continuous
rim circuit is claimed. The validated western engineered route is one connected
component, one block wide. Natural approach reaches feet34; staged access spans
feet33.5..35, with1.5 up and1.5 down over the full task. Gold-face interaction is
four horizontal blocks from the start along the western approach, zero room
edges. The final pickup center is five horizontal blocks from entry, after the
staged construction. Neither roof height nor chain count is used as dungeon depth.

Empty/dead activity sites are **0/1**: one reward and its meaningful lava obstacle.
Strict enclosed-room fractions are N/A at denominator zero. Loot is **one central
block reward, zero containers or loot-table chest rolls**. The pinned gold-block
loot table SHA-256 a9f4d6ceb0979876daa7579b701ef60f8ac2ea69aae6d9a45d1a6752d20745e4
is reused from the [blackstone temple assessment](adorabuild-blackstone_temple-report.md).
A gold block in saved data is not proof that a player recovered it. The chain is
a removed obstruction, not a separately promised expedition reward.

There is no separate final room. The central terminal objective has clarity
PRESENT, distinctive environmental challenge PRESENT, enemy climax ABSENT,
reward linkage PRESENT, and route integration CONDITIONAL on a declared crossing/
retrieval capability. Its open-sided exposure is PRESENT. The concrete engineering
route bypasses swimming through the lava for three blocks and two slabs while
retaining placement effort, material expenditure and pickup risk. It is not a
protected mandatory swimming route, and no arbitrary block restrictions are
proposed. The hanging fire/upper frame is not a second required combat floor.

Expected structural replay variety is low for this fixed single-site layout;
central processor outcome and surrounding terrain are supported variation inputs.
Revisiting a harvested block is not an authored dungeon reset. No observed player
preference or repeat-visit outcome is claimed. The large perimeter frame surrounds
one localized hazard/reward task, so it is mechanically shallow in room progression
while retaining a meaningful environmental retrieval problem.

This is the **gold outcome only**. The shared ordered randomize_gold_block rules
also admit ancient debris and lodestone. Their probabilities are source parameters,
not empirical frequencies. Different mining/dropped-item behavior can matter over
lava; this gold model must not silently stand in for either alternate. The exact
remaining scope is to inspect existing evidence for those outcomes before declaring
any minimal additional controlled experiment. No new world survey is authorized
by this single-case completion, and no Item 13 exit gate is claimed.

## Reproduction

Use the existing pinned javap procedure for Blocks and SlabBlock with the SRG jar
SHA-25626ca9c40d7e1681190b428583c38816852218e78df3f8bdb60a59a78503aec71.
Relevant SlabBlock.getStateForPlacement branches: same-block double at offsets14..48;
water-only flag at78..94; lower-side bottom choice at111..162. Ordinary partial-
block body support and crouched eye/height reuse the earlier collision/source
assessment. These are source and geometry checks, not a fresh runtime trial.

```sh
uv run python -m evidence.item-13.render_pilot --input evidence/item-13/fixed-blocks/adorabuild-nether_temple_medium_1.json.gz --output /tmp/item13-nether-temple.svg
timeout 30 convert -background white /tmp/item13-nether-temple.svg /tmp/item13-nether-temple.png
uv run python - <<'NETHER_TEMPLE'
import gzip, hashlib, importlib, json, math
from pathlib import Path
raw = Path('evidence/item-13/fixed-blocks/adorabuild-nether_temple_medium_1.json.gz').read_bytes()
assert hashlib.sha256(raw).hexdigest() == 'ae02f5f37494fc594a80c81fd2f49483a8ebf102254df46a06a9d695e622c24f'
c = json.loads(gzip.decompress(raw))['cases'][0]
s = importlib.import_module('evidence.item-13.render_pilot').state_at
for x in range(311,318):
    for z in range(487,494):
        assert s(c,x,33,z) == {'Name':'minecraft:lava','Properties':{'level':'0'}}
for x in range(310,314):
    for y in (34,35,36):
        assert s(c,x,y,490)['Name'] == 'minecraft:air'
assert s(c,314,34,490)['Name'] == 'minecraft:air'
assert s(c,314,35,490)['Name'] == 'minecraft:gold_block'
assert s(c,314,36,490)['Name'] == 'minecraft:chain'
assert s(c,314,37,490)['Name'] == 'minecraft:netherrack'
print('underside reach',math.dist((313.5,34.77,490.5),(314.5,35,490.5)))
for name,u,crouch,step,n,a,sel,k,v in [
        ('A',5,1.5,1,.5,.25,.25,1,2),('B',4,1.2,.5,1,.5,.5,2,4),
        ('C',3,.9,.25,1.5,1,1,4,8)]:
    print(name,13.6/u+2.4/crouch+3/step+1.55+9*n+7*a+5*sel+k+v)
NETHER_TEMPLE
```


## Correction: structure-level monster potential and declared combat case

The initial no-enemy task remains a conditional harvest scenario. Empty template
entities and no spawner blocks do not mean no authored monster potential:
`data/adorabuild_structures/worldgen/structure/nether_temple_medium_1.json`,
SHA-256db77b537d34db93259c458acc533ec14943a2126939f8738537fd54c7700aaab,
has the same five-entry piece-bounded override listed in the
[wart-house correction](adorabuild-nether_fortress_medium_1-report.md#correction-structure-level-monster-potential-and-declared-combat-case).
Potential diversity is five override types, zero placed-template types. Weights
and pack parameters do not establish a realized population. This integration
corrects the omitted structure-level source; it does not alter frozen evidence.

Predeclare a two-blaze complete-task sensitivity: ordinary health20/armor0,
no additional enemies or effects, initially at (310.5,34,489.5) and
(310.5,34,491.5) on the clear western rim. Clear from the entry phase before
construction, return to the starting step, then perform the whole declared
catcher/ramp harvest. Add one initial iron-sword selection and one combat-phase
decision. Both positions have full rim support and clear body cells; their
occurrence there is stipulated, not observed natural placement. The source-backed
pair attack work is5.2 seconds from the linked derivation, divided by duty.
Defense/pursuit/return is charged within duty; additional ranged equipment or
healing is not silently added. Censor extra spawns, inaccessible airborne enemies,
failed return, lava contact, lingering fire, death, or any existing harvest failure.
This does not establish a finite bound for ongoing natural spawning.

The additional declared case gives **25.32/42.383333/71.15 seconds** for A/B/C.
It is a conditional two-blaze workload, not a measured or typical clear.

```sh
uv run python - <<'OVERRIDE_CASE'
import gzip, importlib, json
from pathlib import Path
c = json.loads(gzip.decompress(Path('evidence/item-13/fixed-blocks/adorabuild-nether_temple_medium_1.json.gz').read_bytes()))['cases'][0]
s = importlib.import_module('evidence.item-13.render_pilot').state_at
for x,y,z in [(310, 34, 489), (310, 34, 491)]:
    assert s(c,x,y-1,z)['Name'] == 'minecraft:nether_bricks'
    assert s(c,x,y,z)['Name'] == s(c,x,y+1,z)['Name'] == 'minecraft:air'
for name,base,n,sel,duty in zip('ABC',(19.37,33.95,58.25),(.5,1,1.5),(.25,.5,1),(1,.75,.5),strict=True):
    print(name,base+5.2/duty+n+sel)
OVERRIDE_CASE
```
