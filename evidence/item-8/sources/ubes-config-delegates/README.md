# Ubes Delight configuration delegates

Extractor 77c035a4dbda38cf1d61256799e57e37f4b57ff7. Manifest SHA-256:
7f66a6ae89d97fd1e117a53a6b86fad2e8d45ad83a5fd0228ce83acf77fbef41.
Independent r1 matches every generated file.

Configuration forwards settings to ConfigurationImpl. The implementation initializes
MidnightConfig with its annotated options and exposes their values; it has no
independent generation callback. Crop consumers are in the provider capture.

```sh
uv run -m tools.inspect_item8_pool_elements --archive ubesdelight-neoforge-1.21.1-0.4.13.jar --class-name com/chefmooon/ubesdelight/common/Configuration.class --class-name com/chefmooon/ubesdelight/common/neoforge/ConfigurationImpl.class --output evidence/raw/item8/ubes-config-delegates-r1
```
