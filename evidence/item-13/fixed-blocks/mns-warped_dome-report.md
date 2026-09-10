# Warped Dome: quality assessment

Status: local sampled assessment recorded under the accepted conditional method.
One ground room, resource access, full scenario timing and quality dimensions are
integrated below. Family repetitions and Item 13 delivery remain IN PROGRESS.

Sample: full-ordinary-r2-baseline|minecraft:the_nether|mns:warped_dome|11|2.
The existing [saved blocks](mns-warped_dome.json.gz), SHA-256
5529ab7797e146dc660a7d2f1e6cec6f5b357c5b03052b15725481f5bd25b602,
retain 18,816 voxels, envelope[165,64,19,186,78,44] and padded bounds
[162,61,16,189,81,47]. World/start identity and full saved-section checks are
already retained in that dataset and its execution record. No new extraction,
world generation or server experiment is needed for the observations below.

The saved start contains one rigid mns:warped_dome single-pool component,
empty processors, origin(186,64,44), rotation CLOCKWISE_180. Local template
block(u,v,w) maps to world(186-u,64+v,44-w). The source resource is
data/mns/structure/warped_dome.nbt inside the retained
MoogsNetherStructures-1.21-3.0.0-alpha.2.jar, JAR SHA-256
05024f18690436fff2fbc088f880a95cc30f23bacfe6e8058f6b02106032a990;
resource SHA-256 3f9d841ef97afc84a8ffde17fc9c28b4149fdc6a638c0579e04e88052e1d7274.
Its dimensions 22x15x26 identify the authored layout, not rooms or playable depth.

The [slice sheet](mns-warped_dome-slices.svg) was visually inspected. It shows
an open central volume beneath a curved shell of slabs, stairs, fences and
trapdoors, with terrain/vegetation around it. Repeated horizontal shell rings
are not stacked rooms or floors. Their collision, support and any usable
vertical transition must be resolved before scoring. Rendering categories
alone do not establish walkable topology.

## Saved content, attribution and measurement boundary

The template has no entity entries, block entities or spawner palette entry.
The saved envelope likewise contains no ordinary spawners, chests or barrels.
The retained barrel at(171,81,46), with mns:chests/houses table potential,
lies outside the envelope and is not a Dome reward node. Its inclusion in
the padded dataset does not establish authorship. These observations support
zero template-authored resident/spawner types, not a census of naturally
spawned enemies. A workload restricted to those absent template enemy sources
has zero attacks by definition; actual combat duration and realized enemies
remain NOT MEASURED. Do not infer a safe or pressure-free visit.

The Dome is not reward-free. Direct source-to-saved comparison establishes:

| Source material | Authored positions | Saved identical block names | Interpretation |
| --- | ---: | ---: | --- |
| Nether gold ore | 26 | 26 | Placed extractable-material opportunities, not generated container loot or acquired gold |
| Nether wart | 17 | 17 | Surviving plants, not a measured harvest or renewable yield |
| Soul sand | 28 | 28 | Plant substrate/material; movement effect needs route-specific support |
| Magma block | 12 | 12 | Saved hazard ingredients with an already supported contact mechanism; route exposure remains pending |

Gold ore occupies 21 source positions at Y64 and five at Y65. Magma occupies
11 positions at Y64 and one at Y65. All 17 wart plants are at Y65. This places
the resource/hazard inputs near the ground rather than in the high shell, but
does not establish reach or classify every nearby pocket as a room. Matching
names do not prove matching growth age or other properties; the raw palettes
retain those values for any later harvest model. No harvesting model is scored
here. The source also contains 47 cyan-concrete-powder blocks; that alone is
not evidence of an operating falling-block trap.

All 572 saved WORLD_SURFACE columns are Y127. The difference 127-78=49 above
envelope top is heightmap context, not 49 solid blocks of roof cover or a
validated underground approach. Local overhead and entry conditions remain
separate measurements.

## Reproduction and next measurement

The existing renderer reproduces the inspected sheet:

