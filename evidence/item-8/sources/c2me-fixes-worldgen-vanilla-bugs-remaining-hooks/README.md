# C2ME declared hooks: c2me-fixes-worldgen-vanilla-bugs-remaining-hooks

Extractor 5347ff21fd07a10e07ed7fc4c6057342100cf211. Independent r1 reproduction
matches every disassembly and identity manifest. Manifest SHA-256:
0e25e1612cf79d84c4ece787de3b612f6b3e062c8fbf22b9b936174e0b54cc9c

```sh
uv run -m tools.inspect_item8_pool_elements --archive c2me-neoforge-mc1.21.1-0.3.0+alpha.0.93.jar --nested-archive META-INF/jars/c2me-fixes-worldgen-vanilla-bugs-mc1.21.1-0.3.0+alpha.0.93.jar --class-name com/ishland/c2me/fixes/worldgen/vanilla_bugs/mixin/ensure_chunk_status_before_callback/MixinChunkHolder.class --output evidence/raw/item8/c2me-fixes-worldgen-vanilla-bugs-remaining-hooks-r1
```

This retains the remaining declared common/server hooks in this module.
Previously captured hooks are reused. The null scheduling declaration has
no class target and is preserved as packaged, not replaced or counted.
The raw disassemblies are isolated generated evidence for membership review;
this capture alone is not whole-provider closure or operational validation.

The hook gates existing chunk futures/callbacks by reached chunk status. It does not add content.

This identifies membership roles. It does not prove runtime activation,
unchanged world generation, persistence safety or concurrency correctness.
Do not turn this into a generic scheduler, I/O or network implementation audit.
