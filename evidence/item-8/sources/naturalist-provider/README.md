# Naturalist provider mechanisms

Extractor cebed2eaef5ddf5104d657816b7c38cd231e42a3. Manifest SHA-256:
2b5d4824d4dfcbd499f73366a72e001e098f794e26eb20bffa58b4e375932f2d.
Independent r1 matches every generated file.

Retains the main entry and callbacks, all seven common mixins, and the custom
biome-modifier registration and implementation. The modifier adds mob spawn
entries; the common hooks affect existing entities/items/crops. Packaged data
and complete archive accounting accompany provider acceptance. No observed
spawn abundance or gameplay compatibility claim is made by this capture.

```sh
uv run -m tools.inspect_item8_pool_elements --archive naturalist-1.0.2-neoforge-1.21.1.jar --class-name com/starfish_studios/naturalist/Naturalist.class --class-name com/starfish_studios/naturalist/mixin/BottleItemMixin.class --class-name com/starfish_studios/naturalist/mixin/CreeperMixin.class --class-name com/starfish_studios/naturalist/mixin/CropBlockMixin.class --class-name com/starfish_studios/naturalist/mixin/MapItemMixin.class --class-name com/starfish_studios/naturalist/mixin/MobMixin.class --class-name com/starfish_studios/naturalist/mixin/MonsterMixin.class --class-name com/starfish_studios/naturalist/mixin/ZombieMixin.class --class-name com/starfish_studios/naturalist/registry/NaturalistBiomeModifiers.class --class-name com/starfish_studios/naturalist/server/level/modifiers/AddAnimalsBiomeModifier.class --output evidence/raw/item8/naturalist-provider-r1
```
