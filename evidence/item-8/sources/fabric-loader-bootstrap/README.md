# fabric-loader-bootstrap source checkpoint

Extractor be54e72. Independent r1 reproduction matches the manifest and every
disassembly byte. Manifest SHA-256: 2800b7f9a5f95e344a15a56a68fdf137c30184114f23b10e969d1c48344fb764.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/forgified-fabric-loader-2.5.68+0.18.4+1.21.1-full.jar --class-name net/fabricmc/loader/impl/bootstrap/FabricLoaderBootstrap.class --output evidence/raw/item8/fabric-loader-bootstrap-r1
```

Preserves the remaining startup boundary. Provider disposition remains separate.
