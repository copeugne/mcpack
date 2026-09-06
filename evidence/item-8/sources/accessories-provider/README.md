# Accessories provider boundaries

Extractor fcc3d8a09d0e3f00f7133785135428df2a27abb1. Independent r1 reproduction
matches all 36 disassemblies and the identity manifest. Manifest SHA-256:
93c8d040e59e2df4b2b46de805f7bb529018b99c9e275a765c6b4f5a9295a646

```sh
uv run -m tools.inspect_item8_pool_elements --archive accessories-neoforge-1.1.0-beta.53+1.21.1.jar --class-name io/wispforest/accessories/mixin/AccessoriesMixinPlugin.class --class-name io/wispforest/accessories/mixin/ApplyBonusCountMixin.class --class-name io/wispforest/accessories/mixin/ArmorSlotMixin.class --class-name io/wispforest/accessories/mixin/ConfigurableRegistryLookupAccessor.class --class-name io/wispforest/accessories/mixin/CraftingMenuAccessor.class --class-name io/wispforest/accessories/mixin/CriteriaTriggersAccessor.class --class-name io/wispforest/accessories/mixin/DelegatingOpsAccessor.class --class-name io/wispforest/accessories/mixin/EnchantedCountIncreaseFunctionMixin.class --class-name io/wispforest/accessories/mixin/EnchantmentAttributeEffectMixin.class --class-name io/wispforest/accessories/mixin/EnchantmentHelperMixin.class --class-name io/wispforest/accessories/mixin/EndermanMixin.class --class-name io/wispforest/accessories/mixin/EntityTrackerAccessor.class --class-name io/wispforest/accessories/mixin/EquipmentSlotMixin.class --class-name io/wispforest/accessories/mixin/EquipmentSlotTypeMixin.class --class-name io/wispforest/accessories/mixin/HolderLookupAdapterAccessor.class --class-name io/wispforest/accessories/mixin/InventoryMixin.class --class-name io/wispforest/accessories/mixin/ItemStackAccessor.class --class-name io/wispforest/accessories/mixin/LivingEntityAccessor.class --class-name io/wispforest/accessories/mixin/LivingEntityMixin.class --class-name io/wispforest/accessories/mixin/PatchedDataComponentMapMixin.class --class-name io/wispforest/accessories/mixin/PigEntityMixin.class --class-name io/wispforest/accessories/mixin/PiglinAiMixin.class --class-name io/wispforest/accessories/mixin/PlayerMixin.class --class-name io/wispforest/accessories/mixin/PowderSnowBlockMixin.class --class-name io/wispforest/accessories/mixin/RegistryOpsAccessor.class --class-name io/wispforest/accessories/mixin/ServerChunkLoadingManagerAccessor.class --class-name io/wispforest/accessories/mixin/SlotAccessor.class --class-name io/wispforest/accessories/mixin/StateHolderAccessor.class --class-name io/wispforest/accessories/mixin/StriderMixin.class --class-name io/wispforest/accessories/mixin/owo/ConfigWrapperAccessor.class --class-name io/wispforest/accessories/mixin/temp_fixes/NbtCompoundMixin.class --class-name io/wispforest/accessories/mixin/temp_fixes/NbtUtilsMixin.class --class-name io/wispforest/accessories/neoforge/AccessoriesForge.class --class-name io/wispforest/accessories/neoforge/client/AccessoriesClientForge.class --class-name io/wispforest/accessories/neoforge/mixin/AccessoriesNeoforgeMixinConfig.class --class-name io/wispforest/accessories/neoforge/mixin/curios/CurioInventoryMixin.class --output evidence/raw/item8/accessories-provider-r1
```

The capture covers two automatic entries, all 32 common hooks and both mixin
plugins. Entries register accessory capabilities, commands, data synchronization,
equip/use/drop handling and existing living-entity/world tick callbacks.
The common hooks extend inventory, equipment, enchantment/loot, entity behavior,
NBT and accessors; these are not automatically generated structure families.

Both plugins return empty extra-mixin lists. The common plugin can disable
temporary NBT fixes when a configuration marker exists and logs an old-world
warning. The NeoForge plugin enables its Curios hook only when curios is
present and cclayer is absent. Preserve those conditions without claiming
compatibility or altering the frozen configuration.

Accessories.init and AccessoriesEventHandler are the remaining direct
initialization/event delegates to inspect before whole-provider closure.
No family or provider-count change is claimed by this partial capture.