```sh
uv run python -m evidence.item-13.render_pilot --input evidence/item-13/fixed-blocks/mns-warped_dome.json.gz --output /tmp/item13-dome-slices.svg
```

Reproduce the material correspondence using the existing NBT decoder:

```sh
uv run python - <<'DOME_CHECK'
import gzip, hashlib, importlib, json, zipfile
from pathlib import Path
from mcpack_evidence.item7_nbt import decode_compound_nbt
raw = Path('evidence/item-13/fixed-blocks/mns-warped_dome.json.gz').read_bytes()
assert hashlib.sha256(raw).hexdigest()=='5529ab7797e146dc660a7d2f1e6cec6f5b357c5b03052b15725481f5bd25b602'
case = json.loads(gzip.decompress(raw))['cases'][0]
state = importlib.import_module('evidence.item-13.render_pilot').state_at
with zipfile.ZipFile('downloads/item3/candidates/MoogsNetherStructures-1.21-3.0.0-alpha.2.jar') as jar:
    source = jar.read('data/mns/structure/warped_dome.nbt')
assert hashlib.sha256(source).hexdigest()=='3f9d841ef97afc84a8ffde17fc9c28b4149fdc6a638c0579e04e88052e1d7274'
template = decode_compound_nbt(gzip.decompress(source))
assert not template.get('entities')
assert not any('nbt' in b for b in template['blocks'])
for name,count in [('nether_gold_ore',26),('nether_wart',17),('soul_sand',28),('magma_block',12)]:
    positions = [(186-b['pos'][0],64+b['pos'][1],44-b['pos'][2])
                 for b in template['blocks']
                 if template['palette'][b['state']]['Name']=='minecraft:'+name]
    assert len(positions)==count
    assert all(state(case,*p)['Name']=='minecraft:'+name for p in positions)
    print(name,positions)
assert len(case['surface_xzy'])==572
assert {p[2] for p in case['surface_xzy']}=={127}
DOME_CHECK
```

The completed local route, predeclared resource task and resulting quality
assessment follow below. Item 14 remains UNSTARTED.

## Northern ground access, geometric measurement

The retained blocks resolve a direct northern entry without interacting with the
shell. A 0.6-block-wide, 1.8-block-high adult actor can follow this axis-aligned
centerline at feet Y65. Add 0.5 to each listed X/Z cell coordinate:

(176,26), (176,27), (176,28), (176,29), (176,30), (175,30),
(175,31), (174,31), (174,32), (174,33), (174,34).

All eleven positions have ordinary full-cube support at Y64 and air at Y65/66.
The eight concrete-powder supports have netherrack immediately beneath them at
Y63. They are supported floor on this route, not an activated falling trap.
The other three supports are warped nylium, warped planks and a copper bulb.
The centerline stays within the air cells, including at its right-angle turns;
no stair, door, fence or trapdoor shape is traversed. Adjacent decoration is not
counted as traversed collision geometry. No mining, jumping, crouching, magma or
soul-sand contact is required along these ten blocks. The path connects the
northern opening to the central southern floor sector without a vertical change.
This is geometric access evidence, not observed movement or complete task timing.

The southern axial approach is different: the wall at (176,65,37) and fence at
(176,66,37) interrupt it. Do not infer symmetric access from the shell's appearance.
The northern path avoids the four closed central trapdoors rather than treating
them as air. This establishes a usable entrance and a route through the central
volume, not a proof of all peripheral resource access or an exhaustive route graph.

Reproduce the direct inspection against the already retained hash:

