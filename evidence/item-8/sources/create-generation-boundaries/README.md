# Create ore and test registration boundaries

Extractor: cb34d9e6f3928284d1b2a028b99cb98ddc0c164a.
Four complete class disassemblies reproduce byte-for-byte in an independent
capture. This isolated generated increment preserves the custom ore writer,
feature registration, configuration filter and GameTest registration boundary.
It does not close Create's full provider membership check.

```sh
uv run -m tools.inspect_item8_pool_elements --archive create-1.21.1-6.0.10.jar \
  --class-name com/simibubi/create/infrastructure/worldgen/AllFeatures.class \
  --class-name com/simibubi/create/infrastructure/worldgen/LayeredOreFeature.class \
  --class-name com/simibubi/create/infrastructure/worldgen/ConfigPlacementFilter.class \
  --class-name com/simibubi/create/infrastructure/gametest/CreateGameTests.class \
  --output evidence/raw/item8/create-generation-boundaries-r1
```
