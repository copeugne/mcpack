# Module section assignment

Captured at `8e25d4c`; identities are in `identities.json`. Reproduction at
`b38d3f4` matched byte for byte with the unchanged selection:

```sh
uv run -m tools.inspect_item8_pool_elements --archive Zeta-1.1-40.jar --class-name org/violetmoon/zeta/module/ZetaModuleManager.class --output evidence/raw/item8/zeta-module-assignment-b38d3f4
```

constructAndSetup logs the TentativeModule display name, constructs its class,
and copies its category, displayName and lowercaseName to ZetaModule. This is
the assignment consumed by ConfigManager's module-section getter. Name
derivation is preserved in `../zeta-module-name`. Other manager operations are
retained as raw source context, not additional inventory acceptance claims.