```sh
uv run python - <<'DOME_ROUTE'
import gzip, hashlib, importlib, json
from pathlib import Path
raw = Path('evidence/item-13/fixed-blocks/mns-warped_dome.json.gz').read_bytes()
assert hashlib.sha256(raw).hexdigest() == '5529ab7797e146dc660a7d2f1e6cec6f5b357c5b03052b15725481f5bd25b602'
case = json.loads(gzip.decompress(raw))['cases'][0]
state = importlib.import_module('evidence.item-13.render_pilot').state_at
route = [(176,26),(176,27),(176,28),(176,29),(176,30),(175,30),
         (175,31),(174,31),(174,32),(174,33),(174,34)]
supports = {'minecraft:warped_nylium', 'minecraft:warped_planks',
            'minecraft:cyan_concrete_powder', 'minecraft:waxed_oxidized_copper_bulb'}
for x,z in route:
    assert state(case,x,64,z)['Name'] in supports
    assert state(case,x,63,z)['Name'] == 'minecraft:netherrack'
    assert all(state(case,x,y,z)['Name'] == 'minecraft:air' for y in (65,66))
assert sum(abs(a-c)+abs(b-d) for (a,b),(c,d) in zip(route,route[1:])) == 10
assert state(case,176,65,37)['Name'] == 'minecraft:deepslate_brick_wall'
assert state(case,176,66,37)['Name'] == 'minecraft:warped_fence'
print('Northern access: ten horizontal blocks, eleven supported air positions.')
DOME_ROUTE
```

The complete-objective model below adds resource acquisition and its external
route using the accepted [conditional accounting method](../timing-scenario-proposal.md).
The ten-block interior inspection alone is not completion timing. No runtime or
new materialization was used for this geometric measurement.

## Harvest potential, source inspection

All 17 saved wart plants listed in the envelope have `age=3` in the retained
palette and block positions. In the pinned Minecraft extra JAR, the resource
`data/minecraft/loot_table/blocks/nether_wart.json`, SHA-256
205549738d20027a55381b8dcc2f47110c9669fdb6661d32e6db12ea9a7a583b,
sets mature-plant item-count potential to 2..4 before the declared Fortune and
explosion modifiers. Under the accepted standard actor assumptions, ordinary breaking uses no Fortune.
This supports mature resource potential, not an acquired inventory count.

The same JAR's `data/minecraft/loot_table/blocks/nether_gold_ore.json`, SHA-256
ebe0027917b98546370bfbc086ab60cbe29ccf131777954c642ab74bf39d449b,
selects the ore block with Silk Touch, otherwise 2..6 gold nuggets before its
Fortune/explosion modifiers. The unenchanted diamond-pick scenario follows the
nugget branch. The ore is a material opportunity rather than a dungeon
loot-table chest or an engineering-progression reward. Source-table potential
does not establish collection, tool use, approach safety or actual generated drops.

These resources were read directly from the pinned local extra JAR at
`instances/pristine-baseline-v0/libraries/net/minecraft/server/1.21.1-20240808.144430/server-1.21.1-20240808.144430-extra.jar`,
SHA-256 24a5d2d162cfad2a1a574c4d552e99dc6c6303a49d1e68b43a7b638f3b0930fd.
The JSON conditions above are the derivation; no runtime harvest was performed.

## Resource-task predeclaration

The site has no authored boss, clear trigger or terminal reward. Define its complete
modeled expedition task explicitly: start at the northern entry (176.5,65,26.5),
inspect the central floor to (174.5,65,34.5), return through the same entry, harvest
one exposed ore at (175,64,24) and one mature wart at (176,65,22), acquire their
drops, and return alive to the entry. This is a representative resource-acquisition
objective, not exhaustive stripping of all 43 resource positions, an authored
completion trigger, or proof that every peripheral deposit is accessible.

Reuse the approved single-adult actor, full knowledge, iron armor, unenchanted
iron sword/diamond pick, full health/food and free inventory. No natural or
pre-existing mobs are stipulated; the source supplies no residents/spawners.
Combat work is therefore zero in this scenario only. No construction, flight,
teleportation, healing, extra mining or assistance is allowed. Use 20 TPS.

After the 20-block out-and-back interior route, take entry cell (176,26) to
(176,25), (176,24), then crouch into magma cell (176,23). Reverse to the entry
after resource work. Mine the neighboring ore from (176.5,65,24.5), without
removing the route's supporting nylium. Break the wart from the crouched magma
station. Exact target rays and supporting cells must pass before calculating.
Magma crossing uses the already sourced shift-key avoidance mechanism.

