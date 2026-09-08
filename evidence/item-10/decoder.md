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

## Registry census preparation

The existing `tools/analyze_structure_density.py` now reads stopped-world Anvil
files instead of accepting occurrence JSONL and a caller-supplied denominator.
`decode_region_payloads` exposes the validated raw NBT alongside the unchanged
Item 7 normalized record. The counter requires each raw start's `ChunkX` and
`ChunkZ` to match its stored source chunk and rejects key/ID disagreement. It
retains per-start coordinates, counts and MCA/external-MCC source hashes.

A census succeeds only when every selected coordinate in the inclusive rectangle
is present exactly once with status `minecraft:full`. Halo chunks do not inflate
the denominator. The CLI holds the existing Java-compatible world lock, refuses
to overwrite output and writes its result only after complete validation. Custom
dimensions require an explicit dimension-to-`[min_y, build_height]` geometry JSON
through `--dimension-geometry`; geometry must come from verified dimension types.
The default CLI does not silently assign Overworld geometry to custom dimensions.

The reconstructed CLI was not an accepted evidence consumer; its old input and
`--full-chunks` interface is replaced. New interface, exercised by the fixture
CLI test (paths and bounds here are illustrative, not a real measurement run):

```sh
uv run --no-sync python -m tools.analyze_structure_density WORLD OUTPUT \
  --dimension minecraft:overworld --bounds MIN_X MAX_X MIN_Z MAX_Z
```

Validation:

```sh
uv run --no-sync pytest -q tests/item10 tests/item7/test_anvil_decoder.py tests/item7/test_world_region_dimensions.py
uv run --no-sync ruff check tools/analyze_structure_density.py src/mcpack_evidence/item7_anvil.py tests/item10
uv run --no-sync basedpyright src/mcpack_evidence/item7_anvil.py tests/item10
```

Result: 31 tests passed; focused lint and type checks pass. The new fixtures
cover original normalized-output equivalence, inline/external chunk payloads,
missing or inconsistent authoritative starts, incomplete/missing/wrong-dimension
coverage, the actual CLI output and overwrite refusal. Initial test package/import,
formatting and typing failures were corrected before this result. No Item 11
workflow was imported, executed or linted.

This produces registry-start census diagnostics, not the complete Item 10 result.
Canonical classification joins, nonregistry occurrences, spatial summaries,
new-world lifecycle and durable custody integration still remain. No real-world
density, gameplay observation or performance claim is inferred from the fixtures.
