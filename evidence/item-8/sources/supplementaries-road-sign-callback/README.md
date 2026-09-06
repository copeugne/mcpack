# Supplementaries deferred road-sign callback

Extractor dabd67533dd5e8dbf0c8616b1615f56d9f07d94d. Manifest SHA-256: a6a99e646dd7b65793defda3168306b20e1a70a901b7d37e024d4aea3f6f5194. Independent r1 matches every generated file.

The road-sign feature places this generator block entity and supplies its configuration. The callback starts a destination lookup and passes the result to the already captured RoadSignFeature.applyPostProcess. Preserve asynchronous lookup, failure cleanup and saved configuration as parts of the same sign generation path, not additional families.

```sh
uv run -m tools.inspect_item8_pool_elements --archive supplementaries-neoforge-1.21.1-3.6.8.jar --class-name net/mehvahdjukaar/supplementaries/common/block/tiles/BlockGeneratorBlockTile.class --output evidence/raw/item8/supplementaries-road-sign-callback-r1
```
