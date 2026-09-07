# Fabric rendering_fluids entry

Captured with 6ff2013. An independent repeat reproduced the disassembly and
identity manifest exactly. Manifest SHA-256: fced898b4d81ad78a18d99dc2e36d482b63dd3105d049363b8abb9bb59e14908.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-rendering-fluids-v1-3.1.6+a51883b219.jar --class-name org/sinytra/fabric/rendering_fluids/generated/GeneratedEntryPoint.class --output evidence/raw/item8/fabric-rendering_fluids-entry-r1
```

The constructor invokes FabricRenderingFabricV1.onInitializeClient only when FMLEnvironment.dist.isClient is true. The packaged mixin configuration declares client hooks only.

The existing Fabric provider test binds the complete module payload and sole
annotated entry. This module contributes no independent server structure family.
Do not extend this membership check into client rendering implementation details.
