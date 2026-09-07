# Fzzy Config registry and event boundaries

Extractor 01f80c0c971fdc3f95c96fddc53a6f644fd3662f. Independent r1 reproduction matches all
disassemblies and the identity manifest. Manifest SHA-256:
99281fc1128f2e399175b18e758391429143a955706256519cb1e79acaa595a8

```sh
uv run -m tools.inspect_item8_pool_elements --archive fzzy_config-0.7.6+1.21+neoforge.jar --class-name me/fzzyhmstrs/fzzy_config/networking/NetworkEvents.class --class-name me/fzzyhmstrs/fzzy_config/util/platform/impl/PlatformUtils.class --class-name 'me/fzzyhmstrs/fzzy_config/util/platform/impl/RegistryBuilderImpl$Companion.class' --output evidence/item-8/sources/fzzy-delegates
```

Source boundaries for provider membership, not general configuration or network testing.
