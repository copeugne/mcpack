# Cloth Config provider entry point

Extractor ce673ed3. Independent r1 reproduction matches source and manifest
bytes. Manifest SHA-256:
9315320632f2c0a1dfefe98525b2b6c25fe90d1949a63579421be3ad5bd281df

```sh
uv run -m tools.inspect_item8_pool_elements --archive cloth-config-15.0.140-neoforge.jar --class-name me/shedaniel/clothconfig/ClothConfigForge.class --output evidence/raw/item8/cloth-config-provider-r1
```

The sole automatic entry calls registerModsPage only when Dist.isClient is
true. Dedicated-server initialization returns without registration. There are
no mixins or services. Access transformation exposes three client GUI members.
No independent generated family; no further UI helper inspection is needed.
