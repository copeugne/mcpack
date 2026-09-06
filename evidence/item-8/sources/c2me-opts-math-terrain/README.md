# C2ME terrain computation: c2me-opts-math-terrain

Extractor f5d6ecb59c7bcf07f7ce09ecfa19861610cb4f20. Independent r1 reproduction
matches every disassembly and identity manifest. Manifest SHA-256:
3ed57063924de3f102c06c28d45bc83c6835514eb6ea6dedc5aa98a2d36c0177

```sh
uv run -m tools.inspect_item8_pool_elements --archive c2me-neoforge-mc1.21.1-0.3.0+alpha.0.93.jar --nested-archive META-INF/jars/c2me-opts-math-mc1.21.1-0.3.0+alpha.0.93.jar --class-name com/ishland/c2me/opts/math/mixin/MixinChunkNoiseSampler.class --class-name com/ishland/c2me/opts/math/mixin/MixinChunkPos.class --class-name com/ishland/c2me/opts/math/mixin/MixinOctavePerlinNoiseSampler.class --class-name com/ishland/c2me/opts/math/mixin/MixinPerlinNoiseSampler.class --output evidence/raw/item8/c2me-opts-math-terrain-r1
```

Every common hook declared by this module is captured here. This is membership
evidence, not a claim of numerical equivalence or whole-provider closure.

The hooks iterate existing noise interpolators, compare chunk coordinates, and
compute octave/Perlin samples. They define no new family. Numerical equivalence
and performance remain outside this source-membership assessment.
