# Adorabuild blackstone temple: quality assessment

Status: IN PROGRESS. Exact saved/source reward and encounter inputs recorded;
playable topology, complete task timing and quality synthesis remain required.
This is the first case in the [five-root batch](../coverage.md#next-fixed-layout-batch-five-observed-adorabuild-roots).
Complete it end to end before extracting the other four cases.

Sample: full-ocean-heavy-r2-baseline|minecraft:the_nether|adorabuild_structures:blackstone_temple_small_1|29|-8.
The [saved blocks](adorabuild-blackstone_temple.json.gz) have SHA-256
4c95ea5111f2ddc86866fba1eabc739ee4f221149a940296a172e9b6d562796b.
The [execution record](adorabuild-blackstone_temple-execution.txt) reports
2,366 voxels, 2,158 compressed bytes, 6.157766 seconds and 45,012 KiB peak RSS.
All are within the predeclared per-case budget. The existing extractor verified
full accepted-world inventories before and after under its POSIX lock, with
complete selected chunks/sections. No server was started or world changed.
Original envelope [464,31,-128,470,38,-122], padded bounds
[461,28,-131,473,41,-119]. Input, producer and world identities remain inside raw.

## Source and saved content

The pinned jar is adorabuild-structures-2.11.0-neoforge-1.21.3.jar, SHA-256
6f399680da36dbb95b9a0dbf8b600f173e650be4d6bc25f50fcac792dcce081e.
Its filename is not a compatibility claim; the accepted Item 3 runtime remains
authoritative. Resource data/adorabuild_structures/structure/blackstone_temple_small_1.nbt
has SHA-256 4ca5c2ff86de36326b1075b09daef8f2eb4e21c035ec4d72126dbc8c805a942a.
The source is 7x8x7, with no entity records or block-entity NBT. Saved block
entities are also empty. There is no authored resident or ordinary-spawner
assignment in these inputs; natural spawning and realized enemies are separate.

The single saved component has rotation NONE, rigid projection, origin
(464,31,-128), and processor adorabuild_structures:randomize_gold_block.
Source local(u,v,w) maps to(464+u,31+v,-128+w). Source gold local(3,4,3)
remains a saved gold block at(467,35,-125). Eight gilded-blackstone positions
also match exactly: at each Y33 and Y37, (466,-125), (467,-126), (467,-124)
and (468,-125) in X/Z. These are placed material rewards, not container loot,
rolled nugget outcomes or acquired resources. They cannot be omitted because
there are no chests. Four lower and four upper positions describe distribution,
not eight rooms or a demonstrated upper playable floor.

The processor JSON resource
`data/adorabuild_structures/worldgen/processor_list/randomize_gold_block.json`,
SHA-256 10e1f4737dbaf0351575f87e9fd7b56ac9007ca52886a16e990eb137e867fd87,
contains two ordered gold-block rules: a random-block-match probability 0.2
outputs ancient debris, then a probability 0.1 rule outputs lodestone. Retain
these as rule parameters, not independent observed outcome frequencies or a
claim that either alternative occurred here. The selected saved block is gold.
Material-outcome coverage and consequences for harvesting remain explicit
sampling work; do not tune or reroll this accepted occurrence.

Reproduce by reading the exact jar entries above with zipfile and decoding
gzip NBT using mcpack_evidence.item7_nbt.decode_compound_nbt, then compare
transformed gold/gilded source positions against cases[0] using the existing
render_pilot.state_at helper. Read processors as ordered JSON. No new source
inventory, extraction or custom validator is required for these direct facts.

## Next bounded assessment

The saved core contains dense wall blocks rather than an automatically playable
7x7 room. Inspect its floor, supports and complete body clearances before room
coding. The north stair at (467,32,-128) is south-facing, bottom, straight.
A candidate engineered approach must explicitly account for the chiseled block
at (467,33,-127), the lower gilded block at (467,33,-126), and central wall
blocks at (467,Y33..34,-125). They are not saved air. Validate resource rays,
source drops/tool costs, pickup assumptions and return before timing the task.
Retain all nine material nodes, plus any added removals, in the objective budget.

Use the existing slice renderer once for this 14-layer padded volume, budget
30 seconds and 2 MiB combined SVG/PNG, as an overall layout aid. Exact state and
source-shape checks remain necessary for partial walls and stairs. Rendering
is not player-view observation or a collision trial. Local hazards, room/depth
sensitivity, finale, bypass, replay and shallow-form assessment remain required.
Items 14 through 18 remain UNSTARTED pending predecessor gates.
