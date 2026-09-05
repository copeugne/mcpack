# Remaining Extras generator and processor sources

The eight remaining configured feature types use custom desert/swamp generators
and processors. Packaged template contents and dimensions cannot establish their
placement transformations or runtime-added contents. This capture reuses the
existing extractor for twelve exact classes: eight concrete generators, one
swamp base and three processor/interface classes. Earlier desert source and
registration captures remain separate and unchanged.

Archive SHA-256:
`0cd26474e514f5dc3114aaf5ec7e049bcd285f0c5db191bb45223193f35df70d`.
Manifest SHA-256:
`6295b0a24fca944020cd1f489beae29c75deef061d93c411504e7aaadfe23210`.

Use verified frozen inputs and a fresh output directory:

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive YungsExtras-1.21.1-NeoForge-5.1.1.jar \
  --output evidence/raw/item8/yungs-extras-generators-reproduction \
  --class-name com/yungnickyoung/minecraft/yungsextras/world/feature/desert/DesertObeliskFeature.class \
  --class-name com/yungnickyoung/minecraft/yungsextras/world/feature/desert/DesertWellFeature.class \
  --class-name com/yungnickyoung/minecraft/yungsextras/world/feature/swamp/AbstractSwampFeature.class \
  --class-name com/yungnickyoung/minecraft/yungsextras/world/feature/swamp/SwampArchFeature.class \
  --class-name com/yungnickyoung/minecraft/yungsextras/world/feature/swamp/SwampChurchFeature.class \
  --class-name com/yungnickyoung/minecraft/yungsextras/world/feature/swamp/SwampCubbyFeature.class \
  --class-name com/yungnickyoung/minecraft/yungsextras/world/feature/swamp/SwampDoubleArchFeature.class \
  --class-name com/yungnickyoung/minecraft/yungsextras/world/feature/swamp/SwampOgreFeature.class \
  --class-name com/yungnickyoung/minecraft/yungsextras/world/feature/swamp/SwampPillarFeature.class \
  --class-name com/yungnickyoung/minecraft/yungsextras/world/processor/DesertWellProcessor.class \
  --class-name com/yungnickyoung/minecraft/yungsextras/world/processor/INbtFeatureProcessor.class \
  --class-name com/yungnickyoung/minecraft/yungsextras/world/processor/SwampFeatureProcessor.class
cmp evidence/item-8/sources/yungs-extras-generators/identities.json evidence/raw/item8/yungs-extras-generators-reproduction/identities.json
uv run ruff check tools/inspect_item8_pool_elements.py
uv run basedpyright tools/inspect_item8_pool_elements.py
```

The initial extraction used this source directory and the same selection.
Fresh reproduction matched the manifest byte-for-byte and all twelve captured
and reproduced disassembly hashes. Scoped quality checks passed. Full class
outputs are retained as one generated source-evidence increment with no unrelated
changes. Interpretation and inventory integration remain open. No new runtime,
measurement system or generalized extraction mechanism was added.
