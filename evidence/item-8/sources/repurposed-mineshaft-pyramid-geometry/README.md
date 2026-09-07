# Repurposed mineshaft and pyramid geometry integration

Four required size attributes are integrated from existing full-start observations.
No new generation, measurement or tool is needed. The existing world-bounds
artifact and inventory builder already retain and derive the envelopes; this
increment accepts their explicit, limited use in the family decisions.

## Direct examples

- repurposed_structures:mineshaft: run-a/ordinary/chunks.jsonl line 2085, seed 42, minecraft:the_nether chunk 4,0, repurposed_structures:mineshaft_soul. Envelope [8, 2, -75, 144, 21, 32], inclusive size [137, 20, 108].
- repurposed_structures:pyramid: run-a/mountainous/chunks.jsonl line 2498, seed 6671238423019257953, minecraft:the_nether chunk 12,15, repurposed_structures:pyramid_nether. Envelope [182, 34, 230, 202, 46, 250], inclusive size [21, 13, 21].

Coordinates are inclusive: each size equals maximum minus minimum plus one.
The examples establish assembled saved-piece extents, including air and padding.
They do not establish occupied volume, component population, exposure, typical
size or bounds across every variant. The authoritative entries retain all existing
observed extent alternatives, not only the examples listed above. Repeated run-a
and run-b observations are not independent family samples.

These two families still need seven other required attribute assessments each.
Their size integration does not mark either family, or Item 8, complete.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/repurposed-mineshaft-pyramid-geometry-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

Use a fresh output path. Only the two named families and input identity may change.
The tracked world-bounds decoder/builder provide the derivation; direct references
above locate the accepted observations without an additional measurement system.
