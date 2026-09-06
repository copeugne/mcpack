# AzureLib Armor contribution sources

Extractor 2117e23d. Eight classes cover common/NeoForge initialization,
three declared services and two common hooks. Independent r1 reproduction
matches every source and manifest byte. Manifest SHA-256:
ae7ea280aed8ac0998e60626314df2d78c7048224c11c9104bb7d8fb42d06a22

```sh
uv run -m tools.inspect_item8_pool_elements --archive azurelibarmor-neo-1.21.1-3.1.2.jar --class-name mod/azure/azurelibarmor/AzureLib.class --class-name mod/azure/azurelibarmor/AzureLibMod.class --class-name mod/azure/azurelibarmor/common/internal/mixins/AbstractContainerMenuMixin_AzItemIDFix.class --class-name mod/azure/azurelibarmor/common/internal/mixins/ItemStackMixin_AzItemStackIdentityRegistry.class --class-name mod/azure/azurelibarmor/neoforge/NeoForgeAzureLibMod.class --class-name mod/azure/azurelibarmor/neoforge/platform/NeoForgeAzureLibInitializer.class --class-name mod/azure/azurelibarmor/neoforge/platform/NeoForgeAzureLibNetwork.class --class-name mod/azure/azurelibarmor/neoforge/platform/NeoForgePlatformHelper.class --output evidence/raw/item8/azurelib-armor-provider-r1
```

The sources register an item identity data component and animation packet,
provide platform lookup/network services, and preserve item identity through
container interactions. Initializer reload registration is client-conditional.
Packet dispatch and the unconditional rendering-compatibility initializer
remain to be bound before the provider disposition is complete.
