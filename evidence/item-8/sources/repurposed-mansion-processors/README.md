# Mansion content processors and spawner source

Captured at extractor revision ea00bb9. All four captures and identities.json
reproduced byte for byte before this README was added:

```sh
uv run -m tools.inspect_item8_pool_elements --archive repurposed_structures-7.5.21+1.21.1-neoforge.jar --class-name com/telepathicgrunt/repurposedstructures/world/processors/ForcePlaceMushroomBlocksProcessor.class --class-name com/telepathicgrunt/repurposedstructures/world/processors/SpawnerRandomizingProcessor.class --class-name com/telepathicgrunt/repurposedstructures/misc/mobspawners/MobSpawnerManager.class --class-name com/telepathicgrunt/repurposedstructures/misc/mobspawners/MobSpawnerObj.class --output evidence/raw/item8/repurposed-mansion-processors-ea00bb9
```

ForcePlaceMushroomBlocksProcessor handles only MushroomBlock instances: it
writes the supplied state directly to the chunk at the supplied position and
returns null to suppress ordinary placement. Other block info is unchanged.
It does not assign entities, spawners or loot and does not extend the position.

SpawnerRandomizingProcessor handles SpawnerBlock states only. It obtains a
position-based random from placement settings, selects an entity through
MobSpawnerManager and creates new NBT with configured timing/range values,
SpawnData and a single weight-one SpawnPotentials entry for that same entity.
Optional block/sky light ranges are copied to custom_spawn_rules. If selection
returns null, it replaces the spawner with replacementState and null NBT.
Other blocks, including chest loot data, are unchanged by this processor.
The source template's original spawner NBT is therefore not the accepted
effective enemy source without resolving the referenced spawner data.

MobSpawnerManager reads the rs_spawners resource directory and its mobs lists.
It resolves entity names, removes zero weights and unresolved optional entities,
and rejects negative surviving weights. Missing required entities or parse
exceptions are logged; the rejected list is not inserted. A missing list falls
back to the dungeon mob array, zero total weight returns null, and an exception
during weighted selection logs and returns pig. These failure paths must remain
distinct from the selected valid mansion list. MobSpawnerObj checks registry
membership and throws for missing nonoptional entities.

Next: bind the eight selected mansion rs_spawners documents and processor lists,
then attribute effective enemy IDs alongside child templates. Resource listener
registration and preserved logs remain separate from this method inspection.
Do not infer live spawning, accepted reload state or encounter counts from the
source alone. Scoped extractor Ruff and Basedpyright passed. No new measurement.

## Selected mansion spawner data

The focused test now binds all eight selected rs_spawners mansion lists. Each
contains only minecraft:spider with weight 100, with identical SHA-256
39439a1a2e54f048e0e61d770536233ccf68443f48fb0188fda1d46958bc7dc0.
Each matching processor list references that variant's spawner resource and
block-light range 0..7. Mushroom lists contain only the captured mushroom
processor. These are selected packaged inputs to the inspected manager, not
proof of listener registration, successful reload or live spawning.

```sh
uv run pytest -q tests/item8/test_mansion_components.py
```

The first test attempt selected every processor list and failed on an unrelated
competing repurposed_structures:villages/bamboo/crop_randomizer definition.
Selection is now limited to mansion processor resource identities, including
their competing candidates. The village conflict is not resolved or suppressed
for its own consumers. Static checking then found two missing supported kind
annotations and an invariant list type mismatch. The selector's existing JSON
selection behavior needs no change: its declared kinds now include the two
current consumers, and the filtered list has the required JsonValue annotation.
The resulting overlong line was split after Ruff rejected it. Final validation:
10 mansion/resource-selection tests passed; scoped Ruff and Basedpyright passed.
