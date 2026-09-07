# Create dynamic recipe serialization

Extractor: 346e42e106e564ebf503f37fdcf12d5cf77648e0.
The complete StandardBuilder disassembly independently reproduces byte-for-byte.
It resolves the exact output boundary delegated by RuntimeDataGenerator:
Recipe.CONDITIONAL_CODEC encoding and insertion under the recipe/ prefix.

```sh
uv run -m tools.inspect_item8_pool_elements --archive create-1.21.1-6.0.10.jar \
  --class-name 'com/simibubi/create/foundation/data/RuntimeDataGenerator$StandardBuilder.class' \
  --output evidence/raw/item8/create-dynamic-recipe-serializer-r1
```
