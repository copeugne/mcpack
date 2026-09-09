# Warped Dome: quality assessment

Status: IN PROGRESS. Saved/source content and visual layout are recorded;
playable room boundaries, access, routes and quality synthesis remain pending.

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

Next, establish a supported entry and central activity boundary using the saved
blocks and existing shape/source rules. Predeclare an actor, objective route,
resource interactions and failure handling before its timing or quality scoring.
Resolve magma/soul-sand exposure on that route and distinguish the shell's
visual height from connected progression. No inventory/classification repeat,
new machinery or world generation is justified by the current gaps. Item 14
remains UNSTARTED.
