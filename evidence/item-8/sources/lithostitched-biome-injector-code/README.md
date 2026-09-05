# Dimension-biome source boundary

Item 8 requires dimension attribution for every family. This inspection uses
the existing extractor to establish what the saved biome-source representation
can and cannot prove. It does not add a runtime measurement system.

Extractor extension: `87b3bd7`. Source archive SHA-256:
`d367ea1885486755dd8a162b8bb28404a35155e9fd34eba03108991363b6c70a`.
Identities manifest SHA-256:
`b48129fffa046624fb15e6381edb678001d491c4be8ddcd03e2c5ec440f8afaa`.

```sh
uv run -m tools.inspect_item8_pool_elements --archive lithostitched-1.7.10+beta4-neoforge-21.1.jar --class-name dev/worldgen/lithostitched/impl/worldgen/biomeinjector/internal/InjectorBiomeSource.class --class-name dev/worldgen/lithostitched/impl/worldgen/biomeinjector/internal/BiomeInjectorManager.class --class-name dev/worldgen/lithostitched/api/worldgen/biomeinjector/BiomeInjector.class --output evidence/item-8/sources/lithostitched-biome-injector-code
uv run ruff check tools/inspect_item8_pool_elements.py
uv run basedpyright tools/inspect_item8_pool_elements.py
```

Extraction and scoped checks passed. Use a fresh output directory to reproduce.
The three disassemblies are an isolated source evidence increment, not game
binaries. The extractor verifies archive identity and records member/output hashes.

## Findings

`InjectorBiomeSource.collectPossibleBiomes` concatenates the direct delegate's
possible biomes with those accumulated from injectors, then filters biomes in
the replaced-biomes list. `lambda$applyInjectors$0` adds each injector's possible
biomes and collects ReplaceFully targets into that exclusion list. The codec's
single serialized field is `delegate`; its decoder uses Function.identity.
Consequently a saved injector wrapper does not serialize these accumulated
runtime lists and must not be treated as their complete enumeration.

`BiomeInjectorManager.applyBiomeInjectors` selects registry injectors by dimension,
then invokes AddBiomeInjectorsEvent. Event entries are admitted only for the
matching dimension and when their ID is not already present. An empty injector
map or a generator outside NoiseBasedChunkGenerator skips this path. The manager
also loads dimension-matching regions and invokes AddRegionsEvent. It checks
CANNOT_INJECT_INTO, applies the injectors, installs the wrapper and refreshes
the generator's feature-step supplier. This establishes an event-supplied input
path in addition to packaged registry resources.

The saved `runtime/registry-r1/world-context.json` is already retained and bound
by SHA-256 `0615a2dcdeb2120a467648df95f69aa9f1ef53e8989ae8c2191028d6f5c1aca2`.
Its Overworld and Nether generators contain injector wrappers. Inspect their
full biome-source objects rather than deriving eligibility from a delegate's
preset name. The End uses a separate Wover biome-source path, outside these
three classes. This inspection does not resolve the full effective biome set
of any dimension, nor does possible-biome membership alone prove a structure
will successfully generate.

## Continuation boundary

Check the existing runtime export before writing collection code. The adjacent
`../neoforge-dump-command-code` inspection establishes the existing registry
command's key-only output. Resolving effective biome-source membership must also
account for other retained providers and their runtime transformations. A new
collector, if required, must directly close this shared Item 8 gap and reuse
the frozen materialization/lifecycle path. Do not build a second worldgen harness
or emulate every generator to recover information available from runtime objects.
No family dimension eligibility is promoted by this source milestone.
