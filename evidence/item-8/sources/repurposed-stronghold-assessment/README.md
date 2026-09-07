# Repurposed stronghold assessment

Seven remaining requirements are integrated for two variants/45 pool-traced
templates. Existing End full-start geometry remains accepted under
repurposed-final-geometry. No runtime capture or new tool is needed.

## Content and spawn sources

The trace resolves components with no missing inputs, unresolved template entity
sources or generation markers. End templates author endermen and endermites;
Nether authors wither skeletons. End additionally selects mobs/shulker_mob,
whose existing repurposed-feature-roles capture creates a persistent shulker and
adds it with passengers. Chain decoration features are separate physical content.

Ordinary spawners occur in fountain,pillar,storage crossings and portal rooms.
Their original blaze/endermite NBT is replaced by selected spawner processors:

- strongholds/end and end_portal_room: sole endermite,weight10.
- strongholds/nether: blaze50,zoglin30,zombified_piglin20.
- strongholds/nether_portal_room: sole blaze,weight10.

These four packaged lists contain required vanilla entities. The existing
SpawnerRandomizingProcessor/MobSpawnerManager capture in
repurposed-mansion-processors explains weighted selection and replacement NBT;
its missing-list/null/error fallback paths remain distinct. No trial spawners
are present. General Nether spawners must not be described as exclusively blaze.
Weights and source blocks are not live populations or guaranteed generated counts.

Natural monster overrides use piece bounds. End selects endermite weight100,
min2/max4. Nether selects blaze weight10,group2..3; zombified_piglin weight3,group4;
wither_skeleton weight10,group5; skeleton weight2,group5; magma_cube weight3,group4.
These are distinct from authored templates/features/spawners. Endermen have
conditional hostility, zombified piglins are neutral until provoked. Other
selected enemies support hostile potential without a difficulty tier.

Six literal loot definitions exist: chests/strongholds/nether_hallway,
nether_library,nether_storage_room and shulker_boxes/strongholds/end_hallway,
end_library,end_storage_room, all in repurposed_structures. Exact template
associations remain in the inventory. Material/spawner/fluid/portal processors
append no table source. No guaranteed contents or reward quantities are claimed.

## Processor and placement limits

Portal-room lists select fill_end_portal_frame_processor probability_per_block0.1.
Direct pinned candidate member
com/telepathicgrunt/repurposedstructures/world/processors/FillEndPortalFrameProcessor.class
has SHA-256 d388eaf44d1bb95425f8a4c8dc3f505cd42aab012c19566711a6ab2644a6a12e.
Its processBlock handles END_PORTAL_FRAME, draws nextFloat from the placement
position random, sets HAS_EYE according to probability, and preserves NBT. Other
blocks pass through. It does not create portal interior blocks or prove an active
portal, and does not spawn an entity or append loot.

Selected Nether fluid-source closing uses replacement gilded blackstone,
blackstone and cracked polished blackstone bricks; general spawner processing
sets ignore_down. These are fluid-boundary material operations, not extra enemy
sources. Selected noise/random/material rules likewise do not append loot or
create infestation. No claim of perfect liquid containment is made.

Nether generic jigsaw starts26..29 with allowedY4..35; End starts3..6 with
vertical_distance_from_start_piece45. Both have no terrain adaptation.
Existing StrongholdEndStructure.extraSpawningChecks first applies the base check,
then samples four horizontal directions at offsets70 and35 from the start chunk
origin, followed by the center. getHeightAt updates the running minimum as
min(previous,WORLD_SURFACE_WG height)-1, preserving the cumulative subtraction.
It rejects samples below min(maxTerrainLimit,generatorMinY+45). This is a land
eligibility check, not measured cover depth or proof of whole-layout burial.
Source identity is bound by repurposed-assembly.

Low-elevation corridor/room architecture supports underground/under-island intent.
Caves or excavation may expose it. Neither the source settings nor the accepted
saved-piece example establishes sightlines, visible entrances or occupied volume.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/repurposed-stronghold-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -p -c -classpath downloads/item3/candidates/repurposed_structures-7.5.21+1.21.1-neoforge.jar com.telepathicgrunt.repurposedstructures.world.processors.FillEndPortalFrameProcessor
```

Use a fresh output path. Only stronghold and input identity may change. Existing
captured source/catalog identities are bound in the family decision. Item8 final
acceptance and PR/review/main delivery remain open.
