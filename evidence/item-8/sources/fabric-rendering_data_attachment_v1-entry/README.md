# Fabric rendering_data_attachment_v1 contribution paths

Captured with 231284d; independent repeat matched all source files exactly.
Manifest SHA-256: 1563f045f7690ab90e53d9e9ae5e126d657b09fece385ba2414a03f08c6eadd4.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-rendering-data-attachment-v1-0.3.49+73761d2e19.jar --class-name net/fabricmc/fabric/mixin/rendering/data/BlockEntityMixin.class --class-name net/fabricmc/fabric/mixin/rendering/data/WorldViewMixin.class --class-name org/sinytra/fabric/rendering_data_attachment_v1/generated/GeneratedEntryPoint.class --output evidence/raw/item8/fabric-rendering_data_attachment_v1-entry-r1
```

The loader is empty. BlockEntity defaults render attachment data to null and forwards getRenderData to that accessor. WorldView adds the render attachment interface. These roles add no generation path.

Complete module payload and mixin membership are checked separately. This
capture is not whole Fabric provider closure. Do not follow generic interface
helpers beyond a demonstrated content-contribution question.
