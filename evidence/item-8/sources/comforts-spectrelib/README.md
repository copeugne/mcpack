# comforts-spectrelib source boundaries

Extractor fbbebc88ce6c88abda9d4856dde5ca3d1518aa2f. Independent r1 reproduction matches all disassemblies
and the identity manifest. Manifest SHA-256:
a7bc109634fc422c5e64b85dd7ecd264de17cf9bd1177fdfda251a59078fe02c

```sh
uv run -m tools.inspect_item8_pool_elements --archive comforts-neoforge-9.0.5+1.21.1.jar --nested-archive META-INF/jarjar/spectrelib-neoforge-0.17.2+1.21.jar --class-name com/illusivesoulworks/spectrelib/SpectreNeoForgeMod.class --class-name com/illusivesoulworks/spectrelib/platform/NeoForgeConfigHelper.class --output evidence/item-8/sources/comforts-spectrelib
```

Captured entry, registration, sleep-event and configuration boundaries for
provider membership inspection. These captures do not establish gameplay
compatibility or observed world generation.
