# Fabric model_loading_api entry roles

Captured with e2ae798. Independent repeat matched all source files exactly.
Manifest SHA-256: 2cb25059a4bba8b4638ba8716fc2fec8cef40bb44bfc0cc54fd69eb88094755e.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-model-loading-api-v1-2.1.0+6e8f52c719.jar --class-name org/sinytra/fabric/model_loading_api/generated/GeneratedEntryPoint.class --output evidence/raw/item8/fabric-model_loading_api-entry-r1
```

The generated loader constructor calls Object and returns.

Full payload and declared-hook coverage are verified separately by the existing
Fabric provider check. No further client-helper tracing is required for these
entry contribution roles. This capture alone is not whole-provider closure.
