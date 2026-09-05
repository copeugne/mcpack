# Better End Island exit portal invocation

Manifest SHA-256: `c33781ceaf0c25c60be92da62653f8fe73afbdc83b6248066bedd7ad2b61dcbd`.
Archive SHA-256: `8005f1ea798d09fc05dad07a21ed1f393a523a718197cdbd37b1ce6d9a17e4a4`.

ExitPortalUtils is the direct helper used by the captured EndDragonFightMixin
for podium placement. The full class preserves overload argument ordering,
configuration selection, origin adjustment and placement/state-update limits.

Reproduce with extractor revision `f74d4f4` and a fresh output directory:

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive YungsBetterEndIsland-1.21.1-NeoForge-3.1.2.jar \
  --class-name com/yungnickyoung/minecraft/betterendisland/world/util/ExitPortalUtils.class \
  --output evidence/raw/item8/better-end-island-exit-portal-reproduction
```

Recursive comparison before adding this README matched the fresh reproduction
exactly. Generated mixin metadata is identical to the authoritative copy in
better-end-island-platform-gateway and is not committed again. Scoped extractor
Ruff/Basedpyright passed. No runtime observation or new measurement is claimed.
