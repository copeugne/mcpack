# Zeta dynamic registration source

Extractor 8e70500 captures one class. Independent r1 output matches
every generated file byte for byte.
Manifest SHA-256: 57fec3b7ea3952e0ece732fa29d13960a59ccfb7ace26c3daa4eb5a9d32c375c.

```sh
uv run -m tools.inspect_item8_pool_elements --archive Zeta-1.1-40.jar --class-name org/violetmoon/zeta/util/RegisterDynamicUtil.class --output evidence/raw/item8/zeta-dynamic-registration-r1
```

RegisterDynamicUtil dispatches registry-load notifications to signed-up Zeta
instances. ZetaRegistry.performDynamicRegistration selects the queued entries
for the supplied registry key and returns if absent or empty. It evaluates each
consumer-supplied creator, registers its result with the supplied resource key
and binds an optional late-bound holder. The registerDynamic/registerDynamicF
methods queue supplied objects or creators; this is dispatch, not an authored
structure definition. The companion source is in zeta-dynamic-registry.

This resolves the callback exposed by RegistryDataLoaderMixin. Full provider
payload checking and disposition remain separate; no runtime claim is made.
