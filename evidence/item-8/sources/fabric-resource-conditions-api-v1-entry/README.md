# fabric-resource-conditions-api-v1-entry source checkpoint

Extractor 4cc1096. Independent r1 reproduction matches the manifest and every
disassembly byte. Manifest SHA-256: 1b89585428466581c618936da06eef4e7dc4684c64a150080ccf2ba02dda9c21.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-resource-conditions-api-v1-4.3.0+5bdd099819.jar --class-name net/fabricmc/fabric/mixin/resource/conditions/DataPackContentsMixin.class --class-name net/fabricmc/fabric/mixin/resource/conditions/DataProviderMixin.class --class-name net/fabricmc/fabric/mixin/resource/conditions/JsonDataLoaderMixin.class --class-name net/fabricmc/fabric/mixin/resource/conditions/RecipeManagerMixin.class --class-name net/fabricmc/fabric/mixin/resource/conditions/RegistryLoaderMixin.class --class-name net/fabricmc/fabric/mixin/resource/conditions/ReloadableRegistriesMixin.class --class-name net/fabricmc/fabric/mixin/resource/conditions/ResourcePackProfileMixin.class --class-name net/fabricmc/fabric/mixin/resource/conditions/ServerAdvancementLoaderMixin.class --class-name net/fabricmc/fabric/mixin/resource/conditions/SinglePreparationResourceReloaderMixin.class --class-name net/fabricmc/fabric/mixin/resource/conditions/TagManagerLoaderMixin.class --class-name org/sinytra/fabric/resource_conditions_api/generated/GeneratedEntryPoint.class --output evidence/raw/item8/fabric-resource-conditions-api-v1-entry-r1
```

The generated initializer and ten data-loading hooks are captured. Their condition evaluation and registration contribution roles remain open.

Source capture alone does not close whole-provider membership.
