# Player Animator entry sources

Extractor 3996aee7. Both disassemblies and the manifest reproduce byte for
byte in the independent r1 capture. Manifest SHA-256:
85e2ae91df3e9e2b56155adf63d19dc330ea1c829a4e3b53e04ebeaefbf17fa5

```sh
uv run -m tools.inspect_item8_pool_elements --archive player-animation-lib-forge-2.0.4+1.21.1.jar --class-name dev/kosmx/playerAnim/forge/ForgeClientEvent.class --class-name dev/kosmx/playerAnim/impl/mixin/MixinConfig.class --output evidence/raw/item8/player-animation-provider-r1
```

The mod entry is explicitly Dist.CLIENT. It registers client animation-resource
reload and rendering-compatibility setup. The mixin plugin has empty lifecycle
callbacks, returns no additional mixins and conditionally permits bend-only
client hooks. These are client animation roles, not a generation contribution.
