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
graph/depth sensitivity, timing and quality assessments. Both house variants
retain full-runtime/human-observation limitations and pending raw-capture custody.


The [Nether Brick Circle assessment](mns-circle_nether_brick-report.md) records
its authored debris rewards, saved/source hazard differences and mixed spawner
workload. The supplemental sample now has a connected reward inspection circuit,
northern external approach and one-area quality assessment. The original mixed
case records a detour and explicit one-area/two-sector room sensitivity. Both
local assessments retain their model limits; the blackstone root remains required.

The [Warped Dome assessment](mns-warped_dome-report.md) records one ground room,
external reward access and a complete conditional 16/27/45-second resource task.
The [accepted timing method](../timing-scenario-proposal.md) resolves the earlier
methodology pause; full coverage and layout-specific budgets remain required.
The [Giant Skull assessment](mns-giant_skull-report.md) now integrates source/saved
content, chest access and a conditional 46/74/125..146-second complete task.
Its one-covered-space/zero-enclosed-room sensitivity, shallow-topology assessment
and remaining roof/parkour uncertainty are now integrated.
