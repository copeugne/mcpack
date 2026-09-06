# C2ME generation hooks: c2me-opts-worldgen-vanilla-generation

Extractor 736d66fa99506e243106ed8b93d63410546b5417. Independent r1 reproduction
matches every disassembly and identity manifest. Manifest SHA-256:
8ae72a4fe02ed2361ccd123d3e51618b208bbe33b16fd6b0aa34312cd96c9acc

```sh
uv run -m tools.inspect_item8_pool_elements --archive c2me-neoforge-mc1.21.1-0.3.0+alpha.0.93.jar --nested-archive META-INF/jars/c2me-opts-worldgen-vanilla-mc1.21.1-0.3.0+alpha.0.93.jar --class-name com/ishland/c2me/opts/worldgen/vanilla/mixin/aquifer/MixinAquiferSamplerImpl.class --class-name com/ishland/c2me/opts/worldgen/vanilla/mixin/structure_weight_sampler/MixinStructureWeightSampler.class --class-name com/ishland/c2me/opts/worldgen/vanilla/mixin/the_end_biome_cache/MixinTheEndBiomeSource.class --class-name com/ishland/c2me/opts/worldgen/vanilla/mixin/tlcache/MixinBlock.class --output evidence/raw/item8/c2me-opts-worldgen-vanilla-generation-r1
```

This capture retains the pool/generation boundary for membership inspection.
It does not establish whole-provider closure or unchanged generation outcomes.

These hooks compute aquifer fluid/block state, structure terrain-density contribution, cached End biome selection and cached full-block shape checks. Existing bounding boxes and jigsaw junctions are inputs to the terrain sampler, not new family definitions. No authored family is added by these hooks.
