# comforts-provider source boundaries

Extractor fbbebc88ce6c88abda9d4856dde5ca3d1518aa2f. Independent r1 reproduction matches all disassemblies
and the identity manifest. Manifest SHA-256:
bc8225ebfe7a6c9adb2ae59292190d4be3b3f4a3664e25c6cbf3b31eadc2846c

```sh
uv run -m tools.inspect_item8_pool_elements --archive comforts-neoforge-9.0.5+1.21.1.jar --class-name com/illusivesoulworks/comforts/ComfortsNeoForgeMod.class --class-name com/illusivesoulworks/comforts/ComfortsCommonMod.class --class-name com/illusivesoulworks/comforts/common/ComfortsCommonEventsListener.class --class-name com/illusivesoulworks/comforts/common/ComfortsRegistry.class --class-name com/illusivesoulworks/comforts/common/ComfortsEvents.class --class-name com/illusivesoulworks/comforts/mixin/AccessorPlayer.class --class-name com/illusivesoulworks/comforts/mixin/MixinServerSleepStatus.class --class-name com/illusivesoulworks/comforts/mixin/MixinSleepStatus.class --class-name com/illusivesoulworks/comforts/platform/NeoForgePlatformHelper.class --class-name com/illusivesoulworks/comforts/platform/NeoForgeRegistryProvider.class --class-name com/illusivesoulworks/comforts/platform/NeoForgeRegistryUtil.class --class-name com/illusivesoulworks/comforts/platform/NeoForgeSleepEvents.class --output evidence/item-8/sources/comforts-provider
```

Captured entry, registration, sleep-event and configuration boundaries for
provider membership inspection. These captures do not establish gameplay
compatibility or observed world generation.
