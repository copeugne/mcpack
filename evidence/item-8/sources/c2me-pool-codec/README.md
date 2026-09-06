# C2ME pool codec wrapper

Extractor 8a44c95236fded277b1b712abaaf1f16c7359c99. Independent r1 reproduction
matches the disassembly and identity manifest. Manifest SHA-256:
e5b186ca6272b7a3e105cafc86c6cb96b348e0bef03d18435b11531895848430

```sh
uv run -m tools.inspect_item8_pool_elements --archive c2me-neoforge-mc1.21.1-0.3.0+alpha.0.93.jar --nested-archive META-INF/jars/c2me-fixes-chunkio-threading-issues-mc1.21.1-0.3.0+alpha.0.93.jar --class-name com/ishland/c2me/fixes/chunkio/threading_issues/common/SynchronizedCodec.class --output evidence/raw/item8/c2me-pool-codec-r1
```

SynchronizedCodec retains the supplied codec as its delegate. Both encode and
decode take an interruptible lock, invoke the delegate with unchanged arguments,
and unlock when held. InterruptedException becomes RuntimeException. The
caller wraps the existing StructurePoolElement.CODEC; this defines no new pool,
pool-element type or authored family. No further generic serialization audit
is needed for this membership boundary.
