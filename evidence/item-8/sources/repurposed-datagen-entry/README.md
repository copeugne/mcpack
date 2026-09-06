# Repurposed data-generation entry

Extractor b01b87f captures the remaining annotated entry. Independent r1
extraction matches every file. Manifest SHA-256: 0d2237b825ac55da59a8908beb120e562b67a58ccc3a5de1c151e1bbd980d9bf.

```sh
uv run -m tools.inspect_item8_pool_elements --archive repurposed_structures-7.5.21+1.21.1-neoforge.jar --class-name com/telepathicgrunt/repurposedstructures/datagen/StructureNbtUpdaterDatagen.class --output evidence/raw/item8/repurposed-datagen-entry-r1
```

The sole callback takes GatherDataEvent and adds a StructureNbtUpdater data
provider when includeServer is true. It is a data-generation tool entry,
not an additional runtime world-generation family.
