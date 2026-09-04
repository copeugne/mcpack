# Item 7 final candidate validation

Validated revision: `e462dee7b6d37b096b9f22dc7a683e46f28c508e`

Verdict: `PASS`

Repository worktree checks:

- `uv run pytest -q tests/item7`: 173 passed.
- `uv run pytest -q`: 854 passed.
- The restriction audit inspected 762 structures, recorded five impossible restrictions, and reproduced `evidence/item-7/biome-restriction-audit.json` byte for byte.
- The completion builder returned `PASS` and reproduced `evidence/item-7/completion.json` byte for byte with 124 exact artifact identities.

Clean Git export checks:

- Export: `/tmp/mcpack-item7-clean-e462dee.ETt7XS`, created from `git archive e462dee7b6d37b096b9f22dc7a683e46f28c508e`.
- `uv run pytest -q tests/item7`: 173 passed.
- Ruff formatting: 98 Item 7 Python files already formatted.
- Ruff checks: passed.
- basedpyright: 0 errors, 0 warnings, 0 notes.
- Item 7 shell syntax: passed.
- The tracked restriction-audit command ran from the clean export against the declared, uncommitted binary inputs and reproduced the committed JSON byte for byte.
- The tracked completion command ran from the clean export against the preserved raw root and reproduced the committed receipt byte for byte.

This validation is not an independent review approval. PR `#15` still requires a fresh completed GitHub Codex review at the pushed corrected SHA, with no valid unresolved findings, before merge.
