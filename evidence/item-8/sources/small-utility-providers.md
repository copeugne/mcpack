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

## Additional shared boundaries, selector 4f65e40

The following isolated generated increment captures 38 classes from three more
retained providers. Each repeated capture matches byte for byte. It resolves
candidate boundaries, not the correctness or performance of their algorithms.

### Almanac

Archive `Almanac-1.21.1-2-neoforge-1.5.2.jar`, SHA-256 `379893246c33aaa6dd8e4a8711e349cd6835e08c2bd5b8bd7b7e81be9822aacb`.
All 13 classes captured. Identity manifest SHA-256 `846bc2adbd79f5625a83d1fd71ea8be43843b42b3ce16e7b001035f0c9fe6bb1`.

```sh
uv run -m tools.inspect_item8_pool_elements --archive 'Almanac-1.21.1-2-neoforge-1.5.2.jar' --output evidence/raw/item8/almanac-provider-r1
diff -qr evidence/item-8/sources/almanac-provider evidence/raw/item8/almanac-provider-r1
```

### Library Ferret

Archive `libraryferret-neoforge-1.21.1-4.0.0.jar`, SHA-256 `fcc7cbe7ec7d2e5bce6a9d24c14d94bc27a577c293311077476e5f43937be1a2`.
All 9 classes captured. Identity manifest SHA-256 `818982bd379cd4f31dc2ece2b16bd22cdbc1332cac40de8a56c87f34b4b60e65`.

```sh
uv run -m tools.inspect_item8_pool_elements --archive 'libraryferret-neoforge-1.21.1-4.0.0.jar' --output evidence/raw/item8/libraryferret-provider-r1
diff -qr evidence/item-8/sources/libraryferret-provider evidence/raw/item8/libraryferret-provider-r1
```

### Structure Layout Optimizer

Archive `structure_layout_optimizer-neoforge-1.0.12.jar`, SHA-256 `ef8eb29c5c4f111c74a49d379843e4c2f51d11b28c8116a49be13636c83f4385`.
All 16 classes captured. Identity manifest SHA-256 `3a24a425f1eae35abdb77547922cedf22f9212c09a69043b4f6baf95b1e5d197`.

```sh
uv run -m tools.inspect_item8_pool_elements --archive 'structure_layout_optimizer-neoforge-1.0.12.jar' --output evidence/raw/item8/structure-layout-optimizer-provider-r1
diff -qr evidence/item-8/sources/structure-layout-optimizer-provider evidence/raw/item8/structure-layout-optimizer-provider-r1
```

Almanac's entry registers common configuration and initializes configuration and
command support. Its config subscriber's load/reload bodies make no changes.
CommandsMixin dispatches registered command callbacks; EntityMixin handles the
picked-item marker; ItemStackMixin and SlotMixin invoke empty custom-data cleanup.
ItemNBTUtil applies configured item exclusions and caches. ReloadCommand manages
configuration, and the platform helper reads the NeoForge configuration. The
public equipment-drop helper operates on existing entities and is already linked
to Let Me Despawn. No template, root, feature or direct structure-generation path.

Library Ferret's entry registers coin items, an optional creative tab and a common
setup callback that queues an empty body. Configuration/Props and Color support
settings and presentation. AwesomeStructure and AwesomePlacementRndSpread are
abstract consumer-facing bases, with no packaged concrete subclass. The former
passes constructor-supplied pools and dimensions to vanilla JigsawPlacement after
its abstract canGenerate predicate. The latter supplies random-spread and
exclusion-zone behavior with abstract configuration bindings. The nested exclusion
record checks other supplied structure sets; AwesomeStructureConfiguration holds
consumer-specified enable/spacing/separation/salt settings. The public registration
helper registers the caller-supplied placement type. None supplies an independent
authored layout. Non-code content is coin recipes and visual assets, not generation
resources. Existing Better Village coverage is reused, not rerun or reclassified.

Structure Layout Optimizer's entry initializes Resourceful Config. Its five
mixins replace jigsaw collision/connection checks, filter shuffled candidates and
rotations, change jigsaw shuffle/prioritization, and filter template blocks by
placement bounds, with one pool accessor. Helpers manipulate existing bounding
boxes, candidate lists, rotations and palette contents. PlatformService resolves
the NeoForge finalization method name for processor inspection. No helper creates
an independent root or hard-coded authored layout, and there is no packaged data
pack or template. Preserve its modifying role for existing jigsaw families; this
inspection does not establish equivalent layouts, better performance, or safety
of enabling/disabling its configuration. No configuration or algorithm is changed.

## Bundle and shield boundaries, selector 49dd5dd

This isolated source increment captures all 30 classes from the two following
archives. Both independent extractions reproduce byte for byte. Standard javap
is used for ordinary classes; verbose output preserves the entry, mixin and EMI
plugin annotations. A display-only probe initially expected verbose braces in
ordinary output and failed; the corrected display handles both retained formats.
The raw captures and reproduction comparison were unaffected.

### bundle-api

