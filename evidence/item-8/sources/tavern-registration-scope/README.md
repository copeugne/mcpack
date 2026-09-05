# Tavern configuration and block registration

Extractor revision 297edcb. Identity manifest SHA-256:
2c540f221c3bff4de00c0e671aec0832635db171c61ab08f6e54171600255fd3.
The three captures reproduce byte for byte before this README was added.

```sh
uv run -m tools.inspect_item8_pool_elements --archive village_taverns-neoforge-1.1.5+1.21.1.jar --class-name net/village_taverns/config/Defaults.class --class-name net/village_taverns/block/TavernBlocks.class --class-name 'net/village_taverns/block/TavernBlocks$Entry.class' --output evidence/raw/item8/tavern-registration-scope-r1
```

Defaults constructs five StructurePoolConfig entries. Each links
minecraft:village/V/houses to village_taverns:village/V/tavern for desert,
savanna, plains, taiga and snowy. Those are the same five component identities
already recorded for packaged Lithostitched additions. The constructor receives
integer arguments 10 and 1; do not replace the separately preserved packaged
Lithostitched weight with these fallback constructor arguments.

TavernBlocks constructs one BrewTapBlock and matching BlockItem under barrel.
register writes the block and item registries, then appends the item to the
functional-block creative tab. Entry is a record holding name, block and item.
These registration methods add no structure root or feature registration.

The remaining provider-scope check concerns full archive accounting, the
BrewTapBlock/client/compatibility classes where relevant to entry coverage, and
the bundled tiny-config library's actual entry behavior. The bundled library
metadata has an empty mixin list and no generation data, which alone is not proof
of no code contribution. No new generation measurement or trade analysis.
