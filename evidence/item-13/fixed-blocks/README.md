# Selected fixed-layout saved blocks

Status: raw block coverage complete for these nine selected instances only.
Playable topology, traversal/combat models and quality assessments remain pending.
Protocol: `item13-fixed-blocks-v1`, declared in [coverage](../coverage.md).
The raw `protocol_sha256` binds the unchanged shared definitions in
[protocol.md](../protocol.md); the fixed-block declaration is preserved by this
batch's delivering commit, alongside its exact selection hash.
Exact candidate IDs, dimensions, bounds and source components are in the
[selection](../fixed-moog-selection.json). Each compressed file below retains the
selection, producer, protocol, archive and backup identities, exact saved blocks,
block entities, WORLD_SURFACE columns and saved start NBT. Its same-basename
`-execution.txt` records output SHA-256, elapsed seconds, peak RSS and voxel count.

All nine reads passed full-chunk and required-section checks and complete world
inventory verification before and after under the existing POSIX lock. Total:
556,065 voxels, 87,559 compressed bytes, 60.887 seconds and 53,536 KiB maximum RSS.
The [first-house reproduction](reproduction.txt) was byte-identical in 6.336 seconds
at 45,420 KiB RSS.
No server was started. No raw world, seed or frozen configuration was changed.

The following are saved block-entity counts **inside the original component
envelope**, not room counts, realized enemies, activated encounters or acquired
loot. Other inventory blocks and loot-table assignments still need assessment.
Named enemy types are only explicit `SpawnData.entity.id` values. Empty assignments
are retained without inventing a default mob or treating a spawner as operational.
The later [runtime lookup](../collision/README.md#saved-spawner-lookup-result)
resolves the Medium House 1/2 empty payloads: no entity type is returned, and
empty potential lists supply no alternative. That result is reused for identical
payloads; it is not a realized-spawn observation.

| Raw file | Voxels | Ordinary spawners | Explicit types / empty assignments | Chests / barrels |
| --- | ---: | ---: | --- | ---: |
| [Circle](mns-circle_nether_brick.json.gz) | 8,464 | 2 | piglin, piglin brute | 0 / 0 |
| [Giant Skull](mns-giant_skull.json.gz) | 82,574 | 1 | wither skeleton | 2 / 0 |
| [Large House](mns-large_house_1.json.gz) | 72,981 | 7 | blaze, piglin, piglin brute, wither skeleton | 0 / 16 |
| [Medium House 1](mns-medium-house.json.gz) | 8,500 | 4 | one piglin; three empty assignments | 1 / 2 |
| [Medium House 2](mns-medium_house_2.json.gz) | 8,500 | 2 | two empty assignments | 0 / 4 |
| [Nether Tower](mns-nether_tower.json.gz) | 43,732 | 0 | none in saved spawners | 1 / 16 |
| [Warped Dome](mns-warped_dome.json.gz) | 18,816 | 0 | none in saved spawners | 0 / 0 |
| [Desert Pyramid](mss-desert_pyramid.json.gz) | 219,834 | 11 | husk, zombie | 4 / 0 |
| [Small Tower](mss-small_tower.json.gz) | 92,664 | 2 | witch, wither skeleton | 2 / 0 |

Derivation: inspect each `cases[0].block_entities` entry and retain it only when
`x,y,z` lie inclusively within `cases[0].envelope`. Count `minecraft:mob_spawner`,
`minecraft:chest` and `minecraft:barrel` separately. Medium House 1's empty spawn
assignments are at 462,51,432; 465,48,434; 466,51,432, each with an empty
`SpawnPotentials` list. Its piglin assignment is at 465,48,430. Warped Dome's
retained barrel at 171,81,46 is in the external padding, outside the structure
envelope, and is not counted as its authored reward. Mere containment would still
not establish authorship if a different structure overlapped the envelope.

The [Medium House slice sheet](mns-medium-house-slices.svg) was visually inspected.
It shows block categories at Y 43 through 56, with exact properties available in
SVG titles and raw palettes. It is not a collision-shape or player-view render.
The saved spawners and rewards occur at several heights; route connectivity is
not inferred from that. Doors, trapdoors, stairs, slabs, fences, vines and local
vegetation require explicit movement/collision support before traversal scoring.

Reproduce in a new directory, preserving the retained outputs:

```sh
timeout 900 bash evidence/item-13/fixed-blocks/extract.sh /tmp/item13-fixed-blocks-reproduction
uv run python -m evidence.item-13.render_pilot --input evidence/item-13/fixed-blocks/mns-medium-house.json.gz --output /tmp/item13-house-slices.svg
```

The extractor at the commit delivering this batch must be used for exact raw
producer-hash reproduction. A later producer change does not rewrite this raw
history. Decoding equivalence is checked by the nine affected saved-content tests;
the first world case additionally has a byte-identical reproduction. The retained
execution hashes and exact selected IDs were checked across every one of nine
outputs before delivery. None of these checks establishes gameplay quality.

The [configured type-check output](configured-typecheck.txt) retains the 20 errors
and five warnings in two unchanged files described in the main README. Focused
checks for the extractor, renderer, benchmark and changed test file pass. Direct
strict checking of the preexisting untyped density tool also reported 560 errors
and 13 warnings; this is not presented as a clean global type gate or repaired by
a broad unrelated rewrite. Final delivery must retain an explicit disposition.


The [first-house assessment](mns-medium-house-report.md) now records its local
modeled quality and depth. The [second-house assessment](mns-medium_house_2-report.md)
now records both validated vine links, modeled door opening, storage access,
graph/depth sensitivity and quality assessments. Its complete four-barrel model
adds a checked three-scaffold branch beneath the roof barrel and gives conditional
64/116/207-second totals. Both variants retain human-observation limitations;
all three existing raw captures now have delivered custody. The first-house
three-container model gives 68/119/202 seconds with source disablement before its
733-tick delay expires. Family repetitions remain pending.


The [Nether Brick Circle assessment](mns-circle_nether_brick-report.md) records
its authored debris rewards, saved/source hazard differences and mixed spawner
workload. The supplemental sample now has a connected reward inspection circuit,
northern external approach and one-area quality assessment. The original mixed
case records a detour and explicit one-area/two-sector room sensitivity. Both
local assessments now include complete conditional task budgets, retaining
repeated-batch source ceilings for the original overlap. The blackstone root
remains required.

The [Warped Dome assessment](mns-warped_dome-report.md) records one ground room,
external reward access and a complete conditional 16/27/45-second resource task.
The [accepted timing method](../timing-scenario-proposal.md) resolves the earlier
methodology pause; full coverage and layout-specific budgets remain required.
The [Giant Skull assessment](mns-giant_skull-report.md) now integrates source/saved
content, chest access and a conditional 46/74/125..146-second complete task.
Its one-covered-space/zero-enclosed-room sensitivity, shallow-topology assessment
and remaining roof/parkour uncertainty are now integrated.

The [Large House 1 assessment](mns-large_house_1-report.md) maps all seven spawners
and sixteen barrels to the active source. Its `empty` table supplies mixed
empty/item alternatives, so none of those assignments is a guaranteed empty room.
Its five authored activity spaces and separate engineered roof workspace now
have an access graph, complete conditional task timing and quality synthesis.
A capped vine shaft and solid partition remain baseline obstacles, overcome only
by declared construction. Family repetitions and broader coverage remain pending;
the report retains all native-versus-engineered and unobserved-gameplay limits.

The [Nether Tower assessment](mns-nether_tower-report.md) resolves seventeen source/
saved reward assignments and zero explicit spawner/resident-entity sources.
Its conditional access, complete task timing and two-room quality assessment
are integrated. Family repetitions and broader coverage remain pending.

The [Desert Pyramid assessment](mss-desert_pyramid-report.md) integrates all eleven
source interactions, three container arrangements, complete conditional timing
and a staged graph for two indoor rooms plus one outdoor activity area.
Family repetitions and broader coverage remain pending.

The [Small Tower assessment](mss-small_tower-report.md) integrates both sources
and chests, its constructed island connector, main ladder, complete conditional
timing and three-space quality synthesis. Family repetitions remain pending.

The next [Adorabuild blackstone temple](adorabuild-blackstone_temple-report.md)
now integrates all nine material nodes, a checked breach route and a complete
conditional 33/56/94-second harvest. One shrine activity site supplies no room
sequence or required vertical progression; central processor-outcome coverage
remains open. Continue the other four selected Adorabuild cases.

## Remaining four selected Adorabuild inputs

After the blackstone-temple local assessment, the other four preselected reads
passed: 15,914 voxels, 10,069 compressed bytes, 19.344913 seconds total and
182,852 KiB maximum process RSS. Each verified the full accepted world inventory
before/after under the existing lock and matched its predeclared selection hash.
No server, world regeneration or configuration change occurred. There was no
failed extraction in this batch. These are saved blocks and source inputs,
not four completed quality assessments or realized enemy observations.

| Case/raw input | Bytes | Seconds | Source-resident potential | Saved block entities |
| --- | ---: | ---: | --- | --- |
| [Crimson hall](adorabuild-crimson_house_medium_2.json.gz) | 2,964 | 4.980163 | Two adult hoglins, Health40 each; two piglin brutes, Health50 each | One bastion_treasure chest at (-308,34,-420) |
| [End ship](adorabuild-end_ship_small_1.json.gz) | 1,799 | 3.431474 | One shulker, Health30, Peek30, AttachFace0 | One end_city_treasure chest at (8082,58,8125); one skull at (8082,59,8116) |
| [Wart house](adorabuild-nether_fortress_medium_1.json.gz) | 2,508 | 5.286360 | No template residents | Three nether_bridge chests at (156,36,-143), (156,36,-137), (159,36,-140) |
| [Nether temple](adorabuild-nether_temple_medium_1.json.gz) | 2,798 | 5.646916 | No template residents | None; placed material rewards still require inspection |

Each raw file's same-basename `-execution.txt` retains its exact SHA-256, selected
ID, voxel count and memory. The complete selection remains
[fixed-adorabuild-selection.json](../fixed-adorabuild-selection.json).
All saved chests above have LootTable fields but no Lock or Items field. No
ordinary spawner block entity is present. The extractor does not capture realized
entity populations; do not convert the template residents into a saved mob census.
The End skull is an object, not another enemy.

Source jar identity reuses the pinned Adorabuild artifact in the
[blackstone-temple report](adorabuild-blackstone_temple-report.md#source-and-saved-content).
The resources below are under `data/adorabuild_structures/structure/`:

| Template filename | Exact resource SHA-256 | Source size |
| --- | --- | --- |
| crimson_house_medium_2.nbt | 10119ab54d33c6b1f772f3a7f8861c0cdcbdf08d967de9ad65be83ca51bdf120 | 15x6x9 |
| end_ship_small_1.nbt | 99f845b28ec4ed9148fd376d08c931533d8d4faf337fb0cd3eb28c0e7b157caa | 13x10x5 |
| nether_fortress_medium_1.nbt | d85dd98a02113b6b7ddcb8fb34730057a32ba5b3f7114cac0c1743e4753c8793 | 9x9x9 |
| nether_temple_medium_1.nbt | a801a45ea22c6cabe0f70bf667b2bdd28217cc8fd816f9ee53bf8ac28d2a04e8 | 13x9x13 |

Directly decode each gzip NBT resource with the existing decoder. Count
`entities[].nbt.id` for the source-resident column, preserving source health,
empty equipment and the distinction from loaded attributes. Source entities use
historical attribute-key spellings; a modeled combat profile must use the pinned
1.21.1 entity rules rather than assuming every old NBT attribute was applied.
Inspect `blocks[].nbt` for the source containers; the following saved transforms
map their locations to the exact saved nodes above (local coordinates u,v,w):

- Crimson hall: (-304-w,31+v,-432+u), CLOCKWISE_90;
  processor `adorabuild_structures:replace_glass_with_air`.
- End ship: (8080+w,56+v,8128-u), COUNTERCLOCKWISE_90; empty processor.
- Wart house: (160-w,31+v,-144+u), CLOCKWISE_90; empty processor.
- Nether temple: (320-u,31+v,496-w), CLOCKWISE_180;
  processor `adorabuild_structures:randomize_gold_block`.

All four saved components have rigid projection. Those source sizes and transforms
are attribution inputs, never room counts. The Crimson hall's
playable layout, resident model, chest access and complete-task/quality assessment
is now [recorded](adorabuild-crimson_house_medium_2-report.md), with conditional
39/62/104-second four-resident tasks. Its fixed-family sample minimum is satisfied.
Continue the End ship, wart house and Nether temple. Preserve their individual
processor, dimension and enemy-mechanism differences.

Reproduce the four raw extractions with the existing implementation into a new
directory; the extractor rejects existing output files:

```sh
set -euo pipefail
mkdir /tmp/item13-adorabuild-reproduction
for root in crimson_house_medium_2 end_ship_small_1 nether_fortress_medium_1 nether_temple_medium_1; do
  uv run python -m evidence.item-13.measure --fixed-root "adorabuild_structures:$root" --selection evidence/item-13/fixed-adorabuild-selection.json --output "/tmp/item13-adorabuild-reproduction/$root.json.gz"
done
```

No extra reader or evidence format was added. For upcoming local layout views,
reuse the renderer and ImageMagick conversion with a 30-second/2-MiB combined
SVG/PNG per-case cap, followed by exact partial-block checks where needed.

The [End ship assessment](adorabuild-end_ship_small_1-report.md) completes the
selected fixed case with one open deck, both reward targets and a conditional
shulker model. The authored resident overlaps a stair, so its settled position
is not inferred. The rejected label-overlap image and corrected view are retained.

The [wart-house assessment](adorabuild-nether_fortress_medium_1-report.md)
completes the selected fixed case: two usable levels, a46-plant age0 field and
three upper chests. Its conditional task visits the field and empties the three
chests; crop harvesting remains an explicitly separate optional activity.

The [Nether-temple gold assessment](adorabuild-nether_temple_medium_1-report.md)
completes the fifth selected Adorabuild case. Its49-cell authored lava basin
requires a declared catcher/ramp for the conditional gold task. Both temples now have saved debris/lodestone diagnostics and verified
[external custody](../temple-variants/custody/README.md); their reports integrate
the conditional material models.


## Basalt Chambers two-assembly result

The [assessment](basalt-chambers-report.md) integrates both predeclared baseline
assemblies: five and12 rooms, validated breached graphs, complete conditional
tasks, source mechanisms, trap handling, loot/dead-room/finale/replay assessment
and retained failures. The second case's lava recesses require the declared
two-block bridge. Central debris/lodestone/netherite outcomes are supported by
baseline/control cubes and the single missing-material diagnostic, with
[verified raw custody](../basalt-variant/custody/README.md). These are local family
results under the modeled/inspection scope, not full Item13 completion.

The [modular Nether fortress](adorabuild-nether-fortress-report.md) has both
predeclared seed samples assessed, collectively covering all eight components.
The five-/fourteen-space results retain native obstructions, conditional slot
crossings, validated clearing/interaction sequences, complete task estimates and
independent ground-window bypasses. This is a local family result, not full
Item13 completion.

The [Slime Cave report](explorations-slime-cave-report.md) starts the next local
family assessment from its custom source and accepted saved inputs. The first
material-state assessment now includes the dry route, one-room topology, conditional
six-parent/splitting task, source suppression condition and direct loot bypass.
The second selected material state still needs its own saved assessment.
