# BetterEnd lake helper sources

The existing lake pieces invoke EndBiome.findTopMaterial and, for EndLakePiece,
BlockFixer.fixBlocks. These calls leave material and post-carving block effects
outside the already preserved piece bodies. The existing extractor selects these
two exact helper classes to resolve that direct content-attribution gap. No new
measurement system, runtime experiment or general extraction framework is added.

Retained archive: `BetterEnd-21.0.31.jar`, SHA-256
`dd883e2f91fa7ee8a0594dc3844de38bf3e550d91ff1247b2801808904fd013a`.
Identity manifest SHA-256:
`80e48ad38d1350b83906950d68567f0d97909b1c062bea40ce50e2952a6f99c2`.
The manifest binds archive, class and disassembly identities.

Reproduction into a fresh output directory:

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive BetterEnd-21.0.31.jar \
  --output evidence/raw/item8/betterend-lake-helpers-reproduction \
  --class-name org/betterx/betterend/world/biome/EndBiome.class \
  --class-name org/betterx/betterend/util/BlockFixer.class
cmp evidence/item-8/sources/betterend-lake-helpers/identities.json evidence/raw/item8/betterend-lake-helpers-reproduction/identities.json
uv run ruff check tools/inspect_item8_pool_elements.py
uv run basedpyright tools/inspect_item8_pool_elements.py
```

Initial extraction used the same class selection and this source directory.
Fresh reproduction succeeded and the manifests match byte-for-byte, including
both disassembly hashes. Scoped Ruff and Basedpyright passed.

Initial inspection: EndBiome.findTopMaterial performs a surface-material-provider
lookup with a configured default; it does not itself enumerate every biome's
material. BlockFixer traverses a region and includes plant survival and chorus
cleanup paths, with AIR/WATER replacement states. Its complete branch effects
still need disposition before accepting the lake content claim. These helper
sources do not alone establish absent indirect mobs, spawners, loot, or complete
material identities. Existing family attributes and inventory remain unchanged.
