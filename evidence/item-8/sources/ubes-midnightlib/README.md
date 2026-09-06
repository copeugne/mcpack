# Ubes Delight bundled MidnightLib entries

Extractor cc4b5277d85391748ae64ad52ab24fa2980e9caa. Manifest SHA-256:
41ab47040644ab1dfc3ec5b67c1ccb679960c8df1fde22fa992b70a85cb293cc.
Independent r1 matches every generated file.

Retains all three annotated entry classes in the exact bundled library. They
initialize configuration/client presentation and register configuration screens
and commands. The command-builder and configuration delegates still require
their direct role check before full provider acceptance.

```sh
uv run -m tools.inspect_item8_pool_elements --archive ubesdelight-neoforge-1.21.1-0.4.13.jar --nested-archive META-INF/jars/midnightlib-1.9.2+1.21.1-neoforge.jar --class-name eu/midnightdust/core/MidnightLib.class --class-name 'eu/midnightdust/core/MidnightLib$MidnightLibBusEvents.class' --class-name 'eu/midnightdust/core/MidnightLib$MidnightLibEvents.class' --output evidence/raw/item8/ubes-midnightlib-r1
```
