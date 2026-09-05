# Extras processor constructor bindings

DesertWellFeature and AbstractSwampFeature reference processor module fields.
This exact module capture binds those fields to DesertWellProcessor and
SwampFeatureProcessor, respectively. The register helper appends the supplied
instance to PROCESSORS and returns that same instance.

Manifest SHA-256:
`1b79d6b5d0afdc5a965dd1fa0f9ed732d77fe3dcaa9378e4115fa942efb1e0d6`.
Archive SHA-256:
`0cd26474e514f5dc3114aaf5ec7e049bcd285f0c5db191bb45223193f35df70d`.

Reproduce using extractor revision `1164c98` and a fresh output directory:

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive YungsExtras-1.21.1-NeoForge-5.1.1.jar \
  --class-name com/yungnickyoung/minecraft/yungsextras/module/FeatureProcessorModule.class \
  --output evidence/raw/item8/yungs-extras-processor-bindings-reproduction
cmp evidence/item-8/sources/yungs-extras-processor-bindings/identities.json evidence/raw/item8/yungs-extras-processor-bindings-reproduction/identities.json
```

Before adding this README, recursive comparison of the captured and fresh
reproduction directories matched every file byte-for-byte. The existing
extractor passed scoped Ruff and Basedpyright checks. No new runtime or
measurement system was added.
