# Underground per-position context

Captured at extractor revision ae7e1b7. identities.json binds the exact retained
archive, class and disassembly. Capture and identity reproduced byte for byte
before this README was added:

```sh
uv run -m tools.inspect_item8_pool_elements --archive Quark-4.1-480.jar --class-name 'org/violetmoon/quark/content/world/undergroundstyle/base/UndergroundStyleGenerator$Context.class' --output evidence/raw/item8/quark-underground-context-ae7e1b7
```

The context stores world, source position, chunk generator, random and style
configuration. canPlaceAt requires WORLD_SURFACE_WG height strictly greater
than the candidate Y. consume delegates directly to info.style.fill(context,
position). There are no direct world writes or authored entity/loot operations
in this context. This identifies the per-position consumer but does not resolve
what UndergroundStyle.fill does to the supplied terrain.

The earlier outer-generator and BasicUndergroundStyle captures remain valid.
The next direct implementation to inspect is UndergroundStyle.fill, inherited
by both CorundumStyle and PermafrostStyle. Do not repeat context or source
selection inspection. Family inclusion remains unresolved until the fill
dispatcher is understood. Scoped extractor checks passed; no new measurement
system or server run was added.
