# WorldWeaver bootstrap boundaries

Extractor 2010250228ade981058af66e92800cc43c9d6133. Independent r1 reproduction
matches all six disassemblies and the identity manifest. Manifest SHA-256:
901508185dd2583e0a22de2eb10e017b8a241ba262781803c158d43a0fa5e1be

```sh
uv run -m tools.inspect_item8_pool_elements --archive worldweaver-21.0.24.jar --class-name org/betterx/wover/core/api/ModCore.class --class-name org/betterx/wover/feature/impl/configured/FeatureConfiguratorImpl.class --class-name org/betterx/wover/feature/impl/placed/PlacedFeatureManagerImpl.class --class-name org/betterx/wover/structure/impl/pools/StructurePoolManagerImpl.class --class-name org/betterx/wover/structure/impl/sets/StructureSetManagerImpl.class --class-name org/betterx/wover/surface/impl/SurfaceRuleRegistryImpl.class --output evidence/raw/item8/wover-bootstrap-boundaries-r1
```

The configured-feature, placed-feature, template-pool and structure-set
managers register bootstrap callbacks that emit their consumer events. The
surface registry likewise emits consumer bootstrap and installs the surface
injection callback before levels are created. These are shared registration
and terrain paths, not default independent family definitions.

ModCore starts its providedDatapacks list empty. Its AddPackFinders listener
iterates supplied entries for SERVER_DATA and resolves each pack root from the
owning mod. It logs and skips missing pack.mcmeta or invalid metadata; retain
those failure paths, not a claim that every requested pack loaded. No generic
pack-loading audit is needed to inventory this archive's contribution.

These captures preserve method handles as well as direct bodies. Together with
the retained entries, registration targets, common hooks and packaged/runtime
catalogs, they support the provider membership disposition. The final provider
record must bind this source set and preserve terrain/consumer effects.
