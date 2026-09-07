# Fabric client_tags_api entry

Captured with 6ff2013. An independent repeat reproduced the disassembly and
identity manifest exactly. Manifest SHA-256: c21d8171de5516eadbedab75ab654617416551609d47d38c667bccc6d483bbd2.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-client-tags-api-v1-1.1.15+e053909619.jar --class-name org/sinytra/fabric/client_tags_api/generated/GeneratedEntryPoint.class --output evidence/raw/item8/fabric-client_tags_api-entry-r1
```

The loader constructor only calls Object and returns. No module mixin configuration is packaged.

The existing Fabric provider test binds the complete module payload and sole
annotated entry. This module contributes no independent server structure family.
Do not extend this membership check into client rendering implementation details.
