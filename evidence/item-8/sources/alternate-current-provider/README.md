# Alternate Current provider contribution

Selector ec856af captures all 30 packaged classes. The 31 generated files
reproduce exactly against independent r1 output. Manifest SHA-256:
8838261bd796edf444cfbf312d9f6bd8f779d09deae3472b68ed510a4c78ec7f.

```sh
uv run -m tools.inspect_item8_pool_elements --archive alternate_current-mc1.21-1.9.0.jar --output evidence/raw/item8/alternate-current-provider-r1
```

The mod subscriber registers redstone configuration/profiler commands.
ServerLevelMixin creates a WireHandler, MinecraftServerMixin saves its
configuration, and RedStoneWireBlockMixin directs existing wire placement,
removal and neighbor changes into that handler. Nodes, connections, queues and
update-order classes calculate and propagate existing wire signals. LevelHelper
writes the supplied wire block state and updates neighbors; it does not register
or lay out authored world content. Profiler classes report this processing.

The only non-class files are loader metadata, the mixin declaration and an icon.
No independent structure family or packaged generation contribution. Redstone
behavior may affect an existing mechanism, but this provider census makes no
claim of measured redstone equivalence, performance or trap behavior.
