# Aether custom generation entry paths

Captured with extractor revision a1fa603. All five disassemblies and identities
reproduced byte for byte before this README was added. Reproduce:

```sh
uv run -m tools.inspect_item8_pool_elements --archive aether-1.21.1-1.5.10-neoforge.jar --class-name com/aetherteam/aether/world/structure/BronzeDungeonStructure.class --class-name com/aetherteam/aether/world/structure/SilverDungeonStructure.class --class-name com/aetherteam/aether/world/structure/GoldDungeonStructure.class --class-name com/aetherteam/aether/world/structure/LargeAercloudStructure.class --class-name com/aetherteam/aether/world/structurepiece/LargeAercloudChunk.class --output evidence/raw/item8/aether-custom-entry-r1
```

## Direct entry and cloud-writer findings

BronzeDungeonStructure delegates assembly to BronzeDungeonBuilder.initializeDungeon.
Its entry contains terrain/height search and reads bronze_dungeon/boss_room
for a room-height constraint. SilverDungeonStructure delegates room assembly to
SilverDungeonBuilder and constructs SilverTemplePiece and SilverBossRoom pieces.
It also builds a cloud bed using LargeAercloudChunk. GoldDungeonStructure
constructs GoldIsland, GoldBossRoom and GoldStub pieces and delegates further
cave/island content. These named pieces and builders are direct dependencies,
not independently verified family content from this entry capture alone.

LargeAercloudStructure supplies its configured BlockStateProvider to
LargeAercloudChunk. Its position generation begins at chunk-minimum X/Z and
min-build-height plus nextInt(rangeY), builds a random-walk set of cloud
positions, and divides positions by chunk. The call to onTopOfChunkCenter at
entry does not mean the generated cloud Y uses that sampled surface height.
Per-chunk bounding boxes use initial Y minus 16 clamped at literal zero and
final walk Y plus 16; those are assembly envelopes, not occupied measurements.
Do not use the entry heightmap label as a surface-placement classification.

LargeAercloudChunk stores positions and the provider. postProcess visits stored
positions and removes ones accepted by placeBlock. Inside the supplied bounds,
placeBlock writes the provider-selected state with flag 2 only when the world
position is empty. It discards the write result and returns true even when an
occupied position prevents a write. Outside bounds it returns false. Therefore
removed positions and a successful lifecycle do not prove placed block counts.
This writer contains no direct mob spawn, chest loot or spawner assignment.
Its source contribution is configured block formation, also reused as a Silver
Dungeon component. The selected standalone cloud provider still needs a catalog
binding before accepting its material/content disposition.

Next: bind that provider and follow the actual bronze/silver/gold assembly and
piece content. Reuse templates, processors and existing sources. Do not count
cloud chunks, room builders, island stubs or serialized pieces as families.
No new world measurement or runtime acceptance claim. Scoped extractor Ruff
and Basedpyright passed.

## Standalone cloud provider

The selected large_aercloud definition is now bound by
tests/item8/test_aether_cloud_source.py: simple_state_provider supplies
aether:cold_aercloud with double_drops=true, size 3, rangeY 32 and empty
spawn_overrides. Its SHA-256 is
c6590b05dabf5f822bd7447c79efe3801f1426c1437d5fde986d9b620cc43097.
Together with the direct writer, this supports a working terrain/cloud
disposition. The registry row remains for coverage; it is not an accepted
authored-structure family count. Ordinary block drops, external modifications,
world geometry and discoverability remain outside this source finding.

```sh
uv run pytest -q tests/item8/test_aether_cloud_source.py
```

The focused test and scoped test/builder Ruff and Basedpyright passed.
