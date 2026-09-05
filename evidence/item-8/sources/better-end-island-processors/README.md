# Better End Island content processors

Manifest SHA-256: `dfeb5a2586c4b82b3e0e6eb5712149d1ab8adfc6689cc7ece108490a2b7d9b95`.
Retained archive SHA-256: `8005f1ea798d09fc05dad07a21ed1f393a523a718197cdbd37b1ce6d9a17e4a4`.

DragonEggProcessor preserves a dragon egg already present at a target world
position; its name does not mean that it creates an egg reward at an empty site.
ObsidianProcessor substitutes crying obsidian for incoming obsidian based on
a threshold interpolated from zero to 0.5 using dragon kills clamped to 0..10.
Both preserve target position and incoming NBT. Other block states pass through.
These are direct processor rules, not observations of actual reward or block counts.

Reproduce with extractor revision `e839306` and a fresh output directory:

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive YungsBetterEndIsland-1.21.1-NeoForge-3.1.2.jar \
  --class-name com/yungnickyoung/minecraft/betterendisland/world/processor/ObsidianProcessor.class \
  --class-name com/yungnickyoung/minecraft/betterendisland/world/processor/DragonEggProcessor.class \
  --output evidence/raw/item8/better-end-island-processors-reproduction
```

Before adding this README, recursive comparison with fresh reproduction matched
every file byte-for-byte. Scoped extractor Ruff/Basedpyright passed.
