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
