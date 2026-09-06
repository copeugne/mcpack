# Railways provider entry capture

Extractor: 60016db8b933160d1f967ae18d4191ff13065712.
Thirteen classes reproduced byte-for-byte in an independent capture.
This isolated generated increment retains full pinned javap output for the eight
annotated entries, common initializer/event delegate, both mixin plugins and the
structure-template save hook. Its size comes from unabridged bytecode and metadata.
Source capture is not provider closure.

```sh
uv run -m tools.inspect_item8_pool_elements --archive railways-0.2.1+neoforge-mc1.21.1.jar \
  --class-name com/railwayteam/railways/Railways.class \
  --class-name com/railwayteam/railways/config/neoforge/CRConfigsImpl.class \
  --class-name com/railwayteam/railways/events/CommonEvents.class \
  --class-name com/railwayteam/railways/mixin/CRMixinPlugin.class \
  --class-name com/railwayteam/railways/mixin/StructureMixin.class \
  --class-name com/railwayteam/railways/neoforge/RailwaysClientImpl.class \
  --class-name com/railwayteam/railways/neoforge/RailwaysImpl.class \
  --class-name com/railwayteam/railways/neoforge/datagen/DataGenerators.class \
  --class-name 'com/railwayteam/railways/neoforge/events/ClientEventsForge$ModBusEvents.class' \
  --class-name com/railwayteam/railways/neoforge/events/ClientEventsForge.class \
  --class-name com/railwayteam/railways/neoforge/events/CommonEventsForge.class \
  --class-name com/railwayteam/railways/neoforge/mixin/CRMixinPlugin.class \
  --class-name com/railwayteam/railways/util/neoforge/RegistrationListeningImpl.class \
  --output evidence/raw/item8/railways-provider-r1
```
