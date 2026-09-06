# fabric-command-entry source roles

Extractor a2c1e65. Independent r1 reproduction matches the manifest and every
disassembly byte for byte. Manifest SHA-256:
2905c60a6b616efc27154aa9fb5cf2768184f535238df1cbaf8d406d1a72a3f5.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-command-api-v2-2.2.28+36d727be19.jar --class-name net/fabricmc/fabric/mixin/command/EntitySelectorReaderMixin.class --class-name org/sinytra/fabric/command_api/generated/GeneratedEntryPoint.class --output evidence/raw/item8/fabric-command-entry-r1
```

EntitySelectorReaderMixin stores and queries caller-defined selector flags. The loader calls org/sinytra/fabric/command_api/FabricCommandApiV2.onInitialize; that server initializer remains open. Its client initializer is guarded by Dist.isClient.

The initial extraction attempt was rejected by argument parsing because the
new nested archives were absent from the allowlist. No output was produced;
a2c1e65 adds the exact nested identities before this successful capture.
These are source roles, not whole-provider closure or effective-consumer proof.
