# C2ME terrain computation: c2me-opts-natives-math-terrain

Extractor f5d6ecb59c7bcf07f7ce09ecfa19861610cb4f20. Independent r1 reproduction
matches every disassembly and identity manifest. Manifest SHA-256:
4b17968266655f2d9a94965231af29283add9e2838e23541a1331900c95271f4

```sh
uv run -m tools.inspect_item8_pool_elements --archive c2me-neoforge-mc1.21.1-0.3.0+alpha.0.93.jar --nested-archive META-INF/jars/c2me-opts-natives-math-mc1.21.1-0.3.0+alpha.0.93.jar --class-name com/ishland/c2me/opts/natives_math/mixin/MixinBiomeAccess.class --class-name com/ishland/c2me/opts/natives_math/mixin/MixinDFTypesEndIslands.class --class-name com/ishland/c2me/opts/natives_math/mixin/MixinDoublePerlinNoiseSampler.class --class-name com/ishland/c2me/opts/natives_math/mixin/MixinInterpolatedNoiseSampler.class --output evidence/raw/item8/c2me-opts-natives-math-terrain-r1
```

Every common hook declared by this module is captured here. This is membership
evidence, not a claim of numerical equivalence or whole-provider closure.

The hooks compute biome choice and End-island, double-Perlin and interpolated
noise values through native bindings or existing samplers. Inputs are existing
noise data and coordinates. No authored family is registered here. This records
packaged roles, not proof these optional hooks load under the frozen Java/runtime
or that native and Java numerical results agree. Do not benchmark them for
Item 8 membership.
