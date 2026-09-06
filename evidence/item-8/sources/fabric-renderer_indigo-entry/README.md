# Fabric renderer_indigo entry roles

Captured with e2ae798. Independent repeat matched all source files exactly.
Manifest SHA-256: 6dfed069d59ffc725aec5a0e6e5cfb8df092bf0a7f17277fe217cf410fddbfe8.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-renderer-indigo-1.7.1+9125b6dc19.jar --class-name net/fabricmc/fabric/impl/client/indigo/IndigoMixinConfigPlugin.class --class-name org/sinytra/fabric/renderer_indigo/generated/GeneratedEntryPoint.class --output evidence/raw/item8/fabric-renderer_indigo-entry-r1
```

The generated loader guards Indigo initialization with isClient. The mixin plugin reads renderer-related mod properties, selects Indigo applicability and returns no additional mixin list. Its load/pre/post/target callbacks add no content.

Full payload and declared-hook coverage are verified separately by the existing
Fabric provider check. No further client-helper tracing is required for these
entry contribution roles. This capture alone is not whole-provider closure.
