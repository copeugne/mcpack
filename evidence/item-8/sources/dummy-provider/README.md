# Target dummy contribution sources

Extractor 521b7f0a. Eleven source classes cover initialization, the event
callbacks, common mixins and item/dispenser placement. This generated capture
is isolated because exact disassembly is the reproducible membership source.
Independent r1 reproduction matches every byte and the identity manifest.
Manifest SHA-256: a8985f1a1ebcf35bdde52c8efdf335ebd6fbd12fc09eb6f42f6ef19e9e44568e

```sh
uv run -m tools.inspect_item8_pool_elements --archive dummmmmmy-1.21-2.0.12-neoforge.jar --class-name 'net/mehvahdjukaar/dummmmmmy/Dummmmmmy$SpawnDummyBehavior.class' --class-name net/mehvahdjukaar/dummmmmmy/Dummmmmmy.class --class-name net/mehvahdjukaar/dummmmmmy/common/ModEvents.class --class-name net/mehvahdjukaar/dummmmmmy/common/TargetDummyItem.class --class-name net/mehvahdjukaar/dummmmmmy/mixins/ArmorStandFIxMixin.class --class-name net/mehvahdjukaar/dummmmmmy/mixins/EnchantmentMixin.class --class-name net/mehvahdjukaar/dummmmmmy/mixins/LivingEntityMixin.class --class-name net/mehvahdjukaar/dummmmmmy/mixins/PlayerMixin.class --class-name net/mehvahdjukaar/dummmmmmy/mixins/SwordItemMixin.class --class-name net/mehvahdjukaar/dummmmmmy/mixins/ToolItemMixin.class --class-name net/mehvahdjukaar/dummmmmmy/neoforge/DummmmmmyForge.class --output evidence/raw/item8/dummy-provider-r1
```

Startup registers the target-dummy entity/item, particles, attributes,
configuration and client messages. Entity events implement scarecrow/decoy
behavior and damage/healing displays. Item use and dispensing place a dummy.
The six common hooks handle armor-stand rotation, enchantment applicability,
damage/healing and equipment wear. These sources define no generated site.
