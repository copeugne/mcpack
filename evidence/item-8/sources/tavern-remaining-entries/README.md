# Remaining Tavern class scope

Extractor revision 1f8119a. Manifest SHA-256:
d17cdb8b2a04d87ed1483d00f6cc3aa5902bceebdbaaadcf5de5eb8565215e8f.
All seven captures reproduced byte for byte before this README was added.

```sh
uv run -m tools.inspect_item8_pool_elements --archive village_taverns-neoforge-1.1.5+1.21.1.jar --class-name 'net/village_taverns/block/BrewTapBlock$1.class' --class-name net/village_taverns/block/BrewTapBlock.class --class-name net/village_taverns/client/TavernsModClient.class --class-name net/village_taverns/compat/RangedWeaponCompat.class --class-name net/village_taverns/compat/SpellPowerCompat.class --class-name net/village_taverns/neoforge/client/NeoForgeClientMod.class --class-name architectury_inject_village_taverns_common_9feb1bb9f94a4fa08c0c87b571be378b_a8fac20701f86f005801059a650cef1ec65724e970fe2c13ffa0269f8465b11bvillage_tavernscommon1151211devjar/PlatformMethods.class --output evidence/raw/item8/tavern-remaining-entries-r1
```

The client setup delegates to an empty init. BrewTapBlock defines block shape,
facing, placement-state transformation and tooltip behavior; its companion is
the generated direction-switch table. It has no feature registration, template
placement or block tick that creates a separate structure. The platform helper
returns the target name. Compatibility classes configure potion-related data
used by the already inspected conditional Potions mixin, not generation roots.

Together with tavern-provider-entries and tavern-registration-scope, these cover
all fifteen top-level classes. Bundled Tiny Config entry evidence is preserved
separately. Next: full archive accounting and the existing component links, then
close this provider disposition without further block or trade investigation.
