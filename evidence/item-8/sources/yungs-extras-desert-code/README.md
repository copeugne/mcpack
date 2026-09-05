# Extras empty-config desert generator sources

Three configured features omit location fields, so packaged JSON cannot bind
their templates or expose custom content/placement effects. This capture uses
the existing extractor for five exact classes: FeatureModule, AbstractNbtFeature
and the three desert generators. No new runtime or measurement system is added.

Archive: `YungsExtras-1.21.1-NeoForge-5.1.1.jar`, SHA-256
`0cd26474e514f5dc3114aaf5ec7e049bcd285f0c5db191bb45223193f35df70d`.
Manifest SHA-256:
`c595f5123a71105b276884d33229e4b7da2bf9b91b70ec8e5cbf1cba069d465b`.

Reproduce with verified frozen inputs and a fresh destination:

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive YungsExtras-1.21.1-NeoForge-5.1.1.jar \
  --output evidence/raw/item8/yungs-extras-desert-code-reproduction \
  --class-name com/yungnickyoung/minecraft/yungsextras/module/FeatureModule.class \
  --class-name com/yungnickyoung/minecraft/yungsextras/world/feature/AbstractNbtFeature.class \
  --class-name com/yungnickyoung/minecraft/yungsextras/world/feature/desert/ChillzoneDesertFeature.class \
  --class-name com/yungnickyoung/minecraft/yungsextras/world/feature/desert/DesertGiantTorchFeature.class \
  --class-name com/yungnickyoung/minecraft/yungsextras/world/feature/desert/DesertSmallRuinsFeature.class
cmp evidence/item-8/sources/yungs-extras-desert-code/identities.json evidence/raw/item8/yungs-extras-desert-code-reproduction/identities.json
uv run ruff check tools/inspect_item8_pool_elements.py
uv run basedpyright tools/inspect_item8_pool_elements.py
```

The initial extraction used this source directory and the same class selection.
A fresh reproduction matched the manifest byte-for-byte; all five captured and
reproduced disassembly hashes matched their manifest. Scoped quality checks
passed. Complete class outputs are retained as one source-evidence increment.

Initial inspection finds desert/misc/chillzone, giant_torch and ruins_0 constants
in their corresponding generators. Full registration-to-placement interpretation
remains required before accepting the mappings or effective contents. The working
inventory is unchanged by this capture.
