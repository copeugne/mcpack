# Nether house and forge comparison

Renderer 0926552a selects ten templates from the hash-verified retained
MoogsNetherStructures-1.21-3.0.0-alpha.2.jar archive. Both sheets were manually
inspected and independently reproduce byte for byte.

```sh
uv run -m tools.view_item8_betterend_ruins --nether-houses --output evidence/raw/item8/nether-house-views-r1
```

The medium and large houses and forge are shown together; all six warped-house
alternatives are shown on the second sheet. Existing pool data identifies the
warped templates as equal-weight alternatives, not connected components.
The existing cube projection rescales each template independently and omits
fully occluded cells. It does not render actual partial block models, hidden
interiors, assembled world placement or measured dimensions. Join the views to
the packaged contents and selected pool traces. The ten-path pilot succeeded;
scoped Ruff and Basedpyright pass. No rendering behavior was added.

Compressed SHA-256 identities:

- house_comparison.svg.gz: 9c6b16aaceb9d5c81f7a313c729bf633402c15db409dbf2bf438bfd3e7eac667
- warped_houses.svg.gz: 1b373c79cb3d91ea811a15a4a3b530a84466694b35564ef7c38b1ffbd2c737df
