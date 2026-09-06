# create-dragons-plus-conditional

Extractor 00c6a943f0e3bde95118d5809decea68e78a57f0. Independent r1 reproduction
matches all three disassemblies and the identity manifest. Manifest SHA-256:
c45e2412785aa38544e33ef491a9983cd5d4db094d26e8fcd32bf85d9b4eb14c

```sh
uv run -m tools.inspect_item8_pool_elements --archive CreateDragonsPlus-1.11.2b.jar --nested-archive META-INF/jarjar/conditional-mixin-neoforge-0.6.4.jar --class-name me/fallenbreath/conditionalmixin/ConditionalMixinMod.class --class-name me/fallenbreath/conditionalmixin/api/mixin/RestrictiveMixinConfigPlugin.class --class-name me/fallenbreath/conditionalmixin/neoforge/ConditionalMixinNeoForge.class --output evidence/raw/item8/create-dragons-plus-conditional-r1
```

The nested NeoForge and common entries have no initialization behavior.
RestrictiveMixinConfigPlugin uses a restriction checker for mixin selection and
annotation cleanup during application. It declares no additional generation
content. This is shared conditional injection infrastructure, not a family.
Do not expand family membership into a general restriction-checker audit.

Bind the full parent and nested payload in the provider closure before
changing the provider count. Preserve consumer gameplay effects.
