# Aether holiday eligibility filter

Extractor cf93f3b captures HolidayFilter. Independent r1 extraction matches every
file. Manifest SHA-256: 8bd3d11068bb8ad3118257f19db123ecf37961fdfb5625db475b3def34be130b.

```sh
uv run -m tools.inspect_item8_pool_elements --archive aether-1.21.1-1.5.10-neoforge.jar --class-name com/aetherteam/aether/world/placementmodifier/HolidayFilter.class --output evidence/raw/item8/aether-holiday-filter-r1
```

shouldPlace reads Calendar.getInstance().get(Calendar.MONTH), accepting month
11 or 0 for the seasonal branch. The returned condition is always enabled, or
seasonally enabled together with December/January. It uses the JVM calendar,
not Minecraft world time, and does not itself place a tree.

The already bound frozen settings are always=false and seasonally=true. Thus
this filter permits the holiday-tree candidate during December/January, subject
to its other placement conditions. This does not prove an observed tree or
that runtime configuration cannot be changed. Preserve the time-dependent input
for later effective-eligibility and observation interpretation.
