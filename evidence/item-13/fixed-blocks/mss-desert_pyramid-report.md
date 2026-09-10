# Desert Pyramid: quality assessment

Status: IN PROGRESS. Active component assembly and source/saved encounter and
reward inputs are integrated. Playable topology, full timing and quality synthesis
remain required. Item 14 stays UNSTARTED.

Sample: full-biome-diverse-r2-baseline|minecraft:overworld|mss:desert_pyramid|8|29.
Reuse [saved blocks](mss-desert_pyramid.json.gz), SHA-256
7dfc8e4d500459ad0839137e3939e9ee19df3a6b3cf1c7ae709b2711f8eb43a4.
This 17,911-byte compressed extraction retains 219,834 padded voxels, envelope
[99,134,440,151,196,487] and bounds [96,131,437,154,199,490]. Existing extraction
and custody records retain the accepted world identity and full chunk coverage.
No regeneration, new world read or runtime experiment is part of this intake.

## Active source assembly

Retained MoogsSoaringStructures-1.21-2.1.2.jar SHA-256:
5392b23878488bf167669b9d9eb0ed3b129115155856ac28059e88d8ac9b0080.
Resolve the base's saved version map using the frozen Minecraft 1.21.1 entry,
`1.21-1.21.8 -> mss:desert_pyramid`, not its later-version location field.
All three saved components are rigid, CLOCKWISE_90, with empty processors.

| Active resource under data/mss/structure/ | Source size | Saved origin | Resource SHA-256 |
| --- | --- | --- | --- |
| desert_pyramid.nbt | 48x48x48 | (151,134,440) | 0291712faf6811316e199888b1a6c1144a849296c3b14286ada557a46c6b5b70 |
| desert_pyramid_top.nbt | 48x15x48 | (151,182,440) | 1f004da3ed8bb53ef3615c58d29209707753e02bb597c88e1914d5c835da29cd |
| desert_pyramid_side.nbt | 17x8x5 | (103,175,454) | fd366e332a22e46e2e05352f91e93abd30aeebbfef561a2c7a9c8e2cc80f6186 |

For each origin (ox,oy,oz), source local (u,v,w) maps to (ox-w,oy+v,oz+u).
All three source entity lists are empty. Base contributes ten spawners and two
chest blocks; top contributes one spawner and two chest blocks; side contributes
neither. Component counts and saved junction offsets are assembly evidence, not
room counts, stair connectivity or dungeon depth.

## Enemy sources and unresolved realized population

All eleven source spawner positions and their SpawnData, SpawnPotentials, Delay,
SpawnCount, Min/MaxSpawnDelay, RequiredPlayerRange, MaxNearbyEntities and SpawnRange
match the saved payloads. Preserve their saved `minecraft:mob_spawner` block-entity
id; no raw normalization or replacement is performed.

| Position | Authored entity | Initial Delay, ticks |
| --- | --- | ---: |
| (110,181,464) | zombie | 0 |
| (111,178,449) | zombie | 0 |
| (114,178,454) | husk | 0 |
| (116,178,443) | husk | 0 |
| (118,180,467) | husk | 0 |
| (123,171,459) | zombie | 0 |
| (126,171,457) | zombie | 0 |
| (126,177,465) | husk | 0 |
| (127,178,450) | zombie | 169 |
| (132,181,481) | husk | 0 |
| (133,182,461) | husk | 0 |

All use SpawnCount 4, SpawnRange 4, RequiredPlayerRange 16, MaxNearbyEntities 6,
MinSpawnDelay 200, MaxSpawnDelay 800 and empty SpawnPotentials. This establishes
five zombie and six husk sources, two explicitly assigned types and zero source
residents. It does not establish 44 realized enemies or a one-wave lifetime cap.
Activation windows and permitted repetitions depend on the eventual route; no
combat time is assigned until those conditions and husk source mechanics are
resolved. Natural mobs and actual encounters remain NOT MEASURED.

## Reward blocks, paired containers and potential

All four source LootTable assignments match the saved records:

| Saved position | Saved chest state | Table |
| --- | --- | --- |
| (115,177,445) | single, south-facing | mss:rare |
| (115,177,452) | single, north-facing | mss:rare |
| (120,182,453) | left, north-facing | mss:general |
| (121,182,453) | right, north-facing | mss:general |

The adjacent left/right pair is one double-chest arrangement. Use four authored
loot-bearing block entities and three container arrangements as separate
denominators. A successful paired opening would expose 54 slots, not two unrelated
27-slot interactions. Pair/lid access and actual runtime opening still require
inspection. Stored LootTableSeed values do not establish rolled contents.

Packaged table `data/mss/loot_table/rare.json`, SHA-256
ddb3f6cf10bda5bacb1aa8d84db1be25bc1e916fe35f75fad80a2705b89201c3,
has one 3..7-roll uniform pool with 27 weighted entries, including diamond/iron/
gold/emerald, apples, netherite scrap, totem, heart of the sea, saddle/horse armor,
trident, equipment and book alternatives. This is potential, not a guaranteed
rare item or generated value. `general.json`, SHA-256
eb37851c0db1093cede4e0fdbab30378d766235a41dc2fe79d87d1e61038ec4f,
has three pools: 1..3 mineral rolls, 2..4 provision/material rolls and 0..1 rolls
from an empty-or-item bonus pool. Keep the two halves' assignments distinct even
when counting one paired container arrangement.

Five saved decorated pots have no item or LootTable field: (113,177,446),
(117,177,451), (122,177,448), (125,177,470), (126,172,454). They are not additional
authored loot nodes from this evidence. The three skull block entities likewise
do not constitute source-resident enemies. Actual generated/acquired loot remains
NOT MEASURED.

Reproduce correspondence with the existing NBT decoder on the named immutable
resources, transform source positions with each saved origin, and compare fields
against `block_entities` in the hash-bound extraction. Use `render_pilot.state_at`
for the four saved chest states. No new helper, validator or runtime probe is
required for these direct source/saved facts.

## Next bounded topology measurement

