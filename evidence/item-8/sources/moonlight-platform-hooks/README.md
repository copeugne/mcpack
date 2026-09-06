# Moonlight platform hooks

Extractor f1d6b260527afacd421743f0366d33b5fd64657b. Independent r1 reproduction matches all
disassemblies and the identity manifest. Manifest SHA-256:
a6866cc98941df5676b89ccd4c7d87103bef79c06f6bc96b54493e88011e478f

```sh
uv run -m tools.inspect_item8_pool_elements --archive moonlight-neoforge-1.21.1-3.0.17.jar --class-name net/mehvahdjukaar/moonlight/core/mixins/platform/BeeGoalMixin.class --class-name net/mehvahdjukaar/moonlight/core/mixins/platform/ConditionHackMixin.class --class-name net/mehvahdjukaar/moonlight/core/mixins/platform/ConfigTrackerMixin.class --class-name net/mehvahdjukaar/moonlight/core/mixins/platform/ContextAwareReloadListenerAccessor.class --class-name net/mehvahdjukaar/moonlight/core/mixins/platform/FireBlockMixin.class --class-name net/mehvahdjukaar/moonlight/core/mixins/platform/HoldingPlayerMixin.class --class-name net/mehvahdjukaar/moonlight/core/mixins/platform/MinecraftServerMixin.class --class-name net/mehvahdjukaar/moonlight/core/mixins/platform/SelfEntitySpawnDataMixin.class --class-name net/mehvahdjukaar/moonlight/core/mixins/platform/SelfModFlowingFluidMixin.class --output evidence/item-8/sources/moonlight-platform-hooks
```

All nine common hooks in the platform configuration. Provider disposition remains open.
