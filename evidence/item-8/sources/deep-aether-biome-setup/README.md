# Deep Aether biome setup delegates

Extractor ced7bc21bb20af0bdbe123a04b1bada8ae772d18. Manifest SHA-256: d0c5ae38827b28d5db0048c2f5da5603e116a8c070991d1ab198b610af2a126f. Independent r1 matches every generated file.

These three classes are the direct region/surface delegates from the captured common setup. This closes that concrete source boundary using the existing extractor; do not expand into unrelated terrain measurements.

```sh
uv run -m tools.inspect_item8_pool_elements --archive deep_aether-1.21.1-1.1.5.1.jar --class-name io/github/razordevs/deep_aether/world/biomes/DARegion.class --class-name io/github/razordevs/deep_aether/world/biomes/DARareRegion.class --class-name io/github/razordevs/deep_aether/world/biomes/DASurfaceData.class --output evidence/raw/item8/deep-aether-biome-setup-r1
```
