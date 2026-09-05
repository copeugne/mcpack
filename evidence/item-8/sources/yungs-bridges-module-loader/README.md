# YUNG initialization source evidence

Captured with extractor revision `691d62a`. Manifest SHA-256:
`9bed9e79b9acc13472a27c341058a7f38d23fd072c0433847e2f7b4b8c600595`.

The NeoForge module loader delegates to IModulesLoader.loadModules. Its default
implementation still needs inspection before concluding which configuration
controls apply. Extras entrypoints scan the module package and call the loader;
Bridges entrypoints are preserved in yungs-bridge-generation.

Reproduce with frozen hash-verified inputs and a fresh output directory:

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive YungsBridges-1.21.1-NeoForge-5.1.1.jar \
  --class-name com/yungnickyoung/minecraft/yungsbridges/services/NeoForgeModulesLoader.class \
  --output evidence/raw/item8/yungs-bridges-module-loader-reproduction
```

Before adding this README, recursive comparison against the fresh reproduction
directory matched all files byte-for-byte. Scoped extractor Ruff/Basedpyright
passed. No new runtime or measurement system was added.
