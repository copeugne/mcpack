# Fzzy Config consumer registration boundary

Extractor f20a008ef5e1e746a6eb6beecef9a46eeab52c96. Independent r1 reproduction matches all
disassemblies and the identity manifest. Manifest SHA-256:
9ba43a7c31efdd79947956bc6c9ff1ed7e3f249b4a5a98f94728d8ed4cd691eb

```sh
uv run -m tools.inspect_item8_pool_elements --archive fzzy_config-0.7.6+1.21+neoforge.jar --class-name me/fzzyhmstrs/fzzy_config/util/platform/impl/RegistryBuilderImpl.class --class-name me/fzzyhmstrs/fzzy_config/util/platform/impl/RegistrarImpl.class --class-name 'me/fzzyhmstrs/fzzy_config/util/platform/impl/RegistrarImpl$Companion.class' --output evidence/item-8/sources/fzzy-registrations
```

Provider membership boundary for registry builders and consumer registration.
