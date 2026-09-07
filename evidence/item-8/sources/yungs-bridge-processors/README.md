# YUNG bridge processor sources

The captured BridgeFeature installs twelve processor entries after template
placement. Their implementations and registration bindings are required to
resolve effective bridge materials, support geometry and content. This uses
the existing extractor without a new runtime or measurement system.

Reproduce with frozen inputs into a fresh output directory:

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive YungsBridges-1.21.1-NeoForge-5.1.1.jar \
  --output evidence/raw/item8/yungs-bridge-processors-reproduction \
  --class-name com/yungnickyoung/minecraft/yungsbridges/module/FeatureProcessorModule.class \
  --class-name com/yungnickyoung/minecraft/yungsbridges/world/processor/ITemplateFeatureProcessor.class \
  --class-name com/yungnickyoung/minecraft/yungsbridges/world/processor/DynamicLegProcessor.class \
  --class-name com/yungnickyoung/minecraft/yungsbridges/world/processor/FenceBiomeProcessor.class \
  --class-name com/yungnickyoung/minecraft/yungsbridges/world/processor/LanternRotProcessor.class \
  --class-name com/yungnickyoung/minecraft/yungsbridges/world/processor/LogBiomeProcessor.class \
  --class-name com/yungnickyoung/minecraft/yungsbridges/world/processor/OptionalBlockProcessor.class \
  --class-name com/yungnickyoung/minecraft/yungsbridges/world/processor/OptionalSlabProcessor.class \
  --class-name com/yungnickyoung/minecraft/yungsbridges/world/processor/OptionalStairProcessor.class \
  --class-name com/yungnickyoung/minecraft/yungsbridges/world/processor/OptionalWallProcessor.class \
  --class-name com/yungnickyoung/minecraft/yungsbridges/world/processor/PlanksBiomeProcessor.class \
  --class-name com/yungnickyoung/minecraft/yungsbridges/world/processor/SlabBiomeProcessor.class \
  --class-name com/yungnickyoung/minecraft/yungsbridges/world/processor/StairBiomeProcessor.class \
  --class-name com/yungnickyoung/minecraft/yungsbridges/world/processor/StoneVariationProcessor.class
cmp evidence/item-8/sources/yungs-bridge-processors/identities.json evidence/raw/item8/yungs-bridge-processors-reproduction/identities.json
uv run ruff check tools/inspect_item8_pool_elements.py
uv run basedpyright tools/inspect_item8_pool_elements.py
```

Retained archive SHA-256:
`bf93a85422a6b457358c3b56352641a97ec09cc37dec18b2cedcac2bd1ff9bec`.
Fourteen-class identity manifest SHA-256:
`97da8471a115645afe18fee88f98407410097d244ed1d43d2a25ae4a6ad0bfaf`.
Initial extraction and fresh reproduction succeeded; manifests match
byte-for-byte, including all class/disassembly hashes. Scoped Ruff and
Basedpyright passed. Full generated classes are preserved together so registration,
default interface behavior and processor implementations remain reviewable.

The preceding generator capture shows template placement before custom processor
iteration. DynamicLegProcessor includes biome-dependent support materials and
randomized stone/cobblestone selectors; the remaining processing and interface
helper bodies require interpretation before final geometry/content attribution.
Do not infer final vertical size from the raw template envelope. No family
attribute or completion claim changes in this source increment.
