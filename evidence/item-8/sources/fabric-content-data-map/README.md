# fabric-content-data-map source roles

Extractor d3be53f. Independent r1 reproduction matches the manifest and every
disassembly byte. Manifest SHA-256: ba7fcec72be79425015cea676ff60b645990ed84d277c9b237358cd1fa8fa9df.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-content-registries-v0-8.0.19+5e0d320019.jar --class-name net/fabricmc/fabric/impl/content/registry/DataMapModifications.class --output evidence/raw/item8/fabric-content-data-map-r1
```

The generic registry hook only handles COMPOSTABLES and RAID_HERO_GIFTS. It reads custom maps and returns composting values or a gift loot-table key; it has no site-generation branch.
