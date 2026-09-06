# CristelLib built-in consumer

Extractor 09afdba5. Independent r2 reproduction matches source and manifest
bytes. Manifest SHA-256:
e1a8ad79183b283beab90e8a4c6571a84f3dc7d128ea8262ecf0e6f5db2220f3

```sh
uv run -m tools.inspect_item8_pool_elements --archive cristellib-neoforge-1.21.1-3.1.7.jar --class-name de/cristelknight/cristellib/api/BuiltInAPI.class --output evidence/raw/item8/cristellib-builtin-r2
```

The annotated built-in API registers vanilla structure-set configuration and
the CONFIG_PACK with a true condition. It does not register a new structure
design. The earlier pre-selector capture and r1 remain in evidence/raw/item8;
they ran before selector delivery when an unrelated raw trailing-blank-line
check stopped a command chain. Accepted capture/r2 were run after delivery.
The raw ConditionNode trailing blank line was preserved, not edited to pass.
