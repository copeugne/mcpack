# quark spawner replacement

Extractor 1ee9b51 captures 1 selected classes. Independent r1
extraction matches every generated file byte for byte.
Manifest SHA-256: f98c7135cebbc6868cc86ddb249f99cfff8eca8a3bbb7d802c5c8ff61434bb7e.

```sh
uv run -m tools.inspect_item8_pool_elements --archive Quark-4.1-480.jar --class-name org/violetmoon/quark/content/experimental/module/SpawnerReplacerModule.class --output evidence/raw/item8/quark-spawner-replacement-r1
```

SpawnerReplacerModule.configChanged assigns staticEnabled from isEnabled.
spawnerUpdate returns immediately when staticEnabled is false or on the client.
When enabled on the server, it maps an existing spawner display entity type to
its configured replacement, then updates that existing spawner. It does not
create a new structure layout. The static replacement map starts empty.

Frozen evidence/item-6/frozen/config/quark-common.toml sets
experimental."Spawner Replacer" = false. Reuse the existing Zeta configuration
binding and initial refresh evidence; the hook declaration alone is not active
replacement evidence. This resolves the specific callback identified in
quark-provider-entries without a new runtime experiment.
