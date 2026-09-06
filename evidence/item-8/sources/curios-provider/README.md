# Curios entry and common hook boundaries

Extractor dc6d701d4448ebe43fd44ec7c7662850c3cabf81. Independent r1 reproduction matches all
disassemblies and the identity manifest. Manifest SHA-256:
e1d8df4787a575099d1181f4519104940bc0d87e29d46c1fb236c3e7129b0270

```sh
uv run -m tools.inspect_item8_pool_elements --archive curios-neoforge-9.5.1+1.21.1.jar --class-name top/theillusivec4/curios/Curios.class --class-name 'top/theillusivec4/curios/Curios$ClientProxy.class' --class-name top/theillusivec4/curios/platform/NeoForgeCurios.class --class-name top/theillusivec4/curios/mixin/core/AccessorEntity.class --class-name top/theillusivec4/curios/mixin/core/MixinCuriosTriggers.class --class-name top/theillusivec4/curios/mixin/core/MixinCuriosTriggersEquip.class --class-name top/theillusivec4/curios/mixin/core/MixinApplyBonusCount.class --class-name top/theillusivec4/curios/mixin/core/MixinCuriosApi.class --class-name top/theillusivec4/curios/mixin/core/MixinCuriosDataProvider.class --class-name top/theillusivec4/curios/mixin/core/MixinEnchantedCountIncreaseFunction.class --class-name top/theillusivec4/curios/mixin/core/MixinInventory.class --class-name top/theillusivec4/curios/mixin/core/MixinLivingEntity.class --class-name top/theillusivec4/curios/mixin/core/MixinNbtPredicate.class --class-name top/theillusivec4/curios/mixin/core/MixinPiglinAi.class --class-name top/theillusivec4/curios/mixin/core/MixinPowderSnowBlock.class --class-name top/theillusivec4/curios/mixin/core/MixinV1460.class --output evidence/item-8/sources/curios-provider
```

Provider membership inspection, not general equipment or gameplay acceptance.
