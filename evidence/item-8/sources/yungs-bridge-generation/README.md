# YUNG bridge generation sources

The feature-based bridge contribution uses custom generation and placement.
Packaged template envelopes and empty entity/block-entity lists do not expose
its processors or placement checks. This capture reuses the existing extractor
for eight exact classes: entry points, template/bridge generation, selector,
bridge feature configuration, bridge placement and RNG initialization. It is
needed for Item 8 effective contents and geometry, without a new runtime or
measurement system.

Archive: `YungsBridges-1.21.1-NeoForge-5.1.1.jar`, SHA-256
`bf93a85422a6b457358c3b56352641a97ec09cc37dec18b2cedcac2bd1ff9bec`.
Identity manifest SHA-256:
`2e6f68933e8b02e097901bb8db1afb3d277be7204e31574d44e66445696552da`.

Reproduce with frozen inputs and a fresh output directory:

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive YungsBridges-1.21.1-NeoForge-5.1.1.jar \
  --output evidence/raw/item8/yungs-bridge-generation-reproduction \
  --class-name com/yungnickyoung/minecraft/yungsbridges/world/feature/AbstractTemplateFeature.class \
  --class-name com/yungnickyoung/minecraft/yungsbridges/world/feature/BridgeFeature.class \
  --class-name com/yungnickyoung/minecraft/yungsbridges/world/feature/MultipleAttemptSingleRandomFeature.class \
  --class-name com/yungnickyoung/minecraft/yungsbridges/world/feature/config/BridgeFeatureConfig.class \
  --class-name com/yungnickyoung/minecraft/yungsbridges/world/placement/BridgePlacement.class \
  --class-name com/yungnickyoung/minecraft/yungsbridges/world/placement/RngInitializerPlacement.class \
  --class-name com/yungnickyoung/minecraft/yungsbridges/YungsBridgesCommon.class \
  --class-name com/yungnickyoung/minecraft/yungsbridges/YungsBridgesNeoForge.class
cmp evidence/item-8/sources/yungs-bridge-generation/identities.json evidence/raw/item8/yungs-bridge-generation-reproduction/identities.json
uv run ruff check tools/inspect_item8_pool_elements.py
uv run basedpyright tools/inspect_item8_pool_elements.py
```

Initial extraction used this source directory and the same selection. Fresh
reproduction succeeded; manifests match byte-for-byte, including the eight
class/disassembly identities. Scoped Ruff and Basedpyright passed.

Initial inspection: BridgeFeature builds a twelve-entry processor list covering
legs, log/stair/plank/slab/fence biome material, stone variation, lantern rot and
optional wall/block/slab/stair handling. Processor names are not proof of their
full behavior. Interpret the captured generator/placement and bind the processor
implementations before accepting effective contents or occupied dimensions.
The NeoForge entry point calls common initialization; configuration absence is
not established merely by no config-named class/file. Inventory is unchanged.
