# Packaged JSON source catalog

This is source evidence, not a canonical family inventory or an Item 8 gate pass.
The extractor scans every hash-verified retained candidate plus the pinned
Minecraft and NeoForge archives. Nested JARs and optional data-pack paths remain
explicit. Their presence does not prove runtime activation or resource priority.
All packaged data JSON is retained so nonstandard provider injection resources
remain inspectable. Recipes and other unrelated resources are not families.

Extraction implementation: `d042ed172e7750d13efa4b2302b45ced37281247`.
Redaction implementation: `bdeb98a9fcda86466fb32e3174e678c43ae221b8`.
Output: `packaged-json-redacted.json.gz`.
SHA-256: `a5279d453f32edf7b1adc5c06b09953785b990b4b01c362b1423ed2f88930fdd`.
Size: 4,601,947 bytes. Compression is deterministic gzip with mtime zero.

The original derived catalog contained three authored profile components and was
removed from the current tree to comply with AGENTS.md's player-UUID prohibition.
Git history is preserved. Its raw input remains outside ordinary Git at
`evidence/raw/item8/packaged-json-r1.json.gz`, with SHA-256
`c7ea06de3f7cd2dedaead5c6f9ac9021ebe4d03deb007bc15dc712ddfe28a5a2`.
The replacement explicitly records this input identity and every omitted field
path. Archive and member hashes still identify original packaged bytes, not
redacted document serialization. Redacted fields cannot support content claims.

Reproduce from the repository root with the acquired frozen inputs available:

```sh
uv run -m tools.extract_item8_sources --output evidence/raw/item8/packaged-json-reproduction.json.gz
uv run -m tools.redact_item8_catalog --input evidence/raw/item8/packaged-json-reproduction.json.gz --output evidence/raw/item8/packaged-json-redacted-reproduction.json.gz
cmp evidence/item-8/sources/packaged-json-redacted.json.gz evidence/raw/item8/packaged-json-redacted-reproduction.json.gz
```

Each record preserves archive ownership, exact ZIP member path, uncompressed
member hash and size, decoded document, and parsing method. Competing definitions
are separate records. Standalone JSON comment removal is disclosed. Invalid JSON
has a null document, explicit parse error, and original text. It must not be used
as a valid definition.

The initial pilot rejected the empty CTOV member
`data/ctov/tags/worldgen/process_list/village/beach/house_natures_spirit.json`.
The extractor now preserves this failure as a source record rather than aborting
the entire catalog. Its empty original content, identity, and diagnostic remain
in the committed catalog. The initial local traceback is retained at
`evidence/raw/item8/packaged-json-pilot1.log`; it is not an acceptance artifact.
The subsequent pilot and committed-source extraction were byte-identical.

`structure-inputs.json` binds all runtime structure IDs to candidate definitions
and packaged placement sets in the redacted catalog. Reproduce it with
`uv run -m tools.build_item8_structure_inputs --output evidence/raw/item8/structure-inputs-reproduction.json`.
It preserves competing and unregistered definitions and identifies same-provider
definitions differing only in expansion size. These size relationships do not
establish the final canonical family count or prove effective placement.

Remaining work: distinguish actual resource kinds, resolve runtime availability
and competing definitions, decode template evidence, bind accepted Item 7 world
observations, and establish source-supported canonical family relationships and
all required attributes. No Item 9 classification is included here.