Inspect actual saved floor/body cells and a slice view before deriving rooms or
paths. Priorities are the side-component entrance, the Y171..182 spawner/reward
bands, their vertical connections, chest pairing/lid clearance and any meaningful
trap mechanism. A 63-block envelope height or three components is not playable
depth. Use the approved complete-task accounting after the route is validated.

Direct read-only queries: one minute, 512 MiB and under 1 MiB textual output.
A 63-layer envelope sheet uses the retained 219,834-voxel padded extraction; allow
one bounded render up to 180 seconds and at most 60 MiB SVG/PNG output, reflecting
its larger footprint than the prior tower. Preserve timeout or overrun rather
than repeatedly rerunning it. Reuse the existing renderer and extraction; no new
world generation, server work or evidence re-extraction is planned.

## Side-component disposition and husk model inputs

Inspection corrects the provisional entrance priority: the side component is not
an established doorway. Its complete active source has 486 air, 162 sandstone,
23 sand, seven stone, one dead bush and one jigsaw blocks. This is a terrain
appendage with no source reward or enemy, not evidence of a playable room or
entrance merely because its resource is named `side`. Saved Y175..179 sections
in that region are predominantly solid. Find the actual access through occupied
floor/body geometry rather than treating the component junction as a door.

Pinned mapped source supports a husk-specific nominal combat input without a
new runtime experiment. `DefaultAttributes` offsets 405..414 register HUSK using
`Zombie.createAttributes`. Reuse the established health 20, intrinsic armor 2
and iron-sword damage derivation in the model-source notes: ordinary unarmored
adults receive 5.904 nominal damage per full attack and require four hits, or
2.6 seconds of reserved 13-tick attack cycles. This is active attack work per
entity, not total combat time or a prediction of encounter count.

`Husk` extends Zombie, returns false from `isSunSensitive`, and applies HUNGER
when `doHurtTarget` succeeds with an empty main hand against a living target.
Its source duration is 140 times the integer effective local difficulty, in
game ticks. Do not assume an observed hunger duration or food consumption here.
`checkHuskSpawnRules` accepts spawner origin without the additional sky-visibility
condition required for its non-spawner branch; it still calls the underlying
monster spawn checks. This does not guarantee a successful attempt in these rooms.
These differences support two assigned enemy types, even though the nominal
per-entity attack-cycle workload matches. Actual sunlight exposure, hunger hits,
reinforcements, equipment, survival and realized populations remain unobserved.

Reproduce these source facts with `javap -c -p` on `Husk` and `DefaultAttributes`
in the already pinned mapped server JAR. They resolve the missing husk mechanism
input; route activation and repeated-spawn accounting are still required before
complete conditional timing can be declared.

A bounded full-envelope block-name query finds 39 vanilla cactus blocks and ten
`biomesoplenty:tiny_cactus` blocks. It finds no TNT, pressure plate, tripwire,
redstone, lava, fire or dispenser block. This rejects an assumed vanilla-pyramid
TNT trap for this retained envelope; it does not prove all gameplay hazards absent.
Cactus contact relevance and the modded tiny-cactus behavior require route/source
support before hazard scoring. No trigger or damage observation is fabricated.

## Preserved full-sheet render timeout

The first predeclared full-sheet attempt failed at the 180-second conversion
limit, exit 124. Bash timing: real 180.02, user 187.22, system 1.09 seconds.
The SVG producer completed and wrote 36,017,200 bytes; the converter did not
return a successful image. No rendered-sheet inspection or complete visual
validation is claimed from this attempt. A live RSS snapshot during conversion
was 563,464 KiB, not a measured peak. The source extraction is unchanged.

Exact reproduction command:

```sh
uv run python -m evidence.item-13.render_pilot --input evidence/item-13/fixed-blocks/mss-desert_pyramid.json.gz --output /tmp/item13-desert-pyramid-slices.svg
time -p timeout 180 convert -background white /tmp/item13-desert-pyramid-slices.svg /tmp/item13-desert-pyramid-slices.png
```

Do not rerun the unchanged full conversion. The 63-layer conversion exceeded
its time budget; the raw blocks are already retained. Continue direct saved-block inspection
and use a bounded sectional view for the relevant Y171..182 activity band. Any
renderer adjustment must remain confined to selecting explicit layers in the
existing path, retaining raw identity and default behavior; no second renderer
or new evidence framework is justified. This is a visualization failure, not a
failed generated-world sample or permission to omit uninspected topology.

## Bounded sectional-render correction

The full-sheet timeout justifies one narrow change to the existing renderer:
`--layers` accepts explicit unique Y heights within the saved envelope. Its panels
retain actual coordinates and original raw-file hash, and label the view as
selected layers only. Omission preserves default output byte for byte. Empty,
duplicate and out-of-envelope selections are rejected; no new renderer or raw
extraction is introduced.

Predeclare a sixteen-layer Y169..184 view, bracketing the Y171..182 activity band.
Allow one 180-second conversion and 24 MiB combined SVG/PNG output. Other levels
remain available for direct inspection and are not silently declared inspected.
This targeted visualization resolves the demonstrated full-sheet budget failure.

Focused validation verified default Nether Tower SVG bytes unchanged against its
previous render, selection labels and original input hash, and rejection of empty,
duplicate and out-of-envelope layers. Ruff lint/formatting pass. The initial type
command mistakenly used unavailable `pyright`; use the configured `basedpyright`.
The configured focused type check passes with zero errors/warnings/notes.
Reproduce the focused boundary/default checks without converting an image:

