# Decoder preparation validation

Item 10's expanded dimension scope exposed a specific defect in `world_regions`:
custom dimension paths were labeled Overworld with Overworld build geometry.
The existing decoder now retains vanilla contexts and requires explicit build
geometry for a named custom dimension. It rejects unidentified nested region
directories instead of silently counting them as Overworld. This changes region
identification, not the accepted Item 7 chunk-record schema or old raw evidence.

Focused validation command:

```sh
uv run --no-sync pytest -q tests/item7/test_world_region_dimensions.py tests/item7/test_anvil_decoder.py
```

Result: 22 passed. Coverage includes all four existing compression paths, the
existing Anvil integrity cases, preserved vanilla contexts, nested custom IDs,
missing/invalid custom geometry and unidentified directory layout. Focused Ruff
and type checks accompany this change. This is preparation validation, not an
Item 10 measured density or a repeated Item 7 acceptance audit.

A second reuse limit remains: the Item 7 normalized structure-start record retains
IDs and piece boxes but omits the raw start's `ChunkX` and `ChunkZ`. Item 10 must
retain and verify authoritative start coordinates before using those normalized
records as the complete occurrence input. The reconstructed density counter is
still insufficient; no accepted count has been produced with it.
