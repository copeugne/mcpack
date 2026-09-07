# fabric-data-generation-entry source checkpoint

Extractor b4c5d26. Independent r1 reproduction matches the manifest and all
disassembly bytes. Manifest SHA-256: 005d5198b431bd5f83257d280cead53e562acb126ce11f94285bc0dcf397022d.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-data-generation-api-v1-20.2.34+a4c3605619.jar --class-name net/fabricmc/fabric/mixin/datagen/DataGeneratorMixin.class --class-name net/fabricmc/fabric/mixin/datagen/DataProviderMixin.class --class-name net/fabricmc/fabric/mixin/datagen/ModelProviderMixin.class --class-name net/fabricmc/fabric/mixin/datagen/loot/BlockLootTableGeneratorAccessor.class --class-name net/fabricmc/fabric/mixin/datagen/loot/BlockLootTableGeneratorMixin.class --class-name net/fabricmc/fabric/mixin/datagen/recipe/AllCraftingRecipeJsonBuildersMixin.class --class-name net/fabricmc/fabric/mixin/datagen/recipe/ComplexRecipeJsonBuilderMixin.class --class-name net/fabricmc/fabric/mixin/datagen/recipe/RecipeOutputMixin.class --class-name net/fabricmc/fabric/mixin/datagen/recipe/SmithingTransformRecipeJsonBuilderMixin.class --class-name net/fabricmc/fabric/mixin/datagen/recipe/SmithingTrimRecipeJsonBuilderMixin.class --class-name org/sinytra/fabric/data_generation_api/generated/GeneratedEntryPoint.class --output evidence/raw/item8/fabric-data-generation-entry-r1
```

The generated initializer is empty. Ten common data-generator, model, loot and recipe hooks are preserved for contribution-role reconciliation.

Source capture is not whole-provider closure or effective-consumer evidence.