Use the accepted A/B/C speeds and action allowances. Predeclare five decision
budgets: entry orientation, central inspection, resource sequence, ore-to-wart
transition and return. Two targeting budgets cover the two broken blocks; one
tool selection equips the pickaxe. One final verification checks acquired items
and return. Mining work uses source hardness/tool mechanics; instant plant breaking
still consumes the targeting/input budget. There is no menu or container action.

For each of the two drops, use two accepted acquisition allowances, not an
unverified extra path at ordinary speed. The doubled allowance includes local
pickup movement, footing adjustments, remaining pickup delay and inventory
confirmation, with return to the mining station. This is a provisional 2/4/8-second
budget per resource, varied with A/B/C, not calibrated pickup time. It explicitly
covers the ore pit and wart's soul-sand edge; no guaranteed route or success is
claimed. No additional pickup-distance term is charged. Censor failed acquisition
within that budget, magma damage from incorrect pose, required healing/death,
extra enemies, mining disruption beyond allowances, invalid access or non-20-TPS
conditions. Do not estimate success probability or count censoring as a clear.

This local calculation reuses the retained 18,816-voxel dataset and pinned sources.
It requires no server/materialization and no new extraction. Limit the remaining
direct checks to the two rays, route cells and source breaking work, with under
one minute of processing and no new raw dataset. Existing broader resource and
shell observations supply the quality assessment; do not repeat them as a survey.

## Resource-task result and quality synthesis

The four resource-route cells at X176, Z23..26 have air at Y65/66. Their Y64
supports are magma at Z23 and nylium at Z24..26. Mining (175,64,24) does not remove
that support. The standing eye (176.5,66.62,24.5) can aim at the ore's top-center
(175.5,65,24.5), approximately 1.90 blocks away, through air. The crouched eye
(176.5,66.27,23.5) can aim at (176.5,65.5,22.5), approximately 1.26 blocks away.
The wart's mature outline occupies the full X/Z cell and Y65..65.875, so this ray
enters that target after crossing air above the magma. Both targets are within
three blocks; no intervening stem or shell block lies on either segment. This
resolves breaking access only; acquisition remains explicitly conditional.

Mapped source `Blocks` assigns nether gold ore hardness 3 and correct-tool drops.
The previously verified diamond-pick mechanism therefore gives ceil(3*30/8)=12
nominal ticks, or 0.6 seconds. Nether wart's registration sets no strength, leaving
`BlockBehaviour.Properties.destroyTime` at its default zero; its input is an
instant break, charged in targeting rather than an added mining-duration term.
`NetherWartBlock.SHAPE_BY_AGE[3]` is Block.box(0,0,0,16,14,16), and the registration
sets no collision. These are direct inspections of the pinned mapped server JAR,
SHA-256 26ca9c40d7e1681190b428583c38816852218e78df3f8bdb60a59a78503aec71.
Reproduce with the pinned `javap -c -p` on `net.minecraft.world.level.block.Blocks`,
`net.minecraft.world.level.block.NetherWartBlock`, and
`net.minecraft.world.level.block.state.BlockBehaviour$Properties` in that JAR.
The existing Circle source derivation supplies tool progress and magma behavior.

The route has 24 upright and two crouched blocks, including the full interior
return and resource return. Let u,c,n,a,s,k,v retain the accepted profile meanings.
Complete successful-scenario time is T=24/u+2/c+0.6+5n+2a+s+4k+v.
Combat contributes zero under the explicitly empty encounter condition. Decision
budgets include the two shift-pose transitions, without an additional latency term.

| Profile | Movement component | Complete task, seconds |
| --- | ---: | ---: |
| A | 6.13 | 15.98 |
| B | 7.67 | 26.77 |
| C | 10.22 | 45.32 |

Report approximately 16/27/45 seconds, conditional on the predeclared successful
resource pickup, actor and encounter conditions. This is not a confidence interval,
measured human time, typical expedition duration or guaranteed bound. Reproduce:

