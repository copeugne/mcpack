# Amendments block replacement boundaries

Extractor 1332fac7479f3e6301221bdc097dfb01678d30dc. Independent r1 reproduction
matches all four disassemblies and the identity manifest. Manifest SHA-256:
fd304f7b1fe85d565256a827dadd1566f1b83e93d6c84a69c22d312e7c575f50

```sh
uv run -m tools.inspect_item8_pool_elements --archive amendments-1.21-2.0.15-neoforge.jar --class-name net/mehvahdjukaar/amendments/common/block/StructureCauldronHack.class --class-name net/mehvahdjukaar/amendments/integration/SuppCompat.class --class-name 'net/mehvahdjukaar/amendments/integration/neoforge/BlueprintIntegration$BlockStateRepaletter.class' --class-name net/mehvahdjukaar/amendments/reg/ModRegistry.class --output evidence/raw/item8/amendments-block-replacement-r1
```

ModRegistry registers blocks, items, block entities and entity types. Additional
placements extend item/block placement variants such as ceiling banners.
SuppCompat.setup registers faucet interactions. These are existing-block and
player-operation paths, not independent generated structure definitions.

BlueprintIntegration.BlockStateRepaletter checks the supplied original block
and random chance, returning the configured replacement state on a match.
StructureCauldronHack registers the cauldron block and block entity used by that
replacement. The three packaged Blueprint definitions target existing structure
tags, including villages. Retain them as content modifiers, not new families.
This does not by itself establish which replacements were active or observed
in the frozen worlds, or their eventual fluid contents.

No generic block-entity, interaction or rendering implementation expansion is
needed for family membership. Use these captures with the parent payload and
entry/hook evidence for the provider disposition.
