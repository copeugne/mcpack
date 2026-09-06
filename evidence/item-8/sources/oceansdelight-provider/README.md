# Ocean's Delight provider source

Selector revision: 75232ba. All 15 classes in the exact retained archive
`oceansdelight-neoforge-1.0.4-1.21.1.jar` are captured. Archive SHA-256:
`30fec2263f77bcd4002995d9fc127a911c964317dbd0e3c54e348954d1722d38`.
Identity manifest SHA-256:
`db7a1ce1a12229d00abefb1eacf24bb3b5a28f824e6b86746855e1c943458c48`.
The independent repeated extraction matches byte for byte.

```sh
uv run -m tools.inspect_item8_pool_elements --archive oceansdelight-neoforge-1.0.4-1.21.1.jar --output evidence/raw/item8/oceansdelight-provider-r1
```

Compare identities.json and every listed disassembly against this directory;
the README is explanatory text added after comparison, not raw tool output.

The sole mod entry calls Registration.init and installs client setup. Registration
registers blocks, items and a creative tab. GuardianSoupBlock specializes food
block shape; food/item definitions and render-layer setup do not generate terrain.
The only auto-subscriber is DataGenerators on the mod bus. GatherDataEvent installs
recipe, block-state, language, block-tag and item-model data providers. These are
build-time data generators, not structure-generation entry points. No other code,
mixin, service, nested archive or runtime data-loader hook is present.

Packaged data includes four Farmer's Delight add-item loot modifiers for squid,
glow squid, guardian and elder guardian, with a NeoForge global modifier list.
These are loot-source contributions for existing mobs, not authored families.
The three cut modifiers require an attacking entity holding a knife. guardian_drop
has the guardian entity condition only. Effective combined loot behavior remains
subject to shared modifier implementation and whole-stack resource selection.
Recipes, recipe-unlock advancements and diet/block tags add no structure route.
Five packaged .cache files are build data-generation cache manifests, not active
resources. Preserve their archive identity without publishing machine-local raw
cache content. No baseline or family-decision file changed.
