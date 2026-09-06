# C2ME declared hooks: c2me-client-uncapvd-remaining-hooks

Extractor 5347ff21fd07a10e07ed7fc4c6057342100cf211. Independent r1 reproduction
matches every disassembly and identity manifest. Manifest SHA-256:
d8e2f43b60052ce1087d46d0371fe0e51e067eca82ac4c709652455c938ef00e

```sh
uv run -m tools.inspect_item8_pool_elements --archive c2me-neoforge-mc1.21.1-0.3.0+alpha.0.93.jar --nested-archive META-INF/jars/c2me-client-uncapvd-mc1.21.1-0.3.0+alpha.0.93.jar --class-name com/ishland/c2me/client/uncapvd/mixin/ISimpleOption.class --class-name com/ishland/c2me/client/uncapvd/mixin/MixinGameOptions.class --class-name com/ishland/c2me/client/uncapvd/mixin/MixinSodiumUserConfigCategories.class --class-name com/ishland/c2me/client/uncapvd/mixin/MixinSyncedClientOptions.class --class-name com/ishland/c2me/client/uncapvd/mixin/MixinVKModOptions.class --output evidence/raw/item8/c2me-client-uncapvd-remaining-hooks-r1
```

This retains the remaining declared common/server hooks in this module.
Previously captured hooks are reused. The null scheduling declaration has
no class target and is preserved as packaged, not replaced or counted.
The raw disassemblies are isolated generated evidence for membership review;
this capture alone is not whole-provider closure or operational validation.

Hooks change view-distance options, client settings and optional renderer option limits. They do not generate authored content.

This identifies membership roles. It does not prove runtime activation,
unchanged world generation, persistence safety or concurrency correctness.
Do not turn this into a generic scheduler, I/O or network implementation audit.
