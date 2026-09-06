# C2ME membership boundary: c2me-mixinsquared-entry

Extractor 9c16bd6eee0944af76d0df4a8abd2b4d43a6d8d2. Independent r1 reproduction
matches every disassembly and identity manifest. Manifest SHA-256:
a707c9fdd9123e3aadf801707a8c2b326dc2b0955184a6d58f1c648f50064690

```sh
uv run -m tools.inspect_item8_pool_elements --archive c2me-neoforge-mc1.21.1-0.3.0+alpha.0.93.jar --nested-archive META-INF/jars/mixinsquared-neoforge-0.2.0-beta.6.jar --class-name com/bawnorton/mixinsquared/platform/neoforge/MixinSquaredMixinConfigPlugin.class --class-name com/bawnorton/mixinsquared/platform/neoforge/MixinCancellerLoader.class --class-name com/bawnorton/mixinsquared/platform/neoforge/MixinAnnotationAdjusterLoader.class --output evidence/raw/item8/c2me-mixinsquared-entry-r1
```

The plugin initializes MixinSquared and loads service-provided annotation adjusters and cancellers. It supplies no content definitions or authored generation. These services extend mixin processing, not world generation registration.
