# Better Combat weapon resource boundary

Extractor a835af39. Independent r1 reproduction matches all source and manifest
bytes. Manifest SHA-256:
b6b66cb55ed1fc68c07a3370a6e2d4bbd56a83b5d61befc8279d91a0d7a52645

```sh
uv run -m tools.inspect_item8_pool_elements --archive bettercombat-neoforge-2.3.2+1.21.1.jar --class-name net/bettercombat/logic/WeaponRegistry.class --class-name net/bettercombat/compat/CompatFeatures.class --output evidence/raw/item8/better-combat-resources-r1
```

WeaponRegistry loads weapon_attributes resource objects into attribute maps and
encodes them for synchronization. It does not register worldgen content.
CompatFeatures delegates to FTBTeamsCompat.init; capture that final dependency
before closing membership. No generic attribute parsing or network audit needed.
