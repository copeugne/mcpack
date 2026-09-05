# Deep Aether totem scope

Captured with f92c2d3 and reproduced byte for byte. Manifest SHA-256:
a4a20f4109769622d01ebc02d5324d2ff55b6cc10aefde39e15132e377a3865d.

```sh
uv run -m tools.inspect_item8_pool_elements --archive deep_aether-1.21.1-1.1.5.1.jar --class-name io/github/razordevs/deep_aether/world/feature/features/TotemFeature.class --output evidence/raw/item8/deep-aether-totem-scope-r1
```

The packaged deep_aether:totem configured feature uses deep_aether:totem type
and occurs in the live configured-feature registry. The captured TotemFeature
attempts a vertical stack, selecting two or three iterations and one horizontal
facing. Direct block choices are MOA_TOTEM, ZEPHYR_TOTEM and AERWHALE_TOTEM.
The call uses getRandomTotem(random, false), so its optional SKYROOT_LOG branch
is not the direct generation choice. Placement can skip writes; iteration count
is not a guarantee of generated height.

This is one authored totem design candidate with block/height/facing variants,
not one family per block or iteration. The method does not construct a separate
house or dungeon. Its feature registration binding and placed-feature/biome
use still need reconciliation before final inventory acceptance. Do not inspect
unrelated block economics to establish this family boundary.
