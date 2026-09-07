# BCLib common-hooks

Extractor 60bc470e84bcc2e06f94158848060814dfccd917. Independent r1 reproduction matches every
disassembly and identity manifest byte. Manifest SHA-256:
909cc6737418099310e6cabfedcc22048e089b2fc1c386946ff00847f7e9447f

```sh
uv run -m tools.inspect_item8_pool_elements --archive bclib-21.0.24.jar --class-name org/betterx/bclib/mixin/common/AnvilBlockMixin.class --class-name org/betterx/bclib/mixin/common/AnvilMenuMixin.class --class-name org/betterx/bclib/mixin/common/ComposterBlockAccessor.class --class-name org/betterx/bclib/mixin/common/CraftingMenuMixin.class --class-name org/betterx/bclib/mixin/common/EnchantingTableBlockMixin.class --class-name org/betterx/bclib/mixin/common/IdMapperAccessor.class --class-name org/betterx/bclib/mixin/common/IdMapperDebugMixin.class --class-name org/betterx/bclib/mixin/common/LayerLightSectionStorageMixin.class --class-name org/betterx/bclib/mixin/common/LootPoolMixin.class --class-name org/betterx/bclib/mixin/common/PistonBaseBlockMixin.class --class-name org/betterx/bclib/mixin/common/PortalShapeMixin.class --class-name org/betterx/bclib/mixin/common/RecipeManagerMixin.class --class-name org/betterx/bclib/mixin/common/RecipeMixin.class --class-name org/betterx/bclib/mixin/common/ShovelItemAccessor.class --class-name org/betterx/bclib/mixin/common/SurfaceRulesContextAccessor.class --class-name org/betterx/bclib/mixin/common/boat/BoatItemMixin.class --class-name org/betterx/bclib/mixin/common/boat/BoatMixin.class --class-name org/betterx/bclib/mixin/common/boat/ChestBoatMixin.class --class-name org/betterx/bclib/mixin/common/elytra/LivingEntityMixin.class --class-name org/betterx/bclib/mixin/common/shears/BeehiveBlockMixin.class --class-name org/betterx/bclib/mixin/common/shears/MatchToolMixin.class --class-name org/betterx/bclib/mixin/common/shears/MushroomCowMixin.class --class-name org/betterx/bclib/mixin/common/shears/PumpkinBlockMixin.class --class-name org/betterx/bclib/mixin/common/shears/SheepMixin.class --class-name org/betterx/bclib/mixin/common/shears/SnowGolemMixin.class --class-name org/betterx/bclib/mixin/common/shears/TripWireBlockMixin.class --class-name org/betterx/bclib/mixin/common/signs/BlockEntityTypeMixin.class --output evidence/raw/item8/bclib-common-hooks-r1
```

The remaining 27 declared common hooks handle existing anvil/crafting/recipe,
loot-list, lighting, piston, portal, boat, elytra, shears and sign operations,
registry ID diagnostics and registry/surface accessors. Combined with the eight
generation hooks in bclib-provider-entry, all 35 declared common hooks are
retained. Consumer gameplay effects remain relevant; these hooks do not supply
an independent architectural family.

Whole-provider closure still requires the nested library disposition and final
payload binding. Do not treat these captures alone as Item 8 completion.
