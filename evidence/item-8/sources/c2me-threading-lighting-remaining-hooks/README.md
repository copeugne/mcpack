# C2ME declared hooks: c2me-threading-lighting-remaining-hooks

Extractor 5347ff21fd07a10e07ed7fc4c6057342100cf211. Independent r1 reproduction
matches every disassembly and identity manifest. Manifest SHA-256:
de5ef5961614f6755b216a9a2fa94993fc10a7b146208453598dc1842a9970c0

```sh
uv run -m tools.inspect_item8_pool_elements --archive c2me-neoforge-mc1.21.1-0.3.0+alpha.0.93.jar --nested-archive META-INF/jars/c2me-threading-lighting-mc1.21.1-0.3.0+alpha.0.93.jar --class-name com/ishland/c2me/threading/lighting/mixin/MixinServerLightingProvider.class --class-name com/ishland/c2me/threading/lighting/mixin/MixinThreadedAnvilChunkStorage.class --class-name com/ishland/c2me/threading/lighting/mixin/scalablelux/MixinSchedulingUtil.class --output evidence/raw/item8/c2me-threading-lighting-remaining-hooks-r1
```

This retains the remaining declared common/server hooks in this module.
Previously captured hooks are reused. The null scheduling declaration has
no class target and is preserved as packaged, not replaced or counted.
The raw disassemblies are isolated generated evidence for membership review;
this capture alone is not whole-provider closure or operational validation.

Hooks schedule light updates, select lighting execution and close its executor. They operate on existing chunk light data.

This identifies membership roles. It does not prove runtime activation,
unchanged world generation, persistence safety or concurrency correctness.
Do not turn this into a generic scheduler, I/O or network implementation audit.
