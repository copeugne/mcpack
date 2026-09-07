# Repurposed outpost assessment

Seven remaining attributes are integrated for one family,18 variants and205
pool-traced templates. Existing oak full-start geometry remains accepted in
repurposed-final-geometry. No additional world capture or tool is needed.

## Enemy and loot sources

The pool-traces-content catalog reports no missing components, unresolved entity
sources, generation markers or ordinary/trial spawners. Template entity mappings
remain explicit in the inventory: land watchtowers author pillagers; four Nether
variants author piglins and tower brutes, with hoglin cages; soul authors zombified
piglins and zoglin cages. End authors phantoms. Ocean authors pufferfish, drowned
and guardian cages. Allays, iron golems, snow golem and mangrove cage slime retain
their source associations. Alternative cages/towers are not guaranteed occupants
of every assembly, and captive helpers are not classified as hostile enemies.

End pool edges also select repurposed_structures:mobs/shulker_mob, with matching
placed/configured feature definitions and the captured ShulkerMob.place method in
repurposed-feature-roles. The method creates a persistent shulker below the feature
origin, selects an attachment face and calls addFreshEntityWithPassengers. This
is an authored feature source absent from the ordinary template entity list;
it is neither an ordinary spawner nor a measured population. The other selected
feature is chorus_plant_checked, a vegetation contribution.

Natural spawn overrides remain separate. Eleven land Overworld variants select
piece-bounded monster pillagers; basalt/crimson/nether_brick/warped select piglin,
soul selects zombified_piglin, and End selects phantom. Each uses weight10 and
min/max1. Ocean instead sets full-bounded water_ambient pufferfish weight10,
min1/max3; ambient,axolotls,creature,misc,monster,underground_water_creature and
water_creature have empty lists. These are category selection rules, not actual
mob counts or a safe-area guarantee. Piglin hostility is conditional; zombified
piglins are neutral until provoked. Pufferfish is a contact hazard.

Eighteen literal loot sources exist:17 chests/outposts/{variant} tables plus
shulker_boxes/outposts/end. Exact template/table associations remain in the
inventory. Definitions are in the packaged catalog's loot_table directory.
No selected support/material processor appends a loot table. Source presence
is not guaranteed reward availability, count or contents.

## Support and placement interpretation

Eleven land Overworld roots use WORLD_SURFACE_WG offset0, beard_thin and a biome
radius check1. End uses WORLD_SURFACE_WG offset0,beard_box,minY55,terrain radius3,
allowed terrain range15 and biome radius2. Ocean uses OCEAN_FLOOR_WG,AVERAGE_LAND,
offset0,maxY42,beard_box. Nether crimson uses HIGHEST_LAND; basalt,nether_brick,soul,
warped use LOWEST_LAND, all offset0/beard_box. The existing repurposed-assembly
captures support these generator interpretations. Tower/camp architecture is a
qualitative landmark; vegetation, terrain and water may obscure access. No
sightline range, block exposure or water depth is measured.

BottomPillarProcessor operates on original template bottom-layer positions
(original Y0), applies center-chunk/land checks, and extends downward through
its replacement predicate. Optional child processor lists process synthetic
block info with null NBT. The processor directly writes the resulting state,
not NBT, and returns original incoming block info. It does not invoke child
finalizeProcessing. This distinguishes support extension from saved-piece bounds
and from loot/entity generation. Referenced bottom_pillar_overworld/nether lists
contain material rules, block-ignore and waterlogging handling, not mob sources.
Nether-brick explicit colored-glass pillar rules use the already captured
PillarProcessor. Support heights and occupied extents remain unmeasured.

WaterlogWhenReplacingWaterProcessor handles incoming states supporting WATERLOGGED,
reads existing water, preserves incoming NBT and sets that property. When water
is present it schedules a zero-delay block tick under its build-height checks.
It does not add mobs or loot. Direct immutable candidate members under
com/telepathicgrunt/repurposedstructures/world/processors/ are:

- BottomPillarProcessor.class SHA-256 4f599f3d0af9cc66a1590c2f6690ead87baa2196ff1cdf1a2dffae0ca7db92e8.
- WaterlogWhenReplacingWaterProcessor.class SHA-256 19f0cf2f618e260067e79c48d69b74916f274dd8fb45211f391d45698fc9659e.

The first lookup used WaterloggingWhenReplacingWaterProcessor and failed; archive
inspection identified the actual WaterlogWhenReplacingWaterProcessor class.
No result from the failed lookup supports this assessment.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/repurposed-outpost-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -p -c -classpath downloads/item3/candidates/repurposed_structures-7.5.21+1.21.1-neoforge.jar com.telepathicgrunt.repurposedstructures.world.processors.BottomPillarProcessor com.telepathicgrunt.repurposedstructures.world.processors.WaterlogWhenReplacingWaterProcessor
```

Use a fresh inventory output path. Only outpost and input identity may change.
Catalog and captured-source identities are bound in the family decision. Final
Item8 acceptance and PR/review/main delivery remain open.
