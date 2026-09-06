# Supplementaries client entry dispositions

Extractor 5e58a1a41c9541b4cc201ff4e70cb2ccd47d94fc. Manifest SHA-256:
b0e1d475ee276f5923a241dcc90190b1c369119fd784f0963ffe67c65cd623c9.
Independent r1 matches every generated file.

Both SupplementariesForgeClient and PicklePlayer declare EventBusSubscriber
with modid supplementaries and value Dist.CLIENT. Their automatic registration
is client-only, not a dedicated-server structure-generation entry. The complete
annotation candidate set is bound by the existing parent-payload test.

```sh
uv run -m tools.inspect_item8_pool_elements --archive supplementaries-neoforge-1.21.1-3.6.8.jar --class-name net/mehvahdjukaar/supplementaries/platform/SupplementariesForgeClient.class --class-name net/mehvahdjukaar/supplementaries/client/renderers/platform/PicklePlayer.class --output evidence/raw/item8/supplementaries-client-entries-r1
```
