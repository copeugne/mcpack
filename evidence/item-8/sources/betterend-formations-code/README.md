# BetterEnd formation generator sources

This uses the existing hash-verified Item 8 javap extractor to resolve the open
lake and mountain family relationships. Packaged structure definitions name
custom types but contain neither their implementation nor template paths.
Registration, the shared base class and the seven lake/mountain root classes are
the smallest direct source set for that relationship inspection. No new evidence
framework, runtime experiment or measurement system is introduced.

The retained BetterEnd archive is `BetterEnd-21.0.31.jar`, SHA-256
`dd883e2f91fa7ee8a0594dc3844de38bf3e550d91ff1247b2801808904fd013a`.
The nine-class identity manifest SHA-256 is
`150df9fc0a941cc523bca51a782c39fcd0f08a32b11af77a64cf6f248c170961`.
It records exact archive, class and disassembly hashes. EndStructures uses verbose
output to retain constructor method handles and bootstrap bindings. The existing
extractor removes its machine-local Classfile header path.

Reproduce to a fresh output directory using the frozen retained inputs:

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive BetterEnd-21.0.31.jar \
  --output evidence/raw/item8/betterend-formations-reproduction \
  --class-name org/betterx/betterend/registry/EndStructures.class \
  --class-name org/betterx/betterend/world/structures/features/FeatureBaseStructure.class \
  --class-name org/betterx/betterend/world/structures/features/EndLakeStructure.class \
  --class-name org/betterx/betterend/world/structures/features/EndLakeNormalStructure.class \
  --class-name org/betterx/betterend/world/structures/features/EndLakeRareStructure.class \
  --class-name org/betterx/betterend/world/structures/features/MegaLakeStructure.class \
  --class-name org/betterx/betterend/world/structures/features/MegaLakeSmallStructure.class \
  --class-name org/betterx/betterend/world/structures/features/MountainStructure.class \
  --class-name org/betterx/betterend/world/structures/features/PaintedMountainStructure.class
cmp evidence/item-8/sources/betterend-formations-code/identities.json evidence/raw/item8/betterend-formations-reproduction/identities.json
uv run ruff check tools/inspect_item8_pool_elements.py
uv run basedpyright tools/inspect_item8_pool_elements.py
```

Initial extraction used the same class selection and the committed source output
directory. It completed successfully; scoped Ruff and Basedpyright passed.

Initial inspection establishes that EndLakeNormalStructure and
EndLakeRareStructure extend EndLakeStructure and declare only a forwarding
constructor and type() override. This supports a shared generation implementation,
subject to the packaged settings and placement distinctions. MegaLakeSmallStructure
has its own generatePieces implementation; its name alone is not proof of
inheritance or identical geometry. Mountain and painted mountain likewise use
separate piece classes. Full family integration and required attribute assessment
remain pending. This source increment does not change the inventory count or
claim completion, effective generation or observed geometry.

The fresh reproduction command above was executed successfully. Its identity
manifest matched byte-for-byte, including all nine disassembly hashes. The
source increment is separate from later family decisions so those decisions can
be reviewed against already delivered evidence.
