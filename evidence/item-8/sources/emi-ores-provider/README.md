# EMI Ores contribution sources

Extractor 6869c159. Eighteen classes cover the two entries, empty common
initializer, platform path helper, feature sender and thirteen common accessors.
This isolated generated capture retains the exact source for the membership
disposition. Independent r1 reproduction matches all source and manifest bytes.
Manifest SHA-256: 30f6cd1c8f2dfcb1a705504c399490876639fe7c6df5c1f9cfc54f338fc22442

```sh
uv run -m tools.inspect_item8_pool_elements --archive emi_ores-1.2+1.21.1+neoforge.jar --class-name cc/abbie/emi_ores/EmiOres.class --class-name cc/abbie/emi_ores/mixin/accessor/BlockMatchTestAccessor.class --class-name cc/abbie/emi_ores/mixin/accessor/BlockStateMatchTestAccessor.class --class-name cc/abbie/emi_ores/mixin/accessor/CountPlacementAccessor.class --class-name cc/abbie/emi_ores/mixin/accessor/HeightRangePlacementAccessor.class --class-name cc/abbie/emi_ores/mixin/accessor/NoiseProviderAccessor.class --class-name cc/abbie/emi_ores/mixin/accessor/RandomBlockMatchTestAccessor.class --class-name cc/abbie/emi_ores/mixin/accessor/RandomBlockStateMatchTestAccessor.class --class-name cc/abbie/emi_ores/mixin/accessor/RarityFilterAccessor.class --class-name cc/abbie/emi_ores/mixin/accessor/SimpleStateProviderAccessor.class --class-name cc/abbie/emi_ores/mixin/accessor/TagMatchTestAccessor.class --class-name cc/abbie/emi_ores/mixin/accessor/TrapezoidHeightAccessor.class --class-name cc/abbie/emi_ores/mixin/accessor/UniformHeightAccessor.class --class-name cc/abbie/emi_ores/mixin/accessor/WeightedStateProviderAccessor.class --class-name cc/abbie/emi_ores/neoforge/EmiOresNeoForge.class --class-name cc/abbie/emi_ores/neoforge/PlatformImpl.class --class-name cc/abbie/emi_ores/neoforge/client/EmiOresNeoForgeClient.class --class-name cc/abbie/emi_ores/networking/FeaturesSender.class --output evidence/raw/item8/emi-ores-provider-r1
```

Datapack synchronization reads existing biome/placed-feature registries and
sends filtered ore/geode information to clients. Temporary PlacedFeature
objects enter the outgoing map, not the runtime registry or placement path.
All common mixins are getters for existing generation parameters. No site
generation or independent family is defined by these entry paths.
