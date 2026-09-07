# IDAS existing world geometry integration

Ten required size entries integrated for five families using existing captured
world evidence. No new run, archive, renderer or measurement system is added.

| Family | Sample x,y,z extent in blocks | Preserved source |
| --- | --- | --- |
| ancient_portal | 37,35,57 | world-bounds observation18; run-a/ordinary/chunks.jsonl line2252, seed42, Nether variant |
| bearclaw_inn | 27,20,53 | world-bounds observation164; run-a/mountainous/chunks.jsonl line12226, seed6671238423019257953 |
| apothecary_abode | 40,39,60 | integrated-stronghold-geometry-r1/chunks.jsonl line202 |
| pillager_fortress | 63,89,63 | illager-geometry-r1/chunks.jsonl line2151 |
| ruins_of_the_deep | 60,103,74 | vanilla-final-geometry-r1/chunks.jsonl line2122 |

Observation indexes are zero-based; decoded file lines are one-based. Additional
capture paths are under evidence/raw/item8. Each source has a full start chunk.
Exact root, chunk position, envelope and source identity remain in the attributes.
The two original observations already belong to the hash-bound world-bounds
catalog derived from preserved Item7 evidence. The other three decoded files
were checked byte-for-byte against their existing downloaded-restored copies;
file hashes match the committed archive manifests, and manifest hashes match
the existing verified downloaded-restore receipts. Those artifacts are bound
in the corresponding family evidence mappings. Existing archive revisions and
raw observations remain unchanged.

## Derivation and limits

The existing observed_bounds function in src/mcpack_evidence/item8_world_bounds.py
validates box order and computes each axis as maximum upper bound minus minimum
lower bound plus1. It operates on ChunkRecord from the preserved decoder output.
The first two observations already contain that result; the three later records
were inspected with the same function. No alternative decoder or geometry logic
is introduced. These are saved-piece samples, including air and padding. A full
start chunk does not prove that all component chunks populated or every possible
branch generated. Samples do not establish family-wide bounds, occupied volume,
burial or loot/enemy populations. Other variants remain separately documented.

## Reproduction

Use the exact referenced decoded lines and existing observed_bounds function,
or inspect the two named catalog observations. Verify decoded hashes against the
bound manifests and restored copies before rebuilding the inventory.

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/idas-existing-world-geometry-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

Use a fresh output path. Only these five families and input identity may change.
Other family attributes, final integration, acceptance and reviewed delivery
remain open.24 other connected IDAS assemblies still need geometry assessment.
