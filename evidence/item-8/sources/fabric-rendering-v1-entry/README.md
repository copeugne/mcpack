# fabric-rendering-v1-entry source checkpoint

Extractor 4cc1096. Independent r1 reproduction matches the manifest and every
disassembly byte. Manifest SHA-256: adb9d93ad3ff1cf27a2299424fe89e188fd41e24d8bede1957c9bb4db9b5f4e7.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-rendering-v1-5.1.0+1a09bd5a19.jar --class-name org/sinytra/fabric/rendering/generated/GeneratedEntryPoint.class --output evidence/raw/item8/fabric-rendering-v1-entry-r1
```

Initialization calls FabricRenderingV1.onInitializeClient only when Dist.isClient. All fifteen declared mixins are client-only. No server generation entry.

Source capture alone does not close whole-provider membership.
