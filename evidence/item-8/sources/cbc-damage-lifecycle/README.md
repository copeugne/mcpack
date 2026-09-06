# Big Cannons damage lifecycle

Extractor ffdb4ac1640878eedb6077a6b22f3a6281bd4a2d. Independent r1 reproduction matches the
disassembly and identity manifest. Manifest SHA-256:
fc3bb447345adec09fbd181d9c43b2490d69e17931a464c80545ad5ad0d3e0dc

```sh
uv run -m tools.inspect_item8_pool_elements --archive createbigcannons-5.11.6+mc.1.21.1.jar --class-name rbasamoyai/createbigcannons/base/PartialBlockDamageManager.class --output evidence/item-8/sources/cbc-damage-lifecycle
```

Direct world-load and tick delegate from CBCCommonEvents, for membership inspection.
No persistence, cannon balance or gameplay correctness acceptance is implied.
