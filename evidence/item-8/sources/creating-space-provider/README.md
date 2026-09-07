# Creating Space generation entry sources

Extractor c212c8a7e2f61d354075449d4eff1a16bbf0e70c. Manifest SHA-256: eba1da2e07326fc6b3f57060d05bc7130695911a5fc118be589e2e09a1a515c4. Independent r1 matches every generated file.

The 39 sources cover thirteen annotated entries, nineteen declared mixins and their plugin, and six indexed generation-reference classes. Capture is not provider closure; interpret the entry paths and resource consumers before accepting coverage.

```sh
uv run -m tools.inspect_item8_pool_elements --archive creatingspace-1.21.1-1.7.18.jar --class-name com/rae/creatingspace/CreatingSpace.class --class-name com/rae/creatingspace/CreatingSpaceClient.class --class-name com/rae/creatingspace/configs/CSConfigs.class --class-name 'com/rae/creatingspace/content/event/CSClientEvent$ModBusEvents.class' --class-name com/rae/creatingspace/content/event/CSClientEvent.class --class-name 'com/rae/creatingspace/content/event/CSEventHandler$ModBusEvents.class' --class-name com/rae/creatingspace/content/event/CSEventHandler.class --class-name com/rae/creatingspace/content/event/DataEventHandler.class --class-name com/rae/creatingspace/content/event/IgniteOnPlace.class --class-name com/rae/creatingspace/content/life_support/spacesuit/CopperOxygenBacktankFirstPersonRenderer.class --class-name com/rae/creatingspace/content/life_support/spacesuit/NetheriteDivingHandler.class --class-name com/rae/creatingspace/content/life_support/spacesuit/NetheriteOxygenBacktankFirstPersonRenderer.class --class-name com/rae/creatingspace/content/life_support/spacesuit/SpacesuitHelmetItem.class --class-name 'com/rae/creatingspace/content/planets/worldgen/CraterCarver$1.class' --class-name com/rae/creatingspace/content/planets/worldgen/CraterCarver.class --class-name com/rae/creatingspace/content/planets/worldgen/CraterCarverConfig.class --class-name com/rae/creatingspace/content/rocket/RocketContraptionEntity.class --class-name com/rae/creatingspace/content/rocket/contraption/RocketContraption.class --class-name com/rae/creatingspace/init/worldgen/CarverInit.class --class-name com/rae/creatingspace/mixin/CSMixinPlugin.class --class-name com/rae/creatingspace/mixin/WindowResizeMixin.class --class-name com/rae/creatingspace/mixin/entity/ContraptionMixin.class --class-name com/rae/creatingspace/mixin/entity/EntityMixin.class --class-name com/rae/creatingspace/mixin/entity/LivingEntityMixin.class --class-name com/rae/creatingspace/mixin/entity/PlayerMixin.class --class-name com/rae/creatingspace/mixin/entity/gravity/BoatMixin.class --class-name com/rae/creatingspace/mixin/entity/gravity/FallingBlockEntityMixin.class --class-name com/rae/creatingspace/mixin/entity/gravity/ItemEntityMixin.class --class-name com/rae/creatingspace/mixin/entity/gravity/LivingEntityMixin.class --class-name com/rae/creatingspace/mixin/entity/gravity/MinecartMixin.class --class-name com/rae/creatingspace/mixin/entity/gravity/PrimedTntMixin.class --class-name com/rae/creatingspace/mixin/fluid/FluidInteractionRegistryMixin.class --class-name com/rae/creatingspace/mixin/kinetics/BacktankBlockEntityMixin.class --class-name com/rae/creatingspace/mixin/recipe/DataComponentIngredientMixin.class --class-name com/rae/creatingspace/mixin/recipe/ItemApplicationMixin.class --class-name com/rae/creatingspace/mixin/recipe/ProcessingRecipeMixin.class --class-name com/rae/creatingspace/mixin/recipe/ProcessingRecipeParamsMixin.class --class-name com/rae/creatingspace/mixin/recipe/SequencedAssemblyRecipeMixin.class --class-name com/rae/creatingspace/mixin/recipe/SequencedAssemblyRecipeSerializerMixin.class --output evidence/raw/item8/creating-space-provider-r1
```

