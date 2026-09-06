# Fabric lookup entity validation callback

Captured with 65b700e. Independent repeat matched disassembly and manifest.
Manifest SHA-256: fea7a06fabe1eea4364d75c4cbc4c7d272033a5af585f44296fa5d1aeebfbd60.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-api-lookup-api-v1-1.6.71+c290471319.jar --class-name net/fabricmc/fabric/impl/lookup/entity/EntityApiLookupImpl.class --output evidence/raw/item8/fabric-lookup-entity-check-r1
```

The startup callback runs its check once, over REGISTERED_SELVES. That map starts
empty; registerSelf adds caller-supplied EntityType values under the requested
API class and registers the corresponding lookup provider. The callback calls
EntityType.create with the server Overworld, then checks Class.isInstance.
It throws NullPointerException if creation returns null and IllegalArgumentException
if the instance does not implement the requested API class. It neither adds the
instance to the world nor registers a generation route. Entity construction is
not evidence of a spawned encounter. Consumer entity types remain attributable
to their own providers; no general constructor audit is needed for this boundary.

The static initializer creates logging, lookup storage and the empty map. Together
with the preserved empty-content payload and cache/entry captures, this resolves
lookup as API infrastructure with no independent structure family. Full Fabric
provider coverage and family attributes remain separate work.
