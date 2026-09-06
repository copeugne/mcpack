# Patchouli provider entry points

Extractor 0d52fb06. Six entry/service/common-hook classes. Independent r1
reproduction matches source and manifest bytes. Manifest SHA-256:
556bb66d051e4a453adb76d4a8d84b073b9bf0c90564274d1948870ec9762041

```sh
uv run -m tools.inspect_item8_pool_elements --archive Patchouli-1.21.1-93-NEOFORGE.jar --class-name vazkii/patchouli/mixin/AccessorSmithingTransformRecipe.class --class-name vazkii/patchouli/mixin/AccessorSmithingTrimRecipe.class --class-name vazkii/patchouli/neoforge/client/NeoForgeClientInitializer.class --class-name vazkii/patchouli/neoforge/client/NeoForgeClientXplatImpl.class --class-name vazkii/patchouli/neoforge/common/NeoForgeModInitializer.class --class-name vazkii/patchouli/neoforge/xplat/NeoForgeXplatImpl.class --output evidence/raw/item8/patchouli-provider-r1
```

Registration supplies book items, sounds, item data and advancement triggers.
Common hooks expose smithing recipe ingredients. Services provide book events,
client rendering and platform lookup. Book initialization and multiblock roles
remain to be reconciled before membership closure.
