# Direct configuration binding sources

Captured at `266b69f` using the existing extractor. Exact archive, class and
output identities are in `identities.json`. Reproduction matched byte for byte:

```sh
uv run -m tools.inspect_item8_pool_elements --archive Zeta-1.1-40.jar --class-name org/violetmoon/zeta/config/ConfigObjectMapper.class --class-name org/violetmoon/zeta/config/ConfigManager.class --class-name org/violetmoon/zetaimplforge/config/ForgeBackedConfig.class --output evidence/raw/item8/zeta-config-binding-266b69f
```

ConfigManager.onReload runs its data bindings with Zeta.configInternals, then
its reload listeners. ConfigObjectMapper's captured readInto binding lambda
reads the ValueDefinition through IZetaConfigInternals.get and calls setField.
The captured setField uses Java reflection and propagates reflection failure as
a RuntimeException. The mapper also has nested IConfigType processing and an
onReload callback. Verbose output retains bootstrap bindings for these lambdas.

ForgeBackedConfig recursively traverses section definitions and maps value
definitions to NeoForge configuration values. These are the direct sources for
the open Item 8 field-binding gap, not proof that a particular runtime reload
occurred. Finish annotation/name mapping and the configuration-event connection
before treating the frozen values as effective. Unrelated configuration UI,
network synchronization and flag consumers are outside this inspection.
