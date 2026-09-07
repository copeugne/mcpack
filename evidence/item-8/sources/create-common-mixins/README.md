# Create declared common mixins

Extractor: 969a3d94fb48c503d9503c187a362917f184e9d8.
All 43 common mixins declared in create.mixins.json are retained in full,
including annotations. An independent capture reproduces byte-for-byte.
This isolated generated increment is the complete declared common-hook batch;
it excludes already captured plugin code and separately declared client hooks.

```sh
uv run -m tools.inspect_item8_pool_elements --archive create-1.21.1-6.0.10.jar \
  --class-name com/simibubi/create/foundation/mixin/ArmorTrimMixin.class \
  --class-name com/simibubi/create/foundation/mixin/BeehiveBlockMixin.class \
  --class-name com/simibubi/create/foundation/mixin/BlockItemMixin.class \
  --class-name com/simibubi/create/foundation/mixin/BlockMixin.class \
  --class-name com/simibubi/create/foundation/mixin/BuiltInRegistriesMixin.class \
  --class-name com/simibubi/create/foundation/mixin/CustomItemUseEffectsMixin.class \
  --class-name com/simibubi/create/foundation/mixin/EnchantedCountIncreaseFunctionMixin.class \
  --class-name com/simibubi/create/foundation/mixin/EntityMixin.class \
  --class-name com/simibubi/create/foundation/mixin/ItemStackMixin.class \
  --class-name com/simibubi/create/foundation/mixin/LavaSwimmingMixin.class \
  --class-name com/simibubi/create/foundation/mixin/MapItemSavedDataMixin.class \
  --class-name com/simibubi/create/foundation/mixin/MobMixin.class \
  --class-name com/simibubi/create/foundation/mixin/PlayerMixin.class \
  --class-name com/simibubi/create/foundation/mixin/ProjectileUtilMixin.class \
  --class-name com/simibubi/create/foundation/mixin/SmithingMenuMixin.class \
  --class-name com/simibubi/create/foundation/mixin/WaterWheelFluidSpreadMixin.class \
  --class-name com/simibubi/create/foundation/mixin/accessor/BlockBehaviourAccessor.class \
  --class-name com/simibubi/create/foundation/mixin/accessor/BlockLootSubProviderAccessor.class \
  --class-name com/simibubi/create/foundation/mixin/accessor/ConcretePowderBlockAccessor.class \
  --class-name com/simibubi/create/foundation/mixin/accessor/CropBlockAccessor.class \
  --class-name com/simibubi/create/foundation/mixin/accessor/DispenserBlockAccessor.class \
  --class-name com/simibubi/create/foundation/mixin/accessor/FallingBlockEntityAccessor.class \
  --class-name com/simibubi/create/foundation/mixin/accessor/FlowingFluidAccessor.class \
  --class-name com/simibubi/create/foundation/mixin/accessor/FluidInteractionRegistryAccessor.class \
  --class-name com/simibubi/create/foundation/mixin/accessor/GameTestHelperAccessor.class \
  --class-name com/simibubi/create/foundation/mixin/accessor/ItemFrameAccessor.class \
  --class-name com/simibubi/create/foundation/mixin/accessor/ItemModelGeneratorsAccessor.class \
  --class-name com/simibubi/create/foundation/mixin/accessor/ItemStackHandlerAccessor.class \
  --class-name com/simibubi/create/foundation/mixin/accessor/LivingEntityAccessor.class \
  --class-name com/simibubi/create/foundation/mixin/accessor/MappedRegistryAccessor.class \
  --class-name com/simibubi/create/foundation/mixin/accessor/MinecartFurnaceAccessor.class \
  --class-name com/simibubi/create/foundation/mixin/accessor/MobEffectInstanceAccessor.class \
  --class-name com/simibubi/create/foundation/mixin/accessor/NbtAccounterAccessor.class \
  --class-name com/simibubi/create/foundation/mixin/accessor/PotionBrewingAccessor.class \
  --class-name com/simibubi/create/foundation/mixin/accessor/ProjectileDispenseBehaviorAccessor.class \
  --class-name com/simibubi/create/foundation/mixin/accessor/ServerLevelAccessor.class \
  --class-name com/simibubi/create/foundation/mixin/accessor/ShapedRecipeAccessor.class \
  --class-name com/simibubi/create/foundation/mixin/accessor/StateHolderAccessor.class \
  --class-name com/simibubi/create/foundation/mixin/accessor/SystemReportAccessor.class \
  --class-name com/simibubi/create/foundation/mixin/accessor/UseOnContextAccessor.class \
  --class-name com/simibubi/create/foundation/mixin/datafixer/BlockPosFormatAndRenamesFixMixin.class \
  --class-name com/simibubi/create/foundation/mixin/datafixer/ItemStackComponentizationFixMixin.class \
  --class-name com/simibubi/create/foundation/mixin/datafixer/V1460Mixin.class \
  --output evidence/raw/item8/create-common-mixins-r1
```
