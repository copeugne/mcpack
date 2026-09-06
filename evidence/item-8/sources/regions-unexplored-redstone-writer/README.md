# Regions Unexplored pointed-redstone writer

Extractor 346014444bdb11a0e9026a62437684d281afae95. Manifest SHA-256: 31143f1076e6d08d7280dd918331ce67087d07626cfe25778608398c26827bdd. Independent r1 matches all generated files.

This shared writer is called by both captured pointed-redstone features. It closes their direct block-generation source boundary using the existing extractor.

```sh
uv run -m tools.inspect_item8_pool_elements --archive regions-unexplored-0.6.1-neoforge-21.1.jar --class-name net/regions_unexplored/world/level/feature/configuration/PointedRedstoneUtils.class --output evidence/raw/item8/regions-unexplored-redstone-writer-r1
```
