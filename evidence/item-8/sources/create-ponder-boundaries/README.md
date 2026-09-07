# Embedded Ponder entry and scene boundaries

Extractor: 28badcf334e508dbe249496c76b778b9589846de.
Seventeen complete classes independently reproduce byte-for-byte: all six
annotated entries, five service implementations, three declared common accessors,
common/client initialization and the scene template consumer. This isolated
generated increment records the final embedded-library membership boundary.

```sh
uv run -m tools.inspect_item8_pool_elements --archive create-1.21.1-6.0.10.jar \
  --nested-archive META-INF/jarjar/ponder-neoforge-1.0.82+mc1.21.1.jar \
  --class-name net/createmod/catnip/platform/NeoForgeClientHooksHelper.class \
  --class-name net/createmod/catnip/platform/NeoForgeFluidHelper.class \
  --class-name net/createmod/catnip/platform/NeoForgeHooksHelper.class \
  --class-name net/createmod/catnip/platform/NeoForgeNetworkHelper.class \
  --class-name net/createmod/catnip/platform/NeoForgePlatformHelper.class \
  --class-name 'net/createmod/ponder/NeoForgePonder$Events.class' \
  --class-name 'net/createmod/ponder/NeoForgePonder$ModBusEvents.class' \
  --class-name net/createmod/ponder/NeoForgePonder.class \
  --class-name 'net/createmod/ponder/NeoForgePonderClient$ClientEvents.class' \
  --class-name 'net/createmod/ponder/NeoForgePonderClient$ModBusClientEvents.class' \
  --class-name net/createmod/ponder/NeoForgePonderClient.class \
  --class-name net/createmod/ponder/Ponder.class \
  --class-name net/createmod/ponder/PonderClient.class \
  --class-name net/createmod/ponder/foundation/registration/PonderSceneRegistry.class \
  --class-name net/createmod/ponder/mixin/accessor/BiomeManagerAccessor.class \
  --class-name net/createmod/ponder/mixin/accessor/EntityAccessor.class \
  --class-name net/createmod/ponder/mixin/accessor/MinecraftServerAccessor.class \
  --output evidence/raw/item8/create-ponder-boundaries-r1
```
