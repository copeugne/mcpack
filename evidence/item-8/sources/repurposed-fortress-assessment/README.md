# Repurposed jungle fortress assessment

Seven remaining requirements are integrated for one family/17 pool-traced
templates. Existing saved geometry is accepted under repurposed-final-geometry.
No runtime capture or new tool is needed.

## Enemy and loot sources

The trace has no directly authored entities, unresolved entity sources, missing
components or generation markers. The selected mobs/drowned_with_armor feature
is nevertheless an authored enemy source. Its existing DrownedWithArmor capture
in repurposed-feature-roles rejects a nonwater origin or null entity creation;
otherwise it equips a drowned, marks persistence, finalizes spawning and adds it
with passengers. Equipment choices and successful populations are not inferred
from a feature reference. Other selected features are structure/vine breakage
and vines, not independent families.

The jungle/spawner template contains an ordinary silverfish spawner. jungle_main
selects spawner_randomizing_processor, rs_spawners/fortresses/jungle, with one
required silverfish at weight10 and block-light0..7. Existing manager/processor
captures in repurposed-mansion-processors bind replacement NBT and retain failure
paths. No trial spawner occurs in the trace.

Root piece-bounded natural monster overrides are separate: wither_skeleton
weight1,group1; skeleton weight10,group1..3; zombie weight10,group1..4; spider
weight10,group1..3; creeper weight5,group1..2; enderman weight3,group1..2; witch
weight2,group1..2. These are selection inputs, not observed group counts.

Three literal chest tables are defined: chests/fortresses/jungle_center,
jungle_hallway,jungle_shrine. jungle_main additionally selects
structure_surface_processor with delegate rules appending
repurposed_structures:archaeology/fortress_jungle to suspicious gravel from
matching stone/cracked/mossy stone-brick states. All four table definitions exist.
Existing CappedStructureSurfaceProcessor inspection in repurposed-monument-processors
preserves surface predicates, unseeded shuffle and changed-result handling.
Random rule probabilities do not establish archaeological counts or availability.
Pillar child processing does not invoke finalizeProcessing, so archaeology is not
inferred on extended pillars merely from their delegate reference.

## Placement, flooding and limits

The root uses generic jigsaw startY56..65, size10, vertical-distance35, biome
radius4 and no terrain adaptation. This is terrain-associated fortress intent;
startY is not final occupied height or burial depth. Ruined masonry, corridors
and vines provide local cues, with jungle cover, terrain and flooding potentially
obscuring them. No sightline or visible entrance is guaranteed.

Both jungle_main and jungle_fungus select flood_with_water_processor level62.
Direct pinned candidate member
com/telepathicgrunt/repurposedstructures/world/processors/FloodWithWaterProcessor.class
has SHA-256 903520feca0e466b1d29317ed07ac948fcf073003ca593868dc8c71da6e2f9b3.
Incoming water delegates fluid ticking and returns. Other processing applies a
center-chunk guard and Y<=floodLevel. Eligible air, pots, buttons and water-replaceable
states become water; supported waterlogging is enabled, and BushBlock handling
can also replace with water. Replacement water uses null NBT; waterlogging
preserves incoming NBT. Changed flooded blocks can cause neighboring nonoccluding,
fluid-empty positions, excluding upward direction, to be filled with cracked
stone bricks. This is a source-level flooding rule, not measured water depth,
complete containment or proof that the drowned feature succeeds.

Other processors perform material changes, pillar extension, floating-block
removal and mushroom-block placement. Their existing captures/direct inspection
are recorded in repurposed-monument-processors, repurposed-bastion-assessment and
repurposed-mansion-processors. Red-glass pillar replacements are stone bricks;
the jungle_main self-list does not reintroduce the trigger. Support extension
and direct block writes remain outside the saved-piece occupied-volume claim.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/repurposed-fortress-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -p -c -classpath downloads/item3/candidates/repurposed_structures-7.5.21+1.21.1-neoforge.jar com.telepathicgrunt.repurposedstructures.world.processors.FloodWithWaterProcessor
```

Use a fresh output path. Only fortress and input identity may change. Existing
catalog/assembly/feature/processor identities are bound in the family decision.
Final Item8 acceptance and PR/review/main remain open.
