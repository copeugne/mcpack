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

## Fairy Ring interpretation

generateChunk chooses chunk-local X/Z and samples its biome at Y=128. The forest
tag takes precedence over the plains tag when selecting the chance field; all
other biomes receive zero chance. After the chance check, it searches downward
from Y=128 to Y=30 for a DIRT-tag block. It invokes spawnFairyRing one block
below that found block, which is the anchor used below.

For X/Z offsets -3 through 3, the ring consists of positions whose squared
horizontal distance is in [7,10]. Outside that band, it searches Y offsets 6
through -2 and removes the first SMALL_FLOWERS block in each column. Inside
the band, it searches floor offsets 5 through -3 for DIRT with empty space
above. At the first qualifying position it either places an oxeye daisy or
invokes the selected biome flower feature and reads the resulting block state
at the requested position. Later ring positions copy that state. Feature and
block-write booleans are discarded. If the delegated feature leaves air there,
the later copies can also be air; a complete visible ring is not guaranteed.

The generator then starts 25 through 34 blocks below the anchor and searches
up to ten further blocks downward for a STONES-tag block. If found, it chooses
one configured ore state, writes the center and independently attempts each
of six face neighbors with nextBoolean. The neighbors have no additional
stone-replacement check. This is one requested center plus up to six neighbors,
not a measured occupied ore count. The module's configChanged method resolves
oresRaw through the block registry, adds non-air default states, and prints an
IllegalArgumentException for air entries while continuing. Its initial ores
list is empty until populated by that callback.

Direct writes fit X/Z offsets -3 through 3 and Y offsets -45 through 6, giving
a conservative 7x52x7 XYZ envelope including empty space and the buried deposit.
This bound excludes the delegated flower feature, whose own placement can
extend beyond the requested origin. The surface ring alone is roughly seven
blocks across; it must not be described as a 52-block-tall visible structure.

The frozen world.fairy_rings section records forest chance 0.00625, plains
chance 0.0025, emerald/diamond ore and an Overworld dimension allowlist. These
agree with module defaults; callback/annotation binding and effective biome-tag
membership remain to be reconciled. The direct generator requests no entities,
physical spawners or container loot. The flower feature and natural mobs remain
separate dependencies. Source-derived discoverability is a surface flower ring
marking a buried ore reward, not an observed visibility distance.

The ring and associated buried deposit support one working landmark design,
with flower and ore choices as variants. Do not split the deposit into another
family. Final inventory integration, effective constraints and saved-world
attribution remain open; no Item 9 tier is assigned here.
