# Create entry and template consumers

Extractor: cd1fefbab675bbbfd868bfd9d545edab2b2c6d73.
Four full disassemblies reproduce byte-for-byte in an independent capture.
This isolated generated increment preserves the main registration entry,
GameTest template-ID construction, schematic processor registration and declared
mixin plugin. It does not assert closure of every Create event or nested library.

```sh
uv run -m tools.inspect_item8_pool_elements --archive create-1.21.1-6.0.10.jar \
  --class-name com/simibubi/create/infrastructure/gametest/CreateTestFunction.class \
  --class-name com/simibubi/create/Create.class \
  --class-name com/simibubi/create/AllStructureProcessorTypes.class \
  --class-name com/simibubi/create/foundation/mixin/CreateMixinPlugin.class \
  --output evidence/raw/item8/create-entry-template-consumers-r1
```
