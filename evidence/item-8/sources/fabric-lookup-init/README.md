# Fabric lookup initializer

Captured with 2043743 and independently reproduced exactly. Manifest SHA-256:
feb6c7996b8b362e2aacc07549301ad0e44c23c02b6e9a4a79ee5f1f08b904be.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-api-lookup-api-v1-1.6.71+c290471319.jar --class-name net/fabricmc/fabric/impl/lookup/ApiLookupImpl.class --output evidence/raw/item8/fabric-lookup-init-r1
```

The initializer registers one SERVER_STARTED callback. Its preserved bootstrap
method handle targets EntityApiLookupImpl.checkSelfImplementingTypes. That
callback remains the concrete unresolved lookup-module contribution boundary.
The initializer itself registers no content. Do not infer whole-module closure
from the callback name. Reuse this capture and inspect that target next.
