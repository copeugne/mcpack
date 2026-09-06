# Fabric api_lookup_api contribution paths

Captured with 231284d; independent repeat matched all source files exactly.
Manifest SHA-256: 7fdd492bfcaf9f4d3840f9c7d238f2a2db88d94979b29a84f4592ae3d5aae0c9.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-api-lookup-api-v1-1.6.71+c290471319.jar --class-name net/fabricmc/fabric/mixin/lookup/ServerWorldMixin.class --class-name org/sinytra/fabric/api_lookup_api/generated/GeneratedEntryPoint.class --output evidence/raw/item8/fabric-api_lookup_api-entry-r1
```

ServerWorldMixin stores weak cache references, invalidates caller caches and prunes expired references. The loader calls ApiLookupImpl.onInitialize, which remains to be inspected before module closure.

Complete module payload and mixin membership are checked separately. This
capture is not whole Fabric provider closure. Do not follow generic interface
helpers beyond a demonstrated content-contribution question.
