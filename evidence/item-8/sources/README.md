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
and competing definitions, resolve template relationships, bind accepted Item 7 world
observations, and establish source-supported canonical family relationships and
all required attributes. No Item 9 classification is included here.

## Template observations

`templates-redacted.json.gz` contains 12,550 packaged template observations from
all 138 source archives. SHA-256:
`b4a2ed8ff0d16ff06c224119f623f248e75e9c8c838fbf2455bf37936c6d3705`.
Size: 6,211,961 bytes. The extraction implementation is `4cb8ce5`; redaction uses
`bdeb98a`. The completed original pilot is retained outside Git as
`evidence/raw/item8/templates-pilot1.json.gz`, SHA-256
`9ffec196748525b0dc115a57e8141a67755e6c9d66ce056fbca667d8cb8ff3c0`.
It must not be published without redaction.

Reproduce using fresh output names:

```sh
uv run -m tools.extract_item8_sources --kind template --output evidence/raw/item8/templates-reproduction.json.gz
uv run -m tools.redact_item8_catalog --input evidence/raw/item8/templates-reproduction.json.gz --output evidence/raw/item8/templates-redacted-reproduction.json.gz
cmp evidence/item-8/sources/templates-redacted.json.gz evidence/raw/item8/templates-redacted-reproduction.json.gz
```

Each template records XYZ size, data version, palettes, block-state counts,
block entity NBT and authored entities. Original archive/member hashes remain
available for exact recovery. Profile, owner, UUID and password fields are
explicitly omitted with their JSON-pointer paths recorded. These omitted fields
cannot prove ownership behavior or credential validity. The catalog retains
spawner configurations, loot references, jigsaw connectors, block positions for
block entities and authored-entity positions. It does not retain ordinary block
positions or constitute a visual render, generated-world observation, or assembled
structure footprint. Resolve pool membership, processors, effective resources
and actual generated bounds before attributing template contents to a family.

## Pack metadata

`pack-metadata.json.gz` preserves root and nested `pack.mcmeta` documents from the
same verified archive set. SHA-256:
`a0ff3cb2c9d363810752acca0948402ce24b7587bb0a1c430d08820857bbf426`.
Reproduce with:

```sh
uv run -m tools.extract_item8_sources --kind metadata --output evidence/raw/item8/pack-metadata-reproduction.json.gz
cmp evidence/item-8/sources/pack-metadata.json.gz evidence/raw/item8/pack-metadata-reproduction.json.gz
```

Lithostitched's metadata declares its `overlay.breaks_seed_parity` overlay under
the NeoForge condition `lithostitched:breaks_seed_parity`. The frozen
`evidence/item-6/frozen/config/lithostitched.json` sets `breaks_seed_parity` to
true. The runtime context is preserved in
`evidence/item-8/runtime/registry-r1/world-context.json`. These inputs support
resolving the competing packaged resources; the inventory must still distinguish
selected resources, unselected alternatives, and unresolved conditions.

## Potential pool relationships

`pool-traces.json.gz` records direct start-pool walks for 818 registered structure
IDs and explicitly lists the other 69 IDs for custom generation inspection.
SHA-256: `d09325da6389180f95f6687f8479374b35b54a8cea81badca6d9540734abe920`.
Size: 157,886 bytes. Implementation: `f9fb51f`, using the selected-resource
rules in `b135beb` and tracing implementation in `9fae9cf`.

```sh
uv run -m tools.trace_item8_structure_pools --output evidence/raw/item8/pool-traces-reproduction.json.gz
cmp evidence/item-8/sources/pool-traces.json.gz evidence/raw/item8/pool-traces-reproduction.json.gz
```

The committed-source run reproduced the successful pilot byte for byte. An
earlier attempt stopped before writing output because the frozen Lithostitched
configuration contains comments. The tool now reads the already inspected
setting from that exact hash-verified configuration.

This is a partial relationship result, not the final inventory. Missing pools
and templates remain explicit. Pool aliases are retained in each structure's
context but are not resolved by this walk. Inline features and processor-list
references remain terminal edges. Potential fallback and jigsaw paths are not
proof of assembly feasibility, generated contents, probabilities, or footprint.
Optional-pack exclusions remain unresolved where activation has not been proved.
Custom generation, dynamic injection, processors, aliases and generated-world
observations still need to be incorporated before assigning family attributes.

## Generated-world piece bounds

`world-bounds.json.gz` retains 792 saved structure starts from the eight Item 7
`run-a` and `run-b` decoded streams across all four frozen seeds. SHA-256:
`fd8ebda1d1778b51c312cb98734248ce8c8ead623b201d79943df05ff36f169b`.
Size: 474,504 bytes. Extraction source: `bf623f1`; envelope calculation and direct
tests: `472a1f7`. The committed-source extraction reproduced its pilot byte for
byte. Every decoded input is checked against its size and hash in the committed
Item 7 r14 core archive manifest before reading observations.

After restoring the Item 7 r14 core archive using its existing delivery records:

```sh
uv run -m tools.extract_item8_world_bounds --core <restored-core-directory> --output evidence/raw/item8/world-bounds-reproduction.json.gz
cmp evidence/item-8/sources/world-bounds.json.gz evidence/raw/item8/world-bounds-reproduction.json.gz
```

Rows retain source file and line, run, seed, dimension, chunk coordinates,
chunk generation status, structure and start IDs, and every decoded piece box.
The envelope uses the minimum and maximum coordinates across those boxes;
XYZ sizes include both endpoint blocks. Empty boxes remain null, and reversed
boxes fail extraction. Repeated runs remain separate observations.

These are saved piece envelopes, not occupied-block volume, generation frequency,
or proof that every piece has finished placement. The start chunk's full status
does not establish that all intersecting chunks are full. Structures absent from
these bounded worlds still need other evidence. Do not interpret sample extrema
as global size limits or these observations as exploration pacing.
