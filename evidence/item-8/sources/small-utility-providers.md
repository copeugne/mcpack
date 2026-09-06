# Small utility provider source capture

Selector revision: 39ef785. Pinned javap extracts every class from each of these
six exact retained archives. This is an isolated generated-source increment;
69 class disassemblies preserve annotations, hook targets and callback bindings.
No binaries or runtime changes are included. Each capture was independently
repeated and compared byte for byte before acceptance.

## AI Improvements

Archive: `AI-Improvements-1.21-0.5.3.jar`. SHA-256: `795618769ff1ac782750be9e8faaf3e3d212f1687c3baab98c1282a98a63a41e`.
All 20 classes captured. Identity manifest SHA-256:
`15b2c2a5826ddbfea4b8befab50ba609ac1ec17de1540a169fac968c08b06bbd`.

```sh
uv run -m tools.inspect_item8_pool_elements --archive 'AI-Improvements-1.21-0.5.3.jar' --output evidence/raw/item8/ai-improvements-provider-r1
diff -qr evidence/item-8/sources/ai-improvements-provider evidence/raw/item8/ai-improvements-provider-r1
```

## AttributeFix

Archive: `attributefix-neoforge-1.21.1-21.1.3.jar`. SHA-256: `b2b20f3d44e824071284c14de3f4d3323d420e1c450040b339a5c37d2c382ad4`.
All 5 classes captured. Identity manifest SHA-256:
`6b5f5497616109f88376d894557a498edcf9b97bccb58e8e639702dca1d9206b`.

```sh
uv run -m tools.inspect_item8_pool_elements --archive 'attributefix-neoforge-1.21.1-21.1.3.jar' --output evidence/raw/item8/attributefix-provider-r1
diff -qr evidence/item-8/sources/attributefix-provider evidence/raw/item8/attributefix-provider-r1
```

## Leaves Be Gone

Archive: `LeavesBeGone-v21.1.1-1.21.1-NeoForge.jar`. SHA-256: `ea85ad07672f7c2199c28fe58a80c354ef2f2c60bfb0315e3730c344068526e0`.
All 12 classes captured. Identity manifest SHA-256:
`19cc43de2ea86c8bc0f3f6212f49903de293517fe1d78ddef0c805e3f0584af4`.

```sh
uv run -m tools.inspect_item8_pool_elements --archive 'LeavesBeGone-v21.1.1-1.21.1-NeoForge.jar' --output evidence/raw/item8/leavesbegone-provider-r1
diff -qr evidence/item-8/sources/leavesbegone-provider evidence/raw/item8/leavesbegone-provider-r1
```

## Let Me Despawn

Archive: `letmedespawn-1.21.x-neoforge-1.5.0.jar`. SHA-256: `074ffdbe34bf97b7d15fa4db7cfff547578a9c2f547479128a43d184c4ca642a`.
All 6 classes captured. Identity manifest SHA-256:
`57020da079e8b92682e1bf9e6b7328b281a034c4c543966bd8c2e126d96a90bc`.

```sh
uv run -m tools.inspect_item8_pool_elements --archive 'letmedespawn-1.21.x-neoforge-1.5.0.jar' --output evidence/raw/item8/letmedespawn-provider-r1
diff -qr evidence/item-8/sources/letmedespawn-provider evidence/raw/item8/letmedespawn-provider-r1
```

## Sparse Structures

Archive: `sparsestructures-neoforge-1.21.1-3.0.jar`. SHA-256: `5aca0b33c0c83154810bbdd8ddc0d3e6a3e4591577274e2d27c10de0b45f2a45`.
All 14 classes captured. Identity manifest SHA-256:
`33d153974364c484e57da384dc44729b0d61cb3628dc529f4020f62e97337c54`.

```sh
uv run -m tools.inspect_item8_pool_elements --archive 'sparsestructures-neoforge-1.21.1-3.0.jar' --output evidence/raw/item8/sparsestructures-provider-r1
diff -qr evidence/item-8/sources/sparsestructures-provider evidence/raw/item8/sparsestructures-provider-r1
```

