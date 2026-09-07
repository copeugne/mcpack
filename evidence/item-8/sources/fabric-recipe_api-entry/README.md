# Fabric recipe_api entry roles

Captured with 5049826 and independently reproduced exactly. Manifest SHA-256:
1778fbf2dcb132483978c5333401a7b5dcd77cc4bc6879ce057d1a05a0c96ab5.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-recipe-api-v1-5.0.15+59440bcc19.jar --class-name net/fabricmc/fabric/mixin/recipe/ingredient/CraftingHelperMixin.class --class-name net/fabricmc/fabric/mixin/recipe/ingredient/IngredientMixin.class --class-name org/sinytra/fabric/recipe_api/generated/GeneratedEntryPoint.class --output evidence/raw/item8/fabric-recipe_api-entry-r1
```

Ingredient mixins wrap custom ingredients and delegate codec construction. The loader calls CustomIngredientInit and FabricRecipeApiV1 initializers; their registration roles remain to be inspected before closure.

Complete payload and declared-hook coverage are verified by the existing Fabric
provider check. This capture is not whole-provider or effective-loot acceptance.