```sh
uv run ruff check evidence/item-13/render_pilot.py
uv run ruff format --check evidence/item-13/render_pilot.py
uv run basedpyright evidence/item-13/render_pilot.py
uv run python - <<'LAYER_CHECK'
import hashlib, importlib, subprocess, tempfile
from pathlib import Path
current = importlib.import_module('evidence.item-13.render_pilot')
prior = {'__file__': current.__file__, '__name__': 'prior_renderer'}
code = subprocess.check_output(['git','show','28ac65c9:evidence/item-13/render_pilot.py'])
exec(compile(code,'prior renderer','exec'),prior)
source = Path('evidence/item-13/fixed-blocks/mns-nether_tower.json.gz')
with tempfile.TemporaryDirectory() as directory:
    old, new = Path(directory)/'old.svg', Path(directory)/'new.svg'
    prior['render_slices'](source,old)
    current.render_slices(source,new)
    assert old.read_bytes()==new.read_bytes()
    current.render_slices(source,new,layers=[55,75])
    text = new.read_text()
    assert 'Selected layers only: 55, 75' in text
    assert 'Y=55;' in text and 'Y=75;' in text and 'Y=56;' not in text
    assert hashlib.sha256(source.read_bytes()).hexdigest() in text
    for invalid in ([],[55,55],[50],[97]):
        try:
            current.render_slices(source,new,layers=invalid)
        except ValueError:
            continue
        raise AssertionError(invalid)
print('Layer selection and unchanged default verified.')
LAYER_CHECK
```

The first sectional conversion completed in 14.82 seconds (user 14.35, system
0.78), producing 150,578 PNG bytes and 9,207,469 SVG bytes. Visual inspection
found the selected-layer caption overlapped the first row's labels. Preserve
that [rejected presentation](mss-desert_pyramid-169-184-header-overlap.png).
The narrow fix gives selected views fifteen more header pixels, leaving default
rendering unchanged. This defect justified one corrected conversion, not a retry
of the timed-out full sheet.

The [corrected Y169..184 sheet](mss-desert_pyramid-169-184.png) completed in
37.78 seconds (user 35.18, system 1.88), with clean exit. It is 150,773 bytes at
2972x2882 pixels; SVG is 9,208,181 bytes, combined 9,358,954 bytes. Both conversions
fit their declared time/storage budgets. The agent inspected the corrected sheet
and confirmed that the caption and row labels no longer overlap. Focused default,
selection-boundary, lint, formatting and type checks pass after the fix.

Reproduce the accepted selected view:

```sh
uv run python -m evidence.item-13.render_pilot --input evidence/item-13/fixed-blocks/mss-desert_pyramid.json.gz --output /tmp/item13-pyramid-169-184.svg --layers 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184
time -p timeout 180 convert -background white /tmp/item13-pyramid-169-184.svg /tmp/item13-pyramid-169-184.png
```

The selected slices expose a narrow buried cavity/connection band and the rare
chest area at Y177/178, plus surface reward geometry at Y182. Much of the lower
selected footprint is solid. These are visual leads for exact floor/body queries,
not room counts or proof that the apparent connections fit an actor. Continue
with access from the upper surface into the buried corridor and the lower Y171
sources. Unselected Y134..168 and Y185..196 remain outside this visual inspection;
they must not be represented as reviewed merely because their raw bytes exist.

## Native entrance stair and buried corridor

Direct saved-block inspection resolves a native passage from (114.5,182,469.5)
to (124.5,177,469.5). It contains 10 horizontal blocks and five blocks of vertical
descent. At Z469, the stair cells are (115,181), (116,180), (120,179), (121,178)
and (122,177), expressed as (X,Y). All five are bottom, straight, west-facing,
non-waterlogged sandstone stairs. Their source-shape model combines a whole-cell
bottom half with a west-half upper half. The intermediate full floors are X114
at Y181, X117..119 at Y179, and X123..124 at Y176. A 0.6-wide, 1.8-high actor
therefore encounters half-block support changes, within the declared 0.6 step
limit. The center lane has sufficient headroom throughout. This establishes a
reversible modeled stair connection without mining, doors or ladders. It is not
a timed traversal or runtime actor observation.

The claim is specifically the Z469.5 centerline. The adjacent lanes contain
fences and pots; do not generalize it to three unobstructed lanes. A preliminary
1,001-position support/headroom sample passed. The reproduction below replaces
sampling with finite critical intervals: support and intersected block columns
can change only at collision-box edges shifted by the actor half-width. Testing
those boundaries and each interval midpoint checks the entire declared centerline
under this source-shape model. It does not validate actor-context equivalence.

From the lower endpoint, X124.5 at feet Y177 continues six blocks north to
Z463.5 on full sandstone floors with air at Y177/178. At Z462 a two-cell-high
fence occupies X124, so the straight centerline does not continue through it.
The adjacent X125 corridor has air at Y177/178 and full support at Y176 through
Z462. A north-facing ladder at (125,Y172..176,461), backed by the Z462 wall,
provides a concrete lead for the deeper chamber. Its approach, climbing contact
and lower landing remain to be validated before adding a graph edge.

The upper paired chest has air immediately above both halves at Y183. Its north
face borders water at Y181 in X120..121,Z452, rather than a full dry standing
floor. Side sandstone walls also constrain approach. Thus clear lids alone do
not yet prove the declared actor can reach/open this double container. Preserve
that distinction when completing its route and acquisition budget.

Reproduce the stair and corridor derivation from the hash-bound extraction:

