# GlitchCore contribution sources

Extractor 34d0808. Independent r1 reproduction matches all twenty sources and
the manifest byte for byte. Manifest SHA-256:
491a475ee26288951ffdac1e0e66dd7cd94cef92bd94193fd2f80a61dd9ed609

```sh
uv run -m tools.inspect_item8_pool_elements --archive GlitchCore-neoforge-1.21.1-2.1.0.2.jar --class-name glitchcore/mixin/MixinItemStack.class --class-name glitchcore/mixin/MixinServerConfigurationPacketListenerImpl.class --class-name glitchcore/mixin/MixinServerLevel.class --class-name glitchcore/neoforge/GlitchCoreNeoForge.class --class-name glitchcore/neoforge/handlers/ColorsEventHandler.class --class-name glitchcore/neoforge/handlers/InteractionEventHandler.class --class-name glitchcore/neoforge/handlers/LevelRenderEventHandler.class --class-name glitchcore/neoforge/handlers/RegisterCommandsEventHandler.class --class-name glitchcore/neoforge/handlers/RegisterParticleProvidersEventHandler.class --class-name glitchcore/neoforge/handlers/RegistryEventHandler.class --class-name glitchcore/neoforge/handlers/TagsUpdatedEventHandler.class --class-name glitchcore/neoforge/handlers/TickEventHandler.class --class-name glitchcore/neoforge/handlers/ToolModificationEventHandler.class --class-name glitchcore/neoforge/handlers/TooltipEventHandler.class --class-name glitchcore/neoforge/handlers/VillagerTradesEventHandler.class --class-name glitchcore/neoforge/mixin/MixinServerPlayer.class --class-name glitchcore/neoforge/mixin/impl/MixinBlockHelper.class --class-name glitchcore/neoforge/mixin/impl/MixinEnvironment.class --class-name glitchcore/neoforge/mixin/impl/MixinPacketHandler.class --class-name glitchcore/neoforge/mixin/impl/MixinRenderHelper.class --output evidence/raw/item8/glitchcore-provider-r1
```

Preserves twelve automatic entries and eight common hooks. The hooks forward
consumer events, configure networking and adapt existing block/entity/client
operations. The loader invokes glitchcore.core.GlitchCore.init; that common
initializer remains the concrete startup boundary to resolve before closure.
