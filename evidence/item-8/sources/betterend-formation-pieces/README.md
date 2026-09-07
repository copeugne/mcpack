# BetterEnd formation piece sources

These six classes extend the existing Item 8 source extraction to the pieces
instantiated by the already preserved lake and mountain generators. Packaged
definitions and template traces do not expose their procedural geometry or
content. This source set supports the required footprint, vertical size and
content attributes without another runtime experiment or measurement system.

Retained archive: `BetterEnd-21.0.31.jar`, SHA-256
`dd883e2f91fa7ee8a0594dc3844de38bf3e550d91ff1247b2801808904fd013a`.
Identity manifest SHA-256:
`2ecc0877f072bee316254a4e5df4395c43e24802d923a29bd83c19c8a7718f39`.
The manifest binds each class and disassembly to that archive.

Reproduce with the frozen inputs into a fresh output directory:

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive BetterEnd-21.0.31.jar \
  --output evidence/raw/item8/betterend-formation-pieces-reproduction \
  --class-name org/betterx/betterend/world/structures/piece/BasePiece.class \
  --class-name org/betterx/betterend/world/structures/piece/EndLakePiece.class \
  --class-name org/betterx/betterend/world/structures/piece/LakePiece.class \
  --class-name org/betterx/betterend/world/structures/piece/MountainPiece.class \
  --class-name org/betterx/betterend/world/structures/piece/CrystalMountainPiece.class \
  --class-name org/betterx/betterend/world/structures/piece/PaintedMountainPiece.class
cmp evidence/item-8/sources/betterend-formation-pieces/identities.json evidence/raw/item8/betterend-formation-pieces-reproduction/identities.json
uv run ruff check tools/inspect_item8_pool_elements.py
uv run basedpyright tools/inspect_item8_pool_elements.py
```

Initial extraction and fresh reproduction succeeded. Their identity manifests
match byte-for-byte, including all six disassembly hashes. Scoped Ruff and
Basedpyright passed for the extractor change.

Initial inspection: MountainPiece stores separate radius and height parameters,
but makeBoundingBox uses radius for all three axes, including Y. Consequently,
the saved piece envelope must not be presented as measured occupied mountain
height. Content inspection and inventory attribute integration remain pending.
This capture does not establish absence of indirect content, final geometry,
observed discoverability, or Item 8 completion.

## Lake geometry and dimension assessment

This increment integrates eleven existing facts: dimension eligibility for all
nine BetterEnd families and the lake family's two size attributes. The effective
root biome sets in structure-inputs.json intersect only minecraft:the_end in the
captured dimension-r3/dimension-biomes.json. Eligibility is not generation success.
The lake family now has all required Item8 attributes; the other eight BetterEnd
families still need assessment. No new capture or measurement tool is needed.

The preserved world-bounds.json.gz contains three full-start lake observations:

| Root | Seed | Decoded source and line | Chunk | Saved size X,Y,Z |
| --- | --- | --- | --- | --- |
| end_lake_normal | 42 | run-a/ordinary/chunks.jsonl:6419 | 90,4 | 57,44,57 |
| end_lake_rare | -3503646078644842058 | run-a/biome-diverse/chunks.jsonl:7809 | 98,4 | 75,45,75 |
| end_lake_rare | -3503646078644842058 | run-b/biome-diverse/chunks.jsonl:7441 | 108,-10 | 77,46,77 |

These are three distinct observed starts, not repeated measurements of one
identical layout. Preserve their different positions and dimensions across runs.
The exact envelopes and identities are integrated in family-decisions.json.
Inclusive envelope subtraction is performed by the existing observed_bounds
implementation; the world-bounds artifact and underlying Item7 custody remain
the evidence source. No new runtime or archive is introduced.

EndLakePiece.makeBoundingBox uses floor(1.5 * radius), with ten blocks of additional
margin on each side horizontally. Its lower Y is waterLevel minus floor(depth)
minus twelve, and upper Y is centerY plus22. The saved vertical span consequently
includes support and clearance, not just water depth. These explicitly labelled
generation envelopes provide approximate examples for this procedural family;
they are not occupied volumes, typical dimensions, or all-variant maxima.
No full-start megalake example is present in this set. That limitation does not
turn variant sampling or a water-depth measurement into additional Item8 work.

The source inspection and exact class identities above explain the envelope's
meaning. The mountain family must retain its separate warning: MountainPiece
uses radius on Y, so a cubic saved box must not be described as occupied mountain
height. Its two size attributes remain open after this increment.
