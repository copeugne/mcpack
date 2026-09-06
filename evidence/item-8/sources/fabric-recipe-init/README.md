# fabric-recipe-init source roles

Captured with extractor fa3226d. Existing independent r1 reproduction matches
the identity manifest and every disassembly byte for byte. Manifest SHA-256:
284be5d480faf7950a489a9134fa4db894a3ed59174e3e3c28b07dcb4c2c98ae.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-recipe-api-v1-5.0.15+59440bcc19.jar --class-name net/fabricmc/fabric/impl/recipe/ingredient/CustomIngredientInit.class --class-name org/sinytra/fabric/recipe_api/FabricRecipeApiV1.class --output evidence/raw/item8/fabric-recipe-init-r1
```

CustomIngredientInit registers All, Any, Difference, Components and CustomData ingredient serializers. FabricRecipeApiV1 registers the NeoForge fabric ingredient-wrapper type and supplies ingredient codecs. These paths register recipe support, not generation content.

This is source evidence for the existing Fabric provider check, not whole-provider
closure or proof of effective consumer behavior.
