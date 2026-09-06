# Fabric GameTest consumers

Extractor: ad51ae442f208cddbe85270ec4cd1fe1d0908565.
Eight complete classes independently reproduce byte for byte. These retain the
five declared mixins and entry/initialization consumers of the test fixture.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-gametest-api-v1-2.0.5+29f188ce19.jar --class-name net/fabricmc/fabric/mixin/gametest/TestCommandMixin.class --class-name net/fabricmc/fabric/mixin/gametest/GameTestRegistryMixin.class --class-name net/fabricmc/fabric/mixin/gametest/GameTestHooksMixin.class --class-name net/fabricmc/fabric/mixin/gametest/StructureTemplateManagerMixin.class --class-name net/fabricmc/fabric/mixin/gametest/TestServerMixin.class --class-name net/fabricmc/fabric/impl/gametest/FabricGameTestModInitializer.class --class-name org/sinytra/fabric/gametest_api/generated/GeneratedEntryPoint.class --class-name org/sinytra/fabric/gametest_api_v1/FabricGameTestApiV1.class --output evidence/raw/item8/fabric-gametest-consumers-r1
```
