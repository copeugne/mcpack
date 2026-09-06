# Supplementaries MixinSquared core entries

Extractor 27c648bf529b175d7c985a065e34df20db059c23. Manifest SHA-256:
a46ec939d8f5fba8cbb02ca91e76e87d25d830ebc7be3711056659e04a14d673.
Independent r1 matches every generated file.

Preserves bundled library entry mechanisms for provider contribution analysis.
This capture alone does not close the provider or prove runtime activation.

```sh
uv run -m tools.inspect_item8_pool_elements --archive supplementaries-neoforge-1.21.1-3.6.8.jar --nested-archive 'META-INF/jarjar/mixinsquared-forge-0.3.3.jar!/META-INF/jars/MixinSquared-0.3.3.jar' --class-name com/bawnorton/mixinsquared/MixinSquaredBootstrap.class --class-name com/bawnorton/mixinsquared/ext/ExtensionRegistrar.class --class-name com/bawnorton/mixinsquared/canceller/MixinCancellerRegistrar.class --class-name com/bawnorton/mixinsquared/adjuster/MixinAnnotationAdjusterRegistrar.class --output evidence/raw/item8/supplementaries-mixinsquared-core-r1
```
