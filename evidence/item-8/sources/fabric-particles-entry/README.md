# Fabric particles entry roles

Captured with e2ae798. Independent repeat matched all source files exactly.
Manifest SHA-256: a0b59940d7e1991761a4f4ceb66df00b00b2b16907e6215dedbb52be62f11ab8.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-particles-v1-4.0.2+824f924c19.jar --class-name net/fabricmc/fabric/impl/client/particle/ClientParticleEventHooks.class --class-name org/sinytra/fabric/particles/generated/GeneratedEntryPoint.class --output evidence/raw/item8/fabric-particles-entry-r1
```

The generated loader is empty. ClientParticleEventHooks handles RegisterParticleProvidersEvent by initializing the client particle factory registry with the Minecraft particle engine.

Full payload and declared-hook coverage are verified separately by the existing
Fabric provider check. No further client-helper tracing is required for these
entry contribution roles. This capture alone is not whole-provider closure.
