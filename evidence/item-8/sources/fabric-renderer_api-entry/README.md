# Fabric renderer_api entry

Captured with 6ff2013. An independent repeat reproduced the disassembly and
identity manifest exactly. Manifest SHA-256: cf785b7b3847dfffba0113e5805331b67d6d5ea866d2c9e20a30fa8e596a7f55.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-renderer-api-v1-3.4.1+9125b6dc19.jar --class-name org/sinytra/fabric/renderer_api/generated/GeneratedEntryPoint.class --output evidence/raw/item8/fabric-renderer_api-entry-r1
```

The loader constructor only calls Object and returns. Both packaged mixin configurations declare client hooks only.

The existing Fabric provider test binds the complete module payload and sole
annotated entry. This module contributes no independent server structure family.
Do not extend this membership check into client rendering implementation details.
