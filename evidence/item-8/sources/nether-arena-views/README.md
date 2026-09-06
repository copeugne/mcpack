# Nether arena architecture comparison

Renderer 973b531d selects 30 architectural templates from the hash-verified
retained MoogsNetherStructures-1.21-3.0.0-alpha.2.jar archive. Shared mob templates
remain in the existing source graph. All four sheets were manually inspected;
independent outputs match byte for byte. The selected-path pilot succeeded.

```sh
uv run -m tools.view_item8_betterend_ruins --nether-arenas --output evidence/raw/item8/nether-arena-views-r1
```

These are individual pieces, not reconstructed whole arenas. Existing pool traces
remain authoritative for their connections and version selection. The existing
cube projection omits occluded cells and rescales each piece separately; partial
models, hidden interiors and generated-world placement are not rendered. Large
lower-platform diagrams can approach adjacent labels or sheet edges, so use their
SVG names and pool identities, not screen scale, for attribution. The views are
sufficient for this architectural comparison and are not dimension measurements.
Scoped Ruff and Basedpyright pass. No new rendering behavior was introduced.

Compressed SHA-256 identities:

- dragon_lower.svg.gz: 273fb1b70b5b1a2259f17e05ace8a416309df5af99f160261d99dab2adff3ea2
- dragon_upper.svg.gz: 5ceb4d72e6b81a44ef63520b2be16bfcc82135d29887b47667a049a241d31f70
- large_arena.svg.gz: 9e277febf077a9222d81df9053a7425753253cbd1338e96131aaf082858cfa8f
- small_arena.svg.gz: 0ffc2a583a818a18922afe962c48750078099acb11fefff42b84f48a44fe5dc5
