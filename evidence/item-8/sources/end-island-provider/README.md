# Better End Island remaining entry hooks

Extractor 15c9a65 retains nine previously uncaptured entry classes. The independent
r1 reproduction matches every generated file. Existing template, generator,
configuration and activation captures are reused, not regenerated.

Manifest SHA-256: 0db009720863b6d44792a50e2f39f0adc418cc90a11e486c9d28343235cb9be2.

```sh
uv run -m tools.inspect_item8_pool_elements --archive YungsBetterEndIsland-1.21.1-NeoForge-3.1.2.jar --class-name com/yungnickyoung/minecraft/betterendisland/command/EndIslandCommand.class --class-name com/yungnickyoung/minecraft/betterendisland/mixin/EndergeticExpansionMixins.class --class-name com/yungnickyoung/minecraft/betterendisland/mixin/PrimaryLevelDataMixin.class --class-name com/yungnickyoung/minecraft/betterendisland/mixin/ServerLevelMixin.class --class-name com/yungnickyoung/minecraft/betterendisland/mixin/TheEndGatewayBlockEntityMixin.class --class-name com/yungnickyoung/minecraft/betterendisland/mixin/accessor/EndDragonFightAccessor.class --class-name com/yungnickyoung/minecraft/betterendisland/module/CommandModule.class --class-name com/yungnickyoung/minecraft/betterendisland/module/StructureProcessorTypeModule.class --class-name com/yungnickyoung/minecraft/betterendisland/services/IModulesLoader.class --output evidence/raw/item8/end-island-provider-r1
```

The reset command requires permission level two and delegates to the existing
End dragon fight reset. CommandModule registers that command. The processor
module exposes the three already captured component processors. IModulesLoader's
default body is empty.

PrimaryLevelDataMixin serializes extra dragon-fight state. ServerLevelMixin
attaches that state, saves it and triggers the existing initial dragon summon
from its tick hook. EndergeticExpansionMixins conditionally replaces the existing
dragon-fight object for compatibility. These are existing-arena lifecycle paths.
EndDragonFightAccessor exposes existing fight fields and dragon creation.
TheEndGatewayBlockEntityMixin changes landing-position searches and reads the
packaged cannot-place-player-on tag. It does not place a new design.

This source capture supports bounded provider reconciliation. It does not prove
successful runtime behavior, final canonical grouping or complete Item 8 attributes.
