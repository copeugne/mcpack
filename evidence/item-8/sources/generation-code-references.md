# Whole-stack generation code reference inventory

Extractor revision: d475f15. Output: generation-code-references.json.gz.
SHA-256: 95b9991457704f4cf710b09456a82db78c2dcdd79544212c77d8f31d64c8883f.
The capture and a second extraction compare byte for byte.

```sh
uv run -m tools.extract_item8_sources --kind code --output evidence/raw/item8/generation-code-references-r1.json.gz
cmp evidence/item-8/sources/generation-code-references.json.gz evidence/raw/item8/generation-code-references-r1.json.gz
uv run pytest -q tests/item8/test_sources.py
```

All 136 retained candidates plus the two platform inputs are hash-verified before
inspection. Nested archives are traversed using the existing source collector.
Each matching class retains its archive location, class path, class hash and
matched reference terms. The exact terms are in item8_sources.py. This supports
a whole-stack review queue alongside the existing packaged JSON, templates,
runtime registry and family decisions. It does not turn class matches into
families, prove runtime activation, or prove semantic absence from zero matches.
Libraries, datagen, commands, client code and construction tools can match.

The existing collector tests, including a new nested code-only archive case,
pass (seven tests). Scoped Ruff and Basedpyright pass. Initial static checks
identified two overlong lines and a JsonValue list-variance annotation issue;
these were corrected before the successful checks. No runtime experiment.

The broad pass exposes candidate paths needing explicit reconciliation, rather
than continuing one provider's helper implementation indefinitely:

- BetterEnd: BuildingListFeature, CrashedShipFeature and NBTFeature, plus their
  registration and templates. Establish whether already represented by roots.
- Biomes O' Plenty: anomaly, monolith and bone-spine configured features, and
  other terrain/vegetation boundary candidates. Four packaged definitions use
  three named types because nether_bone_spine reuses bone_spine. Definitions are
  not yet accepted family assignments.
- Deep Aether: TotemFeature and deep_aether:totem configured feature.
- Explorations: ScarecrowFeature, separate from its structure-registry roots.
- Supplementaries: road-sign feature/structure relationship and mineshaft
  elevator component. Avoid counting both implementations as separate families.
- Village additions: Farmer's Delight, Chef's Delight, Village Taverns,
  Regions Unexplored and retained compatibility data require consumer assignment.

These are review candidates located in preserved sources, not a claim that all
remaining candidates have already been semantically resolved. Complete the
manifest-wide reconciliation before resuming individual attribute tracing.
