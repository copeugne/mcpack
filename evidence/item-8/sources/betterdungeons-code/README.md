# Better Dungeons custom generation sources

Source tool revision: `d7c955f`.
Retained archive: `YungsBetterDungeons-1.21.1-NeoForge-5.1.4.jar`.
Archive SHA-256: `61816c3b7c9d92c6b44f93dce87ceb0a22827f20285d5d9c4d10d519d734de04`.
Seven class disassemblies are bound by `identities.json`, SHA-256
`c82c912cff651c87b11db309057ff0cd5c2f00ee5e0e12146ad645ac0f563036`.
Only text is committed, not the archive or class binaries.

Executed from the repository root:

```sh
uv run -m tools.inspect_item8_pool_elements --archive YungsBetterDungeons-1.21.1-NeoForge-5.1.4.jar --output evidence/item-8/sources/betterdungeons-code
diff -rq evidence/raw/item8/betterdungeons-code-pilot evidence/item-8/sources/betterdungeons-code
```

The committed extraction reproduced the pilot exactly before this README was
added. For a new reproduction use an absent output directory, and compare the
identity file and its seven listed disassemblies. The existing tool verifies
the retained archive hash and uses the pinned Temurin javap.

The Spider Dungeon has no direct start pool. `SpiderDungeonStructure` samples
its start height, creates a `SpiderDungeonBigTunnelPiece`, adds it to a pieces
builder and calls `addChildren`. Big tunnels can construct more big tunnels,
small tunnels and nests. Small tunnels can construct egg rooms. These classes
are components of the registered dungeon, not additional families.

`SpiderDungeonNestPiece` places a spawner and calls `setEntityId` with
`EntityType.CAVE_SPIDER`. `SpiderDungeonEggRoomPiece` has a chest branch using
`betterdungeons:spider_dungeon/chests/egg_room` and an alternative spawner branch
calling `setEntityId` with `EntityType.SPIDER`. These are source possibilities;
they do not establish per-structure counts or unconditional placement.

The Small Nether Dungeon class is retained for its distinct placement path.
It checks the small-Nether-dungeon enabled configuration before continuing.
Its effective frozen configuration and downstream assembly still require
attribution. This extraction does not close dimensions, occupied geometry,
discoverability, replacement behavior, loot integration or the Item 8 gate.
