# CC:Tweaked provider entry paths

Extractor f1b6ab01d5e6c6f910c53338dd983673118b341f. Independent r1 reproduction matches
all nine disassemblies and the identity manifest. Manifest SHA-256:
eb5f29f53bff4cb1e977a4c2f35c4c1e0b4c70a582f2c77acd4a072b1b4327ab

```sh
uv run -m tools.inspect_item8_pool_elements --archive cc-tweaked-1.21.1-forge-1.119.0.jar --class-name dan200/computercraft/ComputerCraft.class --class-name dan200/computercraft/shared/ForgeCommonHooks.class --class-name dan200/computercraft/mixin/V3818_3Mixin.class --class-name dan200/computercraft/mixin/DataFixersMixin.class --class-name dan200/computercraft/mixin/ItemStackComponentizationFixMixin.class --class-name dan200/computercraft/mixin/V1460Mixin.class --class-name dan200/computercraft/impl/ComputerCraftAPIImpl.class --class-name 'dan200/computercraft/shared/integration/ForgePermissionRegistry$Provider.class' --class-name dan200/computercraft/shared/platform/PlatformHelperImpl.class --output evidence/raw/item8/cc-tweaked-provider-r1
```

These are automatic common entries, common mixins and common service providers.
Whole-provider membership remains to reconcile with their startup delegates.

The common mixins migrate existing computer/turtle item and block-entity data.
The common entry registers ModRegistry setup, peripheral capabilities and
Create/More Red integrations. ForgeCommonHooks delegates server lifecycle,
chunk, entity, interaction and loot events to CommonHooks. Service providers
expose computer APIs, permission creation and platform operations. Resolve
ModRegistry, CommonHooks and direct startup integrations before provider
closure. Do not audit every player-programmed turtle or network operation.
