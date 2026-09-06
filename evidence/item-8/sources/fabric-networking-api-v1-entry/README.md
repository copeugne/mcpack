# fabric-networking-api-v1-entry source checkpoint

Extractor a6fa580. Independent r1 reproduction matches the manifest and every
disassembly byte. Manifest SHA-256: 971327a550fa9613691f4ef1f17389cf24d00373a109cce7fe7e788618d7bfeb.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-networking-api-v1-4.3.0+30a980d919.jar --class-name net/fabricmc/fabric/mixin/networking/ClientConnectionMixin.class --class-name net/fabricmc/fabric/mixin/networking/EntityTrackerEntryMixin.class --class-name net/fabricmc/fabric/mixin/networking/GenericPacketSplitterMixin.class --class-name net/fabricmc/fabric/mixin/networking/LoginQueryRequestS2CPacketMixin.class --class-name net/fabricmc/fabric/mixin/networking/LoginQueryResponseC2SPacketMixin.class --class-name net/fabricmc/fabric/mixin/networking/NetworkRegistryMixin.class --class-name net/fabricmc/fabric/mixin/networking/ServerCommonNetworkHandlerMixin.class --class-name net/fabricmc/fabric/mixin/networking/ServerConfigurationNetworkHandlerMixin.class --class-name net/fabricmc/fabric/mixin/networking/ServerLoginNetworkHandlerMixin.class --class-name net/fabricmc/fabric/mixin/networking/ServerPlayNetworkHandlerMixin.class --class-name net/fabricmc/fabric/mixin/networking/accessor/EntityTrackerAccessor.class --class-name net/fabricmc/fabric/mixin/networking/accessor/NetworkRegistryAccessor.class --class-name net/fabricmc/fabric/mixin/networking/accessor/ServerChunkLoadingManagerAccessor.class --class-name net/fabricmc/fabric/mixin/networking/accessor/ServerCommonNetworkHandlerAccessor.class --class-name net/fabricmc/fabric/mixin/networking/accessor/ServerLoginNetworkHandlerAccessor.class --class-name org/sinytra/fabric/networking_api/NetworkingEventHooks.class --class-name org/sinytra/fabric/networking_api/generated/GeneratedEntryPoint.class --output evidence/raw/item8/fabric-networking-api-v1-entry-r1
```

The generated initializer is empty. Automatic networking event hooks and fifteen common networking hooks are retained for contribution-role reconciliation.

Source capture alone does not close whole-provider membership.
