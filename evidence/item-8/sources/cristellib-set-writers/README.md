# CristelLib concrete structure-set writers

Extractor cb9503c9. Independent r1 reproduction matches source and manifest
bytes. Manifest SHA-256:
710a8a7a2c265c7e41b10177367ce927644e5b9d7f3cfe9bffcabeb56191ff01

```sh
uv run -m tools.inspect_item8_pool_elements --archive cristellib-neoforge-1.21.1-3.1.7.jar --class-name de/cristelknight/cristellib/StructureConfigPlacement.class --class-name de/cristelknight/cristellib/StructureConfigToggle.class --output evidence/raw/item8/cristellib-set-writers-r1
```

Toggle removes disabled structure members from an existing set. Placement
changes salt, spacing, separation and frequency on an existing set. Both
write the result under that set ID in CONFIG_PACK; neither supplies a new
structure design. Unchanged configurations return without an override.
