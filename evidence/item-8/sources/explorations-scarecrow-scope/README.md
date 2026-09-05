# Explorations scarecrow scope

Captured with f92c2d3 and reproduced byte for byte. Manifest SHA-256:
10fef0e01f61350f80a293996510e87642d07ada473ecbc81882236a2b7d3b43.

```sh
uv run -m tools.inspect_item8_pool_elements --archive explorations-neoforge-1.21.1-1.6.2.jar --class-name com/tristankechlo/explorations/worldgen/features/ScarecrowFeature.class --output evidence/raw/item8/explorations-scarecrow-scope-r1
```

ScarecrowFeature writes a five-position figure: legs at the origin, body above,
head two blocks above and two arms beside the body. Head/body/legs/arm states
come from configuration. Horizontal facing and material choices do not create
different structure families. The write results are ignored; the code returning
true does not prove every block was placed.

The packaged catalog contains nine named material configurations of type
explorations:scarecrow (acacia, bamboo, birch, cherry, dark_oak, jungle, mangrove,
oak and spruce). The unsuffixed scarecrow configured feature instead uses
minecraft:simple_random_selector. All ten names occur in the preserved live
configured-feature registry. This is one scarecrow design candidate, not ten
families. Complete registration, selector and placement/biome relationships
before final acceptance; no further arm/head helper tracing is needed for the
family boundary. No new world measurement.
