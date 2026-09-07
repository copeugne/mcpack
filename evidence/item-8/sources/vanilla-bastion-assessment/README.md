# Bastion remnant family assessment

This assessment reuses the existing runtime/biome join, packaged JSON/template
catalog, pool trace and world-bounds evidence already hash-bound in the family.
No new capture, extractor or measurement tool is required.

The root starts at absoluteY33 with size6,distance80 and no heightmap projection.
The starts pool selects four equally weighted rigid components: units/air_base,
hoglin_stable/air_base,treasure/big_air_full and bridge/starting_pieces/entrance_base.
They are alternatives of one family.167 reachable templates have no missing
components in the retained trace. Five carry entity NBT:

| Template under minecraft:bastion/mobs | Actual entity ID |
|---|---|
| crossbow_piglin | minecraft:piglin |
| hoglin | minecraft:hoglin |
| melee_piglin | minecraft:piglin_brute |
| melee_piglin_always | minecraft:piglin_brute |
| sword_piglin | minecraft:piglin |

minecraft:bastion/treasure/bases/lava_basin has the ordinary spawner compound at
/block_entities/6,position11,7,19. SpawnData is magma_cube, with one weight1 magma-
cube potential. Delay0,min/max delay200/800,SpawnCount4,MaxNearbyEntities6,
RequiredPlayerRange16,SpawnRange4 are preserved in the family attribute. These
are configured inputs, not a measured rate or a guaranteed spawner per bastion.
No DATA encounter markers or unresolved entities occur in the retained trace.
Authored template mobs and the treasure spawner establish encounter provenance;
empty root spawn_overrides does not exclude natural or external entity sources.

Literal loot sources are chests/bastion_bridge,bastion_hoglin_stable,bastion_other
and bastion_treasure in the Minecraft namespace. All have packaged definitions.
The12 selected processor lists are bastion_generic_degradation,bottom_rampart,
bridge,entrance_replacement,high_rampart,high_wall,housing,rampart_degradation,
roof,side_wall_degradation,stable_degradation and treasure_rooms. Inspection of
their complete packaged documents shows block rules for cracked/normal/gilded
blackstone,gold,magma and air, including a height-dependent air rule in high_rampart.
No loot appenders or entity-spawning actions occur in these processor documents.
This does not measure final loot or rule out external retained hooks.

One existing full-start assembly supplies approximate size: run-a/biome-diverse/
chunks.jsonl line1032,seed-3503646078644842058,chunk-9,13,envelope
[-175,31,192,-120,95,255],size56x65x64. It includes air/padding and is not occupied
volume,typical/all-layout size or complete piece-population proof. Four start
choices do not require four families or imply this sample represents every layout.

Blackstone ramparts,walls,bridges and multi-storey rooms provide visual cues where
exposed. Nether terrain may enclose them. The absolute anchor and observedY31..95
support cavern/terrain-associated vertical placement; surface_structures is a
pipeline label, not proof of open sky or full burial. No guaranteed entrance,
sightline distance or exploration pacing is claimed.
