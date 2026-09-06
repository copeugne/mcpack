# BCLib generation entry delegates

Extractor commit: 9da60b337be1663acbc9abdf93866cc4c2633240.
Independent r1 reproduction matches all three disassemblies and the identity
manifest byte for byte. Manifest SHA-256:
6e3641e3a2aa875328b5db7a2af8374c61e8e3f15075ca6e71fa95c8d3c90365

```sh
uv run -m tools.inspect_item8_pool_elements --archive bclib-21.0.24.jar --class-name org/betterx/bclib/api/v2/levelgen/LevelGenEvents.class --class-name org/betterx/bclib/api/v2/levelgen/structures/TemplatePiece.class --class-name org/betterx/bclib/BCLibPatch.class --output evidence/raw/item8/bclib-generation-entry-r1
```

LevelGenEvents subscribes world lifecycle callbacks for data exchange and data
fixing. Its initializeWorldConfig method is empty; beforeWorldLoad invokes
setupWorld. BCLibPatch registers a data-fixer patch supplier.

TemplatePiece registers a STRUCTURE_PIECE type. Its constructors accept the
caller's template resource location or saved piece NBT. postProcess delegates
template placement to TemplateStructurePiece and optionally erodes or covers
the supplied piece bounds. These are real block modifications by a consumer
piece, not an independently enumerated family or evidence of no world effects.

This capture resolves these three direct entry delegates only. BCLib's complete
provider disposition remains open. Reuse bclib-integration-dispatch for the
previously captured main entry and integration dispatch.
