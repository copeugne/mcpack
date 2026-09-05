# Slime Cave processor attribution

Captured at extractor revision 7400ef3 and reproduced byte for byte before
this README was added:

```sh
uv run -m tools.inspect_item8_pool_elements --archive explorations-neoforge-1.21.1-1.6.2.jar --class-name com/tristankechlo/explorations/worldgen/structures/processors/DeepslateProcessor.class --output evidence/raw/item8/explorations-deepslate-7400ef3
```

DeepslateProcessor replaces only stone with deepslate and mossy cobblestone
with tuff, only when the transformed block position has Y below zero. It keeps
that position and uses the replacement default state with null NBT. Unmapped
blocks and positions at or above zero return unchanged. Thus Slime Cave's
structure-block markers and chest, including their metadata/loot reference,
are preserved by this processor. It adds no entities, spawners or loot tables
and does not change the template envelope. This resolves the direct processor
gap recorded in explorations-slime-cave; it is not proof of observed placement
or of all cross-provider runtime hooks. Scoped extractor static checks passed.
