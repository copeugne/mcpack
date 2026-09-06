# C2ME terrain computation: c2me-opts-dfc-terrain

Extractor f5d6ecb59c7bcf07f7ce09ecfa19861610cb4f20. Independent r1 reproduction
matches every disassembly and identity manifest. Manifest SHA-256:
346ca11293ec270e17688984850b6dc463b4db59db97ef9a841507d1c824ddef

```sh
uv run -m tools.inspect_item8_pool_elements --archive c2me-neoforge-mc1.21.1-0.3.0+alpha.0.93.jar --nested-archive META-INF/jars/c2me-opts-dfc-mc1.21.1-0.3.0+alpha.0.93.jar --class-name com/ishland/c2me/opts/dfc/mixin/MixinChunkNoiseSampler.class --class-name com/ishland/c2me/opts/dfc/mixin/MixinChunkNoiseSampler1.class --class-name com/ishland/c2me/opts/dfc/mixin/MixinChunkNoiseSamplerCache2D.class --class-name com/ishland/c2me/opts/dfc/mixin/MixinChunkNoiseSamplerCacheOnce.class --class-name com/ishland/c2me/opts/dfc/mixin/MixinChunkNoiseSamplerCellCache.class --class-name com/ishland/c2me/opts/dfc/mixin/MixinChunkNoiseSamplerDensityInterpolator.class --class-name com/ishland/c2me/opts/dfc/mixin/MixinChunkNoiseSamplerFlatCache.class --class-name com/ishland/c2me/opts/dfc/mixin/MixinDFTBinaryOperation.class --class-name com/ishland/c2me/opts/dfc/mixin/MixinDFTWrapping.class --class-name com/ishland/c2me/opts/dfc/mixin/MixinNoiseConfig.class --class-name com/ishland/c2me/opts/dfc/mixin/MixinSplineImplementation.class --output evidence/raw/item8/c2me-opts-dfc-terrain-r1
```

Every common hook declared by this module is captured here. This is membership
evidence, not a claim of numerical equivalence or whole-provider closure.

The hooks expose coordinate arrays, cache density values, wrap density-function
visitors and equality, and replace spline evaluation. MixinNoiseConfig passes
existing NoiseRouter and Climate.Sampler functions through BytecodeGen.compile
and rebuilds those containers. These are terrain computation paths, not
structure registration or authored templates. Numerical equivalence and the
compiler implementation are outside this family-membership claim.
