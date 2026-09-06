# Create common events and schematic consumers

Extractor: 76ac38c743939fef364d7cc8862750c46d9d326f.
Five complete disassemblies independently reproduce byte-for-byte. This isolated
generated increment records common-event dispatch and the uploaded schematic
construction path. The dynamic-data generator called by ModBusEvents remains
a concrete membership question; this capture does not close Create as a provider.

```sh
uv run -m tools.inspect_item8_pool_elements --archive create-1.21.1-6.0.10.jar \
  --class-name com/simibubi/create/foundation/events/CommonEvents.class \
  --class-name 'com/simibubi/create/foundation/events/CommonEvents$ModBusEvents.class' \
  --class-name com/simibubi/create/content/schematics/SchematicProcessor.class \
  --class-name com/simibubi/create/content/schematics/SchematicPrinter.class \
  --class-name com/simibubi/create/content/schematics/ServerSchematicLoader.class \
  --output evidence/raw/item8/create-common-schematics-r1
```
