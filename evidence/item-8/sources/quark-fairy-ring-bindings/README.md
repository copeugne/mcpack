# Fairy Ring configuration and callback binding

The existing ordinary module capture omitted annotations. The same extractor now
requests verbose output for this one class so its binding is directly inspectable.
Original ordinary source remains in quark-landmark-encounter-generators and is
reproducible using that record's extractor revision. Exact new archive, class and
disassembly identities are in identities.json.

```sh
uv run -m tools.inspect_item8_pool_elements --archive Quark-4.1-480.jar --class-name org/violetmoon/quark/content/world/module/FairyRingsModule.class --output evidence/raw/item8/quark-fairy-ring-bindings-reproduction
```

ZetaLoadModule specifies only category world. Config annotates forestChance,
plainsChance and dimensions; oresRaw explicitly names Ores. Both setup and
configChanged have LoadEvent annotations. The latter clears ores and resolves
each configured string through BuiltInRegistries.BLOCK, adding non-air states.
Invalid air entries print an exception. Frozen inputs and static defaults agree
on emerald_ore and diamond_ore, forest chance 0.00625, plains chance 0.0025 and
an Overworld allowlist. These chances are configured inputs, not observed rates.

Registry-r1 debug line 13845 names Fairy Rings. Reuse zeta-module-section for
section naming and loaded/frozen file identity, zeta-config-event-fields for
annotated nested fields and the initial-refresh event, and quark-world-category
for category/module enablement ordering. The category and Fairy Rings toggles
are true, and the module annotation adds no overlap or required-mod restriction.
This follows the same source/configuration/log derivation already accepted for
Monster Box; it does not introduce another field-dump or runtime measurement.

The existing log SHA-256 is e5b47378d791027242ba28dd36c999c07ae4e01a1b90e1534e66bcd42c1e694b.
The frozen/captured configuration SHA-256 is 94bfff490eea33f9bb105fae298606c4708ddb8af2f3df8630cc0f0ac7e85327.
The derived dimension and ore-source attributes are integrated in the Fairy Ring
record. No actual ore-list dump or successful generated ring is asserted.
Delegated flower-feature effects remain the one specific unanswered question.
