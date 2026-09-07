# Repurposed temple assessment

This increment integrates nine required attributes for one family with seven
variants. Existing packaged data, processor inspection and saved-world evidence
suffice; no new capture or tool is needed.

## Evidence and derivation

The seven roots temple_nether_basalt, temple_nether_crimson, temple_nether_soul,
temple_nether_warped, temple_nether_wasteland, temple_ocean and temple_taiga each
select one corresponding template under repurposed_structures:temples/. The
pool-traces-content catalog reports no missing components or unresolved entity
sources for these templates. Ocean authors pufferfish; taiga authors a minecart,
which is not a mob. There are no generation markers or trial spawners.

Five Nether templates contain ordinary spawners, with legacy minecraft:mob_spawner
NBT IDs. Their selected worldgen/processor_list/temples/<variant>_randomizer lists
reference rs_spawners/temples/<variant>.json. Each of those lists contains one
required mob with weight 10: basalt magma_cube, crimson zoglin, soul skeleton,
warped strider and wasteland zombified_piglin. The original basalt template also
contains zombified-piglin spawner data; that data is replaced, not an additional
effective source. Ocean and taiga templates have no ordinary spawners.

The existing repurposed-mansion-processors identities and SpawnerRandomizingProcessor
inspection establish replacement of spawner NBT with selected SpawnData and a
single weight-one SpawnPotentials entry. MobSpawnerManager failure/fallback paths
remain preserved in that source record. These valid packaged lists identify
configured sources, not observed spawning or encounter counts. Magma cubes,
zoglins and skeletons support hostile potential; zombified piglins are neutral
until provoked, striders non-hostile, and pufferfish a contact hazard. Empty root
spawn overrides leave natural biome spawning separate from authored sources.

The authoritative loot_table_source mapping retains 15 distinct literal tables:
seven chests/temples/{basalt,crimson,ocean,soul,taiga,warped,wasteland}, seven
dispensers/temples/{basalt,crimson,soul,taiga,warped,wasteland,wasteland_lava}, and
trapped_chests/temples/warped, all in the repurposed_structures namespace.
The ocean processor adds archaeology/temple_ocean to suspicious gravel through
its structure_surface_processor delegate rules. All 16 corresponding definitions
exist in the packaged JSON catalog under data/repurposed_structures/loot_table/.
These are source references, not guaranteed contents, counts or trap operation.

The existing repurposed-monument-processors capture binds structure_surface_processor
to CappedStructureSurfaceProcessor. Its surface predicates and delegate rules
control eligibility; unseeded Collections.shuffle ordering remains a limitation.
Noise replacement preserves NBT and does not add entities or loot itself. Taiga
uses only structure_void_processor. Direct inspection of the pinned candidate
repurposed_structures-7.5.21+1.21.1-neoforge.jar member
com/telepathicgrunt/repurposedstructures/world/processors/StructureVoidProcessor.class
(SHA-256 5b9fce8fbb951f275f4d2d048063f7f56259d372a0488edaf0e78813886120f6)
shows processBlock returns null for STRUCTURE_VOID, otherwise the incoming block
info unchanged. It adds no entities or loot. The initial lookup for a class named
StructureSurfaceProcessor failed; the existing registration capture identifies
the actual CappedStructureSurfaceProcessor class used above.

Existing world-bounds evidence for run-a/mountainous/chunks.jsonl line 2198,
seed 6671238423019257953, full Nether crimson start chunk 9,4, records envelope
[138,60,57,149,73,71]. Inclusive coordinate differences give size 12x14x15:
footprint 12x15 and vertical extent 14 blocks. This is a saved-piece envelope
example, not occupied geometry, exposed height or a bound for all seven variants.

The five Nether roots select GenericNetherJigsawStructure HIGHEST_LAND with
offset -4. Ocean selects OCEAN_FLOOR_WG, AVERAGE_LAND, offset -3 and maximum-Y
allowance 51. Taiga selects WORLD_SURFACE_WG, AVERAGE_LAND and offset -3.
All have no terrain adaptation. These settings support terrain-associated partial
burial, ocean seabed intent and qualitative entrance-obscuration descriptions;
they do not measure individual block exposure or sightlines. Assembly source
identities, packaged catalogs and world bounds are bound in the family decision.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/repurposed-temple-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -p -c -classpath downloads/item3/candidates/repurposed_structures-7.5.21+1.21.1-neoforge.jar com.telepathicgrunt.repurposedstructures.world.processors.StructureVoidProcessor
```

Use a fresh inventory output path. Only temple and input identity may change.
Source inspection supports descriptions; existing tests cover integration and
evidence paths. Item 8 final acceptance and delivery remain open.
