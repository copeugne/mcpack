# Ancient city family assessment

This assessment reuses the verified runtime root, effective biome/dimension join,
packaged JSON/template catalog, pool trace and retained full-start observations.
Their hashes are bound in family-decisions.json. No new capture or measurement
tool is needed. Direct immutable class inspection resolves the selected sculk
feature's encounter mechanism; exact JAR/member hashes are in processor_inspection.

The root selects city_center,size7,distance116,city_anchor at absoluteY-27 and
beard_box adaptation. Its eight spawn categories all have empty lists with full
bounding-box scope.57 reachable templates have no template entities, DATA markers
or ordinary/trial spawner blocks in the retained trace. The missing template
minecraft:ancient_city/walls/intact_horizontal_wall_stairs_5 remains explicit;
no baseline repair or successful realization of every component is claimed.

The three selected degradation lists are ancient_city_generic_degradation,
ancient_city_start_degradation and ancient_city_walls_degradation. They use block
rot where applicable, cracked deepslate substitutions, possible lantern/slab
removal and protected-block checks. They do not assign loot or spawn entities.
Template chests reference minecraft:chests/ancient_city and
minecraft:chests/ancient_city_ice_box, both defined in the preserved catalog.
This identifies reward sources, not measured contents or external loot additions.

The pool trace also selects minecraft:sculk_patch_ancient_city. Its placed feature
has no placement modifiers and references the same configured-feature ID. The
configured sculk_patch uses extra_rare_growths uniform1..3, distinct from the
ordinary deep-dark patch's zero. Direct SculkPatchFeature.place inspection shows
these are placement attempts at X/Z offsets nextInt(5)-2, requiring air with a
sturdy upper support face. It writes SCULK_SHRIEKER with CAN_SUMMON=true. Actual
success/count depends on the feature and terrain; these are not guaranteed counts.

SculkShriekerBlockEntity.canRespond requires CAN_SUMMON, non-Peaceful difficulty
and doWardenSpawning. tryToWarn delegates to WardenSpawnTracker.tryWarn;
trySummonWarden requires warningLevel>=4 and invokes SpawnUtil.trySpawnMob for
WARDEN with TRIGGERED reason. Spawn failure remains possible. tryRespond applies
darkness and may play a reply when summoning fails. These guards establish a
conditional triggered threat, not an observed Warden or ordinary spawner block.
The empty ordinary spawn lists do not negate this path or every external source.
No need to simulate player warning progression to identify Item8 mob provenance.

Direct inspection, using the hash-verified mapped server from the frozen runtime:

```sh
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -p -c -classpath instances/pristine-baseline-v0/libraries/net/minecraft/server/1.21.1-20240808.144430/server-1.21.1-20240808.144430-srg.jar net.minecraft.world.level.levelgen.feature.SculkPatchFeature net.minecraft.world.level.block.entity.SculkShriekerBlockEntity
```

Two existing full-start assemblies supply approximate geometry:

| Source | Line | Chunk | Saved envelope | Size X,Y,Z |
|---|---:|---|---|---|
| run-a/mountainous/chunks.jsonl | 13428 | 22,2 | 237,-52,-74,458,-22,140 | 222,31,215 |
| run-a/ocean-heavy/chunks.jsonl | 12215 | 25,-26 | 343,-52,-525,507,-22,-304 | 165,31,222 |

Saved envelopes include air/padding and do not bound every sculk/terrain effect,
occupied volume, typical size or all possible layouts. Deepslate buildings/walls,
soul lanterns and sculk provide underground cues. Neither the negative anchor nor
these two examples establishes a sealed roof, entrance or discovery distance.