## Four registered family assessments

Thirty-five attributes finish the four registered families, four roots and seven
traced templates. This uses the pinned packaged-json, templates-redacted,
pool-traces-content and dimension-biomes catalogs already retained under Item8.
Creating Space templates belong to creatingspace-1.21.1-1.7.18.jar at
data/creatingspace/structure/; the two fallback leg templates belong to the
nested vanilla server archive identified by the trace. Exact per-template NBT
loot paths remain in the inventory. No new runtime capture or tool is required.

Mars start_pool selects one weight-one rigid mars/test_mars template with empty
processors, size25x37x31 and no jigsaw blocks. The pool fallback references
minecraft:bastion/bridge/legs, but those two 3x22x3 templates are not appended
to a connector-free primary template. Their traversal presence is not an
assembled footprint or additional encounter. This corrects the earlier rationale
that described them simply as structural components. Normal root selection uses
the primary template; its footprint25x31 and height37 retain source air/padding.

Moon outpost top is15x12x15; basement15x9x15. Top block_entities/0 connector at
(7,0,7) points down_west, is rollable and targets minecraft:staircase. Basement
block_entities/73 at(7,8,7) points up_south and has that name. The parent's
rollable joint permits horizontal rotation; the centered square dimensions
preserve footprint15x15. In the unrotated matching-facing example, basement
origin=(7,0,7)+(0,-1,0)-(7,8,7)=(0,-9,0). Its Y-9..-1 joins top Y0..11,
total21. Both pools select one rigid weight-one piece with empty processors.
This is nominal source architecture, not proof of actual placement or exposure.
Existing Rocket8x4x7 and Ship29x6x20 source dimensions are preserved.

Mars main saves one armor stand with basic spacesuit boots/leggings/helmet and
copper oxygen backtank, one glow item frame with extendo_grip, and two Create
glue entities. It saves no inhabitants. The other selected templates save no
top-level entities. None contains ordinary/trial spawners; all root spawn
overrides are empty. The inventory does not equate lack of authored enemies
with safe planetary conditions or functioning life support.

Mars barrel block_entities0/1/15/49/51/52 reference underground_mars_outpost;
27 references ground_mars_outpost, under creatingspace:chests/. Its cryogenic
tank158 saves Fluid Amount0. Rocket barrel5 references
creatingspace:crashed_rocket_loot; tank12/13/21/23 contents are empty, and
chute24/29/31/32/33 items are air Count0. Copycat Item compounds are saved
building materials, not container loot. Ship has only two sliding-door block
entities, with no table or fixed inventory payload.

Moon basement has no loot-table reference but does save fixed contents.
block_entities/29 contains a clipboard maintenance page about oxygen, repairs
and departure. Tank0 saves flowing_liquid_oxygen Amount2536; air_liquefier34
OutputTanks/0 saves Amount984 of that fluid, with second output empty. Amounts
are retained source units, not measured usable reserves. Brewing stand30 has
empty Items. Use the selected basement path, not the unselected combined
moon/abandoned_outpost.nbt template. Equipment operation, conversion of legacy
NBT, recoverability and survival of saved contents are not tested here.

Captured dimension biome intersections place mars_plains only in
creatingspace:mars and moon_plains only in creatingspace:the_moon. Mars root
projects OCEAN_FLOOR with offset-30; Rocket WORLD_SURFACE with offset+1;
Ship OCEAN_FLOOR with offset+1; Moon outpost WORLD_SURFACE_WG with offset0.
These placement rules and source forms support qualitative discoverability,
not measured sight distance, exposed height or exploration pace.

Rebuild: `uv run -m tools.build_item8_inventory --output <absent-path>`.
Validation: `uv run pytest -q tests/item8/test_creating_space_provider_scope.py tests/item8/test_inventory_sources.py`.

Inventory SHA-256: `41237d2aaa4fd87e555c80d88fc8b1b79d4f21ce64b65752a3973f9ef072f1da`.

Eight focused tests pass. Semantic comparison changes only the four family
assessments and decisions identity; registry membership, biome constraints,
world observations and existing wreck geometry remain unchanged.
