# Supplementaries map lookup

Extractor c989eb6d0b1345ef5a1e00549ff7445dc8b08f62. Manifest SHA-256:
3e28fdfcaf21c79d87ef0ad595aa145dea869903dd1692776fc9643bebdac3f2.
Independent r1 matches every generated file.

AdventurerMapsHandler consumes existing structure holders and the existing
adventure-map destination tag. It requests a location or a Quark quill, then
creates and decorates a map item. It adds no independent authored layout.
The previously recorded null-returning Quark implementation remains a
limitation; this capture does not establish successful map or quill creation.

```sh
uv run -m tools.inspect_item8_pool_elements --archive supplementaries-neoforge-1.21.1-3.6.8.jar --class-name net/mehvahdjukaar/supplementaries/common/entities/trades/AdventurerMapsHandler.class --output evidence/raw/item8/supplementaries-map-lookup-r1
```
