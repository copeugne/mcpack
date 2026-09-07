# C2ME declared hooks: c2me-server-utils-remaining-hooks

Extractor 5347ff21fd07a10e07ed7fc4c6057342100cf211. Independent r1 reproduction
matches every disassembly and identity manifest. Manifest SHA-256:
070d2e2b0f803ce2cb834565638238629f7bf9e89573577c702f050f1698339b

```sh
uv run -m tools.inspect_item8_pool_elements --archive c2me-neoforge-mc1.21.1-0.3.0+alpha.0.93.jar --nested-archive META-INF/jars/c2me-server-utils-mc1.21.1-0.3.0+alpha.0.93.jar --class-name com/ishland/c2me/server/utils/mixin/MixinCommandManager.class --output evidence/raw/item8/c2me-server-utils-remaining-hooks-r1
```

This retains the remaining declared common/server hooks in this module.
Previously captured hooks are reused. The null scheduling declaration has
no class target and is preserved as packaged, not replaced or counted.
The raw disassemblies are isolated generated evidence for membership review;
this capture alone is not whole-provider closure or operational validation.

The command hook delegates registration to C2MECommands.register. That direct command boundary remains to inspect before closing this module.

This identifies membership roles. It does not prove runtime activation,
unchanged world generation, persistence safety or concurrency correctness.
Do not turn this into a generic scheduler, I/O or network implementation audit.
