# fabric-item-api-v1-entry source checkpoint

Extractor f633bf8. Independent r1 reproduction matches the manifest and all
disassembly bytes. Manifest SHA-256: 079c11a09085ddb9668c75ede629e2222a0485498ba7f8bb896c28a4cf3ece8a.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-item-api-v1-11.2.0+0c57911319.jar --class-name net/fabricmc/fabric/impl/client/item/ClientItemEventHooks.class --class-name net/fabricmc/fabric/impl/item/DefaultItemComponentImpl.class --class-name net/fabricmc/fabric/mixin/item/AnvilScreenHandlerMixin.class --class-name net/fabricmc/fabric/mixin/item/ComponentMapBuilderMixin.class --class-name net/fabricmc/fabric/mixin/item/EnchantCommandMixin.class --class-name net/fabricmc/fabric/mixin/item/EnchantRandomlyLootFunctionMixin.class --class-name net/fabricmc/fabric/mixin/item/EnchantmentBuilderAccessor.class --class-name net/fabricmc/fabric/mixin/item/EnchantmentHelperMixin.class --class-name net/fabricmc/fabric/mixin/item/IItemExtensionMixin.class --class-name net/fabricmc/fabric/mixin/item/ItemAccessor.class --class-name net/fabricmc/fabric/mixin/item/ItemMixin.class --class-name net/fabricmc/fabric/mixin/item/ItemSettingsMixin.class --class-name net/fabricmc/fabric/mixin/item/ItemStackMixin.class --class-name net/fabricmc/fabric/mixin/item/LivingEntityMixin.class --class-name net/fabricmc/fabric/mixin/item/RegistryLoaderMixin.class --class-name org/sinytra/fabric/item_api/generated/GeneratedEntryPoint.class --output evidence/raw/item8/fabric-item-api-v1-entry-r1
```

The generated initializer is empty. Captured hooks adapt item components, equipment, durability, enchantment acceptance and tooltip callbacks. RegistryLoaderMixin delegates to EnchantmentUtil; that loading boundary remains open.

Source capture alone does not close whole-provider membership.
