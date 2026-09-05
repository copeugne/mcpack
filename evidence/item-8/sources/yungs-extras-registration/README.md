# Extras feature registration annotations

The initial non-verbose FeatureModule capture omitted field annotations needed
to bind configured feature IDs to generator classes. This one-class verbose
capture fixes that concrete omission within the existing extractor. The previous
raw evidence is retained unchanged.

Archive SHA-256:
`0cd26474e514f5dc3114aaf5ec7e049bcd285f0c5db191bb45223193f35df70d`.
Manifest SHA-256:
`07300368df9a9fe1fe8f7e6efad0bc12505ebeb2e4db2a00389150a39b9e417e`.

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive YungsExtras-1.21.1-NeoForge-5.1.1.jar \
  --class-name com/yungnickyoung/minecraft/yungsextras/module/FeatureModule.class \
  --output evidence/raw/item8/yungs-extras-registration-reproduction
cmp evidence/item-8/sources/yungs-extras-registration/identities.json evidence/raw/item8/yungs-extras-registration-reproduction/identities.json
uv run ruff check tools/inspect_item8_pool_elements.py
uv run basedpyright tools/inspect_item8_pool_elements.py
```

Use a fresh output directory and the frozen retained inputs. Initial extraction
used this source directory. Fresh reproduction matched the manifest byte-for-byte
and both disassembly hashes. Scoped quality checks passed. The class-level
AutoRegister annotation supplies yungsextras; the three desert fields declare
desert_chillzone, desert_giant_torch and desert_ruins_0 and instantiate the
previously captured corresponding classes. Inventory integration follows this
source delivery. No new runtime or measurement system is introduced.
