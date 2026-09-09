# Nether Tower: quality assessment

Status: IN PROGRESS. Source/saved enemy and reward inputs are integrated.
Playable topology, complete task timing and quality synthesis remain required.

Sample: full-ocean-heavy-r1-baseline|minecraft:the_nether|mns:nether_tower|14|16.
Reuse the retained [saved blocks](mns-nether_tower.json.gz), SHA-256
03e5bcfe3dacf13b7780dc46b1a525145ad945aa5255baecc6e7386fac47eb0c.
The compressed file is 8,464 bytes and contains 43,732 padded voxels. Envelope
[213,51,245,235,96,267], padded bounds [210,48,242,238,99,270]. Existing extraction
and custody records retain world identity and complete chunk coverage. No new
world generation or extraction is required for this inspection.

## Source correspondence and encounter inputs

The saved rigid single-pool component directly selects `mns:nether_tower`, with
empty processors, origin (235,51,245) and CLOCKWISE_90 rotation. Source local
(u,v,w) maps to (235-w,51+v,245+u). This is one fixed authored component, not a
room count or proof of continuous vertical access.

Use the previously verified MNS JAR SHA-256
05024f18690436fff2fbc088f880a95cc30f23bacfe6e8058f6b02106032a990.
Its `data/mns/structure/nether_tower.nbt` SHA-256 is
06621f2778578d2bf4b043abb8afbc54cfaba827f38a43b1ccca5167e68e55a6.
Source dimensions are 23x46x23. The template's entities list is empty and its
palette contains no spawner state. Saved block entities likewise contain no
spawner. The packaged `data/mns/worldgen/structure/nether_tower.json` has empty
spawn_overrides. These establish zero explicit template-resident enemies and
zero authored spawner sources, not zero realized enemies in the accepted world.
Natural mobs, surrounding structures and actual encounters remain NOT MEASURED.
A no-natural-spawn conditional task can therefore have zero authored combat work;
it must not be reported as a measured peaceful visit.

All seventeen source reward blocks map to unique matching saved block entities,
with identical type and LootTable assignments:

| Group | Saved positions | Source table |
| --- | --- | --- |
| West lower stack | (218,55,258), (218,55,259), (218,55,261), (218,55,262), (218,56,258), (218,56,262), (218,57,258) | `mns:chests/houses` |
| Inner lower stack | (219,55,258), (219,55,259), (219,55,262), (219,56,258), (221,55,262) | `mns:chests/houses` |
| East lower stack | (222,55,261), (222,55,262), (222,56,262), (223,57,262) | `mns:chests/houses` |
| Elevated chest | (224,75,256) | `mns:chests/treasure` |

These are sixteen barrels and one chest, not seventeen rooms. Reuse the
[Large House table inspection](mns-large_house_1-report.md#active-source-and-positional-correspondence)
for houses/treasure content potential and exact resource hashes. Saved LootTableSeed
values do not establish rolled contents. Access, chest-lid clearance, generated
items and acquired inventories are not established by positional correspondence.
Do not assume that the elevated treasure chest is an authored finale merely
because it is higher than the lower cache.

Reproduce correspondence by decoding the named template with the existing
`mcpack_evidence.item7_nbt.decode_compound_nbt`, applying the transform above to
barrel/chest positions, and joining against `block_entities` in the hash-bound
extraction. The 17 transformed positions are unique and each type/table matches;
there are no source spawner palette states and no source entities. Direct immutable
artifact inspection suffices; no new helper or runtime probe is introduced.

## Bounded topology inspection predeclaration

Inspect the retained block slices to identify entrance, lower cache, vertical
connections, elevated chest access and any other playable activity space. Resolve
actual floor support, doors, ladders/stairs and overhead clearance before modeling
a route. The 20-block difference between lower barrel Y55 and chest Y75 is a
target-height difference, not established progression.

Budget direct queries at one minute, 512 MiB memory and under 1 MiB text. If a
slice render is needed, reuse `render_pilot.render_slices`, with one bounded
180-second conversion and at most 20 MiB SVG/PNG output. This is read-only analysis
of the already retained extraction; no server or world materialization is planned.
Record render failures rather than silently replacing them. Use the separately
accepted complete-task accounting method after access is resolved. Item 14 stays
UNSTARTED.

## Retained slices and first vertical constraint

The bounded conversion completed with clean exit in 32.42 seconds (Bash time,
user 29.17, system 5.12). Its [slice sheet](mns-nether_tower-slices.png) is
201,810 bytes at 1532x4771 pixels; temporary SVG is 7,191,441 bytes, for a combined
7,393,251 bytes. No render failure occurred. The agent inspected the full sheet;
colors represent saved block categories, not collision shapes or human gameplay.

Reproduce without new world reads:

```sh
uv run python -m evidence.item-13.render_pilot --input evidence/item-13/fixed-blocks/mns-nether_tower.json.gz --output /tmp/item13-nether-tower-slices.svg
time -p timeout 180 convert -background white /tmp/item13-nether-tower-slices.svg /tmp/item13-nether-tower-slices.png
```

A full-envelope name query finds no ladder or twisting-vine block. The sixteen
trapdoors are all warped trapdoors at Y79, above the treasure chest. They do not
by themselves provide a lower-to-chest route. Stair-shaped decoration remains
present; its existence is not proof of a continuous climb.

At the chest's column (224,256), the saved vertical sequence is full deepslate
tiles at Y54, air Y55..63, red nether bricks Y64, air Y65, polished blackstone
Y66..74, east-facing single chest Y75, then air Y76/77. The adjacent west column
(223,256) has the same lower sequence through Y66 but air Y67..77. Thus the chest
sits atop a nine-block polished-blackstone column above Y66, with no axial access
through that solid column. Air beside a pillar is not a supported staircase.
The Y64 and Y66 layers also interrupt a direct ascent from the lower cache.
A lateral native route or explicit construction must be established before
counting this as twenty blocks of playable progression.

These facts are reproducible using `render_pilot.state_at` on the two named
columns and a palette-name query over the exact envelope. They resolve the axial
obstruction and preserve the distinction between decorative height and playable
access. Entrance, cache-container access and the complete vertical route remain
the next measurements; no unsupported traversal time is assigned.
