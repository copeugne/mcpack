# Quark landmark and encounter generator sources

Captured at `62f760e` through the existing extractor. Exact archive, class and
disassembly hashes are preserved in `identities.json`. Reproduction matched all
six captures and the identity list byte for byte:

```sh
uv run -m tools.inspect_item8_pool_elements --archive Quark-4.1-480.jar --class-name org/violetmoon/quark/content/world/module/FallenLogsModule.class --class-name org/violetmoon/quark/content/world/module/FairyRingsModule.class --class-name org/violetmoon/quark/content/world/module/MonsterBoxModule.class --class-name org/violetmoon/quark/content/world/gen/FallenLogGenerator.class --class-name org/violetmoon/quark/content/world/gen/FairyRingGenerator.class --class-name org/violetmoon/quark/content/world/gen/MonsterBoxGenerator.class --output evidence/raw/item8/quark-landmarks-62f760e
```

## Direct registration and content findings

FallenLogsModule registers FallenLogGenerator at TOP_LAYER_MODIFICATION.
FairyRingsModule registers FairyRingGenerator at that same stage.
MonsterBoxModule registers MonsterBoxGenerator at UNDERGROUND_DECORATION.
All use WorldGenHandler.addGenerator, whose dispatch is already preserved.
These are additional provider paths to account for, not registry structure roots.

MonsterBoxGenerator rejects FlatLevelSource. Its chancePerChunk loop chooses a
chunk-local X/Z and a configured Y, searches downward within searchRange and
above minY, and requests one monster_box block at a qualifying location.
The location must be replaceable, non-liquid, and above a stone-based block
with a sturdy upper face. canPlaceHere temporarily moves the mutable position
down and restores it before returning. The setBlock boolean is discarded.
Values above one in chancePerChunk permit additional attempts through subtraction
of one per iteration. This describes source logic, not observed placement rates.
No entity is requested directly by this generator. MonsterBoxBlock and its block
entity require interpretation before describing the encounter or spawner role.

FairyRingGenerator.spawnFairyRing reads the biome's flower features and selects
a RandomPatchConfiguration feature when available, otherwise using oxeye daisy.
Its full placement and terrain logic remains to be interpreted. Do not infer
occupied size from the first loop or classify it as ordinary vegetation solely
because some materials are flowers. Fallen-log geometry, decoration choices and
placement conditions likewise remain open.

No additional canonical family is accepted by this capture alone. Reconcile
these designs, frozen settings and world evidence using the existing inventory
path. Other Quark generators and full retained-provider coverage remain open.
