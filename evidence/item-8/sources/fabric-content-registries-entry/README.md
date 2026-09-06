# fabric-content-registries-entry source checkpoint

Extractor b4c5d26. Independent r1 reproduction matches the manifest and all
disassembly bytes. Manifest SHA-256: 9f1c23a98141bc5449ee93e4f103ba67a7d15f5e333ab85a56712e27661d20d0.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-content-registries-v0-8.0.19+5e0d320019.jar --class-name net/fabricmc/fabric/api/registry/TillableBlockRegistry.class --class-name net/fabricmc/fabric/impl/content/registry/FuelRegistryImpl.class --class-name net/fabricmc/fabric/mixin/content/registry/AxeItemAccessor.class --class-name net/fabricmc/fabric/mixin/content/registry/BaseRegistryMixin.class --class-name net/fabricmc/fabric/mixin/content/registry/BrewingRecipeRegistryBuilderMixin.class --class-name net/fabricmc/fabric/mixin/content/registry/FarmerWorkTaskAccessor.class --class-name net/fabricmc/fabric/mixin/content/registry/FireBlockMixin.class --class-name net/fabricmc/fabric/mixin/content/registry/GiveGiftsToHeroTaskAccessor.class --class-name net/fabricmc/fabric/mixin/content/registry/HoeItemAccessor.class --class-name net/fabricmc/fabric/mixin/content/registry/HoneycombItemMixin.class --class-name net/fabricmc/fabric/mixin/content/registry/LandPathNodeMakerMixin.class --class-name net/fabricmc/fabric/mixin/content/registry/OxidizableMixin.class --class-name net/fabricmc/fabric/mixin/content/registry/PathContextMixin.class --class-name net/fabricmc/fabric/mixin/content/registry/ShovelItemAccessor.class --class-name net/fabricmc/fabric/mixin/content/registry/VillagerEntityAccessor.class --class-name org/sinytra/fabric/content_registries/generated/GeneratedEntryPoint.class --output evidence/raw/item8/fabric-content-registries-entry-r1
```

The generated initializer is empty. Two automatic subscriber entries and thirteen common hooks are preserved for contribution-role reconciliation.

Source capture is not whole-provider closure or effective-consumer evidence.
