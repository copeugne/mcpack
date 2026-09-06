# GeckoLib initialization delegates

Extractor 1ba861e7. Both disassemblies and manifest reproduce byte for byte
in the independent r1 capture. Manifest SHA-256:
4ef7f6553e9311199ba73bee38146ce63fd967657c98e3b33215b79411168237

```sh
uv run -m tools.inspect_item8_pool_elements --archive geckolib-neoforge-1.21.1-4.8.4.jar --class-name software/bernie/geckolib/GeckoLibConstants.class --class-name software/bernie/geckolib/service/GeckoLibNetworking.class --output evidence/raw/item8/geckolib-init-r1
```

Constants initialization registers only the persistent/synchronized item
animation ID data component. Networking initialization registers fifteen
client-bound animation data, trigger, stop and stateless-animation packets.
This resolves the outstanding startup registration boundary; no generated
site is registered. No further packet serialization audit is needed here.
