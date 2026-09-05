# Explorations Slime Cave custom generator

Captured using extractor revision 82af4f1. Both captures and identities.json
reproduced byte for byte before this README was added:

```sh
uv run -m tools.inspect_item8_pool_elements --archive explorations-neoforge-1.21.1-1.6.2.jar --class-name com/tristankechlo/explorations/worldgen/structures/SlimeCaveStructure.class --class-name com/tristankechlo/explorations/worldgen/structures/pieces/SlimeCaveStructurePiece.class --output evidence/raw/item8/explorations-slime-cave-82af4f1
```

SlimeCaveStructure uses UNDERGROUND_STRUCTURES, BURY terrain adjustment and an
empty spawn-override map. Its codec takes biomes. Generation rejects sea level
at or below 30 and a height span below ten. Otherwise it chooses the chunk's
world X/Z origin and Y = minY + 15 + nextInt(abs(seaLevel - 20 - (minY + 15))).
It adds exactly one SlimeCaveStructurePiece using explorations:slime_cave and
a random Rotation. This is one design with rotation variants, not a pool tree.

The piece uses DeepslateProcessor, which still needs direct attribution. Its
data-marker handler first clears the marker position. A spawner marker places
a vanilla spawner and, if its block entity exists, replaces SpawnData with
minecraft:slime and custom spawn-rule ranges of zero through seven for both
light channels. A slime marker creates a slime, finalizes it with STRUCTURE
spawn reason, sets size to nextInt(3)+1 and requests entity insertion. Failed
creation is skipped; insertion and block-write booleans are discarded. These
are authored requests, not verified successful entities or encounter counts.

The preserved template catalog contains data/explorations/structure/slime_cave.nbt,
SHA-256 02f9dc19b1fd4cf766ff772961298ab96049d1353a765889260f0e78953119d3,
with size [15,12,15], no stored entities, six slime DATA markers, one spawner
DATA marker and one chest referencing explorations:chests/slime_cave. The
template does not contain a stored spawner block; the marker handler authors it.
Bind these catalog observations in the existing inventory validation before
closing the family. Exact effective processor behavior and saved-world
attribution remain open. No claim of live spawning or visual inspection.

Scoped extractor Ruff and Basedpyright checks passed. No new measurement,
server run or additional structure family was introduced.
