# CristelLib resource writer dispatch

Extractor 83269a6c. Three classes. Independent r1 reproduction matches all
source and manifest bytes. Manifest SHA-256:
cf2b2a4ef6e3965343d69b694eac128f554668ec354491fb0280aa394845bd2d

```sh
uv run -m tools.inspect_item8_pool_elements --archive cristellib-neoforge-1.21.1-3.1.7.jar --class-name de/cristelknight/cristellib/StructureConfig.class --class-name de/cristelknight/cristellib/data/ReadData.class --class-name de/cristelknight/cristellib/util/Util.class --output evidence/raw/item8/cristellib-writers-r1
```

Util iterates consumer mods and excludes CristelLib itself from automatic
configuration. ReadData reads consumer declarations and configuration overrides,
and registers their conditional packs. StructureConfig dispatches changes to
existing structure-set IDs. Its addChanges method is abstract: the concrete
StructureConfigToggle and StructureConfigPlacement writers still require binding
before membership closure. Do not treat this dispatch capture as their result.
