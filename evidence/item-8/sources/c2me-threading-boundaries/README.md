# C2ME threading transformation boundaries

Extractor 7c153bbab1990dd912c030966b1bde4db6d76c6f. Independent r1 reproduction
matches all five disassemblies and the identity manifest. Manifest SHA-256:
d5fa087330c5a7c3f210efe1e2cb06debcff3447009f470a6cdcaa1b2b6c2174

```sh
uv run -m tools.inspect_item8_pool_elements --archive c2me-neoforge-mc1.21.1-0.3.0+alpha.0.93.jar --nested-archive META-INF/jars/c2me-fixes-worldgen-threading-issues-mc1.21.1-0.3.0+alpha.0.93.jar --class-name 'com/ishland/c2me/fixes/worldgen/threading_issues/MixinPlugin$1.class' --class-name com/ishland/c2me/fixes/worldgen/threading_issues/asm/ASMTransformerMakeVolatile.class --class-name com/ishland/c2me/fixes/worldgen/threading_issues/common/Config.class --class-name com/ishland/c2me/fixes/worldgen/threading_issues/common/ConcurrentFlagMatrix.class --class-name com/ishland/c2me/fixes/worldgen/threading_issues/common/CheckedThreadLocalRandom.class --output evidence/raw/item8/c2me-threading-boundaries-r1
```

The transformer adds the volatile access bit (64) to fields marked MakeVolatile.
Its plugin extension exports class debug mappings to SMAPPool. Config.init is
empty; class initialization reads fixes.enforceSafeWorldRandomAccess. The
mansion matrix wraps the existing SimpleGrid operations with read/write locks.
CheckedThreadLocalRandom checks thread ownership, logs or throws on invalid
access, and delegates random draws to existing random implementations. These
are changes to existing generation state and diagnostics, not new families.

This closes the named delegates from the worldgen-threading hook capture for
family membership. Do not pursue the debug mapping formatter, exception subclass
or generic config parser: their consumers here do not generate content. This
is not a concurrency correctness test or a claim that generated outcomes are
unchanged. Other C2ME modules and whole-provider coverage remain open.
