# Diesel oil data boundary

Extractor 6d3df5bf4347f8da59d00538989458f4d432969f. Independent r1 reproduction matches the
disassembly and identity manifest. Manifest SHA-256:
3a526470b2149eb8a87fde6003b6cc7f44134f996c65ad542538115d132960c0

```sh
uv run -m tools.inspect_item8_pool_elements --archive createdieselgenerators-1.21.1-1.3.15.jar --class-name com/jesz/createdieselgenerators/world/OilChunksSavedData.class --output evidence/item-8/sources/diesel-oil-data
```

Oil command target for distinguishing saved resource values from authored families.
This does not validate resource balance or persistence correctness.