```sh
uv run python - <<'PYRAMID_STAIRS'
import gzip, hashlib, importlib, json
from fractions import Fraction as F
from pathlib import Path
p = Path('evidence/item-13/fixed-blocks/mss-desert_pyramid.json.gz')
assert hashlib.sha256(p.read_bytes()).hexdigest() == '7dfc8e4d500459ad0839137e3939e9ee19df3a6b3cf1c7ae709b2711f8eb43a4'
c = json.loads(gzip.decompress(p.read_bytes()))['cases'][0]
s = importlib.import_module('evidence.item-13.render_pilot').state_at
floor = {114:181,115:181,116:180,117:179,118:179,119:179,
         120:179,121:178,122:177,123:176,124:176}
boxes = []
for x, y in floor.items():
    state = s(c,x,y,469)
    if state['Name'] == 'minecraft:sandstone_stairs':
        assert state['Properties'] == dict(facing='west',half='bottom',
                                          shape='straight',waterlogged='false')
        boxes += [(F(x),F(x+1),F(y)+F(1,2)),
                  (F(x),F(x)+F(1,2),F(y+1))]
    else:
        assert state['Name'] in ('minecraft:sandstone','minecraft:smooth_sandstone')
        boxes += [(F(x),F(x+1),F(y+1))]
a,b,r = F(229,2),F(249,2),F(3,10)
points = sorted({a,b} | {v+d for lo,hi,_ in boxes for v in (lo,hi)
                        for d in (-r,r) if a <= v+d <= b})
probes = sorted(set(points + [(u+v)/2 for u,v in zip(points,points[1:])]))
levels = []
for x in probes:
    feet = max(top for lo,hi,top in boxes if x+r>lo and x-r<hi)
    for bx,y0 in floor.items():
        if x+r<=bx or x-r>=bx+1:
            continue
        for y in range(y0+1,185):
            if y<feet+F(9,5) and y+1>feet:
                assert s(c,bx,y,469)['Name']=='minecraft:air', (x,bx,y)
    levels.append(feet)
assert levels[0]==182 and levels[-1]==177
assert all(abs(u-v)<=F(1,2) for u,v in zip(levels,levels[1:]))
for z in range(463,470):
    assert s(c,124,176,z)['Name'] in ('minecraft:sandstone','minecraft:smooth_sandstone')
    assert all(s(c,124,y,z)['Name']=='minecraft:air' for y in (177,178))
print('Stair critical intervals and six-block lower corridor pass.')
PYRAMID_STAIRS
```

## Lower ladder and upper double-chest access

