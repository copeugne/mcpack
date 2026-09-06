# Supplementaries MixinSquared wrapper entries

Extractor 27c648bf529b175d7c985a065e34df20db059c23. Manifest SHA-256:
6a7cbdcfb28d23625a5a4468a982f9d5011767bc226793639d02532001fc47c2.
Independent r1 matches every generated file.

Preserves bundled library entry mechanisms for provider contribution analysis.
This capture alone does not close the provider or prove runtime activation.

```sh
uv run -m tools.inspect_item8_pool_elements --archive supplementaries-neoforge-1.21.1-3.6.8.jar --nested-archive META-INF/jarjar/mixinsquared-forge-0.3.3.jar --class-name com/bawnorton/mixinsquared/platform/forge/MixinCancellerLoader.class --class-name com/bawnorton/mixinsquared/platform/forge/MixinSquaredMixinConfigPlugin.class --class-name com/bawnorton/mixinsquared/platform/forge/MixinAnnotationAdjusterLoader.class --class-name com/bawnorton/mixinsquared/platform/forge/MixinSquaredMod.class --output evidence/raw/item8/supplementaries-mixinsquared-wrapper-r1
```
