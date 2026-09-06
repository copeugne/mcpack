# Simply Swords content delegates

Extractor 2f9fbd4090cd80ff5ddf0454b46d656c5dea8c8d. Independent r1 reproduction matches all
disassemblies and the identity manifest. Manifest SHA-256:
fff0b8605559f05fb254ebed2018fc99eae5ea6575ed138584260234779d5017

```sh
uv run -m tools.inspect_item8_pool_elements --archive simplyswords-neoforge-1.63.0-1.21.1.jar --class-name net/sweenus/simplyswords/util/ModLootTableModifiers.class --class-name net/sweenus/simplyswords/registry/GemPowerRegistry.class --class-name net/sweenus/simplyswords/registry/TransformationRegistry.class --class-name net/sweenus/simplyswords/item/ContainedRemnantItem.class --output evidence/item-8/sources/simplyswords-content-delegates
```

Loot, gem/transformation registration and remnant interaction boundaries.
