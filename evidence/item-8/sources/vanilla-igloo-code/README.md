# Vanilla igloo source inspection

The existing extractor, extended in `3a174ef`, preserves three generation
classes from the frozen mapped-server archive. Manifest SHA-256:
`5104752aa5eb795053f75e8d62731b7ea7d79af1f9cacfdccfe2e55f9336838e`.
Archive SHA-256:
`26ca9c40d7e1681190b428583c38816852218e78df3f8bdb60a59a78503aec71`.

```sh
uv run -m tools.inspect_item8_pool_elements --archive server-1.21.1-20240808.144430-srg.jar --class-name net/minecraft/world/level/levelgen/structure/structures/IglooStructure.class --class-name net/minecraft/world/level/levelgen/structure/structures/IglooPieces.class --class-name 'net/minecraft/world/level/levelgen/structure/structures/IglooPieces$IglooPiece.class' --output evidence/item-8/sources/vanilla-igloo-code
uv run ruff check tools/inspect_item8_pool_elements.py
uv run basedpyright tools/inspect_item8_pool_elements.py
```

Extraction and scoped checks passed. Reproduce into a fresh output directory.
The identities manifest binds the archive, class members and disassembly files.
This is source evidence, not a generated-world observation.

## Generation and placement

`IglooStructure.generatePieces` selects a rotation and calls `IglooPieces.addPieces`.
The latter always adds `minecraft:igloo/top`. When nextDouble is less than 0.5,
it also adds `minecraft:igloo/bottom` and repeated `minecraft:igloo/middle`
components. With n = nextInt(8) + 4, the bottom constructor receives depth 3n;
middle constructors receive depths 3i for 0 <= i < n - 1. Thus n ranges from
4 through 11 and there are 3 through 10 middle components. These are code
selection rules, not measured world frequencies. They describe one family
with an optional basement, not three independent families.

`makePosition` adds the component offset and subtracts the supplied depth.
Offsets are top (0, 0, 0), middle (2, -3, 4), bottom (0, -3, -2).
Rotation pivots are top (3, 5, 5), middle (1, 3, 1), bottom (3, 6, 7).
Settings use no mirror, ignore structure blocks and ignore waterlogging.
`postProcess` samples WORLD_SURFACE_WG at the transformed reference position,
then shifts the template by sampled height minus 91 before calling the base
template placement. The initial construction Y of 90 is not final placement Y.
For the top piece, it replaces the transformed (3, 0, 5) block with snow when
the block below is neither air nor ladder. It restores the stored template
position after processing.

## Chest marker

`handleDataMarker` handles exactly `chest`: it clears the marker to air, looks
at the block entity below, and assigns IGLOO_CHEST with a random seed if that
entity is a ChestBlockEntity. Existing BuiltInLootTables evidence under
`../vanilla-end-city-code` maps this constant to `minecraft:chests/igloo_chest`.
That manifest SHA-256 is
`ca7cb2c777ad0fc638e28cded50a78ab048ca26ad243eeb564fa72be7cac943c`.
The marker handler does not create mobs. This does not establish absence of
authored entities in templates.

## Remaining integration

Reconcile these three references with the existing frozen template catalog,
including its entities and block entities, before updating the igloo family.
The inventory and decisions are unchanged at this source milestone. Effective
retained-mod transformations and final Item 8 closure remain open. No new
measurement system was introduced or required for these source facts.
