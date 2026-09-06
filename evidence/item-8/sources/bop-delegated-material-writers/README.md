# BOP delegated material writers

Selector 6c3083c captures the shared tree writer and quartz material consumers.
All four generated files reproduce exactly against the independent r1 capture.
Manifest SHA-256: fbb0dcdc15d9fd3f38663af03a7db1d3f942b01f0f8c243cfb3ed032ec647080.

```sh
uv run -m tools.inspect_item8_pool_elements --archive BiomesOPlenty-neoforge-1.21.1-21.1.0.13.jar --class-name biomesoplenty/worldgen/feature/tree/BOPTreeFeature.class --class-name 'biomesoplenty/worldgen/feature/misc/LargeRoseQuartzFeature$LargeRoseQuartz.class' --class-name biomesoplenty/util/biome/RoseQuartzUtils.class --output evidence/raw/item8/bop-delegated-material-writers-r1
```

BOPTreeFeature supplies configured trunk, foliage, alternate foliage, vine,
hanging and fruit block states to its placement consumers. It checks replaceable
space and orients logs/vines. This binds the common material writer used by the
fourteen already captured tree implementations; it is not a new family.

The large-quartz inner writer places rose-quartz blocks and buds/clusters within
its geometric footprint. RoseQuartzUtils supplies material eligibility and
mineral-growth helpers. WindOffsetter supplies positions to the material writer;
there is no need to reconstruct its geometry to establish this mineral role.
These sources close the concrete delegated material questions. No unrelated
tree interaction, shape measurement or feature-balancing work is included.
