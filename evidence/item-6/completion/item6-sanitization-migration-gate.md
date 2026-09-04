# Item 6 sanitization identity migration gate

Commit under test: uncommitted indivisible phase-C migration on `codex/item-6-completion`

## RED proof

- Scenario: the committed manifest must declare the v2 canonical sanitization identity.
- Invocation: `uv run pytest -q tests/item6/test_sanitization_wiring.py`
- Binary observable: manifest schema is v2 and contains canonical receipt metadata.
- Result before migration: `1 failed`, because the manifest remained v1. Captured in `item6-sanitization-migration-red.txt`.

## GREEN identity and attack coverage

- Scenario: a copied Item 6 repository validates a v2 manifest and rejects receipt-path redirection, traversal, digest and count mutations, missing or unknown metadata fields, stale receipt bytes, missing receipt, and symlinked receipt.
- Invocation: `uv run pytest -q tests/item6/test_sanitization_wiring.py tests/item6/test_sanitization_receipt.py tests/item6/test_manifest_contract.py`
- Binary observable: valid evidence returns successfully; every adversarial variant raises a validation error.
- Result: `48 passed`.

## Frozen-tree and secret invariants

- Scenario: compare SHA-256 inventories before and after migration for every frozen file except `config/resourceful-config-web.json`.
- Invocation: `find evidence/item-6/frozen -type f ! -path 'evidence/item-6/frozen/config/resourceful-config-web.json' -print0 | sort -z | xargs -0 sha256sum`, compared before and after with `cmp --silent`.
- Binary observable: exactly 227 unaffected rows are byte-identical.
- Result: passed, `unaffected_frozen_rows_before=227`, `unaffected_frozen_rows_after=227`.
- Scenario: read the pre-migration credential only in process memory, scan tracked and untracked current working-tree files without emitting the value, and inspect the current JSON pointer.
- Invocation: a local `uv run python -c` verifier over `git show HEAD:evidence/item-6/frozen/config/resourceful-config-web.json` and `git ls-files -co --exclude-standard -z`.
- Binary observable: sentinel at `/validator/if/password` and zero current working-tree occurrences of the prior value.
- Result: passed, `credential_pointer_contains_sentinel=true`, `credential_occurrences_current_working_tree=0`, `files_scanned=606`.

## Regression and static checks

- Invocation: `uv run pytest -q tests/item6`
- Binary observable: exit code 0.
- Result: `414 passed`.
- Invocation: `uv run pytest -q`
- Binary observable: exit code 0.
- Result: `541 passed`.
- Invocation: changed-file Ruff format/check and basedpyright.
- Binary observable: exit code 0 and `0 errors, 0 warnings`.
- Result: passed.
- Invocation: `uv run tools/freeze_item6_config.py validate --root evidence/item-6/frozen --manifest evidence/item-6/generated-config-manifest.json --audit evidence/item-6/config-audit.json`
- Binary observable: exact output `validated Item 6 frozen configuration and audit` and exit code 0.
- Result: passed.
- Invocation: `git diff --check`
- Binary observable: exit code 0.
- Result: passed.

This migration is intentionally indivisible: the frozen target, canonical receipt, manifest v2 row and metadata, audit identity, and top-level binding must agree in the same commit for validation to remain meaningful.
