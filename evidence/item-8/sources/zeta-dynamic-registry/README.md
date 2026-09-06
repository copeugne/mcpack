# Zeta dynamic registration source

Extractor bad6b54 captures one class. Independent r1 output matches
every generated file byte for byte.
Manifest SHA-256: a36377227dbb20649ef7b39f6f08c2c59afbbdf793117946a94251c2f867b77f.

```sh
uv run -m tools.inspect_item8_pool_elements --archive Zeta-1.1-40.jar --class-name org/violetmoon/zeta/registry/ZetaRegistry.class --output evidence/raw/item8/zeta-dynamic-registry-r1
```

RegisterDynamicUtil dispatches registry-load notifications to signed-up Zeta
instances. ZetaRegistry.performDynamicRegistration selects the queued entries
for the supplied registry key and returns if absent or empty. It evaluates each
consumer-supplied creator, registers its result with the supplied resource key
and binds an optional late-bound holder. The registerDynamic/registerDynamicF
methods queue supplied objects or creators; this is dispatch, not an authored
structure definition. The companion source is in zeta-dynamic-registration.

This resolves the callback exposed by RegistryDataLoaderMixin. Full provider
payload checking and disposition remain separate; no runtime claim is made.
