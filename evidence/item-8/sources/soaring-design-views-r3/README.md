# Soaring canonical design views

The existing template renderer at ef751a51 selects fixed Soaring templates from
MoogsSoaringStructures-1.21-2.1.2.jar through hash-verified retained_sources.
Five losslessly compressed SVG sheets contain 26 templates representing portions
of 24 provisional designs. Arena is deliberately excluded: its 21-piece assembly
requires the existing pool graph, not an assumed arena.nbt. The pyramid's side
and top are explicitly shown as pieces, not independent designs.

```sh
uv run -m tools.view_item8_betterend_ruins --soaring --output evidence/raw/item8/soaring-design-views-compressed-repro
```

Every compressed output matches this directory. Decompression also matches the
independently reproduced uncompressed r3 output. To inspect a sheet:

```sh
gzip -dc evidence/item-8/sources/soaring-design-views-r3/houses.svg.gz > evidence/raw/item8/soaring-houses.svg
convert evidence/raw/item8/soaring-houses.svg evidence/raw/item8/soaring-houses.png
```

Houses and towers were manually inspected. The other three sheets are preserved
comparison inputs, not yet accepted membership decisions. Drawn cells are cubes,
not actual partial block models. Cells occluded by occupied neighbors in all three
visible directions are omitted. Green hints at plant-related names; it is not a
classification. Diagrams rescale templates independently. They do not show hidden
interiors, complete modular assemblies, observed dimensions or world placement.
Use the existing packaged NBT summaries and complete pool traces alongside them.

Rejected pilots are preserved under evidence/raw/item8:
soaring-design-views-rejected-missing-arena stopped on the nonexistent arena.nbt;
soaring-design-views-rejected-unculled reproduced but its house sheet was 70 MB.
The unculled conversion was deliberately stopped after three minutes. A premature
conversion before file creation failed. Neither failed conversion is evidence.
The culling revision reduces hidden island geometry; default BetterEnd outputs
remain byte-identical. One missing set type annotation was fixed after type checking.
Scoped Ruff and Basedpyright pass. Compression avoids committing 47 MB of SVG text
without introducing another renderer or changing the underlying views.

Compressed SHA-256 identities:

- houses.svg.gz: becf720243fdafb2bae2b075fdb22ed5a44e02af1a47bfdee9df0f92335584f7
- islands.svg.gz: f31095e60af3bff22c0b260fe68ab2cda1685556372a19e0152fe8ab7b3b3e53
- landscapes.svg.gz: 9d822d81b30aea19622f15bd71b7ffb911a280e912f4be9a05ef83ea518ecc06
- monuments.svg.gz: 101b3442c545a5dfcbe18e9c7844aff90f60068057eec926f71a014559e96e37
- towers.svg.gz: da9fdd6a124f8653f104fb9007367dfeb14910450ba89de65928a2b6df6ae054
