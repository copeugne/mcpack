# C2ME declared hooks: c2me-fixes-general-threading-issues-remaining-hooks

Extractor 5347ff21fd07a10e07ed7fc4c6057342100cf211. Independent r1 reproduction
matches every disassembly and identity manifest. Manifest SHA-256:
8aea25489ec0316addc4b4bb7360855a4c65580e99f8733c62d19f2632ea01da

```sh
uv run -m tools.inspect_item8_pool_elements --archive c2me-neoforge-mc1.21.1-0.3.0+alpha.0.93.jar --nested-archive META-INF/jars/c2me-fixes-general-threading-issues-mc1.21.1-0.3.0+alpha.0.93.jar --class-name com/ishland/c2me/fixes/general/threading_issues/mixin/MixinChunkTicketManager.class --class-name com/ishland/c2me/fixes/general/threading_issues/mixin/asynccatchers/MixinMinecraftServer.class --class-name com/ishland/c2me/fixes/general/threading_issues/mixin/asynccatchers/MixinServerChunkManager.class --class-name com/ishland/c2me/fixes/general/threading_issues/mixin/asynccatchers/MixinThreadedAnvilChunkStorage.class --output evidence/raw/item8/c2me-fixes-general-threading-issues-remaining-hooks-r1
```

This retains the remaining declared common/server hooks in this module.
Previously captured hooks are reused. The null scheduling declaration has
no class target and is preserved as packaged, not replaced or counted.
The raw disassemblies are isolated generated evidence for membership review;
this capture alone is not whole-provider closure or operational validation.

Hooks change ticket iteration and reject off-thread save, tick or entity load/unload calls. These are lifecycle/thread constraints, not authored generation.

This identifies membership roles. It does not prove runtime activation,
unchanged world generation, persistence safety or concurrency correctness.
Do not turn this into a generic scheduler, I/O or network implementation audit.
