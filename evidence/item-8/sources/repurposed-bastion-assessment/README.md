# Repurposed underground bastion assessment

Seven remaining requirements are integrated for one family/162 pool-traced
templates. Existing full-start geometry remains in repurposed-final-geometry.
No runtime capture or new tool is needed.

## Enemy sources

The pool trace resolves all components without unresolved template entities or
generation markers. Its only directly authored entity is a bat. Eight terminal
features supply the authored enemies: mobs/skeleton_bow, skeleton_bow_deadly,
skeleton_bow_deadliest, skeleton_sword, skeleton_sword_deadly,
skeleton_sword_deadliest, skeleton_horseman_bow and skeleton_horseman_sword,
all in repurposed_structures. Matching placed/configured definitions are in the
packaged JSON catalog. These are components, not eight new families.

Existing Skeletons and SkeletonHorseman captures in repurposed-feature-roles
create skeletons or a skeleton horse and skeleton, finalize with STRUCTURE spawn
reason, apply configured equipment/attributes and add entities with passengers.
Horseman code installs the skeleton in the horse passenger list via EntityAccessor;
it is not evidence of an independently observed successful riding interaction.
Persistent source flags and configured health/speed/equipment are recorded in
those immutable inputs. Bow/sword variants and names containing deadly/deadliest
must not be converted into an observed difficulty ranking. Populations, equipment
drops and combat performance are not measured by this inventory assessment.

Treasure water_basin has an ordinary skeleton spawner. treasure_rooms selects
spawner_randomizing_processor with rs_spawners/bastions/underground, a sole
required minecraft:skeleton entry at weight10 and block-light0..7. Existing
SpawnerRandomizingProcessor/MobSpawnerManager captures establish selected NBT
replacement and preserve failure paths. No trial spawners occur in the trace.
The root separately overrides piece-bounded natural monster spawning with
skeleton weight10,min1/max4. These natural parameters, authored features and
spawner sources are distinct. The template bat is non-hostile.

## Loot, processor and placement evidence

Four literal loot definitions exist under chests/bastions/underground/:
bridge,other,skeleton_horse_stable,treasure. Exact template associations remain
in the inventory. Feature equipment is separate from container table sources.
No guaranteed contents, drop quantities or completed encounter is inferred.

Selected processor lists apply material degradation, random wood replacement,
floating-block removal and fluid-source closing; housing also uses the already
captured ForcePlaceMushroomBlocksProcessor. Fluid closing selects deepslate with
if_air_in_world and ignore_down enabled. These material operations do not
establish complete enclosure or watertightness. Treasure spawner selection is
the distinct enemy-bearing processor noted above.

Direct pinned candidate member
com/telepathicgrunt/repurposedstructures/world/processors/RemoveFloatingBlocksProcessor.class
has SHA-256 a7014124be7af5f983e3abd00156dd7e1cc9f876f32590430f41455303f1d0a9.
Its processBlock applies a center-chunk guard and, for incoming air, direct writes
and survival checks above and horizontally adjacent to the position. It returns
incoming block info, not an entity or loot assignment. These side effects are
not a measurement of final visible architecture. Source/material rules do not
replace an actual saved-piece envelope with a template-size estimate.

The generic jigsaw root starts atY-45, size10, generation step underground_structures,
no terrain adaptation and biome radius check7. The accepted assembled example
extends above the start; startY is not total height or burial depth. Ramparts,
bridges, housing and treasure rooms give local architectural cues when exposed
through caves or excavation. No surface entrance or sightline is guaranteed.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/repurposed-bastion-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -p -c -classpath downloads/item3/candidates/repurposed_structures-7.5.21+1.21.1-neoforge.jar com.telepathicgrunt.repurposedstructures.world.processors.RemoveFloatingBlocksProcessor
```

Use a fresh output path. Only bastion and input identity may change. Existing
feature/assembly/processor identities are bound in the family decision. Final
Item8 acceptance and PR/review/main remain open.