## Structure Pool API

Archive: `structure_pool_api-neoforge-1.2.1+1.21.1.jar`. SHA-256: `c18460025b07bc05fdc95bf62621c6b56f45e4eeb1c319f12787f39eb9315ea9`.
All 12 classes captured. Identity manifest SHA-256:
`0c401d9a9c6234c9dceb36d6d5e108c1eb0daf90c7d6dc0c4fa8fbddc6837538`.

```sh
uv run -m tools.inspect_item8_pool_elements --archive 'structure_pool_api-neoforge-1.2.1+1.21.1.jar' --output evidence/raw/item8/structure-pool-api-provider-r1
diff -qr evidence/item-8/sources/structure-pool-api-provider evidence/raw/item8/structure-pool-api-provider-r1
```

## Inspected candidate boundaries

- AI Improvements: Mod constructor registers common configuration. Common setup
  initializes FastTrig and ModifierSystem. The entity-join subscriber dispatches
  configured goal removals and look-control replacement on existing entities.
  Editor/filter classes operate on goals and entity predicates. FastTrig and
  FixedLookControl implement orientation calculations. Its access transformer
  exposes goal/look-control fields and nested goal types. No generation entry.
- AttributeFix: the mod-bus load-complete subscriber calls AttributeFixMod.init,
  iterates the attribute registry and applies configured RangedAttribute bounds.
  Its sole nonempty mixin declaration is the min/max accessor. Constants and
  RangeConfig supply IDs, configuration and bound updates. No generation entry.
- Leaves Be Gone: the entry/config holder and client setup supply configuration
  integration. Four common mixins handle leaf distance, scheduled random leaf
  ticks and their chunk serialization/container lifecycle. Two ticker interfaces
  expose those queues. The NeoForge mixin list and access transformer are empty.
  This affects existing leaves, including player-triggered decay, not a family.
- Let Me Despawn: initialization loads/saves configuration through Almanac. The
  Mob mixin changes equipment-related persistence and the discard path, calling
  Almanac's equipment-drop helper. Commands edit configured mob names and items.
  Access declarations expose persistenceRequired. It contributes no generation
  path. Effects on authored enemies remain relevant to later family attributes;
  no combat or persistence behavior is inferred merely from provider closure.
- Sparse Structures: initialization loads the JSON5 configuration; its service
  implementation supplies platform/config-directory information. The registry
  loader mixin modifies placement JSON for existing structure sets before codec
  parsing, excludes concentric-ring placement, and applies configured spread and
  optional ID-based salt. The other mixins raise the spread codec bound and alter
  locate-distance arithmetic. The command dumps encountered set IDs. Configuration
  holders and the set collector do not create roots or components. Effective
  placement remains bound to the frozen configuration in existing Item 8 inputs.
- Structure Pool API: empty common init, NeoForge server-start listener processes
  caller-supplied pending injections. The API adds caller-named templates to
  existing pools and remembers element IDs/optional limits. Its accessor and
  two behavioral mixins expose pool elements, retain their IDs and enforce
  caller-supplied piece limits during jigsaw assembly. It packages no components
  or independent family. Village Taverns' already inspected fallback consumer
  remains conditional on Lithostitched absence; do not count it a second time.

These are provider-role findings. Canonical family reconciliation, other retained
providers and effective whole-stack attributes remain separate work. No assumption
that zero keyword hits proves absence is used. The full archive closure check
must bind these captures and account for every non-class file before these rows
are marked resolved. A metadata inspection probe initially matched a class path
containing /services/ and failed UTF-8 decoding; the corrected inspection used
META-INF/services/ only. No partial probe output supports an acceptance claim.

Git's whitespace check reports the original extra EOF blank line in javap's
StructurePoolAPI$SpawnPerk output. It is retained verbatim and reproduces exactly;
normalizing it would change the preserved raw capture.