Archive `bundle-api-neoforge-1.1.0.jar`, SHA-256 `73328888d1dede4c121974a0914f5a35cb857283223217a59de7b5b697e43771`.
All 19 classes captured. Identity manifest SHA-256 `761564dccceb00a1ee3e781dd8380987076f885d8d14d011d03e172522d0f59a`.

```sh
uv run -m tools.inspect_item8_pool_elements --archive 'bundle-api-neoforge-1.1.0.jar' --output evidence/raw/item8/bundle-api-provider-r1
diff -qr evidence/item-8/sources/bundle-api-provider evidence/raw/item8/bundle-api-provider-r1
```

### shield-api

Archive `shield_api-neoforge-2.2.0.jar`, SHA-256 `adbd8facfcaf318956d670ff3f0341c0d8e15e136ae9c00749a255e25a9c0194`.
All 11 classes captured. Identity manifest SHA-256 `d713942af83a5e1f30c824e2cef9b04cde23d2024ba46d7955b57ec3d457cd2b`.

```sh
uv run -m tools.inspect_item8_pool_elements --archive 'shield_api-neoforge-2.2.0.jar' --output evidence/raw/item8/shield-api-provider-r1
diff -qr evidence/item-8/sources/shield-api-provider evidence/raw/item8/shield-api-provider-r1
```

Bundle API's mod entry and client subscriber call common/client initializers. Its common
registry mixins register the custom bundle data-component and item predicate;
client mixins register item model predicates and custom tooltip rendering.
Contents records/builders, predicates, the container-component manipulator and
CustomBundleItem operate on existing item stacks, occupancy, inventory interaction
and dropping stored items. They do not construct an authored world layout. The
client class is a client-setup subscriber. No additional entry or packaged
generation data exists.

Shield API's common initializer logs initialization; its client initializer is
empty. Its Minecraft startup mixin registers shield model predicates. CustomShieldItem supplies repair ingredients,
attributes and equip sounds. Player and axe mixins handle custom-shield damage,
cooldown and strip-attempt behavior. The EMI plugin displays anvil repair recipes
for registered shield items. Its client class subscribes to client setup.
The archive declares MinecraftClientMixin in the common mixin list and the model
predicate invoker in the client list; preserve that exact declaration rather than
silently relabeling it. This is not a newly reproduced server failure or a reason
to change the frozen stack. There are no roots, templates, features, pool injections
or independent authored structure families in either provider. Inventory/combat
behavior and consumer loot remain relevant separately from family membership.

## Save and structure utility boundaries

Selector 2498f47 captures all six Fast Async World Save classes and all 26
Structure Essentials classes. Independent captures reproduced exactly.

| Archive | Archive SHA-256 | Capture directory | Identity manifest SHA-256 |
| --- | --- | --- | --- |
| fastasyncworldsave-1.21-2.6.jar | 099316ee212ff44bcd7aea853f0153cd28432e0297676d21f61e8b000089714f | fastasyncworldsave-provider | 4b60ee73ab2950958e58b4d5cede24ab5055d75693f3434ddec4e6438fd5d9a2 |
| structureessentials-1.21.1-5.0.jar | 7ecb6c9d04e20a6803ba6e51dd226eaa289ba2c2c095248f3645222a8bfc1c8d | structureessentials-provider | 2cb92ed499c3a7fa07688426be09e5a59b0939adb21ce7151a102982a203a6a5 |

```sh
uv run -m tools.inspect_item8_pool_elements --archive fastasyncworldsave-1.21-2.6.jar --output evidence/raw/item8/fastasyncworldsave-provider-r1
uv run -m tools.inspect_item8_pool_elements --archive structureessentials-1.21.1-5.0.jar --output evidence/raw/item8/structureessentials-provider-r1
```

Fast Async World Save initializes a single-thread executor. Its two mixins route
saved-data and level-data writes through it; saved-data filenames also receive
platform-specific colon replacement. Client initialization is separate. The
packaged CommonConfiguration describes a sleep/weather option, not a generation
entry; do not infer an active configuration consumer from its presence. No
authored generation resource, template or layout-writing route is supplied.
This disposition does not establish save correctness or measured performance.

Structure Essentials registers configuration and inspection/timing commands.
Its generation hooks operate on existing registry entries, jigsaw inputs,
structure settings, lookup operations and starts. They provide configurable
biome compatibility, spacing/separation, nearby-start exclusion, search limits,
timings, logs and error handling. They supply no independent authored geometry,
root, pool or template. The mixin plugin only rejects LegacyRandomSourceMixin
when disableLegacyRandomCrashes is false; other declared mixins pass its filter.
Its pre/post-apply callbacks do not introduce additional class transformations.

The frozen structureessentials.json (SHA-256
54826c1ce55156e6a3d19a22949d733668806c7ed4a77218cc1d26bb6c5fa7bd)
has automatic biome compatibility and minimum-distance exclusion disabled,
spacingSeparationModifier=1.0, and disableLegacyRandomCrashes=true. Search settings
and error-handling changes remain relevant to interpreting observed lookups.
PlacedFeatureErrorMixin catches placement exceptions and reports warnings;
successful startup or continued generation must not be substituted for successful
placement of every feature. Preserve the existing raw logs and failures. No
runtime experiment, baseline configuration or family grouping was changed here.
