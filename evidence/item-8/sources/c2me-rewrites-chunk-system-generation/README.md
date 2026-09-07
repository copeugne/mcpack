# C2ME generation hooks: c2me-rewrites-chunk-system-generation

Extractor 736d66fa99506e243106ed8b93d63410546b5417. Independent r1 reproduction
matches every disassembly and identity manifest. Manifest SHA-256:
06affc64e374eaeb4af55381e46da04a7ca04ff394e9930785dcf861a525714d

```sh
uv run -m tools.inspect_item8_pool_elements --archive c2me-neoforge-mc1.21.1-0.3.0+alpha.0.93.jar --nested-archive META-INF/jars/c2me-rewrites-chunk-system-mc1.21.1-0.3.0+alpha.0.93.jar --class-name com/ishland/c2me/rewrites/chunksystem/mixin/MixinChunkGenerator.class --class-name com/ishland/c2me/rewrites/chunksystem/mixin/MixinNoiseChunkGenerator.class --output evidence/raw/item8/c2me-rewrites-chunk-system-generation-r1
```

This capture retains the pool/generation boundary for membership inspection.
It does not establish whole-provider closure or unchanged generation outcomes.

The ChunkGenerator and NoiseChunkGenerator hooks redirect the biome/noise executor. They neither define nor register structure content. Other chunk-system hooks remain separately open.
