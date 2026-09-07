# Quick Right Click active entry points

Extractor ddfbd738. Seven NeoForge entry/event/common-hook classes. Independent
r1 reproduction matches all source and manifest bytes. Manifest SHA-256:
4f9724746eeee02ac4eca0bf9fd2971528211b78efd60f550bfcc3325f129649

```sh
uv run -m tools.inspect_item8_pool_elements --archive quickrightclick-1.21.1-1.9.jar --class-name com/natamus/quickrightclick/ModNeoForge.class --class-name com/natamus/quickrightclick/neoforge/events/NeoForgeQuickEvent.class --class-name com/natamus/quickrightclick_common_neoforge/ModCommon.class --class-name com/natamus/quickrightclick_common_neoforge/events/QuickEvent.class --class-name com/natamus/quickrightclick_common_neoforge/mixin/LivingEntityMixin.class --class-name com/natamus/quickrightclick_common_neoforge/mixin/ServerPlayerMixin.class --class-name com/natamus/quickrightclick_common_neoforge/mixin/ShulkerBoxBlockEntityMixin.class --output evidence/raw/item8/quick-right-click-provider-r1
```

The active entry uses Collective loading/configuration support and registers
item right-click handling. The handler dispatches held beds, tables and storage
items. Hooks restore sleeping/respawn and temporary shulker state. Remaining
binding: temporary bed/shulker placement and the external Collective mixin
plugin. Forge/Fabric counterparts are not the active NeoForge entry path.
