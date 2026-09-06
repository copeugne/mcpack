# C2ME membership boundary: c2me-mixinsquared-bootstrap

Extractor 9c16bd6eee0944af76d0df4a8abd2b4d43a6d8d2. Independent r1 reproduction
matches every disassembly and identity manifest. Manifest SHA-256:
d514724250d1b03fd389728e358ebc9029c751688703bde50d0ccb3d22f74674

```sh
uv run -m tools.inspect_item8_pool_elements --archive c2me-neoforge-mc1.21.1-0.3.0+alpha.0.93.jar --nested-archive 'META-INF/jars/mixinsquared-neoforge-0.2.0-beta.6.jar!/META-INF/jars/MixinSquared-0.2.0-beta.6.jar' --class-name com/bawnorton/mixinsquared/MixinSquaredBootstrap.class --class-name com/bawnorton/mixinsquared/ext/ExtensionRegistrar.class --output evidence/raw/item8/c2me-mixinsquared-bootstrap-r1
```

Bootstrap registers the MixinSquared target selector and annotation-adjust/cancellation extensions in the existing mixin transformer. These are bytecode integration APIs, not authored world content. Do not audit generic annotation rewriting for Item 8 membership.
