# Spiral Spires configuration annotations

Verbose capture at `266b69f`, with exact identities in `identities.json`.
Reproduction matched byte for byte:

```sh
uv run -m tools.inspect_item8_pool_elements --archive Quark-4.1-480.jar --class-name org/violetmoon/quark/content/world/module/SpiralSpiresModule.class --output evidence/raw/item8/quark-spire-config-266b69f
```

The dimensions, biomes, rarity and radius static fields each carry the Zeta
Config annotation. The previous non-verbose module capture remains preserved
at `../quark-end-registration`; use its recorded extractor revision to reproduce
that earlier output. This additional capture is needed because ordinary javap
output omitted the annotations required to attribute configuration binding.
It does not replace the earlier generation interpretation or prove runtime
field values. Nested dimension/biome annotations and configuration-event
connection remain to be reconciled with `../zeta-config-binding`.
