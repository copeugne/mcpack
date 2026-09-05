# Module section identity

Captured at `30458dc` through the existing extractor, with exact archive, class
and disassembly identities in `identities.json`. Reproduction matched exactly:

```sh
uv run -m tools.inspect_item8_pool_elements --archive Zeta-1.1-40.jar --class-name org/violetmoon/zeta/module/ZetaModule.class --output evidence/raw/item8/zeta-module-section-30458dc
```

ZetaModule.lowerCaseName returns its stored lowercaseName. The constructor
initializes this to an empty string; this class does not establish how the
module loader assigns the final section name. ConfigManager's previously
captured lambda$new$5 uses that getter as the module section name. The module
loader assignment therefore remains the direct unresolved identity link.
Do not infer that the configuration section is empty in a loaded module.

The nested sections are already resolved by ConfigObjectMapper.lambda$readInto$0:
it lowercases names with Locale.ROOT and replaces spaces with underscores.
Dimension and compound-biome fields consequently map to dimensions,
biomes.tags and biomes.biomes beneath the module section.

## Loaded file identity

The registry-r1 debug log at lines 14017 through 14020 identifies the loaded
quark-common.toml. Its existing custody-restored configuration copy is byte
identical to the Item 6 frozen file. Both SHA-256 values are
`94bfff490eea33f9bb105fae298606c4708ddb8af2f3df8630cc0f0ac7e85327`.
The log identity is recorded in `../zeta-config-event-fields/README.md`.
Reproduce the file comparison with:

```sh
sha256sum evidence/raw/item8/custody-r1/restored-download/configuration/config/quark-common.toml evidence/item-6/frozen/config/quark-common.toml
cmp evidence/raw/item8/custody-r1/restored-download/configuration/config/quark-common.toml evidence/item-6/frozen/config/quark-common.toml
sed -n '14017,14020p' evidence/raw/item8/custody-r1/restored-download/debug.log
```

This resolves loaded-file identity using retained evidence, without a new run.
It does not independently prove every effective field or module enablement.
