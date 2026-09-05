# Aether piece processor callback binding

Extractor revision 13755ac enables verbose javap only for the shared Aether
piece class. The prior ordinary capture remains in aether-placement and lacks
the bootstrap target required to bind its processor consumer. This capture
resolves that specific omission; it does not change runtime behavior.
The disassembly and identities reproduced byte for byte:

```sh
uv run -m tools.inspect_item8_pool_elements --archive aether-1.21.1-1.5.10-neoforge.jar --class-name com/aetherteam/aether/world/structurepiece/AetherTemplateStructurePiece.class --output evidence/raw/item8/aether-piece-binding-r1
```

In addProcessors, the selected StructureProcessorList.list() is visited with
List.forEach. InvokeDynamic #4 binds its consumer to
StructurePlaceSettings.addProcessor, as shown by BootstrapMethods entry 4.
Together with the captured constructor, this binds the configured processor
list to the template placement settings. It resolves the missing callback
target noted in aether-placement/README.md, but does not establish successful
world placement or eliminate retained external modifications.

Scoped extractor Ruff and Basedpyright passed. No new tests or measurement
system were needed for this capture-format correction. Next: reuse this
binding during inventory reconciliation; inspect the inherited chest writer
and direct sentry/trap block behavior where they affect Bronze attribution.
