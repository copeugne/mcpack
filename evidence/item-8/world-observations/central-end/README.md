# Saved central-End block observations

Extractor revision: `aff899784806db11100e999d2514580adb51765b`.
Output: `blocks.json`, 154544 bytes, SHA-256
`10836fec936f904a0fedaf38304b7f0e4aabeb747433d8b176a861d346202730`.

This is an offline projection of the accepted Item 7 ordinary seed 42 run-a
world, limited to block X/Z -64 through 63 in the End. The extractor verifies
the pinned r14 run-a world manifest and each of the four input region files by
size and SHA-256. Input identities are included in the output. Raw worlds remain
under the existing Item 7 archive custody and restore records; no new world or
server run was used. This selection is not a representative exploration sample.

Reproduce from the repository root with the restored run-a archive and a fresh
output path:

```sh
uv run -m tools.extract_item8_end_blocks \
  --restored-run-a ../mcpack-item7-r14-delivery/restored-final/run-a \
  --output evidence/raw/item8/end-blocks-aff8997-reproduction.json
cmp evidence/item-8/world-observations/central-end/blocks.json \
  evidence/raw/item8/end-blocks-aff8997-reproduction.json
```

The committed-revision reproduction matched byte for byte. The earlier local
pilot `evidence/raw/item8/end-blocks-pilot.json` has identical input and chunk
records but a longer scope description. It is not the authoritative output.
Three focused tests passed, covering single-state sections, actual packed-state
use rather than unused palette entries, and malformed packed data. Scoped Ruff
and Basedpyright passed before the extractor commit.

Each chunk records saved generation status and data version, actual block-name
counts for each section, and block-entity types and coordinates. Block properties
are collapsed by name; individual block positions, ordinary entities and
inventories are not projected. The evidence therefore supports material presence
and block-entity observations within the selected chunks, not exact template
matching, occupied geometry, dragon state, family counts or world-wide absence.
In particular, do not treat obsidian or End Stone brickwork alone as proof of an
exact Better End Island variant, or infer podium generation from those materials.
