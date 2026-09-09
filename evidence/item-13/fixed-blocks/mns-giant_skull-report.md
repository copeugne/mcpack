# Giant Skull: quality assessment

Status: IN PROGRESS. Source/saved content, visual evidence and ground chest
access are integrated. Playable activity boundaries, covered-spawner access,
full task budget and quality synthesis remain open.

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
