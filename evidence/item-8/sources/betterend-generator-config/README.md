# BetterEnd generator key binding

Selector 13f1e49 captures GeneratorConfig. Independent r1 output reproduces byte
for byte. Manifest SHA-256:
ecf9389b2ff32e43bfedd76f5039971e8b4de987b0022373470f61a3b372334e.

```sh
uv run -m tools.inspect_item8_pool_elements --archive BetterEnd-21.0.31.jar --class-name org/betterx/betterend/config/GeneratorConfig.class --output evidence/raw/item8/betterend-generator-config-r1
```

The constructor binds the following keys to the fields copied by the previously
captured GeneratorOptions.init. Frozen config path:
evidence/item-6/frozen/config/betterend/generator.json, SHA-256
6f1156606391286f22eda4f84a1101fa9059ca1efdd1b2be49d7ab29a37ffa75.

| Frozen key | GeneratorConfig field | Frozen value |
| --- | --- | --- |
| structure.generate_central_island | generateCentralIsland | true |
| structure.generate_obsidian_platform | generateObsidianPlatform | true |
| structure.has_portal | hasPortal | true |
| structure.replace_portal | replacePortal | true |
| structure.has_pillars | hasPillars | true |
| structure.replace_pillars | replacePillars | true |
| structure.end_city_fail_chance | endCityFailChance | 1 |
| generator.use_new_generator | newGenerator | true |
| entity.has_dragon_fights | hasDragonFights | true |
| entity.spawn.has_spawn | changeSpawn | false |

In particular changeSpawn binds has_spawn, not a guessed change_spawn key.
With these values, BetterEnd's platform helper returns without cancelling or
relocating the existing platform. Its portal and pillar replacement conditions
are enabled. The End-city hook's nextInt(1) branch cannot suppress a generation
stub. These are derivations of this provider's code under frozen values, not
proof of the final behavior after other providers' mixins or world overrides.
Keep those interactions in their existing rows; do not add a new measurement.
