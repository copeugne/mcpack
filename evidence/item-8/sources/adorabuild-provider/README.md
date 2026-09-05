# AdoraBuild provider code

All seven packaged classes captured with extractor 6fcc20c and reproduced byte
for byte before adding this README. Identity manifest SHA-256:
446d2811b3bd46642a1ae419f030e7d78b24fa061eb12c8e37f2702b086f038d.
Archive SHA-256: 6f399680da36dbb95b9a0dbf8b600f173e650be4d6bc25f50fcac792dcce081e.

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive adorabuild-structures-2.11.0-neoforge-1.21.3.jar \
  --output evidence/raw/item8/adorabuild-provider-r1
```

AdorabuildStructuresMod registers end_jigsaw_structure, nether_jigsaw_structure
and overworld_jigsaw_structure in STRUCTURE_TYPE and attaches that registration
to the mod bus. Verbose bootstrap bindings associate each supplier with its
corresponding codec. ModRegistry forwards caller-supplied registrations to
DeferredRegister; RegistryEntries and RegistryEntry retain and return them.
There is no separate feature, event-based placement or authored root declaration.

Each custom generator uses its configured start pool and calls vanilla
JigsawPlacement.addPieces with configured aliases, padding and liquid settings.
The Overworld generator checks configured height limits when projecting to a
heightmap, including its special ocean-floor projection branch. The End generator
uses surface height plus sampled offset when projection is absent. The Nether
generator searches a base column for non-air below and air at the candidate and
two blocks above, then delegates assembly. These are placement differences for
existing roots, not independent families or extra hardcoded template designs.
Exact height behavior remains available here for later attribute attribution.

The separate provider check reconciles all packaged pools/templates against the
existing graph and runtime-root regression. Keep the basalt chambers reference
to missing minecraft:basalt_chambers/chambers unresolved as a component failure;
do not silently substitute a differently namespaced pool. Candidate coverage
does not certify successful generation or canonical grouping of all 106 roots.
