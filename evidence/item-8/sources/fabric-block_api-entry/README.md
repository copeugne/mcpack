# Fabric block_api contribution paths

Captured with 231284d; independent repeat matched all source files exactly.
Manifest SHA-256: 3378c30e4764b45310fd52494bfb1d88ad4f8e7ff250e7a58232388d4c7f705d.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-block-api-v1-1.1.0+b0c22bb819.jar --class-name net/fabricmc/fabric/mixin/block/IBlockExtensionMixin.class --class-name net/fabricmc/fabric/mixin/block/IBlockStateExtensionMixin.class --class-name net/fabricmc/fabric/mixin/block/LivingEntityMixin.class --class-name org/sinytra/fabric/block_api/generated/GeneratedEntryPoint.class --output evidence/raw/item8/fabric-block_api-entry-r1
```

The loader is empty. Two interface mixins add block API interfaces. LivingEntityMixin lets tagged blocks support trapdoor climbing, retaining ladder-facing checks. These roles do not place structure content.

Complete module payload and mixin membership are checked separately. This
capture is not whole Fabric provider closure. Do not follow generic interface
helpers beyond a demonstrated content-contribution question.
