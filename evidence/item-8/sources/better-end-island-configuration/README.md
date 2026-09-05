# Better End Island configuration binding

Manifest SHA-256: `56c0b14dfb0f0a11156acd745548cb01085bce05ed965bbc38bdbeae19fed3cb`.
Frozen TOML: `evidence/item-6/frozen/config/betterendisland-neoforge-1_21.toml`, SHA-256
`9f967435aa86ab5959ee76a215cde5176bee106fae08df3b6e440c77a823867a`.

BEIConfigNeoForge defines the named boolean keys under YUNG's Better End Island.
ConfigModuleNeoForge.init registers that spec as COMMON with the exact frozen
filename. bakeConfig reads the ConfigValue booleans into the corresponding
BetterEndIslandCommon.CONFIG fields. The platform/gateway keys map to
useVanillaSpawnPlatform/useVanillaEndGateways. Both frozen values and constructor
defaults are false, selecting the custom branches when the captured hooks apply.
The egg-repeat key is false; bell, initial tower and resummoned tower keys are true.
This binds keys to fields, not mixin activation or observed generation.

Reproduce with extractor revision `0e4a8af` and a fresh output directory:

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive YungsBetterEndIsland-1.21.1-NeoForge-3.1.2.jar \
  --class-name com/yungnickyoung/minecraft/betterendisland/config/BEIConfigNeoForge.class \
  --class-name com/yungnickyoung/minecraft/betterendisland/module/ConfigModule.class \
  --class-name com/yungnickyoung/minecraft/betterendisland/module/ConfigModuleNeoForge.class \
  --output evidence/raw/item8/better-end-island-configuration-reproduction
```

Before adding this README, recursive comparison with fresh reproduction matched
every file byte-for-byte. Scoped extractor Ruff/Basedpyright passed. No runtime
or new measurement system was added. Inventory integration remains pending.
