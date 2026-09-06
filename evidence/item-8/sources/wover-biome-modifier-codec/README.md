# Wover biome modifier codec

Frozen worldweaver-21.0.24.jar source for BetterEnd biome modifier coverage.
The complete capture reproduced exactly against the independent r1 directory.
Manifest SHA-256: dfea087f9938a66807e94d9d2f9a46d110e82dae07092fde2777780979299cbf.

```sh
uv run -m tools.inspect_item8_pool_elements --archive worldweaver-21.0.24.jar --class-name org/betterx/wover/biome/api/modification/BiomeModification.class --output evidence/raw/item8/wover-biome-modifier-codec-r1
```

The codec binds predicate, features, biome_tags and spawns. Consumers apply
matching modifiers to existing biome generation settings and tags on server
readiness. The six selected predicate implementations match the operators used
by BetterEnd defaults.json and eternal_portals.json. FeatureMap resolves
placed-feature holders and GenerationSettingsWorker adds them by decoration
step; this is not an independent authored generator. BiomeTagModificationWorker
updates existing tag contents and reports failure if its accessor is unavailable.

Use with the companion wover-biome-modifier-consumers capture.
The consumer capture uses selector 0e58d71; the additional codec binding uses
ff36c78. No duplicate world experiment or new measurement system. Detailed
BetterEnd candidate dispositions and runtime limitations are in provider-scope.md.
