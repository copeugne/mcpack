# Coffee Delight provider entries

Extractor 79387e3e4c04df1254cd78a86d1e8cba2d4012a5. Manifest SHA-256:
4c0bf1002f4b2838cb7e2b4938aa5a9b964266defbb604acb874d47927ef84ee.
Independent r1 matches every generated file.

The main constructor registers blocks, items, an item tab and block entities.
The sole automatic event subscriber handles development data generation.
The three generation bootstraps define a vanilla random patch of coffee bushes
and its placement/biome modifier. There is no custom site generator in these
entries. Full archive accounting and packaged-data checks accompany acceptance.

```sh
uv run -m tools.inspect_item8_pool_elements --archive coffee_delight-1.4.1.jar --class-name lcyzsdh/coffee_delight/CoffeeDelight.class --class-name lcyzsdh/coffee_delight/data/ModDataGenerator.class --class-name lcyzsdh/coffee_delight/worldgen/ModBiomeModifier.class --class-name lcyzsdh/coffee_delight/worldgen/ModFeatures.class --class-name lcyzsdh/coffee_delight/worldgen/ModPlacement.class --output evidence/raw/item8/coffee-delight-provider-r1
```
