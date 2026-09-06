# BCLib nested MixinExtras entry

Extractor 3e73201d9141c6a6901efa94c7ded6388e464bba. Independent r1 reproduction
matches the disassembly and identity manifest. Manifest SHA-256:
0a86d854b1de84af1cbffd2c9e1dd4ff1a47a9ff01197773667b9fdae2a1490a

```sh
uv run -m tools.inspect_item8_pool_elements --archive bclib-21.0.24.jar --nested-archive META-INF/jarjar/mixinextras-neoforge-0.5.0.jar --class-name com/llamalad7/mixinextras/platform/neoforge/MixinExtrasConfigPlugin.class --output evidence/raw/item8/bclib-mixinextras-entry-r1
```

The manifest declares GAMELIBRARY and the initialization mixin configuration.
That configuration declares this plugin and no mixins. The plugin initializes
MixinExtrasBootstrap, returns no extra mixins or refmap, and has empty target,
pre-apply and post-apply callbacks. The full nested payload is 503 classes plus
its manifest, configuration, license and annotation-processor service. It has
no Minecraft class references or packaged generation data. This is shared
injection infrastructure, not an independent generated family. No generic
injection implementation audit is required for family membership.

A read-only reconnaissance command incorrectly requested nonexistent nested
neoforge.mods.toml and raised KeyError. The actual manifest identifies this as
a game library; no missing metadata was fabricated or silently assumed.
