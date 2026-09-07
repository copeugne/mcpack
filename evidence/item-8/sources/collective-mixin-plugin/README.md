# Collective Mixin Plugin

Extractor b7e053eb. Independent r1 reproduction matches source and manifest
bytes. Manifest SHA-256:
17633f917be4a00d30225d1efbb2f7b7a2e7ccd5237e3db2e1a5d4fa623b3e14

```sh
uv run -m tools.inspect_item8_pool_elements --archive collective-1.21.1-8.25.jar --class-name com/natamus/collective/neoforge/mixin/plugin/NeoForgeMixinConfigPlugin.class --output evidence/raw/item8/collective-mixin-plugin-r1
```

The plugin filters declared hooks by loader and bundle eligibility. getMixins
returns null; load/target/pre/post callbacks are empty. It adds no extra hooks.
Collective whole-provider disposition remains open. Reuse this capture there;
do not treat closure of this shared hook boundary as whole-library closure.