```sh
uv run python - <<'DOME_TIME'
for name,u,c,n,a,s,k,v in [('A',5,1.5,.5,.25,.25,1,2),
                          ('B',4,1.2,1,.5,.5,2,4),
                          ('C',3,.9,1.5,1,1,4,8)]:
    movement = 24/u + 2/c
    print(name, movement, movement + .6 + 5*n + 2*a + s + 4*k + v)
DOME_TIME
```

Room R1 is the single central ground activity volume inside the curved shell,
roughly X171..181, Z27..37, feet Y65; its footprint follows the shell, not the
rectangle. The central four trapdoors are decoration within this open volume,
not partitions. The verified northern route and an unobstructed cross-floor row
at Z30, X171..181, establish continuous use around them. That row has air at Y65/66
and full-cube floor throughout. Peripheral outdoor vegetation/resource patches
are not separately bounded rooms or arenas. Higher shell rings enclose the same
void; they do not supply additional activity floors, objectives or connections.
Roof standing through additional climbing/construction is not an authored room.

| Requirement | Local assessment and denominator |
| --- | --- |
| Rooms and branching | 1 room, 1 connected room component, 0 inter-room edges, junctions or cycles. The exterior is not an extra room. Alternative paths around decoration do not create room-graph branches. |
| Vertical progression | 0 ascent/descent and 0 floor-height span on the declared centerline. Pickup footing adjustments are covered conditionally, not a measured vertical route. No authored upper objective or activity floor is identified. |
| Depth | Deepest room graph depth 0 edges. Entry to declared interior station is 10 blocks, achieving its Manhattan lower bound. This is station depth, not a global maximum over every floor position. The 49-block surface-height difference remains context, not measured cover. |
| Enemies | 0 template-authored residents and spawners, 0 authored hostile types. Realized/natural populations NOT MEASURED. |
| Hazards | The resource route crosses magma at (176,64,23); shift avoidance makes it a meaningful, avoidable contact hazard. Soul-sand pickup footing is an explicit conditional allowance. Supported concrete powder on the inspected interior route is not a working trap. |
| Chokepoint | Northern entry cell (176,65,26) is a one-block-wide full-height air lane between the neighboring stair cells. A centered adult route passes. This is a conservative clear lane, not the exact widest opening after partial-shape optimization. The southern axis is obstructed; no live enemy exploitation is claimed. |
| Empty/dead rooms | R1 contains no supported authored encounter, hazard, reward or usable facility: 1 empty / 1 room. It is dead for a resource-only visit (1/1), because resources are outside. The stipulated survey task gives it an inspection purpose by definition (dead 0/1 under that task); this does not create an authored gameplay objective. |
| Loot distribution | 26 ore and 17 mature-wart positions are outside the central activity room, near Y64/65. No container or terminal reward. Two representative positions enter the acquisition model; remaining positions are potential, not proven harvested. |
| Finale | NONE. Authored objective clarity, distinctive terminal challenge, terminal reward linkage and route integration are ABSENT. External resource access is PRESENT for the two modeled targets. |
| Bypass/external access | Starting at the same northern entry, the six-block resource excursion can omit the twenty-block interior survey entirely, with identical harvest work and pickup conditions. No mining breach, flight or special capability is required. Thus the shell interior does not gate these rewards. |
| Replay | Fixed template gives no demonstrated authored layout/encounter variation. Natural terrain may vary access. Ore depletion persists; wart can support later cultivation under normal mechanics, which is a resource activity rather than a reset dungeon encounter. No player enjoyment or observed replay outcome is claimed. |
| Large but shallow | The 15-block-high authored shell surrounds one unchallenged ground activity volume, while the demonstrated rewards are outside and bypass its interior. This supports a visually substantial but mechanically shallow landmark assessment, not a conclusion drawn from volume or template count alone. |

This completes the local sampled assessment under the accepted conditional method.
It does not complete family repetitions, broader Item 13 coverage or delivery gates.
No human observation, realized combat or acquired loot has been manufactured.
