# Aethers Delight provider entries

Extractor a5ba054fa2ebf8d86a2a2e66231c7d4a51976379. Manifest SHA-256:
d81bb46059e7f892de6c77b74ef25b553a9f3400d45d6ebb7efe5304e4263000.
Independent r1 matches every generated file.

All six annotated entry candidates are retained. The main entry registers food,
blocks, block entities, loot and configuration; common/server callbacks log
configuration values. Other subscribers handle client setup/rendering, config
loading, creative-tab contents and development data generation. Packaged ore
and plant resource consumers are checked separately at provider acceptance.

```sh
uv run -m tools.inspect_item8_pool_elements --archive aethersdelight-0.1.4.2-1.21.1.jar --class-name net/zjjohn121110/aethersdelight/AethersDelight.class --class-name 'net/zjjohn121110/aethersdelight/AethersDelight$ClientModEvents.class' --class-name net/zjjohn121110/aethersdelight/Config.class --class-name net/zjjohn121110/aethersdelight/datagen/DataGenerators.class --class-name net/zjjohn121110/aethersdelight/event/ClientEvents.class --class-name net/zjjohn121110/aethersdelight/registry/ADCreativeTabs.class --output evidence/raw/item8/aethers-delight-provider-r1
```
