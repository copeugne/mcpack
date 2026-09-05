# YUNG default module initialization

The preserved IModulesLoader.loadModules default method contains only return.
The captured NeoForgeModulesLoader invokes that default method, so this branch
of initialization adds no configuration registration. This is a direct-method
conclusion, not proof that no external or data-driven controls exist.

Manifest SHA-256: `a88c07b516b2ee1692c6629ab8db0a4f4a63c8455265ce3aa7c061679e67a581`.
Extractor revision: `da44ce2`. Reproduce in a fresh directory:

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive YungsBridges-1.21.1-NeoForge-5.1.1.jar \
  --class-name com/yungnickyoung/minecraft/yungsbridges/services/IModulesLoader.class \
  --output evidence/raw/item8/yungs-bridges-module-default-reproduction
```

Before adding this README, recursive comparison against fresh reproduction
matched every file byte-for-byte. Scoped extractor Ruff/Basedpyright passed.
