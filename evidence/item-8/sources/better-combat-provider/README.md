# Better Combat membership entry paths

Extractor d2788da1. Independent r1 reproduction matches source and manifest
bytes. Manifest SHA-256:
7f90725b678a3a3965742f31d2939b4ee5c56e35b3e40bbbc4afed3d25c22b00

```sh
uv run -m tools.inspect_item8_pool_elements --archive bettercombat-neoforge-2.3.2+1.21.1.jar --class-name net/bettercombat/BetterCombatMod.class --class-name net/bettercombat/mixin/BetterCombatMixinPlugin.class --class-name net/bettercombat/mixin/DataComponentTypesMixin.class --class-name net/bettercombat/mixin/EnchantmentMixin.class --class-name net/bettercombat/mixin/ItemStackMixin.class --class-name net/bettercombat/mixin/RangedWeaponItemMixin.class --class-name net/bettercombat/mixin/ServerPlayNetworkHandlerMixin.class --class-name net/bettercombat/mixin/player/LivingEntityAccessor.class --class-name net/bettercombat/mixin/player/LivingEntityMixin.class --class-name net/bettercombat/mixin/player/PlayerEntityAccessor.class --class-name net/bettercombat/mixin/player/PlayerEntityMixin.class --class-name net/bettercombat/mixin/player/PlayerEntityRangeMixin.class --class-name net/bettercombat/neoforge/NeoForgeEvents.class --class-name net/bettercombat/neoforge/NeoForgeMod.class --class-name net/bettercombat/neoforge/client/NeoForgeClientEvents.class --class-name net/bettercombat/neoforge/client/NeoForgeClientMod.class --class-name net/bettercombat/neoforge/network/NetworkEvents.class --output evidence/raw/item8/better-combat-provider-r1
```

Five automatic entries, ten common hooks, the plugin and common initializer.
Entries register combat sounds/particles, configuration and attack/sync packets.
Hooks modify existing player combat, item attributes and interaction ranges.
The plugin requires the retained Player Animator class and supplies no additional
hooks. Remaining membership checks: weapon resource loading and compatibility
initialization. Reuse Tiny Config evidence because all nested member bytes match
the retained Village Taverns copy despite different nested archive hashes.
