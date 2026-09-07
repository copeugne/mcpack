# Grave event and resource delegates

Extractor 8fcd84b766722d53517b9b8946ce8c0cf90ce292. Independent r1 reproduction matches all files.
Manifest SHA-256: 08214afb2c7f64e433c24feff30c9d7e910aff9ce5bc4dc0c83b1e9fa4723174.

```sh
uv run -m tools.inspect_item8_pool_elements --archive youre-in-grave-danger-neoforge-2.0.13.jar --class-name com/b1n_ry/yigd/events/ServerEventHandler.class --class-name com/b1n_ry/yigd/events/YigdServerEventHandler.class --class-name com/b1n_ry/yigd/util/YigdResourceHandler.class --output evidence/item-8/sources/yigd-delegates
```

Registered server events and packaged custom resource consumption.
