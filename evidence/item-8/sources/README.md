# Packaged JSON source catalog

This is source evidence, not a canonical family inventory or an Item 8 gate pass.
The extractor scans every hash-verified retained candidate plus the pinned
Minecraft and NeoForge archives. Nested JARs and optional data-pack paths remain
explicit. Their presence does not prove runtime activation or resource priority.
All packaged data JSON is retained so nonstandard provider injection resources
remain inspectable. Recipes and other unrelated resources are not families.

Source implementation: `d042ed172e7750d13efa4b2302b45ced37281247`.
Output: `packaged-json.json.gz`.
SHA-256: `c7ea06de3f7cd2dedaead5c6f9ac9021ebe4d03deb007bc15dc712ddfe28a5a2`.
Size: 4,592,633 bytes. Compression is deterministic gzip with mtime zero.

Reproduce from the repository root with the acquired frozen inputs available:

```sh
uv run -m tools.extract_item8_sources --output evidence/raw/item8/packaged-json-reproduction.json.gz
cmp evidence/item-8/sources/packaged-json.json.gz evidence/raw/item8/packaged-json-reproduction.json.gz
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

Remaining work: distinguish actual resource kinds, resolve runtime availability
and competing definitions, decode template evidence, bind accepted Item 7 world
observations, and establish source-supported canonical family relationships and
all required attributes. No Item 9 classification is included here.
