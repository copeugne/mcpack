# Supplementaries retained integration entries

Extractor 5355d74b8c0a9cf4605cbcf63ad14aaf92eec7d2. Manifest SHA-256:
1ec5f3694856a3a56bf280d1ceb4bf980a741f63fe7ad1fddba78ea6c7d2b1d3.
Independent r1 matches every generated file.

Retains the Create, CC:Tweaked, Curios, Farmer's Delight and Quark integration
entries and direct platform delegates for provider membership interpretation.
Source coverage alone does not close Supplementaries.

```sh
uv run -m tools.inspect_item8_pool_elements --archive supplementaries-neoforge-1.21.1-3.6.8.jar --class-name net/mehvahdjukaar/supplementaries/integration/CCCompat.class --class-name net/mehvahdjukaar/supplementaries/integration/CreateCompat.class --class-name net/mehvahdjukaar/supplementaries/integration/CuriosCompat.class --class-name net/mehvahdjukaar/supplementaries/integration/FarmersDelightCompat.class --class-name net/mehvahdjukaar/supplementaries/integration/QuarkCompat.class --class-name net/mehvahdjukaar/supplementaries/integration/platform/CCCompatImpl.class --class-name net/mehvahdjukaar/supplementaries/integration/platform/CreateCompatImpl.class --class-name net/mehvahdjukaar/supplementaries/integration/platform/QuarkCompatImpl.class --output evidence/raw/item8/supplementaries-integrations-r1
```
