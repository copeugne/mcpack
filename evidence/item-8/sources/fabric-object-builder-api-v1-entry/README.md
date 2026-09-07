# fabric-object-builder-api-v1-entry source checkpoint

Extractor f633bf8. Independent r1 reproduction matches the manifest and all
disassembly bytes. Manifest SHA-256: d7a0bf493eb787b68c5ec8df4170657dbd74f1686d1a6b4fa58b22059570e393.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-object-builder-api-v1-15.2.1+cc242efd19.jar --class-name net/fabricmc/fabric/mixin/object/builder/AbstractBlockAccessor.class --class-name net/fabricmc/fabric/mixin/object/builder/AbstractBlockSettingsAccessor.class --class-name net/fabricmc/fabric/mixin/object/builder/BlockEntityTypeBuilderMixin.class --class-name net/fabricmc/fabric/mixin/object/builder/BlockEntityTypeMixin.class --class-name net/fabricmc/fabric/mixin/object/builder/DefaultAttributeRegistryAccessor.class --class-name net/fabricmc/fabric/mixin/object/builder/DefaultAttributeRegistryMixin.class --class-name net/fabricmc/fabric/mixin/object/builder/DetectorRailBlockMixin.class --class-name net/fabricmc/fabric/mixin/object/builder/EntityTypeBuilderMixin.class --class-name net/fabricmc/fabric/mixin/object/builder/EntityTypeMixin.class --class-name net/fabricmc/fabric/mixin/object/builder/PersistentStateManagerMixin.class --class-name net/fabricmc/fabric/mixin/object/builder/TradeOffersTypeAwareBuyForOneEmeraldFactoryMixin.class --class-name org/sinytra/fabric/object_builder_api/generated/GeneratedEntryPoint.class --output evidence/raw/item8/fabric-object-builder-api-v1-entry-r1
```

The generated initializer is empty. Hooks expose supplied block/entity builders, mutable type/property collections, existing-minecart comparator callbacks, saved-data compatibility and empty-trade handling. No independent generated site is introduced by these entries.

Source capture alone does not close whole-provider membership.