The deeper connection now has a source-supported route. From the preceding
corridor endpoint (124.5,177,463.5), move east to X125.5, north through Z462.5 to
the ladder center Z461.5, descend to feet Y172, then move east to the clear
landing (126.5,172,461.5). This adds four horizontal and five vertical blocks.
The five existing ladders occupy (125,Y172..176,461), face north, and have full
sandstone/smooth-sandstone backing at Z462. Reuse the pinned ladder/climbable
source identity and transfer model in the
[Large House report](mns-large_house_1-report.md#conditional-connections-with-explicit-construction-costs).
A north-facing ladder's blocking plate occupies the southern 3/16 of its cell;
the centered actor's Z461.2..461.8 body stays north of that plate, while its feet
occupy the climbable block. Air at Y177/178 permits the top transfer. Full floors
at Y171 support the ladder center and east landing; the latter has air at Y172/173.
This is a reversible native modeled link, with no block changes. A runtime climb
has not been observed. The remaining chamber contains pointed dripstone and
other obstacles; a clear landing does not establish unrestricted floor access.

For the upper double chest, use the dry station (119.5,182,452.5), eye
(119.5,183.62,452.5), and aim at (120.5,182.5,453.0625), the north face of its
western half. The interaction ray is approximately 1.603 blocks, below the
three-block modeled reach. It crosses Z453 only after X120, so it avoids the
sandstone wall at X119,Z453. Before that crossing, intersected body-level cells
are air. The target is the first chest face; water below feet level does not
intercept the ray. Both halves have air above, mutually consistent north-facing
left/right states, the same chest block type, and no saved Lock field. Under the
existing no-blocking-entity and unlocked-container scenario, this supports one
54-slot opening. No GUI opening, rolled loot or acquired loot was observed.
The dry station also connects west six blocks to (113.5,182,452.5) on full-height
saved sand/sandstone floors with clear body cells. Connecting that surface strip
to the full objective circuit remains required before timing synthesis.

Reproduce these local block conditions using the same hash-bound extraction and
`state_at` helper as the preceding command:

```sh
uv run python - <<'PYRAMID_ACCESS'
import gzip, hashlib, importlib, json, math
from pathlib import Path
p=Path('evidence/item-13/fixed-blocks/mss-desert_pyramid.json.gz')
assert hashlib.sha256(p.read_bytes()).hexdigest()=='7dfc8e4d500459ad0839137e3939e9ee19df3a6b3cf1c7ae709b2711f8eb43a4'
c=json.loads(gzip.decompress(p.read_bytes()))['cases'][0]
s=importlib.import_module('evidence.item-13.render_pilot').state_at
full={'minecraft:sandstone','minecraft:smooth_sandstone','minecraft:sand'}
for y in range(172,177):
    assert s(c,125,y,461)=={'Name':'minecraft:ladder','Properties':{'facing':'north','waterlogged':'false'}}
    assert s(c,125,y,462)['Name'] in full
for x,z in ((124,463),(125,463),(125,462)):
    assert s(c,x,176,z)['Name'] in full
    assert all(s(c,x,y,z)['Name']=='minecraft:air' for y in (177,178))
for y in (177,178):
    assert s(c,125,y,461)['Name']=='minecraft:air'
for x in (125,126):
    assert s(c,x,171,461)['Name'] in full
assert all(s(c,126,y,461)['Name']=='minecraft:air' for y in (172,173))
for x in range(113,120):
    assert s(c,x,181,452)['Name'] in full
    assert all(s(c,x,y,452)['Name']=='minecraft:air' for y in (182,183))
for x,kind in ((120,'left'),(121,'right')):
    assert s(c,x,182,453)=={'Name':'minecraft:chest','Properties':{'facing':'north','type':kind,'waterlogged':'false'}}
    assert s(c,x,183,453)['Name']=='minecraft:air'
    be=next(b for b in c['block_entities'] if (b.get('x'),b.get('y'),b.get('z'))==(x,182,453))
    assert 'Lock' not in be
assert s(c,120,182,452)['Name']=='minecraft:air'
assert s(c,120,183,452)['Name']=='minecraft:air'
length=math.dist((119.5,183.62,452.5),(120.5,182.5,453.0625))
assert length<3
print(f'Ladder/landing and dry chest access conditions pass; ray {length:.6f} blocks.')
PYRAMID_ACCESS
```

## Lower chamber: source access and stalagmite hazard

The lower activity space occupies interior X123..126,Z453..461 above its Y171
floor. Its two zombie spawners are embedded in that floor at (126,171,457) and
(123,171,459). The saved chamber has 23 pointed-dripstone blocks in Y172..178:
17 upward tips, five upward frustums and one upward base, with no downward
stalactites in that inspected volume. These are collision/hazard ingredients,
not 23 independent hazards or enemies. There is no loot-table container in this
lower space; the decorated pot at (126,172,454) has no stored item or LootTable,
as recorded in the intake. The source pair makes this an encounter-bearing
space rather than an empty room even though realized spawning is unmeasured.

The pinned mapped `PointedDripstoneBlock.fallOn` applies
`causeFallDamage(fallDistance + 2, 2, damageSources.stalagmite())` when direction
is UP and thickness TIP. Other states delegate to the base block. This supports
an amplified fall-on-tip hazard, not damage merely from standing near a spike.
The chamber's ladder gives an alternative to jumping down among those tips.
Falling-stalactite damage is not established here: no downward state is present
in the inspected chamber. The full Pyramid may have other hazards outside this
volume. Reproduce the mechanism with the pinned mapped JAR SHA-256
26ca9c40d7e1681190b428583c38816852218e78df3f8bdb60a59a78503aec71:

```sh
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -classpath instances/pristine-baseline-v0/libraries/net/minecraft/server/1.21.1-20240808.144430/server-1.21.1-20240808.144430-srg.jar -c -p net.minecraft.world.level.block.PointedDripstoneBlock
```

Predeclare a small engineering bypass for source access. From the ladder's east
landing (126.5,172,461.5), move north to Z458.5, then west to X123.5. Remove the
skeleton skull at (126,172,459), four-candle block at (126,172,458), and two-candle
block at (123,172,458) before entering their cells. Each is accessible from the
preceding adjacent clear cell: respectively (126.5,172,460.5),
(126.5,172,459.5), and (124.5,172,458.5). Aim at their top centers, with modeled
eye Y173.62. Candle targets use Y172.375 at the block X/Z center. Pinned
`CandleBlock` TWO_AABB is (5,0,6)..(11,6,9)/16 and FOUR_AABB is
(5,0,5)..(11,6,10)/16, so those target points lie on the top face. Reproduce
these constants with the same `javap` command, substituting `CandleBlock`.
Each target is within two blocks, with air above it and no preceding
intercepting block on that local ray. This removes three decorative blocks,
not three stalagmites. Their breaking and selection costs remain to be included
in the complete task budget; they are not treated as free actions.

After those explicit removals, the six-block L-shaped route has full support at
Y171 and clear body cells Y172/173. It avoids all spike cells. From the eastern
endpoint (126.5,172,458.5), target the first spawner's top center
(126.5,172,457.5); from the western endpoint (123.5,172,458.5), target the second
at (123.5,172,459.5). Both rays are about 1.904 blocks and reach exposed top faces
without standing on the spawners. Removing them therefore does not remove route
support. Reverse the same six blocks to return to the ladder landing. This
establishes conditional access to both lower sources, not combat success or a
claim that the untouched chamber is freely walkable. No saved block was changed.

Reproduce the saved route and hazard ingredients:

```sh
uv run python - <<'PYRAMID_CHAMBER'
import collections, gzip, hashlib, importlib, json, math
from pathlib import Path
p=Path('evidence/item-13/fixed-blocks/mss-desert_pyramid.json.gz')
assert hashlib.sha256(p.read_bytes()).hexdigest()=='7dfc8e4d500459ad0839137e3939e9ee19df3a6b3cf1c7ae709b2711f8eb43a4'
c=json.loads(gzip.decompress(p.read_bytes()))['cases'][0]
s=importlib.import_module('evidence.item-13.render_pilot').state_at
removed={(126,172,459):'minecraft:skeleton_skull',
         (126,172,458):'minecraft:light_gray_candle',
         (123,172,458):'minecraft:light_gray_candle'}
for xyz,name in removed.items():
    assert s(c,*xyz)['Name']==name
route={(126,z) for z in range(458,462)} | {(x,458) for x in range(123,127)}
for x,z in route:
    assert s(c,x,171,z)['Name'] in ('minecraft:sandstone','minecraft:smooth_sandstone')
    for y in (172,173):
        assert (x,y,z) in removed or s(c,x,y,z)['Name']=='minecraft:air'
for x,z in ((126,457),(123,459)):
    assert s(c,x,171,z)['Name']=='minecraft:spawner'
    assert all(s(c,x,y,z)['Name']=='minecraft:air' for y in (172,173))
counts=collections.Counter()
for x in range(123,127):
    for z in range(453,462):
        for y in range(172,179):
            state=s(c,x,y,z)
            if state['Name']=='minecraft:pointed_dripstone':
                props=state['Properties']
                counts[props['vertical_direction'],props['thickness']]+=1
assert counts=={('up','tip'):17,('up','frustum'):5,('up','base'):1}
print('Lower source-access route passes after three declared removals.', dict(counts))
print('Spawner interaction ray:', math.hypot(1,1.62))
PYRAMID_CHAMBER
```

## Upper corridor gap and declared bridge

The reward corridor north of the lower chamber resumes at (125.5,177,452.5).
It does not have a continuous native floor back to the southern ladder landing
(125.5,177,462.5). Along X125,Y176,Z453..460 all eight cells are air; Z461
contains the existing top ladder. All nine cells have air at Y177/178. Therefore
an air-only route query at feet Y177 would incorrectly accept a walk across the
chamber. This is a specific support failure, not proof that no other native or
parkour route exists anywhere in the Pyramid.

Predeclare the following connector for the complete engineering objective, after
finishing the lower chamber and returning up its ladder. Remove the top ladder
at (125,176,461), then place nine cobblestone blocks at (125,176,Z453..461).
The remaining lower ladder is retained but its original top transfer is changed;
do not reuse the untouched-ladder route after this modification without assessing
that changed state. The declared objective visits the lower chamber first, so
no later lower transfer is required by this route.

From the south landing the top ladder is reachable at its upper plate, with no
intercepting block above it. For bridge construction, use the existing crouched
edge-placement model: feet Y177, eye Y178.27, X125.5, center Z=k-0.1 for support
cell Z=k, beginning k=462. The body retains 0.2 blocks of horizontal overlap with
that support. Aim at its north face (125.5,176.5,k); the 1.773-block ray approaches
the exposed face through the next empty cell and places the new block at Z=k-1.
Repeat k=462 down through 454. Each newly placed cell supplies the next support;
body and eye remain below the ceiling and above the placed floor. The actor is
stipulated to crouch and place successfully, with no entity interference, as in
the approved engineering model. This is not an observed build.

The completed crossing is ten horizontal blocks from Z462.5 to Z452.5 at feet
Y177, including the two half-cell approaches. Charge one ladder removal, nine
placements, selection/decision allowances and crouched movement in the eventual
complete timing model. No world/configuration edits were performed. The bridge
bypasses the chamber's fall exposure while the separately assessed lower route
still supplies its two-source objective. Both are conditional engineering
choices, not evidence of authored protection or a reason to prohibit bridging.

The northern landing connects on saved full-height floors through X125,Z452..449,
then west along Z449 to X117. The intervening body cells are air. This supplies
eleven further horizontal blocks to (117.5,177,449.5), at the eastern edge of the
rare-chest activity area. Its central chiseled-sandstone blocks at X114..116,
Z448..449 occupy Y177 and must not be mistaken for open floor-level cells.

Reproduce the gap and northern corridor from the retained extraction:

```sh
uv run python - <<'PYRAMID_BRIDGE'
import gzip, hashlib, importlib, json
from pathlib import Path
p=Path('evidence/item-13/fixed-blocks/mss-desert_pyramid.json.gz')
assert hashlib.sha256(p.read_bytes()).hexdigest()=='7dfc8e4d500459ad0839137e3939e9ee19df3a6b3cf1c7ae709b2711f8eb43a4'
c=json.loads(gzip.decompress(p.read_bytes()))['cases'][0]
s=importlib.import_module('evidence.item-13.render_pilot').state_at
for z in range(453,462):
    assert s(c,125,176,z)['Name']==('minecraft:ladder' if z==461 else 'minecraft:air')
    assert all(s(c,125,y,z)['Name']=='minecraft:air' for y in (177,178))
route={(125,z) for z in range(449,453)} | {(x,449) for x in range(117,126)}
for x,z in route | {(125,462)}:
    assert s(c,x,176,z)['Name'] in ('minecraft:sandstone','minecraft:smooth_sandstone','minecraft:sand')
    assert all(s(c,x,y,z)['Name']=='minecraft:air' for y in (177,178))
print('Nine-cell unsupported crossing and northern floor/body conditions verified.')
PYRAMID_BRIDGE
```

## Rare-chest room: native circuit and three recessed sources

From the northern corridor endpoint (117.5,177,449.5), the following circuit
returns to that endpoint after visiting both rare chests and three recessed
spawners. All listed coordinates are block-column (X,Z); add 0.5 for the actor
center and use feet Y177 throughout:

```text
(117,449) -> (117,447) -> (116,447) -> (116,445)
-> (116,446) -> (115,446) -> (115,447) -> (113,447)
-> (113,449) -> (113,451) -> (114,451) -> (114,452)
-> (114,451) -> (115,451) -> (114,451) -> (113,451)
-> (113,447) -> (117,447) -> (117,449)
```

Its eighteen axis-aligned legs total 30 horizontal blocks. Every intersected
column has a full-height sand/sandstone floor at Y176 and air at Y177/178.
The 0.6-wide, 1.8-high actor fits the centered route and its corners. It bypasses
the central plinth and decorative pots without breaking or stepping onto them.
This is one activity space with a central obstacle, not a room for each chest,
each source niche or each turn. It has two rare-loot chest arrangements and three
authored enemy sources (two husks, one zombie); none is an observed encounter.

Both single chests have air above and no saved Lock field. Under the existing
unlocked/no-blocking-entity scenario, use the following interaction rays from
upright eye Y178.62:

| Station (X,feet Y,Z) | Aim point | Action |
| --- | --- | --- |
| (115.5,177,446.5) | (115.5,177.5,445.9375) | Open north rare chest's south face |
| (115.5,177,451.5) | (115.5,177.5,452.0625) | Open south rare chest's north face |
| (116.5,177,445.5) | (116.5,178.1,444) | Reach husk source at (116,178,443) |
| (113.5,177,449.5) | (112,178.1,449.5) | Reach zombie source at (111,178,449) |
| (114.5,177,452.5) | (114.5,178.9,454) | Reach husk source at (114,178,454) |

Chest rays are approximately 1.253 blocks. The northern and western source rays
are approximately 1.588 blocks; the southern source ray is approximately 1.526
blocks. All satisfy the three-block modeled reach. The northern/western recesses
have top sandstone slabs at (116,178,444) and (112,178,449), respectively. At the
near boundary of each slab cell the ray is Y178.446667, descending to Y178.1 at
the source face, entirely below the slab's Y178.5 lower surface. The southern
recess has a bottom slab at (114,178,453): its ray enters at Y178.713333 and rises
to Y178.9, entirely above that slab's Y178.5 top. Surrounding floor and ceiling
therefore do not block these specific rays. No slab removal is needed. Removing
the recessed sources also leaves the route's floor untouched.

Two 27-slot GUI operations, three source removals and their associated selection,
acquisition, verification and encounter phases remain costs for the complete
objective budget. This access result does not establish generated/acquired loot,
realized spawning or a human completion time.

Reproduce the route, lid conditions and recessed slab states:

```sh
uv run python - <<'PYRAMID_RARE'
import gzip, hashlib, importlib, json
from pathlib import Path
p=Path('evidence/item-13/fixed-blocks/mss-desert_pyramid.json.gz')
assert hashlib.sha256(p.read_bytes()).hexdigest()=='7dfc8e4d500459ad0839137e3939e9ee19df3a6b3cf1c7ae709b2711f8eb43a4'
c=json.loads(gzip.decompress(p.read_bytes()))['cases'][0]
s=importlib.import_module('evidence.item-13.render_pilot').state_at
points=[(117,449),(117,447),(116,447),(116,445),(116,446),
        (115,446),(115,447),(113,447),(113,449),(113,451),
        (114,451),(114,452),(114,451),(115,451),(114,451),
        (113,451),(113,447),(117,447),(117,449)]
length=0
for (x,z),(xx,zz) in zip(points,points[1:]):
    assert x==xx or z==zz
    length+=abs(x-xx)+abs(z-zz)
    for bx in range(min(x,xx),max(x,xx)+1):
        for bz in range(min(z,zz),max(z,zz)+1):
            assert s(c,bx,176,bz)['Name'] in ('minecraft:sandstone','minecraft:smooth_sandstone','minecraft:sand')
            assert all(s(c,bx,y,bz)['Name']=='minecraft:air' for y in (177,178))
assert length==30
for x,z,kind in ((116,444,'top'),(112,449,'top'),(114,453,'bottom')):
    assert s(c,x,178,z)=={'Name':'minecraft:sandstone_slab','Properties':{'type':kind,'waterlogged':'false'}}
for x,z in ((116,443),(111,449),(114,454)):
    assert s(c,x,178,z)['Name']=='minecraft:spawner'
for z in (445,452):
    assert s(c,115,178,z)['Name']=='minecraft:air'
    be=next(b for b in c['block_entities'] if (b.get('x'),b.get('y'),b.get('z'))==(115,177,z))
    assert be['LootTable']=='mss:rare' and 'Lock' not in be
print('Thirty-block rare-room circuit, chest lids and recessed source states pass.')
PYRAMID_RARE
```

## Remaining stair and corridor sources

Three more sources are accessible directly from already checked route stations,
with no added movement or breach. Reuse the same saved extraction and source
collision assumptions. The following are direct block/ray derivations, not live
interaction observations:

| Station (X,feet Y,Z) | Eye Y | Target face point | Source |
| --- | ---: | --- | --- |
| (118.5,180,469.5) | 181.62 | (118.5,180.5,468) | Husk at (118,180,467) |
| (124.5,177,465.5) | 178.62 | (126,177.5,465.5) | Husk at (126,177,465) |
| (125.5,177,450.5) | 178.62 | (127,178.9,450.5) | Zombie at (127,178,450) |

The first two rays are 1.872004 blocks. Their intervening cells, respectively
(118,Y180/181,468) and (125,Y177/178,465), are air. The source faces are reached
below the full blocks over those sources. The third ray is 1.525910 blocks,
passing over the bottom sandstone slab at (126,178,450): it enters that cell at
Y178.713333 and reaches the source at Y178.9, above the slab top Y178.5 and below
the Y179 ceiling. The standing stations have full support and two air body cells.
No adjacent fence lies on these centerline rays. These actions remove no route
support; their mining/selection and encounter costs still belong in full timing.

A first direct assertion incorrectly required all three floors to be ordinary
sandstone and failed. Exact inspection shows the third floor, (125,176,450), is
smooth sandstone. The corrected full-block assertion passes; no raw evidence or
route geometry changed. The other floors are sandstone at (118,179,469) and
(124,176,465). This was a checking error, not a failed traversal observation.

Local access coverage is now eight of eleven authored sources: two in the lower
chamber, three around the rare-chest room, and these three stair/corridor sources.
All three chest arrangements have local conditional access. The remaining three
sources are the surface positions (110,181,464), (132,181,481) and (133,182,461).
Their access and the surface links still need integration before claiming a
complete circuit. This accounting does not mark the Pyramid sample or Item 13
complete, and does not replace family repetitions or broader material coverage.

## Surface source access and western entrance link

The three remaining surface sources have exposed top faces. Each has a dry,
full-block-supported adjacent station with air in both body cells and above the
source. At each station use upright eye height 1.62 above feet and target the
source top center. Each ray is 1.903786 blocks and does not cross another block:

| Source | Station (X,feet Y,Z) | Top-face target |
| --- | --- | --- |
| Zombie (110,181,464) | (111.5,182,464.5) | (110.5,182,464.5) |
| Husk (132,181,481) | (131.5,182,481.5) | (132.5,182,481.5) |
| Husk (133,182,461) | (132.5,183,461.5) | (133.5,183,461.5) |

The station floors are sandstone (111,181,464), sand (131,181,481), and sandstone
(132,182,461), respectively. The ray volume occupies only the station and source
columns above those floors. Removal leaves station support intact. These direct
saved-block derivations complete local conditional access for eleven of eleven
sources, but do not yet provide a single connected full-task route.

A first western entrance-link check failed: the direct route along X111 at feet
Y182 crosses air at (111,181,466), with actual sandstone support one block lower.
The original eight-block level-walk candidate is rejected. No traversal occurred.
Instead use this ten-block detour, all at feet Y182, with column coordinates
converted to centers by adding 0.5:

```text
(114,469) -> (111,469) -> (111,467) -> (112,467)
-> (112,465) -> (111,465) -> (111,464)
```

Direct queries of every traversed column confirm full sand/sandstone support at
Y181 and air at Y182/183. The detour avoids both the depression at (111,466) and
the two-high sandstone wall at (112,468). It needs no block changes, jumps or
vertical transitions. Reversing it adds ten more horizontal blocks if the full
objective returns to the same stair entrance. The eastern source stations and
upper chest station still require surface links. Do not count local interaction
coverage as complete traversal, timing or family sampling.

## Complete surface circuit with six declared half-step inserts

The surface circuit joins the western source, upper chest, eastern source,
southeastern source and original stair entrance. Use the previously checked
10-block western link first. The four subsequent paths below are ordered
(X,feet Y,Z) column coordinates; add 0.5 to X/Z. Expand same-height legs along
their single horizontal axis. Each height-changing pair is horizontally adjacent.

```text
West source to upper chest, 20 horizontal blocks:
(111,182,464), (111,182,461), (111,183,460), (111,183,455),
(111,182,454), (111,182,453), (112,182,453), (112,182,452), (119,182,452)

Upper chest to eastern source, 28 horizontal blocks:
(119,182,452), (116,182,452), (116,182,456), (120,182,456),
(121,183,456), (126,183,456), (126,183,457), (130,183,457),
(130,183,458), (131,183,458), (131,183,459), (132,183,459), (132,183,461)

Eastern to southeastern source, 21 horizontal blocks:
(132,183,461), (132,183,462), (131,183,462), (131,183,478),
(131,182,479), (131,182,481)

Southeastern source to stair entrance, 37 horizontal blocks:
(131,182,481), (130,182,481), (130,182,480), (128,182,480),
(127,183,480), (124,183,480), (124,183,481), (121,183,481),
(120,182,481), (116,182,481), (116,182,480), (114,182,480),
(114,182,479), (112,182,479), (112,182,473), (111,182,473),
(111,182,469), (114,182,469)
```

Every raw route column has full sand/sandstone/stone support and air at feet and
head. Six transitions change raw floor elevation by one block, exceeding the
0.6 step limit. Predeclare six cobblestone bottom slabs in the lower route cells:
(111,182,461), (111,182,454), (120,182,456), (131,182,479), (128,182,480),
and (120,182,481). These are air before construction, supported by full floors;
all have a third air cell overhead. A bottom slab raises their standing surface
by 0.5, turning each transition into two half-block support changes. The actor's
raised 1.8-high body remains clear. The actual slab-center feet levels replace
the raw lower feet levels in the path above; do not traverse those cells at the
unmodified heights after placement.

Place each slab on the exposed top face of its supporting floor before entering
that cell. For ascents, the preceding same-level station is respectively
(111.5,182,462.5), (119.5,182,456.5), and (129.5,182,480.5). For descents, place
from the higher adjacent station: (111.5,183,455.5), (131.5,183,478.5), and
(121.5,183,481.5). Aim at the lower cell's floor top center. Upright-eye rays
are 1.904 blocks from a same-level station and 2.804 blocks from a higher one,
both within reach. For a high-to-low ray, it crosses the high floor's boundary
0.31 blocks above that floor, so the high support does not occlude it. Each target
cell is air, the floor is full, and the actor is outside the cell being filled.
Top-face placement creates a bottom slab. Reuse the pinned vanilla slab model;
this is conditional construction, not an observed placement or acquired resource.

Including the initial western link, the complete surface circuit totals 116
horizontal blocks, three blocks of ascent and three of descent, with six slab
placements and no mining beyond the three source removals. These are route and
construction inputs, not a finished timing result. Its feet span Y182..183; the
inserted half-level stations are Y182.5. The route avoids water, tree trunks,
leaves, cactus and sandstone-wall cells rather than treating them as air. It
connects all three surface sources and the double chest to the same stair
entrance used by the underground objective. The earlier direct western route
failure remains rejected; the accepted ten-block detour is included here.

Direct verification below checks the coordinate derivation against the retained
raw extraction. It does not use a general pathfinder as evidence of playability:

```sh
uv run python - <<'PYRAMID_SURFACE'
import gzip, hashlib, importlib, json
from pathlib import Path
p=Path('evidence/item-13/fixed-blocks/mss-desert_pyramid.json.gz')
assert hashlib.sha256(p.read_bytes()).hexdigest()=='7dfc8e4d500459ad0839137e3939e9ee19df3a6b3cf1c7ae709b2711f8eb43a4'
c=json.loads(gzip.decompress(p.read_bytes()))['cases'][0]
s=importlib.import_module('evidence.item-13.render_pilot').state_at
paths=[
[(111,182,464),(111,182,461),(111,183,460),(111,183,455),(111,182,454),(111,182,453),(112,182,453),(112,182,452),(119,182,452)],
[(119,182,452),(116,182,452),(116,182,456),(120,182,456),(121,183,456),(126,183,456),(126,183,457),(130,183,457),(130,183,458),(131,183,458),(131,183,459),(132,183,459),(132,183,461)],
[(132,183,461),(132,183,462),(131,183,462),(131,183,478),(131,182,479),(131,182,481)],
[(131,182,481),(130,182,481),(130,182,480),(128,182,480),(127,183,480),(124,183,480),(124,183,481),(121,183,481),(120,182,481),(116,182,481),(116,182,480),(114,182,480),(114,182,479),(112,182,479),(112,182,473),(111,182,473),(111,182,469),(114,182,469)]]
full={'minecraft:sand','minecraft:sandstone','minecraft:smooth_sandstone','minecraft:stone'}
slabs=set(); totals=[]
for path in paths:
    length=0
    for a,b in zip(path,path[1:]):
        x,y,z=a; xx,yy,zz=b
        assert x==xx or z==zz
        distance=abs(x-xx)+abs(z-zz); length+=distance
        if y!=yy:
            assert distance==1 and abs(y-yy)==1
            lower=min((a,b),key=lambda q:q[1]); slabs.add(lower)
            assert s(c,lower[0],lower[1]+2,lower[2])['Name']=='minecraft:air'
            cells=[a,b]
        else:
            cells=[(bx,y,bz) for bx in range(min(x,xx),max(x,xx)+1)
                   for bz in range(min(z,zz),max(z,zz)+1)]
        for bx,by,bz in cells:
            assert s(c,bx,by-1,bz)['Name'] in full, (bx,by,bz)
            assert all(s(c,bx,k,bz)['Name']=='minecraft:air' for k in (by,by+1)),(bx,by,bz)
    totals.append(length)
assert totals==[20,28,21,37]
assert slabs=={(111,182,461),(111,182,454),(120,182,456),
               (131,182,479),(128,182,480),(120,182,481)}
print('Surface legs verified:',totals,'plus prior 10-block western link; six slab inserts.')
PYRAMID_SURFACE
```
