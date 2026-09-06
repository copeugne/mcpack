# C2ME membership boundary: c2me-commands

Extractor 9c16bd6eee0944af76d0df4a8abd2b4d43a6d8d2. Independent r1 reproduction
matches every disassembly and identity manifest. Manifest SHA-256:
62384112742db067336aa8d060475a0cf7579e1892504b9b2990ff3b112fd066

```sh
uv run -m tools.inspect_item8_pool_elements --archive c2me-neoforge-mc1.21.1-0.3.0+alpha.0.93.jar --nested-archive META-INF/jars/c2me-server-utils-mc1.21.1-0.3.0+alpha.0.93.jar --class-name com/ishland/c2me/server/utils/common/C2MECommands.class --output evidence/raw/item8/c2me-commands-r1
```

The c2me/notick command reads and reports the pending no-tick chunk load count, with permission checks. It does not place or register content.
