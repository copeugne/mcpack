# YUNG initialization source evidence

Captured with extractor revision `691d62a`. Manifest SHA-256:
`9a3c1a412e4ddc0e2ac21911776e5fc251fd36a51deb441f50e8df56c9e83675`.

The NeoForge module loader delegates to IModulesLoader.loadModules. Its default
implementation still needs inspection before concluding which configuration
controls apply. Extras entrypoints scan the module package and call the loader;
Bridges entrypoints are preserved in yungs-bridge-generation.

Reproduce with frozen hash-verified inputs and a fresh output directory:

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive YungsExtras-1.21.1-NeoForge-5.1.1.jar \
  --class-name com/yungnickyoung/minecraft/yungsextras/YungsExtrasCommon.class \
  --class-name com/yungnickyoung/minecraft/yungsextras/YungsExtrasNeoForge.class \
  --class-name com/yungnickyoung/minecraft/yungsextras/services/NeoForgeModulesLoader.class \
  --output evidence/raw/item8/yungs-extras-initialization-reproduction
```

Before adding this README, recursive comparison against the fresh reproduction
directory matched all files byte-for-byte. Scoped extractor Ruff/Basedpyright
passed. No new runtime or measurement system was added.
