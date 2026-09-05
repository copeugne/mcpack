# Village Taverns entry and mixin scope

Extractor revision d8d1107. Identity manifest SHA-256:
06bcc5f00e19ecf856680ccc3174706a4ba0988957a5005d40511833479d1b45.
The five selected classes reproduced byte for byte before this README was added.

```sh
uv run -m tools.inspect_item8_pool_elements --archive village_taverns-neoforge-1.1.5+1.21.1.jar --output evidence/raw/item8/tavern-provider-entries-r1
```

NeoForgeMod calls TavernsMod.init and registers callbacks for blocks, points of
interest and villager professions. Its POI registration callback catches an
Exception without reporting it; preserve that limitation rather than inferring
successful profession functionality from startup.

TavernsMod.init refreshes village configuration and calls StructurePoolAPI.injectAll
only if the loader reports lithostitched absent. It then saves the configuration.
The packaged Lithostitched additions and this fallback injection are alternative
routes, not evidence of two independent tavern contributions. The retained stack
includes Lithostitched; exact loader/config attribution must remain attached to
the provider's final scope disposition rather than assumed from names alone.

PotionsMixin targets the tail of Potions static initialization. It conditionally
initializes spell_power and ranged_weapon_api compatibility, catching Throwable
around each initialization. VillagerMixin wraps Brain.setSchedule inside
Villager.registerBrainGoals, substituting the always-work schedule for the
bartender profession and preserving the supplied schedule for other professions.
Neither inspected mixin places a structure or independently injects a pool.

This is a source checkpoint, not full-provider closure. Continue the existing
registration helpers, configuration defaults and bundled tiny-config entry
mechanisms as needed for full archive accounting. Reuse the five recorded tavern
component relationships; do not repeat template content or add trade economics.
