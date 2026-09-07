# Quark selected End-generation registrations

Extractor revision: `d554c8d9002a1d13b3b84e5065e4e9b455cc654a`.
Exact identities are in identities.json. Fresh reproduction matched exactly
before this README was added; scoped extractor Ruff/Basedpyright passed.

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive Quark-4.1-480.jar \
  --class-name org/violetmoon/quark/content/world/module/ChorusVegetationModule.class \
  --class-name org/violetmoon/quark/content/world/module/SpiralSpiresModule.class \
  --output evidence/raw/item8/quark-end-registration-d554c8d-reproduction
diff -r --exclude=README.md evidence/item-8/sources/quark-end-registration \
  evidence/raw/item8/quark-end-registration-d554c8d-reproduction
```

ChorusVegetationModule.setup registers ChorusVegetationGenerator through
WorldGenHandler.addGenerator at VEGETAL_DECORATION with weight zero.
SpiralSpiresModule.setup registers SpiralSpireGenerator with its dimensions
configuration at SURFACE_STRUCTURES with weight zero. These are direct consumer
registrations, not independent registered structure roots or accepted families.
Generator implementations and effective configuration binding remain to be
resolved before assigning applicability or generated contents. Unrelated block
interaction methods in the full module capture are not acceptance claims here.
