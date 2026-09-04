# Item 7 rejected GitHub Codex review

Reviewed revision: `eed044337bed03dcd8893d369cef9e6b5e6fd483`

Pull request: `https://github.com/copeugne/mcpack/pull/15`

Verdict: `REJECTED`

The completed GitHub Codex review reported two P1 findings. Both were technically valid and blocked merge:

1. The core raw-evidence staging boundary rejected only lowercase `.jar` files and `session.lock`. It could admit other forbidden Minecraft binaries, credentials, player data, caches, or instance state. Source: `https://github.com/copeugne/mcpack/pull/15#discussion_r3933530043`.
2. `SPECS.md` marked impossible biome restrictions complete while the Item 7 report said that inspection remained unresolved until Item 8. Source: `https://github.com/copeugne/mcpack/pull/15#discussion_r3933530051`.

Disposition:

- Six parameterized RED cases proved that the staging boundary accepted an `instances/` path, an uppercase `.JAR`, a `.class` file, a credential token path, player data, and cache state. Commit `b857f01da0d82d0131f005ef734f16b47c3677a0` replaces the incomplete predicate with the exact core-root and evidence-suffix allowlist plus explicit forbidden-component and secret-name rejection. The focused staging suite then passed all 17 tests.
- Commit `1de9b4b2b4283f41bf44ad8e538534a7b92b60f7` adds a tracked, hash-bound packaged-data audit and binds it into the completion validator. The audit command is:

  `uv run python tools/audit_item7_biome_restrictions.py --repository . --provider-catalog evidence/item-7/provider-catalog.json --output evidence/item-7/biome-restriction-audit.json`

- The deterministic audit inspected 762 structures from the exact 37 Item 7 provider components plus frozen Minecraft and NeoForge data. It resolved 757 restrictions and recorded five impossible restrictions. Two empty tags belong to unplaced definitions. Three active IDAS lumber-camp variants reference missing compatibility biome tags through `idas:idas_small`; they remain explicit findings for Item 8.
- A second run wrote byte-identical audit output. The focused staging, restriction, and completion suites passed 23 tests. The complete Item 7 suite passed 173 tests, and the full repository suite passed 854 tests. Ruff formatting, Ruff checks, and basedpyright passed on the changed Python surface.
- The completion receipt now binds `biome-restriction-audit.json` as its 124th exact artifact. The Item 7 report, execution ledger, and handoffs state the same counts and findings.

This rejected review is not approval. The corrected candidate requires a fresh completed GitHub Codex review at its exact pushed SHA before merge.
