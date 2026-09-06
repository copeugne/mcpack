# BetterEnd configured cave carvers

Selector a156d8e captures EndCarvers and its seven carver-package classes.
The complete capture reproduces exactly against independent r1 output.
Manifest SHA-256: 7b8c98b8426309d3b5b6457d99af0a6a4273a16aabf23914bc418360c27223ba.

```sh
uv run -m tools.inspect_item8_pool_elements --archive BetterEnd-21.0.31.jar --class-name org/betterx/betterend/registry/EndCarvers.class --class-name 'org/betterx/betterend/world/carvers/CaveSurfaceCoater$ColumnResolver.class' --class-name org/betterx/betterend/world/carvers/CaveSurfaceCoater.class --class-name org/betterx/betterend/world/carvers/EndCaveCarver.class --class-name org/betterx/betterend/world/carvers/EndCaveCarverConfiguration.class --class-name 'org/betterx/betterend/world/carvers/EndTunnelCarver$Noises3.class' --class-name org/betterx/betterend/world/carvers/EndTunnelCarver.class --class-name org/betterx/betterend/world/carvers/EndTunnelCarverConfiguration.class --output evidence/raw/item8/betterend-configured-carvers-r1
```

The packaged configured carvers round_cave and tunnel_cave bind end_round_cave
and end_tunnel_cave. Both replace eligible terrain with cave air, maintain the
carving mask and delegate surface coating to CaveSurfaceCoater. The coater
uses cave-biome floor/ceiling/wall material states. This is cave terrain, not
an additional authored structure or encounter family. These configured-carver
entries are distinct from the previously captured cave features. Preserve
their separation rather than double-counting the shared cave terminology.

No cave-density measurement, geometry redesign or baseline repair is involved.
