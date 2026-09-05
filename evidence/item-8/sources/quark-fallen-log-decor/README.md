# Fallen-log decoration eligibility

Captured at `5a17e9a`; archive, class and output hashes are in identities.json.
Reproduction matched byte for byte:

```sh
uv run -m tools.inspect_item8_pool_elements --archive Quark-4.1-480.jar --class-name 'org/violetmoon/quark/content/world/gen/FallenLogGenerator$Decor.class' --output evidence/raw/item8/quark-fallen-log-decor-5a17e9a
```

Decor.get reads the placement biome's modified climate settings. It clamps
temperature and downfall separately to [0,1], then multiplies the clamped
values. Fern is eligible when temperature is below 0.3; moss carpet when the
product is above 0.5; vine when it is above 0.75. These are strict comparisons.
The enum order is moss carpet, vine, fern, matching the captured generator's
ordinal switch. These choices are decorations, not separate families.

Effective biome climate modifications remain a separate input. This capture
adds the missing direct decoration-selection logic; it does not prove actual
placement or require another runtime measurement.
