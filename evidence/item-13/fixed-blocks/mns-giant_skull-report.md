# Giant Skull: quality assessment

Status: local sampled quality assessment recorded, including activity-space
sensitivity and complete conditional task timing. Family repetitions and Item 13
coverage/review/delivery remain IN PROGRESS.

Sample: full-mountainous-r1-baseline|minecraft:the_nether|mns:giant_skull|22|13.
The retained [saved blocks](mns-giant_skull.json.gz), SHA-256
5f16362e0a61c47c85c438b512ec0ef60afe81215a4130f0ba5af5ac134e2233,
contain 82,574 voxels, envelope [335,75,185,369,106,231], padded bounds
[332,72,182,372,109,234]. The original extraction retains archive/world identity,
full-section checks and the unchanged source selection. No new world read or
materialization is needed for these direct inspections.

## Source identity and saved content

The single rigid component has origin (335,75,185), rotation NONE and empty
processors. Source local (u,v,w) maps to (335+u,75+v,185+w). The existing
[versioned-component correction](../README.md#narrow-versioned-component-correction)
selects `mns:giant_skull` for Minecraft 1.21.1. Do not use the serialized fallback
`mns:1_21_9/giant_skull` as the active source. The latter contains the later
iron-chain identifier, while the retained version uses `minecraft:chain`.

Retained MoogsNetherStructures JAR SHA-256:
05024f18690436fff2fbc088f880a95cc30f23bacfe6e8058f6b02106032a990.
Active resource `data/mns/structure/giant_skull.nbt`, SHA-256
c299c175bf8ed3cd7a029bd57c3ab59703b0c80d5e8bc29c4da69c69e783c444,
has size 35x32x47, 3,160 placed block records and no entity entries. Those are
source construction facts, not rooms, depth, playable size or realized populations.

| Authored object | Saved correspondence | Interpretation |
| --- | --- | --- |
| Wither-skeleton spawner | (352,75,212), matching source (17,0,27) | 1 source, 1 explicit hostile type; no authored resident entity |
| Chest 1 | (356,75,205), matching source (21,0,20) | `mns:chests/uncommon` potential, not acquired contents |
| Chest 2 | (368,76,217), matching source (33,1,32) | Same table potential, different position and saved loot seed |
| Lava | All 61 authored positions retain lava: 37 at Y75, 20 at Y76, 4 at Y77 | Hazard ingredients with route exposure still to be resolved |
| Nether gold ore | All 54 authored positions match: 38 at Y75, 16 at Y76 | Material opportunity, not container loot |
| Nether wart | All 32 authored positions match: 23 at Y76, 9 at Y77 | Plant opportunity; no harvest observation |

The saved spawner retains Delay 160, SpawnCount 4, SpawnRange 4,
MaxNearbyEntities 6, RequiredPlayerRange 16, MinSpawnDelay 200,
MaxSpawnDelay 800 and empty SpawnPotentials. Its exact SpawnData ID is
`minecraft:wither_skeleton`. Four is a spawn-attempt batch parameter, not a
realized enemy count, success guarantee or lifetime population cap. A future
timing scenario must distinguish the saved initial delay from later batches.

Both chests retain LootTable rather than a measured acquired inventory. The source
`data/mns/loot_table/chests/uncommon.json`, SHA-256
f6729e4590d9ed6968f8e3e0be82b9fd826aa90561671379d484a508efb76b6f,
is in the same retained MNS JAR. Its weighted alternatives include tools,
ancient debris, netherite scrap, food and material supplies, plus separate optional
trim/upgrade-template pools. These are alternatives, not guaranteed rewards.
The saved chest seeds differ from the template seed. No table roll, effective
runtime modifier, opened inventory or acquired result is inferred here.

All 1,645 saved WORLD_SURFACE columns are Y127. The difference 127-106=21
above envelope top remains heightmap context, not a measured solid-cover depth.
The source object contains no implied extra floor merely because it is 32 blocks tall.

## Visual inspection and next bounded measurement

The existing renderer produced and the agent inspected all saved Y75..106 slices,
with a full-resolution crop for Y75..78. Ground-level objects sit amid lava/fire
and decoration; upper slices contain substantial terrain as well as the source
skull. Separate source attribution from saved terrain before counting rooms or
vertical progression. The renderer's categories are not collision shapes.

Reproduce the visual directly without committing a duplicate 13 MiB slice SVG:

```sh
uv run python -m evidence.item-13.render_pilot --input evidence/item-13/fixed-blocks/mns-giant_skull.json.gz --output /tmp/item13-skull-slices.svg
convert -background white /tmp/item13-skull-slices.svg /tmp/item13-skull-slices.png
convert /tmp/item13-skull-slices.png -crop 2108x780+0+0 +repage /tmp/item13-skull-ground.png
```

Next resolve supported ground routes to the spawner and both chests, chest opening
clearance, and whether skull cavities provide additional playable activity spaces.
Reuse the existing full-cube/partial-shape source rules. Predeclare the complete
objective and encounter lifecycle before timing. These checks use this retained
82,574-voxel sample only: budget one minute for direct geometry calculations,
512 MiB memory and under 1 MiB textual output, excluding the optional full-sheet
render above. No server, extraction or new world survey is authorized by this
local measurement declaration. Item 14 remains UNSTARTED.

## Ground reward access and covered spawner

Direct saved-block analysis resolves ground access to both chest stations from
(350.5,76,212.5). Admit only cells with air at Y76/77 over ordinary full-cube
netherrack, ore, wart block, gravel or obsidian at Y75. This deliberately excludes
lava, fire, plants, soul sand and partial shapes. It is a conservative route
subset, not a full navigation mesh or room-count proxy.

The first station (355.5,76,205.5) is reached in 12 horizontal blocks. The second
(369.5,76,217.5) has a 50-block path in this restricted subset, detouring north
and east around lava/decorative obstructions. These are independent access paths,
not the length of a complete two-chest task, nor a global shortest-path claim
that includes jumping or partial-block routes. Both paths remain inside the
retained padded bounds. Their full cell sequences reproduce below.

Chest 1's block above at (356,76,205) is air, as is Y77. Chest 2 has air directly
above at (368,77,217) and Y78. From the first station, aim at chest top-center
(356.5,75.875,205.5); from the second, aim at (368.5,76.5,217.5). Each segment
crosses air before entering the chest outline and is under three blocks long.
Opening access is thus supported under the declared source/geometry model;
menu operation and item transfer still need explicit timing allowances. No chest
was actually opened and no saved world was changed.

The spawner at (352,75,212) is covered by a double polished-deepslate slab at
Y76. Four neighboring bottom slabs occupy (351,76,212), (353,76,212),
(352,76,211), (352,76,213). Do not model direct unobstructed spawner mining from
the adjacent ground station. The complete task must account for this cover and
its approach/target geometry; an initial-delay rush cannot silently omit it.
This is a concrete mechanical obstruction, not a new generation or source gap.

```sh
uv run python - <<'SKULL_ACCESS'
import collections, gzip, hashlib, importlib, json
from pathlib import Path
raw = Path('evidence/item-13/fixed-blocks/mns-giant_skull.json.gz').read_bytes()
assert hashlib.sha256(raw).hexdigest() == '5f16362e0a61c47c85c438b512ec0ef60afe81215a4130f0ba5af5ac134e2233'
case = json.loads(gzip.decompress(raw))['cases'][0]
state = importlib.import_module('evidence.item-13.render_pilot').state_at
solid = {'minecraft:netherrack','minecraft:nether_gold_ore',
         'minecraft:nether_wart_block','minecraft:gravel',
         'minecraft:nether_quartz_ore','minecraft:obsidian'}
valid = {(x,z) for x in range(332,373) for z in range(182,235)
         if state(case,x,75,z)['Name'] in solid
         and all(state(case,x,y,z)['Name']=='minecraft:air' for y in (76,77))}
start = (350,212)
assert start in valid
queue = collections.deque([start]); previous = {start: None}
while queue:
    x,z = queue.popleft()
    for point in ((x+1,z),(x-1,z),(x,z+1),(x,z-1)):
        if point in valid and point not in previous:
            previous[point] = (x,z); queue.append(point)
for goal,expected in [((355,205),12),((369,217),50)]:
    point = goal; path = []
    while point is not None:
        path.append(point); point = previous[point]
    assert len(path)-1 == expected
    print(goal,expected,list(reversed(path)))
for x,y,z in [(356,76,205),(356,77,205),(368,77,217),(368,78,217)]:
    assert state(case,x,y,z)['Name']=='minecraft:air'
assert state(case,352,76,212) == {'Name':'minecraft:polished_deepslate_slab',
    'Properties':{'type':'double','waterlogged':'false'}}
SKULL_ACCESS
```

## Complete-task predeclaration

Use the accepted conditional accounting method with a fully informed single adult
at (350.5,76,212.5), full health/food, unenchanted iron armor/sword and diamond
pickaxe, and sufficient inventory for both chest results. Start the model at first
spawner activation with its saved Delay 160 and no pre-existing/natural hostiles.
This is a stipulated local starting state, not a reconstructed population history.

Objective: remove the west bottom slab and central double slab, disable the
spawner, defeat any hostiles it produced, transfer both chest inventories, and
return alive to the starting station. The two slab removals and spawner breaking
are permitted; no extra mining, construction, flight, healing, pre-applied effects, criticals,
sweeps or assistance. Ignore incidental slab drops and scattered ore/wart, which
are not the two-container expedition objective. Use 20 TPS throughout.

All three mining targets are approached from the starting station. Two initial
decision budgets cover orientation and breach sequence. Three targeting events,
one initial tool selection and actual breaking work must precede disablement.
Disable before 160 ticks to prevent the first attempt batch; if that deadline is
missed, allow one batch with successful count p=0..4, provided disablement still
occurs before 360 ticks. The latter conservatively precedes the earliest second
batch after the saved initial delay and minimum 200-tick reset. Do not treat
SpawnCount as a lifetime cap outside this condition.

For the full route use the verified 12-block start-to-first-chest path, a 40-block
first-to-second-chest path in the same conservative cell subset, and the reverse
50-block second-chest-to-start path: 102 upright blocks. The inter-chest path
starts west to (354,205), then follows the previously recorded northern/eastern
detour. That cell is step 11 of the retained 50-block path, so the remaining
39 blocks plus the one-block west move establish the 40-block inter-chest link.
Combat pursuit is excluded from these distances and included only in contact duty. No speed term is used for unverified pickup excursions.

Use A/B/C's existing speeds and allowances. Predeclare six decision events:
orientation, breach sequence, encounter confirmation, first-chest route/inspection,
second-chest route/inspection, and return. Three selections equip pickaxe, sword
for encounter confirmation/combat, and an empty hand for containers. Charge 61
targeting/interaction events: three mined blocks, two opens, two closes, and a
fixed scan/shift-click through all 27 slots of each chest. This is an explicitly
provisional inventory-operation budget, not a measurement of GUI performance or
an assertion that 54 slots contain loot. Two acquisition-confirmation allowances
check the transfers. Charge one final verification allowance. No ground-item pickup
or mining duration is charged again in the GUI budget.

Combat is source-based full-cycle iron-sword work for ordinary unarmored wither
skeletons, scaled by the accepted contact-duty profiles. Unmodeled modifiers, extra
armor/targets, pursuit outside the duty budget, death/healing, failed transfers,
mining interruptions beyond allowances, invalid access, disablement at/after
360 ticks or non-20-TPS conditions censor successful completion. No survival or
success probability is estimated. The method does not guarantee a successful rush.

## Covered-spawner access and complete conditional timing

The two permitted slab removals resolve the earlier obstruction without moving
onto partial blocks. From eye (350.5,77.62,212.5), target the west bottom slab at
(351.5,76.25,212.5), then the central double slab at (352.5,76.75,212.5), then the
spawner's top at (352.5,76,212.5). Target distances are approximately 1.70, 2.18
and 2.57 blocks. The first ray reaches the bottom slab; after its removal the
second crosses air and enters the double slab; after both removals the third
crosses the cleared cells and reaches the spawner top. No floor under the actor
is removed. Y77/78 over the relevant X350..352 cells is air. This is conditional
breach geometry, not a claim that the saved spawner was actually destroyed.

In the pinned mapped server JAR, `Blocks` copies polished-deepslate-slab properties
from polished deepslate, which copies cobbled deepslate. The latter sets strength
(3.5,6), so breaking hardness is 3.5. Both slab states use that same hardness;
a double slab is one block break, not two. The diamond-pick calculation is
ceil(3.5*30/8)=14 ticks per slab, plus the previously sourced 19-tick spawner:
47 nominal ticks or 2.35 seconds. Input and targeting remain separate budgets.

`DefaultAttributes` registers WITHER_SKELETON with `AbstractSkeleton.createAttributes`,
which changes movement speed but inherits max health 20. `Attributes.MAX_HEALTH`
defaults to 20. For the declared ordinary unarmored target and iron sword, four
full-strength six-damage hits require 4*13=52 nominal ticks, or 2.6 seconds of
active cycle work per target. These are source/model inputs, not actual hit or
kill observations. `WitherSkeleton.doHurtTarget` also applies WITHER for 200 ticks
after a successful hit on a living target. That pressure is not treated as harmless:
withering may occur, but survival without healing is a condition, not a modeled
guarantee. Extra delay outside the stated action/contact budgets censors the case.
The model contains no estimated incoming-damage or survival probability.

All these class derivations use mapped JAR SHA-256
26ca9c40d7e1681190b428583c38816852218e78df3f8bdb60a59a78503aec71;
inspect the named methods with the pinned `javap -c -p`. The retained Minecraft
pickaxe-mining tag includes `minecraft:polished_deepslate_slab`; no new tool or
runtime experiment is needed to reuse the already sourced breaking formula.

Disablement D=2.35+2n+3a+s gives A/B/C 4.35/6.35/9.35 seconds. A and B precede
the eight-second saved delay and therefore use p=0. C crosses the initial-delay
boundary and uses p=0..4 while remaining below the conservative 18-second second-
batch cutoff. A profile cannot be reported with an incompatible population just
because a different composition makes a more appealing result.

With the predeclared interaction counts, full successful-scenario time is:

T=102/u+2.35+6n+61a+3s+2k+v+2.6p/d.

| Profile | Movement only | Population scenario | Complete task, seconds |
| --- | ---: | --- | ---: |
| A | 20.40 | p=0, early disablement | 45.75 |
| B | 25.50 | p=0, early disablement | 73.85 |
| C | 34.00 | p=0..4, at most one batch | 125.35..146.15 |

Thus report approximately 46, 74, and 125..146 seconds under the stated profiles
and lifecycle. This is not a confidence interval, observed human performance,
expected natural population or guaranteed completion bound. Mining, route travel,
combat contact, decisions, all chest-slot interactions, acquisition confirmation
and final return verification are accounted for. The 102-block route alone is
not reported as complete timing.

Reproduce the arithmetic:

```sh
uv run python - <<'SKULL_TIME'
for name,u,n,a,s,k,v,d in [('A',5,.5,.25,.25,1,2,1),
                          ('B',4,1,.5,.5,2,4,.75),
                          ('C',3,1.5,1,1,4,8,.5)]:
    disable = 2.35+2*n+3*a+s
    assert disable < 18
    populations = [0] if disable < 8 else range(5)
    base = 102/u+2.35+6*n+61*a+3*s+2*k+v
    print(name,'disable',disable,'population/time',
          [(p,base+2.6*p/d) for p in populations])
SKULL_TIME
```

The complete-task budget and covered-spawner access feed the activity-space and
quality assessment below; timing alone does not establish those other dimensions.

## Activity-space judgment and quality synthesis

Use one covered mouth/under-skull activity space, R1, for the protocol's inclusive
activity-space count. Its approximate ground sector is X347..358, Z200..218 at
feet Y76, following the skull/jaw rather than filling that rectangle. The covered
spawner and first chest occupy this sector. The verified ground routes connect
them without an interior dividing wall. The second chest at (368,76,217) lies in
the exterior eastern reward sector, which has no separate enclosing room boundary.
Surrounding ore/wart patches and the terrain detour are not extra rooms.

R1 is semi-open, not a conventional enclosed chamber. Report sensitivity explicitly:
1 covered activity space under the adopted definition, 0 fully enclosed ground
rooms under a strict enclosure-only definition. Neither construction records nor
all air cells in a rectangular volume are counted as rooms. The shape above the
activity sector narrows and fills in upper slices; its rings/ledges do not establish
additional rooms. No upper authored enemy, container, usable facility or terminal
goal is present. Optional climbing onto sculptural surfaces is not evidence of a
separate authored progression floor; its exact parkour reach remains unmeasured.

Direct overhead attribution reinforces this distinction. Above the start station
(X350,Z212), non-air blocks inside the retained vertical range occur at Y85..88
and Y91..93; all seven match the active source's corresponding block names.
Above the first-chest station (X355,Z205), Y80 and Y88..93 likewise match the
source. These are sculptural overhead blocks, not measured natural burial cover.
Netherrack at Y109 over the first and second chest stations is outside the source
placement. The retained sample does not determine the whole roof thickness above
that level. Preserve that cover uncertainty rather than substituting the Y127
heightmap or counting the Nether roof as an authored upper floor.

| Requirement | Local result and evidence boundary |
| --- | --- |
| Room count | 1 covered activity space (R1); sensitivity 0 fully enclosed rooms. The eastern external cache is a reward sector, not an invented second room. |
| Branching | Adopted room graph: 1 node, 0 inter-room edges, junctions or cycles, 1 connected component. Under strict enclosure, the room graph is empty. The two reward stations and route turns are not room branches. |
| Vertical progression | Declared ground centerline remains at Y76: 0 ascent/descent and 0 floor-elevation span. Breaching is performed from the same floor. Two chest block elevations do not imply two playable floors. Optional sculptural climbing is not measured or needed for either chest. |
| Depth | Room-graph depth 0. Ground station distances are 12 blocks to the first chest and 50 to the second in the declared conservative route subset; the inter-chest link is 40. These are not global shortest paths over jumps/partial shapes. Entry and targets share the same actor-floor elevation, so there is no required descent. Natural roof thickness remains censored above retained Y109. |
| Traversal and combat | Complete conditional budgets above: approximately 46, 74, or 125..146 seconds. Movement-only components are 20.4/25.5/34 seconds. Authored combat work is 2.6p/d seconds, with p constrained by the spawner lifecycle. Human timing and realized combat remain NOT MEASURED. |
| Enemy count/diversity | No source-resident entities; one wither-skeleton spawner, one explicit authored hostile type. Realized count unknown. The conditional population is zero before initial-delay expiry or 0..4 after one permitted batch, not a general population cap. |
| Hazards | Authored lava lies across the direct eastern travel area and is avoided by the retained detour; fire is also excluded from its admitted cells. Lava is therefore a meaningful route-denial/contact hazard, not merely a palette entry. Successful wither-skeleton hits apply a source-supported 200-tick wither effect. Actual damage, pursuit and survival are not observed. |
| Chokepoints | No mandatory inter-room chokepoint exists in the adopted one-space graph. Lava/decorative obstacles constrain local ground travel, but the restricted-cell detour is not proof of a unique bottleneck or live AI exploit. The source slab cover constrains spawner targeting until two permitted breaks. |
| Empty/dead spaces | R1 contains encounter and reward potential: 0 empty / 1 and 0 dead / 1. Under strict enclosure both room denominators are 0, so ratios are NOT APPLICABLE, not 0 percent. No unvalidated upper cavity is added to inflate the denominator. |
| Loot distribution | One uncommon-table chest inside the covered activity sector and one in the eastern exterior sector, plus 54 source ore positions and 32 source wart positions. Container potential is spread across the site, not concentrated in a verified terminal room. Generated contents and acquired items remain NOT MEASURED. |
| Final-room quality | NONE as an authored terminal room. A visible landmark and local hostile source are present, but there is no source-supported terminal trigger, distinct final encounter or reward gate. The modeled clear-and-loot objective is analyst-declared, not an authored completion event. |
| Bypass/external access | Both chest stations can be visited on the retained ground routes without breaking the spawner cover or entering an upper skull cavity. Omitting the breach leaves the hostile source active and can change encounters, so this is access bypass with retained risk, not a cost-free combat-clear result. The early-disable scenario separately shows how two slab breaks can prevent the initial batch under its conditions. |
| Expected replay | Fixed sculpture and one fixed hostile type offer no demonstrated authored layout/encounter-composition variation. Table alternatives and natural terrain can change inputs. Revisiting a mined spawner/opened ordinary chest does not itself reset the physical site. No chest-refill mechanism or realized replay enjoyment is established here. |
| Visually large but shallow | The 32-block-high sculpture supports one ground activity sector and no demonstrated upper objective progression. The 102-block task route is largely a hazard/terrain detour and must not be mistaken for many rooms. This supports a large landmark with shallow authored topology, while retaining meaningful lava exposure, breach effort and conditional hostile pressure. |

The local sampled quality assessment is now recorded across all Item 13 dimensions.
This is not completion of family repetitions, material coverage or the final
review/delivery gate. Roof-thickness and optional parkour limits remain explicit;
no human session, spawned population, inventory transfer or successful clear was
fabricated to resolve them.
