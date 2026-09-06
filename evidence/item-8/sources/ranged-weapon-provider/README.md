# Ranged Weapon API contribution sources

Extractor 08fc668a. Thirteen classes bind both entries, initialization and ten
common hooks. Independent r1 reproduction matches all source and manifest bytes.
Manifest SHA-256:
cfab4d2f0e3c4e1b4d4139deea58158c0ed58aaba43ab05f6dd0f299cd86a84f

```sh
uv run -m tools.inspect_item8_pool_elements --archive ranged_weapon_api-neoforge-2.3.3+1.21.1.jar --class-name net/fabric_extras/ranged_weapon/RangedWeaponMod.class --class-name net/fabric_extras/ranged_weapon/mixin/PersistentProjectileEntityMixin.class --class-name net/fabric_extras/ranged_weapon/mixin/attribute/EntityAttributesMixin.class --class-name net/fabric_extras/ranged_weapon/mixin/attribute/LivingEntityMixin.class --class-name net/fabric_extras/ranged_weapon/mixin/attribute/StatusEffectsMixin.class --class-name net/fabric_extras/ranged_weapon/mixin/item/BowItemMixin.class --class-name net/fabric_extras/ranged_weapon/mixin/item/ComponentMapBuilderAccessor.class --class-name net/fabric_extras/ranged_weapon/mixin/item/CrossbowItemMixin.class --class-name net/fabric_extras/ranged_weapon/mixin/item/ItemSettingMixin.class --class-name net/fabric_extras/ranged_weapon/mixin/item/ProjectileUtilMixin.class --class-name net/fabric_extras/ranged_weapon/mixin/item/RangedWeaponItemMixin.class --class-name net/fabric_extras/ranged_weapon/neoforge/NeoForgeMod.class --class-name net/fabric_extras/ranged_weapon/neoforge/client/NeoForgeClientMod.class --output evidence/raw/item8/ranged-weapon-provider-r1
```

Initialization adds ranged damage/haste effect modifiers. Common hooks register
attributes/effects, alter draw timing, item attributes and arrow damage/velocity,
and expose item components. NeoForge item-use ticking applies ranged haste;
client initialization is visual support. No generated-site entry point or
authored structure design. Preserve combat effects for later attribution.
No generic weapon mechanics or damage-balance audit is needed for membership.
