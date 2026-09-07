# Underground fill dispatch and family disposition

Captured at extractor revision 343647b. identities.json binds the retained
archive, class and disassembly. Capture and identity reproduced byte for byte
before this README was added:

```sh
uv run -m tools.inspect_item8_pool_elements --archive Quark-4.1-480.jar --class-name org/violetmoon/quark/content/world/undergroundstyle/base/UndergroundStyle.class --output evidence/raw/item8/quark-underground-fill-343647b
```

fill first rejects blocks with destroy speed -1. It then dispatches to exactly
one operation in priority order: floor, ceiling, wall, inside. Floor and ceiling
require the current block to render solid and be replaceable or tagged
quark:underground_biome_replaceable; the block above or below respectively must
be empty or replaceable. Walls use the same current-block predicate plus a
horizontal border check. Inside means membership in that replacement tag.
The dispatcher does not carve an empty volume or place templates.

Combined with the captured implementations, Corundum decorates existing
floor/ceiling surfaces with crystals and changes qualifying walls to stone;
its inherited fillInside does nothing because mimicInside is false. Its AIR
floor constructor argument does not imply cave carving: Corundum overrides
fillFloor without invoking the base floor writer. Permafrost replaces selected
floor/ceiling material, walls and qualifying interior terrain and may add short
pillars above existing floors. Its mimicInside is true. These paths contain no
authored entity, spawner or container-loot operation.

Working Item 8 disposition: account for both as underground terrain-decoration
contributions, with no additional canonical structure family from these style
operations. The reason is their existing-surface/material behavior, not their
procedural implementation or absence from the structure registry. Crystal colors
and short repeated pillars are decoration variants, not independent families.
This does not establish complete Quark coverage, exact runtime tag/configuration
membership, total affected area or observed world occurrence. The shared cluster
enumerator is not claimed exhaustively inspected by this record.

No further fill-dispatch capture is needed for these two style dispositions.
Retain their source links in provider coverage and continue other generators.
Scoped extractor Ruff and Basedpyright checks passed. No new measurement system
or server run was added.
