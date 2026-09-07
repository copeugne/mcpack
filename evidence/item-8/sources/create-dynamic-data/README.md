# Create dynamic-data writer

Extractor: 6c265951e0cf4bf00613b1e2ae5bc37ac9eea22a.
The full RuntimeDataGenerator capture independently reproduces byte-for-byte.
This isolated source increment follows the concrete AddPackFindersEvent call
observed in CommonEvents.ModBusEvents. It is required to account for runtime
resources outside the packaged-data catalog.

```sh
uv run -m tools.inspect_item8_pool_elements --archive create-1.21.1-6.0.10.jar \
  --class-name com/simibubi/create/foundation/data/RuntimeDataGenerator.class \
  --output evidence/raw/item8/create-dynamic-data-r1
```
