# Ubes Delight configuration delegates

Extractor 77c035a4dbda38cf1d61256799e57e37f4b57ff7. Manifest SHA-256:
7452a1b57ebcff8b9aedde0c4bde57d6db5c7a661a08cf7219896d4e2c3dc817.
Independent r1 matches every generated file.

AutoCommand builds commands for reading or setting configuration fields and writes
configuration via MidnightConfig. MidnightLibConfig declares library UI options.
Neither delegate constructs an independent generation route.

```sh
uv run -m tools.inspect_item8_pool_elements --archive ubesdelight-neoforge-1.21.1-0.4.13.jar --nested-archive META-INF/jars/midnightlib-1.9.2+1.21.1-neoforge.jar --class-name eu/midnightdust/core/config/MidnightLibConfig.class --class-name eu/midnightdust/lib/config/AutoCommand.class --output evidence/raw/item8/ubes-midnightlib-delegates-r1
```
